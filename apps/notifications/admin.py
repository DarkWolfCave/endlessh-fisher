"""Notification admin configuration."""

from django.contrib import admin

from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = [
        "title_de", "category", "rarity", "is_read", "toast_shown", "created_at",
    ]
    list_filter = ["category", "is_read", "toast_shown"]
    ordering = ["-created_at"]
    search_fields = ["title_de", "message_de"]
