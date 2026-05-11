"""Template-based URL routes for achievements."""

from django.urls import path

from . import views

app_name = "achievements"

urlpatterns = [
    path("", views.gallery, name="gallery"),
    path("<slug:slug>/", views.achievement_detail, name="detail"),
]
