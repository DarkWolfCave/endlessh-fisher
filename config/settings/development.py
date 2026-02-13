"""
Development settings for Endlessh Fisher project.
"""

from .base import *  # noqa: F401, F403

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Use browsable API in development
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = [  # noqa: F405
    "rest_framework.renderers.JSONRenderer",
    "rest_framework.renderers.BrowsableAPIRenderer",
]

# Database and cache: use base.py defaults (PostgreSQL + Redis from env vars).
# For local dev without Docker, override via .env or environment variables.
