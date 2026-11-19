---
name: SKILL — Testimonial Carousel (Vanilla)
source: localhost:8080/ovh/gpt-oss-120b
round: 160
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Testimonial Carousel (Vanilla)

**Name:** `testimonial-carousel`
**When to apply:** На лендингах, где есть раздел отзывов/кейсов (в текущем сайте – секция «Отзывы и работы»), но без готовой карусели. Позволяет показать несколько отзывов в компактном виде, улучшая доверие и удерживая внимание.
**Steps:**
1. В HTML‑разметке заменить список отзывов на контейнер `<div class="testimonial-carousel" role="region" aria-label="Отзывы клиентов">` и вложить отдельные `<article class="testimonial">`‑элементы.
2. Добавить файл `skills/testimonial-carousel.css` и подключить его.
3. Добавить файл `skills/testimonial-carousel.js` (defer) – простой автопрокручивающий скрипт с поддержкой клавиатурной навигации (arrow‑keys) и `aria-live` для объявлений.
**SAFE CSS:**
```css
.testimonial-carousel {
position: relative;
overflow: hidden;
max-width: 720px;
margin: 0 auto;
}
.testimonial {
min-width: 100%;
box-sizing: border-box;
padding: 1.5rem;
opacity: 0;
transition: opacity .4s ease;
}
.testimonial.active {
opacity: 1;
}
.testimonial::before {
content: "“";
font-size: 3rem;
line-height: 0;
color: var(--muted);
position: absolute;
left: 1rem;
top: .5rem;
}
.carousel-nav {
position: absolute;
inset: 0;
display: flex;
justify-content: space-between;
align-items: center;
pointer-events: none;
}
.carousel-nav button {
pointer-events: all;
background: var(--bg);
border: none;
border-radius: 50%;
width: 2.4rem;
height: 2.4rem;
font-size: 1.2rem;
color: var(--blue);
cursor: pointer;
transition: background .2s;
}
.carousel-nav button:hover { background: var(--muted); }
```
**SAFE JS:**
```js
document.addEventListener('DOMContentLoaded', () => {
const carousel = document.querySelector('.testimonial-carousel');
if (!carousel) return;
const items = carousel.querySelectorAll('.testimonial');
let idx = 0;
const show = i => {
items.forEach((el, n) => el.classList.toggle('active', n === i));
carousel.setAttribute('aria-live', 'polite');
};
const next = () => { idx = (idx + 1) % items.length; show(idx); };
const prev = () => { idx = (idx - 1 + items.length) % items.length; show(idx); };
// initial
show(idx);
// auto‑rotate
const auto = setInterval(next, 8000);
// navigation
const nav = document.createElement('div');
nav.className = 'carousel-nav';
nav.innerHTML = `<button aria-label="Предыдущий отзыв" class="prev">&larr;</button>
<button aria-label="Следующий отзыв" class="next">&rarr;</button>`;
carousel.appendChild(nav);
nav.querySelector('.next').addEventListener('click', () => { clearInterval(auto); next(); });
nav.querySelector('.prev').addEventListener('click', () => { clearInterval(auto); prev(); });
// keyboard
document.addEventListener('keydown', e => {
if (e.key === 'ArrowRight') { clearInterval(auto); next(); }
if (e.key === 'ArrowLeft')  { clearInterval(auto); prev(); }
});
});
```

## Когда применять


## Проверка
Открыть страницу, убедиться, что один отзыв виден, остальные скрыты; нажать стрелки и клавиши ←/→ – переключение работает; проверить, что в мобильном режиме отзывы адаптивно масштабируются.
