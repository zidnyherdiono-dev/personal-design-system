# Foundation: Motion

## Principle
Motion explains change. If it doesn't explain anything, remove it.

## Rules
1. Duration roles: `fast` (micro-feedback), `normal` (state change), `slow` (entrance/exit of large elements).
2. Ease roles: `standard` (general), `entrance` (arriving), `exit` (leaving).
3. Prefer `transform`/`opacity` animation (performance).
4. **Respect `prefers-reduced-motion`** — provide a no-motion path (see accessibility.md).
5. Motion must never block interaction or delay content.

## Do / Don't
- DO animate state changes that benefit from continuity (hover, reveal, progress).
- DON'T add ambient looping animation without purpose — it competes with content.
- DO keep durations in tokens.
