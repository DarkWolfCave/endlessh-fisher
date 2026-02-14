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
        "rarity": "rare",
        "rarity_color": "#34D399",
        "points": 50,
        "spawn_weight": 10,
        "min_pond_percentile": 55,
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
]
