"""HTMX partial views for live-updating dashboard components."""

import json

from django.shortcuts import render

from .models import CaughtBot
from .services import check_rare_fish_alerts, get_pond_fish
from .views import _get_active_traps, get_cached_stats


def stats_bar(request):
    """Live stats bar - polled every 30s. Uses cached aggregations."""
    stats = get_cached_stats()
    stats["active_traps"] = _get_active_traps()
    return render(request, "components/stats_bar.html", stats)


def activity_feed(request):
    """Recent catches - polled every 15s."""
    recent = CaughtBot.objects.select_related("species", "server")[:8]
    return render(request, "components/activity_feed.html", {
        "recent_catches": recent,
    })


def live_pond(request):
    """Live pond - polled every 15s via HTMX."""
    pond_data = get_pond_fish()
    return render(request, "components/live_pond.html", {
        "fish_list": pond_data["fish"],
        "total_active": pond_data["total_active"],
        "last_updated": pond_data["last_updated"],
        "fish_json": json.dumps(pond_data["fish"]),
    })


def catch_ticker(request):
    """Scrolling catch ticker - polled every 15s."""
    recent = (
        CaughtBot.objects
        .select_related("species", "server")
        .order_by("-first_seen")[:10]
    )
    return render(request, "components/catch_ticker.html", {
        "ticker_catches": recent,
    })


def rare_alert(request):
    """Rare fish alert toast - polled every 30s."""
    alerts = check_rare_fish_alerts()
    return render(request, "components/rare_alert.html", {
        "alerts": alerts,
        "alerts_json": json.dumps(alerts),
    })
