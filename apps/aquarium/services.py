"""Aquarium business logic - fish classification, score calculation, live pond."""

import hashlib
import math
from datetime import timedelta

from django.core.cache import cache
from django.utils import timezone

from apps.aquarium.models import CaughtBot, FishSpecies, Server
from apps.collector.influx_client import query_active_bots, query_active_connections


def classify_fish(trapped_seconds: float) -> FishSpecies | None:
    """Classify a bot into a fish species based on trapped duration.

    Iterates species ordered by min_trapped_seconds (ascending).
    Returns the matching species or None if no match.
    """
    species_list = FishSpecies.objects.all().order_by("min_trapped_seconds")
    result = None
    for species in species_list:
        if trapped_seconds >= species.min_trapped_seconds:
            result = species
        else:
            break
    return result


def calculate_score(species: FishSpecies | None, trapped_seconds: float) -> int:
    """Calculate score: species.points + log2(trapped_seconds + 1)."""
    base_points = species.points if species else 1
    time_bonus = int(math.log2(trapped_seconds + 1))
    return base_points + time_bonus


# --- Fish emoji mapping ---

FISH_EMOJI = {
    "plankton": "\U0001F9A0",       # microbe
    "sardine": "\U0001F41F",        # fish
    "anchovy": "\U0001F41F",        # fish
    "trout": "\U0001F41F",          # fish
    "pike": "\U0001F988",           # shark
    "salmon": "\U0001F420",         # tropical fish
    "tuna": "\U0001F420",           # tropical fish
    "swordfish": "\U0001F42C",      # dolphin shape
    "marlin": "\U0001F42C",         # dolphin shape
    "whale-shark": "\U0001F40B",    # whale
    "kraken": "\U0001F419",         # octopus
    "leviathan": "\U0001F409",      # dragon
}


def _get_fish_emoji(species) -> str:
    """Map species to an emoji for pond visualization."""
    if not species:
        return FISH_EMOJI["plankton"]
    return FISH_EMOJI.get(species.slug, "\U0001F41F")


def _calculate_fish_size(trapped_seconds: float) -> str:
    """Calculate CSS size class based on trap time."""
    if trapped_seconds < 60:
        return "xs"
    if trapped_seconds < 300:
        return "sm"
    if trapped_seconds < 1800:
        return "md"
    if trapped_seconds < 14400:
        return "lg"
    if trapped_seconds < 86400:
        return "xl"
    return "xxl"


def _hash_ip(ip: str) -> str:
    """SHA256 hash of IP for DSGVO-compliant display."""
    return hashlib.sha256(ip.encode()).hexdigest()


def _compute_fish_position(fish_id: str) -> dict:
    """Compute deterministic position and animation for a fish.

    Uses SHA256 of fish_id to generate stable values that survive HTMX swaps.
    """
    h = int.from_bytes(hashlib.sha256(fish_id.encode()).digest()[:4], "big")
    return {
        "pos_top": 15 + (h % 55),
        "pos_left": 5 + ((h >> 8) % 85),
        "swim_dir": "right" if h % 2 == 0 else "left",
        "swim_speed": 12 + ((h >> 16) % 12),
    }


# --- Live Pond ---

def get_pond_fish() -> dict:
    """Build live pond data: currently active bots as fish.

    Returns dict with fish list, total_active count, and last_updated timestamp.
    Cached 12 seconds in Redis.
    """
    cache_key = "endlessh:live_pond"
    cached = cache.get(cache_key)
    if cached is not None:
        return cached

    active_bots = query_active_bots()
    servers = {s.host_identifier: s for s in Server.objects.filter(is_active=True)}
    species_list = list(FishSpecies.objects.order_by("min_trapped_seconds"))

    fish = []
    for bot in active_bots:
        host = bot["host"]
        if host not in servers:
            continue

        server = servers[host]
        trapped = bot["trapped_seconds"]

        # Classify using cached species list
        species = None
        for sp in species_list:
            if trapped >= sp.min_trapped_seconds:
                species = sp
            else:
                break

        country = (bot.get("country", "") or "")[:2].upper()
        ip_hash = _hash_ip(bot["ip"])

        fish_id = f"{host}:{ip_hash[:16]}"
        pos = _compute_fish_position(fish_id)

        fish.append({
            "id": fish_id,
            "ip_hash": ip_hash[:12],
            "country": country,
            "server_slug": server.slug,
            "server_name": server.name,
            "server_theme": server.pond_theme,
            "trapped_seconds": trapped,
            "last_seen": bot["last_seen"],
            "species_name": species.name_de if species else "Plankton",
            "species_slug": species.slug if species else "plankton",
            "species_emoji": _get_fish_emoji(species),
            "rarity": species.rarity if species else "common",
            "rarity_color": species.rarity_color if species else "#9CA3AF",
            "points": species.points if species else 1,
            "size": _calculate_fish_size(trapped),
            "pos_top": pos["pos_top"],
            "pos_left": pos["pos_left"],
            "swim_dir": pos["swim_dir"],
            "swim_speed": pos["swim_speed"],
        })

    # Sort by trapped_seconds desc (biggest fish first) and limit display
    fish.sort(key=lambda f: f["trapped_seconds"], reverse=True)

    # Use global active connections count (matches stats bar)
    total_active = query_active_connections()
    # Fall back to fish count if query fails
    if total_active < len(fish):
        total_active = len(fish)

    result = {
        "fish": fish[:50],
        "total_active": total_active,
        "last_updated": timezone.now().isoformat(),
    }
    cache.set(cache_key, result, 12)
    return result


# --- Rare Fish Alerts ---

def check_rare_fish_alerts() -> list[dict]:
    """Check for new rare fish catches (epic+) since last alert check.

    Returns at most 3 alert dicts. Uses Redis to avoid duplicate alerts.
    """
    cache_key = "endlessh:rare_alert_seen"
    seen_ids = set(cache.get(cache_key) or [])

    rare_rarities = ["epic", "legendary", "mythic"]
    recent_rare = (
        CaughtBot.objects
        .filter(
            species__rarity__in=rare_rarities,
            first_seen__gte=timezone.now() - timedelta(minutes=10),
        )
        .select_related("species", "server")
        .exclude(id__in=[s for s in seen_ids if isinstance(s, int)])
        .order_by("-trapped_seconds")[:3]
    )

    alerts = []
    new_seen = set(seen_ids)

    for catch in recent_rare:
        alerts.append({
            "id": catch.id,
            "species_name": catch.species.name_de,
            "species_emoji": _get_fish_emoji(catch.species),
            "rarity": catch.species.rarity,
            "rarity_color": catch.species.rarity_color,
            "server_name": catch.server.name,
            "trapped_seconds": catch.trapped_seconds,
            "country": catch.country_code,
            "ip_hash": catch.ip_hash[:8],
            "is_live": False,
        })
        new_seen.add(catch.id)

    # Also check live pond for fish that reached epic+ threshold
    pond_data = get_pond_fish()
    for fish in pond_data.get("fish", []):
        if fish["rarity"] in rare_rarities:
            alert_key = f"live:{fish['id']}"
            if alert_key not in seen_ids:
                alerts.append({
                    "id": alert_key,
                    "species_name": fish["species_name"],
                    "species_emoji": fish["species_emoji"],
                    "rarity": fish["rarity"],
                    "rarity_color": fish["rarity_color"],
                    "server_name": fish["server_name"],
                    "trapped_seconds": fish["trapped_seconds"],
                    "country": fish.get("country", ""),
                    "ip_hash": fish["ip_hash"],
                    "is_live": True,
                })
                new_seen.add(alert_key)

    if new_seen != seen_ids:
        cache.set(cache_key, list(new_seen), 1800)

    # Deduplicate by ip_hash (same bot on multiple servers → 1 alert)
    unique = {}
    for alert in alerts:
        h = alert["ip_hash"][:8]
        if h not in unique or alert["trapped_seconds"] > unique[h]["trapped_seconds"]:
            unique[h] = alert
    return list(unique.values())[:3]
