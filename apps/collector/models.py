"""Collector models - tracks sync state with InfluxDB."""

from django.db import models

from apps.core.models import TimeStampedModel


class SyncState(TimeStampedModel):
    """Tracks the last successful sync timestamp per server per metric type."""

    METRIC_CHOICES = [
        ("client_open", "Client Open Count"),
        ("trapped_time", "Trapped Time"),
        ("client_closed", "Client Closed Count"),
        ("sent_bytes", "Sent Bytes"),
    ]

    server_host = models.CharField(max_length=100, db_index=True)
    metric_type = models.CharField(max_length=50, choices=METRIC_CHOICES)
    last_sync_at = models.DateTimeField()
    records_synced = models.PositiveIntegerField(default=0)
    last_error = models.TextField(blank=True, default="")

    class Meta:
        unique_together = ["server_host", "metric_type"]
        indexes = [
            models.Index(
                fields=["server_host", "metric_type"],
                name="idx_sync_server_metric",
            ),
        ]

    def __str__(self):
        return f"{self.server_host} / {self.metric_type} (last: {self.last_sync_at})"
