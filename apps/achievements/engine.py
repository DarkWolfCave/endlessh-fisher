"""Achievement evaluation engine - checks thresholds and unlocks badges."""

import logging

from django.db.models import Count, Max, Sum
from django.utils import timezone

from apps.aquarium.models import (
    CaughtBot, CollectedTreasure, CountryStats, DailyChallenge, IPLookupLog,
    Server,
)

from apps.notifications.services import create_notification

from .models import Achievement, UnlockedAchievement

logger = logging.getLogger(__name__)

_ACHIEVEMENT_RARITY_COLORS = {
    "bronze": "#CD7F32",
    "silver": "#C0C0C0",
    "gold": "#FBBF24",
    "platinum": "#93C5FD",
    "diamond": "#C4B5FD",
}


def _get_current_stats() -> dict:
    """Gather current aggregate stats for achievement evaluation."""
    total_catches = CaughtBot.objects.count()
    total_trapped = (
        CaughtBot.objects.aggregate(t=Sum("trapped_seconds"))["t"] or 0
    )
    unique_countries = CountryStats.objects.count()
    unique_ips = CaughtBot.objects.values("ip_hash").distinct().count()
    single_longest = (
        CaughtBot.objects.aggregate(m=Max("trapped_seconds"))["m"] or 0
    )
    species_caught = (
        CaughtBot.objects.values("species").distinct().count()
    )
    # bytes_sent is tracked per-server (from endlessh_sent_bytes_total counter),
    # not per-bot, so aggregate from Server model
    total_bytes = (
        Server.objects.filter(is_active=True)
        .aggregate(b=Sum("total_bytes_sent"))["b"] or 0
    )

    # Per-server catches
    server_catches = dict(
        CaughtBot.objects.values_list("server__slug")
        .annotate(count=Count("id"))
        .values_list("server__slug", "count")
    )

    # Min catches across all active servers (for "master every server" achievements)
    active_servers = set(
        Server.objects.filter(is_active=True).values_list("slug", flat=True)
    )
    min_server = (
        min(server_catches.get(s, 0) for s in active_servers)
        if active_servers
        else 0
    )

    # Best daily catch count
    from apps.aquarium.models import DailyStats
    daily_best = (
        DailyStats.objects.aggregate(m=Max("new_catches"))["m"] or 0
    )

    # Treasure & challenge stats
    total_treasures = CollectedTreasure.objects.count()
    unique_treasure_types = (
        CollectedTreasure.objects.values("treasure_type").distinct().count()
    )
    challenges_completed = DailyChallenge.objects.filter(
        is_completed=True
    ).count()

    # IP lookup stats
    ip_lookups_total = IPLookupLog.objects.count()
    ip_lookups_high_abuse = IPLookupLog.objects.filter(abuse_score__gte=90).count()
    ip_lookups_tor = IPLookupLog.objects.filter(is_tor=True).count()
    ip_lookups_dangerous_ports = IPLookupLog.objects.filter(has_dangerous_ports=True).count()
    ip_lookups_vulns = IPLookupLog.objects.filter(has_vulns=True).count()

    return {
        "total_catches": total_catches,
        "total_trapped_seconds": total_trapped,
        "unique_countries": unique_countries,
        "unique_ips": unique_ips,
        "single_trap_seconds": single_longest,
        "species_caught": species_caught,
        "total_bytes_sent": total_bytes,
        "daily_catches": daily_best,
        "server_catches": server_catches,
        "min_server_catches": min_server,
        "total_treasures": total_treasures,
        "unique_treasure_types": unique_treasure_types,
        "challenges_completed": challenges_completed,
        "ip_lookups_total": ip_lookups_total,
        "ip_lookups_high_abuse": ip_lookups_high_abuse,
        "ip_lookups_tor": ip_lookups_tor,
        "ip_lookups_dangerous_ports": ip_lookups_dangerous_ports,
        "ip_lookups_vulns": ip_lookups_vulns,
    }


def evaluate_all_achievements() -> list[str]:
    """Evaluate all active achievements and unlock those that meet thresholds.

    Returns list of newly unlocked achievement slugs.
    """
    stats = _get_current_stats()
    now = timezone.now()
    newly_unlocked = []

    # Get all active achievements that haven't been unlocked yet
    unlocked_ids = UnlockedAchievement.objects.values_list(
        "achievement_id", flat=True
    )
    pending = Achievement.objects.filter(
        is_active=True
    ).exclude(id__in=unlocked_ids)

    for achievement in pending:
        metric = achievement.metric
        threshold = achievement.threshold
        current_value = 0

        if metric == "server_catches" and achievement.server_filter:
            server_slug = achievement.server_filter.slug
            current_value = stats.get("server_catches", {}).get(server_slug, 0)
        elif metric in stats:
            current_value = stats[metric]

        if current_value >= threshold:
            UnlockedAchievement.objects.create(
                achievement=achievement,
                unlocked_at=now,
                current_value=current_value,
                notified=False,
            )
            newly_unlocked.append(achievement.slug)
            logger.info(
                "Achievement unlocked: %s (value: %s >= %s)",
                achievement.slug, current_value, threshold,
            )
            create_notification(
                category="achievement",
                title=f"Achievement Unlocked: {achievement.name}",
                title_de=f"Achievement freigeschaltet: {achievement.name_de}",
                message=achievement.description,
                message_de=achievement.description_de,
                emoji="\U0001F3C5",
                rarity=achievement.rarity,
                rarity_color=_ACHIEVEMENT_RARITY_COLORS.get(
                    achievement.rarity, "#9CA3AF"
                ),
                achievement_slug=achievement.slug,
            )

    return newly_unlocked
