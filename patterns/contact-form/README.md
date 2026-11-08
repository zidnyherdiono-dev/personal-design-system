# Pattern: Contact Form

Form region: labeled inputs, validation feedback, submit action, privacy note.

Preview: [contact-form.html](contact-form.html)

## Anatomy
`heading → name input → message textarea → (optional) consent checkbox → submit button → status message`

## Variants
| Variant | Use when |
|---|---|
| Name + message (default) | General contact |
| Extended | Extra fields (subject, category select) — keep ≤ 5 fields |
| Newsletter | Email only + consent note |

## States
pristine → editing → invalid (per-field errors) → submitting (button `aria-busy`) →
success (`role="status"` message) → server error (retry affordance).

## Layout rules
- Single column, field max-width ~420–520px.
- Errors appear under the field they belong to.
- Status message region (`role="status"`) after submit.

## Responsive
- Full-width fields under 640px; submit button `pds-btn--block` on mobile.

## Accessibility
- `<form>` with real submit; `novalidate` + custom validation keeps messages accessible.
- All fields labeled; errors `role="alert"` + `aria-invalid`.
- Privacy note visible before submit (no hidden data collection).
