# Component: Button

Trigger for an action. Always a real `<button>` element (links that navigate use `<a>`).

Preview: [button.html](button.html)

## Anatomy

```html
<button class="pds-btn pds-btn--primary">
  <span class="pds-btn__label">Label</span>
</button>
```

Optional: leading/trailing icon slots (`.pds-btn__icon`), spinner (`.pds-btn__spinner`) for loading.

## Variants

| Variant | Class | Use when |
|---|---|---|
| Primary | `pds-btn--primary` | The single main action of a view |
| Secondary | `pds-btn--secondary` | Supporting actions |
| Ghost | `pds-btn--ghost` | Low-emphasis actions (toolbars, cards) |
| Danger | `pds-btn--danger` | Destructive/irreversible actions |

Sizes: `pds-btn--sm` / (default) / `pds-btn--lg`.
Icon-only buttons must carry `aria-label`.

## States

| State | Behavior |
|---|---|
| default | Resting appearance |
| hover | Background shift via `--pds-accent-hover` (ghost: subtle surface) |
| focus-visible | 3px `--pds-focus-ring` outline, 2px offset — never removed |
| active | Slight background deepen + 1px translateY |
| disabled | 45% opacity, `not-allowed` cursor, removed from tab order via `disabled` |
| loading | Label replaced by spinner + `aria-busy="true"`; button stays same width |

## Responsive behavior

- ≥768px: default padding, label on one line.
- <768px: full-width modifier `pds-btn--block` recommended for primary CTAs in forms;
  icon-only buttons keep ≥44×44px touch target.
- Text must never truncate; wrap to 2 lines max before reducing size.

## Accessibility

- Real `<button>` (submit buttons: `type="submit"` explicitly).
- Accessible name: visible text, or `aria-label` for icon-only.
- Focus-visible ring on **all** variants (contrast ≥ 3:1 against adjacent colors).
- Disabled buttons: use the `disabled` attribute, not just CSS.
- Loading: `aria-busy="true"`; keep focus on the button.

## Do / Don't

- DO use one primary button per view region.
- DON'T use `<div>`/`<span>` as buttons.
- DO use Danger only for destructive actions.
- DON'T rely on color alone to signal danger — the label should say it (e.g. "Delete").
