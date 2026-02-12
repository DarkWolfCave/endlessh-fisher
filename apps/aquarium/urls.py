"""Template-based URL routes for aquarium views."""

from django.urls import path

from . import views

app_name = "aquarium"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("aquarium/", views.aquarium, name="aquarium"),
    path("aquarium/<slug:slug>/", views.server_detail, name="server-detail"),
    path("fish/<int:pk>/", views.fish_detail, name="fish-detail"),
    path("map/", views.world_map, name="world-map"),
]
