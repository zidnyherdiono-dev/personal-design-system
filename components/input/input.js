// Input preview behavior (demo only): live error-state simulation.
(function () {
  var form = document.querySelector('[data-pds-demo="validate"]');
  if (!form) return;
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var input = form.querySelector('.pds-input');
    var err = form.querySelector('.pds-error-text');
    var ok = input.value.trim().length > 0;
    input.classList.toggle('pds-input--error', !ok);
    input.setAttribute('aria-invalid', String(!ok));
    err.hidden = ok;
  });
})();
