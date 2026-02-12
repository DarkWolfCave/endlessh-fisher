"""DRF API URL routes for aquarium."""

from django.urls import path

from . import views

app_name = "aquarium-api"

urlpatterns = [
    path("dashboard/", views.dashboard_stats, name="dashboard"),
    path("catches/", views.CaughtBotListView.as_view(), name="catches-list"),
    path("catches/latest/", views.latest_catches, name="catches-latest"),
    path("catches/<int:pk>/", views.CaughtBotDetailView.as_view(), name="catch-detail"),
    path("servers/", views.ServerListView.as_view(), name="servers-list"),
    path("servers/<slug:slug>/", views.ServerDetailView.as_view(), name="server-detail"),
    path("species/", views.FishSpeciesListView.as_view(), name="species-list"),
    path("stats/daily/", views.daily_stats, name="daily-stats"),
    path("stats/countries/", views.country_stats, name="country-stats"),
    path("health/", views.health_check, name="health"),
]
