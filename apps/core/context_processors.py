"""Global template context processors."""

from django.conf import settings


def game_context(request):
    """Add game-wide context to all templates."""
    return {
        "GAME_NAME": "Endlessh Fisher",
        "GAME_VERSION": "1.0.0",
        "DEBUG": settings.DEBUG,
    }
