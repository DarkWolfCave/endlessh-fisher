"""
Celery App Configuration for Endlessh Game.

Scheduled Tasks:
- Every 5 min:  Sync bot data from InfluxDB
- Every 1 hour: Aggregate daily statistics
- Every 10 min: Check achievement thresholds
- Daily 3 AM:   Full recalculate (consistency check)
"""

import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

app = Celery("endlessh_game")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(["apps.collector"])

# Worker settings
app.conf.update(
    task_track_started=True,
    task_time_limit=600,  # 10 min max per task
    task_soft_time_limit=540,  # Soft limit: 9 min
    result_expires=86400,  # Results expire after 24h
    worker_prefetch_multiplier=1,  # One task at a time (long-running)
    worker_max_tasks_per_child=100,  # Restart worker after 100 tasks
    task_default_retry_delay=60,  # 1 minute retry delay
    task_max_retries=3,
)

# Beat schedule (periodic tasks)
app.conf.beat_schedule = {
    "sync-bot-data": {
        "task": "apps.collector.tasks.sync_bot_data",
        "schedule": 300.0,  # every 5 minutes
    },
    "aggregate-daily-stats": {
        "task": "apps.collector.tasks.aggregate_daily_stats",
        "schedule": 3600.0,  # every 1 hour
    },
    "check-achievements": {
        "task": "apps.collector.tasks.check_achievements",
        "schedule": 600.0,  # every 10 minutes
    },
    "full-recalculate": {
        "task": "apps.collector.tasks.full_recalculate",
        "schedule": crontab(hour=3, minute=0),  # daily 3 AM
    },
}
