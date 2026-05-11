"""Template-based URL routes for aquarium views."""

from django.urls import path
from django.views.generic import RedirectView

from . import views

app_name = "aquarium"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("lexikon/", views.species_dex, name="species-dex"),
    path("bestenliste/", views.bestenliste, name="bestenliste"),
    path("server/<slug:slug>/", views.server_detail, name="server-detail"),
    path("fish/<int:pk>/", views.fish_detail, name="fish-detail"),
    path("schatzkammer/", views.schatzkammer, name="schatzkammer"),
    path("map/", views.world_map, name="world-map"),
    # Legacy redirect
    path("aquarium/", RedirectView.as_view(pattern_name="aquarium:species-dex", permanent=True)),
]
