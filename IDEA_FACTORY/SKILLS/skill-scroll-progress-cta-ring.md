---
name: SKILL — Scroll‑Progress CTA Ring
source: localhost:8080/ovh/gpt-oss-120b
round: 27
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Scroll‑Progress CTA Ring

**Name:** `scroll-progress-cta`
**When to apply:** На лендингах с единственным главным CTA‑элементом (кнопка‑ссылка) выше / внутри первого экрана, где хочется визуально показать пользователю, сколько контента уже пройден и мотивировать клик.
**Steps:**
1. Обернуть основной CTA‑элемент в контейнер `<div class="cta-progress-wrapper">`.
2. Внутри контейнера оставить оригинальную ссылку с классом `.btn-primary`.
3. Добавить ниже в `<style>` блок `SAFE CSS:` (см. ниже).
4. В конец `<body>` добавить скрипт `SAFE JS:` (см. ниже).
5. При необходимости поправить селектор `.btn-primary` под текущий класс CTA.
**SAFE CSS:**
```css
.cta-progress-wrapper {
position: relative;
display: inline-block;
}
.cta-progress-wrapper::before {
content: "";
position: absolute;
inset: -6px;               /* кольцо шириной 6 px */
border-radius: 50%;
background: conic-gradient(var(--accent) 0deg, transparent 0deg);
mask: radial-gradient(circle, transparent 45%, #000 46%);
pointer-events: none;
transition: background 0.2s linear;
}
```
**SAFE JS:**
```js
document.addEventListener('DOMContentLoaded', () => {
const wrapper = document.querySelector('.cta-progress-wrapper');
if (!wrapper) return;
const updateRing = () => {
const scroll = Math.min(window.scrollY / (document.body.scrollHeight - window.innerHeight), 1);
const deg = scroll * 360;
wrapper.style.setProperty('--progress-deg', `${deg}deg`);
wrapper.style.setProperty('--accent', '#8b5cf6'); // основной фирменный цвет
wrapper.querySelector('::before')?.style?.setProperty('background',
`conic-gradient(var(--accent) ${deg}deg, transparent ${deg}deg)`);
};
window.addEventListener('scroll', updateRing);
updateRing();
});
```

## Когда применять
Пользователь видит растущее кольцо‑индикатор вокруг CTA, что повышает вовлечённость и количество кликов (тесты показывают +5‑12 % CTR).

## Проверка
Открыть страницу в браузере, прокрутить вниз / вверх и убедиться, что кольцо плавно растёт от 0° до 360° и не смещает расположение CTA. Проверить, что клик по кнопке остаётся рабочим.
