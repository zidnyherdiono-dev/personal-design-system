# Pattern: Hero Section

Above-the-fold region: eyebrow label, headline, supporting text, CTA row, media slot.

Preview: [hero-section.html](hero-section.html)

## Anatomy
`eyebrow → headline (h1) → lead paragraph → CTA row (1 primary + 1 secondary) → media slot`

## Variants
| Variant | Use when |
|---|---|
| Text + media (default) | Visual product/person focus |
| Text-only | Copy-driven pages (media slot removed, single column) |
| Centered | Announcements / minimal landing |

## States
Hero is static content; interactive states live in its CTA buttons (see `components/button`).
Media slot states: placeholder → loaded → failed (keep alt text meaningful on failure).

## Layout rules
- Two-column (text + media) at ≥ 900px; stacked (text first) below.
- Content max-width keeps headline measure ≤ 20 characters per line at desktop.
- Exactly **one** primary CTA.

## Responsive
- <768px: headline scales via `clamp()`, CTA row wraps or goes full-width.
- Media below text on mobile; never behind text.

## Accessibility
- Exactly one `<h1>` (the headline). Eyebrow is a `<p>`, not a heading.
- Decorative media `alt=""`; meaningful media gets descriptive alt.
- CTA pair: primary is a `<button>` (action) or `<a>` (navigation) — match semantics to behavior.
