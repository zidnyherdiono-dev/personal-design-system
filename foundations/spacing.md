# Foundation: Spacing

## Principle
Consistent spacing creates rhythm and perceived quality more than any ornament.

## Rules
1. Use the **4px base unit** scale (`tokens/spacing`). No arbitrary values.
2. Vertical rhythm: section padding > block padding > element padding (strictly ordered).
3. Gaps within a group < gaps between groups (Gestalt proximity).
4. Layout containers: define max content width per project type (landing ≠ dashboard ≠ article).

## Scale reference
`1` 4px · `2` 8px · `3` 12px · `4` 16px · `6` 24px · `8` 32px · `12` 48px · `16` 64px · `24` 96px

## Do / Don't
- DO express spacing via tokens/variables in components.
- DON'T center everything by default; alignment should follow content structure.
