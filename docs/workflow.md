# Workflow — Using This Repository End to End

## 0. Prerequisites
A static server (Python is enough): `python scripts/serve.py` → `http://localhost:8080`.

## 1. Choose design direction (per project)
Before styling anything, decide the direction **with the stakeholder**:
theme (light/dark), mood (minimal/bold/editorial/playful), density, motion level.
If undecided: deliver structure first (wireframe/scaffold) — never silently pick an identity.

## 2. Map token roles
Open `tokens/tokens.json`. For each role (`background`, `accent`, `text-primary`, …), assign the
project's real values. Keep role names. Update `tokens.css` counterpart in the project.

## 3. Compose from components & patterns
1. Browse previews (`index.html`) and read the component README (variants/states/responsive/a11y).
2. Copy `<name>.html` markup + `<name>.css` + `<name>.js` into the project.
3. Replace any placeholder content — never invent real content on behalf of a person.

## 4. Assemble pages from templates
Pick a category from `templates/README.md`, open the scaffold, replace section content,
apply the design direction. Keep the accessibility contract from the template README.

## 5. Verify
- [ ] Keyboard pass (Tab/Enter/Escape), visible focus everywhere
- [ ] Contrast ≥ 4.5:1 (body) / 3:1 (large/UI)
- [ ] Responsive check at 375 / 768 / 1280 px (use the gallery viewport switcher)
- [ ] Reduced-motion pass
- [ ] Run `python scripts/validate.py` if you modified this repo

## 6. Record provenance
Note in the project (README/AGENTS.md) which parts were adapted from this repository.
