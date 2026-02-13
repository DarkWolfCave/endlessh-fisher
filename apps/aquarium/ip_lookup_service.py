"""IP intelligence lookup via Shodan InternetDB and AbuseIPDB."""

import ipaddress
import json
import logging
import urllib.request
import urllib.error

from django.conf import settings
from django.core.cache import cache

logger = logging.getLogger(__name__)

_CACHE_PREFIX = "endlessh:ip_lookup:"
_CACHE_TTL = 21600  # 6 hours

# Ports commonly associated with dangerous/exploitable services
_DANGEROUS_PORTS = {
    21, 23, 25, 135, 137, 139, 445, 1433, 1434, 3306, 3389,
    5432, 5900, 5985, 6379, 8080, 8443, 9200, 11211, 27017,
}

_REQUEST_TIMEOUT = 5  # seconds


def _is_public_ip(ip_str: str) -> bool:
    """Check if IP is a valid public (non-private, non-reserved) address."""
    try:
        addr = ipaddress.ip_address(ip_str)
        return addr.is_global and not addr.is_reserved
    except ValueError:
        return False


def _fetch_json(url: str, headers: dict | None = None) -> dict | None:
    """Fetch JSON from URL with timeout. Returns None on any error."""
    all_headers = {"User-Agent": "EndlesshGame/1.0"}
    if headers:
        all_headers.update(headers)
    req = urllib.request.Request(url, headers=all_headers)
    try:
        with urllib.request.urlopen(req, timeout=_REQUEST_TIMEOUT) as resp:
            if resp.status == 200:
                return json.loads(resp.read().decode())
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError,
            json.JSONDecodeError, OSError) as exc:
        logger.debug("IP lookup fetch failed for %s: %s", url, exc)
    return None


def _fetch_shodan(ip: str) -> dict:
    """Query Shodan InternetDB (free, no auth)."""
    data = _fetch_json(f"https://internetdb.shodan.io/{ip}")
    if not data:
        return {"available": False}

    ports = data.get("ports", [])
    return {
        "available": True,
        "ports": sorted(ports),
        "dangerous_ports": sorted(p for p in ports if p in _DANGEROUS_PORTS),
        "cpes": data.get("cpes", []),
        "hostnames": data.get("hostnames", []),
        "tags": data.get("tags", []),
        "vulns": data.get("vulns", []),
    }


def _fetch_abuseipdb(ip: str) -> dict:
    """Query AbuseIPDB (requires API key)."""
    api_key = getattr(settings, "ABUSEIPDB_API_KEY", "")
    if not api_key:
        return {"available": False, "reason": "no_key"}

    data = _fetch_json(
        f"https://api.abuseipdb.com/api/v2/check"
        f"?ipAddress={ip}&maxAgeInDays=90&verbose",
        headers={
            "Key": api_key,
            "Accept": "application/json",
        },
    )
    if not data or "data" not in data:
        return {"available": False, "reason": "api_error"}

    d = data["data"]
    return {
        "available": True,
        "abuse_score": d.get("abuseConfidenceScore", 0),
        "total_reports": d.get("totalReports", 0),
        "distinct_users": d.get("numDistinctUsers", 0),
        "isp": d.get("isp", ""),
        "usage_type": d.get("usageType", ""),
        "domain": d.get("domain", ""),
        "is_tor": d.get("isTor", False),
        "is_whitelisted": d.get("isWhitelisted", False),
        "country_code": d.get("countryCode", ""),
        "last_reported": d.get("lastReportedAt", ""),
    }


def lookup_ip(ip_address: str) -> dict:
    """Combined IP intelligence lookup with caching.

    Returns dict with 'shodan' and 'abuseipdb' sub-dicts,
    plus 'ip' and 'cached' keys.
    """
    ip_address = str(ip_address).strip()

    if not _is_public_ip(ip_address):
        return {
            "ip": ip_address,
            "error": "private_ip",
            "shodan": {"available": False},
            "abuseipdb": {"available": False},
        }

    # Check cache first
    cache_key = f"{_CACHE_PREFIX}{ip_address}"
    cached = cache.get(cache_key)
    if cached:
        # Invalidate cache if AbuseIPDB key was added after caching
        abuse_stale = (
            cached.get("abuseipdb", {}).get("reason") == "no_key"
            and getattr(settings, "ABUSEIPDB_API_KEY", "")
        )
        if not abuse_stale:
            cached["cached"] = True
            return cached

    result = {
        "ip": ip_address,
        "cached": False,
        "shodan": _fetch_shodan(ip_address),
        "abuseipdb": _fetch_abuseipdb(ip_address),
    }

    cache.set(cache_key, result, _CACHE_TTL)
    return result
