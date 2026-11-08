# AGENTS.md — Personal Design System (AI Agent Instructions)

You are an AI coding agent. This repository is a **design reference**, not a project to modify casually.
Follow these rules when consuming it from another project.

## Hard rules (never violate)

1. **Never treat provisional tokens as a final design identity.**
   `tokens/tokens.json` has `"status": "PROVISIONAL"`. Placeholder values must not be copied into a
   client/published project as "the brand" without an explicit design decision from the user.
2. **Never invent or freeze the user's design preference.**
   If a design direction has not been decided, ASK. Do not silently pick one.
3. **Never lock a project to one visual style** because it is what this repo happens to show.
   Components here demonstrate *structure and behavior*; the look is deliberately neutral.
4. **Never fabricate missing information** (content, brand colors, user data).
5. Do not delete or restructure files without clear reason; this repo is versioned reference material.

## How to consume this repo

| Need | Where |
|---|---|
| Token roles & placeholder values | `tokens/tokens.json` (source of truth), `tokens/tokens.css` (CSS mirror) |
| Design principles (color/typography/spacing/motion/a11y) | `foundations/*.md` |
| Component structure + states + a11y contract | `components/<name>/README.md` |
| Live visual reference | `components/<name>/<name>.html` (static preview) |
| Composition recipes | `patterns/<name>/` |
| Website scaffolds by category | `templates/catalog.json` → `templates/<name>/` |
| End-to-end usage procedure | `docs/workflow.md` |
| Deeper integration options (submodule, raw URLs) | `docs/ai-integration.md` |

## Integration procedure (in a client project)

1. Determine project type and design direction **with the user** (ask if undecided).
2. Map this repo's token *roles* to the project's own values. Keep role names if possible.
3. Copy component markup/behavior from `components/<name>/<name>.html` + `.js`; re-skin via tokens.
4. Validate accessibility contract from the component README (focus states, labels, contrast).
5. Record in the project what was adapted from here (provenance note) — do not present it as original work.

## File conventions

- Component folder: `components/<name>/<name>.html|css|js` + `README.md` (same four-section doc: Variants, States, Responsive, Accessibility).
- `templates/catalog.json` is the machine-readable index. Keep it in sync when adding templates.
- All previews are static and must open without a build step.

## If you must change this repo

- Additive changes are fine (new components/patterns/templates) — follow `docs/contributing.md`.
- Changing the meaning of existing token roles requires updating `tokens/STATUS.md` and both token files together.
