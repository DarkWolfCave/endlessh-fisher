"""Custom template tags for Endlessh Game."""

from django import template

register = template.Library()


@register.filter
def duration_format(seconds):
    """Format seconds into human-readable duration."""
    if seconds is None:
        return "0s"
    seconds = float(seconds)
    if seconds < 60:
        return f"{seconds:.0f}s"
    if seconds < 3600:
        minutes = seconds / 60
        return f"{minutes:.1f}min"
    if seconds < 86400:
        hours = seconds / 3600
        return f"{hours:.1f}h"
    days = seconds / 86400
    return f"{days:.1f}d"


@register.filter
def rarity_color(rarity):
    """Return CSS color class for fish rarity."""
    colors = {
        "common": "text-gray-400",
        "uncommon": "text-green-400",
        "rare": "text-blue-400",
        "epic": "text-purple-400",
        "legendary": "text-yellow-400",
        "mythic": "text-red-500",
    }
    return colors.get(rarity, "text-gray-400")


@register.filter
def score_format(score):
    """Format score with thousand separators."""
    if score is None:
        return "0"
    return f"{int(score):,}".replace(",", ".")
