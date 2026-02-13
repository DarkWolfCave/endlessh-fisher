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


class SecurityTip(TimeStampedModel):
    """Server security tip revealed when collecting a treasure."""

    RARITY_CHOICES = [
        ("common", "Common"),
        ("uncommon", "Uncommon"),
        ("rare", "Rare"),
        ("epic", "Epic"),
        ("legendary", "Legendary"),
    ]

    CATEGORY_CHOICES = [
        ("ssh", "SSH"),
        ("firewall", "Firewall"),
        ("monitoring", "Monitoring"),
        ("auth", "Authentication"),
        ("updates", "Updates"),
        ("network", "Network"),
        ("container", "Container"),
        ("strategy", "Strategy"),
    ]

    slug = models.SlugField(unique=True, max_length=80)
    title = models.CharField(max_length=200)
    title_de = models.CharField(max_length=200)
    content = models.TextField(max_length=2000, default="")
    content_de = models.TextField(max_length=2000)
    source_url = models.URLField(max_length=500, blank=True, default="")
    source_label = models.CharField(max_length=200, blank=True, default="")
    source_label_de = models.CharField(max_length=200, blank=True, default="")
    rarity = models.CharField(max_length=20, choices=RARITY_CHOICES)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    emoji = models.CharField(max_length=10, default="\U0001F512")
    sort_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["rarity", "sort_order"]

    def __str__(self):
        return f"{self.emoji} {self.title_de} ({self.rarity})"


class TreasureType(TimeStampedModel):
    """Collectible treasure type that can appear in the live pond."""

    RARITY_CHOICES = [
        ("common", "Common"),
        ("uncommon", "Uncommon"),
        ("rare", "Rare"),
        ("epic", "Epic"),
        ("legendary", "Legendary"),
    ]

    slug = models.SlugField(unique=True, max_length=50)
    name = models.CharField(max_length=100)
    name_de = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, default="")
    description_de = models.TextField(max_length=500, blank=True, default="")
    emoji = models.CharField(max_length=10)
    rarity = models.CharField(max_length=20, choices=RARITY_CHOICES)
    rarity_color = models.CharField(max_length=7, default="#808080")
    points = models.PositiveIntegerField(default=5)
    spawn_weight = models.PositiveIntegerField(
        default=100,
        help_text="Relative spawn probability. Higher = more likely.",
    )
    min_active_fish = models.PositiveSmallIntegerField(
        default=1,
        help_text="Minimum fish in pond for this treasure to spawn.",
    )
    css_class = models.CharField(max_length=50, blank=True, default="")
    sort_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["sort_order"]
        verbose_name_plural = "Treasure Types"

    def __str__(self):
        return f"{self.emoji} {self.name_de} ({self.rarity})"


class CollectedTreasure(TimeStampedModel):
    """Record of a collected treasure. Single-user: no user FK.

    When going multi-user: add User FK (same pattern as UnlockedAchievement).
    """

    treasure_type = models.ForeignKey(
        TreasureType, on_delete=models.CASCADE, related_name="collections"
    )
    security_tip = models.ForeignKey(
        SecurityTip, on_delete=models.SET_NULL, null=True, blank=True,
        related_name="tip_collections",
    )
    pond_treasure_id = models.CharField(
        max_length=64, unique=True, db_index=True,
        help_text="UUID of the treasure instance in the pond.",
    )
    collected_at = models.DateTimeField()
    active_fish_count = models.PositiveSmallIntegerField(default=0)
    points_awarded = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-collected_at"]
        indexes = [
            models.Index(fields=["-collected_at"], name="idx_treasure_collected"),
        ]

    def __str__(self):
        return f"{self.treasure_type.name_de} @ {self.collected_at}"


class ChallengeTemplate(TimeStampedModel):
    """Template for generating daily challenges with variable thresholds."""

    METRIC_CHOICES = [
        ("daily_catches", "Catches Today"),
        ("daily_trapped_seconds", "Trapped Seconds Today"),
        ("daily_unique_countries", "Unique Countries Today"),
        ("daily_unique_species", "Unique Species Today"),
        ("daily_rare_catches", "Rare+ Catches Today"),
        ("daily_treasures", "Treasures Collected Today"),
    ]

    DIFFICULTY_CHOICES = [
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("hard", "Hard"),
    ]

    slug = models.SlugField(unique=True, max_length=80)
    name = models.CharField(max_length=200)
    name_de = models.CharField(max_length=200)
    description_template = models.CharField(
        max_length=300,
        help_text="Template string with {threshold} placeholder.",
    )
    description_template_de = models.CharField(
        max_length=300,
        help_text="German template string with {threshold} placeholder.",
    )
    metric = models.CharField(max_length=50, choices=METRIC_CHOICES)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    threshold_min = models.PositiveIntegerField()
    threshold_max = models.PositiveIntegerField()
    reward_points = models.PositiveIntegerField(default=25)
    emoji = models.CharField(max_length=10, default="\U0001F3AF")
    server_filter = models.ForeignKey(
        Server, on_delete=models.SET_NULL, null=True, blank=True,
        help_text="If set, challenge only counts catches on this server.",
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["difficulty", "slug"]

    def __str__(self):
        return f"{self.name_de} ({self.difficulty})"


class DailyChallenge(TimeStampedModel):
    """Concrete daily challenge instance, generated from a template.

    3 challenges are generated each day at midnight (1 easy, 1 medium, 1 hard).
    """

    date = models.DateField(db_index=True)
    template = models.ForeignKey(
        ChallengeTemplate, on_delete=models.CASCADE, related_name="instances"
    )
    threshold = models.PositiveIntegerField()
    description = models.CharField(max_length=300)
    description_de = models.CharField(max_length=300)
    reward_points = models.PositiveIntegerField()
    current_value = models.FloatField(default=0)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    notified = models.BooleanField(default=False)

    class Meta:
        ordering = ["-date", "template__difficulty"]
        unique_together = ["date", "template"]
        indexes = [
            models.Index(
                fields=["date", "is_completed"], name="idx_challenge_date_done"
            ),
        ]

    def __str__(self):
        status = "done" if self.is_completed else f"{self.current_value}/{self.threshold}"
        return f"{self.date}: {self.description_de} [{status}]"

    @property
    def progress_percent(self) -> int:
        if self.threshold == 0:
            return 100
        return min(100, int((self.current_value / self.threshold) * 100))
