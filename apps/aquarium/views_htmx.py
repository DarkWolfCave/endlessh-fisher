"""HTMX partial views for live-updating dashboard components."""

import ipaddress
import json

from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import render
from django.utils.html import strip_tags
from django.views.decorators.http import require_POST

from .models import CaughtBot
from .services import check_rare_fish_alerts, get_pond_fish
from .treasure_service import collect_treasure, get_active_treasures
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
    treasures = get_active_treasures(pond_data["total_active"])
    return render(request, "components/live_pond.html", {
        "fish_list": pond_data["fish"],
        "total_active": pond_data["total_active"],
        "last_updated": pond_data["last_updated"],
        "fish_json": json.dumps(pond_data["fish"]),
        "treasures": treasures,
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


@require_POST
def collect_treasure_view(request):
    """Collect a treasure from the pond. Returns JSON."""
    treasure_id = strip_tags(request.POST.get("treasure_id", ""))[:64]
    if not treasure_id:
        return JsonResponse({"error": "Missing treasure_id"}, status=400)

    result = collect_treasure(treasure_id)
    if result is None:
        return JsonResponse({"error": "Treasure not available"}, status=404)

    # Evaluate daily challenges immediately so progress updates on next poll
    from .challenge_service import evaluate_daily_challenges
    evaluate_daily_challenges()

    response = JsonResponse({"success": True, **result})
    response["HX-Trigger"] = "challenges-updated"
    return response


def daily_challenges(request):
    """Daily challenges widget - polled every 60s via HTMX."""
    from .challenge_service import get_today_challenges

    challenges = get_today_challenges()
    return render(request, "components/daily_challenges.html", {
        "challenges": challenges,
    })


def ip_lookup(request):
    """IP intelligence lookup — returns HTMX partial or JSON.

    Only available when SHOW_REAL_IP=true.
    Rate-limited to 10 lookups per minute.
    """
    if not settings.SHOW_REAL_IP:
        return HttpResponseForbidden("IP lookup disabled")

    ip = strip_tags(request.GET.get("ip", ""))[:45]
    if not ip:
        return render(request, "components/ip_lookup_result.html", {
            "error": "missing_ip",
        })

    # Validate IP format
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return render(request, "components/ip_lookup_result.html", {
            "error": "invalid_ip",
        })

    # Rate limit: 10 lookups per minute
    rate_key = "endlessh:ip_lookup_rate"
    count = cache.get(rate_key, 0)
    if count >= 10:
        return render(request, "components/ip_lookup_result.html", {
            "error": "rate_limited",
        })
    cache.set(rate_key, count + 1, 60)

    from .ip_lookup_service import lookup_ip
    result = lookup_ip(ip)

    # Log lookup for achievement tracking (only for public IPs with data)
    if not result.get("error"):
        _log_ip_lookup(result)

    # Return JSON if requested (for live pond modal)
    if request.headers.get("Accept") == "application/json":
        return JsonResponse(result)

    return render(request, "components/ip_lookup_result.html", {
        "result": result,
    })


def _log_ip_lookup(result: dict) -> None:
    """Log IP lookup result for achievement evaluation."""
    from .models import IPLookupLog

    shodan = result.get("shodan", {})
    abuse = result.get("abuseipdb", {})

    IPLookupLog.objects.update_or_create(
        ip_address=result["ip"],
        defaults={
            "abuse_score": abuse.get("abuse_score", 0) if abuse.get("available") else 0,
            "is_tor": abuse.get("is_tor", False) if abuse.get("available") else False,
            "has_vulns": bool(shodan.get("vulns")) if shodan.get("available") else False,
            "has_dangerous_ports": bool(shodan.get("dangerous_ports")) if shodan.get("available") else False,
        },
    )
