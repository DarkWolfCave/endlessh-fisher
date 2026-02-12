# Endlessh Game - Bot Fishing & Achievement System

## Project Overview
Gamification of SSH tarpit (endlessh-go) data. Bots = Fish, Trap Duration = Fish Species.

## Tech Stack
- Python 3.14, Django 6.0.2, DRF 3.16.1, Celery 5.6.2
- HTMX + Alpine.js + Tailwind CSS (all self-hosted)
- PostgreSQL 18, Redis 8.6
- InfluxDB as data source (read-only)

## Project Structure
- `config/` - Django project config (settings/base.py, production.py, development.py)
- `apps/core/` - Base models, utilities, template tags
- `apps/collector/` - InfluxDB → PostgreSQL data pipeline (Celery tasks)
- `apps/aquarium/` - Game entities (CaughtBot, FishSpecies, Server)
- `apps/achievements/` - Achievement system (badges, milestones)

## Commands
- `python manage.py runserver` - Development server
- `python manage.py test` - Run tests
- `docker compose up` - Full stack (dev)
- `docker compose -f docker-compose.prod.yml up` - Production

## Key Rules
- ALL static assets self-hosted (DSGVO!)
- IPs hashed (SHA256) in frontend display
- Settings split: base.py (shared), development.py, production.py
- Celery tasks in apps/collector/tasks.py
