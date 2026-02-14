"""Celery tasks for syncing InfluxDB data into the game database."""

import hashlib
import logging
from datetime import timedelta

from celery import shared_task
from django.core.cache import cache
from django.db import transaction
from django.db.models import Count, Max, Sum
from django.utils import timezone

from apps.achievements.engine import evaluate_all_achievements
from apps.aquarium.models import CaughtBot, CountryStats, DailyStats, FishSpecies, Server
from apps.aquarium.services import calculate_score, classify_fish

from .influx_client import query_bot_connections, query_global_totals, query_trapped_times
from .models import SyncState

logger = logging.getLogger(__name__)


def _hash_ip(ip: str) -> str:
    return hashlib.sha256(ip.encode()).hexdigest()


# ISO 3166-1 alpha-2 country code mapping for InfluxDB country names
_COUNTRY_CODES = {
    "afghanistan": "AF", "albania": "AL", "algeria": "DZ", "andorra": "AD",
    "angola": "AO", "argentina": "AR", "armenia": "AM", "australia": "AU",
    "austria": "AT", "azerbaijan": "AZ", "bahrain": "BH", "bangladesh": "BD",
    "belarus": "BY", "belgium": "BE", "bolivia": "BO", "bosnia and herzegovina": "BA",
    "brazil": "BR", "brunei": "BN", "bulgaria": "BG", "cambodia": "KH",
    "cameroon": "CM", "canada": "CA", "chile": "CL", "china": "CN",
    "colombia": "CO", "costa rica": "CR", "croatia": "HR", "cuba": "CU",
    "cyprus": "CY", "czech republic": "CZ", "czechia": "CZ",
    "denmark": "DK", "ecuador": "EC", "egypt": "EG", "estonia": "EE",
    "ethiopia": "ET", "finland": "FI", "france": "FR", "georgia": "GE",
    "germany": "DE", "ghana": "GH", "greece": "GR", "guadeloupe": "GP",
    "guatemala": "GT", "hong kong": "HK", "hungary": "HU", "iceland": "IS",
    "india": "IN", "indonesia": "ID", "iran": "IR", "iraq": "IQ",
    "ireland": "IE", "israel": "IL", "italy": "IT", "ivory coast": "CI",
    "jamaica": "JM", "japan": "JP", "jordan": "JO", "kazakhstan": "KZ",
    "kenya": "KE", "kuwait": "KW", "kyrgyzstan": "KG", "latvia": "LV",
    "lebanon": "LB", "libya": "LY", "lithuania": "LT", "luxembourg": "LU",
    "macao": "MO", "macau": "MO", "malaysia": "MY", "maldives": "MV",
    "mali": "ML", "malta": "MT", "mexico": "MX", "moldova": "MD",
    "mongolia": "MN", "morocco": "MA", "mozambique": "MZ", "myanmar": "MM",
    "nepal": "NP", "netherlands": "NL", "the netherlands": "NL",
    "new zealand": "NZ", "nicaragua": "NI", "nigeria": "NG", "north korea": "KP",
    "north macedonia": "MK", "norway": "NO", "oman": "OM", "pakistan": "PK",
    "palestine": "PS", "panama": "PA", "paraguay": "PY", "peru": "PE",
    "philippines": "PH", "poland": "PL", "portugal": "PT", "qatar": "QA",
    "romania": "RO", "russia": "RU", "saudi arabia": "SA", "senegal": "SN",
    "serbia": "RS", "seychelles": "SC", "singapore": "SG", "slovakia": "SK",
    "slovenia": "SI", "somalia": "SO", "south africa": "ZA",
    "south korea": "KR", "spain": "ES", "sri lanka": "LK", "sudan": "SD",
    "sweden": "SE", "switzerland": "CH", "syria": "SY", "taiwan": "TW",
    "tajikistan": "TJ", "tanzania": "TZ", "thailand": "TH", "tunisia": "TN",
    "turkey": "TR", "turkmenistan": "TM", "uganda": "UG", "ukraine": "UA",
    "united arab emirates": "AE", "united kingdom": "GB", "united states": "US",
    "uruguay": "UY", "uzbekistan": "UZ", "venezuela": "VE", "vietnam": "VN",
    "yemen": "YE", "zambia": "ZM", "zimbabwe": "ZW",
}


def _country_to_code(name: str) -> str:
    """Convert country name to ISO 3166-1 alpha-2 code."""
    if not name:
        return ""
    return _COUNTRY_CODES.get(name.lower().strip(), name[:2].upper())


@shared_task(bind=True, max_retries=3)
def sync_bot_data(self):
    """Sync bot data from InfluxDB.

    Queries aggregated per unique (host, ip) - not per scrape interval.
    Creates/updates one CaughtBot per unique bot per server.
    Runs every 5 minutes via Celery Beat.
    """
    state, _ = SyncState.objects.get_or_create(
        server_host="global",
        metric_type="client_open",
        defaults={"last_sync_at": timezone.now() - timedelta(hours=24)},
    )
    since = state.last_sync_at.isoformat()

    try:
        connections = query_bot_connections(since)
        if not connections:
            logger.info("No new connections since %s", since)
            return "No new data"

        # Always use wide lookback for trapped times - they are cumulative
        # counters and we need the latest value regardless of sync window.
        trapped_times = query_trapped_times("-30d")
        servers = {s.host_identifier: s for s in Server.objects.filter(is_active=True)}

        created_count = 0
        updated_count = 0

        with transaction.atomic():
            for conn in connections:
                ip = conn["ip"]
                host = conn["host"]
                if not ip or host not in servers:
                    continue

                server = servers[host]
                fingerprint = f"{host}:{ip}"
                trapped_seconds = trapped_times.get(fingerprint, 0)
                species = classify_fish(trapped_seconds)
                score = calculate_score(species, trapped_seconds)
                ip_hash = _hash_ip(ip)
                country = conn.get("country", "") or ""
                country_code = _country_to_code(country)

                shared_fields = {
                    "server": server,
                    "species": species,
                    "ip_address": ip,
                    "ip_hash": ip_hash,
                    "country_code": country_code,
                    "country_name": country,
                    "geohash": conn.get("geohash", "") or "",
                    "local_port": int(conn.get("local_port", 22) or 22),
                    "trapped_seconds": trapped_seconds,
                    "connection_count": int(conn.get("open_count", 1)),
                    "last_seen": conn["time"],
                    "score": score,
                }
                obj, created = CaughtBot.objects.update_or_create(
                    influx_fingerprint=fingerprint,
                    create_defaults={
                        **shared_fields,
                        "first_seen": conn["time"],
                    },
                    defaults=shared_fields,
                )
                if created:
                    created_count += 1
                else:
                    updated_count += 1

            state.last_sync_at = timezone.now()
            state.records_synced += created_count
            state.last_error = ""
            state.save()

        # Invalidate cached stats so next request gets fresh data
        cache.delete_many(["endlessh:game_stats", "endlessh:ticker_catches"])

        # Evaluate daily challenges right after sync so progress is current
        if created_count > 0 or updated_count > 0:
            try:
                from apps.aquarium.challenge_service import evaluate_daily_challenges
                evaluate_daily_challenges()
            except Exception:
                logger.debug("Challenge evaluation after sync failed", exc_info=True)

        logger.info(
            "Sync complete: %d new, %d updated from %d connections",
            created_count, updated_count, len(connections),
        )
        return f"{created_count} new, {updated_count} updated"

    except Exception as exc:
        state.last_error = str(exc)
        state.save()
        logger.exception("Sync failed")
        raise self.retry(exc=exc, countdown=60)


@shared_task
def aggregate_daily_stats():
    """Aggregate daily statistics per server. Runs every hour."""
    today = timezone.localtime().date()

    for server in Server.objects.filter(is_active=True):
        today_catches = CaughtBot.objects.filter(
            server=server, first_seen__date=today
        )
        DailyStats.objects.update_or_create(
            date=today,
            server=server,
            defaults={
                "new_catches": today_catches.count(),
                "total_trapped_seconds": (
                    today_catches.aggregate(t=Sum("trapped_seconds"))["t"] or 0
                ),
                "unique_ips": today_catches.values("ip_hash").distinct().count(),
                "unique_countries": (
                    today_catches.exclude(country_code="")
                    .values("country_code").distinct().count()
                ),
                "longest_trap_seconds": (
                    today_catches.aggregate(m=Max("trapped_seconds"))["m"] or 0
                ),
            },
        )

        # Update server aggregate fields
        server_catches = CaughtBot.objects.filter(server=server)
        server.total_catches = server_catches.count()
        server.total_trapped_seconds = (
            server_catches.aggregate(t=Sum("trapped_seconds"))["t"] or 0
        )
        server.unique_ips = server_catches.values("ip_hash").distinct().count()
        server.unique_countries = (
            server_catches.exclude(country_code="")
            .values("country_code").distinct().count()
        )
        server.save()

    # Update country stats
    country_data = (
        CaughtBot.objects.exclude(country_code="")
        .values("country_code", "country_name")
        .annotate(
            total_catches=Count("id"),
            total_trapped=Sum("trapped_seconds"),
            unique_ips=Count("ip_hash", distinct=True),
            last_catch=Max("first_seen"),
        )
    )
    for cd in country_data:
        CountryStats.objects.update_or_create(
            country_code=cd["country_code"],
            defaults={
                "country_name": cd["country_name"],
                "total_catches": cd["total_catches"],
                "total_trapped_seconds": cd["total_trapped"] or 0,
                "unique_ips": cd["unique_ips"],
                "last_catch_at": cd["last_catch"],
            },
        )

    # Update bytes sent
    byte_totals = query_global_totals()
    for server in Server.objects.filter(is_active=True):
        if server.host_identifier in byte_totals:
            server.total_bytes_sent = int(byte_totals[server.host_identifier])
            server.save(update_fields=["total_bytes_sent"])

    logger.info("Aggregated daily stats for %s", today)
    return f"Aggregated stats for {today}"


@shared_task
def check_achievements():
    """Check and unlock achievements. Runs every 10 minutes."""
    unlocked = evaluate_all_achievements()
    if unlocked:
        logger.info("Unlocked %d achievements: %s", len(unlocked), unlocked)
    return f"{len(unlocked)} newly unlocked"


@shared_task
def generate_daily_challenges_task():
    """Generate daily challenges at midnight. Runs daily at 00:05."""
    from apps.aquarium.challenge_service import generate_daily_challenges

    generated = generate_daily_challenges()
    logger.info("Generated %d daily challenges", len(generated))
    return f"Generated {len(generated)} challenges"


@shared_task
def evaluate_daily_challenges_task():
    """Evaluate daily challenge progress. Runs every 10 minutes."""
    from apps.aquarium.challenge_service import evaluate_daily_challenges

    completed = evaluate_daily_challenges()
    if completed:
        logger.info("Completed %d challenges: %s", len(completed), completed)
    return f"{len(completed)} newly completed"


@shared_task
def full_recalculate():
    """Full recalculation of scores and species. Runs daily at 3 AM."""
    species_list = list(FishSpecies.objects.order_by("min_trapped_seconds"))
    updated = 0

    for bot in CaughtBot.objects.select_related("species").iterator(chunk_size=500):
        new_species = None
        for sp in species_list:
            if bot.trapped_seconds >= sp.min_trapped_seconds:
                new_species = sp
            else:
                break

        new_score = calculate_score(new_species, bot.trapped_seconds)
        if bot.species != new_species or bot.score != new_score:
            bot.species = new_species
            bot.score = new_score
            bot.save(update_fields=["species", "score", "updated_at"])
            updated += 1

    logger.info("Recalculated %d bot scores", updated)
    return f"Recalculated {updated} bot scores"


@shared_task
def warm_pond_cache():
    """Pre-warm the live pond cache so no user request pays the InfluxDB cost."""
    from apps.aquarium.services import get_pond_fish

    try:
        data = get_pond_fish(force_refresh=True)
        return f"{data['total_active']} active bots cached"
    except Exception:
        logger.debug("Cache warming failed, keeping stale cache", exc_info=True)
        return "warming failed, stale cache preserved"
