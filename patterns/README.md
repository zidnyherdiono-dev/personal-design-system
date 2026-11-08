# Patterns

Multi-component compositions: recipes that assemble components into common page regions.
Patterns are **structural** — copy the arrangement, re-skin with the project's tokens.

```
patterns/<name>/
├── <name>.html   ← live static preview
├── <name>.css    ← composition-only styles (token-driven)
└── README.md     ← anatomy, layout rules, responsive + a11y notes
```

| Pattern | Composes | Status |
|---|---|---|
| [hero-section](hero-section/) | typography + button + media slot | stable |
| [contact-form](contact-form/) | input + button + badge (feedback) | stable |
