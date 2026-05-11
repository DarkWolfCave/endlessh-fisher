"""DRF API views for achievements."""

from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.achievements.models import Achievement, UnlockedAchievement


@api_view(["GET"])
def achievement_list(request):
    """All achievements with unlock status."""
    achievements = Achievement.objects.filter(is_active=True).select_related(
        "category", "unlock_record"
    )
    data = []
    for a in achievements:
        unlock = getattr(a, "unlock_record", None)
        data.append({
            "slug": a.slug,
            "name_de": a.name_de,
            "description_de": a.description_de,
            "category": a.category.name_de,
            "rarity": a.rarity,
            "points": a.points,
            "is_secret": a.is_secret,
            "unlocked": unlock is not None,
            "unlocked_at": unlock.unlocked_at if unlock else None,
        })
    return Response(data)


@api_view(["GET"])
def pending_toasts(request):
    """Unnotified achievement unlocks for toast notifications."""
    pending = UnlockedAchievement.objects.filter(notified=False).select_related(
        "achievement", "achievement__category"
    )
    data = [
        {
            "slug": ua.achievement.slug,
            "name_de": ua.achievement.name_de,
            "description_de": ua.achievement.description_de,
            "rarity": ua.achievement.rarity,
            "points": ua.achievement.points,
            "category": ua.achievement.category.name_de,
            "unlocked_at": ua.unlocked_at,
        }
        for ua in pending
    ]
    return Response(data)


@api_view(["POST"])
def acknowledge_toast(request):
    """Mark achievement notification as seen."""
    slug = request.data.get("slug")
    if not slug:
        return Response({"error": "slug required"}, status=400)

    updated = UnlockedAchievement.objects.filter(
        achievement__slug=slug, notified=False
    ).update(notified=True)

    return Response({"acknowledged": updated > 0})
