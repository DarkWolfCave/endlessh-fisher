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

from .influx_client import query_global_totals, query_new_connections, query_trapped_time
from .models import SyncState

logger = logging.getLogger(__name__)


def _get_or_create_sync_state(host: str, metric: str) -> SyncState:
    """Get or create a SyncState, defaulting to 24h ago."""
    state, created = SyncState.objects.get_or_create(
        server_host=host,
        metric_type=metric,
        defaults={"last_sync_at": timezone.now() - timedelta(hours=24)},
    )
    return state


def _hash_ip(ip: str) -> str:
    return hashlib.sha256(ip.encode()).hexdigest()


@shared_task(bind=True, max_retries=3)
def sync_bot_data(self):
    """Sync new bot connection data from InfluxDB into CaughtBot records.

    Runs every 5 minutes via Celery Beat.
    """
    servers = Server.objects.filter(is_active=True)
    total_synced = 0

    for server in servers:
        host = server.host_identifier
        state = _get_or_create_sync_state(host, "client_open")
        since = state.last_sync_at.isoformat()

        try:
            # Get new connections
            connections = query_new_connections(since, host=host)
            if not connections:
                continue

            # Get trapped time data for enrichment
            trapped_data = query_trapped_time(since, host=host)
            trapped_by_ip = {}
            for t in trapped_data:
                ip = t["ip"]
                if ip and (ip not in trapped_by_ip or t["value"] > trapped_by_ip[ip]):
                    trapped_by_ip[ip] = t["value"]

            synced = 0
            with transaction.atomic():
                for conn in connections:
                    ip = conn["ip"]
                    if not ip:
                        continue

                    fingerprint = f"{host}:{ip}:{conn['time'].isoformat()}"
                    trapped_seconds = trapped_by_ip.get(ip, 0) or 0
                    species = classify_fish(trapped_seconds)
                    score = calculate_score(species, trapped_seconds)
                    ip_hash = _hash_ip(ip)
                    country = conn.get("country", "") or ""

                    # Parse country code (endlessh-go sends "US", "DE", etc.)
                    country_code = country[:2].upper() if country else ""

                    _, created = CaughtBot.objects.update_or_create(
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
                            "first_seen": conn["time"],
                            "last_seen": conn["time"],
                            "score": score,
                        },
                    )
                    if created:
                        synced += 1

                state.last_sync_at = timezone.now()
                state.records_synced += synced
                state.last_error = ""
                state.save()

            total_synced += synced
            logger.info("Synced %d new catches from %s", synced, host)

        except Exception as exc:
            state.last_error = str(exc)
            state.save()
            logger.exception("Failed to sync data from %s", host)
            raise self.retry(exc=exc, countdown=60)

    return f"Synced {total_synced} new catches"


@shared_task
def aggregate_daily_stats():
    """Aggregate daily statistics per server.

    Runs every hour via Celery Beat.
    """
    today = timezone.now().date()

    for server in Server.objects.filter(is_active=True):
        today_catches = CaughtBot.objects.filter(
            server=server, first_seen__date=today
        )
        stats, _ = DailyStats.objects.update_or_create(
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
        server.total_catches = CaughtBot.objects.filter(server=server).count()
        server.total_trapped_seconds = (
            CaughtBot.objects.filter(server=server)
            .aggregate(t=Sum("trapped_seconds"))["t"] or 0
        )
        server.unique_ips = (
            CaughtBot.objects.filter(server=server)
            .values("ip_hash").distinct().count()
        )
        server.unique_countries = (
            CaughtBot.objects.filter(server=server)
            .exclude(country_code="")
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

    # Update bytes sent from InfluxDB
    byte_totals = query_global_totals("-24h")
    for server in Server.objects.filter(is_active=True):
        if server.host_identifier in byte_totals:
            server.total_bytes_sent = int(byte_totals[server.host_identifier])
            server.save(update_fields=["total_bytes_sent"])

    logger.info("Aggregated daily stats for %s", today)
    return f"Aggregated stats for {today}"


@shared_task
def check_achievements():
    """Check and unlock achievements based on current stats.

    Runs every 10 minutes via Celery Beat.
    """
    unlocked = evaluate_all_achievements()
    if unlocked:
        logger.info("Unlocked %d new achievements: %s", len(unlocked), unlocked)
    return f"Checked achievements, {len(unlocked)} newly unlocked"


@shared_task
def full_recalculate():
    """Full recalculation of all scores and species classifications.

    Runs daily at 3 AM. Ensures data consistency.
    """
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
