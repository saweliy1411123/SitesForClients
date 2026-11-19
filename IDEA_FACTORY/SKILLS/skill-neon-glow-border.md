---
name: SKILL — neon-glow-border
source: localhost:8080/ovh/gpt-oss-120b
round: 91
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — neon-glow-border

**Name:** `neon-glow-border`
**When to apply:** На всех CTA‑кнопках (`.btn-primary`) и на карточках цены (`.price-card`) для придания премиального «неонового» обводки.
**SAFE CSS:**
```css
/* neon glow border */
.neon-glow {
position: relative;
overflow: hidden;
}
.neon-glow::before {
content: "";
position: absolute;
inset: -2px;
background: linear-gradient(45deg,
#8b5cf6, #4ec9f0, #8b5cf6);
filter: blur(6px);
opacity: 0;
transition: opacity .3s ease-in-out;
z-index: -1;
}
.neon-glow:hover::before,
.neon-glow:focus-visible::before {
opacity: 0.8;
}
.neon-glow {
box-shadow: 0 0 10px rgba(139,92,246,.2);
}
```
**SAFE JS:** (необязательно)
```js
// добавляем класс .neon-glow к нужным элементам один раз
document.querySelectorAll('.btn-primary,.price-card').forEach(el=>el.classList.add('neon-glow'));
```

## Когда применять
Усиление визуального восприятия CTA и ценовых карточек, повышает чувство эксклюзивности и привлекает внимание к конверсионным элементам.

## Проверка
Открыть страницу, навести курсор на кнопку и карточку – должна появиться мягкая неоновая подсветка без смещения контента; проверить в режиме «prefers-reduced-motion» (должно быть отключено).

## SAFE JS
```js
** (необязательно)
```js
// добавляем класс .neon-glow к нужным элементам один раз
document.querySelectorAll('.btn-primary,.price-card').forEach(el=>el.classList.add('neon-glow'));
```
```
