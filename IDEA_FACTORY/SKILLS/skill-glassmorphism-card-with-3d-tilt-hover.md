---
name: SKILL — Glassmorphism Card with 3D Tilt Hover
source: localhost:8080/ovh/gpt-oss-120b
round: 7
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Glassmorphism Card with 3D Tilt Hover

METHOD: Create reusable skill **glass-tilt-card**
```markdown
# glass-tilt-card.md
## Название
Glassmorphism Card with 3D Tilt Hover
## Когда применять
Для визуально‑привлекательных блоков‑карточек (услуги, отзывы, демо‑концепты) на премиальном лендинге, где нужен лёгкий 3D‑эффект и «стеклянный» фон без тяжёлых библиотек.
## Шаги
1. Добавьте в HTML любой контейнер с классом `glass-card` и вложенный контент.
2. Подключите файл `glass-tilt-card.css` в `<head>`.
3. (Опционально) подключите `glass-tilt-card.js` в конце `<body>` для интерактивного наклона по курсору.
4. При необходимости переопределите переменные `--card-bg`, `--card-blur`, `--card-radius`.
## SAFE CSS:
```css
/* glass-tilt-card.css */
.glass-card {
position: relative;
padding: 1.5rem;
border-radius: var(--card-radius, 12px);
background: var(--card-bg, rgba(255,255,255,0.12));
backdrop-filter: blur(var(--card-blur, 8px));
box-shadow: 0 8px 32px rgba(0,0,0,0.12);
transition: transform 0.3s ease, box-shadow 0.3s ease;
transform-style: preserve-3d;
perspective: 800px;
}
.glass-card::before {
content: "";
position: absolute;
inset: 0;
border-radius: inherit;
background: linear-gradient(135deg, rgba(255,255,255,0.25), rgba(255,255,255,0));
pointer-events: none;
}
.glass-card:hover {
transform: rotateX(4deg) rotateY(6deg) scale(1.02);
box-shadow: 0 12px 48px rgba(0,0,0,0.2);
}
@media (prefers-reduced-motion: reduce) {
.glass-card,
.glass-card:hover {
transition: none;
transform: none;
}
}
```
## SAFE JS:
```js
/* glass-tilt-card.js */
document.querySelectorAll('.glass-card').forEach(card => {
const rect = () => card.getBoundingClientRect();
const update = e => {
const {width, height, left, top} = rect();
const x = ((e.clientX - left) / width - 0.5) * 12;   // ±6deg
const y = ((e.clientY - top) / height - 0.5) * -12; // ±6deg
card.style.transform = `rotateX(${y}deg) rotateY(${x}deg) scale(1.02)`;
};
const reset = () => {
card.style.transform = '';
};
card.addEventListener('mousemove', update);
card.addEventListener('mouseleave', reset);
});
```
```

## Когда применять
Делает карточки визуально «премиальными», повышает время на странице и воспринимаемую ценность, стимулирует клик за счёт интерактивного отклика.

## Проверка
Откройте страницу в браузере, наведите курсор на элемент с классом `glass-card` — должен появиться лёгкий наклон и блеск; включите `prefers-reduced-motion` в системе — анимация должна исчезнуть.

## SAFE JS
```js
```js
/* glass-tilt-card.js */
document.querySelectorAll('.glass-card').forEach(card => {
const rect = () => card.getBoundingClientRect();
const update = e => {
const {width, height, left, top} = rect();
const x = ((e.clientX - left) / width - 0.5) * 12;   // ±6deg
const y = ((e.clientY - top) / height - 0.5) * -12; // ±6deg
card.style.transform = `rotateX(${y}deg) rotateY(${x}deg) scale(1.02)`;
};
const reset = () => {
card.style.transform = '';
};
card.addEventListener('mousemove', update);
card.addEventListener('mouseleave', reset);
});
```
```
```
