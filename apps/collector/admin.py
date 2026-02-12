"""Admin configuration for Collector models."""

from django.contrib import admin

from .models import SyncState


@admin.register(SyncState)
class SyncStateAdmin(admin.ModelAdmin):
    list_display = ["server_host", "metric_type", "last_sync_at", "records_synced"]
    list_filter = ["metric_type"]
    ordering = ["-last_sync_at"]
