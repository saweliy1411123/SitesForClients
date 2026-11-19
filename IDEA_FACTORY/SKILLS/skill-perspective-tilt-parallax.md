---
name: SKILL — perspective-tilt-parallax
source: localhost:8080/ovh/gpt-oss-120b
round: 91
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — perspective-tilt-parallax

**Name:** `perspective-tilt-parallax`
**When to apply:** На секциях с фоновыми иллюстрациями (например, `.hero`, `.final`) чтобы добавить лёгкий 3‑D‑параллакс‑эффект при скролле.
**SAFE CSS:**
```css
/* container with perspective */
.parallax-perspective {
perspective: 800px;
overflow: hidden;
}
.parallax-perspective .parallax-layer {
transform: translateZ(var(--tz, 0));
transition: transform .2s ease-out;
}
```
**SAFE JS:**
```js
// лёгкий скролл‑тильт, без throttling (мало элементов)
document.addEventListener('scroll', () => {
const scrollY = window.scrollY;
document.querySelectorAll('.parallax-perspective .parallax-layer')
.forEach(el => {
const depth = parseFloat(el.dataset.depth) || 0;
const tz = (scrollY * depth) * 0.05;
el.style.setProperty('--tz', `${tz}px`);
});
});
```

## Когда применять
Создаёт ощущение глубины и динамики, усиливая премиальный «тёплый» визуальный стиль без тяжёлых библиотек.

## Проверка
Прокрутить страницу, убедиться, что фоновые слои слегка смещаются в зависимости от скролла; включить/выключить `prefers-reduced-motion` в DevTools – эффект исчезает.

## SAFE JS
```js
**
```js
// лёгкий скролл‑тильт, без throttling (мало элементов)
document.addEventListener('scroll', () => {
const scrollY = window.scrollY;
document.querySelectorAll('.parallax-perspective .parallax-layer')
.forEach(el => {
const depth = parseFloat(el.dataset.depth) || 0;
const tz = (scrollY * depth) * 0.05;
el.style.setProperty('--tz', `${tz}px`);
});
});
```
```
