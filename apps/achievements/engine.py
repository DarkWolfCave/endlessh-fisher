"""Achievement evaluation engine - checks thresholds and unlocks badges."""

import logging

from django.db.models import Count, Max, Sum
from django.utils import timezone

from apps.aquarium.models import CaughtBot, CountryStats

from .models import Achievement, UnlockedAchievement

logger = logging.getLogger(__name__)


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
    total_bytes = (
        CaughtBot.objects.aggregate(b=Sum("bytes_sent"))["b"] or 0
    )

    # Per-server catches
    server_catches = dict(
        CaughtBot.objects.values_list("server__slug")
        .annotate(count=Count("id"))
        .values_list("server__slug", "count")
    )

    # Best daily catch count
    from apps.aquarium.models import DailyStats
    daily_best = (
        DailyStats.objects.aggregate(m=Max("new_catches"))["m"] or 0
    )

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

    return newly_unlocked
