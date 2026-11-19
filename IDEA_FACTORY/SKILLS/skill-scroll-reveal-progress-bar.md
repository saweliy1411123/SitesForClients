---
name: SKILL — scroll-reveal-progress-bar
source: localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct
round: 125
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — scroll-reveal-progress-bar


**Name:** `scroll-reveal-progress-bar`
**When to apply:** На любом статическом лендинге, где есть секции с информацией.
**Steps:**
1. Добавьте контейнер для прогресс-бара над секцией с информацией.
2. Используйте CSS, чтобы создать анимацию заполнения прогресс-бара при скролле.
SAFE CSS:
```css
.scroll-progress {
position: relative;
height: 5px;
background: #ccc;
border-radius: 5px;
}
.scroll-progress .fill {
position: absolute;
top: 0;
left: 0;
height: 100%;
background: var(--blue);
border-radius: 5px;
width: 0;
transition: width 0.5s ease-out;
}
```
SAFE JS:
```javascript
const progressBars = document.querySelectorAll('.scroll-progress .fill');
window.addEventListener('scroll', () => {
const scrollPosition = window.scrollY;
const maxHeight = document.body.offsetHeight - window.innerHeight;
const scrollFraction = scrollPosition / maxHeight;
progressBars.forEach((bar) => {
bar.style.width = `${scrollFraction * 100}%`;
});
});
```

## Когда применять
Добавление интерактивного прогресс-бара, который заполняется при скролле, повышая вовлеченность пользователя.

## Проверка
Проверить, что прогресс-бар заполняется правильно при скролле.

## SAFE JS
```js
```javascript
const progressBars = document.querySelectorAll('.scroll-progress .fill');
window.addEventListener('scroll', () => {
const scrollPosition = window.scrollY;
const maxHeight = document.body.offsetHeight - window.innerHeight;
const scrollFraction = scrollPosition / maxHeight;
progressBars.forEach((bar) => {
bar.style.width = `${scrollFraction * 100}%`;
});
});
```
```
