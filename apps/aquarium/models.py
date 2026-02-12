"""Aquarium models - game entities: fish, servers (ponds), caught bots, stats."""

from django.db import models

from apps.core.models import TimeStampedModel


class FishSpecies(TimeStampedModel):
    """Fish types based on trapped duration. Seeded via data migration."""

    RARITY_CHOICES = [
        ("common", "Common"),
        ("uncommon", "Uncommon"),
        ("rare", "Rare"),
        ("epic", "Epic"),
        ("legendary", "Legendary"),
        ("mythic", "Mythic"),
    ]

    slug = models.SlugField(unique=True, max_length=50)
    name = models.CharField(max_length=100)
    name_de = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, default="")
    description_de = models.TextField(max_length=500, blank=True, default="")
    min_trapped_seconds = models.PositiveIntegerField()
    max_trapped_seconds = models.PositiveIntegerField(null=True, blank=True)
    rarity = models.CharField(max_length=20, choices=RARITY_CHOICES)
    rarity_color = models.CharField(max_length=7, default="#808080")
    points = models.PositiveIntegerField(default=1)
    lottie_file = models.CharField(max_length=200, blank=True, default="")
    svg_file = models.CharField(max_length=200, blank=True, default="")
    css_class = models.CharField(max_length=50, blank=True, default="")
    sort_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["sort_order", "min_trapped_seconds"]
        verbose_name_plural = "Fish Species"

    def __str__(self):
        return f"{self.name_de} ({self.rarity})"


class Server(TimeStampedModel):
    """Endlessh server instance = a 'Fishing Pond'."""

    POND_CHOICES = [
        ("ocean", "Deep Ocean"),
        ("lake", "Mountain Lake"),
        ("reef", "Coral Reef"),
    ]

    slug = models.SlugField(unique=True, max_length=50)
    name = models.CharField(max_length=100)
    host_identifier = models.CharField(max_length=100, unique=True, db_index=True)
    description = models.TextField(max_length=500, blank=True, default="")
    icon = models.CharField(max_length=50, default="server")
    is_active = models.BooleanField(default=True)
    pond_theme = models.CharField(max_length=30, default="ocean", choices=POND_CHOICES)
    # Aggregated stats (updated by Celery)
    total_catches = models.PositiveBigIntegerField(default=0)
    total_trapped_seconds = models.PositiveBigIntegerField(default=0)
    total_bytes_sent = models.PositiveBigIntegerField(default=0)
    unique_ips = models.PositiveIntegerField(default=0)
    unique_countries = models.PositiveIntegerField(default=0)

    class Meta:
        indexes = [
            models.Index(fields=["host_identifier"], name="idx_server_host_id"),
        ]

    def __str__(self):
        return self.name


class CaughtBot(TimeStampedModel):
    """A trapped SSH bot = a caught fish. Core game entity."""

    server = models.ForeignKey(
        Server, on_delete=models.CASCADE, related_name="catches"
    )
    species = models.ForeignKey(
        FishSpecies, on_delete=models.SET_NULL, null=True, related_name="catches"
    )
    ip_address = models.GenericIPAddressField(db_index=True)
    ip_hash = models.CharField(max_length=64, db_index=True)
    country_code = models.CharField(max_length=2, blank=True, default="", db_index=True)
    country_name = models.CharField(max_length=100, blank=True, default="")
    geohash = models.CharField(max_length=12, blank=True, default="")
    local_port = models.PositiveIntegerField(default=22)
    trapped_seconds = models.FloatField(default=0)
    bytes_sent = models.PositiveBigIntegerField(default=0)
    first_seen = models.DateTimeField()
    last_seen = models.DateTimeField()
    is_active = models.BooleanField(default=False, db_index=True)
    connection_count = models.PositiveIntegerField(default=1)
    score = models.PositiveIntegerField(default=0)
    influx_fingerprint = models.CharField(max_length=128, unique=True, db_index=True)

    class Meta:
        ordering = ["-first_seen"]
        indexes = [
            models.Index(
                fields=["server", "-first_seen"], name="idx_catch_server_time"
            ),
            models.Index(
                fields=["species", "-trapped_seconds"], name="idx_catch_species_time"
            ),
            models.Index(fields=["country_code"], name="idx_catch_country"),
            models.Index(fields=["-score"], name="idx_catch_score"),
            models.Index(fields=["is_active"], name="idx_catch_active"),
            models.Index(fields=["ip_hash"], name="idx_catch_ip_hash"),
        ]

    def __str__(self):
        species_name = self.species.name_de if self.species else "Unknown"
        return f"{species_name} ({self.ip_hash[:8]}...) - {self.trapped_seconds:.0f}s"


class DailyStats(TimeStampedModel):
    """Pre-aggregated daily statistics per server."""

    date = models.DateField(db_index=True)
    server = models.ForeignKey(
        Server,
        on_delete=models.CASCADE,
        related_name="daily_stats",
        null=True,
        blank=True,
    )
    new_catches = models.PositiveIntegerField(default=0)
    total_trapped_seconds = models.FloatField(default=0)
    total_bytes_sent = models.PositiveBigIntegerField(default=0)
    unique_ips = models.PositiveIntegerField(default=0)
    unique_countries = models.PositiveIntegerField(default=0)
    top_species_slug = models.SlugField(max_length=50, blank=True, default="")
    longest_trap_seconds = models.FloatField(default=0)

    class Meta:
        unique_together = ["date", "server"]
        ordering = ["-date"]
        indexes = [
            models.Index(
                fields=["date", "server"], name="idx_daily_date_server"
            ),
        ]
        verbose_name_plural = "Daily Stats"

    def __str__(self):
        server_name = self.server.name if self.server else "Global"
        return f"{self.date} - {server_name}: {self.new_catches} catches"


class CountryStats(TimeStampedModel):
    """Aggregated stats per country for the world map."""

    country_code = models.CharField(max_length=2, primary_key=True)
    country_name = models.CharField(max_length=100)
    total_catches = models.PositiveIntegerField(default=0)
    total_trapped_seconds = models.FloatField(default=0)
    unique_ips = models.PositiveIntegerField(default=0)
    last_catch_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-total_catches"]
        verbose_name_plural = "Country Stats"

    def __str__(self):
        return f"{self.country_name} ({self.country_code}): {self.total_catches} catches"
