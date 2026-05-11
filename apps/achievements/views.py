"""Achievement template views."""

from django.shortcuts import get_object_or_404, render

from .models import Achievement, AchievementCategory, UnlockedAchievement


def gallery(request):
    """Achievement gallery with all categories and unlock status."""
    categories = AchievementCategory.objects.prefetch_related(
        "achievements", "achievements__unlock_record"
    ).all()

    total_achievements = Achievement.objects.filter(is_active=True).count()
    unlocked_count = UnlockedAchievement.objects.count()
    total_points = sum(
        ua.achievement.points for ua in UnlockedAchievement.objects.select_related("achievement")
    )

    return render(request, "achievements/gallery.html", {
        "categories": categories,
        "total_achievements": total_achievements,
        "unlocked_count": unlocked_count,
        "total_points": total_points,
    })


def achievement_detail(request, slug):
    """Single achievement detail with progress."""
    achievement = get_object_or_404(
        Achievement.objects.select_related("category"), slug=slug
    )
    return render(request, "achievements/detail.html", {
        "achievement": achievement,
    })
