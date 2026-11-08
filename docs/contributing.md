# Contributing to This Repository

## Adding a component
1. Create `components/<name>/` with `<name>.html|css|js` + `README.md`.
2. README must follow the 4-section standard: **Variants, States, Responsive, Accessibility**
   (copy the skeleton from `docs/documentation-standard.md`).
3. Styles reference `tokens.css` variables only — no hard-coded identity colors.
4. Update the catalog table in `components/README.md`.
5. Register the preview in `previews/preview.js` (NAV array).
6. Run `python scripts/serve.py` and verify in `index.html`; then `python scripts/validate.py`.

## Adding a pattern
Same rules as components, folder `patterns/<name>/`, and register in `patterns/README.md`.

## Adding a template
See `templates/README.md` (category taxonomy). Always add/refresh the `templates/catalog.json`
entry — AI agents read it.

## Changing tokens
- Values may be tweaked freely **while status is PROVISIONAL** (both `tokens.json` and `tokens.css`).
- Changing the *meaning* of a role requires a note in `tokens/STATUS.md`.
- Promoting to FINAL requires an explicit design decision recorded in `tokens/STATUS.md`.

## Hard rules
- No build-step dependencies. Static HTML/CSS/JS only.
- No fabricated content in examples — use clearly-labeled placeholders.
- Don't remove existing files without documenting why.
