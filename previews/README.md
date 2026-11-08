# Previews — shared preview system

Zero-build static preview infrastructure.

| File | Purpose |
|---|---|
| `preview.css` | Shared chrome for preview pages (`.pv-page`, `.pv-header`, `.pv-section`, …) |
| `preview.js` | Gallery shell behavior: navigation + viewport switcher (desktop/tablet/mobile) |
| `../index.html` | **Preview hub** — lists every component/pattern/template in an iframe canvas |

## How it works

- Every component/pattern/template ships its own `<name>.html` — a complete static page.
- `index.html` embeds those pages in an iframe and lets you switch viewport width
  (1280 / 768 / 375 px) to inspect responsive behavior.
- Everything works from a plain static server (`python scripts/serve.py`) with no build step.

## Preview page conventions

- `<body class="pv-page">`, header via `.pv-header` / `.pv-title` / `.pv-sub`.
- Sections via `.pv-section` + `.pv-h2`; rows/stacks via `.pv-row` / `.pv-stack`.
- Simulated states are labeled "(simulated)" so nobody mistakes them for real interaction.
