---
name: SKILL — scroll‑triggered‑counter
source: localhost:8080/ovh/gpt-oss-120b
round: 97
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — scroll‑triggered‑counter

**Name:** `scroll-triggered-counter`
**When to apply:** На лендингах, где в секциях (например, «Боль», «Доказательства», «Отзывов») присутствуют статистические цифры, которые должны «оживить» пользователя при прокрутке.
**Steps:**
1. Обернуть каждое число в элемент с классом `counter` и атрибутом `data-target` — целевое значение (например, `<span class="counter" data-target="124">0</span>`).
2. Вставить ниже CSS‑правило из `SAFE CSS` в глобальный стиль.
3. Добавить JavaScript‑блок из `SAFE JS` в конец `<body>` (или в отдельный файл). Скрипт использует `IntersectionObserver` и анимирует счётчик от 0 до `data-target` за 1.5 сек.
**SAFE CSS:**
```css
/* scroll‑triggered‑counter */
.counter {
font-weight: 700;
font-size: clamp(30px,4vw,46px);
line-height: 1.05;
display: inline-block;
}
```
**SAFE JS:**
```js
// scroll‑triggered‑counter
(() => {
const formatNumber = n => Math.floor(n).toLocaleString('ru-RU');
const animate = (el, target) => {
const duration = 1500;
const start = performance.now();
const step = now => {
const elapsed = now - start;
const progress = Math.min(elapsed / duration, 1);
el.textContent = formatNumber(progress * target);
if (progress < 1) requestAnimationFrame(step);
};
requestAnimationFrame(step);
};
const observer = new IntersectionObserver((entries, obs) => {
entries.forEach(entry => {
if (entry.isIntersecting) {
const el = entry.target;
const target = +el.dataset.target;
animate(el, target);
obs.unobserve(el);
}
});
}, {threshold: 0.6});
document.querySelectorAll('.counter[data-target]').forEach(el => observer.observe(el));
})();
```

## Когда применять


## Проверка

1. Открыть страницу в браузере, убедиться, что заголовок с классом `gradient-text` отображает плавный градиент и анимацию (можно временно отключить через DevTools → `animation: none`).
2. Прокрутить до элемента с классом `counter`; убедиться, что цифра плавно считает от 0 до целевого значения и останавливается.

## SAFE JS
```js
**
```js
// scroll‑triggered‑counter
(() => {
const formatNumber = n => Math.floor(n).toLocaleString('ru-RU');
const animate = (el, target) => {
const duration = 1500;
const start = performance.now();
const step = now => {
const elapsed = now - start;
const progress = Math.min(elapsed / duration, 1);
el.textContent = formatNumber(progress * target);
if (progress < 1) requestAnimationFrame(step);
};
requestAnimationFrame(step);
};
const observer = new IntersectionObserver((entries, obs) => {
entries.forEach(entry => {
if (entry.isIntersecting) {
const el = entry.target;
const target = +el.dataset.target;
animate(el, target);
obs.unobserve(el);
}
});
}, {threshold: 0.6});
document.querySelectorAll('.counter[data-target]').forEach(el => observer.observe(el));
})();
```
```
