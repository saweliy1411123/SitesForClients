---
name: SKILL — scroll-progress-bar
source: localhost:8080/ovh/gpt-oss-120b
round: 76
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — scroll-progress-bar

**Name:** `scroll-progress-bar`
**When to apply:** На одностраничных лендингах, где пользователь прокручивает контент от начала до конца; индикатор прогресса повышает ориентацию и мотивирует дочитывать страницу.
**Steps:**
1. В начале `<body>` добавить пустой элемент‑контейнер:
```html
<div class="scroll-progress" aria-hidden="true"></div>
```
2. В CSS задать фиксированную высоту, ширину 0 % и стили оформления.
3. В безопасном JS‑скрипте отследить событие `scroll`, вычислить процент прокрутки (`(scrollY / (document.body.scrollHeight - innerHeight)) * 100`) и установить `style.width` у `.scroll-progress`.
**SAFE CSS:**
```css
.scroll-progress{
position:fixed;
top:0; left:0;
height:4px;
width:0%;
background:linear-gradient(90deg,var(--c-primary),#a78bfa);
z-index:9999;
transition:width .1s ease-out;
}
```
**SAFE JS:**
```js
(() => {
const bar = document.querySelector('.scroll-progress');
const update = () => {
const scroll = window.scrollY;
const height = document.body.scrollHeight - innerHeight;
const perc = height ? (scroll / height) * 100 : 0;
bar.style.width = perc + '%';
};
window.addEventListener('scroll', update);
window.addEventListener('resize', update);
update();
})();
```

## Когда применять
Пользователь видит визуальный индикатор, сколько контента осталось, что повышает вовлечённость и может улучшить конверсию (меньше «потери» на середине страницы).

## Проверка
Прокрутить страницу – индикатор должен плавно заполняться от 0 % до 100 %; проверить, что он остаётся вверху при скролле и не перекрывает важные элементы.

## SAFE JS
```js
**
```js
(() => {
const bar = document.querySelector('.scroll-progress');
const update = () => {
const scroll = window.scrollY;
const height = document.body.scrollHeight - innerHeight;
const perc = height ? (scroll / height) * 100 : 0;
bar.style.width = perc + '%';
};
window.addEventListener('scroll', update);
window.addEventListener('resize', update);
update();
})();
```
```
