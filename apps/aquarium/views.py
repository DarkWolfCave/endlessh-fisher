"""Aquarium template views - dashboard, species dex, bestenliste, fish detail."""

import json

from django.core.cache import cache
from django.db.models import Count, Max, Min, OuterRef, Subquery, Sum
from django.shortcuts import get_object_or_404, render

from .challenge_service import get_today_challenges
from .models import CaughtBot, CollectedTreasure, CountryStats, DailyStats, FishSpecies, SecurityTip, Server
from .services import get_pond_fish
from .treasure_service import get_active_treasures

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
    treasures = get_active_treasures(pond_data["total_active"])
    challenges = get_today_challenges()

    return render(request, "aquarium/dashboard.html", {
        "servers": servers,
        "recent_catches": recent_catches,
        "active_traps": pond_data["total_active"],
        **stats,
        "fish_list": pond_data["fish"],
        "total_active": pond_data["total_active"],
        "last_updated": pond_data["last_updated"],
        "fish_json": json.dumps(pond_data["fish"]),
        "treasures": treasures,
        "challenges": challenges,
    })


def species_dex(request):
    """Species Dex - Pokédex-style overview of all 12 fish species."""
    cache_key = "endlessh:species_dex"
    species_list = cache.get(cache_key)
    if species_list is None:
        species_list = list(
            FishSpecies.objects.all()
            .annotate(
                catch_count=Count("catches"),
                best_trapped=Max("catches__trapped_seconds"),
                best_score=Max("catches__score"),
                first_caught=Min("catches__first_seen"),
            )
            .order_by("sort_order")
        )
        cache.set(cache_key, species_list, _STATS_CACHE_TTL)
    return render(request, "aquarium/species_dex.html", {
        "species_list": species_list,
    })


def bestenliste(request):
    """Leaderboard - top catches by trap time, score, and per-species records."""
    cache_key = "endlessh:bestenliste"
    cached = cache.get(cache_key)
    if cached is not None:
        return render(request, "aquarium/bestenliste.html", cached)

    longest = (
        CaughtBot.objects.select_related("species", "server")
        .order_by("-trapped_seconds")[:10]
    )
    highest_score = (
        CaughtBot.objects.select_related("species", "server")
        .order_by("-score")[:10]
    )
    # Best catch per species — single query with Subquery instead of N+1 loop
    best_pk_subquery = Subquery(
        CaughtBot.objects.filter(species_id=OuterRef("pk"))
        .order_by("-trapped_seconds")
        .values("pk")[:1]
    )
    best_pks = (
        FishSpecies.objects.annotate(best_pk=best_pk_subquery)
        .exclude(best_pk=None)
        .values_list("best_pk", flat=True)
    )
    best_catches = {
        c.species_id: c
        for c in CaughtBot.objects.filter(pk__in=best_pks)
        .select_related("species", "server")
    }
    species_records = [
        {"species": c.species, "record": c}
        for c in sorted(best_catches.values(), key=lambda c: c.species.sort_order)
    ]

    # Force evaluation so results are cacheable
    context = {
        "longest": list(longest),
        "highest_score": list(highest_score),
        "species_records": species_records,
    }
    cache.set(cache_key, context, _STATS_CACHE_TTL)
    return render(request, "aquarium/bestenliste.html", context)


def server_detail(request, slug):
    """Per-server pond view."""
    server = get_object_or_404(Server, slug=slug)
    catches = CaughtBot.objects.filter(server=server).select_related("species")[:50]
    daily_stats = DailyStats.objects.filter(server=server)[:30]
    species_counts = (
        CaughtBot.objects.filter(server=server)
        .values("species__name", "species__name_de", "species__rarity_color", "species__css_class")
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


def schatzkammer(request):
    """Treasure vault - collected treasures with security tips."""
    collections = (
        CollectedTreasure.objects
        .select_related("treasure_type", "security_tip")
        .order_by("-collected_at")
    )
    agg = CollectedTreasure.objects.aggregate(
        total_points=Sum("points_awarded"),
        total_collected=Count("id"),
    )
    unique_tips = (
        CollectedTreasure.objects.exclude(security_tip=None)
        .values("security_tip_id").distinct().count()
    )
    total_tips = SecurityTip.objects.count()

    return render(request, "aquarium/schatzkammer.html", {
        "collections": collections,
        "total_collected": agg["total_collected"],
        "unique_tips": unique_tips,
        "total_tips": total_tips,
        "total_points": agg["total_points"] or 0,
    })


def world_map(request):
    """World map showing attacks by country."""
    countries = CountryStats.objects.all()
    return render(request, "aquarium/world_map.html", {
        "countries": countries,
    })
