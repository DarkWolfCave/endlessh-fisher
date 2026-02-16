"""Custom template tags for Endlessh Fisher."""

import re

from django import template
from django.conf import settings
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()


# --- Language-aware mappings ---

_COUNTRY_NAMES_DE = {
    "AF": "Afghanistan", "AL": "Albanien", "DZ": "Algerien", "AD": "Andorra",
    "AO": "Angola", "AR": "Argentinien", "AM": "Armenien", "AU": "Australien",
    "AT": "Österreich", "AZ": "Aserbaidschan", "BH": "Bahrain", "BD": "Bangladesch",
    "BY": "Belarus", "BE": "Belgien", "BO": "Bolivien", "BA": "Bosnien und Herzegowina",
    "BR": "Brasilien", "BN": "Brunei", "BG": "Bulgarien", "KH": "Kambodscha",
    "CM": "Kamerun", "CA": "Kanada", "CL": "Chile", "CN": "China",
    "CO": "Kolumbien", "CR": "Costa Rica", "HR": "Kroatien", "CU": "Kuba",
    "CY": "Zypern", "CZ": "Tschechien", "DK": "Dänemark", "EC": "Ecuador",
    "EG": "Ägypten", "EE": "Estland", "ET": "Äthiopien", "FI": "Finnland",
    "FR": "Frankreich", "GE": "Georgien", "DE": "Deutschland", "GH": "Ghana",
    "GR": "Griechenland", "GP": "Guadeloupe", "GT": "Guatemala", "HK": "Hongkong",
    "HU": "Ungarn", "IS": "Island", "IN": "Indien", "ID": "Indonesien",
    "IR": "Iran", "IQ": "Irak", "IE": "Irland", "IL": "Israel",
    "IT": "Italien", "CI": "Elfenbeinküste", "JM": "Jamaika", "JP": "Japan",
    "JO": "Jordanien", "KZ": "Kasachstan", "KE": "Kenia", "KW": "Kuwait",
    "KG": "Kirgisistan", "LV": "Lettland", "LB": "Libanon", "LY": "Libyen",
    "LT": "Litauen", "LU": "Luxemburg", "MO": "Macau", "MY": "Malaysia",
    "MV": "Malediven", "ML": "Mali", "MT": "Malta", "MX": "Mexiko",
    "MD": "Moldawien", "MN": "Mongolei", "MA": "Marokko", "MZ": "Mosambik",
    "MM": "Myanmar", "NP": "Nepal", "NL": "Niederlande", "NZ": "Neuseeland",
    "NI": "Nicaragua", "NG": "Nigeria", "KP": "Nordkorea", "MK": "Nordmazedonien",
    "NO": "Norwegen", "OM": "Oman", "PK": "Pakistan", "PS": "Palästina",
    "PA": "Panama", "PY": "Paraguay", "PE": "Peru", "PH": "Philippinen",
    "PL": "Polen", "PT": "Portugal", "QA": "Katar", "RO": "Rumänien",
    "RU": "Russland", "SA": "Saudi-Arabien", "SN": "Senegal", "RS": "Serbien",
    "SC": "Seychellen", "SG": "Singapur", "SK": "Slowakei", "SI": "Slowenien",
    "SO": "Somalia", "ZA": "Südafrika", "KR": "Südkorea", "ES": "Spanien",
    "LK": "Sri Lanka", "SD": "Sudan", "SE": "Schweden", "CH": "Schweiz",
    "SY": "Syrien", "TW": "Taiwan", "TJ": "Tadschikistan", "TZ": "Tansania",
    "TH": "Thailand", "TN": "Tunesien", "TR": "Türkei", "TM": "Turkmenistan",
    "UG": "Uganda", "UA": "Ukraine", "AE": "Verein. Arab. Emirate", "GB": "Vereinigtes Königreich",
    "US": "Vereinigte Staaten", "UY": "Uruguay", "UZ": "Usbekistan", "VE": "Venezuela",
    "VN": "Vietnam", "YE": "Jemen", "ZM": "Sambia", "ZW": "Simbabwe",
}

_COUNTRY_NAMES_EN = {
    "AF": "Afghanistan", "AL": "Albania", "DZ": "Algeria", "AD": "Andorra",
    "AO": "Angola", "AR": "Argentina", "AM": "Armenia", "AU": "Australia",
    "AT": "Austria", "AZ": "Azerbaijan", "BH": "Bahrain", "BD": "Bangladesh",
    "BY": "Belarus", "BE": "Belgium", "BO": "Bolivia", "BA": "Bosnia and Herzegovina",
    "BR": "Brazil", "BN": "Brunei", "BG": "Bulgaria", "KH": "Cambodia",
    "CM": "Cameroon", "CA": "Canada", "CL": "Chile", "CN": "China",
    "CO": "Colombia", "CR": "Costa Rica", "HR": "Croatia", "CU": "Cuba",
    "CY": "Cyprus", "CZ": "Czechia", "DK": "Denmark", "EC": "Ecuador",
    "EG": "Egypt", "EE": "Estonia", "ET": "Ethiopia", "FI": "Finland",
    "FR": "France", "GE": "Georgia", "DE": "Germany", "GH": "Ghana",
    "GR": "Greece", "GP": "Guadeloupe", "GT": "Guatemala", "HK": "Hong Kong",
    "HU": "Hungary", "IS": "Iceland", "IN": "India", "ID": "Indonesia",
    "IR": "Iran", "IQ": "Iraq", "IE": "Ireland", "IL": "Israel",
    "IT": "Italy", "CI": "Ivory Coast", "JM": "Jamaica", "JP": "Japan",
    "JO": "Jordan", "KZ": "Kazakhstan", "KE": "Kenya", "KW": "Kuwait",
    "KG": "Kyrgyzstan", "LV": "Latvia", "LB": "Lebanon", "LY": "Libya",
    "LT": "Lithuania", "LU": "Luxembourg", "MO": "Macao", "MY": "Malaysia",
    "MV": "Maldives", "ML": "Mali", "MT": "Malta", "MX": "Mexico",
    "MD": "Moldova", "MN": "Mongolia", "MA": "Morocco", "MZ": "Mozambique",
    "MM": "Myanmar", "NP": "Nepal", "NL": "Netherlands", "NZ": "New Zealand",
    "NI": "Nicaragua", "NG": "Nigeria", "KP": "North Korea", "MK": "North Macedonia",
    "NO": "Norway", "OM": "Oman", "PK": "Pakistan", "PS": "Palestine",
    "PA": "Panama", "PY": "Paraguay", "PE": "Peru", "PH": "Philippines",
    "PL": "Poland", "PT": "Portugal", "QA": "Qatar", "RO": "Romania",
    "RU": "Russia", "SA": "Saudi Arabia", "SN": "Senegal", "RS": "Serbia",
    "SC": "Seychelles", "SG": "Singapore", "SK": "Slovakia", "SI": "Slovenia",
    "SO": "Somalia", "ZA": "South Africa", "KR": "South Korea", "ES": "Spain",
    "LK": "Sri Lanka", "SD": "Sudan", "SE": "Sweden", "CH": "Switzerland",
    "SY": "Syria", "TW": "Taiwan", "TJ": "Tajikistan", "TZ": "Tanzania",
    "TH": "Thailand", "TN": "Tunisia", "TR": "Turkey", "TM": "Turkmenistan",
    "UG": "Uganda", "UA": "Ukraine", "AE": "United Arab Emirates", "GB": "United Kingdom",
    "US": "United States", "UY": "Uruguay", "UZ": "Uzbekistan", "VE": "Venezuela",
    "VN": "Vietnam", "YE": "Yemen", "ZM": "Zambia", "ZW": "Zimbabwe",
}

_RARITY_NAMES = {
    "de": {
        "common": "Gewöhnlich",
        "uncommon": "Ungewöhnlich",
        "rare": "Selten",
        "epic": "Episch",
        "legendary": "Legendär",
        "mythic": "Mythisch",
    },
    "en": {
        "common": "Common",
        "uncommon": "Uncommon",
        "rare": "Rare",
        "epic": "Epic",
        "legendary": "Legendary",
        "mythic": "Mythic",
    },
}

_UNKNOWN = {"de": "Unbekannt", "en": "Unknown"}

# --- Static UI translations (DE key → EN value) ---

_TRANSLATIONS = {
    # Navigation
    "Fischlexikon": "Species Dex",
    "Bestenliste": "Leaderboard",
    "Schatzkammer": "Treasure Vault",
    "Weltkarte": "World Map",
    # Stats bar
    "Fische": "Fish",
    "Aktiv": "Active",
    "Verschwendet": "Wasted",
    "Länder": "Countries",
    # Dashboard
    "Live-Teich": "Live Pond",
    "Aktuell gefangene Bots": "Currently Trapped Bots",
    "Tägliche Herausforderungen": "Daily Challenges",
    "Angelteiche": "Fishing Ponds",
    "Live-Fänge": "Live Catches",
    "Statistiken": "Statistics",
    "Gesamt-Fänge": "Total Catches",
    "Aktuell in Falle": "Currently Trapped",
    "Verschwendete Zeit": "Wasted Time",
    "Verschiedene Länder": "Unique Countries",
    "Gesamt-Score": "Total Score",
    # Live Pond
    "Keine Fische in der Falle... noch nicht!": "No fish in the trap... yet!",
    "aktiv gefangen": "actively trapped",
    # Ticker / prepositions
    "aus": "from",
    "auf": "on",
    # Activity feed
    "Warte auf den ersten Fang...": "Waiting for the first catch...",
    # Daily challenges
    "Abgeschlossen!": "Completed!",
    "Keine Herausforderungen heute. Morgen gibt es neue!":
        "No challenges today. New ones tomorrow!",
    # Fish card / common labels
    "Trap-Zeit": "Trap Time",
    "Fänge": "Catches",
    # Rare alert
    "FANG!": "CATCH!",
    # Bestenliste
    "Längste Fänge": "Longest Catches",
    "Fischart": "Species",
    "Noch keine Fänge.": "No catches yet.",
    "Höchste Scores": "Highest Scores",
    "Rekorde pro Fischart": "Records by Species",
    "Pkt.": "pts.",
    # Species dex
    "Arten": "Species",
    "Fange sie alle!": "Catch them all!",
    "Noch nicht entdeckt...": "Not yet discovered...",
    "Gefangen": "Caught",
    "Rekord": "Record",
    "Bester Score": "Best Score",
    "Erstfang": "First Catch",
    "Noch nicht entdeckt": "Not yet discovered",
    # Fish detail
    "IP-Adresse": "IP Address",
    "Land": "Country",
    "Erstmals gesehen": "First Seen",
    "Andere Fänge von dieser IP": "Other catches from this IP",
    "Aquarium": "Aquarium",
    # Schatzkammer
    "Gesammelte Tipps & Entdeckungen": "Collected Tips & Discoveries",
    "Entdeckungsfortschritt": "Discovery Progress",
    "Gesammelte Sicherheitstipps": "Collected Security Tips",
    "Schätze gesammelt": "Treasures collected",
    "Tipps entdeckt": "Tips discovered",
    "Tipps gesamt": "Total tips",
    "Punkte verdient": "Points earned",
    "Punkte gesammelt": "Points collected",
    "Noch keine Schätze gesammelt.": "No treasures collected yet.",
    "Schätze erscheinen zufällig im Live-Teich":
        "Treasures appear randomly in the Live Pond",
    "klicke sie an, um Sicherheitstipps zu entdecken!":
        "click them to discover security tips!",
    # World map
    "Angriffe nach Land": "Attacks by Country",
    "Letzter Fang": "Last Catch",
    "Noch keine Länderdaten verfügbar.": "No country data available yet.",
    # Server detail
    "Einzigartige IPs": "Unique IPs",
    "Gefangene Arten": "Caught Species",
    "Letzte Fänge": "Recent Catches",
    "Noch keine Fänge auf diesem Server.": "No catches on this server yet.",
    # Aquarium
    "Filter": "Filter",
    "Alle anzeigen": "Show all",
    "Noch keine Fische gefangen.": "No fish caught yet.",
    "Die Celery-Pipeline synct alle 5 Minuten neue Daten.":
        "The Celery pipeline syncs new data every 5 minutes.",
    # Achievements
    "Freigeschaltet:": "Unlocked:",
    "Punkte:": "Points:",
    "Geheim": "Secret",
    "Punkte": "Points",
    "Schwellwert": "Threshold",
    "Freigeschaltet am": "Unlocked on",
    "Wie schaltet man das frei?": "How do you unlock this?",
    # IP Lookup
    "IP analysieren": "Analyze IP",
    "IP-Analyse": "IP Analysis",
    "Offene Ports": "Open Ports",
    "Keine offenen Ports gefunden": "No open ports found",
    "Dienste": "Services",
    "Schwachstellen": "Vulnerabilities",
    "Missbrauchsbewertung": "Abuse Score",
    "Berichte": "Reports",
    "von Nutzern": "from users",
    "Anbieter": "Provider",
    "Nutzungstyp": "Usage Type",
    "Tor-Exit-Node": "Tor Exit Node",
    "Ja": "Yes",
    "Nein": "No",
    "Zuletzt gemeldet": "Last Reported",
    "AbuseIPDB nicht konfiguriert": "AbuseIPDB not configured",
    "AbuseIPDB Limit erreicht — bitte später erneut versuchen": "AbuseIPDB rate limit reached — please try again later",
    "AbuseIPDB Zeitüberschreitung — Server nicht erreichbar": "AbuseIPDB timeout — server unreachable",
    "AbuseIPDB Fehler — Daten konnten nicht abgerufen werden": "AbuseIPDB error — could not retrieve data",
    "Keine Daten für private IPs": "No data for private IPs",
    "Ungültige IP-Adresse": "Invalid IP address",
    "Zu viele Anfragen — bitte kurz warten": "Too many requests — please wait",
    "Keine Daten verfügbar": "No data available",
    "Aus Cache": "From cache",
    # Misc
    "Klicken zum Kopieren": "Click to copy",
    # Notifications
    "Nachrichten": "Messages",
    "Alle gelesen": "Mark All Read",
    "Keine Nachrichten.": "No messages.",
    "Gelesen": "Read",
    "Löschen": "Delete",
    "Wirklich löschen?": "Really delete?",
    "ungelesen": "unread",
    "Achievement": "Achievement",
    "Herausforderung": "Challenge",
    "Seltener Fang": "Rare Catch",
    "Alle löschen": "Delete All",
    "Wirklich alle Nachrichten löschen?": "Really delete all messages?",
}


def _lang():
    """Return current game language."""
    return getattr(settings, "GAME_LANGUAGE", "de")


def get_country_name(code, lang=None):
    """Translate ISO country code to localized name. Used by filters and services."""
    lang = lang or _lang()
    if not code:
        return _UNKNOWN.get(lang, "Unknown")
    mapping = _COUNTRY_NAMES_DE if lang == "de" else _COUNTRY_NAMES_EN
    return mapping.get(code.upper(), code)


def get_rarity_name(rarity, lang=None):
    """Translate rarity key to localized name. Used by filters and services."""
    lang = lang or _lang()
    if not rarity:
        return _UNKNOWN.get(lang, "Unknown")
    names = _RARITY_NAMES.get(lang, _RARITY_NAMES["en"])
    return names.get(rarity.lower(), rarity.capitalize())


# --- Template filters ---

@register.filter
def t(text):
    """Translate static UI text. German is the key, English the value.

    Usage: {{ "Fischlexikon"|t }}
    Returns English when GAME_LANGUAGE=en, otherwise returns the input unchanged.
    """
    if not text:
        return ""
    if _lang() == "en":
        return _TRANSLATIONS.get(str(text), str(text))
    return str(text)


@register.filter
def country_de(code):
    """Translate country code respecting GAME_LANGUAGE."""
    return get_country_name(code)


@register.filter
def rarity_de(rarity):
    """Translate rarity respecting GAME_LANGUAGE."""
    return get_rarity_name(rarity)


@register.filter
def lang(obj, field):
    """Return localized field from a model instance.

    Usage: {{ species|lang:"name" }} → species.name_de (German) or species.name (English)
    Works with any model that has field + field_de pairs.
    Falls back gracefully: de→field_de→field, en→field→field_de.
    """
    if obj is None:
        return ""
    game_lang = _lang()
    if game_lang == "de":
        val = getattr(obj, f"{field}_de", None)
        if val:
            return val
    val = getattr(obj, field, None)
    if val:
        return val
    return getattr(obj, f"{field}_de", "")


@register.filter
def lang_dict(d, field):
    """Return localized field from a dict (e.g. values() queryset result).

    Usage: {{ sp|lang_dict:"species__name" }} → sp["species__name_de"] or sp["species__name"]
    """
    if not d or not isinstance(d, dict):
        return ""
    game_lang = _lang()
    if game_lang == "de":
        val = d.get(f"{field}_de")
        if val:
            return val
    val = d.get(field)
    if val:
        return val
    return d.get(f"{field}_de", "")


@register.filter
def duration_format(seconds):
    """Format seconds into human-readable duration."""
    if not seconds:
        return "0s"
    try:
        seconds = float(seconds)
    except (ValueError, TypeError):
        return "0s"
    if seconds < 60:
        return f"{seconds:.0f}s"
    if seconds < 3600:
        minutes = seconds / 60
        return f"{minutes:.1f}min"
    if seconds < 86400:
        hours = seconds / 3600
        return f"{hours:.1f}h"
    days = seconds / 86400
    return f"{days:.1f}d"


@register.filter
def rarity_color(rarity):
    """Return CSS color class for fish rarity."""
    colors = {
        "common": "text-gray-400",
        "uncommon": "text-green-400",
        "rare": "text-blue-400",
        "epic": "text-purple-400",
        "legendary": "text-yellow-400",
        "mythic": "text-red-500",
    }
    return colors.get(rarity, "text-gray-400")


@register.filter
def score_format(score):
    """Format score with thousand separators."""
    if not score and score != 0:
        return "0"
    try:
        return f"{int(score):,}".replace(",", ".")
    except (ValueError, TypeError):
        return "0"


_SPECIES_EMOJI = {
    "fish-plankton": "\U0001F9A0",
    "fish-sardine": "\U0001F41F",
    "fish-anchovy": "\U0001F41F",
    "fish-trout": "\U0001F41F",
    "fish-pike": "\U0001F988",
    "fish-salmon": "\U0001F420",
    "fish-tuna": "\U0001F420",
    "fish-swordfish": "\U0001F42C",
    "fish-marlin": "\U0001F42C",
    "fish-whale-shark": "\U0001F40B",
    "fish-kraken": "\U0001F419",
    "fish-leviathan": "\U0001F409",
}


@register.filter
def species_emoji(css_class):
    """Return emoji for a fish species by its css_class."""
    return _SPECIES_EMOJI.get(css_class, "\U0001F41F")


_BACKTICK_RE = re.compile(r"`([^`]+)`")


@register.filter(needs_autoescape=True)
def format_code(text, autoescape=True):
    """Convert `backtick` notation to clickable <code> tags.

    Text is HTML-escaped first, then backtick patterns are replaced
    with styled <code> elements that copy on click.
    """
    if not text:
        return ""
    escaped = escape(text) if autoescape else text
    tip_title = "Click to copy" if _lang() == "en" else "Klicken zum Kopieren"
    result = _BACKTICK_RE.sub(
        f'<code class="tip-code" title="{tip_title}" '
        "onclick='navigator.clipboard.writeText(this.textContent)'>"
        r"\1</code>",
        escaped,
    )
    return mark_safe(result)
