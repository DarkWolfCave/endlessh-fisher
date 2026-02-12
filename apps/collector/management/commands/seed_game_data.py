"""Management command to seed fish species, servers, and achievements."""

from django.core.management.base import BaseCommand
from django.db import transaction

from apps.achievements.models import Achievement, AchievementCategory
from apps.aquarium.models import FishSpecies, Server
from apps.aquarium.seed_data import (
    ACHIEVEMENT_CATEGORIES,
    ACHIEVEMENTS,
    FISH_SPECIES,
    SERVERS,
)


class Command(BaseCommand):
    help = "Seed game data: fish species, servers, achievement categories, and achievements"

    def handle(self, *args, **options):
        with transaction.atomic():
            self._seed_fish_species()
            self._seed_servers()
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

    def _seed_servers(self):
        created = 0
        for data in SERVERS:
            _, was_created = Server.objects.update_or_create(
                slug=data["slug"],
                defaults=data,
            )
            if was_created:
                created += 1
        self.stdout.write(f"  Servers: {created} created, {len(SERVERS)} total")

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
