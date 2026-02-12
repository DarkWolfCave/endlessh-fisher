"""InfluxDB client for querying endlessh metrics.

Queries use Flux aggregation to return one record per unique (host, ip),
not one per scrape interval. This keeps data transfer and processing efficient.
"""

import logging

from django.conf import settings
from influxdb_client import InfluxDBClient

logger = logging.getLogger(__name__)


def get_influx_client() -> InfluxDBClient:
    """Create an InfluxDB client from Django settings."""
    return InfluxDBClient(
        url=settings.INFLUXDB_URL,
        token=settings.INFLUXDB_TOKEN,
        org=settings.INFLUXDB_ORG,
    )


def query_bot_connections(since_iso: str) -> list[dict]:
    """Query unique bot connections aggregated per (host, ip).

    Uses Flux to aggregate: last() per group(host, ip) gives us one record
    per unique bot with the latest counter value, country, and geohash.

    Returns list of dicts with keys:
        ip, country, geohash, local_port, host, time, open_count
    """
    query = f"""
from(bucket: "{settings.INFLUXDB_BUCKET}")
  |> range(start: {since_iso})
  |> filter(fn: (r) => r["_measurement"] == "endlessh_client_open_count")
  |> group(columns: ["host", "ip", "country", "geohash", "local_port"])
  |> last()
  |> keep(columns: ["_time", "_value", "ip", "country", "geohash", "local_port", "host"])
"""

    client = get_influx_client()
    try:
        query_api = client.query_api()
        tables = query_api.query(query, org=settings.INFLUXDB_ORG)

        results = []
        for table in tables:
            for record in table.records:
                results.append({
                    "ip": record.values.get("ip", ""),
                    "country": record.values.get("country", ""),
                    "geohash": record.values.get("geohash", ""),
                    "local_port": record.values.get("local_port", "22"),
                    "host": record.values.get("host", ""),
                    "time": record.get_time(),
                    "open_count": record.get_value() or 0,
                })
        return results
    except Exception:
        logger.exception("Failed to query InfluxDB for bot connections")
        return []
    finally:
        client.close()


def query_trapped_times(since_iso: str) -> dict[str, float]:
    """Query trapped time aggregated per (host, ip).

    Returns dict mapping "host:ip" -> max trapped_seconds.
    """
    query = f"""
from(bucket: "{settings.INFLUXDB_BUCKET}")
  |> range(start: {since_iso})
  |> filter(fn: (r) => r["_measurement"] == "endlessh_client_trapped_time_seconds")
  |> group(columns: ["host", "ip"])
  |> last()
  |> keep(columns: ["_value", "ip", "host"])
"""

    client = get_influx_client()
    try:
        query_api = client.query_api()
        tables = query_api.query(query, org=settings.INFLUXDB_ORG)

        result = {}
        for table in tables:
            for record in table.records:
                host = record.values.get("host", "")
                ip = record.values.get("ip", "")
                value = record.get_value() or 0
                if host and ip:
                    result[f"{host}:{ip}"] = float(value)
        return result
    except Exception:
        logger.exception("Failed to query InfluxDB for trapped times")
        return {}
    finally:
        client.close()


def _query_total(measurement: str) -> float:
    """Query the sum of a total counter across all hosts."""
    query = f"""
from(bucket: "{settings.INFLUXDB_BUCKET}")
  |> range(start: -5m)
  |> filter(fn: (r) => r["_measurement"] == "{measurement}")
  |> last()
  |> group()
  |> sum()
"""
    client = get_influx_client()
    try:
        query_api = client.query_api()
        tables = query_api.query(query, org=settings.INFLUXDB_ORG)
        for table in tables:
            for record in table.records:
                return float(record.get_value() or 0)
        return 0.0
    except Exception:
        logger.exception("Failed to query InfluxDB for %s", measurement)
        return 0.0
    finally:
        client.close()


def query_active_connections() -> int:
    """Query currently active connections across all servers.

    Calculates open_count_total - closed_count_total to determine
    how many bots are currently trapped.
    """
    opened = _query_total("endlessh_client_open_count_total")
    closed = _query_total("endlessh_client_closed_count_total")
    return max(0, int(opened - closed))


def query_active_bots() -> list[dict]:
    """Query currently active (trapped) bots with their live trap duration.

    Uses three queries:
    1. difference() finds bots where trapped_time is still increasing (= active)
    2. first() finds newly connected bots (only 1 data point, difference can't detect)
    3. last() gets actual trapped_time values for all matched bots

    Returns list of dicts with keys:
        ip, host, country, geohash, trapped_seconds, last_seen
    """
    # Query A: Bots with increasing trapped_time (2+ data points)
    active_query = f"""
from(bucket: "{settings.INFLUXDB_BUCKET}")
  |> range(start: -5m)
  |> filter(fn: (r) => r["_measurement"] == "endlessh_client_trapped_time_seconds")
  |> group(columns: ["host", "ip"])
  |> difference(nonNegative: true)
  |> last()
  |> filter(fn: (r) => r["_value"] > 0)
  |> keep(columns: ["ip", "host"])
"""

    # Query B: Newly connected bots (first appearance in last 90s within the 5m window)
    new_query = f"""
import "experimental"

from(bucket: "{settings.INFLUXDB_BUCKET}")
  |> range(start: -5m)
  |> filter(fn: (r) => r["_measurement"] == "endlessh_client_trapped_time_seconds")
  |> group(columns: ["host", "ip"])
  |> first()
  |> filter(fn: (r) => r._time > experimental.subDuration(d: 90s, from: now()))
  |> keep(columns: ["ip", "host"])
"""

    # Query C: Actual trapped_time values
    values_query = f"""
from(bucket: "{settings.INFLUXDB_BUCKET}")
  |> range(start: -5m)
  |> filter(fn: (r) => r["_measurement"] == "endlessh_client_trapped_time_seconds")
  |> group(columns: ["host", "ip", "country", "geohash"])
  |> last()
  |> keep(columns: ["_time", "_value", "ip", "host", "country", "geohash"])
"""

    client = get_influx_client()
    try:
        query_api = client.query_api()

        # Collect active keys from both queries
        active_keys = set()

        for query in (active_query, new_query):
            tables = query_api.query(query, org=settings.INFLUXDB_ORG)
            for table in tables:
                for record in table.records:
                    host = record.values.get("host", "")
                    ip = record.values.get("ip", "")
                    if host and ip:
                        active_keys.add(f"{host}:{ip}")

        if not active_keys:
            return []

        # Get values, filtered to only active bots
        value_tables = query_api.query(values_query, org=settings.INFLUXDB_ORG)
        results = []
        for table in value_tables:
            for record in table.records:
                host = record.values.get("host", "")
                ip = record.values.get("ip", "")
                if f"{host}:{ip}" not in active_keys:
                    continue
                trapped = record.get_value() or 0
                if trapped > 0:
                    results.append({
                        "ip": ip,
                        "host": host,
                        "country": record.values.get("country", ""),
                        "geohash": record.values.get("geohash", ""),
                        "trapped_seconds": float(trapped),
                        "last_seen": record.get_time().isoformat(),
                    })
        return results
    except Exception:
        logger.exception("Failed to query InfluxDB for active bots")
        return []
    finally:
        client.close()


def query_global_totals() -> dict:
    """Query global total counters for bytes sent per host."""
    query = f"""
from(bucket: "{settings.INFLUXDB_BUCKET}")
  |> range(start: -30d)
  |> filter(fn: (r) => r["_measurement"] == "endlessh_sent_bytes_total")
  |> last()
  |> keep(columns: ["_value", "host"])
"""

    client = get_influx_client()
    try:
        query_api = client.query_api()
        tables = query_api.query(query, org=settings.INFLUXDB_ORG)

        totals = {}
        for table in tables:
            for record in table.records:
                host = record.values.get("host", "unknown")
                totals[host] = record.get_value() or 0
        return totals
    except Exception:
        logger.exception("Failed to query InfluxDB for global totals")
        return {}
    finally:
        client.close()
