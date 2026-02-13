"""DRF serializers for aquarium models."""

from django.conf import settings
from rest_framework import serializers

from apps.aquarium.models import CaughtBot, CountryStats, DailyStats, FishSpecies, Server


class FishSpeciesSerializer(serializers.ModelSerializer):
    display_name = serializers.SerializerMethodField()
    display_description = serializers.SerializerMethodField()

    class Meta:
        model = FishSpecies
        fields = [
            "id", "slug", "name", "name_de", "display_name",
            "description_de", "display_description",
            "min_trapped_seconds", "max_trapped_seconds",
            "rarity", "rarity_color", "points", "sort_order",
        ]

    def get_display_name(self, obj):
        if settings.GAME_LANGUAGE == "de":
            return obj.name_de
        return obj.name

    def get_display_description(self, obj):
        if settings.GAME_LANGUAGE == "de":
            return obj.description_de
        return obj.description


class ServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Server
        fields = [
            "id", "slug", "name", "host_identifier", "description",
            "pond_theme", "is_active", "total_catches",
            "total_trapped_seconds", "unique_ips", "unique_countries",
        ]


class CaughtBotSerializer(serializers.ModelSerializer):
    species_name = serializers.SerializerMethodField()

    def get_species_name(self, obj):
        if settings.GAME_LANGUAGE == "de":
            return obj.species.name_de
        return obj.species.name
    species_rarity = serializers.CharField(source="species.rarity", read_only=True)
    species_color = serializers.CharField(source="species.rarity_color", read_only=True)
    server_name = serializers.CharField(source="server.name", read_only=True)

    class Meta:
        model = CaughtBot
        fields = [
            "id", "ip_hash", "country_code", "country_name",
            "trapped_seconds", "score", "first_seen", "last_seen",
            "is_active", "connection_count",
            "species_name", "species_rarity", "species_color", "server_name",
        ]


class DailyStatsSerializer(serializers.ModelSerializer):
    server_name = serializers.CharField(source="server.name", read_only=True)

    class Meta:
        model = DailyStats
        fields = [
            "date", "server_name", "new_catches", "total_trapped_seconds",
            "unique_ips", "unique_countries", "longest_trap_seconds",
        ]


class CountryStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryStats
        fields = [
            "country_code", "country_name", "total_catches",
            "total_trapped_seconds", "unique_ips", "last_catch_at",
        ]
