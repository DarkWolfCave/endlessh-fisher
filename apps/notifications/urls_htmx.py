"""HTMX partial URL routes for notifications."""

from django.urls import path

from . import views_htmx

app_name = "notifications-htmx"

urlpatterns = [
    path("badge/", views_htmx.notification_badge, name="badge"),
    path("toasts/", views_htmx.notification_toasts, name="toasts"),
    path("mark-read/", views_htmx.mark_notification_read, name="mark-read"),
    path("mark-all-read/", views_htmx.mark_all_notifications_read, name="mark-all-read"),
    path("delete/", views_htmx.delete_notification_view, name="delete"),
    path("delete-all/", views_htmx.delete_all_notifications_view, name="delete-all"),
]
