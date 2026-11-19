---
name: SKILL — 3d‑tilt‑price‑card
source: localhost:8080/ovh/gpt-oss-120b
round: 98
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — 3d‑tilt‑price‑card

**NAME:** 3d-tilt-price-card
**WHEN TO APPLY:** На карточках цены (`.price-card`) в секции «Цена», где нужен интерактивный премиальный эффект при наведении/касании.
**STEPS:**
1. Добавить к каждому `.price-card` класс `tilt‑card`.
2. В CSS задать `perspective` и базовый `transform`.
3. Добавить лёгкий JS‑слушатель `pointermove` для расчёта угла наклона (max 10°).
**SAFE CSS:**
```css
.tilt-card {
perspective: 600px;
transition: transform 0.3s ease;
}
.tilt-card:hover,
.tilt-card:focus-visible {
transform: rotateX(5deg) rotateY(5deg);
}
```
**SAFE JS:**
```js
document.querySelectorAll('.price-card.tilt-card').forEach(card=>{
card.addEventListener('pointermove',e=>{
const rect = card.getBoundingClientRect();
const x = (e.clientX - rect.left) / rect.width - 0.5;
const y = (e.clientY - rect.top) / rect.height - 0.5;
const rotX = y * 10; // max 10°
const rotY = -x * 10;
card.style.transform = `perspective(600px) rotateX(${rotX}deg) rotateY(${rotY}deg)`;
});
card.addEventListener('pointerleave',()=>{ card.style.transform=''; });
});
```

## Когда применять
Делает цену более «осязаемой», повышает вовлечённость и воспринимается как современный премиум‑дизайн → рост кликов по кнопке «Получить демо».

## Проверка
Навести курсор на карточку цены, увидеть плавный наклон; проверить на мобильных (должен быть без наклона).

## SAFE JS
```js
**
```js
document.querySelectorAll('.price-card.tilt-card').forEach(card=>{
card.addEventListener('pointermove',e=>{
const rect = card.getBoundingClientRect();
const x = (e.clientX - rect.left) / rect.width - 0.5;
const y = (e.clientY - rect.top) / rect.height - 0.5;
const rotX = y * 10; // max 10°
const rotY = -x * 10;
card.style.transform = `perspective(600px) rotateX(${rotX}deg) rotateY(${rotY}deg)`;
});
card.addEventListener('pointerleave',()=>{ card.style.transform=''; });
});
```
```
