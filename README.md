# Personal Design System

Framework-independent design reference system built with **HTML, CSS, JavaScript, and Markdown**.
Reusable by humans and AI coding agents across any project, any stack.

> **STATUS: FOUNDATION PHASE.** Design direction is intentionally **not decided yet**.
> All tokens are **PROVISIONAL placeholders** — never treat them as a final visual identity.

## What this is

- A **reference library**: design tokens (roles, not fixed identity), foundations, components, patterns, and template scaffolds.
- A **preview system**: every component and template has a live static preview (zero build step).
- A **machine-readable catalog**: AI agents can discover and reuse everything here.

## What this is NOT

- Not a final design identity / brand.
- Not locked to one visual style (works for portfolio, landing, dashboard, editorial, etc.).
- Not a component *library* to npm-install — copy and adapt, do not depend.

## Repository structure

```
personal-design-system/
├── README.md            ← you are here
├── AGENTS.md            ← instructions for AI coding agents (read this first if you are an agent)
├── index.html           ← preview hub (open in browser)
├── tokens/              ← PROVISIONAL design tokens (roles + placeholder values)
├── foundations/         ← color, typography, spacing, motion, elevation, accessibility
├── components/          ← UI components: preview (html/css/js) + docs (variants/states/responsive/a11y)
├── patterns/            ← multi-component compositions (hero, contact form, …)
├── templates/           ← categorized website scaffolds + machine-readable catalog
├── previews/            ← shared preview chrome (gallery shell, viewport switcher)
├── docs/                ← workflow, contributing, documentation standard, AI integration
└── scripts/             ← validation + local preview server
```

## Quick start (no build step)

```bash
# option 1: helper script
python scripts/serve.py          # serves at http://localhost:8080

# option 2: any static server
python -m http.server 8080
```

Open `http://localhost:8080` — the preview hub lists every component, pattern, and template.

## Core principles

1. **Roles over values.** Tokens define *roles* (`surface`, `accent`, `text-muted`) with placeholder values. Projects map roles to their own palette.
2. **Provisional ≠ permanent.** `tokens/STATUS.md` governs. No token becomes a brand until a design direction is explicitly chosen.
3. **Style-agnostic.** Components demonstrate structure, states, and behavior. Visual styling is intentionally minimal and driven by tokens so it can be swapped wholesale.
4. **Documented behavior.** Every component documents variants, states, responsive behavior, and accessibility.
5. **AI-ready.** `AGENTS.md` + `templates/catalog.json` + `docs/ai-integration.md` make this repo consumable by coding agents.

## For humans

1. Read `docs/workflow.md`.
2. Browse previews via `index.html`.
3. Copy what you need into your project and re-map the tokens.

## For AI agents

Read **`AGENTS.md`** — it defines hard rules (especially: never finalize design preference from this repo).
