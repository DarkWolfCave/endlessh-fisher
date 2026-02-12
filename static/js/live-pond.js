/**
 * Live Pond Controller
 * Handles splash animations for new fish and real-time timer updates.
 * Fish positions are computed server-side (deterministic hash) and set via inline styles.
 */
(function() {
    'use strict';

    let previousFishIds = new Set();

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

    // Initial setup
    document.addEventListener('DOMContentLoaded', function() {
        initFish();
        setInterval(updateTimers, 1000);
    });

    // Re-init after HTMX content swap
    document.addEventListener('htmx:afterSettle', function(evt) {
        if (evt.detail.target && evt.detail.target.id === 'live-pond-container') {
            initFish();
        }
    });
})();
