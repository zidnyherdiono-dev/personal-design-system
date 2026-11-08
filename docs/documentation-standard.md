# Documentation Standard — Component README Template

Copy this skeleton into every new `components/<name>/README.md`:

```markdown
# Component: <Name>

One-sentence purpose. Real-semantic-elements note.

Preview: [<name>.html](<name>.html)

## Anatomy
\`\`\`html
<!-- minimal markup skeleton -->
\`\`\`\

## Variants
| Variant | Class | Use when |
|---|---|---|
| ... | ... | ... |

## States
| State | Behavior |
|---|---|
| default | ... |
| hover | ... |
| focus-visible | ... |
| active | ... |
| disabled | ... |
| loading/empty | ... (if applicable) |

## Responsive behavior
- ≥1024px: ...
- 768–1023px: ...
- <768px: ... (touch targets ≥ 44px where interactive)

## Accessibility
- Keyboard: ...
- Semantics/ARIA: ...
- Contrast: ...
- Reduced motion: ...

## Do / Don't
- DO ...
- DON'T ...
```

Rules:
- Simulated states in previews must be labeled "(simulated)".
- Every claim in the doc must be demonstrable in the preview page.
