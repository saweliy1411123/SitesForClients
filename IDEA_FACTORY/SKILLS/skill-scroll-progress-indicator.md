---
name: SKILL — scroll-progress-indicator
source: localhost:8080/ovh/gpt-oss-120b
round: 125
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — scroll-progress-indicator

**Name:** `scroll-progress-indicator`
**When to apply:** На любой одностраничной статической посадочной странице, где важно визуально подсказать пользователю, сколько контента осталось, повысить вовлечённость и удержание.
**Steps:**
1. В начало `<body>` добавить элемент `<div class="scroll-progress"></div>`.
2. В CSS‑файл (или в `<style>`) вставить правила из `SAFE CSS` ниже.
3. В конец `<body>` добавить скрипт из `SAFE JS` ниже (можно разместить в отдельном файле `scroll-progress.js`).
4. Проверить, что переменная `--grad` уже объявлена (используется в проекте). При её отсутствии добавить `--grad: #8b5cf6;`.
**SAFE CSS:**
```css
.scroll-progress{
position:fixed;
top:0;
left:0;
height:4px;
width:0;
background:var(--grad);
z-index:9999;
transition:width .1s linear;
}
```
**SAFE JS:**
```js
(() => {
const bar = document.querySelector('.scroll-progress');
if (!bar) return;
const doc = document.documentElement;
const set = () => {
const scroll = doc.scrollTop || document.body.scrollTop;
const height = doc.scrollHeight - doc.clientHeight;
const perc = (scroll / height) * 100;
bar.style.width = perc + '%';
};
let ticking = false;
window.addEventListener('scroll', () => {
if (!ticking) {
window.requestAnimationFrame(() => {
set();
ticking = false;
});
ticking = true;
}
});
set(); // init on load
})();
```

## Когда применять
Пользователь сразу видит прогресс чтения, что повышает восприятие «продуманного» сайта и может увеличить время на странице → рост конверсии на CTA.

## Проверка
Открыть страницу в браузере, прокрутить вниз – индикатор должен плавно заполняться от 0 % до 100 %; проверить отсутствие ошибок в консоли.

## SAFE JS
```js
**
```js
(() => {
const bar = document.querySelector('.scroll-progress');
if (!bar) return;
const doc = document.documentElement;
const set = () => {
const scroll = doc.scrollTop || document.body.scrollTop;
const height = doc.scrollHeight - doc.clientHeight;
const perc = (scroll / height) * 100;
bar.style.width = perc + '%';
};
let ticking = false;
window.addEventListener('scroll', () => {
if (!ticking) {
window.requestAnimationFrame(() => {
set();
ticking = false;
});
ticking = true;
}
});
set(); // init on load
})();
```
```
