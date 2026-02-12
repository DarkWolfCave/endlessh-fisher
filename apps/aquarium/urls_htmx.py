"""HTMX partial URL routes."""

from django.urls import path

from . import views_htmx

app_name = "htmx"

urlpatterns = [
    path("stats-bar/", views_htmx.stats_bar, name="stats-bar"),
    path("activity-feed/", views_htmx.activity_feed, name="activity-feed"),
    path("live-pond/", views_htmx.live_pond, name="live-pond"),
    path("catch-ticker/", views_htmx.catch_ticker, name="catch-ticker"),
    path("rare-alert/", views_htmx.rare_alert, name="rare-alert"),
]
