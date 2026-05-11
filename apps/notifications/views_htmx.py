"""HTMX partial views for notification system."""

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.html import strip_tags
from django.views.decorators.http import require_POST

from .models import Notification
from .services import (
    delete_all,
    delete_notification,
    get_pending_toasts,
    get_unread_count,
    mark_all_read,
    mark_read,
    mark_toasts_shown,
)


def notification_badge(request):
    """Unread count badge for header nav - polled every 30s."""
    count = get_unread_count()
    return render(request, "components/notification_badge.html", {
        "unread_count": count,
    })


def notification_toasts(request):
    """Pending toast notifications - polled every 30s.

    Returns toast HTML and marks them as shown.
    """
    toasts = get_pending_toasts(limit=3)
    if toasts:
        mark_toasts_shown([t.id for t in toasts])
    return render(request, "components/notification_toasts.html", {
        "toasts": toasts,
    })


@require_POST
def mark_notification_read(request):
    """Mark single notification as read. Returns updated inbox row."""
    notif_id = strip_tags(request.POST.get("notification_id", ""))[:10]
    try:
        notif_id = int(notif_id)
    except (ValueError, TypeError):
        return HttpResponse(status=400)

    mark_read(notif_id)
    notif = Notification.objects.filter(id=notif_id).first()
    if notif:
        return render(request, "components/notification_row.html", {
            "notification": notif,
        })
    return HttpResponse(status=404)


@require_POST
def mark_all_notifications_read(request):
    """Mark all notifications as read. Returns updated inbox list."""
    mark_all_read()
    notifications = Notification.objects.all()[:100]
    return render(request, "components/notification_list.html", {
        "notifications": notifications,
    })


@require_POST
def delete_notification_view(request):
    """Delete a single notification."""
    notif_id = strip_tags(request.POST.get("notification_id", ""))[:10]
    try:
        notif_id = int(notif_id)
    except (ValueError, TypeError):
        return HttpResponse(status=400)

    delete_notification(notif_id)
    # Empty response removes the row via hx-swap="outerHTML"
    return HttpResponse("")


@require_POST
def delete_all_notifications_view(request):
    """Delete all notifications. Returns updated (empty) inbox list."""
    delete_all()
    return render(request, "components/notification_list.html", {
        "notifications": [],
    })
