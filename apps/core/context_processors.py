"""Global template context processors."""

from django.conf import settings
from django.core.cache import cache

from apps.aquarium.models import CaughtBot


def game_context(request):
    """Add game-wide context to all templates."""
    # Ticker catches cached 60s (changes only on sync every 5 min)
    ticker_catches = cache.get("endlessh:ticker_catches")
    if ticker_catches is None:
        ticker_catches = list(
            CaughtBot.objects
            .select_related("species", "server")
            .order_by("-first_seen")[:10]
        )
        cache.set("endlessh:ticker_catches", ticker_catches, 60)

    return {
        "GAME_NAME": "Endlessh Fisher",
        "GAME_VERSION": "1.0.0",
        "DEBUG": settings.DEBUG,
        "ticker_catches": ticker_catches,
    }
