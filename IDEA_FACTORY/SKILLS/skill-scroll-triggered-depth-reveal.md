---
name: SKILL — scroll-triggered-depth-reveal
source: localhost:8080/ovh/gpt-oss-120b
round: 126
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — scroll-triggered-depth-reveal

**Name:** `scroll-triggered-depth-reveal`
**When to apply:** На блоках, которые появляются ниже первого экрана (например, секции «Три шага», «Демо‑концепты», «FAQ»).
**SAFE CSS:**
```css
/* initial hidden state */
.depth-reveal {
opacity: 0;
transform: translateZ(-40px);
transition: opacity .6s ease-out, transform .6s ease-out;
will-change: opacity, transform;
}
/* when in viewport */
.depth-reveal.in-view {
opacity: 1;
transform: translateZ(0);
}
```
**SAFE JS:**
```js
(() => {
const obs = new IntersectionObserver((entries)=> {
entries.forEach(e=> e.target.classList.toggle('in-view', e.isIntersecting));
}, {threshold: 0.15});
document.querySelectorAll('.depth-reveal').forEach(el=> obs.observe(el));
})();
```

## Когда применять
Элементы «выходят» из глубины при скролле, создавая ощущение 3‑D‑пространства и повышая вовлечённость пользователя.

## Проверка
Прокрутите страницу, элементы с классом `depth-reveal` должны плавно появиться; откройте DevTools → Console, убедитесь в отсутствии ошибок.

## SAFE JS
```js
**
```js
(() => {
const obs = new IntersectionObserver((entries)=> {
entries.forEach(e=> e.target.classList.toggle('in-view', e.isIntersecting));
}, {threshold: 0.15});
document.querySelectorAll('.depth-reveal').forEach(el=> obs.observe(el));
})();
```
```
