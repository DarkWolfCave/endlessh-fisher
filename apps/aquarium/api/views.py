"""DRF API views for aquarium."""

from django.db.models import Sum
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.aquarium.models import CaughtBot, CountryStats, DailyStats, FishSpecies, Server

from .serializers import (
    CaughtBotSerializer,
    CountryStatsSerializer,
    DailyStatsSerializer,
    FishSpeciesSerializer,
    ServerSerializer,
)


@api_view(["GET"])
def health_check(request):
    """Health check endpoint for Docker/Traefik."""
    return Response({"status": "ok"})


@api_view(["GET"])
def dashboard_stats(request):
    """Aggregated dashboard statistics."""
    total_catches = CaughtBot.objects.count()
    active_traps = CaughtBot.objects.filter(is_active=True).count()
    total_score = CaughtBot.objects.aggregate(total=Sum("score"))["total"] or 0
    total_trapped = (
        CaughtBot.objects.aggregate(total=Sum("trapped_seconds"))["total"] or 0
    )
    total_countries = CountryStats.objects.count()

    return Response({
        "total_catches": total_catches,
        "active_traps": active_traps,
        "total_score": total_score,
        "total_trapped_seconds": total_trapped,
        "total_countries": total_countries,
    })


@api_view(["GET"])
def latest_catches(request):
    """Last N catches for activity feed."""
    limit = min(int(request.query_params.get("limit", 10)), 50)
    catches = CaughtBot.objects.select_related("species", "server")[:limit]
    serializer = CaughtBotSerializer(catches, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def daily_stats(request):
    """Daily stats time series."""
    days = min(int(request.query_params.get("days", 30)), 365)
    stats = DailyStats.objects.select_related("server")[:days]
    serializer = DailyStatsSerializer(stats, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def country_stats(request):
    """Country breakdown for world map."""
    countries = CountryStats.objects.all()
    serializer = CountryStatsSerializer(countries, many=True)
    return Response(serializer.data)


class CaughtBotListView(generics.ListAPIView):
    serializer_class = CaughtBotSerializer

    def get_queryset(self):
        qs = CaughtBot.objects.select_related("species", "server")
        server = self.request.query_params.get("server")
        species = self.request.query_params.get("species")
        country = self.request.query_params.get("country")
        if server:
            qs = qs.filter(server__slug=server)
        if species:
            qs = qs.filter(species__slug=species)
        if country:
            qs = qs.filter(country_code=country)
        return qs


class CaughtBotDetailView(generics.RetrieveAPIView):
    queryset = CaughtBot.objects.select_related("species", "server")
    serializer_class = CaughtBotSerializer


class ServerListView(generics.ListAPIView):
    queryset = Server.objects.filter(is_active=True)
    serializer_class = ServerSerializer


class ServerDetailView(generics.RetrieveAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    lookup_field = "slug"


class FishSpeciesListView(generics.ListAPIView):
    queryset = FishSpecies.objects.all()
    serializer_class = FishSpeciesSerializer
