"""Celery tasks for syncing InfluxDB data into the game database."""

import hashlib
import logging
from datetime import timedelta

from celery import shared_task
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

        trapped_times = query_trapped_times(since)
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
                country_code = country[:2].upper() if country else ""

                obj, created = CaughtBot.objects.update_or_create(
                    influx_fingerprint=fingerprint,
                    defaults={
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
                        "first_seen": conn["time"],
                        "last_seen": conn["time"],
                        "score": score,
                    },
                )
                if created:
                    created_count += 1
                else:
                    updated_count += 1

            state.last_sync_at = timezone.now()
            state.records_synced += created_count
            state.last_error = ""
            state.save()

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
    today = timezone.now().date()

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
