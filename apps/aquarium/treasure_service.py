"""Treasure spawning and collection logic for the live pond."""

import hashlib
import json
import random
import time
import uuid

from django.core.cache import cache
from django.utils import timezone
from django.utils.html import strip_tags

from django.conf import settings

from .models import CollectedTreasure, SecurityTip, TreasureType


def _localized(obj, field):
    """Return localized field value (same logic as |lang template filter)."""
    if settings.GAME_LANGUAGE == "de":
        val = getattr(obj, f"{field}_de", None)
        if val:
            return val
    val = getattr(obj, field, None)
    if val:
        return val
    return getattr(obj, f"{field}_de", "")

# Treasures expire after 90s if not collected (urgency!)
TREASURE_MAX_AGE_SECONDS = 90
# 12% chance to spawn a new treasure per pond poll cycle (~1 every 3-5 min)
TREASURE_SPAWN_CHANCE = 0.12
# Max 2 treasures visible at once (feels more special)
TREASURE_MAX_ACTIVE = 2
# Minimum 3 minutes between spawns
TREASURE_SPAWN_COOLDOWN = 180
# Cache keys
_CACHE_KEY = "endlessh:active_treasures"
_CACHE_TTL = 30  # Slightly longer than pond poll (15s)
_COOLDOWN_KEY = "endlessh:treasure_cooldown"
_SPAWN_COOLDOWN_KEY = "endlessh:treasure_spawn_cd"

# --- Pond Activity Tracker ---
# 7-day rolling window histogram for adaptive treasure thresholds.
_ACTIVITY_KEY = "endlessh:pond_activity"
_ACTIVITY_TTL = 7 * 24 * 3600  # 7 days
_ACTIVITY_WARMUP = 200  # Samples before percentiles are reliable (~50 min)


def record_pond_activity(fish_count: int) -> None:
    """Record current fish count into the rolling histogram.

    Called on every pond poll (~15s). Stores a compact histogram
    in Redis: {"buckets": {"0": 500, "3": 120, ...}, "total": 5000,
    "ring": [...last 40320 timestamps+values for 7d rolling window...]}
    """
    data = cache.get(_ACTIVITY_KEY)
    now = time.time()
    if not data:
        data = {"buckets": {}, "total": 0, "ring": []}

    bucket_key = str(int(fish_count))
    data["buckets"][bucket_key] = data["buckets"].get(bucket_key, 0) + 1
    data["total"] = data.get("total", 0) + 1
    data["ring"].append((now, int(fish_count)))

    # Prune entries older than 7 days from ring + adjust buckets
    cutoff = now - _ACTIVITY_TTL
    expired = []
    kept = []
    for ts, val in data["ring"]:
        if ts < cutoff:
            expired.append(val)
        else:
            kept.append((ts, val))

    for val in expired:
        bk = str(val)
        data["buckets"][bk] = data["buckets"].get(bk, 1) - 1
        if data["buckets"][bk] <= 0:
            del data["buckets"][bk]
        data["total"] = max(0, data["total"] - 1)
    data["ring"] = kept

    cache.set(_ACTIVITY_KEY, data, _ACTIVITY_TTL)


def get_pond_percentile(fish_count: int) -> int:
    """Return the percentile (0-100) of the given fish count.

    During warmup (<200 samples), returns -1 to signal that callers
    should use fallback logic.
    """
    data = cache.get(_ACTIVITY_KEY)
    if not data or data.get("total", 0) < _ACTIVITY_WARMUP:
        return -1  # Warmup phase

    total = data["total"]
    below = 0
    for bucket_key, count in data["buckets"].items():
        if int(bucket_key) < fish_count:
            below += count

    return min(100, int(below * 100 / total))


def _compute_treasure_position(treasure_id: str) -> dict:
    """Deterministic position for a treasure (same approach as fish)."""
    h = int.from_bytes(hashlib.sha256(treasure_id.encode()).digest()[:4], "big")
    return {
        "pos_top": 20 + (h % 50),  # 20-70%
        "pos_left": 10 + ((h >> 8) % 75),  # 10-85%
    }


def _select_security_tip(rarity: str) -> SecurityTip | None:
    """Select a random security tip, preferring unseen tips of matching rarity."""
    seen_ids = set(
        CollectedTreasure.objects.exclude(security_tip=None)
        .values_list("security_tip_id", flat=True)
    )
    # 1st: unseen tip of matching rarity
    candidates = SecurityTip.objects.filter(rarity=rarity).exclude(id__in=seen_ids)
    if not candidates.exists():
        # 2nd: any unseen tip
        candidates = SecurityTip.objects.exclude(id__in=seen_ids)
    if not candidates.exists():
        # All seen — recycle a tip of matching rarity
        candidates = SecurityTip.objects.filter(rarity=rarity)
    if not candidates.exists():
        candidates = SecurityTip.objects.all()
    if not candidates.exists():
        return None
    return candidates.order_by("?").first()


def _select_treasure_type(active_fish_count: int) -> TreasureType | None:
    """Weighted random selection based on adaptive pond activity percentile.

    Uses a 7-day rolling histogram to determine how unusual the current
    fish count is for THIS setup. During warmup (<200 samples), all
    treasures are eligible if at least 1 fish is active (spawn_weight
    still limits rare drops).
    """
    percentile = get_pond_percentile(active_fish_count)

    if percentile == -1:
        # Warmup phase: all treasures eligible, spawn_weight handles rarity
        eligible = list(TreasureType.objects.all())
    else:
        eligible = list(
            TreasureType.objects.filter(min_pond_percentile__lte=percentile)
        )

    if not eligible:
        return None
    weights = [t.spawn_weight for t in eligible]
    return random.choices(eligible, weights=weights, k=1)[0]


def get_active_treasures(active_fish_count: int) -> list[dict]:
    """Get or spawn active treasures for the pond.

    Manages treasure lifecycle in Redis cache.
    Called from the live_pond HTMX view.
    """
    # Track pond activity for adaptive treasure thresholds
    record_pond_activity(active_fish_count)

    now = timezone.now()
    treasures = cache.get(_CACHE_KEY) or []

    # Expire old treasures
    treasures = [
        t for t in treasures
        if (now - timezone.datetime.fromisoformat(t["spawned_at"])).total_seconds()
        < TREASURE_MAX_AGE_SECONDS
    ]

    # Remove already-collected treasures
    if treasures:
        collected_ids = set(
            CollectedTreasure.objects.filter(
                pond_treasure_id__in=[t["id"] for t in treasures]
            ).values_list("pond_treasure_id", flat=True)
        )
        treasures = [t for t in treasures if t["id"] not in collected_ids]

    # Maybe spawn a new treasure (respects cooldown between spawns)
    spawn_on_cooldown = cache.get(_SPAWN_COOLDOWN_KEY)
    if (
        len(treasures) < TREASURE_MAX_ACTIVE
        and active_fish_count > 0
        and not spawn_on_cooldown
        and random.random() < TREASURE_SPAWN_CHANCE
    ):
        treasure_type = _select_treasure_type(active_fish_count)
        if treasure_type:
            tid = uuid.uuid4().hex[:16]
            pos = _compute_treasure_position(tid)
            treasures.append({
                "id": tid,
                "type_slug": treasure_type.slug,
                "type_name": _localized(treasure_type, "name"),
                "emoji": treasure_type.emoji,
                "rarity": treasure_type.rarity,
                "rarity_color": treasure_type.rarity_color,
                "points": treasure_type.points,
                "pos_top": pos["pos_top"],
                "pos_left": pos["pos_left"],
                "spawned_at": now.isoformat(),
            })
            # Set spawn cooldown so next treasure can't appear too quickly
            cache.set(_SPAWN_COOLDOWN_KEY, True, TREASURE_SPAWN_COOLDOWN)

    cache.set(_CACHE_KEY, treasures, _CACHE_TTL)
    return treasures


def collect_treasure(pond_treasure_id: str) -> dict | None:
    """Attempt to collect a treasure.

    Returns collection details on success, None if unavailable.
    """
    # Sanitize input
    pond_treasure_id = strip_tags(str(pond_treasure_id))[:64]
    if not pond_treasure_id:
        return None

    now = timezone.now()
    treasures = cache.get(_CACHE_KEY) or []

    # Find treasure in active list
    target = None
    for t in treasures:
        if t["id"] == pond_treasure_id:
            target = t
            break

    if not target:
        return None

    # Double-collect guard (DB unique constraint is final safety net)
    if CollectedTreasure.objects.filter(pond_treasure_id=pond_treasure_id).exists():
        return None

    # Rate limit: max 1 collection per 2 seconds
    if cache.get(_COOLDOWN_KEY):
        return None
    cache.set(_COOLDOWN_KEY, True, 2)

    # Get active fish count from pond cache
    pond_data = cache.get("endlessh:live_pond")
    active_fish_count = len(pond_data.get("fish", [])) if pond_data else 0

    # Create record
    try:
        treasure_type = TreasureType.objects.get(slug=target["type_slug"])
    except TreasureType.DoesNotExist:
        return None

    # Select a security tip (prefer unseen, matching rarity)
    tip = _select_security_tip(treasure_type.rarity)

    CollectedTreasure.objects.create(
        treasure_type=treasure_type,
        security_tip=tip,
        pond_treasure_id=pond_treasure_id,
        collected_at=now,
        active_fish_count=active_fish_count,
        points_awarded=treasure_type.points,
    )

    # Remove from active treasures in cache
    treasures = [t for t in treasures if t["id"] != pond_treasure_id]
    cache.set(_CACHE_KEY, treasures, _CACHE_TTL)

    result = {
        "treasure_name": _localized(treasure_type, "name"),
        "emoji": treasure_type.emoji,
        "rarity": treasure_type.rarity,
        "rarity_color": treasure_type.rarity_color,
        "points": treasure_type.points,
    }

    if tip:
        result["tip"] = {
            "title": _localized(tip, "title"),
            "content": _localized(tip, "content"),
            "category": tip.category,
            "tip_emoji": tip.emoji,
            "source_url": tip.source_url,
            "source_label": _localized(tip, "source_label"),
            "rarity": tip.rarity,
        }

    return result
