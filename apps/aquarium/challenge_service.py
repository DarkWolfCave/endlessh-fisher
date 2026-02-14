"""Daily challenge generation and progress tracking."""

import random
from datetime import timedelta

from django.db.models import Count, Sum
from django.utils import timezone

from .models import (
    CaughtBot, ChallengeTemplate, CollectedTreasure, DailyChallenge,
)


def generate_daily_challenges(target_date=None) -> list[str]:
    """Generate 3 daily challenges (1 easy + 1 medium + 1 hard).

    Threshold randomized within template's min/max range.
    Idempotent: skips if already generated for this date.
    Returns list of generated challenge descriptions.
    """
    if target_date is None:
        target_date = timezone.localtime().date()

    # Skip if already generated
    if DailyChallenge.objects.filter(date=target_date).count() >= 3:
        return []

    generated = []
    for difficulty in ["easy", "medium", "hard"]:
        templates = list(
            ChallengeTemplate.objects.filter(
                difficulty=difficulty, is_active=True
            )
        )
        if not templates:
            continue

        template = random.choice(templates)

        # Avoid duplicate template on same day
        if DailyChallenge.objects.filter(
            date=target_date, template=template
        ).exists():
            remaining = [t for t in templates if t != template]
            if remaining:
                template = random.choice(remaining)
            else:
                continue

        threshold = random.randint(template.threshold_min, template.threshold_max)
        desc = template.description_template.format(threshold=threshold)
        desc_de = template.description_template_de.format(threshold=threshold)

        DailyChallenge.objects.create(
            date=target_date,
            template=template,
            threshold=threshold,
            description=desc,
            description_de=desc_de,
            reward_points=template.reward_points,
        )
        generated.append(desc_de)

    return generated


def evaluate_daily_challenges(target_date=None) -> list[str]:
    """Evaluate progress on today's challenges.

    Returns list of newly completed challenge descriptions.
    """
    if target_date is None:
        target_date = timezone.localtime().date()

    challenges = DailyChallenge.objects.filter(
        date=target_date, is_completed=False
    ).select_related("template")

    if not challenges:
        return []

    today_start = timezone.make_aware(
        timezone.datetime.combine(target_date, timezone.datetime.min.time())
    )
    today_end = today_start + timedelta(days=1)

    # Pre-compute daily metrics
    today_catches = CaughtBot.objects.filter(
        first_seen__gte=today_start, first_seen__lt=today_end
    )

    metrics = {
        "daily_catches": today_catches.count(),
        "daily_trapped_seconds": (
            today_catches.aggregate(t=Sum("trapped_seconds"))["t"] or 0
        ),
        "daily_unique_countries": (
            today_catches.exclude(country_code="")
            .values("country_code").distinct().count()
        ),
        "daily_unique_species": (
            today_catches.values("species").distinct().count()
        ),
        "daily_rare_catches": (
            today_catches.filter(
                species__rarity__in=["rare", "epic", "legendary", "mythic"]
            ).count()
        ),
        "daily_treasures": (
            CollectedTreasure.objects.filter(
                collected_at__gte=today_start, collected_at__lt=today_end
            ).count()
        ),
    }

    # Per-server catches
    server_catches = dict(
        today_catches.values_list("server__slug")
        .annotate(count=Count("id"))
        .values_list("server__slug", "count")
    )

    newly_completed = []

    for challenge in challenges:
        metric = challenge.template.metric
        if metric == "daily_server_catches" and challenge.template.server_filter:
            value = server_catches.get(
                challenge.template.server_filter.slug, 0
            )
        else:
            value = metrics.get(metric, 0)

        challenge.current_value = value

        if value >= challenge.threshold:
            challenge.is_completed = True
            challenge.completed_at = timezone.now()
            challenge.notified = False
            newly_completed.append(challenge.description_de)

        challenge.save(update_fields=[
            "current_value", "is_completed", "completed_at", "notified",
            "updated_at",
        ])

    return newly_completed


def get_today_challenges() -> list[dict]:
    """Get today's challenges with progress for display."""
    today = timezone.localtime().date()
    challenges = DailyChallenge.objects.filter(
        date=today
    ).select_related("template")

    return [
        {
            "id": c.id,
            "description": c.description,
            "description_de": c.description_de,
            "emoji": c.template.emoji,
            "difficulty": c.template.difficulty,
            "threshold": c.threshold,
            "current_value": c.current_value,
            "progress_percent": c.progress_percent,
            "is_completed": c.is_completed,
            "reward_points": c.reward_points,
        }
        for c in challenges
    ]
