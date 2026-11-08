// Card preview behavior (demo only): selectable card toggle.
(function () {
  document.querySelectorAll('[data-pds-demo="select"]').forEach(function (card) {
    card.addEventListener('click', function () {
      var on = card.getAttribute('aria-pressed') === 'true';
      card.setAttribute('aria-pressed', String(!on));
      card.classList.toggle('pds-card--selected', !on);
    });
  });
})();
