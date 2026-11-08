# Design Tokens — PROVISIONAL

> **These tokens are placeholders. They are NOT a design identity.**
> See [`STATUS.md`](STATUS.md) for the governing declaration.

## What a token means here

A token is a **role + placeholder value**. The role is the stable part (`surface`, `accent`,
`text-muted`); the value is a stand-in until a real design direction is chosen.

Projects should:

1. Keep the **role names** (they are the contract).
2. Replace the **values** with their own palette/type/spacing.
3. Never present placeholder values as final brand decisions.

## Files

| File | Purpose |
|---|---|
| `tokens.json` | Source of truth. Framework-agnostic, machine-readable. |
| `tokens.css` | CSS custom-properties mirror for direct use in HTML previews. |
| `STATUS.md` | Provisional-status declaration and rules for promotion to final. |

## Token groups

- **color** — role-based (background, surface, text, accent, feedback, border)
- **typography** — family roles + modular scale
- **spacing** — base unit + scale
- **radius** — corner scale
- **shadow** — elevation levels
- **motion** — durations + easings

## Promotion to "final"

A token group may be marked final only when:

1. The user has explicitly decided a design direction, and
2. `STATUS.md` is updated (scope + date + decision reference), and
3. Both `tokens.json` and `tokens.css` are updated **together**.
