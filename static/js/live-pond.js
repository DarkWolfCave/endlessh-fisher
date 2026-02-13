/**
 * Live Pond Controller
 * Handles splash animations for new fish, real-time timer updates,
 * and treasure collection with security tip modal.
 * Fish positions are computed server-side (deterministic hash) and set via inline styles.
 */
(function() {
    'use strict';

    // --- i18n for static JS strings ---
    var _jsT = {
        'Schatz gefunden!': 'Treasure found!',
        'Punkte': 'Points',
        'Klicken zum Kopieren': 'Click to copy',
        'Verstanden': 'Got it',
    };
    function _t(s) {
        return (window.GAME_LANG === 'en') ? (_jsT[s] || s) : s;
    }

    var previousFishIds = new Set();

    // --- Treasure tracking via localStorage ---
    var collectedTreasureIds = [];
    try {
        collectedTreasureIds = JSON.parse(localStorage.getItem('collectedTreasures') || '[]');
    } catch (e) {
        collectedTreasureIds = [];
    }

    function initFish() {
        var pond = document.getElementById('live-pond-data');
        if (!pond) return;

        var currentFishIds = new Set();
        var fishElements = pond.querySelectorAll('.pond-fish');

        fishElements.forEach(function(el) {
            var fishId = el.dataset.fishId;
            if (!fishId) return;
            currentFishIds.add(fishId);

            // Splash animation for newly appeared fish
            if (previousFishIds.size > 0 && !previousFishIds.has(fishId)) {
                el.classList.add('fish-splash');
                setTimeout(function() { el.classList.remove('fish-splash'); }, 1000);
            }
        });

        previousFishIds = currentFishIds;
    }

    function initTreasures() {
        var pond = document.getElementById('live-pond-data');
        if (!pond) return;

        var treasureElements = pond.querySelectorAll('.pond-treasure');
        treasureElements.forEach(function(el) {
            var tid = el.dataset.treasureId;
            // Hide if already collected in this browser session
            if (collectedTreasureIds.indexOf(tid) !== -1) {
                el.style.display = 'none';
            }
        });
    }

    function formatDuration(seconds) {
        if (seconds < 60) return Math.floor(seconds) + 's';
        if (seconds < 3600) return (seconds / 60).toFixed(1) + 'min';
        if (seconds < 86400) return (seconds / 3600).toFixed(1) + 'h';
        return (seconds / 86400).toFixed(1) + 'd';
    }

    function updateTimers() {
        var now = Date.now() / 1000;
        var timers = document.querySelectorAll('.fish-tooltip-timer');
        timers.forEach(function(el) {
            var base = parseFloat(el.dataset.baseSeconds) || 0;
            var lastSeen = Date.parse(el.dataset.lastSeen) / 1000;
            if (lastSeen && base) {
                var elapsed = Math.max(0, now - lastSeen);
                el.textContent = formatDuration(base + elapsed);
            }
        });
    }

    // --- Treasure Collection (called by hx-on::after-request) ---
    window.treasureCollected = function(evt) {
        if (!evt.detail.successful) return;
        var xhr = evt.detail.xhr;
        var data;
        try { data = JSON.parse(xhr.responseText); } catch (e) { return; }
        if (!data.success) return;

        var el = evt.detail.elt;
        var tid = el.dataset.treasureId;

        // Track in localStorage (keep last 200)
        collectedTreasureIds.push(tid);
        if (collectedTreasureIds.length > 200) {
            collectedTreasureIds = collectedTreasureIds.slice(-200);
        }
        try {
            localStorage.setItem('collectedTreasures', JSON.stringify(collectedTreasureIds));
        } catch (e) { /* quota exceeded - ignore */ }

        // Visual feedback: collect animation
        el.classList.add('treasure-collected');
        el.style.pointerEvents = 'none';
        setTimeout(function() { el.remove(); }, 800);

        // Show security tip modal (or toast if no tip)
        if (data.tip) {
            showTipModal(data);
        } else {
            showTreasureToast(data);
        }
    };

    function showTreasureToast(data) {
        var toast = document.createElement('div');
        toast.className = 'treasure-toast';
        toast.innerHTML =
            '<span class="treasure-toast-emoji">' + data.emoji + '</span>' +
            '<div class="treasure-toast-info">' +
                '<span class="treasure-toast-label" style="color: ' + data.rarity_color + ';">' + _t('Schatz gefunden!') + '</span>' +
                '<span class="treasure-toast-name">' + data.treasure_name + '</span>' +
                '<span class="treasure-toast-points">+' + data.points + ' ' + _t('Punkte') + '</span>' +
            '</div>';
        document.body.appendChild(toast);
        setTimeout(function() {
            toast.classList.add('treasure-toast-leave');
            setTimeout(function() { toast.remove(); }, 400);
        }, 3000);
    }

    function escapeHtml(str) {
        var div = document.createElement('div');
        div.textContent = str;
        return div.innerHTML;
    }

    function formatTipContent(escaped) {
        // Convert `code` backtick notation to <code> tags with copy button
        return escaped.replace(/`([^`]+)`/g, function(_, code) {
            return '<code class="tip-code" title="' + _t('Klicken zum Kopieren') + '" ' +
                'onclick="navigator.clipboard.writeText(this.textContent)' +
                '.then(function(){var b=event.target;b.classList.add(\'tip-code-copied\');' +
                'setTimeout(function(){b.classList.remove(\'tip-code-copied\')},1200)})">' +
                code + '</code>';
        });
    }

    function showTipModal(data) {
        var tip = data.tip;
        var overlay = document.createElement('div');
        overlay.className = 'tip-modal-overlay';

        var sourceHtml = '';
        if (tip.source_url) {
            sourceHtml =
                '<a class="tip-modal-source" href="' + escapeHtml(tip.source_url) +
                '" target="_blank" rel="noopener noreferrer">' +
                escapeHtml(tip.source_label || tip.source_url) + ' &rarr;</a>';
        }

        var contentHtml = formatTipContent(escapeHtml(tip.content));

        overlay.innerHTML =
            '<div class="tip-modal">' +
                '<div class="tip-modal-header">' +
                    '<div class="tip-modal-treasure">' +
                        '<span class="tip-modal-emoji">' + data.emoji + '</span>' +
                        '<div>' +
                            '<span class="tip-modal-name" style="color: ' + data.rarity_color + ';">' +
                                escapeHtml(data.treasure_name) + '</span>' +
                            '<span class="tip-modal-points">+' + data.points + ' ' + _t('Punkte') + '</span>' +
                        '</div>' +
                    '</div>' +
                    '<button class="tip-modal-close" onclick="this.closest(\'.tip-modal-overlay\').remove()">&times;</button>' +
                '</div>' +
                '<div class="tip-modal-body">' +
                    '<div class="tip-modal-category">' +
                        '<span>' + tip.tip_emoji + '</span>' +
                        '<span class="tip-modal-rarity tip-rarity-' + tip.rarity + '">' +
                            escapeHtml(tip.title) + '</span>' +
                    '</div>' +
                    '<div class="tip-modal-content">' + contentHtml + '</div>' +
                    sourceHtml +
                '</div>' +
                '<button class="tip-modal-btn" onclick="this.closest(\'.tip-modal-overlay\').remove()">' + _t('Verstanden') + '</button>' +
            '</div>';

        document.body.appendChild(overlay);

        // Close on overlay click (outside modal)
        overlay.addEventListener('click', function(e) {
            if (e.target === overlay) overlay.remove();
        });

        // Close on Escape key
        var escHandler = function(e) {
            if (e.key === 'Escape') {
                overlay.remove();
                document.removeEventListener('keydown', escHandler);
            }
        };
        document.addEventListener('keydown', escHandler);
    }

    // Initial setup
    document.addEventListener('DOMContentLoaded', function() {
        initFish();
        initTreasures();
        setInterval(updateTimers, 1000);
    });

    // Re-init after HTMX content swap
    document.addEventListener('htmx:afterSettle', function(evt) {
        if (evt.detail.target && evt.detail.target.id === 'live-pond-container') {
            initFish();
            initTreasures();
        }
    });
})();
