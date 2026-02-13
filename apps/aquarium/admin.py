"""Admin configuration for Aquarium models."""

from django.contrib import admin

from .models import (
    CaughtBot, ChallengeTemplate, CollectedTreasure, CountryStats,
    DailyChallenge, DailyStats, FishSpecies, SecurityTip, Server, TreasureType,
)


@admin.register(SecurityTip)
class SecurityTipAdmin(admin.ModelAdmin):
    list_display = ["title_de", "slug", "emoji", "rarity", "category", "sort_order"]
    list_filter = ["rarity", "category"]
    ordering = ["rarity", "sort_order"]
    search_fields = ["title_de", "content_de"]


@admin.register(FishSpecies)
class FishSpeciesAdmin(admin.ModelAdmin):
    list_display = ["name_de", "slug", "rarity", "min_trapped_seconds", "points", "sort_order"]
    list_filter = ["rarity"]
    ordering = ["sort_order"]


@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ["name", "host_identifier", "is_active", "total_catches", "pond_theme"]
    list_filter = ["is_active", "pond_theme"]


@admin.register(CaughtBot)
class CaughtBotAdmin(admin.ModelAdmin):
    list_display = [
        "ip_hash_short", "species", "server", "country_code",
        "trapped_seconds", "score", "first_seen", "is_active",
    ]
    list_filter = ["server", "species", "is_active", "country_code"]
    search_fields = ["ip_hash", "country_name"]
    ordering = ["-first_seen"]

    @admin.display(description="IP Hash")
    def ip_hash_short(self, obj):
        return f"{obj.ip_hash[:12]}..."


@admin.register(DailyStats)
class DailyStatsAdmin(admin.ModelAdmin):
    list_display = ["date", "server", "new_catches", "unique_ips", "longest_trap_seconds"]
    list_filter = ["server"]
    ordering = ["-date"]


@admin.register(CountryStats)
class CountryStatsAdmin(admin.ModelAdmin):
    list_display = ["country_code", "country_name", "total_catches", "unique_ips"]
    ordering = ["-total_catches"]


@admin.register(TreasureType)
class TreasureTypeAdmin(admin.ModelAdmin):
    list_display = ["name_de", "slug", "emoji", "rarity", "points", "spawn_weight", "sort_order"]
    list_filter = ["rarity"]
    ordering = ["sort_order"]


@admin.register(CollectedTreasure)
class CollectedTreasureAdmin(admin.ModelAdmin):
    list_display = ["treasure_type", "pond_treasure_id", "collected_at", "points_awarded"]
    list_filter = ["treasure_type"]
    ordering = ["-collected_at"]


@admin.register(ChallengeTemplate)
class ChallengeTemplateAdmin(admin.ModelAdmin):
    list_display = ["name_de", "slug", "metric", "difficulty", "threshold_min", "threshold_max", "reward_points"]
    list_filter = ["difficulty", "metric"]
    ordering = ["difficulty", "slug"]


@admin.register(DailyChallenge)
class DailyChallengeAdmin(admin.ModelAdmin):
    list_display = ["date", "template", "threshold", "current_value", "is_completed", "reward_points"]
    list_filter = ["is_completed", "date"]
    ordering = ["-date"]
