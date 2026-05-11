#!/bin/bash
set -e

# Docker entrypoint for Endlessh Fisher.
#
# Runs database migrations, seeds game data, and configures servers
# ONLY for web processes (gunicorn/runserver). Celery workers and beat
# pass "celery" as first arg via compose command override and skip init.
#
# The initial InfluxDB sync is NOT run here — Celery handles that on
# its regular schedule (every 5 minutes). This keeps startup fast.

if [[ "$1" == "gunicorn" || "$1" == "python" ]]; then
    echo "[entrypoint] Running database migrations..."
    python manage.py migrate --noinput

    echo "[entrypoint] Seeding game data..."
    python manage.py seed_game_data

    if [[ -f "servers.toml" ]]; then
        echo "[entrypoint] Setting up servers..."
        python manage.py setup_servers --skip-initial-sync
    else
        echo "[entrypoint] No servers.toml found — skipping server setup."
        echo "[entrypoint] Copy servers.toml.example to servers.toml to configure your servers."
    fi

    echo "[entrypoint] Initialization complete."
fi

# Hand off to the main process (gunicorn, celery, runserver, etc.)
exec "$@"
