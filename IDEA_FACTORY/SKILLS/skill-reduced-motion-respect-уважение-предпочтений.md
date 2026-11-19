---
name: SKILL — reduced-motion-respect (уважение предпочтений пользователя по анимациям)
source: localhost:8081/big_only
round: 133
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — reduced-motion-respect (уважение предпочтений пользователя по анимациям)


SKILL — reduced-motion-respect
Name: `reduced-motion-respect`
When to apply: На любом лендинге с CSS-анимациями, трансформациями, параллаксом — для соблюдения WCAG 2.1 (Success Criterion 2.3.3) и уважения пользователей с вестибулярными нарушениями.
SAFE CSS:
```css
@media (prefers-reduced-motion: reduce) {
*, *::before, *::after {
animation-duration: 0.01ms !important;
animation-iteration-count: 1

## Когда применять


## Проверка

