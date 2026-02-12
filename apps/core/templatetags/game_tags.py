"""Custom template tags for Endlessh Game."""

from django import template

register = template.Library()


@register.filter
def duration_format(seconds):
    """Format seconds into human-readable duration."""
    if not seconds:
        return "0s"
    try:
        seconds = float(seconds)
    except (ValueError, TypeError):
        return "0s"
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
    if not score and score != 0:
        return "0"
    try:
        return f"{int(score):,}".replace(",", ".")
    except (ValueError, TypeError):
        return "0"


_SPECIES_EMOJI = {
    "fish-plankton": "\U0001F9A0",
    "fish-sardine": "\U0001F41F",
    "fish-anchovy": "\U0001F41F",
    "fish-trout": "\U0001F41F",
    "fish-pike": "\U0001F988",
    "fish-salmon": "\U0001F420",
    "fish-tuna": "\U0001F420",
    "fish-swordfish": "\U0001F42C",
    "fish-marlin": "\U0001F42C",
    "fish-whale-shark": "\U0001F40B",
    "fish-kraken": "\U0001F419",
    "fish-leviathan": "\U0001F409",
}


@register.filter
def species_emoji(css_class):
    """Return emoji for a fish species by its css_class."""
    return _SPECIES_EMOJI.get(css_class, "\U0001F41F")
