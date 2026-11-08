# Component: Input

Text field with label, optional help text, and error state. Real `<input>`/`<textarea>` elements.

Preview: [input.html](input.html)

## Anatomy

```html
<div class="pds-field">
  <label class="pds-label" for="name">Label</label>
  <input class="pds-input" id="name" type="text" aria-describedby="name-help" />
  <p class="pds-help" id="name-help">Helper text</p>
</div>
```

Error state adds `pds-input--error` + `role="alert"` message with `aria-describedby` link.

## Variants

| Variant | Class | Use when |
|---|---|---|
| Text input | `pds-input` | Single-line text |
| Textarea | `pds-input pds-input--area` | Multi-line text |
| With leading icon | wrap in `pds-input-wrap` + `.pds-input-icon` | Search, dates, etc. |
| Error | `pds-input--error` | Validation failed |

## States

| State | Behavior |
|---|---|
| default | 1px `--pds-border` border |
| hover | border `--pds-border-strong` |
| focus | 2px `--pds-focus-ring` ring + border accent |
| error | `--pds-danger` border + alert message below |
| disabled | muted background, `not-allowed` cursor |
| placeholder | `--pds-text-muted`; never a substitute for the label |

## Responsive behavior

- Fields stack vertically at all widths (single column inside forms).
- <768px: input font-size ≥ 16px (prevents iOS zoom-on-focus); full-width by default.
- Touch targets ≥ 44px height.

## Accessibility

- Every input has a `<label for>` (never placeholder-only).
- Help/error text linked via `aria-describedby`; error container `role="alert"`.
- `aria-invalid="true"` on error.
- `autocomplete` attributes where meaningful.

## Do / Don't
- DO keep labels visible after input (no floating-label-only patterns in this reference).
- DON'T use placeholder as the only label.
- DO mark required fields explicitly (`required` + visible marker + accessible text).
