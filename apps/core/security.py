"""Input sanitization utilities (CLAUDE.md security compliance)."""

import hashlib

from django.utils.html import strip_tags


class InputSanitizer:
    """Sanitize user input to prevent XSS and injection attacks."""

    MAX_NAME_LENGTH = 200
    MAX_DESCRIPTION_LENGTH = 10_000

    @classmethod
    def sanitize_string(cls, value: str, max_length: int = MAX_NAME_LENGTH) -> str:
        """Strip HTML tags and truncate to max length."""
        if not value:
            return ""
        return strip_tags(str(value))[:max_length]

    @classmethod
    def hash_ip(cls, ip_address: str) -> str:
        """SHA256 hash of IP address for DSGVO-safe display."""
        return hashlib.sha256(ip_address.encode()).hexdigest()
