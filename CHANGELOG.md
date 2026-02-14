# Changelog

All notable changes to Endlessh Fisher are documented here.

## [1.1.0] - 2026-02-14

### Changed

- **Adaptive Treasure Thresholds** — treasure spawn requirements now use
  percentile-based pond activity instead of fixed fish counts. A 7-day rolling
  histogram tracks your pond's activity and adjusts thresholds automatically.
  Small setups (2-3 concurrent bots) and large setups (200+ concurrent bots)
  now have equally fair access to rare treasures like the Wolf Head.
- During warmup (first ~50 minutes), all treasures are available to give new
  users a welcome experience. Spawn weights still limit rare drops.
- Renamed `min_active_fish` to `min_pond_percentile` on TreasureType model.

### Migration Notes

After updating, run:

```bash
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py seed_game_data
```

## [1.0.0] - 2025-02-13

Initial public release.

### Core Features

- **Live Aquarium Dashboard** with real-time HTMX updates (15-60s polling)
- **Live Pond** — animated fish swimming based on currently trapped bots
- **Catch Ticker** — scrolling banner of recent catches
- **Rare Fish Alerts** — toast notifications for epic+ catches
- **Activity Feed** — clickable recent catches with fish detail links

### Game Systems

- **12 Fish Species** from Plankton (0-30s) to Leviathan (14d+) across
  6 rarity tiers (common, uncommon, rare, epic, legendary, mythic)
- **Achievement System** — 50+ achievements across 8 categories
  (bronze to diamond), including secret achievements
- **Daily Challenges** — 3 auto-generated challenges per day
  (easy, medium, hard) with 6 different metrics
- **Treasure Collection** — spawning treasures with real-world security tips
- **Score System** — species points + logarithmic trap time bonus

### Pages

- **Dashboard** — server ponds, live pond, stats bar, activity feed,
  challenges, treasures
- **Fish Encyclopedia** — Pokédex-style species collection tracker
- **Leaderboards** — longest traps, highest scores, records per species
- **Server Detail** — per-server catches, daily stats, species distribution
- **Fish Detail** — individual catch info with other catches from same IP
- **Treasure Vault** — collected treasures with security tips
- **World Map** — country-level catch statistics
- **Achievement Gallery** — all achievements with unlock status and progress

### IP Intelligence

- **Shodan InternetDB** integration (no API key required) — open ports,
  CPEs, tags, vulnerabilities, hostnames
- **AbuseIPDB** integration (optional, free tier) — abuse score, ISP,
  usage type, Tor detection, report history
- On-click lookup from fish detail page and live pond
- 6-hour Redis cache, rate limiting (10 lookups/min)
- Dedicated achievement category (Cyber Investigator, 10 achievements)

### Multi-Server & Data Pipeline

- Multiple endlessh-go instances as separate "fishing ponds"
- InfluxDB 2.x → PostgreSQL sync via Celery (every 5 minutes)
- Automatic species classification and score calculation
- Daily stats aggregation, country stats, server totals
- Full data recalculation job (daily consistency check)

### Internationalization

- Full German and English UI support via `GAME_LANGUAGE` setting
- Bilingual model fields (name, description) for all game content
- 100+ translated UI strings, 148 country names
- Language-aware template filters (`|t`, `|lang`)

### Privacy & Security

- SHA256 IP hashing by default (optional real IP display)
- All frontend assets self-hosted (no CDNs, GDPR-friendly)
- Rate limiting on IP lookups
- Non-root Docker user, health checks on all services
- Secret admin URL path via environment variable

### API

- REST API with Django REST Framework
- Endpoints: health, dashboard, catches, servers, species, daily stats,
  country stats, achievements, achievement toasts

### Deployment

- Docker Compose for development and production
- Simple production setup (port 8000, any reverse proxy)
- Advanced Traefik setup with Blue-Green deployment
- Multi-stage Dockerfile (Python 3.14, Gunicorn)
- Celery worker + beat for background tasks
