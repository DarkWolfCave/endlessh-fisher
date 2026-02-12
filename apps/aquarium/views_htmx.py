"""HTMX partial views for live-updating dashboard components."""

from django.db.models import Sum
from django.shortcuts import render

from .models import CaughtBot, CountryStats


def stats_bar(request):
    """Live stats bar - polled every 30s."""
    total_catches = CaughtBot.objects.count()
    active_traps = CaughtBot.objects.filter(is_active=True).count()
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
