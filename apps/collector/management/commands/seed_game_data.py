"""Management command to seed game content (fish, treasures, tips, achievements)."""

from django.core.management.base import BaseCommand
from django.db import transaction

from apps.achievements.models import Achievement, AchievementCategory
from apps.aquarium.models import ChallengeTemplate, FishSpecies, SecurityTip, TreasureType
from apps.aquarium.seed_data import (
    ACHIEVEMENT_CATEGORIES,
    ACHIEVEMENTS,
    CHALLENGE_TEMPLATES,
    FISH_SPECIES,
    SECURITY_TIPS,
    TREASURE_TYPES,
)


class Command(BaseCommand):
    help = "Seed universal game content (fish, treasures, tips, challenges, achievements)"

    def handle(self, *args, **options):
        with transaction.atomic():
            self._seed_fish_species()
            self._seed_security_tips()
            self._seed_treasure_types()
            self._seed_challenge_templates()
            self._seed_achievement_categories()
            self._seed_achievements()

        self.stdout.write(self.style.SUCCESS("Game data seeded successfully!"))

    def _seed_fish_species(self):
        created = 0
        for data in FISH_SPECIES:
            _, was_created = FishSpecies.objects.update_or_create(
                slug=data["slug"],
                defaults=data,
            )
            if was_created:
                created += 1
        self.stdout.write(f"  Fish species: {created} created, {len(FISH_SPECIES)} total")

    def _seed_achievement_categories(self):
        created = 0
        for data in ACHIEVEMENT_CATEGORIES:
            _, was_created = AchievementCategory.objects.update_or_create(
                slug=data["slug"],
                defaults=data,
            )
            if was_created:
                created += 1
        self.stdout.write(
            f"  Achievement categories: {created} created, "
            f"{len(ACHIEVEMENT_CATEGORIES)} total"
        )

    def _seed_security_tips(self):
        created = 0
        for data in SECURITY_TIPS:
            _, was_created = SecurityTip.objects.update_or_create(
                slug=data["slug"],
                defaults=data,
            )
            if was_created:
                created += 1
        self.stdout.write(
            f"  Security tips: {created} created, {len(SECURITY_TIPS)} total"
        )

    def _seed_treasure_types(self):
        created = 0
        for data in TREASURE_TYPES:
            _, was_created = TreasureType.objects.update_or_create(
                slug=data["slug"],
                defaults=data,
            )
            if was_created:
                created += 1
        self.stdout.write(
            f"  Treasure types: {created} created, {len(TREASURE_TYPES)} total"
        )

    def _seed_challenge_templates(self):
        created = 0
        for data in CHALLENGE_TEMPLATES:
            _, was_created = ChallengeTemplate.objects.update_or_create(
                slug=data["slug"],
                defaults=data,
            )
            if was_created:
                created += 1
        self.stdout.write(
            f"  Challenge templates: {created} created, "
            f"{len(CHALLENGE_TEMPLATES)} total"
        )

    def _seed_achievements(self):
        created = 0
        for data in ACHIEVEMENTS:
            category_slug = data.pop("category")
            category = AchievementCategory.objects.get(slug=category_slug)
            _, was_created = Achievement.objects.update_or_create(
                slug=data["slug"],
                defaults={**data, "category": category},
            )
            if was_created:
                created += 1
            data["category"] = category_slug  # Restore for idempotency
        self.stdout.write(
            f"  Achievements: {created} created, {len(ACHIEVEMENTS)} total"
        )
