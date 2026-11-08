# Foundation: Color

## Principle
Color communicates **role** first, taste second. Decide roles before hues.

## Roles (contract)
`background` · `surface` · `text-primary` · `text-secondary` · `text-muted` · `accent` ·
`border` · `focus-ring` · `success` · `warning` · `danger` · `info`

## Rules
1. **Text contrast**: body text ≥ 4.5:1, large text (≥ 24px / 19px bold) ≥ 3:1 (WCAG AA).
2. **Never encode meaning by color alone** — pair with icon, label, or shape.
3. **One dominant accent per screen** is a safe default; more is possible but must be deliberate.
4. Accent is for *interactive/attention* elements; decorative use dilutes it.
5. Semantic colors (success/warning/danger) keep stable meanings across contexts.

## Do / Don't
- DO define palette values as tokens (roles) and reference tokens only.
- DON'T hard-code hex values inside components — that freezes identity.
- DO test the chosen palette in both light and dark contexts before promoting tokens to final.
- DON'T treat the placeholder palette as the user's preference (see tokens/STATUS.md).
