# AI Integration Guide

How AI coding agents should consume this repository from other projects.

## Entry points (read in this order)

1. `AGENTS.md` — hard rules (never finalize design preference, never treat provisional tokens as identity).
2. `tokens/tokens.json` — machine-readable token roles (source of truth).
3. `templates/catalog.json` — machine-readable template catalog (categories, sections, status).
4. Component `README.md` files — behavior contract (variants/states/responsive/a11y).

## Integration options

| Option | How | Best for |
|---|---|---|
| Git submodule | `git submodule add <repo-url> vendor/personal-design-system` | projects that want pinned versions |
| Sparse checkout | `git clone --filter=blob:none --sparse` + `sparse-checkout set tokens components` | minimal footprint |
| Raw file fetch | fetch `tokens/tokens.json` / specific component files from raw URLs | one-off reuse, CI tooling |
| Manual copy | copy folders into the project | simplest; record provenance |

## Consumption contract

1. Token **roles** are the API. Copy role names, replace values.
2. Component HTML/CSS/JS are reference implementations — port them into the target framework
   (React/Vue/Svelte/HTML) rather than importing at runtime.
3. Preserve the accessibility contract from each README when porting.
4. `templates/catalog.json` `status` field: `scaffold` means structure-only — do not present as final design.

## Prohibited behaviors (again, because it matters)

- Presenting placeholder tokens as the user's chosen design.
- Choosing a visual style on the user's behalf without confirmation.
- Fabricating content (names, data, brand claims) to fill placeholders.
- Locking a project to one style because this repo's previews look that way.

## Suggested prompt pattern (for users)

> "Use my personal-design-system repo as the structural reference: take components and the
> token *roles* from it, but let's decide the visual direction first."

## Provenance note template (paste into the consuming project)

```
Design structure adapted from Personal Design System (MIT),
<repo-url>, commit <sha>. Visual identity is project-specific.
```
