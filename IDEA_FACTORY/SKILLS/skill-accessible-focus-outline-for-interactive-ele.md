---
name: SKILL — Accessible Focus Outline for Interactive Elements
source: localhost:8080/ovh/gpt-oss-120b
round: 6
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Accessible Focus Outline for Interactive Elements

METHOD: Add a reusable accessibility skill that globally applies a high‑contrast focus‑visible outline to all interactive elements (links, buttons, and any element with `role="button"`).
SAFE CSS:
```css
/* Accessible focus outline – applies only when user navigates via keyboard */
a:focus-visible,
button:focus-visible,
[role="button"]:focus-visible {
outline: 3px solid #8b5cf6;   /* brand accent */
outline-offset: 4px;
box-shadow: 0 0 0 2px #fff;  /* ensures visibility on dark backgrounds */
}
/* Ensure that focus styles are not overridden by existing :focus rules */
a:focus,
button:focus,
[role="button"]:focus {
outline: none;
}
```

## Когда применять
Improves keyboard navigation visibility, boosting accessibility scores (WCAG 2.1 AA) and increasing conversion among users who rely on keyboard or assistive tech.

## Проверка
Open the page, press **Tab** to cycle through links/buttons; confirm a bright purple outline appears only on keyboard focus, not on mouse click. Use Chrome DevTools → Accessibility audit to see no violations.

## SAFE CSS
```css
```css
/* Accessible focus outline – applies only when user navigates via keyboard */
a:focus-visible,
```
