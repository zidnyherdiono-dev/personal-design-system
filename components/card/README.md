# Component: Card

Container grouping media, text, and actions. Structure-first: the visual style is a neutral
demonstration driven by tokens — projects re-skin it freely.

Preview: [card.html](card.html)

## Anatomy

```html
<article class="pds-card">
  <img class="pds-card__media" src="…" alt="…" />
  <div class="pds-card__body">
    <h3 class="pds-card__title">Title</h3>
    <p class="pds-card__text">Body text</p>
  </div>
  <footer class="pds-card__actions">…</footer>
</article>
```

## Variants

| Variant | Class | Use when |
|---|---|---|
| Basic | `pds-card` | Default content grouping |
| Media top | `pds-card--media-top` | Visual-first entries (projects, articles) |
| Interactive | `pds-card--interactive` | Whole card is clickable/focusable |
| Selectable | `pds-card--selected` | Selection state (with `aria-pressed`) |

## States

| State | Behavior |
|---|---|
| default | border `--pds-border`, shadow `sm` |
| hover (interactive) | shadow `md`, border-strong |
| focus-visible | focus ring around card |
| selected | accent border + `aria-pressed="true"` |
| disabled | 50% opacity, no pointer events |

## Responsive behavior

- Cards live in CSS grid: `repeat(auto-fill, minmax(260px, 1fr))` — 1 col mobile, 2–3 tablet/desktop.
- Media keeps aspect-ratio (e.g. 16/9) and never distorts.
- Actions wrap under content at narrow widths.

## Accessibility

- Semantic wrapper: `<article>` (or `<li>` in lists).
- Interactive card = real `<a>`/`<button>` wrapper or handler — with visible focus.
- Media alt text required; decorative media `alt=""`.
- Heading level inside card follows page heading order.

## Do / Don't
- DO keep one primary action per card.
- DON'T nest interactive elements (no clickable card + inner buttons without clear hierarchy).
