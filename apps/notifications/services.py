"""Notification creation and query service."""

import logging

from django.utils.html import strip_tags

from .models import Notification

logger = logging.getLogger(__name__)

MAX_TITLE_LENGTH = 200
MAX_MESSAGE_LENGTH = 500


def create_notification(
    *,
    category: str,
    title: str,
    title_de: str,
    message: str = "",
    message_de: str = "",
    emoji: str = "\U0001F514",
    rarity: str = "",
    rarity_color: str = "",
    achievement_slug: str = "",
    challenge_id: int | None = None,
    caught_bot_id: int | None = None,
) -> Notification:
    """Create a notification. Sanitizes all text inputs.

    This is the ONLY entry point for creating notifications.
    Called from:
      - achievements/engine.py (achievement unlocks)
      - aquarium/challenge_service.py (challenge completions)
      - collector/tasks.py (rare fish catches)
    """
    return Notification.objects.create(
        category=strip_tags(category)[:20],
        title=strip_tags(title)[:MAX_TITLE_LENGTH],
        title_de=strip_tags(title_de)[:MAX_TITLE_LENGTH],
        message=strip_tags(message)[:MAX_MESSAGE_LENGTH],
        message_de=strip_tags(message_de)[:MAX_MESSAGE_LENGTH],
        emoji=emoji[:10],
        rarity=strip_tags(rarity)[:20],
        rarity_color=strip_tags(rarity_color)[:7],
        achievement_slug=strip_tags(achievement_slug)[:80],
        challenge_id=challenge_id,
        caught_bot_id=caught_bot_id,
    )


def get_unread_count() -> int:
    """Count of unread notifications for badge display."""
    return Notification.objects.filter(is_read=False).count()


def get_pending_toasts(limit: int = 3) -> list[Notification]:
    """Notifications not yet shown as toast popups.

    Returns oldest first so they appear in chronological order.
    """
    return list(
        Notification.objects.filter(toast_shown=False)
        .order_by("created_at")[:limit]
    )


def mark_toasts_shown(notification_ids: list[int]) -> int:
    """Mark notifications as toasted (popup was displayed)."""
    return Notification.objects.filter(
        id__in=notification_ids, toast_shown=False
    ).update(toast_shown=True)


def mark_read(notification_id: int) -> bool:
    """Mark a single notification as read."""
    return Notification.objects.filter(
        id=notification_id, is_read=False
    ).update(is_read=True) > 0


def mark_all_read() -> int:
    """Mark all unread notifications as read."""
    return Notification.objects.filter(is_read=False).update(is_read=True)


def delete_notification(notification_id: int) -> bool:
    """Delete a single notification."""
    return Notification.objects.filter(id=notification_id).delete()[0] > 0


def delete_all_read() -> int:
    """Delete all read notifications."""
    count, _ = Notification.objects.filter(is_read=True).delete()
    return count


def delete_all() -> int:
    """Delete all notifications."""
    count, _ = Notification.objects.all().delete()
    return count
