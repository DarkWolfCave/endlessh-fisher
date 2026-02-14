# Changelog

All notable changes to Endlessh Fisher are documented here.

## [1.3.0] - 2026-02-14

### Added

- **Notification Inbox** — persistent notification system at `/nachrichten/`
  with mark-as-read and delete functionality. All notifications are stored in
  the database and survive browser/container restarts.
- **Toast Popups** — new notifications appear as auto-dismissing popups
  (polled every 30s), complementing the existing rare fish alerts.
- **Notification Bell** — header icon with unread count badge (polled every 30s).
- **Rare Catch Notifications** — Celery task creates persistent notifications
  for epic, legendary, and mythic fish catches (every 10 minutes).
- **Achievement Notifications** — achievement unlocks now create persistent
  inbox entries with links to the achievement detail page.
- **Challenge Notifications** — completed daily challenges create notifications
  with links to the dashboard.
- **Bulk Actions** — "Mark All Read" and "Delete All" buttons in the inbox.
- **Deep Links** — notification titles link to their targets (achievement detail,
  fish detail, or dashboard).

### Migration Notes

After updating, run:

```bash
docker compose exec backend python manage.py migrate
```

The migration backfills existing unlocked achievements as read notifications.

## [1.2.0] - 2026-02-14

### Added

- **Cache Warming** — Celery Beat pre-warms the live pond cache every 10
  seconds, eliminating the ~1.4s InfluxDB cold-cache hit on page loads.
  If InfluxDB is unreachable, stale cache is preserved as fallback.

### Changed

- **Bind mounts** instead of named Docker volumes — persistent data now lives
  under `./data/` (postgres, redis), making backups and inspection easier.
- **View performance** optimized: parallel API calls, N+1 query fix, added
  caching to context processors and template tags.
- CSRF and session cookie settings are now automatically TLS-aware based on
  the `TRAEFIK_TLS` environment variable.

### Fixed

- Celery workers could not reach InfluxDB when using the Traefik compose setup
  (network isolation issue).
- DNS resolution failures inside Docker containers (added explicit DNS servers).

### Breaking Changes

- **Named volumes replaced by bind mounts.** If upgrading from 1.1.0, you must
  migrate your data from Docker named volumes to `./data/postgres` and
  `./data/redis` before starting. See README for migration steps.

## [1.1.0] - 2026-02-14

### Added

- **Adaptive Treasure Thresholds** — treasure spawn requirements now use
  percentile-based pond activity instead of fixed fish counts. A 7-day rolling
  histogram tracks your pond's activity and adjusts thresholds automatically.
  Small setups (2-3 concurrent bots) and large setups (200+ concurrent bots)
  now have equally fair access to rare treasures like the Wolf Head.
- During warmup (first ~50 minutes), all treasures are available to give new
  users a welcome experience. Spawn weights still limit rare drops.
- **Traefik Configuration via `.env`** — TLS, network name, entrypoint, and
  certificate resolver are now fully configurable without editing compose files.
- **`servers.toml` mounted as volume** in production — add or remove endlessh
  servers without rebuilding the Docker image.
- Wolf Digital Empire cross-promotion content on the dashboard.
- Disclaimer noting this is a fun project, not a security tool.

### Changed

- **Project renamed** from endlessh-game to **Endlessh Fisher** (containers,
  User-Agent header, internal references).
- Renamed `min_active_fish` to `min_pond_percentile` on TreasureType model.
- **Default port** changed from 8000 to **8100** (development compose).
- **Fish species duration ranges** rebalanced — fixed a bug where Plankton
  was assigned incorrectly at certain thresholds.

### Fixed

- `first_seen` timestamp was overwritten on every sync cycle instead of being
  preserved from the bot's first appearance.
- Timezone mismatch in daily challenge generation caused challenges to reset
  at the wrong time.
- `null` ip_address crash on fresh installations with no data yet.

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
