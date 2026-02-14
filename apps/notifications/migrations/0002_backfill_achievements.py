"""Backfill notifications for existing unlocked achievements."""

from django.db import migrations

_ACHIEVEMENT_RARITY_COLORS = {
    "bronze": "#CD7F32",
    "silver": "#C0C0C0",
    "gold": "#FBBF24",
    "platinum": "#93C5FD",
    "diamond": "#C4B5FD",
}


def backfill_achievements(apps, schema_editor):
    """Create notification records for all existing unlocked achievements."""
    UnlockedAchievement = apps.get_model("achievements", "UnlockedAchievement")
    Notification = apps.get_model("notifications", "Notification")

    for ua in UnlockedAchievement.objects.select_related("achievement").all():
        a = ua.achievement
        Notification.objects.create(
            category="achievement",
            title=f"Achievement Unlocked: {a.name}",
            title_de=f"Achievement freigeschaltet: {a.name_de}",
            message=a.description,
            message_de=a.description_de,
            emoji="\U0001F3C5",
            rarity=a.rarity,
            rarity_color=_ACHIEVEMENT_RARITY_COLORS.get(a.rarity, "#9CA3AF"),
            achievement_slug=a.slug,
            is_read=True,
            toast_shown=True,
            created_at=ua.unlocked_at,
        )


def reverse_backfill(apps, schema_editor):
    """Remove backfilled achievement notifications."""
    Notification = apps.get_model("notifications", "Notification")
    Notification.objects.filter(category="achievement", is_read=True, toast_shown=True).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("notifications", "0001_initial"),
        ("achievements", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(backfill_achievements, reverse_backfill),
    ]
