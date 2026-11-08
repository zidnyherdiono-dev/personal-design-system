# Component: Badge

Compact label for status, category, or count. Static (`span`) or interactive (`button`).

Preview: [badge.html](badge.html)

## Anatomy

```html
<span class="pds-badge pds-badge--success">Published</span>
```

## Variants

| Variant | Class | Use when |
|---|---|---|
| Neutral | `pds-badge` | Category, metadata |
| Semantic | `--success` `--warning` `--danger` `--info` | Status with stable meaning |
| Outline | `pds-badge--outline` | Low emphasis |
| Interactive | `pds-badge--interactive` (real `<button>`) | Filters, removable tags |

## States

default · hover (interactive) · focus-visible (interactive) · selected (`aria-pressed`) · disabled

## Responsive behavior

Badges are inline flow content; wrap naturally. Minimum font size 11px; on touch, interactive
badges keep ≥ 32px height and adequate padding.

## Accessibility

- Semantic badge: plain `<span>` + text (no ARIA needed).
- Interactive badge: real `<button>`, accessible name, focus-visible ring.
- **Never color-only status**: text label inside the badge carries the meaning.
- Removable tags: separate remove `<button>` with `aria-label="Remove <name>"`.

## Do / Don't
- DO keep labels short (1–2 words).
- DON'T use badges for primary actions.
