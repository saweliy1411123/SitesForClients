---
name: SKILL — glassy-nav-bar
source: localhost:8080/ovh/gpt-oss-120b
round: 105
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — glassy-nav-bar

**Name:** `glassy-nav-bar`
**When to apply:** На любой лендинг с фиксированным верхним меню, где нужен премиальный «стеклянный» вид.
**SAFE CSS:**
```css
/* glassy-nav-bar */
nav.glassy {
position: sticky;
top: 0;
z-index: 1000;
backdrop-filter: blur(12px) saturate(180%);
-webkit-backdrop-filter: blur(12px) saturate(180%);
background: rgba(255,255,255,0.12);
border-bottom: 1px solid rgba(255,255,255,0.18);
padding: 0.5rem 1rem;
display: flex;
justify-content: space-between;
align-items: center;
}
nav.glassy a {
color: var(--blue);
text-decoration: none;
font-weight:600;
}
nav.glassy a:hover,
nav.glassy a:focus-visible {
color: var(--purple);
}
```
**SAFE JS:** (не требуется)

## Когда применять
Повышает восприятие бренда как «премиального», улучшает визуальную иерархию и делает навигацию всегда доступной без дополнительного кода.

## Проверка
Открыть страницу, прокрутить вниз – меню должно «прилипнуть» к верхней части и выглядеть полупрозрачным со стеклянным блёром; проверить в Chrome DevTools → Computed Styles → `backdrop-filter`.

## SAFE JS
```js
** (не требуется)
```
