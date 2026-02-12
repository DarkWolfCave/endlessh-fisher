"""Admin configuration for Achievement models."""

from django.contrib import admin

from .models import Achievement, AchievementCategory, UnlockedAchievement


@admin.register(AchievementCategory)
class AchievementCategoryAdmin(admin.ModelAdmin):
    list_display = ["name_de", "slug", "icon", "sort_order"]
    ordering = ["sort_order"]


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = [
        "name_de", "category", "metric", "threshold",
        "rarity", "points", "is_active", "is_secret",
    ]
    list_filter = ["category", "rarity", "metric", "is_active", "is_secret"]
    ordering = ["category", "sort_order"]


@admin.register(UnlockedAchievement)
class UnlockedAchievementAdmin(admin.ModelAdmin):
    list_display = ["achievement", "unlocked_at", "current_value", "notified"]
    list_filter = ["notified"]
    ordering = ["-unlocked_at"]
