"""URL configuration for Endlessh Fisher."""

import os

from django.contrib import admin
from django.urls import include, path

admin_url = os.environ.get("ADMIN_URL", "admin/")

urlpatterns = [
    path(admin_url, admin.site.urls),
    # API endpoints
    path("api/v1/", include("apps.aquarium.api.urls")),
    path("api/v1/achievements/", include("apps.achievements.api.urls")),
    # HTMX partials
    path("htmx/", include("apps.aquarium.urls_htmx")),
    # Template views
    path("", include("apps.aquarium.urls")),
    path("achievements/", include("apps.achievements.urls")),
]
