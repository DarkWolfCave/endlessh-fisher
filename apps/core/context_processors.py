"""Global template context processors."""

from django.conf import settings

from apps.aquarium.models import CaughtBot


def game_context(request):
    """Add game-wide context to all templates."""
    ticker_catches = (
        CaughtBot.objects
        .select_related("species", "server")
        .order_by("-first_seen")[:10]
    )
    return {
        "GAME_NAME": "Endlessh Fisher",
        "GAME_VERSION": "1.0.0",
        "DEBUG": settings.DEBUG,
        "ticker_catches": ticker_catches,
    }
