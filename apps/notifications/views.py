"""Notification inbox view."""

from django.shortcuts import render

from .models import Notification


def inbox(request):
    """Notification inbox page with all notifications."""
    notifications = Notification.objects.all()[:100]
    unread_count = Notification.objects.filter(is_read=False).count()

    return render(request, "notifications/inbox.html", {
        "notifications": notifications,
        "unread_count": unread_count,
    })
