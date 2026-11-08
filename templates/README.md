# Templates — Categorization System

Reusable website scaffolds. **Every template is structure-first**: wireframe-level layout with
token-driven styling. Final visual design is applied per project, after a design direction is chosen.

## Category taxonomy

Templates are indexed by **category** (what the site is) — visual style is a separate axis and is
deliberately NOT baked in.

| Category | Typical sites | Folder prefix |
|---|---|---|
| `portfolio` | personal portfolio, creative showcase | `portfolio-*` |
| `landing` | product/service landing pages | `landing-*` |
| `editorial` | blog, magazine, documentation | `editorial-*` |
| `dashboard` | admin panels, analytics | `dashboard-*` |
| `commerce` | product pages, catalogs | `commerce-*` |
| `event` | conferences, workshops | `event-*` |

## Style axes (applied at consumption time, not stored as identity)

`theme` (light/dark/auto) · `density` (compact/comfortable) · `mood` (minimal/bold/editorial/playful) ·
`motion` (static/subtle/expressive)

## Machine-readable index

`catalog.json` lists every template with its category, composition, and status.
AI agents must read it instead of guessing folder contents.

## Adding a template

1. Pick a category + folder prefix from the table above.
2. Build the scaffold using components/patterns from this repo.
3. Mark status honestly (`scaffold` until it is more than structure).
4. Add an entry to `catalog.json`.
5. Document sections + slots in the template README.
