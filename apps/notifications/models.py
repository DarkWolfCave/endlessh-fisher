"""Notification models - unified inbox for game events."""

from django.db import models

from apps.core.models import TimeStampedModel


class Notification(TimeStampedModel):
    """A persisted notification for the notification inbox.

    Single-user game: no User FK needed.
    When going multi-user: add User FK (same pattern as UnlockedAchievement).
    """

    CATEGORY_CHOICES = [
        ("achievement", "Achievement Unlocked"),
        ("challenge", "Daily Challenge Completed"),
        ("rare_catch", "Rare Fish Caught"),
        ("treasure", "Treasure Tip Discovered"),
    ]

    RARITY_CHOICES = [
        ("common", "Common"),
        ("uncommon", "Uncommon"),
        ("rare", "Rare"),
        ("epic", "Epic"),
        ("legendary", "Legendary"),
        ("mythic", "Mythic"),
        # Achievement rarities
        ("bronze", "Bronze"),
        ("silver", "Silver"),
        ("gold", "Gold"),
        ("platinum", "Platinum"),
        ("diamond", "Diamond"),
        # Challenge difficulties (used as visual rarity)
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, db_index=True)
    title = models.CharField(max_length=200)
    title_de = models.CharField(max_length=200)
    message = models.TextField(max_length=500, blank=True, default="")
    message_de = models.TextField(max_length=500, blank=True, default="")
    emoji = models.CharField(max_length=10, default="\U0001F514")
    rarity = models.CharField(
        max_length=20, choices=RARITY_CHOICES, blank=True, default=""
    )
    rarity_color = models.CharField(max_length=7, blank=True, default="")

    # References to source objects (plain IDs, no FKs to avoid circular deps)
    achievement_slug = models.SlugField(max_length=80, blank=True, default="")
    challenge_id = models.PositiveIntegerField(null=True, blank=True)
    caught_bot_id = models.PositiveIntegerField(null=True, blank=True)

    # Status flags
    is_read = models.BooleanField(default=False, db_index=True)
    toast_shown = models.BooleanField(default=False, db_index=True)

    class Meta:
        ordering = ["-created_at"]
        indexes = [
            models.Index(
                fields=["is_read", "-created_at"],
                name="idx_notif_unread",
            ),
            models.Index(
                fields=["toast_shown", "-created_at"],
                name="idx_notif_toast",
            ),
            models.Index(
                fields=["category", "-created_at"],
                name="idx_notif_category",
            ),
        ]

    def __str__(self):
        status = "read" if self.is_read else "NEW"
        return f"[{status}] {self.title_de} ({self.category})"
