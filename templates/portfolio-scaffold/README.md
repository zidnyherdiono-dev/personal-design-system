# Template: Portfolio Scaffold

> **STATUS: SCAFFOLD (structure only).** This is NOT a final design.
> Gray-block wireframe with token-driven base styles. Visual direction is intentionally undecided.

Preview: [index.html](index.html)

Category: `portfolio` · Composes: hero-section pattern, card, button, badge, contact-form pattern.

## Sections & content slots

| Section | Slot | Notes |
|---|---|---|
| Header/Nav | site name, 3–5 links | sticky optional |
| Hero | name/headline, role line, 1 CTA | pattern: hero-section |
| About | 2 short paragraphs + skill badges | replaceable with real content |
| Projects | responsive card grid (auto-fill) | card component; images per project |
| Contact | form + social links | pattern: contact-form (privacy note required) |
| Footer | name, year, links | keep minimal |

## Responsive behavior
- <768px: single column, nav collapses to simple stacked links (JS menu intentionally omitted in scaffold).
- ≥768px: two-column hero, 2-col project grid. ≥1024px: 3-col grid.

## How to use
1. Copy folder into your project.
2. Replace placeholder text/images with real content (never invent content).
3. Map tokens to the chosen design system values.
4. Apply the chosen visual direction — until then, keep it neutral.

## Accessibility
Baseline from `foundations/accessibility.md` applies: landmarks (`header`/`main`/`footer`),
single `h1`, labeled form, visible focus.
