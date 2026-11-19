---
name: SKILL — Counter‑Up Animate
source: localhost:8080/ovh/gpt-oss-120b
round: 160
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Counter‑Up Animate

**Name:** `counter-up-animate`
**When to apply:** На любой статический лендинг, где есть цифры‑статистики (например, «100+ проектов», «+30 % рост»), которые должны привлечь внимание при появлении в зоне видимости.
**Steps:**
1. В HTML‑разметке обернуть каждое число в элемент `<span class="counter" data-target="1234">0</span>`.
2. Добавить файл `skills/counter-up-animate.css` и подключить его в `<head>` (или инлайн‑вставить в `index.improved.html`).
3. Добавить файл `skills/counter-up-animate.js` и подключить его в конце `<body>` (defer).
4. Скрипт создаёт `IntersectionObserver`, который при вхождении элемента в viewport запускает анимацию плавного увеличения от 0 до `data-target` за 1.5 с.
**SAFE CSS:**
```css
.counter {
display: inline-block;
font-variant-numeric: tabular-nums;
font-weight: 600;
color: var(--blue);
transition: color .3s;
}
.counter[data-target]::after {
content: '+';
margin-left: .1em;
opacity: .6;
}
```
**SAFE JS:**
```js
document.addEventListener('DOMContentLoaded', () => {
const counters = document.querySelectorAll('.counter[data-target]');
const options = {threshold: 0.6};
const animate = el => {
const target = +el.dataset.target;
const duration = 1500;
const start = performance.now();
const step = now => {
const elapsed = now - start;
const progress = Math.min(elapsed / duration, 1);
el.textContent = Math.floor(progress * target);
if (progress < 1) requestAnimationFrame(step);
};
requestAnimationFrame(step);
};
const observer = new IntersectionObserver((entries, obs) => {
entries.forEach(entry => {
if (entry.isIntersecting) {
animate(entry.target);
obs.unobserve(entry.target);
}
});
}, options);
counters.forEach(c => observer.observe(c));
});
```

## Когда применять


## Проверка
Открыть страницу в браузере, прокрутить до блока со счётчиком, убедиться, что число плавно растёт от 0 до указанного значения; в консоли проверить отсутствие ошибок.

## SAFE JS
```js
**
```js
document.addEventListener('DOMContentLoaded', () => {
const counters = document.querySelectorAll('.counter[data-target]');
const options = {threshold: 0.6};
const animate = el => {
const target = +el.dataset.target;
const duration = 1500;
const start = performance.now();
const step = now => {
const elapsed = now - start;
const progress = Math.min(elapsed / duration, 1);
el.textContent = Math.floor(progress * target);
if (progress < 1) requestAnimationFrame(step);
};
requestAnimationFrame(step);
};
const observer = new IntersectionObserver((entries, obs) => {
entries.forEach(entry => {
if (entry.isIntersecting) {
animate(entry.target);
obs.unobserve(entry.target);
}
});
}, options);
counters.forEach(c => observer.observe(c));
});
```
```
