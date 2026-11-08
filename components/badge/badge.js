// Badge preview behavior (demo only): filter-chip toggle + removable tag.
(function () {
  document.querySelectorAll('[data-pds-demo="filter"]').forEach(function (chip) {
    chip.addEventListener('click', function () {
      var on = chip.getAttribute('aria-pressed') === 'true';
      chip.setAttribute('aria-pressed', String(!on));
    });
  });
  document.querySelectorAll('[data-pds-demo="remove"]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var tag = btn.closest('.pds-badge');
      if (tag) tag.remove();
    });
  });
})();
