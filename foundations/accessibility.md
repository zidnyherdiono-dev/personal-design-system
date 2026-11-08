# Foundation: Accessibility (non-negotiable)

Baseline that applies to every component and template here, regardless of visual style.

## Requirements
1. **Keyboard**: every interactive element reachable and operable via Tab/Enter/Space/Escape.
   Visible focus indicator (token `focus-ring`), never `outline: none` without a replacement.
2. **Color contrast**: ≥ 4.5:1 body, ≥ 3:1 large text and UI component boundaries (WCAG 2.2 AA).
3. **Labels**: form controls have programmatically associated labels; buttons have accessible names.
4. **Semantics**: correct HTML elements (`button`, `a`, `nav`, `main`, headings in order).
5. **Motion**: honor `prefers-reduced-motion: reduce`.
6. **Zoom/reflow**: content usable at 320px width and 200% zoom.
7. **Images**: meaningful alt text; decorative images `alt=""`.

## Verification checklist (per component)
- [ ] Tab order sensible, focus visible
- [ ] Screen-reader name correct (test with accessibility tree if possible)
- [ ] Contrast pass on all states (default/hover/disabled)
- [ ] Reduced-motion path works
