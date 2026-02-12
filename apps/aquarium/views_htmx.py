"""HTMX partial views for live-updating dashboard components."""

import json

from django.db.models import Sum
from django.shortcuts import render

from .models import CaughtBot, CountryStats
from .services import check_rare_fish_alerts, get_pond_fish
from .views import _get_active_traps


def stats_bar(request):
    """Live stats bar - polled every 30s."""
    total_catches = CaughtBot.objects.count()
    active_traps = _get_active_traps()
    total_score = CaughtBot.objects.aggregate(total=Sum("score"))["total"] or 0
    total_countries = CountryStats.objects.count()
    total_trapped = (
        CaughtBot.objects.aggregate(total=Sum("trapped_seconds"))["total"] or 0
    )

    return render(request, "components/stats_bar.html", {
        "total_catches": total_catches,
        "active_traps": active_traps,
        "total_score": total_score,
        "total_countries": total_countries,
        "total_trapped_seconds": total_trapped,
    })


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
