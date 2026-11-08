// Button preview behavior (demo only): loading-state toggle.
// Progressive enhancement — buttons work without this file.
(function () {
  document.querySelectorAll('[data-pds-demo="loading"]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      if (btn.getAttribute('aria-busy') === 'true') return;
      var label = btn.querySelector('.pds-btn__label');
      var original = label.textContent;
      btn.setAttribute('aria-busy', 'true');
      label.textContent = 'Loading…';
      var spinner = document.createElement('span');
      spinner.className = 'pds-btn__spinner';
      btn.prepend(spinner);
      setTimeout(function () {
        btn.removeAttribute('aria-busy');
        label.textContent = original;
        spinner.remove();
      }, 1600);
    });
  });
})();
