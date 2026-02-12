"""DRF API URL routes for achievements."""

from django.urls import path

from . import views

app_name = "achievements-api"

urlpatterns = [
    path("", views.achievement_list, name="list"),
    path("pending/", views.pending_toasts, name="pending"),
    path("ack/", views.acknowledge_toast, name="ack"),
]
