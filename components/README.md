# Components

Self-contained, framework-independent UI components. Each folder contains:

```
components/<name>/
├── <name>.html   ← live static preview (open directly or via index.html gallery)
├── <name>.css    ← component styles (token-driven only)
├── <name>.js     ← behavior (vanilla JS, optional; degrades gracefully)
└── README.md     ← documentation, always in the 4-section standard below
```

## Documentation standard (required sections)

Every component README **must** contain:

1. **Variants** — visual/functional variations (e.g. primary/secondary/danger) with when to use each.
2. **States** — default, hover, focus-visible, active, disabled, loading/empty where applicable.
3. **Responsive behavior** — how it adapts across breakpoints (≥1024 / 768–1023 / <768).
4. **Accessibility** — keyboard, ARIA/semantics, contrast notes, reduced-motion behavior.

Plus: Anatomy (markup structure) and Do/Don't guidance.
See `docs/documentation-standard.md` for the copy-paste template.

## Rules

- Styling references **tokens only** (`../../tokens/tokens.css`) — never hard-coded identity values.
- Must render and behave correctly when opened as a bare file (no build step).
- JS is progressive enhancement: core content visible without it.
- Keep semantics: real `<button>`, `<a>`, `<input>` elements, never divs with click handlers.

## Catalog

| Component | Description | Status |
|---|---|---|
| [button](button/) | Actions: primary/secondary/ghost/danger × states × sizes | stable |
| [input](input/) | Text inputs + textarea, labels, help/error text | stable |
| [card](card/) | Content container: media, body, actions, selectable | stable |
| [badge](badge/) | Status/category labels: neutral/semantic/interactive | stable |
