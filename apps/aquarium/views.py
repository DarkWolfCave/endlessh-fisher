"""Aquarium template views - dashboard, aquarium, fish detail."""

import json

from django.core.cache import cache
from django.db.models import Count, Sum
from django.shortcuts import get_object_or_404, render

from .models import CaughtBot, CountryStats, DailyStats, FishSpecies, Server
from .services import get_pond_fish

# Cache TTL: stats change only on sync (every 5 min), so 120s is safe
_STATS_CACHE_TTL = 120


def get_cached_stats() -> dict:
    """Get aggregated game stats from cache or compute them.

    Cached for 120s. Invalidated by sync_bot_data on completion.
    """
    cache_key = "endlessh:game_stats"
    stats = cache.get(cache_key)
    if stats is not None:
        return stats

    stats = {
        "total_catches": CaughtBot.objects.count(),
        "total_score": CaughtBot.objects.aggregate(t=Sum("score"))["t"] or 0,
        "total_trapped_seconds": (
            CaughtBot.objects.aggregate(t=Sum("trapped_seconds"))["t"] or 0
        ),
        "total_countries": CountryStats.objects.count(),
    }
    cache.set(cache_key, stats, _STATS_CACHE_TTL)
    return stats


def _get_active_traps():
    """Get active trap count from pond data (same source as Live Pond)."""
    return get_pond_fish()["total_active"]


def dashboard(request):
    """Main dashboard with server ponds and live stats."""
    servers = Server.objects.filter(is_active=True)
    recent_catches = CaughtBot.objects.select_related("species", "server")[:10]
    stats = get_cached_stats()

    # Live Pond data for initial render (also provides active_traps)
    pond_data = get_pond_fish()

    return render(request, "aquarium/dashboard.html", {
        "servers": servers,
        "recent_catches": recent_catches,
        "active_traps": pond_data["total_active"],
        **stats,
        "fish_list": pond_data["fish"],
        "total_active": pond_data["total_active"],
        "last_updated": pond_data["last_updated"],
        "fish_json": json.dumps(pond_data["fish"]),
    })


def aquarium(request):
    """Full aquarium view - all fish with filters."""
    server_slug = request.GET.get("server")
    species_slug = request.GET.get("species")
    country = request.GET.get("country")

    catches = CaughtBot.objects.select_related("species", "server")

    if server_slug:
        catches = catches.filter(server__slug=server_slug)
    if species_slug:
        catches = catches.filter(species__slug=species_slug)
    if country:
        catches = catches.filter(country_code=country)

    catches = catches[:100]

    return render(request, "aquarium/aquarium.html", {
        "catches": catches,
        "servers": Server.objects.filter(is_active=True),
        "species_list": FishSpecies.objects.all(),
        "selected_server": server_slug,
        "selected_species": species_slug,
        "selected_country": country,
    })


def server_detail(request, slug):
    """Per-server pond view."""
    server = get_object_or_404(Server, slug=slug)
    catches = CaughtBot.objects.filter(server=server).select_related("species")[:50]
    daily_stats = DailyStats.objects.filter(server=server)[:30]
    species_counts = (
        CaughtBot.objects.filter(server=server)
        .values("species__name_de", "species__rarity_color")
        .annotate(count=Count("id"))
        .order_by("-count")
    )

    return render(request, "aquarium/server_detail.html", {
        "server": server,
        "catches": catches,
        "daily_stats": daily_stats,
        "species_counts": species_counts,
    })


def fish_detail(request, pk):
    """Single fish/catch detail page."""
    catch = get_object_or_404(
        CaughtBot.objects.select_related("species", "server"), pk=pk
    )
    same_ip_catches = (
        CaughtBot.objects.filter(ip_hash=catch.ip_hash)
        .exclude(pk=pk)
        .select_related("species", "server")[:10]
    )

    return render(request, "aquarium/fish_detail.html", {
        "catch": catch,
        "same_ip_catches": same_ip_catches,
    })


def world_map(request):
    """World map showing attacks by country."""
    countries = CountryStats.objects.all()
    return render(request, "aquarium/world_map.html", {
        "countries": countries,
    })
