"""
Production settings for Endlessh Fisher project.
"""

import os

from .base import *  # noqa: F401, F403

DEBUG = False

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

# Security settings for reverse proxy
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True

# TLS: auto-detect from TRAEFIK_TLS env var (default: true)
_USE_TLS = os.environ.get("TRAEFIK_TLS", "true").lower() not in ("false", "0", "no")
_SCHEME = "https" if _USE_TLS else "http"

CSRF_TRUSTED_ORIGINS = [
    f"{_SCHEME}://{host.strip()}" for host in ALLOWED_HOSTS
]

# Session & CSRF cookies — secure flag only with TLS
SESSION_COOKIE_SECURE = _USE_TLS
CSRF_COOKIE_SECURE = _USE_TLS
SESSION_COOKIE_HTTPONLY = True

# HSTS (only meaningful with TLS)
SECURE_HSTS_SECONDS = 31536000 if _USE_TLS else 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = _USE_TLS
SECURE_HSTS_PRELOAD = _USE_TLS

# Admin URL (obfuscated)
ADMIN_URL = os.environ.get("ADMIN_URL", "admin/")

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "apps.collector": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
        "celery": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False,
        },
    },
}
