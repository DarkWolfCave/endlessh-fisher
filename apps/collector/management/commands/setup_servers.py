"""Management command to configure servers from servers.toml."""

import sys
import tomllib
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from apps.aquarium.models import Server

# Valid pond themes (from Server.POND_CHOICES)
VALID_THEMES = {"ocean", "lake", "reef"}
REQUIRED_FIELDS = {"slug", "name", "host_identifier"}


class Command(BaseCommand):
    help = "Load server configuration from servers.toml"

    def add_arguments(self, parser):
        parser.add_argument(
            "--config",
            type=str,
            default=str(settings.BASE_DIR / "servers.toml"),
            help="Path to servers.toml (default: PROJECT_ROOT/servers.toml)",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Show what would be created/updated without making changes.",
        )

    def handle(self, *args, **options):
        config_path = Path(options["config"])
        dry_run = options["dry_run"]

        if not config_path.exists():
            self.stderr.write(self.style.ERROR(
                f"Config file not found: {config_path}\n"
                f"Copy servers.toml.example to servers.toml and add your servers."
            ))
            sys.exit(1)

        try:
            with open(config_path, "rb") as f:
                config = tomllib.load(f)
        except tomllib.TOMLDecodeError as e:
            raise CommandError(f"Invalid TOML in {config_path}: {e}")

        servers = config.get("servers", [])
        if not servers:
            raise CommandError(
                f"No [[servers]] entries found in {config_path}. "
                f"See servers.toml.example for the format."
            )

        # Validate all entries before writing anything
        for i, srv in enumerate(servers, 1):
            missing = REQUIRED_FIELDS - set(srv.keys())
            if missing:
                raise CommandError(
                    f"Server #{i}: missing required fields: {', '.join(sorted(missing))}"
                )
            theme = srv.get("pond_theme", "ocean")
            if theme not in VALID_THEMES:
                raise CommandError(
                    f"Server '{srv['slug']}': invalid pond_theme '{theme}'. "
                    f"Valid: {', '.join(sorted(VALID_THEMES))}"
                )

        if dry_run:
            self.stdout.write(self.style.NOTICE("DRY RUN - no changes will be made"))
            for srv in servers:
                self.stdout.write(
                    f"  Would create/update: {srv['slug']} "
                    f"(host: {srv['host_identifier']}, theme: {srv.get('pond_theme', 'ocean')})"
                )
            return

        created = 0
        updated = 0
        with transaction.atomic():
            for srv in servers:
                _, was_created = Server.objects.update_or_create(
                    slug=srv["slug"],
                    defaults={
                        "name": srv["name"],
                        "host_identifier": srv["host_identifier"],
                        "description": srv.get("description", ""),
                        "pond_theme": srv.get("pond_theme", "ocean"),
                        "is_active": True,
                    },
                )
                if was_created:
                    created += 1
                else:
                    updated += 1

        self.stdout.write(self.style.SUCCESS(
            f"Servers configured: {created} created, {updated} updated, "
            f"{len(servers)} total"
        ))

        # Run initial data population so the dashboard isn't empty.
        # These are called as regular functions, not via Celery broker.
        self.stdout.write("Running initial data sync...")
        self._run_initial_tasks()

    def _run_initial_tasks(self):
        """Populate stats and challenges so the dashboard works immediately."""
        from apps.aquarium.challenge_service import generate_daily_challenges

        # 1. Sync bot data from InfluxDB
        try:
            from apps.collector.tasks import sync_bot_data
            result = sync_bot_data()
            self.stdout.write(f"  Bot sync: {result}")
        except Exception as e:
            self.stderr.write(self.style.WARNING(f"  Bot sync skipped: {e}"))

        # 2. Aggregate daily stats (server cards)
        try:
            from apps.collector.tasks import aggregate_daily_stats
            result = aggregate_daily_stats()
            self.stdout.write(f"  Daily stats: {result}")
        except Exception as e:
            self.stderr.write(self.style.WARNING(f"  Stats aggregation skipped: {e}"))

        # 3. Check achievements
        try:
            from apps.collector.tasks import check_achievements
            result = check_achievements()
            self.stdout.write(f"  Achievements: {result}")
        except Exception as e:
            self.stderr.write(self.style.WARNING(f"  Achievement check skipped: {e}"))

        # 4. Generate daily challenges
        try:
            generated = generate_daily_challenges()
            self.stdout.write(f"  Challenges: {len(generated)} generated")
        except Exception as e:
            self.stderr.write(self.style.WARNING(f"  Challenge generation skipped: {e}"))

        # 5. Evaluate challenge progress against synced data
        try:
            from apps.aquarium.challenge_service import evaluate_daily_challenges
            completed = evaluate_daily_challenges()
            self.stdout.write(f"  Challenge progress: {len(completed)} completed")
        except Exception as e:
            self.stderr.write(self.style.WARNING(f"  Challenge evaluation skipped: {e}"))
