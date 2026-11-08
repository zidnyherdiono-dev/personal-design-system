# Foundation: Typography

## Principle
Hierarchy is created by **scale, weight, spacing, and layout** — not by adding font styles.

## Roles
- `sans` — UI + body default
- `serif` — editorial/display accent (optional)
- `mono` — code, technical labels

## Rules
1. Use the modular scale (`tokens/typography/scale`); avoid one-off font sizes.
2. Body line-height 1.5–1.7; headings tighter (1.1–1.3).
3. Measure (line length) for body text: ~45–75 characters.
4. Limit to **2 weights + 1 accent style** per page as a safe baseline.
5. Fluid type (`clamp()`) is encouraged for display sizes on responsive pages.

## Do / Don't
- DO establish hierarchy before decorating (size → weight → spacing → color).
- DON'T use letter-spacing hacks to force text to fit; fix layout instead.
- DO keep font stacks in tokens so projects can swap families wholesale.
