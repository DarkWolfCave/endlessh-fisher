"""Aquarium business logic - fish classification and score calculation."""

import math

from apps.aquarium.models import FishSpecies


def classify_fish(trapped_seconds: float) -> FishSpecies | None:
    """Classify a bot into a fish species based on trapped duration.

    Iterates species ordered by min_trapped_seconds (ascending).
    Returns the matching species or None if no match.
    """
    species_list = FishSpecies.objects.all().order_by("min_trapped_seconds")
    result = None
    for species in species_list:
        if trapped_seconds >= species.min_trapped_seconds:
            result = species
        else:
            break
    return result


def calculate_score(species: FishSpecies | None, trapped_seconds: float) -> int:
    """Calculate score: species.points + log2(trapped_seconds + 1)."""
    base_points = species.points if species else 1
    time_bonus = int(math.log2(trapped_seconds + 1))
    return base_points + time_bonus
