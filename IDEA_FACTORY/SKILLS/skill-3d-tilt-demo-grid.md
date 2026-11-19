---
name: SKILL — 3d-tilt-demo-grid
source: localhost:8080/ovh/gpt-oss-120b
round: 105
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — 3d-tilt-demo-grid

**Name:** `3d-tilt-demo-grid`
**When to apply:** На секции с демонстрационными концепт‑карточками (примерно L589) для создания глубины и интерактивности без JS.
**SAFE CSS:**
```css
/* 3d-tilt-demo-grid */
.demo-grid {
display: flex;
flex-wrap: wrap;
gap: 1.5rem;
perspective: 800px;
}
.demo-grid .card {
background: rgba(255,255,255,0.08);
border-radius: 12px;
padding: 1.2rem;
flex: 1 1 calc(33.333% - 1rem);
transform-style: preserve-3d;
transition: transform 0.35s ease, box-shadow 0.35s ease;
box-shadow: 0 8px 24px rgba(0,0,0,0.12);
}
.demo-grid .card:hover,
.demo-grid .card:focus-visible {
transform: rotateX(4deg) rotateY(-6deg) translateZ(12px);
box-shadow: 0 20px 48px rgba(0,0,0,0.18);
}
.demo-grid .card h3 {
margin-top:0;
}
```
**SAFE JS:** (не требуется)

## Когда применять
Добавляет премиальный 3‑D‑эффект при наведении, повышает вовлечённость и делает демонстрацию более запоминающейся.

## Проверка
Открыть страницу в десктоп‑браузере, навести курсор на любую карточку – она должна слегка наклониться и подняться; проверить плавность перехода в DevTools → Performance → FPS.

## SAFE JS
```js
** (не требуется)
```
