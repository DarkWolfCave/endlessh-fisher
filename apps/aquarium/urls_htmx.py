"""HTMX partial URL routes."""

from django.urls import path

from . import views_htmx

app_name = "htmx"

urlpatterns = [
    path("stats-bar/", views_htmx.stats_bar, name="stats-bar"),
    path("activity-feed/", views_htmx.activity_feed, name="activity-feed"),
]
