"""Seed data for fish species and servers. Used by data migrations."""

FISH_SPECIES = [
    {
        "slug": "plankton",
        "name": "Plankton",
        "name_de": "Plankton",
        "description": "Barely a blip on the radar. Gone before you noticed.",
        "description_de": "Kaum ein Blip auf dem Radar. Weg, bevor du es bemerkst.",
        "min_trapped_seconds": 0,
        "max_trapped_seconds": 30,
        "rarity": "common",
        "rarity_color": "#9CA3AF",
        "points": 1,
        "css_class": "fish-plankton",
        "sort_order": 1,
    },
    {
        "slug": "sardine",
        "name": "Sardine",
        "name_de": "Sardine",
        "description": "A tiny catch, but every fisher starts somewhere.",
        "description_de": "Ein winziger Fang, aber jeder Angler fängt mal klein an.",
        "min_trapped_seconds": 30,
        "max_trapped_seconds": 120,
        "rarity": "common",
        "rarity_color": "#60A5FA",
        "points": 2,
        "css_class": "fish-sardine",
        "sort_order": 2,
    },
    {
        "slug": "anchovy",
        "name": "Anchovy",
        "name_de": "Sardelle",
        "description": "Small but feisty. Took the bait and struggled a bit.",
        "description_de": "Klein aber zappelig. Hat angebissen und etwas gekämpft.",
        "min_trapped_seconds": 120,
        "max_trapped_seconds": 600,
        "rarity": "common",
        "rarity_color": "#34D399",
        "points": 5,
        "css_class": "fish-anchovy",
        "sort_order": 3,
    },
    {
        "slug": "trout",
        "name": "Rainbow Trout",
        "name_de": "Regenbogenforelle",
        "description": "A respectable catch! This one put up a decent fight.",
        "description_de": "Ein respektabler Fang! Dieser hat ordentlich gekämpft.",
        "min_trapped_seconds": 600,
        "max_trapped_seconds": 1800,
        "rarity": "uncommon",
        "rarity_color": "#A78BFA",
        "points": 10,
        "css_class": "fish-trout",
        "sort_order": 4,
    },
    {
        "slug": "pike",
        "name": "Northern Pike",
        "name_de": "Hecht",
        "description": "The predator became the prey. A satisfying reversal.",
        "description_de": "Der Räuber wurde zur Beute. Eine befriedigende Wendung.",
        "min_trapped_seconds": 1800,
        "max_trapped_seconds": 3600,
        "rarity": "uncommon",
        "rarity_color": "#F472B6",
        "points": 20,
        "css_class": "fish-pike",
        "sort_order": 5,
    },
    {
        "slug": "salmon",
        "name": "Atlantic Salmon",
        "name_de": "Atlantischer Lachs",
        "description": "A prized catch! Hours of wasted bot resources.",
        "description_de": "Ein Prachtfang! Stunden verschwendeter Bot-Ressourcen.",
        "min_trapped_seconds": 3600,
        "max_trapped_seconds": 14400,
        "rarity": "rare",
        "rarity_color": "#FB923C",
        "points": 50,
        "css_class": "fish-salmon",
        "sort_order": 6,
    },
    {
        "slug": "tuna",
        "name": "Bluefin Tuna",
        "name_de": "Thunfisch",
        "description": "Hours of trapped time. This bot's operator is losing money.",
        "description_de": "Stunden in der Falle. Dieser Bot-Betreiber verliert Geld.",
        "min_trapped_seconds": 14400,
        "max_trapped_seconds": 43200,
        "rarity": "rare",
        "rarity_color": "#F87171",
        "points": 100,
        "css_class": "fish-tuna",
        "sort_order": 7,
    },
    {
        "slug": "swordfish",
        "name": "Swordfish",
        "name_de": "Schwertfisch",
        "description": "A majestic beast! A full day trapped in our net.",
        "description_de": "Ein majestätisches Biest! Einen ganzen Tag in unserem Netz.",
        "min_trapped_seconds": 43200,
        "max_trapped_seconds": 86400,
        "rarity": "epic",
        "rarity_color": "#FBBF24",
        "points": 250,
        "css_class": "fish-swordfish",
        "sort_order": 8,
    },
    {
        "slug": "marlin",
        "name": "Blue Marlin",
        "name_de": "Blauer Marlin",
        "description": "The stuff of legends! Days wasted on our tarpit.",
        "description_de": "Der Stoff aus dem Legenden sind! Tage in unserem Tarpit.",
        "min_trapped_seconds": 86400,
        "max_trapped_seconds": 259200,
        "rarity": "epic",
        "rarity_color": "#818CF8",
        "points": 500,
        "css_class": "fish-marlin",
        "sort_order": 9,
    },
    {
        "slug": "whale-shark",
        "name": "Whale Shark",
        "name_de": "Walhai",
        "description": "Incredible! Days of trapped time. The bot forgot it exists.",
        "description_de": "Unglaublich! Tage in der Falle. Der Bot hat vergessen, dass er existiert.",
        "min_trapped_seconds": 259200,
        "max_trapped_seconds": 604800,
        "rarity": "legendary",
        "rarity_color": "#2DD4BF",
        "points": 1000,
        "css_class": "fish-whale-shark",
        "sort_order": 10,
    },
    {
        "slug": "kraken",
        "name": "Kraken",
        "name_de": "Kraken",
        "description": "A mythical creature from the deep! Weeks of wasted compute.",
        "description_de": "Ein mythisches Wesen aus der Tiefe! Wochen verschwendeter Rechenzeit.",
        "min_trapped_seconds": 604800,
        "max_trapped_seconds": 1209600,
        "rarity": "legendary",
        "rarity_color": "#E879F9",
        "points": 2500,
        "css_class": "fish-kraken",
        "sort_order": 11,
    },
    {
        "slug": "leviathan",
        "name": "Leviathan",
        "name_de": "Leviathan",
        "description": "THE ULTIMATE CATCH. Over two weeks trapped. This bot is never coming back.",
        "description_de": "DER ULTIMATIVE FANG. Über zwei Wochen gefangen. Dieser Bot kommt nie wieder.",
        "min_trapped_seconds": 1209600,
        "max_trapped_seconds": None,
        "rarity": "mythic",
        "rarity_color": "#FF0040",
        "points": 5000,
        "css_class": "fish-leviathan",
        "sort_order": 12,
    },
]

TREASURE_TYPES = [
    {
        "slug": "driftwood",
        "name": "Driftwood",
        "name_de": "Treibholz",
        "description_de": "Altes Treibholz, ans Ufer gespült.",
        "emoji": "\U0001FAB5",
        "rarity": "common",
        "rarity_color": "#9CA3AF",
        "points": 5,
        "spawn_weight": 100,
        "min_pond_percentile": 0,
        "sort_order": 1,
    },
    {
        "slug": "sea-glass",
        "name": "Sea Glass",
        "name_de": "Seeglas",
        "description_de": "Vom Meer geschliffenes Glas, glänzt im Licht.",
        "emoji": "\U0001F48E",
        "rarity": "common",
        "rarity_color": "#60A5FA",
        "points": 8,
        "spawn_weight": 80,
        "min_pond_percentile": 10,
        "sort_order": 2,
    },
    {
        "slug": "pearl",
        "name": "Pearl",
        "name_de": "Perle",
        "description_de": "Eine schimmernde Perle aus einer Muschel.",
        "emoji": "\U0001FAE7",
        "rarity": "uncommon",
        "rarity_color": "#E2E8F0",
        "points": 15,
        "spawn_weight": 40,
        "min_pond_percentile": 20,
        "sort_order": 3,
    },
    {
        "slug": "starfish",
        "name": "Starfish",
        "name_de": "Seestern",
        "description_de": "Ein fünfarmiger Seestern in leuchtenden Farben.",
        "emoji": "\u2B50",
        "rarity": "uncommon",
        "rarity_color": "#FBBF24",
        "points": 20,
        "spawn_weight": 30,
        "min_pond_percentile": 30,
        "sort_order": 4,
    },
    {
        "slug": "anchor",
        "name": "Anchor",
        "name_de": "Anker",
        "description_de": "Ein alter Schiffsanker aus vergessenen Zeiten.",
        "emoji": "\u2693",
        "rarity": "rare",
        "rarity_color": "#60A5FA",
        "points": 40,
        "spawn_weight": 15,
        "min_pond_percentile": 45,
        "sort_order": 5,
    },
    {
        "slug": "message-bottle",
        "name": "Message in a Bottle",
        "name_de": "Flaschenpost",
        "description_de": "Eine Nachricht in einer Flasche. Wer hat sie geschrieben?",
        "emoji": "\U0001F9F4",
        "rarity": "common",
        "rarity_color": "#34D399",
        "points": 15,
        "spawn_weight": 60,
        "min_pond_percentile": 0,
        "preferred_tip_types": "article,promo",
        "sort_order": 6,
    },
    {
        "slug": "coral-crown",
        "name": "Coral Crown",
        "name_de": "Korallenkrone",
        "description_de": "Eine Krone aus seltenen Korallen, wie für einen Meeresgott.",
        "emoji": "\U0001F451",
        "rarity": "epic",
        "rarity_color": "#A78BFA",
        "points": 100,
        "spawn_weight": 5,
        "min_pond_percentile": 70,
        "sort_order": 7,
    },
    {
        "slug": "trident",
        "name": "Trident",
        "name_de": "Dreizack",
        "description_de": "Poseidons verlorener Dreizack. Strahlt vor Macht.",
        "emoji": "\U0001F531",
        "rarity": "epic",
        "rarity_color": "#818CF8",
        "points": 150,
        "spawn_weight": 3,
        "min_pond_percentile": 80,
        "sort_order": 8,
    },
    {
        "slug": "golden-compass",
        "name": "Golden Compass",
        "name_de": "Goldener Kompass",
        "description_de": "Ein goldener Kompass, der immer nach Norden zeigt... oder doch nicht?",
        "emoji": "\U0001F9ED",
        "rarity": "legendary",
        "rarity_color": "#FBBF24",
        "points": 300,
        "spawn_weight": 1,
        "min_pond_percentile": 93,
        "sort_order": 9,
    },
    {
        "slug": "wolf-head",
        "name": "Wolf Head",
        "name_de": "Wolfskopf",
        "description_de": "Der Wolfskopf — ein uraltes Symbol der digitalen Wildnis. Nur die geduldigsten Angler finden ihn.",
        "emoji": "\U0001F43A",
        "rarity": "legendary",
        "rarity_color": "#FF6B35",
        "points": 500,
        "spawn_weight": 1,
        "min_pond_percentile": 98,
        "sort_order": 10,
    },
]

SECURITY_TIPS = [
    # --- Common (8): SSH & Server Basics ---
    {
        "slug": "ssh-keys-statt-passwoerter",
        "title": "SSH Keys Instead of Passwords",
        "title_de": "SSH-Schlüssel statt Passwörter",
        "content": (
            "Disable password authentication in `/etc/ssh/sshd_config` with "
            "`PasswordAuthentication no`. Use Ed25519 keys instead "
            "(`ssh-keygen -t ed25519`). SSH keys are virtually uncrackable and "
            "protect against brute-force attacks — exactly the kind endlessh traps."
        ),
        "content_de": (
            "Deaktiviere Passwort-Authentifizierung in `/etc/ssh/sshd_config` mit "
            "`PasswordAuthentication no`. Nutze stattdessen Ed25519-Keys "
            "(`ssh-keygen -t ed25519`). SSH-Keys sind praktisch unknackbar und "
            "schützen gegen Brute-Force-Angriffe — genau die, die endlessh abfängt."
        ),
        "source_url": "https://darkwolfcave.de/ssh-server-absichern-komplettanleitung/",
        "source_label": "DarkWolfCave — Hardening SSH Servers",
        "source_label_de": "DarkWolfCave — SSH-Server absichern",
        "rarity": "common",
        "category": "ssh",
        "emoji": "\U0001F511",
        "sort_order": 1,
    },
    {
        "slug": "root-login-deaktivieren",
        "title": "Disable Root Login via SSH",
        "title_de": "Root-Login über SSH deaktivieren",
        "content": (
            "Set `PermitRootLogin no` in `/etc/ssh/sshd_config`. Use a regular user "
            "with sudo privileges instead. Over 90% of SSH brute-force attacks target "
            "the root account — a single switch eliminates this entire attack vector."
        ),
        "content_de": (
            "Setze `PermitRootLogin no` in `/etc/ssh/sshd_config`. Nutze stattdessen "
            "einen normalen User mit sudo-Rechten. Über 90% der SSH-Brute-Force-"
            "Angriffe zielen auf den root-Account — ein einfacher Schalter eliminiert "
            "diesen gesamten Angriffsvektor."
        ),
        "source_url": "https://darkwolfcave.de/ssh-server-absichern-komplettanleitung/",
        "source_label": "DarkWolfCave — Hardening SSH Servers",
        "source_label_de": "DarkWolfCave — SSH-Server absichern",
        "rarity": "common",
        "category": "ssh",
        "emoji": "\U0001F6AB",
        "sort_order": 2,
    },
    {
        "slug": "ssh-port-aendern",
        "title": "Change SSH Port",
        "title_de": "SSH-Port ändern",
        "content": (
            "Change the default port 22 to a high port (e.g. 2222) with "
            "`Port 2222` in `/etc/ssh/sshd_config`. This won't stop targeted attacks, "
            "but reduces automated scans by over 95%. Combined with endlessh "
            "on port 22, it's an ideal combination."
        ),
        "content_de": (
            "Ändere den Standard-Port 22 auf einen hohen Port (z.B. 2222) mit "
            "`Port 2222` in `/etc/ssh/sshd_config`. Das stoppt keine gezielten Angriffe, "
            "reduziert aber automatisierte Scans um über 95%. Zusammen mit endlessh "
            "auf Port 22 eine ideale Kombination."
        ),
        "source_url": "https://darkwolfcave.de/ssh-server-absichern-komplettanleitung/",
        "source_label": "DarkWolfCave — Hardening SSH Servers",
        "source_label_de": "DarkWolfCave — SSH-Server absichern",
        "rarity": "common",
        "category": "ssh",
        "emoji": "\U0001F6AA",
        "sort_order": 3,
    },
    {
        "slug": "automatische-updates",
        "title": "Automatic Security Updates",
        "title_de": "Automatische Sicherheitsupdates",
        "content": (
            "Enable unattended-upgrades: "
            "`apt install unattended-upgrades && dpkg-reconfigure -plow unattended-upgrades`. "
            "Critical security patches are applied automatically. Unpatched systems are "
            "the most common attack vector — automation closes this window."
        ),
        "content_de": (
            "Aktiviere unattended-upgrades: "
            "`apt install unattended-upgrades && dpkg-reconfigure -plow unattended-upgrades`. "
            "Kritische Sicherheitspatches werden automatisch eingespielt. Der häufigste "
            "Angriffsvektor sind ungepatchte Systeme — Automatisierung schließt dieses Zeitfenster."
        ),
        "source_url": "https://darkwolfcave.de/server-monitoring-intrusion-detection-linux/",
        "source_label": "DarkWolfCave — Server Monitoring",
        "source_label_de": "DarkWolfCave — Server-Monitoring",
        "rarity": "common",
        "category": "updates",
        "emoji": "\U0001F504",
        "sort_order": 4,
    },
    {
        "slug": "firewall-aktivieren",
        "title": "Enable Firewall (ufw/nftables)",
        "title_de": "Firewall mit ufw aktivieren",
        "content": (
            "Enable a firewall and only allow required ports: "
            "`ufw default deny incoming && ufw allow ssh && ufw enable`. "
            "Since 2024, nftables is the default backend for ufw/iptables. "
            "Every open port is an invitation — restrict them to the minimum."
        ),
        "content_de": (
            "Aktiviere eine Firewall und erlaube nur benötigte Ports: "
            "`ufw default deny incoming && ufw allow ssh && ufw enable`. "
            "Seit 2024 ist nftables das Standard-Backend für ufw/iptables. "
            "Jeder offene Port ist eine Einladung — beschränke sie auf das Minimum."
        ),
        "source_url": "https://darkwolfcave.de/netzwerk-sicherheit-firewall-zero-trust/",
        "source_label": "DarkWolfCave — Network Security",
        "source_label_de": "DarkWolfCave — Netzwerk-Sicherheit",
        "rarity": "common",
        "category": "firewall",
        "emoji": "\U0001F6E1\uFE0F",
        "sort_order": 5,
    },
    {
        "slug": "fail2ban-crowdsec",
        "title": "fail2ban or CrowdSec",
        "title_de": "fail2ban oder CrowdSec einsetzen",
        "content": (
            "Install fail2ban (`apt install fail2ban`) or the more modern CrowdSec. "
            "Both automatically block IPs after multiple failed login attempts. "
            "CrowdSec shares threat intelligence with the community and "
            "provides collaborative defense."
        ),
        "content_de": (
            "Installiere fail2ban (`apt install fail2ban`) oder das modernere CrowdSec. "
            "Beide sperren IPs nach mehreren fehlgeschlagenen Login-Versuchen "
            "automatisch. CrowdSec teilt Bedrohungsdaten mit der Community und "
            "bietet eine kollaborative Verteidigung."
        ),
        "source_url": "https://darkwolfcave.de/netzwerk-sicherheit-firewall-zero-trust/",
        "source_label": "DarkWolfCave — Network Security",
        "source_label_de": "DarkWolfCave — Netzwerk-Sicherheit",
        "rarity": "common",
        "category": "firewall",
        "emoji": "\U0001F46E",
        "sort_order": 6,
    },
    {
        "slug": "dienste-deaktivieren",
        "title": "Disable Unnecessary Services",
        "title_de": "Nicht benötigte Dienste deaktivieren",
        "content": (
            "List active services with "
            "`systemctl list-units --type=service --state=running` "
            "and disable unnecessary ones with `systemctl disable --now <service>`. "
            "Every running service is a potential attack surface. "
            "The principle of minimal attack surface is one of the most effective "
            "security measures."
        ),
        "content_de": (
            "Liste aktive Dienste mit "
            "`systemctl list-units --type=service --state=running` "
            "und deaktiviere unnötige mit `systemctl disable --now <dienst>`. "
            "Jeder laufende Dienst ist eine potenzielle Angriffsfläche. "
            "Das Prinzip der minimalen Angriffsfläche ist eine der effektivsten "
            "Sicherheitsmaßnahmen."
        ),
        "source_url": "https://darkwolfcave.de/linux-server-haerten-angriffflaeche-minimieren/",
        "source_label": "DarkWolfCave — Hardening Linux Servers",
        "source_label_de": "DarkWolfCave — Linux-Server härten",
        "rarity": "common",
        "category": "strategy",
        "emoji": "\u2702\uFE0F",
        "sort_order": 7,
    },
    {
        "slug": "ssh-algorithmen-haerten",
        "title": "Harden SSH Algorithms",
        "title_de": "SSH-Algorithmen härten",
        "content": (
            "Only use modern algorithms in sshd_config: "
            "`KexAlgorithms curve25519-sha256` and "
            "`Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com`. "
            "Legacy algorithms like SHA1 and CBC ciphers are cryptographically "
            "broken. `ssh-audit` (github.com/jtesta/ssh-audit) checks your configuration."
        ),
        "content_de": (
            "Nutze nur moderne Algorithmen in sshd_config: "
            "`KexAlgorithms curve25519-sha256` und "
            "`Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com`. "
            "Alte Algorithmen wie SHA1 und CBC-Ciphers sind kryptographisch "
            "gebrochen. `ssh-audit` (github.com/jtesta/ssh-audit) prüft deine Konfiguration."
        ),
        "source_url": "https://darkwolfcave.de/ssh-server-absichern-komplettanleitung/",
        "source_label": "DarkWolfCave — Hardening SSH Servers",
        "source_label_de": "DarkWolfCave — SSH-Server absichern",
        "rarity": "common",
        "category": "ssh",
        "emoji": "\U0001F510",
        "sort_order": 8,
    },
    # --- Uncommon (6): Intermediate ---
    {
        "slug": "ssh-allowusers",
        "title": "SSH AllowUsers/AllowGroups",
        "title_de": "SSH-Zugang auf bestimmte User beschränken",
        "content": (
            "Restrict SSH access to specific users: `AllowUsers admin deploy` "
            "or `AllowGroups ssh-users` in sshd_config. Even if an attacker "
            "has valid credentials — without being on the allow list, they can't "
            "get in. A simple but powerful whitelist strategy."
        ),
        "content_de": (
            "Beschränke SSH-Zugang auf bestimmte User: `AllowUsers admin deploy` "
            "oder `AllowGroups ssh-users` in sshd_config. Selbst wenn ein Angreifer "
            "gültige Credentials hat — ohne in der Allow-Liste zu stehen, kommt er "
            "nicht rein. Eine einfache aber mächtige Whitelist-Strategie."
        ),
        "source_url": "https://darkwolfcave.de/ssh-server-absichern-komplettanleitung/",
        "source_label": "DarkWolfCave — Hardening SSH Servers",
        "source_label_de": "DarkWolfCave — SSH-Server absichern",
        "rarity": "uncommon",
        "category": "ssh",
        "emoji": "\U0001F4CB",
        "sort_order": 9,
    },
    {
        "slug": "ssh-2fa",
        "title": "Two-Factor Authentication for SSH",
        "title_de": "Zwei-Faktor-Authentifizierung für SSH",
        "content": (
            "Set up TOTP for SSH: `apt install libpam-google-authenticator`, "
            "then run `google-authenticator` and configure PAM in `/etc/pam.d/sshd`. "
            "SSH key + TOTP = two independent factors. "
            "Even with a stolen key, no access without the second factor."
        ),
        "content_de": (
            "Richte TOTP für SSH ein: `apt install libpam-google-authenticator`, "
            "dann `google-authenticator` ausführen und PAM in `/etc/pam.d/sshd` "
            "konfigurieren. SSH-Key + TOTP = zwei unabhängige Faktoren. "
            "Selbst bei gestohlenem Key kein Zugang ohne den zweiten Faktor."
        ),
        "source_url": "https://darkwolfcave.de/ssh-server-absichern-komplettanleitung/",
        "source_label": "DarkWolfCave — Hardening SSH Servers",
        "source_label_de": "DarkWolfCave — SSH-Server absichern",
        "rarity": "uncommon",
        "category": "auth",
        "emoji": "\U0001F4F1",
        "sort_order": 10,
    },
    {
        "slug": "audit-logging",
        "title": "Audit Logging with auditd",
        "title_de": "Audit-Logging mit auditd aktivieren",
        "content": (
            "Install auditd (`apt install auditd`) and monitor critical "
            "files: `auditctl -w /etc/ssh/sshd_config -p wa -k ssh_config`. "
            "Logs in `/var/log/audit/audit.log` show who changed what and when. "
            "Essential for forensic analysis after an incident."
        ),
        "content_de": (
            "Installiere auditd (`apt install auditd`) und überwache kritische "
            "Dateien: `auditctl -w /etc/ssh/sshd_config -p wa -k ssh_config`. "
            "Logs in `/var/log/audit/audit.log` zeigen wer wann was geändert hat. "
            "Unverzichtbar für forensische Analyse nach einem Vorfall."
        ),
        "source_url": "https://darkwolfcave.de/server-monitoring-intrusion-detection-linux/",
        "source_label": "DarkWolfCave — Server Monitoring",
        "source_label_de": "DarkWolfCave — Server-Monitoring",
        "rarity": "uncommon",
        "category": "monitoring",
        "emoji": "\U0001F4DD",
        "sort_order": 11,
    },
    {
        "slug": "lynis-security-audit",
        "title": "Security Audit with Lynis",
        "title_de": "Sicherheitsaudit mit Lynis",
        "content": (
            "Run `lynis audit system` regularly. Lynis checks over 300 "
            "security aspects: file permissions, kernel parameters, "
            "network configuration, installed packages. The hardening index "
            "gives you a concrete score — aim for above 80 points."
        ),
        "content_de": (
            "Führe regelmäßig `lynis audit system` aus. Lynis prüft über 300 "
            "Sicherheitsaspekte: Dateiberechtigungen, Kernel-Parameter, "
            "Netzwerk-Konfiguration, installierte Pakete. Der Hardening-Index "
            "gibt dir einen konkreten Score — Ziel: über 80 Punkte."
        ),
        "source_url": "https://darkwolfcave.de/server-monitoring-intrusion-detection-linux/",
        "source_label": "DarkWolfCave — Server Monitoring",
        "source_label_de": "DarkWolfCave — Server-Monitoring",
        "rarity": "uncommon",
        "category": "monitoring",
        "emoji": "\U0001F50D",
        "sort_order": 12,
    },
    {
        "slug": "backup-321-regel",
        "title": "Backup Strategy: 3-2-1 Rule",
        "title_de": "Backup-Strategie: 3-2-1-Regel",
        "content": (
            "3 copies of your data, on 2 different media, with 1 offsite. "
            "Use `restic` or `borgbackup` for encrypted, deduplicated backups. "
            "Test restores regularly — a backup that doesn't work "
            "isn't a backup. Ransomware makes backups a matter of survival."
        ),
        "content_de": (
            "3 Kopien deiner Daten, auf 2 verschiedenen Medien, davon 1 offsite. "
            "Nutze `restic` oder `borgbackup` für verschlüsselte, deduplizierte Backups. "
            "Teste regelmäßig die Wiederherstellung — ein Backup das nicht "
            "funktioniert ist keines. Ransomware macht Backups zur Überlebensfrage."
        ),
        "source_url": "https://darkwolfcave.de/backup-strategie-defense-in-depth-sicherheit/",
        "source_label": "DarkWolfCave — Backup & Security Strategy",
        "source_label_de": "DarkWolfCave — Backup & Sicherheitsstrategie",
        "rarity": "uncommon",
        "category": "strategy",
        "emoji": "\U0001F4BE",
        "sort_order": 13,
    },
    {
        "slug": "ssh-idle-timeout",
        "title": "SSH Idle Timeout",
        "title_de": "SSH-Idle-Timeout konfigurieren",
        "content": (
            "Set `ClientAliveInterval 300` and `ClientAliveCountMax 2` in "
            "sshd_config. Idle SSH sessions are disconnected after 10 minutes. "
            "Prevents forgotten open terminals — a common security "
            "risk, especially when someone leaves their workstation."
        ),
        "content_de": (
            "Setze `ClientAliveInterval 300` und `ClientAliveCountMax 2` in "
            "sshd_config. Inaktive SSH-Sessions werden nach 10 Minuten getrennt. "
            "Verhindert vergessene offene Terminals — ein häufiges Sicherheits"
            "risiko, besonders wenn jemand den Arbeitsplatz verlässt."
        ),
        "source_url": "https://darkwolfcave.de/ssh-server-absichern-komplettanleitung/",
        "source_label": "DarkWolfCave — Hardening SSH Servers",
        "source_label_de": "DarkWolfCave — SSH-Server absichern",
        "rarity": "uncommon",
        "category": "ssh",
        "emoji": "\u23F0",
        "sort_order": 14,
    },
    # --- Rare (5): Advanced ---
    {
        "slug": "ssh-certificate-authority",
        "title": "SSH Certificate Authority",
        "title_de": "SSH Certificate Authority einrichten",
        "content": (
            "Instead of distributing public keys to every server, use an "
            "SSH CA: `ssh-keygen -f ca_key` and then "
            "`ssh-keygen -s ca_key -I user_id -n username user_key.pub`. "
            "Certificates can be time-limited (`-V +52w`) and centrally "
            "revoked. Scales much better than authorized_keys."
        ),
        "content_de": (
            "Statt einzelne Public Keys auf jedem Server zu verteilen, nutze eine "
            "SSH-CA: `ssh-keygen -f ca_key` und dann "
            "`ssh-keygen -s ca_key -I user_id -n username user_key.pub`. "
            "Zertifikate können zeitlich begrenzt werden (`-V +52w`) und zentral "
            "widerrufen. Skaliert besser als authorized_keys."
        ),
        "source_url": "https://darkwolfcave.de/ssh-server-absichern-komplettanleitung/",
        "source_label": "DarkWolfCave — Hardening SSH Servers",
        "source_label_de": "DarkWolfCave — SSH-Server absichern",
        "rarity": "rare",
        "category": "ssh",
        "emoji": "\U0001F3DB\uFE0F",
        "sort_order": 15,
    },
    {
        "slug": "intrusion-detection-aide",
        "title": "Intrusion Detection with AIDE",
        "title_de": "Intrusion Detection mit AIDE",
        "content": (
            "AIDE (Advanced Intrusion Detection Environment) monitors file "
            "integrity: `aideinit && cp /var/lib/aide/aide.db.new /var/lib/aide/"
            "aide.db`, then regularly run `aide --check`. Detects unauthorized "
            "changes to system files — an early warning system for compromises."
        ),
        "content_de": (
            "AIDE (Advanced Intrusion Detection Environment) überwacht Datei-"
            "Integrität: `aideinit && cp /var/lib/aide/aide.db.new /var/lib/aide/"
            "aide.db`, dann regelmäßig `aide --check`. Erkennt unautorisierte "
            "Änderungen an System-Dateien — ein Frühwarnsystem für Kompromittierungen."
        ),
        "source_url": "https://darkwolfcave.de/server-monitoring-intrusion-detection-linux/",
        "source_label": "DarkWolfCave — Server Monitoring",
        "source_label_de": "DarkWolfCave — Server-Monitoring",
        "rarity": "rare",
        "category": "monitoring",
        "emoji": "\U0001F6A8",
        "sort_order": 16,
    },
    {
        "slug": "apparmor-profile",
        "title": "AppArmor Profiles for Services",
        "title_de": "AppArmor-Profile für Dienste erstellen",
        "content": (
            "Create AppArmor profiles for critical services: "
            "`aa-genprof /usr/sbin/sshd`. Profiles restrict file access and "
            "network permissions of a process to the absolute minimum "
            "(Mandatory Access Control). Even with a vulnerability, the "
            "attacker cannot escape the profile."
        ),
        "content_de": (
            "Erstelle AppArmor-Profile für kritische Dienste: "
            "`aa-genprof /usr/sbin/sshd`. Profile beschränken Dateizugriff und "
            "Netzwerk-Berechtigungen eines Prozesses auf das absolute Minimum "
            "(Mandatory Access Control). Selbst bei einer Schwachstelle kann der "
            "Angreifer nicht aus dem Profil ausbrechen."
        ),
        "source_url": "https://darkwolfcave.de/linux-server-haerten-angriffflaeche-minimieren/",
        "source_label": "DarkWolfCave — Hardening Linux Servers",
        "source_label_de": "DarkWolfCave — Linux-Server härten",
        "rarity": "rare",
        "category": "strategy",
        "emoji": "\U0001F6E1\uFE0F",
        "sort_order": 17,
    },
    {
        "slug": "netzwerksegmentierung",
        "title": "Network Segmentation",
        "title_de": "Netzwerksegmentierung implementieren",
        "content": (
            "Separate services into different network segments (VLANs/subnets). "
            "A compromised web server should have no direct access to the "
            "database. Docker networks, WireGuard VPNs, or Tailscale "
            "ACLs help with implementation — even without expensive hardware firewalls."
        ),
        "content_de": (
            "Trenne Dienste in verschiedene Netzwerksegmente (VLANs/Subnetze). "
            "Ein kompromittierter Webserver sollte keinen direkten Zugang zur "
            "Datenbank haben. Docker-Networks, WireGuard-VPNs oder Tailscale "
            "ACLs helfen bei der Umsetzung — auch ohne teure Hardware-Firewalls."
        ),
        "source_url": "https://darkwolfcave.de/netzwerk-sicherheit-firewall-zero-trust/",
        "source_label": "DarkWolfCave — Network Security",
        "source_label_de": "DarkWolfCave — Netzwerk-Sicherheit",
        "rarity": "rare",
        "category": "network",
        "emoji": "\U0001F310",
        "sort_order": 18,
    },
    {
        "slug": "dns-security",
        "title": "DNS Security: DoT/DoH + DNSSEC",
        "title_de": "DNS-Security: DoT und DNSSEC",
        "content": (
            "Configure DNS-over-TLS with systemd-resolved (`DNSOverTLS=yes` in "
            "`resolved.conf`) or Unbound. DNSSEC validates DNS responses "
            "cryptographically (`DNSSEC=yes`). Prevents DNS spoofing and "
            "man-in-the-middle attacks at the DNS level — an often overlooked attack vector."
        ),
        "content_de": (
            "Konfiguriere DNS-over-TLS mit systemd-resolved (`DNSOverTLS=yes` in "
            "`resolved.conf`) oder Unbound. DNSSEC validiert DNS-Antworten "
            "kryptographisch (`DNSSEC=yes`). Verhindert DNS-Spoofing und "
            "Man-in-the-Middle auf DNS-Ebene — ein oft übersehener Angriffsvektor."
        ),
        "source_url": "https://darkwolfcave.de/netzwerk-sicherheit-firewall-zero-trust/",
        "source_label": "DarkWolfCave — Network Security",
        "source_label_de": "DarkWolfCave — Netzwerk-Sicherheit",
        "rarity": "rare",
        "category": "network",
        "emoji": "\U0001F9EC",
        "sort_order": 19,
    },
    # --- Epic (4): Expert ---
    {
        "slug": "zero-trust-architektur",
        "title": "Zero-Trust Architecture",
        "title_de": "Zero-Trust-Architektur implementieren",
        "content": (
            "Trust no network, no device, no user by default. "
            "Every access is verified: identity + device status + context. "
            "Tools like Tailscale or Cloudflare Access implement zero-trust "
            "without VPN complexity. The perimeter model (inside=safe) is dead."
        ),
        "content_de": (
            "Vertraue keinem Netzwerk, keinem Gerät, keinem User per Default. "
            "Jeder Zugriff wird verifiziert: Identität + Gerätestatus + Kontext. "
            "Tools wie Tailscale oder Cloudflare Access implementieren Zero-Trust "
            "ohne VPN-Komplexität. Das Perimeter-Modell (innen=sicher) ist tot."
        ),
        "source_url": "https://darkwolfcave.de/netzwerk-sicherheit-firewall-zero-trust/",
        "source_label": "DarkWolfCave — Network Security",
        "source_label_de": "DarkWolfCave — Netzwerk-Sicherheit",
        "rarity": "epic",
        "category": "strategy",
        "emoji": "\U0001F3F0",
        "sort_order": 20,
    },
    {
        "slug": "container-hardening",
        "title": "Container Hardening",
        "title_de": "Container-Hardening: Minimal & Rootless",
        "content": (
            "Run Docker containers with read-only filesystem (`--read-only`), without root "
            "(`--user 1000:1000`), with limited capabilities (`--cap-drop ALL`). "
            "Use Trivy or `docker scout` for image vulnerability scans. "
            "Rootless Podman is the safer alternative to Docker with its root daemon."
        ),
        "content_de": (
            "Docker-Container mit Read-only Filesystem (`--read-only`), ohne Root "
            "(`--user 1000:1000`), mit begrenzten Capabilities (`--cap-drop ALL`). "
            "Nutze Trivy oder `docker scout` für Image-Schwachstellenscans. "
            "Rootless Podman ist die sicherere Alternative zu Docker mit Root-Daemon."
        ),
        "source_url": "https://darkwolfcave.de/linux-server-haerten-angriffflaeche-minimieren/",
        "source_label": "DarkWolfCave — Hardening Linux Servers",
        "source_label_de": "DarkWolfCave — Linux-Server härten",
        "rarity": "epic",
        "category": "container",
        "emoji": "\U0001F4E6",
        "sort_order": 21,
    },
    {
        "slug": "kernel-hardening",
        "title": "Kernel Hardening with sysctl",
        "title_de": "Kernel-Hardening mit sysctl",
        "content": (
            "Harden the kernel via `/etc/sysctl.d/99-hardening.conf`: "
            "`net.ipv4.conf.all.rp_filter=1` (spoofing protection), "
            "`kernel.dmesg_restrict=1` (kernel log protection), "
            "`kernel.unprivileged_bpf_disabled=1` (eBPF protection), "
            "`kernel.kptr_restrict=2` (pointer obfuscation). "
            "Activate with `sysctl --system`."
        ),
        "content_de": (
            "Härte den Kernel via `/etc/sysctl.d/99-hardening.conf`: "
            "`net.ipv4.conf.all.rp_filter=1` (Spoofing-Schutz), "
            "`kernel.dmesg_restrict=1` (Kernel-Log-Schutz), "
            "`kernel.unprivileged_bpf_disabled=1` (eBPF-Schutz), "
            "`kernel.kptr_restrict=2` (Pointer-Verschleierung). "
            "Aktivieren mit `sysctl --system`."
        ),
        "source_url": "https://darkwolfcave.de/linux-server-haerten-angriffflaeche-minimieren/",
        "source_label": "DarkWolfCave — Hardening Linux Servers",
        "source_label_de": "DarkWolfCave — Linux-Server härten",
        "rarity": "epic",
        "category": "strategy",
        "emoji": "\u2699\uFE0F",
        "sort_order": 22,
    },
    {
        "slug": "systemd-hardening",
        "title": "systemd Service Hardening",
        "title_de": "systemd-Service-Härtung",
        "content": (
            "Use systemd security options in service units: "
            "`ProtectSystem=strict`, `ProtectHome=yes`, `PrivateTmp=yes`, "
            "`NoNewPrivileges=yes`, `CapabilityBoundingSet=`. "
            "Check with `systemd-analyze security <unit>`. Goal: EXPOSED score "
            "below 5.0 for every critical service."
        ),
        "content_de": (
            "Nutze systemd-Sicherheitsoptionen in Service-Units: "
            "`ProtectSystem=strict`, `ProtectHome=yes`, `PrivateTmp=yes`, "
            "`NoNewPrivileges=yes`, `CapabilityBoundingSet=`. "
            "Prüfe mit `systemd-analyze security <unit>`. Ziel: EXPOSED-Score "
            "unter 5.0 für jeden kritischen Dienst."
        ),
        "source_url": "https://darkwolfcave.de/linux-server-haerten-angriffflaeche-minimieren/",
        "source_label": "DarkWolfCave — Hardening Linux Servers",
        "source_label_de": "DarkWolfCave — Linux-Server härten",
        "rarity": "epic",
        "category": "strategy",
        "emoji": "\U0001F9F1",
        "sort_order": 23,
    },
    # --- Legendary (2): Elite ---
    {
        "slug": "defense-in-depth",
        "title": "Defense-in-Depth Strategy",
        "title_de": "Defense-in-Depth: Sicherheit in Schichten",
        "content": (
            "Build security in layers: Firewall \u2192 IDS/IPS \u2192 "
            "OS hardening \u2192 AppArmor/SELinux \u2192 Monitoring \u2192 Backup "
            "\u2192 Incident Response. No single measure is perfect — but "
            "together they form a fortress. Each layer must function independently, "
            "so that failure of one layer doesn't compromise everything. "
            "Endlessh itself is one of these layers."
        ),
        "content_de": (
            "Sicherheit in Schichten aufbauen: Firewall \u2192 IDS/IPS \u2192 "
            "OS-Härtung \u2192 AppArmor/SELinux \u2192 Monitoring \u2192 Backup "
            "\u2192 Incident Response. Keine einzelne Maßnahme ist perfekt — aber "
            "zusammen bilden sie eine Festung. Jede Schicht muss unabhängig "
            "funktionieren, sodass ein Versagen einer Schicht nicht alles "
            "kompromittiert. Endlessh selbst ist eine dieser Schichten."
        ),
        "source_url": "https://darkwolfcave.de/backup-strategie-defense-in-depth-sicherheit/",
        "source_label": "DarkWolfCave — Backup & Security Strategy",
        "source_label_de": "DarkWolfCave — Backup & Sicherheitsstrategie",
        "rarity": "legendary",
        "category": "strategy",
        "emoji": "\U0001F3F0",
        "sort_order": 24,
    },
    {
        "slug": "incident-response-plan",
        "title": "Incident Response Plan",
        "title_de": "Incident Response Plan erstellen",
        "content": (
            "Create an incident response plan BEFORE something happens: "
            "1) Detection — monitoring, centralized logs, alerting. "
            "2) Containment — isolate network, rotate credentials. "
            "3) Eradication — fix root cause, remove malware. "
            "4) Recovery — backup restore, verification. "
            "5) Lessons Learned — document post-mortem. "
            "Test the plan with tabletop exercises at least once a year."
        ),
        "content_de": (
            "Erstelle einen Incident-Response-Plan BEVOR etwas passiert: "
            "1) Erkennung — Monitoring, zentrale Logs, Alerting. "
            "2) Eindämmung — Netzwerk isolieren, Credentials rotieren. "
            "3) Beseitigung — Rootcause fixen, Malware entfernen. "
            "4) Wiederherstellung — Backup restore, Verifizierung. "
            "5) Lessons Learned — Post-Mortem dokumentieren. "
            "Teste den Plan mit Tabletop-Übungen mindestens einmal jährlich."
        ),
        "source_url": "https://darkwolfcave.de/server-monitoring-intrusion-detection-linux/",
        "source_label": "DarkWolfCave — Server Monitoring",
        "source_label_de": "DarkWolfCave — Server-Monitoring",
        "rarity": "legendary",
        "category": "strategy",
        "emoji": "\U0001F4DC",
        "sort_order": 25,
    },
    # --- Wolf Digital Empire ---
    {
        "slug": "cronjob-monitoring",
        "title": "Monitor Your Cronjobs",
        "title_de": "Überwache deine Cronjobs",
        "content": (
            "Cronjobs fail silently — a missed backup or expired certificate "
            "goes unnoticed until it's too late. Use a cron monitoring service "
            "that alerts you when jobs don't run, take too long, or fail. "
            "CronWolf monitors your scheduled tasks and sends alerts via "
            "email or webhook. Currently in beta with 30% lifetime discount."
        ),
        "content_de": (
            "Cronjobs scheitern lautlos — ein verpasstes Backup oder ein "
            "abgelaufenes Zertifikat fällt erst auf, wenn es zu spät ist. "
            "Nutze einen Cron-Monitoring-Dienst, der dich warnt, wenn Jobs "
            "nicht laufen, zu lange brauchen oder fehlschlagen. "
            "CronWolf überwacht deine geplanten Tasks und sendet Alerts per "
            "E-Mail oder Webhook. Aktuell in der Beta mit 30% Lifetime-Rabatt."
        ),
        "source_url": "https://cronwolf.de",
        "source_label": "CronWolf — Cron Job Monitoring",
        "source_label_de": "CronWolf — Cronjob-Überwachung",
        "rarity": "legendary",
        "category": "monitoring",
        "emoji": "\U0001F43A",
        "sort_order": 26,
    },
    {
        "slug": "docker-security-basics",
        "title": "Docker Security: Don't Run as Root",
        "title_de": "Docker-Security: Nicht als Root laufen lassen",
        "content": (
            "Most Docker images run as root by default — a container escape "
            "then means full host access. Always specify a non-root USER in your "
            "Dockerfile, use `--cap-drop ALL`, and scan images with Trivy or "
            "`docker scout`. WolfCoder covers these patterns and more "
            "in depth for secure containerized deployments."
        ),
        "content_de": (
            "Die meisten Docker-Images laufen per Default als Root — ein "
            "Container-Escape bedeutet dann vollen Host-Zugriff. Definiere "
            "immer einen non-root USER im Dockerfile, nutze `--cap-drop ALL` "
            "und scanne Images mit Trivy oder `docker scout`. "
            "WolfCoder behandelt diese Patterns und mehr für sichere "
            "Container-Deployments im Detail."
        ),
        "source_url": "https://wolfcoder.de",
        "source_label": "WolfCoder — Secure Development",
        "source_label_de": "WolfCoder — Sichere Entwicklung",
        "rarity": "epic",
        "category": "container",
        "emoji": "\U0001F40B",
        "sort_order": 27,
    },
    # --- New Security Tips (8): Extracted from darkwolfcave.de articles ---
    {
        "slug": "log-management-zentralisiert",
        "title": "Centralized Log Management",
        "title_de": "Zentralisiertes Log-Management",
        "content": (
            "Ship logs to a central server with rsyslog or Promtail + Loki. "
            "Local logs can be deleted by attackers — centralized logs survive. "
            "Set up log rotation (`logrotate`) to prevent disk overflow. "
            "Correlating logs across multiple servers reveals attack patterns "
            "invisible on individual machines."
        ),
        "content_de": (
            "Leite Logs an einen zentralen Server weiter mit rsyslog oder Promtail + Loki. "
            "Lokale Logs können von Angreifern gelöscht werden — zentrale Logs überleben. "
            "Richte Log-Rotation ein (`logrotate`), um Festplattenüberlauf zu vermeiden. "
            "Die Korrelation von Logs über mehrere Server hinweg enthüllt Angriffsmuster, "
            "die auf einzelnen Maschinen unsichtbar bleiben."
        ),
        "source_url": "https://darkwolfcave.de/server-monitoring-intrusion-detection-linux/",
        "source_label": "DarkWolfCave — Server Monitoring",
        "source_label_de": "DarkWolfCave — Server-Monitoring",
        "rarity": "common",
        "category": "monitoring",
        "tip_type": "security",
        "emoji": "\U0001F4CA",
        "sort_order": 28,
    },
    {
        "slug": "passwort-manager-pflicht",
        "title": "Password Manager: A Must-Have",
        "title_de": "Passwort-Manager: Pflicht für jeden Admin",
        "content": (
            "Use a password manager like Vaultwarden (self-hosted Bitwarden), KeePassXC, "
            "or 1Password. Generate unique 20+ character passwords for every service. "
            "Reused passwords are the #1 reason credential stuffing attacks succeed. "
            "Self-hosting with Vaultwarden keeps your vault under your own control."
        ),
        "content_de": (
            "Nutze einen Passwort-Manager wie Vaultwarden (self-hosted Bitwarden), KeePassXC "
            "oder 1Password. Generiere einzigartige 20+ Zeichen Passwörter für jeden Dienst. "
            "Wiederverwendete Passwörter sind der #1 Grund, warum Credential-Stuffing-Angriffe "
            "funktionieren. Self-Hosting mit Vaultwarden hält deinen Tresor unter eigener Kontrolle."
        ),
        "source_url": "https://darkwolfcave.de/vaultwarden-docker-linux-passwort-manager/",
        "source_label": "DarkWolfCave — Vaultwarden Setup",
        "source_label_de": "DarkWolfCave — Vaultwarden einrichten",
        "rarity": "common",
        "category": "auth",
        "tip_type": "security",
        "emoji": "\U0001F513",
        "sort_order": 29,
    },
    {
        "slug": "vpn-wireguard-einrichten",
        "title": "VPN with WireGuard",
        "title_de": "VPN mit WireGuard einrichten",
        "content": (
            "WireGuard is faster and simpler than OpenVPN: only ~4,000 lines of code "
            "vs 100,000+. Set up a point-to-point VPN with `wg-quick` in minutes. "
            "Combined with a kill switch (`PostDown = iptables -D ...`), your traffic "
            "stays encrypted even if the tunnel drops. Perfect for admin access."
        ),
        "content_de": (
            "WireGuard ist schneller und einfacher als OpenVPN: nur ~4.000 Zeilen Code "
            "statt 100.000+. Richte ein Point-to-Point VPN mit `wg-quick` in Minuten ein. "
            "Kombiniert mit einem Kill-Switch (`PostDown = iptables -D ...`) bleibt dein "
            "Traffic verschlüsselt, selbst wenn der Tunnel abreißt. Ideal für Admin-Zugriff."
        ),
        "source_url": "https://darkwolfcave.de/netzwerk-sicherheit-firewall-zero-trust/",
        "source_label": "DarkWolfCave — Network Security",
        "source_label_de": "DarkWolfCave — Netzwerk-Sicherheit",
        "rarity": "common",
        "category": "network",
        "tip_type": "security",
        "emoji": "\U0001F50F",
        "sort_order": 30,
    },
    {
        "slug": "ssh-jump-host",
        "title": "SSH Jump Host (ProxyJump)",
        "title_de": "SSH Jump Host (ProxyJump)",
        "content": (
            "Never expose internal servers directly. Use a bastion/jump host: "
            "`ssh -J bastion internal-server` or configure `ProxyJump bastion` "
            "in `~/.ssh/config`. The jump host is the only machine with a public SSH port. "
            "All internal access goes through this single, hardened entry point."
        ),
        "content_de": (
            "Exponiere interne Server niemals direkt. Nutze einen Bastion/Jump Host: "
            "`ssh -J bastion interner-server` oder konfiguriere `ProxyJump bastion` "
            "in `~/.ssh/config`. Der Jump Host ist die einzige Maschine mit öffentlichem "
            "SSH-Port. Jeder interne Zugriff geht durch diesen einzelnen, gehärteten Einstiegspunkt."
        ),
        "source_url": "https://darkwolfcave.de/ssh-server-absichern-komplettanleitung/",
        "source_label": "DarkWolfCave — Hardening SSH Servers",
        "source_label_de": "DarkWolfCave — SSH-Server absichern",
        "rarity": "uncommon",
        "category": "ssh",
        "tip_type": "security",
        "emoji": "\U0001F3AF",
        "sort_order": 31,
    },
    {
        "slug": "port-knocking",
        "title": "Port Knocking",
        "title_de": "Port Knocking einrichten",
        "content": (
            "Hide SSH behind port knocking: the port stays closed until a specific "
            "sequence of connection attempts is detected. Tools like `knockd` implement "
            "this. Nmap scans see nothing — your SSH port is invisible to the entire "
            "internet. A simple but effective obscurity layer on top of real security."
        ),
        "content_de": (
            "Verstecke SSH hinter Port Knocking: Der Port bleibt geschlossen, bis eine "
            "bestimmte Sequenz von Verbindungsversuchen erkannt wird. Tools wie `knockd` "
            "implementieren das. Nmap-Scans sehen nichts — dein SSH-Port ist für das "
            "gesamte Internet unsichtbar. Eine einfache aber effektive Verschleierungsschicht."
        ),
        "source_url": "https://darkwolfcave.de/ssh-server-absichern-komplettanleitung/",
        "source_label": "DarkWolfCave — Hardening SSH Servers",
        "source_label_de": "DarkWolfCave — SSH-Server absichern",
        "rarity": "uncommon",
        "category": "ssh",
        "tip_type": "security",
        "emoji": "\U0001F6AA",
        "sort_order": 32,
    },
    {
        "slug": "monitoring-alerting",
        "title": "Monitoring with Alerting",
        "title_de": "Monitoring mit Alerting aufsetzen",
        "content": (
            "Monitoring without alerting is just pretty dashboards. Set up "
            "Prometheus + Grafana with alert rules, or use Uptime Kuma for "
            "simple endpoint monitoring. Alert on: disk >90%, CPU >95% for 5min, "
            "SSH login from unknown IP, service restart. A silent failure is "
            "the most dangerous failure."
        ),
        "content_de": (
            "Monitoring ohne Alerting sind nur hübsche Dashboards. Richte "
            "Prometheus + Grafana mit Alert-Regeln ein, oder Uptime Kuma für "
            "einfaches Endpoint-Monitoring. Alerts bei: Disk >90%, CPU >95% für 5min, "
            "SSH-Login von unbekannter IP, Service-Neustart. Ein lautloser "
            "Fehler ist der gefährlichste Fehler."
        ),
        "source_url": "https://darkwolfcave.de/server-monitoring-intrusion-detection-linux/",
        "source_label": "DarkWolfCave — Server Monitoring",
        "source_label_de": "DarkWolfCave — Server-Monitoring",
        "rarity": "rare",
        "category": "monitoring",
        "tip_type": "security",
        "emoji": "\U0001F514",
        "sort_order": 33,
    },
    {
        "slug": "reverse-proxy-waf",
        "title": "Reverse Proxy as WAF",
        "title_de": "Reverse Proxy als Web Application Firewall",
        "content": (
            "Put Traefik, Nginx, or Caddy as reverse proxy in front of every service. "
            "Add rate limiting, IP whitelisting, and TLS termination at the proxy level. "
            "Services behind the proxy only listen on internal Docker networks — "
            "no direct internet exposure. ModSecurity or Coraza add WAF capabilities."
        ),
        "content_de": (
            "Stelle Traefik, Nginx oder Caddy als Reverse Proxy vor jeden Dienst. "
            "Füge Rate-Limiting, IP-Whitelisting und TLS-Terminierung auf Proxy-Ebene hinzu. "
            "Dienste hinter dem Proxy lauschen nur auf internen Docker-Netzwerken — "
            "keine direkte Internet-Exposition. ModSecurity oder Coraza ergänzen WAF-Fähigkeiten."
        ),
        "source_url": "https://darkwolfcave.de/traefik-docker-linux-einrichten/",
        "source_label": "DarkWolfCave — Traefik Setup",
        "source_label_de": "DarkWolfCave — Traefik einrichten",
        "rarity": "rare",
        "category": "network",
        "tip_type": "security",
        "emoji": "\U0001F6E1\uFE0F",
        "sort_order": 34,
    },
    {
        "slug": "dns-sinkhole-pihole",
        "title": "DNS Sinkhole with Pi-hole",
        "title_de": "DNS-Sinkhole mit Pi-hole",
        "content": (
            "Pi-hole blocks ads, trackers, and malware domains at the DNS level — "
            "for your entire network. Combined with Unbound as recursive resolver, "
            "you get full DNS privacy without relying on third-party DNS servers. "
            "Block lists like Steven Black's host file cover 100,000+ known bad domains."
        ),
        "content_de": (
            "Pi-hole blockiert Werbung, Tracker und Malware-Domains auf DNS-Ebene — "
            "für dein gesamtes Netzwerk. Kombiniert mit Unbound als rekursiver Resolver "
            "bekommst du volle DNS-Privatsphäre ohne fremde DNS-Server. "
            "Blocklisten wie Steven Blacks Host-Datei decken 100.000+ bekannte böse Domains ab."
        ),
        "source_url": "https://darkwolfcave.de/pihole-unbound-fritzbox-ultimative-anleitung/",
        "source_label": "DarkWolfCave — Pi-hole & Unbound",
        "source_label_de": "DarkWolfCave — Pi-hole & Unbound",
        "rarity": "epic",
        "category": "network",
        "tip_type": "security",
        "emoji": "\U0001F30D",
        "sort_order": 35,
    },
    # --- Fun Facts (7): Verified IT trivia ---
    {
        "slug": "http-418-teapot",
        "title": "HTTP 418: I'm a Teapot",
        "title_de": "HTTP 418: Ich bin eine Teekanne",
        "content": (
            "HTTP status code 418 'I'm a teapot' was defined in RFC 2324 as an "
            "April Fools' joke in 1998. It describes the Hyper Text Coffee Pot Control "
            "Protocol (HTCPCP). Despite being a joke, it's implemented in many web "
            "frameworks and was even preserved when Google tried to remove it in 2017."
        ),
        "content_de": (
            "HTTP-Statuscode 418 'I'm a teapot' wurde in RFC 2324 als Aprilscherz "
            "1998 definiert. Er beschreibt das Hyper Text Coffee Pot Control Protocol "
            "(HTCPCP). Obwohl es ein Witz war, ist er in vielen Web-Frameworks "
            "implementiert und wurde sogar bewahrt, als Google ihn 2017 entfernen wollte."
        ),
        "source_url": "https://datatracker.ietf.org/doc/html/rfc2324",
        "source_label": "RFC 2324 — HTCPCP",
        "source_label_de": "RFC 2324 — HTCPCP",
        "rarity": "common",
        "category": "fun",
        "tip_type": "fun_fact",
        "emoji": "\u2615",
        "sort_order": 36,
    },
    {
        "slug": "erster-computerbug-1947",
        "title": "The First Computer Bug (1947)",
        "title_de": "Der erste Computerbug (1947)",
        "content": (
            "On September 9, 1947, engineers found a real moth stuck in a relay of "
            "the Harvard Mark II computer. Grace Hopper taped it into the logbook with "
            "the note 'First actual case of bug being found.' The term 'bug' predates "
            "this incident, but this is the most famous literal one."
        ),
        "content_de": (
            "Am 9. September 1947 fanden Ingenieure eine echte Motte in einem Relais des "
            "Harvard Mark II Computers. Grace Hopper klebte sie ins Logbuch mit der Notiz "
            "'First actual case of bug being found.' Der Begriff 'Bug' ist älter als "
            "dieser Vorfall, aber dies ist der berühmteste buchstäbliche."
        ),
        "source_url": "https://americanhistory.si.edu/collections/nmah_334663",
        "source_label": "Smithsonian National Museum",
        "source_label_de": "Smithsonian Nationalmuseum",
        "rarity": "common",
        "category": "fun",
        "tip_type": "fun_fact",
        "emoji": "\U0001F41B",
        "sort_order": 37,
    },
    {
        "slug": "fork-bomb-bash",
        "title": "The Fork Bomb: :(){ :|:&};:",
        "title_de": "Die Fork-Bomb: :(){ :|:&};:",
        "content": (
            "This 13-character Bash one-liner `:(){ :|:&};:` defines a function "
            "called `:` that calls itself twice in the background. It exponentially "
            "spawns processes until the system crashes. Protection: "
            "`ulimit -u 500` limits max processes per user. A beautiful example of "
            "how dangerous elegance can be."
        ),
        "content_de": (
            "Dieser 13-Zeichen Bash-Einzeiler `:(){ :|:&};:` definiert eine Funktion "
            "namens `:`, die sich selbst zweimal im Hintergrund aufruft. Sie spawnt "
            "exponentiell Prozesse bis das System abstürzt. Schutz: "
            "`ulimit -u 500` begrenzt die maximale Prozessanzahl pro User. "
            "Ein wunderschönes Beispiel, wie gefährlich Eleganz sein kann."
        ),
        "source_url": "https://en.wikipedia.org/wiki/Fork_bomb",
        "source_label": "Wikipedia — Fork bomb",
        "source_label_de": "Wikipedia — Fork-Bomb",
        "rarity": "uncommon",
        "category": "fun",
        "tip_type": "fun_fact",
        "emoji": "\U0001F4A3",
        "sort_order": 38,
    },
    {
        "slug": "ipv4-adressen-aufgebraucht",
        "title": "IPv4 Addresses Ran Out",
        "title_de": "IPv4-Adressen aufgebraucht",
        "content": (
            "On February 3, 2011, IANA allocated the last five /8 blocks of IPv4 "
            "addresses. That's 4,294,967,296 total addresses — about 0.5 per human "
            "alive. NAT and IPv6 are the workarounds, but in 2025, IPv4 addresses "
            "still trade for $30-50 each on the secondary market."
        ),
        "content_de": (
            "Am 3. Februar 2011 vergab die IANA die letzten fünf /8-Blöcke von "
            "IPv4-Adressen. Das sind insgesamt 4.294.967.296 Adressen — etwa 0,5 pro "
            "lebenden Menschen. NAT und IPv6 sind die Behelfslösungen, aber 2025 werden "
            "IPv4-Adressen immer noch für 30-50 USD auf dem Sekundärmarkt gehandelt."
        ),
        "source_url": "https://en.wikipedia.org/wiki/IPv4_address_exhaustion",
        "source_label": "Wikipedia — IPv4 address exhaustion",
        "source_label_de": "Wikipedia — IPv4-Adressknappheit",
        "rarity": "common",
        "category": "fun",
        "tip_type": "fun_fact",
        "emoji": "\U0001F4E6",
        "sort_order": 39,
    },
    {
        "slug": "linux-kernel-zeilen",
        "title": "Linux Kernel: 30+ Million Lines",
        "title_de": "Linux-Kernel: 30+ Millionen Zeilen",
        "content": (
            "The Linux kernel has over 30 million lines of code, maintained by "
            "thousands of developers worldwide. Linus Torvalds wrote the first version "
            "in 1991 with just 10,000 lines. It's the largest collaborative software "
            "project in human history, running on everything from smartwatches to "
            "supercomputers and 96.3% of the world's top 500 supercomputers."
        ),
        "content_de": (
            "Der Linux-Kernel hat über 30 Millionen Zeilen Code, gepflegt von "
            "Tausenden Entwicklern weltweit. Linus Torvalds schrieb die erste Version "
            "1991 mit nur 10.000 Zeilen. Es ist das größte kollaborative Software-"
            "Projekt der Menschheitsgeschichte und läuft auf Smartwatches bis "
            "Supercomputer — 96,3% der Top-500-Supercomputer nutzen Linux."
        ),
        "source_url": "https://www.linuxfoundation.org/",
        "source_label": "Linux Foundation",
        "source_label_de": "Linux Foundation",
        "rarity": "common",
        "category": "fun",
        "tip_type": "fun_fact",
        "emoji": "\U0001F427",
        "sort_order": 40,
    },
    {
        "slug": "rfc-1149-brieftauben",
        "title": "RFC 1149: IP over Avian Carriers",
        "title_de": "RFC 1149: IP über Brieftauben",
        "content": (
            "RFC 1149 (1990) describes how to transmit IP datagrams via carrier pigeons. "
            "In 2001, the Bergen Linux User Group actually implemented it: 9 packets sent, "
            "4 arrived — 55% packet loss and 3,000-6,000ms latency. They noted that "
            "'ichtiological, avian and other biological carriers' are suboptimal for TCP."
        ),
        "content_de": (
            "RFC 1149 (1990) beschreibt, wie man IP-Datagramme über Brieftauben überträgt. "
            "2001 hat die Bergen Linux User Group es tatsächlich implementiert: 9 Pakete "
            "gesendet, 4 angekommen — 55% Paketverlust und 3.000-6.000ms Latenz. "
            "Sie notierten, dass 'ichthyologische, aviale und andere biologische Carrier' "
            "für TCP suboptimal seien."
        ),
        "source_url": "https://datatracker.ietf.org/doc/html/rfc1149",
        "source_label": "RFC 1149 — IP Datagrams on Avian Carriers",
        "source_label_de": "RFC 1149 — IP über Brieftauben",
        "rarity": "uncommon",
        "category": "fun",
        "tip_type": "fun_fact",
        "emoji": "\U0001F54A\uFE0F",
        "sort_order": 41,
    },
    {
        "slug": "laengster-domainname",
        "title": "World's Longest Domain Name",
        "title_de": "Längster Domain-Name der Welt",
        "content": (
            "The Welsh village Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch "
            "has its own website at llanfairpwllgwyngyllgogerychwyrndrobwllllantysilio"
            "gogogoch.co.uk — 58 characters. But the longest valid domain label is 63 "
            "characters (RFC 1035). The full domain can be up to 253 characters total."
        ),
        "content_de": (
            "Das walisische Dorf Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch "
            "hat eine eigene Website mit 58 Zeichen Domainnamen. Aber das längste gültige "
            "Domain-Label ist 63 Zeichen (RFC 1035). Die gesamte Domain kann bis zu "
            "253 Zeichen lang sein. Viel Spaß beim Tippen."
        ),
        "source_url": "https://en.wikipedia.org/wiki/Llanfairpwllgwyngyll",
        "source_label": "Wikipedia — Llanfairpwllgwyngyll",
        "source_label_de": "Wikipedia — Llanfairpwllgwyngyll",
        "rarity": "common",
        "category": "fun",
        "tip_type": "fun_fact",
        "emoji": "\U0001F3F4\U000E0067\U000E0062\U000E0077\U000E006C\U000E0073\U000E007F",
        "sort_order": 42,
    },
    # --- Humor (11): Verified IT stories and quotes ---
    {
        "slug": "bobby-tables",
        "title": "Bobby Tables (xkcd 327)",
        "title_de": "Bobby Tables (xkcd 327)",
        "content": (
            "'Hi, this is your son's school. We're having some computer trouble.' "
            "'Oh, did he break something?' 'Did you really name your son "
            "Robert\\'); DROP TABLE Students;--?' The most famous SQL injection "
            "joke — and sadly, still relevant. Always use parameterized queries."
        ),
        "content_de": (
            "'Hallo, hier ist die Schule Ihres Sohnes. Wir haben Computerprobleme.' "
            "'Oh, hat er etwas kaputt gemacht?' 'Haben Sie Ihren Sohn wirklich "
            "Robert\\'); DROP TABLE Students;-- genannt?' Der berühmteste "
            "SQL-Injection-Witz — und leider immer noch aktuell. Immer parametrisierte Queries nutzen."
        ),
        "source_url": "https://xkcd.com/327/",
        "source_label": "xkcd 327 — Exploits of a Mom",
        "source_label_de": "xkcd 327 — Exploits of a Mom",
        "rarity": "common",
        "category": "fun",
        "tip_type": "humor",
        "emoji": "\U0001F4DD",
        "sort_order": 43,
    },
    {
        "slug": "works-on-my-machine",
        "title": "Works on My Machine",
        "title_de": "Funktioniert auf meiner Maschine",
        "content": (
            "'It works on my machine' — the most feared sentence in software development. "
            "Docker was essentially invented to solve this problem. The unofficial certificate "
            "'Works on My Machine' became a meme so popular that Docker practically made it "
            "their marketing slogan. Containers: because environments shouldn't be unique snowflakes."
        ),
        "content_de": (
            "'Es funktioniert auf meiner Maschine' — der gefürchtetste Satz in der "
            "Softwareentwicklung. Docker wurde quasi erfunden, um dieses Problem zu lösen. "
            "Das inoffizielle Zertifikat 'Works on My Machine' wurde ein Meme, das so "
            "populär war, dass Docker es praktisch als Marketing-Slogan übernahm. "
            "Container: weil Umgebungen keine Schneeflocken sein sollten."
        ),
        "source_url": "https://blog.codinghorror.com/the-works-on-my-machine-certification-program/",
        "source_label": "Coding Horror — Works on My Machine",
        "source_label_de": "Coding Horror — Works on My Machine",
        "rarity": "common",
        "category": "fun",
        "tip_type": "humor",
        "emoji": "\U0001F4BB",
        "sort_order": 44,
    },
    {
        "slug": "toy-story-2-rm-rf",
        "title": "Toy Story 2: Almost Deleted by rm -rf",
        "title_de": "Toy Story 2: Fast gelöscht durch rm -rf",
        "content": (
            "In 1998, someone accidentally ran `rm -rf *` on Pixar's Toy Story 2 "
            "production servers, deleting 90% of the movie. The backups? Also corrupted. "
            "The film was saved because a technical director had a full copy on her "
            "home machine — she'd been working from home after having a baby. "
            "The 3-2-1 backup rule exists for a reason."
        ),
        "content_de": (
            "1998 führte jemand versehentlich `rm -rf *` auf Pixars Toy Story 2 "
            "Produktionsservern aus und löschte 90% des Films. Die Backups? Ebenfalls "
            "defekt. Der Film wurde gerettet, weil eine technische Direktorin eine "
            "vollständige Kopie auf ihrem Heimrechner hatte — sie hatte nach der Geburt "
            "ihres Babys von zu Hause gearbeitet. Die 3-2-1-Backup-Regel existiert aus gutem Grund."
        ),
        "source_url": "https://thenextweb.com/news/how-pixars-toy-story-2-was-deleted-twice",
        "source_label": "TheNextWeb — Toy Story 2 Deletion",
        "source_label_de": "TheNextWeb — Toy Story 2 Löschung",
        "rarity": "uncommon",
        "category": "fun",
        "tip_type": "humor",
        "emoji": "\U0001F4A5",
        "sort_order": 45,
    },
    {
        "slug": "500-mile-email",
        "title": "The 500-Mile Email Problem",
        "title_de": "Das 500-Meilen-E-Mail-Problem",
        "content": (
            "In 2002, a sysadmin reported that emails couldn't be sent farther than "
            "500 miles. Sounds insane? The server's sendmail had a 0-second timeout "
            "due to a config bug. Light travels ~500 miles in 3ms — the TCP handshake "
            "time. Any server farther away timed out before responding. "
            "One of the greatest debugging stories ever told."
        ),
        "content_de": (
            "2002 meldete ein Sysadmin, dass E-Mails nicht weiter als 500 Meilen "
            "gesendet werden konnten. Klingt irre? Der sendmail-Server hatte einen "
            "0-Sekunden-Timeout wegen eines Config-Bugs. Licht reist ~500 Meilen in 3ms "
            "— die TCP-Handshake-Zeit. Jeder weiter entfernte Server bekam einen Timeout "
            "vor der Antwort. Eine der größten Debugging-Geschichten aller Zeiten."
        ),
        "source_url": "https://web.mit.edu/jemorris/humor/500-miles",
        "source_label": "Trey Harris — 500-Mile Email",
        "source_label_de": "Trey Harris — 500-Meilen-E-Mail",
        "rarity": "uncommon",
        "category": "fun",
        "tip_type": "humor",
        "emoji": "\U0001F4E7",
        "sort_order": 46,
    },
    {
        "slug": "zwei-harte-dinge-cs",
        "title": "Two Hard Things in CS",
        "title_de": "Zwei schwere Dinge in der Informatik",
        "content": (
            "'There are only 2 hard things in computer science: cache invalidation, "
            "naming things, and off-by-one errors.' — Attributed to Phil Karlton "
            "(with the off-by-one addition by Leon Bambrick). The joke is the error: "
            "there are 3 items in a list of 2. Every developer has lived this pain."
        ),
        "content_de": (
            "'Es gibt nur 2 schwere Dinge in der Informatik: Cache-Invalidierung, "
            "Benennung von Dingen und Off-by-One-Fehler.' — Phil Karlton zugeschrieben "
            "(mit dem Off-by-One-Zusatz von Leon Bambrick). Der Witz ist der Fehler: "
            "Es sind 3 Punkte in einer Liste von 2. Jeder Entwickler kennt diesen Schmerz."
        ),
        "source_url": "https://martinfowler.com/bliki/TwoHardThings.html",
        "source_label": "Martin Fowler — Two Hard Things",
        "source_label_de": "Martin Fowler — Two Hard Things",
        "rarity": "common",
        "category": "fun",
        "tip_type": "humor",
        "emoji": "\U0001F914",
        "sort_order": 47,
    },
    {
        "slug": "y2k-bug",
        "title": "Y2K Bug: $300 Billion for 2 Digits",
        "title_de": "Y2K-Bug: 300 Milliarden Dollar für 2 Ziffern",
        "content": (
            "The Y2K bug: developers saved memory by storing years as 2 digits (99 instead "
            "of 1999). When 2000 approached, the world spent an estimated $300 billion "
            "fixing code so systems wouldn't think it was 1900. The fix worked so well "
            "that people now think it was overblown. Classic 'prevention paradox.'"
        ),
        "content_de": (
            "Der Y2K-Bug: Entwickler sparten Speicher, indem sie Jahre als 2 Ziffern "
            "speicherten (99 statt 1999). Als 2000 nahte, gab die Welt geschätzt "
            "300 Milliarden Dollar aus, um Code zu fixen, damit Systeme nicht dachten, "
            "es sei 1900. Der Fix war so erfolgreich, dass Leute heute denken, "
            "es war übertrieben. Klassisches 'Präventionsparadox.'"
        ),
        "source_url": "https://en.wikipedia.org/wiki/Year_2000_problem",
        "source_label": "Wikipedia — Year 2000 problem",
        "source_label_de": "Wikipedia — Jahr-2000-Problem",
        "rarity": "common",
        "category": "fun",
        "tip_type": "humor",
        "emoji": "\U0001F4C5",
        "sort_order": 48,
    },
    {
        "slug": "not-a-bug-a-feature",
        "title": "It's Not a Bug, It's a Feature",
        "title_de": "Kein Bug, ein Feature",
        "content": (
            "'It's not a bug, it's a feature' — the classic developer excuse since "
            "the dawn of software. Originally used seriously by marketing teams to "
            "reframe unexpected behavior. Now the universal response when a QA engineer "
            "asks 'why does it do that?' The line between bug and feature is often "
            "just a matter of perspective (and documentation)."
        ),
        "content_de": (
            "'Das ist kein Bug, das ist ein Feature' — die klassische Entwickler-Ausrede "
            "seit Anbeginn der Software. Ursprünglich ernsthaft von Marketing-Teams "
            "verwendet, um unerwartetes Verhalten umzudeuten. Heute die universelle "
            "Antwort, wenn ein QA-Tester fragt 'warum macht es das?' Die Grenze zwischen "
            "Bug und Feature ist oft nur eine Frage der Perspektive (und der Dokumentation)."
        ),
        "source_url": "https://en.wikipedia.org/wiki/Undocumented_feature",
        "source_label": "Wikipedia — Undocumented feature",
        "source_label_de": "Wikipedia — Undokumentiertes Feature",
        "rarity": "common",
        "category": "fun",
        "tip_type": "humor",
        "emoji": "\U0001F60F",
        "sort_order": 49,
    },
    {
        "slug": "captcha-ironie",
        "title": "CAPTCHA Irony: Bots Beat Humans",
        "title_de": "CAPTCHA-Ironie: Bots schlagen Menschen",
        "content": (
            "CAPTCHAs were designed to tell humans and computers apart. Today's AI "
            "solves them faster and more accurately than humans. Google's reCAPTCHA v3 "
            "gave up on challenges entirely and just scores 'human-likeness' based on "
            "behavior. The bots won the CAPTCHA arms race — we now prove our humanity "
            "by how humanly we move our mouse."
        ),
        "content_de": (
            "CAPTCHAs sollten Menschen von Computern unterscheiden. Heutige KI löst "
            "sie schneller und genauer als Menschen. Googles reCAPTCHA v3 gab die "
            "Herausforderungen komplett auf und bewertet nur noch 'Menschenähnlichkeit' "
            "basierend auf Verhalten. Die Bots haben das CAPTCHA-Wettrüsten gewonnen — "
            "wir beweisen unsere Menschlichkeit jetzt dadurch, wie menschlich wir die Maus bewegen."
        ),
        "source_url": "https://en.wikipedia.org/wiki/CAPTCHA",
        "source_label": "Wikipedia — CAPTCHA",
        "source_label_de": "Wikipedia — CAPTCHA",
        "rarity": "uncommon",
        "category": "fun",
        "tip_type": "humor",
        "emoji": "\U0001F916",
        "sort_order": 50,
    },
    {
        "slug": "reddit-place",
        "title": "r/place: The Pixel War",
        "title_de": "r/place: Der Pixel-Krieg",
        "content": (
            "Reddit's r/place (2017, 2022, 2023): a shared 1000x1000 pixel canvas where "
            "each user could place one pixel every 5 minutes. Communities formed alliances, "
            "wrote bots, and waged wars over territory. The result: collaborative pixel art "
            "from millions of users. A beautiful experiment in emergent behavior, "
            "cooperation, and the internet's competitive spirit."
        ),
        "content_de": (
            "Reddits r/place (2017, 2022, 2023): eine gemeinsame 1000x1000 Pixel-Leinwand, "
            "auf der jeder User alle 5 Minuten einen Pixel setzen konnte. Communities "
            "bildeten Allianzen, schrieben Bots und führten Kriege um Territorium. "
            "Das Ergebnis: kollaborative Pixel-Kunst von Millionen Nutzern. "
            "Ein Experiment über emergentes Verhalten, Kooperation und Wettbewerb im Internet."
        ),
        "source_url": "https://en.wikipedia.org/wiki/R/place",
        "source_label": "Wikipedia — r/place",
        "source_label_de": "Wikipedia — r/place",
        "rarity": "uncommon",
        "category": "fun",
        "tip_type": "humor",
        "emoji": "\U0001F3A8",
        "sort_order": 51,
    },
    {
        "slug": "nasa-mars-orbiter",
        "title": "NASA Mars Orbiter: Metric vs Imperial",
        "title_de": "NASA Mars Orbiter: Metrisch vs Imperial",
        "content": (
            "In 1999, NASA lost the $125 million Mars Climate Orbiter because one team "
            "used metric units (Newton-seconds) while another used imperial (pound-seconds). "
            "The spacecraft entered Mars' atmosphere at the wrong altitude and burned up. "
            "The most expensive unit conversion error in history. Always agree on units."
        ),
        "content_de": (
            "1999 verlor die NASA den 125 Millionen Dollar teuren Mars Climate Orbiter, "
            "weil ein Team metrische Einheiten (Newton-Sekunden) und ein anderes imperiale "
            "(Pfund-Sekunden) verwendete. Die Sonde trat in der falschen Höhe in die "
            "Mars-Atmosphäre ein und verglühte. Der teuerste Einheitenumrechnungsfehler "
            "der Geschichte. Immer auf Einheiten einigen."
        ),
        "source_url": "https://solarsystem.nasa.gov/missions/mars-climate-orbiter/in-depth/",
        "source_label": "NASA — Mars Climate Orbiter",
        "source_label_de": "NASA — Mars Climate Orbiter",
        "rarity": "rare",
        "category": "fun",
        "tip_type": "humor",
        "emoji": "\U0001F680",
        "sort_order": 52,
    },
    {
        "slug": "git-blame",
        "title": "git blame: The Passive-Aggressive Tool",
        "title_de": "git blame: Das passiv-aggressivste Tool",
        "content": (
            "`git blame` shows who wrote each line of code. Despite its name, it's "
            "officially for 'tracking changes' — but let's be honest, everyone uses it "
            "to find out who wrote that terrible code. Plot twist: it was you, "
            "six months ago. git blame is the mirror nobody asked for."
        ),
        "content_de": (
            "`git blame` zeigt, wer jede Zeile Code geschrieben hat. Offiziell dient es "
            "der 'Änderungsverfolgung' — aber seien wir ehrlich, jeder nutzt es, "
            "um herauszufinden, wer diesen schrecklichen Code geschrieben hat. "
            "Plot-Twist: Du warst es selbst, vor sechs Monaten. git blame ist der "
            "Spiegel, den niemand wollte."
        ),
        "source_url": "https://git-scm.com/docs/git-blame",
        "source_label": "Git Documentation — git blame",
        "source_label_de": "Git-Dokumentation — git blame",
        "rarity": "common",
        "category": "fun",
        "tip_type": "humor",
        "emoji": "\U0001F52E",
        "sort_order": 53,
    },
    # --- Article Links (11): DarkWolfCave.de Flaschenpost ---
    {
        "slug": "article-ssh-absichern",
        "title": "SSH Hardening: From Password to Certificate",
        "title_de": "SSH absichern: Vom Passwort zum Zertifikat",
        "content": (
            "A comprehensive guide to hardening SSH: from disabling passwords to "
            "SSH certificates. Covers key management, 2FA, AllowUsers, algorithm "
            "hardening, and more. The complete SSH security checklist."
        ),
        "content_de": (
            "Eine vollständige Anleitung zum Härten von SSH: vom Deaktivieren von "
            "Passwörtern bis zu SSH-Zertifikaten. Behandelt Key-Management, 2FA, "
            "AllowUsers, Algorithmen-Härtung und mehr. Die komplette SSH-Sicherheits-Checkliste."
        ),
        "source_url": "https://darkwolfcave.de/ssh-server-absichern-komplettanleitung/",
        "source_label": "DarkWolfCave \u2192 Read article",
        "source_label_de": "DarkWolfCave \u2192 Artikel lesen",
        "rarity": "common",
        "category": "article",
        "tip_type": "article",
        "emoji": "\U0001F4F0",
        "sort_order": 54,
    },
    {
        "slug": "article-netzwerk-sicherheit",
        "title": "Firewall & Zero-Trust Network Security",
        "title_de": "Firewall & Zero-Trust: Netzwerk absichern",
        "content": (
            "ufw firewall, CrowdSec, network segmentation, DNS security, "
            "and zero-trust architecture. Practical Linux network security "
            "from the basics to advanced concepts."
        ),
        "content_de": (
            "ufw-Firewall, CrowdSec, Netzwerksegmentierung, DNS-Security "
            "und Zero-Trust-Architektur. Praktische Linux-Netzwerksicherheit "
            "von den Grundlagen bis zu fortgeschrittenen Konzepten."
        ),
        "source_url": "https://darkwolfcave.de/netzwerk-sicherheit-firewall-zero-trust/",
        "source_label": "DarkWolfCave \u2192 Read article",
        "source_label_de": "DarkWolfCave \u2192 Artikel lesen",
        "rarity": "common",
        "category": "article",
        "tip_type": "article",
        "emoji": "\U0001F4F0",
        "sort_order": 55,
    },
    {
        "slug": "article-monitoring-intrusion",
        "title": "Monitoring & Intrusion Detection",
        "title_de": "Monitoring & Intrusion Detection",
        "content": (
            "Monitor Linux servers: automatic updates, auditd, Lynis, AIDE, "
            "and an incident response plan. Detect attacks early and "
            "respond correctly."
        ),
        "content_de": (
            "Linux-Server überwachen: automatische Updates, auditd, Lynis, AIDE "
            "und ein Incident-Response-Plan. Angriffe früh erkennen und "
            "richtig reagieren."
        ),
        "source_url": "https://darkwolfcave.de/server-monitoring-intrusion-detection-linux/",
        "source_label": "DarkWolfCave \u2192 Read article",
        "source_label_de": "DarkWolfCave \u2192 Artikel lesen",
        "rarity": "common",
        "category": "article",
        "tip_type": "article",
        "emoji": "\U0001F4F0",
        "sort_order": 56,
    },
    {
        "slug": "article-linux-haerten",
        "title": "Linux Server Hardening: Kernel to Container",
        "title_de": "Linux-Server härten: Vom Kernel bis zum Container",
        "content": (
            "Harden Linux systems: disable services, AppArmor, kernel sysctl, "
            "systemd hardening, and container security. A practical guide "
            "to minimizing your attack surface."
        ),
        "content_de": (
            "Linux-Systeme härten: Dienste deaktivieren, AppArmor, Kernel-sysctl, "
            "systemd-Hardening und Container-Sicherheit. Eine praktische Anleitung "
            "zur Minimierung deiner Angriffsfläche."
        ),
        "source_url": "https://darkwolfcave.de/linux-server-haerten-angriffflaeche-minimieren/",
        "source_label": "DarkWolfCave \u2192 Read article",
        "source_label_de": "DarkWolfCave \u2192 Artikel lesen",
        "rarity": "common",
        "category": "article",
        "tip_type": "article",
        "emoji": "\U0001F4F0",
        "sort_order": 57,
    },
    {
        "slug": "article-backup-defense",
        "title": "Backup Strategy & Defense-in-Depth",
        "title_de": "Backup-Strategie & Defense-in-Depth",
        "content": (
            "Backup strategy with restic and borgbackup, the 3-2-1 rule, "
            "and defense-in-depth: security in layers for Linux servers. "
            "Because a backup that doesn't work isn't a backup."
        ),
        "content_de": (
            "Backup-Strategie mit restic und borgbackup, die 3-2-1-Regel "
            "und Defense-in-Depth: Sicherheit in Schichten für Linux-Server. "
            "Denn ein Backup das nicht funktioniert ist kein Backup."
        ),
        "source_url": "https://darkwolfcave.de/backup-strategie-defense-in-depth-sicherheit/",
        "source_label": "DarkWolfCave \u2192 Read article",
        "source_label_de": "DarkWolfCave \u2192 Artikel lesen",
        "rarity": "common",
        "category": "article",
        "tip_type": "article",
        "emoji": "\U0001F4F0",
        "sort_order": 58,
    },
    {
        "slug": "article-rpi5-nvme-ssd",
        "title": "Boot Raspberry Pi 5 from NVMe SSD",
        "title_de": "Raspberry Pi 5 von NVMe-SSD starten",
        "content": (
            "Ditch the microSD card and boot your Raspberry Pi 5 from a fast "
            "NVMe SSD. Hardware recommendations, dd-based OS transfer, boot "
            "order configuration, and PCIe Gen3 activation for maximum speed."
        ),
        "content_de": (
            "Schluss mit der microSD-Karte: Starte deinen Raspberry Pi 5 von "
            "einer schnellen NVMe-SSD. Hardware-Empfehlungen, OS-Transfer per dd, "
            "Boot-Reihenfolge konfigurieren und PCIe Gen3 aktivieren für maximale Geschwindigkeit."
        ),
        "source_url": "https://darkwolfcave.de/raspberry-pi-5-starten-von-nvme-ssd/",
        "source_label": "DarkWolfCave \u2192 Read article",
        "source_label_de": "DarkWolfCave \u2192 Artikel lesen",
        "rarity": "common",
        "category": "article",
        "tip_type": "article",
        "emoji": "\U0001F4F0",
        "sort_order": 59,
    },
    {
        "slug": "article-watchtower-docker",
        "title": "Watchtower: Auto-Update Docker Containers",
        "title_de": "Watchtower: Docker-Container automatisch aktualisieren",
        "content": (
            "Keep your Docker containers up-to-date automatically with Watchtower. "
            "Setup guide with Portainer integration, Discord notifications, "
            "and label-based control for selective container updates."
        ),
        "content_de": (
            "Halte deine Docker-Container automatisch aktuell mit Watchtower. "
            "Einrichtung mit Portainer-Integration, Discord-Benachrichtigungen "
            "und Label-basierte Steuerung für selektive Container-Updates."
        ),
        "source_url": "https://darkwolfcave.de/docker-container-aktualisieren-mit-watchtower/",
        "source_label": "DarkWolfCave \u2192 Read article",
        "source_label_de": "DarkWolfCave \u2192 Artikel lesen",
        "rarity": "common",
        "category": "article",
        "tip_type": "article",
        "emoji": "\U0001F4F0",
        "sort_order": 60,
    },
    {
        "slug": "article-paperless-docker",
        "title": "Paperless: Self-Hosted Document Management",
        "title_de": "Paperless mit Docker: Dokumentenverwaltung selbst hosten",
        "content": (
            "Go paperless with a self-hosted document management system in Docker. "
            "OCR, tagging, full-text search \u2014 manage your documents locally "
            "on a Raspberry Pi or any Linux server."
        ),
        "content_de": (
            "Papierlos mit einem selbstgehosteten Dokumentenmanagementsystem in Docker. "
            "OCR, Tagging, Volltextsuche \u2014 verwalte deine Dokumente lokal "
            "auf einem Raspberry Pi oder jedem Linux-Server."
        ),
        "source_url": "https://darkwolfcave.de/paperless-mit-docker/",
        "source_label": "DarkWolfCave \u2192 Read article",
        "source_label_de": "DarkWolfCave \u2192 Artikel lesen",
        "rarity": "common",
        "category": "article",
        "tip_type": "article",
        "emoji": "\U0001F4F0",
        "sort_order": 61,
    },
    {
        "slug": "article-rpi-passwort-vergessen",
        "title": "Raspberry Pi: Forgotten Password Recovery",
        "title_de": "Raspberry Pi: Passwort vergessen \u2014 So kommst du rein",
        "content": (
            "Locked out of your Raspberry Pi? Step-by-step recovery guide to "
            "regain access when you forgot the password. Works without "
            "reinstalling the OS or losing your data."
        ),
        "content_de": (
            "Aus dem Raspberry Pi ausgesperrt? Schritt-f\u00fcr-Schritt-Anleitung zum "
            "Wiederherstellen des Zugangs bei vergessenem Passwort. Funktioniert "
            "ohne Neuinstallation und ohne Datenverlust."
        ),
        "source_url": "https://darkwolfcave.de/raspberry-pi-passwort-vergessen/",
        "source_label": "DarkWolfCave \u2192 Read article",
        "source_label_de": "DarkWolfCave \u2192 Artikel lesen",
        "rarity": "common",
        "category": "article",
        "tip_type": "article",
        "emoji": "\U0001F4F0",
        "sort_order": 62,
    },
    {
        "slug": "article-rpi-grafana-monitoring",
        "title": "Free Monitoring with Grafana & InfluxDB",
        "title_de": "Kostenloses Monitoring mit Grafana & InfluxDB",
        "content": (
            "Build a free monitoring stack on your Raspberry Pi: Grafana for "
            "dashboards, InfluxDB for time-series data, all managed through "
            "Portainer and Docker. No license costs, full control."
        ),
        "content_de": (
            "Baue einen kostenlosen Monitoring-Stack auf deinem Raspberry Pi: "
            "Grafana f\u00fcr Dashboards, InfluxDB f\u00fcr Zeitreihendaten, alles verwaltet "
            "\u00fcber Portainer und Docker. Keine Lizenzkosten, volle Kontrolle."
        ),
        "source_url": "https://darkwolfcave.de/raspberry-pi-monitoring-grafana-installieren/",
        "source_label": "DarkWolfCave \u2192 Read article",
        "source_label_de": "DarkWolfCave \u2192 Artikel lesen",
        "rarity": "common",
        "category": "article",
        "tip_type": "article",
        "emoji": "\U0001F4F0",
        "sort_order": 63,
    },
    {
        "slug": "article-influxdb-erklaert",
        "title": "InfluxDB Explained: 1.x vs 2.x vs 3.x",
        "title_de": "InfluxDB erkl\u00e4rt: Alles \u00fcber 1.x, 2.x und 3.x",
        "content": (
            "The complete InfluxDB guide: version comparison 1.x vs 2.x vs 3.x, "
            "migration strategies, and practical recommendations for which "
            "version to use in your monitoring setup."
        ),
        "content_de": (
            "Der komplette InfluxDB-Guide: Versionsvergleich 1.x vs 2.x vs 3.x, "
            "Migrationsstrategien und praktische Empfehlungen, welche Version "
            "du f\u00fcr dein Monitoring-Setup nutzen solltest."
        ),
        "source_url": "https://darkwolfcave.de/influxdb-erklart-alles-uber-das-leistungsstarke-datenbank-tool/",
        "source_label": "DarkWolfCave \u2192 Read article",
        "source_label_de": "DarkWolfCave \u2192 Artikel lesen",
        "rarity": "uncommon",
        "category": "article",
        "tip_type": "article",
        "emoji": "\U0001F4F0",
        "sort_order": 64,
    },
    {
        "slug": "article-influxdb-backup",
        "title": "InfluxDB Backup Made Simple",
        "title_de": "InfluxDB-Backup ganz einfach sichern",
        "content": (
            "Protect your time-series data: backup procedures for InfluxDB 1.8 "
            "and 2.x on Raspberry Pi. Includes automation scripts so you "
            "never lose your monitoring history."
        ),
        "content_de": (
            "Sch\u00fctze deine Zeitreihendaten: Backup-Verfahren f\u00fcr InfluxDB 1.8 "
            "und 2.x auf dem Raspberry Pi. Inklusive Automatisierungs-Skripte, "
            "damit du nie deine Monitoring-Historie verlierst."
        ),
        "source_url": "https://darkwolfcave.de/raspberry-pi-influxdb-backup-ganz-einfach-sichern/",
        "source_label": "DarkWolfCave \u2192 Read article",
        "source_label_de": "DarkWolfCave \u2192 Artikel lesen",
        "rarity": "uncommon",
        "category": "article",
        "tip_type": "article",
        "emoji": "\U0001F4F0",
        "sort_order": 65,
    },
    {
        "slug": "article-rpi-nas-mount",
        "title": "Auto-Mount NAS Shares on Raspberry Pi",
        "title_de": "NAS-Freigaben automatisch auf dem Raspberry Pi einbinden",
        "content": (
            "Mount NAS shares reliably on your Raspberry Pi at boot. Solves the "
            "common problem where standard automount fails because the network "
            "is not ready yet during startup."
        ),
        "content_de": (
            "NAS-Freigaben zuverl\u00e4ssig beim Booten auf dem Raspberry Pi einbinden. "
            "L\u00f6st das h\u00e4ufige Problem, dass der Standard-Automount fehlschl\u00e4gt, "
            "weil das Netzwerk beim Start noch nicht bereit ist."
        ),
        "source_url": "https://darkwolfcave.de/raspberry-pi-nas-freigaben-automatisch-einbinden/",
        "source_label": "DarkWolfCave \u2192 Read article",
        "source_label_de": "DarkWolfCave \u2192 Artikel lesen",
        "rarity": "uncommon",
        "category": "article",
        "tip_type": "article",
        "emoji": "\U0001F4F0",
        "sort_order": 66,
    },
    {
        "slug": "article-influxdb2-telegraf-grafana",
        "title": "InfluxDB 2.x + Telegraf + Grafana Stack",
        "title_de": "InfluxDB 2.x + Telegraf + Grafana: Monitoring-Stack",
        "content": (
            "The complete monitoring trio: collect metrics with Telegraf, store "
            "in InfluxDB 2.x with FLUX queries, and visualize everything in "
            "Grafana dashboards. Real-time system monitoring on Raspberry Pi."
        ),
        "content_de": (
            "Das komplette Monitoring-Trio: Metriken sammeln mit Telegraf, speichern "
            "in InfluxDB 2.x mit FLUX-Queries und alles visualisieren in "
            "Grafana-Dashboards. Echtzeit-System-Monitoring auf dem Raspberry Pi."
        ),
        "source_url": "https://darkwolfcave.de/raspberry-pi-influxdb-2-telegraf-grafana-anzeigen/",
        "source_label": "DarkWolfCave \u2192 Read article",
        "source_label_de": "DarkWolfCave \u2192 Artikel lesen",
        "rarity": "uncommon",
        "category": "article",
        "tip_type": "article",
        "emoji": "\U0001F4F0",
        "sort_order": 67,
    },
    {
        "slug": "article-rpi-ssd-boot",
        "title": "Boot Raspberry Pi from SSD",
        "title_de": "Raspberry Pi von SSD starten",
        "content": (
            "Tired of slow and unreliable SD cards? Boot your Raspberry Pi "
            "directly from an SSD for better performance and reliability. "
            "Step-by-step guide for all compatible Pi models."
        ),
        "content_de": (
            "Genug von langsamen und unzuverl\u00e4ssigen SD-Karten? Starte deinen "
            "Raspberry Pi direkt von einer SSD f\u00fcr bessere Leistung und Zuverl\u00e4ssigkeit. "
            "Schritt-f\u00fcr-Schritt-Anleitung f\u00fcr alle kompatiblen Pi-Modelle."
        ),
        "source_url": "https://darkwolfcave.de/raspberry-von-ssd-starten/",
        "source_label": "DarkWolfCave \u2192 Read article",
        "source_label_de": "DarkWolfCave \u2192 Artikel lesen",
        "rarity": "uncommon",
        "category": "article",
        "tip_type": "article",
        "emoji": "\U0001F4F0",
        "sort_order": 68,
    },
    {
        "slug": "article-rpi-docker-install",
        "title": "Install Docker on Raspberry Pi",
        "title_de": "Docker auf dem Raspberry Pi installieren",
        "content": (
            "Install Docker on your Raspberry Pi without the usual headaches. "
            "From initial setup to your first running container, including "
            "Portainer for easy web-based management."
        ),
        "content_de": (
            "Docker auf dem Raspberry Pi installieren ohne die \u00fcblichen Probleme. "
            "Von der Ersteinrichtung bis zum ersten laufenden Container, inklusive "
            "Portainer f\u00fcr komfortable Web-basierte Verwaltung."
        ),
        "source_url": "https://darkwolfcave.de/raspberry-pi-docker-ohne-probleme-installieren/",
        "source_label": "DarkWolfCave \u2192 Read article",
        "source_label_de": "DarkWolfCave \u2192 Artikel lesen",
        "rarity": "uncommon",
        "category": "article",
        "tip_type": "article",
        "emoji": "\U0001F4F0",
        "sort_order": 69,
    },
    # --- Project Promos (4): Wolf Digital Empire ---
    {
        "slug": "promo-cronwolf",
        "title": "CronWolf: Never Miss a Failed Cronjob",
        "title_de": "CronWolf: Nie wieder stille Cronjob-Fehler",
        "content": (
            "Cronjobs fail silently. A missed backup, an expired certificate, "
            "a broken sync — you only notice when it's too late. CronWolf "
            "monitors your scheduled tasks and alerts you via email or webhook "
            "when jobs don't run, take too long, or fail. "
            "Currently in beta with a lifetime discount."
        ),
        "content_de": (
            "Cronjobs scheitern lautlos. Ein verpasstes Backup, ein abgelaufenes "
            "Zertifikat, eine defekte Synchronisation — man merkt es erst, wenn es "
            "zu spät ist. CronWolf überwacht deine geplanten Tasks und warnt per "
            "E-Mail oder Webhook, wenn Jobs nicht laufen, zu lange brauchen oder "
            "fehlschlagen. Aktuell in der Beta mit Lifetime-Rabatt."
        ),
        "source_url": "https://cronwolf.de",
        "source_label": "CronWolf \u2192 Visit",
        "source_label_de": "CronWolf \u2192 Besuchen",
        "rarity": "uncommon",
        "category": "promo",
        "tip_type": "promo",
        "emoji": "\U0001F43A",
        "sort_order": 65,
    },
    {
        "slug": "promo-wolfcoder",
        "title": "WolfCoder: Dev Tutorials & Security",
        "title_de": "WolfCoder: Dev-Tutorials & Security",
        "content": (
            "Practical development tutorials focused on security, Docker, "
            "Linux, and modern web development. From container hardening "
            "to CI/CD pipelines — code that runs safe in production. "
            "Written by a developer, for developers."
        ),
        "content_de": (
            "Praktische Entwickler-Tutorials mit Fokus auf Security, Docker, "
            "Linux und moderne Webentwicklung. Von Container-Hardening "
            "bis CI/CD-Pipelines — Code, der sicher in Produktion läuft. "
            "Von einem Entwickler, für Entwickler."
        ),
        "source_url": "https://wolfcoder.de",
        "source_label": "WolfCoder \u2192 Visit",
        "source_label_de": "WolfCoder \u2192 Besuchen",
        "rarity": "uncommon",
        "category": "promo",
        "tip_type": "promo",
        "emoji": "\U0001F4BB",
        "sort_order": 66,
    },
    {
        "slug": "promo-favoritenportal",
        "title": "Favoritenportal: Your Bookmark Hub",
        "title_de": "Favoritenportal: Dein Lesezeichen-Hub",
        "content": (
            "Tired of losing bookmarks across browsers and devices? "
            "Favoritenportal is a clean, fast bookmark portal you can "
            "set as your browser start page. Organize your favorite links "
            "in categories, access them from anywhere."
        ),
        "content_de": (
            "Lesezeichen über Browser und Geräte hinweg verloren? "
            "Favoritenportal ist ein schnelles, aufgeräumtes Lesezeichen-Portal "
            "als Browser-Startseite. Organisiere deine Lieblingslinks "
            "in Kategorien, zugreifbar von überall."
        ),
        "source_url": "https://favoritenportal.de",
        "source_label": "Favoritenportal \u2192 Visit",
        "source_label_de": "Favoritenportal \u2192 Besuchen",
        "rarity": "rare",
        "category": "promo",
        "tip_type": "promo",
        "emoji": "\U0001F517",
        "sort_order": 67,
    },
    {
        "slug": "promo-meinwolfshund",
        "title": "MeinWolfshund: Marxdorfer Wolfdog Community",
        "title_de": "MeinWolfshund: Marxdorfer Wolfshund Community",
        "content": (
            "The Marxdorfer Wolfshund looks like a wolf but lives as a loyal "
            "family companion. MeinWolfshund is the community for wolf dog "
            "enthusiasts: breed information, health tips, breeder directory, "
            "and a forum to connect with other wolf dog owners."
        ),
        "content_de": (
            "Der Marxdorfer Wolfshund sieht aus wie ein Wolf, lebt aber als treuer "
            "Familienbegleiter. MeinWolfshund ist die Community für Wolfshund-"
            "Liebhaber: Rasseinfos, Gesundheitstipps, Züchterverzeichnis "
            "und ein Forum zum Austausch mit anderen Wolfshund-Besitzern."
        ),
        "source_url": "https://meinwolfshund.de",
        "source_label": "MeinWolfshund \u2192 Visit",
        "source_label_de": "MeinWolfshund \u2192 Besuchen",
        "rarity": "rare",
        "category": "promo",
        "tip_type": "promo",
        "emoji": "\U0001F43A",
        "sort_order": 68,
    },
]

CHALLENGE_TEMPLATES = [
    # Easy
    {
        "slug": "catch-bots-easy",
        "name": "Daily Catch",
        "name_de": "Tagesfang",
        "description_template": "Catch {threshold} bots today.",
        "description_template_de": "Fange heute {threshold} Bots.",
        "metric": "daily_catches",
        "difficulty": "easy",
        "threshold_min": 20,
        "threshold_max": 50,
        "reward_points": 25,
        "emoji": "\U0001F3A3",
    },
    {
        "slug": "trap-time-easy",
        "name": "Time Waster",
        "name_de": "Zeitverschwender",
        "description_template": "Waste {threshold} seconds of bot time today.",
        "description_template_de": "Verschwende heute {threshold} Sekunden Bot-Zeit.",
        "metric": "daily_trapped_seconds",
        "difficulty": "easy",
        "threshold_min": 3600,
        "threshold_max": 10800,
        "reward_points": 25,
        "emoji": "\u23F3",
    },
    {
        "slug": "country-variety-easy",
        "name": "World Fishing",
        "name_de": "Weltangeln",
        "description_template": "Catch bots from {threshold} different countries today.",
        "description_template_de": "Fange heute Bots aus {threshold} verschiedenen Ländern.",
        "metric": "daily_unique_countries",
        "difficulty": "easy",
        "threshold_min": 3,
        "threshold_max": 8,
        "reward_points": 30,
        "emoji": "\U0001F30D",
    },
    {
        "slug": "collect-treasure-easy",
        "name": "Beach Patrol",
        "name_de": "Strandpatrouille",
        "description_template": "Collect {threshold} treasures today.",
        "description_template_de": "Sammle heute {threshold} Schätze.",
        "metric": "daily_treasures",
        "difficulty": "easy",
        "threshold_min": 1,
        "threshold_max": 3,
        "reward_points": 30,
        "emoji": "\U0001F48E",
    },
    # Medium
    {
        "slug": "catch-bots-medium",
        "name": "Fishing Spree",
        "name_de": "Fangrekord",
        "description_template": "Catch {threshold} bots today.",
        "description_template_de": "Fange heute {threshold} Bots.",
        "metric": "daily_catches",
        "difficulty": "medium",
        "threshold_min": 60,
        "threshold_max": 120,
        "reward_points": 50,
        "emoji": "\U0001F3A3",
    },
    {
        "slug": "species-variety",
        "name": "Diverse Nets",
        "name_de": "Vielfalt im Netz",
        "description_template": "Catch {threshold} different species today.",
        "description_template_de": "Fange heute {threshold} verschiedene Fischarten.",
        "metric": "daily_unique_species",
        "difficulty": "medium",
        "threshold_min": 3,
        "threshold_max": 6,
        "reward_points": 60,
        "emoji": "\U0001F420",
    },
    {
        "slug": "rare-catches",
        "name": "Big Game Fisher",
        "name_de": "Großwildfischer",
        "description_template": "Catch {threshold} rare or better fish today.",
        "description_template_de": "Fange heute {threshold} seltene (oder bessere) Fische.",
        "metric": "daily_rare_catches",
        "difficulty": "medium",
        "threshold_min": 1,
        "threshold_max": 3,
        "reward_points": 75,
        "emoji": "\u2B50",
    },
    # Hard
    {
        "slug": "catch-bots-hard",
        "name": "Bot Blitz",
        "name_de": "Bot-Blitz",
        "description_template": "Catch {threshold} bots today.",
        "description_template_de": "Fange heute {threshold} Bots.",
        "metric": "daily_catches",
        "difficulty": "hard",
        "threshold_min": 150,
        "threshold_max": 300,
        "reward_points": 100,
        "emoji": "\u26A1",
    },
    {
        "slug": "trap-time-hard",
        "name": "Endless Trap",
        "name_de": "Endlose Falle",
        "description_template": "Waste {threshold} seconds of bot time today.",
        "description_template_de": "Verschwende heute {threshold} Sekunden Bot-Zeit.",
        "metric": "daily_trapped_seconds",
        "difficulty": "hard",
        "threshold_min": 36000,
        "threshold_max": 86400,
        "reward_points": 100,
        "emoji": "\U0001F570",
    },
    {
        "slug": "collect-treasure-hard",
        "name": "Treasure Dive",
        "name_de": "Schatztauchen",
        "description_template": "Collect {threshold} treasures today.",
        "description_template_de": "Sammle heute {threshold} Schätze.",
        "metric": "daily_treasures",
        "difficulty": "hard",
        "threshold_min": 5,
        "threshold_max": 10,
        "reward_points": 100,
        "emoji": "\U0001F531",
    },
]

ACHIEVEMENT_CATEGORIES = [
    {
        "slug": "first-steps",
        "name": "First Steps",
        "name_de": "Erste Schritte",
        "icon": "footprints",
        "sort_order": 1,
    },
    {
        "slug": "time-waster",
        "name": "Time Waster",
        "name_de": "Zeitverschwender",
        "icon": "clock",
        "sort_order": 2,
    },
    {
        "slug": "patience",
        "name": "Patience is a Virtue",
        "name_de": "Geduld ist eine Tugend",
        "icon": "hourglass",
        "sort_order": 3,
    },
    {
        "slug": "traveler",
        "name": "World Traveler",
        "name_de": "Weltreisender",
        "icon": "globe",
        "sort_order": 4,
    },
    {
        "slug": "collector",
        "name": "Collector",
        "name_de": "Sammler",
        "icon": "collection",
        "sort_order": 5,
    },
    {
        "slug": "server-master",
        "name": "Server Master",
        "name_de": "Server-Meister",
        "icon": "server",
        "sort_order": 6,
    },
    {
        "slug": "data-hoarder",
        "name": "Data Hoarder",
        "name_de": "Datenhamster",
        "icon": "database",
        "sort_order": 7,
    },
    {
        "slug": "treasure-hunter",
        "name": "Treasure Hunter",
        "name_de": "Schatzjäger",
        "icon": "gem",
        "sort_order": 8,
    },
    {
        "slug": "cyber-investigator",
        "name": "Cyber Investigator",
        "name_de": "Cyber-Ermittler",
        "icon": "search",
        "sort_order": 9,
    },
]

ACHIEVEMENTS = [
    # First Steps - total catches
    {"slug": "first-catch", "category": "first-steps", "name": "First Catch", "name_de": "Erster Fang",
     "description": "Catch your first bot.", "description_de": "Fange deinen ersten Bot.",
     "metric": "total_catches", "threshold": 1, "rarity": "bronze", "points": 10, "sort_order": 1},
    {"slug": "ten-catches", "category": "first-steps", "name": "Getting Started", "name_de": "Es geht los",
     "description": "Catch 10 bots.", "description_de": "Fange 10 Bots.",
     "metric": "total_catches", "threshold": 10, "rarity": "bronze", "points": 25, "sort_order": 2},
    {"slug": "hundred-catches", "category": "first-steps", "name": "Century", "name_de": "Jahrhundert",
     "description": "Catch 100 bots.", "description_de": "Fange 100 Bots.",
     "metric": "total_catches", "threshold": 100, "rarity": "silver", "points": 50, "sort_order": 3},
    {"slug": "thousand-catches", "category": "first-steps", "name": "Kilocatch", "name_de": "Kilofang",
     "description": "Catch 1,000 bots.", "description_de": "Fange 1.000 Bots.",
     "metric": "total_catches", "threshold": 1000, "rarity": "gold", "points": 100, "sort_order": 4},
    {"slug": "ten-thousand-catches", "category": "first-steps", "name": "Bot Slayer", "name_de": "Bot-Jäger",
     "description": "Catch 10,000 bots.", "description_de": "Fange 10.000 Bots.",
     "metric": "total_catches", "threshold": 10000, "rarity": "platinum", "points": 250, "sort_order": 5},
    {"slug": "hundred-thousand-catches", "category": "first-steps", "name": "Bot Apocalypse", "name_de": "Bot-Apokalypse",
     "description": "Catch 100,000 bots.", "description_de": "Fange 100.000 Bots.",
     "metric": "total_catches", "threshold": 100000, "rarity": "diamond", "points": 500, "sort_order": 6},
    # Time Waster - total trapped seconds (cumulative across all bots)
    # ~500K trapped_seconds/real day → thresholds scaled for long-term play
    {"slug": "one-hour-wasted", "category": "time-waster", "name": "Coffee Break", "name_de": "Kaffeepause",
     "description": "Waste 1 hour of bot time.", "description_de": "Verschwende 1 Stunde Bot-Zeit.",
     "metric": "total_trapped_seconds", "threshold": 3600, "rarity": "bronze", "points": 25, "sort_order": 1},
    {"slug": "one-day-wasted", "category": "time-waster", "name": "Day Thief", "name_de": "Tagedieb",
     "description": "Waste 1 day of bot time.", "description_de": "Verschwende 1 Tag Bot-Zeit.",
     "metric": "total_trapped_seconds", "threshold": 86400, "rarity": "silver", "points": 50, "sort_order": 2},
    {"slug": "thirty-days-wasted", "category": "time-waster", "name": "Month Muncher", "name_de": "Monats-Fresser",
     "description": "Waste 30 days of bot time.", "description_de": "Verschwende 30 Tage Bot-Zeit.",
     "metric": "total_trapped_seconds", "threshold": 2592000, "rarity": "gold", "points": 100, "sort_order": 3},
    {"slug": "half-year-wasted", "category": "time-waster", "name": "Half-Year Horror", "name_de": "Halbjahres-Horror",
     "description": "Waste 180 days of bot time.", "description_de": "Verschwende 180 Tage Bot-Zeit.",
     "metric": "total_trapped_seconds", "threshold": 15552000, "rarity": "platinum", "points": 250, "sort_order": 4},
    {"slug": "three-years-wasted", "category": "time-waster", "name": "Time Lord", "name_de": "Zeitherrscher",
     "description": "Waste 3 years of bot time.", "description_de": "Verschwende 3 Jahre Bot-Zeit.",
     "metric": "total_trapped_seconds", "threshold": 94608000, "rarity": "diamond", "points": 500, "sort_order": 5},
    # Patience - single longest trap
    {"slug": "one-minute-trap", "category": "patience", "name": "Patience Test", "name_de": "Geduldsprobe",
     "description": "Trap a single bot for 1 minute.", "description_de": "Halte einen einzelnen Bot 1 Minute fest.",
     "metric": "single_trap_seconds", "threshold": 60, "rarity": "bronze", "points": 15, "sort_order": 1},
    {"slug": "one-hour-trap", "category": "patience", "name": "Iron Will", "name_de": "Eiserner Wille",
     "description": "Trap a single bot for 1 hour.", "description_de": "Halte einen einzelnen Bot 1 Stunde fest.",
     "metric": "single_trap_seconds", "threshold": 3600, "rarity": "silver", "points": 50, "sort_order": 2},
    {"slug": "one-day-trap", "category": "patience", "name": "Day Keeper", "name_de": "Tageswächter",
     "description": "Trap a single bot for 24 hours.", "description_de": "Halte einen einzelnen Bot 24 Stunden fest.",
     "metric": "single_trap_seconds", "threshold": 86400, "rarity": "gold", "points": 150, "sort_order": 3},
    {"slug": "one-week-trap", "category": "patience", "name": "Eternal Guardian", "name_de": "Ewiger Wächter",
     "description": "Trap a single bot for 7 days.", "description_de": "Halte einen einzelnen Bot 7 Tage fest.",
     "metric": "single_trap_seconds", "threshold": 604800, "rarity": "diamond", "points": 500, "sort_order": 4},
    # World Traveler - unique countries
    {"slug": "first-country", "category": "traveler", "name": "Local Fisher", "name_de": "Lokaler Angler",
     "description": "Catch bots from 1 country.", "description_de": "Fange Bots aus 1 Land.",
     "metric": "unique_countries", "threshold": 1, "rarity": "bronze", "points": 10, "sort_order": 1},
    {"slug": "ten-countries", "category": "traveler", "name": "Continental", "name_de": "Kontinental",
     "description": "Catch bots from 10 countries.", "description_de": "Fange Bots aus 10 Ländern.",
     "metric": "unique_countries", "threshold": 10, "rarity": "silver", "points": 50, "sort_order": 2},
    {"slug": "thirty-countries", "category": "traveler", "name": "Globetrotter", "name_de": "Globetrotter",
     "description": "Catch bots from 30 countries.", "description_de": "Fange Bots aus 30 Ländern.",
     "metric": "unique_countries", "threshold": 30, "rarity": "gold", "points": 100, "sort_order": 3},
    {"slug": "fifty-countries", "category": "traveler", "name": "World Fisher", "name_de": "Weltangler",
     "description": "Catch bots from 50 countries.", "description_de": "Fange Bots aus 50 Ländern.",
     "metric": "unique_countries", "threshold": 50, "rarity": "platinum", "points": 200, "sort_order": 4},
    {"slug": "hundred-countries", "category": "traveler", "name": "Pangaea Fisher", "name_de": "Pangäa-Angler",
     "description": "Catch bots from 100 countries.", "description_de": "Fange Bots aus 100 Ländern.",
     "metric": "unique_countries", "threshold": 100, "rarity": "diamond", "points": 500, "sort_order": 5},
    # Collector - unique species caught
    {"slug": "three-species", "category": "collector", "name": "Beginner's Net", "name_de": "Anfänger-Netz",
     "description": "Catch 3 different fish species.", "description_de": "Fange 3 verschiedene Fischarten.",
     "metric": "species_caught", "threshold": 3, "rarity": "bronze", "points": 25, "sort_order": 1},
    {"slug": "six-species", "category": "collector", "name": "Diverse Catch", "name_de": "Vielfältiger Fang",
     "description": "Catch 6 different fish species.", "description_de": "Fange 6 verschiedene Fischarten.",
     "metric": "species_caught", "threshold": 6, "rarity": "silver", "points": 75, "sort_order": 2},
    {"slug": "nine-species", "category": "collector", "name": "Master Angler", "name_de": "Meisterangler",
     "description": "Catch 9 different fish species.", "description_de": "Fange 9 verschiedene Fischarten.",
     "metric": "species_caught", "threshold": 9, "rarity": "gold", "points": 150, "sort_order": 3},
    {"slug": "all-species", "category": "collector", "name": "Complete Collection", "name_de": "Vollständige Sammlung",
     "description": "Catch all 12 fish species!", "description_de": "Fange alle 12 Fischarten!",
     "metric": "species_caught", "threshold": 12, "rarity": "diamond", "points": 500, "sort_order": 4},
    # Server Master - min catches across ALL servers
    # ~125 catches/server/day → "at least X on every server"
    {"slug": "server-allrounder", "category": "server-master", "name": "All-Rounder", "name_de": "Allrounder",
     "description": "Catch 50 bots on every server.", "description_de": "Fange 50 Bots auf jedem Server.",
     "metric": "min_server_catches", "threshold": 50, "rarity": "bronze", "points": 25, "sort_order": 1},
    {"slug": "server-balanced", "category": "server-master", "name": "Balanced Fisher", "name_de": "Ausbalancierter Angler",
     "description": "Catch 250 bots on every server.", "description_de": "Fange 250 Bots auf jedem Server.",
     "metric": "min_server_catches", "threshold": 250, "rarity": "silver", "points": 75, "sort_order": 2},
    {"slug": "server-multi", "category": "server-master", "name": "Multi-Pond Master", "name_de": "Multi-Teich-Meister",
     "description": "Catch 1,000 bots on every server.", "description_de": "Fange 1.000 Bots auf jedem Server.",
     "metric": "min_server_catches", "threshold": 1000, "rarity": "gold", "points": 150, "sort_order": 3},
    {"slug": "server-dominator", "category": "server-master", "name": "Server Dominator", "name_de": "Server-Dominator",
     "description": "Catch 5,000 bots on every server.", "description_de": "Fange 5.000 Bots auf jedem Server.",
     "metric": "min_server_catches", "threshold": 5000, "rarity": "platinum", "points": 300, "sort_order": 4},
    # Data Hoarder - total bytes sent (aggregated from Server.total_bytes_sent)
    # ~800KB/day across all servers
    {"slug": "one-kb-sent", "category": "data-hoarder", "name": "Byte Bite", "name_de": "Byte-Häppchen",
     "description": "Send 1 KB of tarpit data.", "description_de": "Sende 1 KB Tarpit-Daten.",
     "metric": "total_bytes_sent", "threshold": 1024, "rarity": "bronze", "points": 10, "sort_order": 1},
    {"slug": "one-mb-sent", "category": "data-hoarder", "name": "Mega Fisher", "name_de": "Mega-Angler",
     "description": "Send 1 MB of tarpit data.", "description_de": "Sende 1 MB Tarpit-Daten.",
     "metric": "total_bytes_sent", "threshold": 1048576, "rarity": "silver", "points": 50, "sort_order": 2},
    {"slug": "hundred-mb-sent", "category": "data-hoarder", "name": "Data Flood", "name_de": "Datenflut",
     "description": "Send 100 MB of tarpit data.", "description_de": "Sende 100 MB Tarpit-Daten.",
     "metric": "total_bytes_sent", "threshold": 104857600, "rarity": "gold", "points": 150, "sort_order": 3},
    {"slug": "one-gb-sent", "category": "data-hoarder", "name": "Giga Chad Fisher", "name_de": "Giga-Chad-Angler",
     "description": "Send 1 GB of tarpit data.", "description_de": "Sende 1 GB Tarpit-Daten.",
     "metric": "total_bytes_sent", "threshold": 1073741824, "rarity": "diamond", "points": 500, "sort_order": 4},
    # Treasure Hunter - total treasures collected
    {"slug": "first-treasure", "category": "treasure-hunter", "name": "Beachcomber", "name_de": "Strandgutsammler",
     "description": "Collect your first treasure.", "description_de": "Sammle deinen ersten Schatz.",
     "metric": "total_treasures", "threshold": 1, "rarity": "bronze", "points": 15, "sort_order": 1},
    {"slug": "ten-treasures", "category": "treasure-hunter", "name": "Treasure Seeker", "name_de": "Schatzsucher",
     "description": "Collect 10 treasures.", "description_de": "Sammle 10 Schätze.",
     "metric": "total_treasures", "threshold": 10, "rarity": "silver", "points": 50, "sort_order": 2},
    {"slug": "fifty-treasures", "category": "treasure-hunter", "name": "Treasure Diver", "name_de": "Schatztaucher",
     "description": "Collect 50 treasures.", "description_de": "Sammle 50 Schätze.",
     "metric": "total_treasures", "threshold": 50, "rarity": "gold", "points": 100, "sort_order": 3},
    {"slug": "all-treasure-types", "category": "treasure-hunter", "name": "Complete Hoard", "name_de": "Vollständiger Hort",
     "description": "Collect every type of treasure.", "description_de": "Sammle jeden Schatztyp.",
     "metric": "unique_treasure_types", "threshold": 10, "rarity": "platinum", "points": 250, "sort_order": 4},
    # Treasure Hunter - challenges completed
    {"slug": "first-challenge", "category": "treasure-hunter", "name": "Challenge Accepted", "name_de": "Herausforderung angenommen",
     "description": "Complete your first daily challenge.", "description_de": "Schließe deine erste tägliche Herausforderung ab.",
     "metric": "challenges_completed", "threshold": 1, "rarity": "bronze", "points": 15, "sort_order": 5},
    {"slug": "ten-challenges", "category": "treasure-hunter", "name": "Challenge Regular", "name_de": "Stammherausforderer",
     "description": "Complete 10 daily challenges.", "description_de": "Schließe 10 tägliche Herausforderungen ab.",
     "metric": "challenges_completed", "threshold": 10, "rarity": "silver", "points": 50, "sort_order": 6},
    {"slug": "fifty-challenges", "category": "treasure-hunter", "name": "Challenge Champion", "name_de": "Herausforderungs-Champion",
     "description": "Complete 50 daily challenges.", "description_de": "Schließe 50 tägliche Herausforderungen ab.",
     "metric": "challenges_completed", "threshold": 50, "rarity": "gold", "points": 150, "sort_order": 7},
    # Cyber Investigator - IP lookups total
    {"slug": "first-lookup", "category": "cyber-investigator", "name": "First Investigation", "name_de": "Erste Ermittlung",
     "description": "Perform your first IP analysis.", "description_de": "Führe deine erste IP-Analyse durch.",
     "metric": "ip_lookups_total", "threshold": 1, "rarity": "bronze", "points": 10, "sort_order": 1},
    {"slug": "ten-lookups", "category": "cyber-investigator", "name": "Curious Mind", "name_de": "Neugieriger Geist",
     "description": "Analyze 10 unique IPs.", "description_de": "Analysiere 10 verschiedene IPs.",
     "metric": "ip_lookups_total", "threshold": 10, "rarity": "bronze", "points": 25, "sort_order": 2},
    {"slug": "fifty-lookups", "category": "cyber-investigator", "name": "Cyber Detective", "name_de": "Cyber-Detektiv",
     "description": "Analyze 50 unique IPs.", "description_de": "Analysiere 50 verschiedene IPs.",
     "metric": "ip_lookups_total", "threshold": 50, "rarity": "silver", "points": 75, "sort_order": 3},
    {"slug": "two-hundred-lookups", "category": "cyber-investigator", "name": "Intelligence Agency", "name_de": "Geheimdienst-Level",
     "description": "Analyze 200 unique IPs.", "description_de": "Analysiere 200 verschiedene IPs.",
     "metric": "ip_lookups_total", "threshold": 200, "rarity": "gold", "points": 150, "sort_order": 4},
    # Cyber Investigator - abuse score discoveries
    {"slug": "first-high-abuse", "category": "cyber-investigator", "name": "Caught Red-Handed", "name_de": "Auf frischer Tat",
     "description": "Find an IP with an abuse score above 90%.", "description_de": "Finde eine IP mit Abuse-Score über 90%.",
     "metric": "ip_lookups_high_abuse", "threshold": 1, "rarity": "bronze", "points": 25, "sort_order": 5},
    {"slug": "ten-high-abuse", "category": "cyber-investigator", "name": "Repeat Offenders", "name_de": "Wiederholungstäter",
     "description": "Find 10 IPs with abuse score above 90%.", "description_de": "Finde 10 IPs mit Abuse-Score über 90%.",
     "metric": "ip_lookups_high_abuse", "threshold": 10, "rarity": "silver", "points": 75, "sort_order": 6},
    # Cyber Investigator - special discoveries
    {"slug": "first-tor", "category": "cyber-investigator", "name": "Tor Discoverer", "name_de": "Tor-Entdecker",
     "description": "Discover a Tor exit node.", "description_de": "Entdecke einen Tor-Exit-Node.",
     "metric": "ip_lookups_tor", "threshold": 1, "rarity": "silver", "points": 50, "sort_order": 7},
    {"slug": "first-dangerous-ports", "category": "cyber-investigator", "name": "Open Barn Door", "name_de": "Offenes Scheunentor",
     "description": "Find an IP with dangerous open ports.", "description_de": "Finde eine IP mit gefährlichen offenen Ports.",
     "metric": "ip_lookups_dangerous_ports", "threshold": 1, "rarity": "bronze", "points": 15, "sort_order": 8},
    {"slug": "first-vuln", "category": "cyber-investigator", "name": "Vulnerability Finder", "name_de": "Schwachstellenfinder",
     "description": "Find an IP with known vulnerabilities.", "description_de": "Finde eine IP mit bekannten Schwachstellen.",
     "metric": "ip_lookups_vulns", "threshold": 1, "rarity": "silver", "points": 50, "sort_order": 9},
    {"slug": "five-vulns", "category": "cyber-investigator", "name": "Vulnerability Scanner", "name_de": "Vulnerability Scanner",
     "description": "Find 5 IPs with known vulnerabilities.", "description_de": "Finde 5 IPs mit bekannten Schwachstellen.",
     "metric": "ip_lookups_vulns", "threshold": 5, "rarity": "gold", "points": 100, "sort_order": 10},
    # Secret Achievement - Wolf Digital Empire
    {"slug": "wolf-friend", "category": "treasure-hunter", "name": "Friend of the Wolf", "name_de": "Freund des Wolfs",
     "description": "Find the legendary Wolf Head treasure.", "description_de": "Finde den legendären Wolfskopf-Schatz.",
     "metric": "unique_treasure_types", "threshold": 10, "rarity": "diamond", "points": 500,
     "is_secret": True, "sort_order": 8},
    # Tip collection achievements (dynamic thresholds updated by seed_game_data)
    {"slug": "security-scholar", "category": "treasure-hunter", "name": "Security Scholar", "name_de": "Sicherheitsforscher",
     "description": "Discover all security tips.", "description_de": "Entdecke alle Sicherheitstipps.",
     "metric": "unique_security_tips", "threshold": 35, "rarity": "gold", "points": 150, "sort_order": 9},
    {"slug": "tip-completionist", "category": "treasure-hunter", "name": "Tip Completionist", "name_de": "Tipp-Komplettist",
     "description": "Discover all tips across all categories.", "description_de": "Entdecke alle Tipps in allen Kategorien.",
     "metric": "unique_tips_total", "threshold": 68, "rarity": "diamond", "points": 500, "sort_order": 10},
]
