"""Aquarium template views - dashboard, aquarium, fish detail."""

import json

from django.core.cache import cache
from django.db.models import Count, Sum
from django.shortcuts import get_object_or_404, render

from apps.collector.influx_client import query_active_connections

from .models import CaughtBot, CountryStats, DailyStats, FishSpecies, Server
from .services import get_pond_fish


def _get_active_traps():
    """Get active trap count from cache or InfluxDB."""
    count = cache.get("endlessh:active_traps")
    if count is None:
        count = query_active_connections()
        cache.set("endlessh:active_traps", count, 60)
    return count


def dashboard(request):
    """Main dashboard with server ponds and live stats."""
    servers = Server.objects.filter(is_active=True)
    recent_catches = CaughtBot.objects.select_related("species", "server")[:10]
    total_score = CaughtBot.objects.aggregate(total=Sum("score"))["total"] or 0
    total_catches = CaughtBot.objects.count()
    active_traps = _get_active_traps()
    total_countries = CountryStats.objects.count()
    total_trapped = (
        CaughtBot.objects.aggregate(total=Sum("trapped_seconds"))["total"] or 0
    )

    # Live Pond data for initial render
    pond_data = get_pond_fish()

    return render(request, "aquarium/dashboard.html", {
        "servers": servers,
        "recent_catches": recent_catches,
        "total_score": total_score,
        "total_catches": total_catches,
        "active_traps": active_traps,
        "total_countries": total_countries,
        "total_trapped_seconds": total_trapped,
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
