"""Admin configuration for Aquarium models."""

from django.contrib import admin

from .models import CaughtBot, CountryStats, DailyStats, FishSpecies, Server


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
