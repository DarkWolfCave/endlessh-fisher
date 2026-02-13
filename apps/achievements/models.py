"""Achievement models - badges, milestones, unlocks."""

from django.db import models

from apps.core.models import TimeStampedModel


class AchievementCategory(TimeStampedModel):
    """Achievement category grouping (e.g., 'First Steps', 'Time Waster')."""

    slug = models.SlugField(unique=True, max_length=50)
    name = models.CharField(max_length=100)
    name_de = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, default="trophy")
    sort_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["sort_order"]
        verbose_name_plural = "Achievement Categories"

    def __str__(self):
        return self.name_de


class Achievement(TimeStampedModel):
    """Achievement definition with metric and threshold."""

    METRIC_CHOICES = [
        ("total_catches", "Total Catches"),
        ("total_trapped_seconds", "Total Trapped Seconds"),
        ("unique_countries", "Unique Countries"),
        ("unique_ips", "Unique IPs"),
        ("single_trap_seconds", "Single Longest Trap"),
        ("server_catches", "Catches on Specific Server"),
        ("min_server_catches", "Min Catches Across All Servers"),
        ("species_caught", "Unique Species Caught"),
        ("daily_catches", "Catches in a Single Day"),
        ("total_bytes_sent", "Total Bytes Sent"),
        ("total_treasures", "Total Treasures Collected"),
        ("unique_treasure_types", "Unique Treasure Types Collected"),
        ("challenges_completed", "Total Challenges Completed"),
    ]

    RARITY_CHOICES = [
        ("bronze", "Bronze"),
        ("silver", "Silver"),
        ("gold", "Gold"),
        ("platinum", "Platinum"),
        ("diamond", "Diamond"),
    ]

    slug = models.SlugField(unique=True, max_length=80)
    category = models.ForeignKey(
        AchievementCategory, on_delete=models.CASCADE, related_name="achievements"
    )
    name = models.CharField(max_length=200)
    name_de = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    description_de = models.TextField(max_length=500)
    metric = models.CharField(max_length=50, choices=METRIC_CHOICES)
    threshold = models.FloatField()
    server_filter = models.ForeignKey(
        "aquarium.Server",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="If set, only counts catches on this server.",
    )
    rarity = models.CharField(max_length=20, choices=RARITY_CHOICES)
    points = models.PositiveIntegerField(default=10)
    lottie_file = models.CharField(max_length=200, blank=True, default="")
    svg_file = models.CharField(max_length=200, blank=True, default="")
    sort_order = models.PositiveSmallIntegerField(default=0)
    is_secret = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["category", "sort_order"]
        indexes = [
            models.Index(
                fields=["metric", "threshold"], name="idx_achievement_metric"
            ),
        ]

    def __str__(self):
        return f"{self.name_de} ({self.rarity})"


class UnlockedAchievement(TimeStampedModel):
    """Tracks unlocked achievements.
    Single-user: OneToOneField on achievement.
    When going multi-user: change to ForeignKey + add User FK.
    """

    achievement = models.OneToOneField(
        Achievement, on_delete=models.CASCADE, related_name="unlock_record"
    )
    unlocked_at = models.DateTimeField()
    current_value = models.FloatField()
    notified = models.BooleanField(default=False)

    class Meta:
        ordering = ["-unlocked_at"]

    def __str__(self):
        status = "notified" if self.notified else "NEW"
        return f"{self.achievement.name_de} [{status}]"
