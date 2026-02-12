"""InfluxDB client for querying endlessh metrics."""

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


def query_new_connections(since_iso: str, host: str | None = None) -> list[dict]:
    """Query new bot connections from InfluxDB.

    Returns list of dicts with keys:
        ip, country, geohash, local_port, host, _time, _value (open_count)
    """
    host_filter = ""
    if host:
        host_filter = f'  |> filter(fn: (r) => r["host"] == "{host}")\n'

    query = f"""
from(bucket: "{settings.INFLUXDB_BUCKET}")
  |> range(start: {since_iso})
  |> filter(fn: (r) => r["_measurement"] == "endlessh_client_open_count")
{host_filter}  |> keep(columns: ["_time", "_value", "ip", "country", "geohash", "local_port", "host"])
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
                    "value": record.get_value(),
                })
        return results
    except Exception:
        logger.exception("Failed to query InfluxDB for new connections")
        return []
    finally:
        client.close()


def query_trapped_time(since_iso: str, host: str | None = None) -> list[dict]:
    """Query trapped time data from InfluxDB.

    Returns list of dicts with keys:
        ip, local_port, host, _time, _value (trapped_seconds)
    """
    host_filter = ""
    if host:
        host_filter = f'  |> filter(fn: (r) => r["host"] == "{host}")\n'

    query = f"""
from(bucket: "{settings.INFLUXDB_BUCKET}")
  |> range(start: {since_iso})
  |> filter(fn: (r) => r["_measurement"] == "endlessh_client_trapped_time_seconds")
{host_filter}  |> keep(columns: ["_time", "_value", "ip", "local_port", "host"])
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
                    "local_port": record.values.get("local_port", "22"),
                    "host": record.values.get("host", ""),
                    "time": record.get_time(),
                    "value": record.get_value(),
                })
        return results
    except Exception:
        logger.exception("Failed to query InfluxDB for trapped time")
        return []
    finally:
        client.close()


def query_global_totals(since_iso: str) -> dict:
    """Query global total counters for bytes sent."""
    query = f"""
from(bucket: "{settings.INFLUXDB_BUCKET}")
  |> range(start: {since_iso})
  |> filter(fn: (r) => r["_measurement"] == "endlessh_sent_bytes_total")
  |> last()
  |> keep(columns: ["_time", "_value", "host"])
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
