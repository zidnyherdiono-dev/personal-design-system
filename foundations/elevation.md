# Foundation: Elevation & Surfaces

## Principle
Depth is a hierarchy tool: higher = more important/interactive, not simply "nicer".

## Rules
1. Three surface levels is a safe baseline: `background` → `surface` → elevated (shadow).
2. Borders and background contrast can replace shadows entirely (flat styles) — elevation
   is achieved by luminance steps, not only blur.
3. Shadows scale with element size: small elements get small shadows.
4. Interactive elements may raise elevation on hover — keep it subtle and consistent.

## Do / Don't
- DO pick one depth language per project (shadows OR border steps OR both) and stay consistent.
- DON'T stack multiple heavy shadows; it reads as noise.
