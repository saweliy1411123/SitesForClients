---
name: SKILL — scroll‑snap sections with navigation dots
source: localhost:8080/ovh/gpt-oss-120b
round: 34
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — scroll‑snap sections with navigation dots

**Name:** `scroll-snap-nav`
**When to apply:** На одностраничных лендингах с несколькими вертикальными секциями, где нужен плавный переход между блоками и визуальная подсказка текущего положения (особенно на мобильных устройствах).
**Steps:**
1. В `<style>` добавить правила для контейнера `<body>` (или обёртки `<main>`) и секций.
2. Добавить в конец `<body>` блок навигационных точек (`<nav class="snap-nav" aria-label="Навигация по секциям">…</nav>`).
3. При желании подключить лёгкий JS‑скрипт, который будет обновлять активную точку при скролле.
**SAFE CSS:**
```css
/* Enable vertical scroll snapping */
html, body {
height: 100%;
scroll-behavior: smooth;
}
.main-scroll {
scroll-snap-type: y mandatory;
overflow-y: auto;
height: 100vh;
}
/* Each section snaps */
.main-scroll > section {
scroll-snap-align: start;
min-height: 100vh;
}
/* Navigation dots */
.snap-nav {
position: fixed;
right: 1rem;
top: 50%;
transform: translateY(-50%);
display: flex;
flex-direction: column;
gap: 0.75rem;
z-index: 1000;
}
.snap-nav a {
width: 0.75rem;
height: 0.75rem;
background: #c3cad9;
border-radius: 50%;
display: block;
transition: background 0.3s;
}
.snap-nav a.active,
.snap-nav a:hover {
background: #8b5cf6;
}
```
**SAFE JS:** (необязательно, но рекомендуется для подсветки активной точки)
```js
document.addEventListener('DOMContentLoaded', () => {
const sections = document.querySelectorAll('.main-scroll > section');
const navLinks = document.querySelectorAll('.snap-nav a');
const setActive = i => {
navLinks.forEach((lnk, idx) => lnk.classList.toggle('active', idx === i));
};
const observer = new IntersectionObserver(
entries => {
entries.forEach(entry => {
if (entry.isIntersecting) {
const idx = [...sections].indexOf(entry.target);
setActive(idx);
}
});
},
{ root: null, threshold: 0.6 }
);
sections.forEach(sec => observer.observe(sec));
});
```

## Когда применять
Улучшает пользовательский опыт (UX) за счёт предсказуемого скроллинга, повышает вовлечённость и время на странице, упрощает навигацию без дополнительных кликов.

## Проверка
Открыть страницу в мобильном режиме, прокручивать – секции должны «прилипать» к верхней границе; точки навигации меняют цвет в соответствии с текущей секцией. Проверить отсутствие горизонтального скролла.

## SAFE JS
```js
** (необязательно, но рекомендуется для подсветки активной точки)
```js
document.addEventListener('DOMContentLoaded', () => {
const sections = document.querySelectorAll('.main-scroll > section');
const navLinks = document.querySelectorAll('.snap-nav a');
const setActive = i => {
navLinks.forEach((lnk, idx) => lnk.classList.toggle('active', idx === i));
};
const observer = new IntersectionObserver(
entries => {
entries.forEach(entry => {
if (entry.isIntersecting) {
const idx = [...sections].indexOf(entry.target);
setActive(idx);
}
});
},
{ root: null, threshold: 0.6 }
);
sections.forEach(sec => observer.observe(sec));
});
```
```
