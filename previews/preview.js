// Gallery shell: sidebar navigation + viewport switcher for the preview iframe.
// Vanilla JS, no dependencies. Works over file:// and any static server.
(function () {
  var NAV = [
    {
      group: 'Components',
      items: [
        { label: 'Button', src: 'components/button/button.html' },
        { label: 'Input', src: 'components/input/input.html' },
        { label: 'Card', src: 'components/card/card.html' },
        { label: 'Badge', src: 'components/badge/badge.html' }
      ]
    },
    {
      group: 'Patterns',
      items: [
        { label: 'Hero Section', src: 'patterns/hero-section/hero-section.html' },
        { label: 'Contact Form', src: 'patterns/contact-form/contact-form.html' }
      ]
    },
    {
      group: 'Templates',
      items: [
        { label: 'Portfolio Scaffold', src: 'templates/portfolio-scaffold/index.html' }
      ]
    }
  ];

  var VIEWPORTS = [
    { label: 'Desktop', width: '100%' },
    { label: 'Tablet', width: '768px' },
    { label: 'Mobile', width: '375px' }
  ];

  var sidebar = document.getElementById('pv-nav');
  var canvas = document.getElementById('pv-canvas');
  var vpRow = document.getElementById('pv-viewports');
  var current = null;

  NAV.forEach(function (group) {
    var h = document.createElement('h2');
    h.className = 'pv-nav-group';
    h.textContent = group.group;
    sidebar.appendChild(h);

    group.items.forEach(function (item) {
      var a = document.createElement('button');
      a.type = 'button';
      a.className = 'pv-nav-item';
      a.textContent = item.label;
      a.addEventListener('click', function () {
        canvas.src = item.src;
        current && current.classList.remove('is-active');
        a.classList.add('is-active');
        current = a;
      });
      sidebar.appendChild(a);
    });
  });

  VIEWPORTS.forEach(function (vp, i) {
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'pv-vp' + (i === 0 ? ' is-active' : '');
    b.textContent = vp.label;
    b.addEventListener('click', function () {
      canvas.style.width = vp.width;
      vpRow.querySelectorAll('.pv-vp').forEach(function (el) { el.classList.remove('is-active'); });
      b.classList.add('is-active');
    });
    vpRow.appendChild(b);
  });

  // Load first item by default.
  var first = sidebar.querySelector('.pv-nav-item');
  if (first) first.click();
})();
