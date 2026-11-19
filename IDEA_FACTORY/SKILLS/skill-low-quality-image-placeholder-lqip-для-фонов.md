---
name: SKILL — Low‑Quality Image Placeholder (LQIP) для фоновых изображений
source: localhost:8080/ovh/gpt-oss-120b
round: 62
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Low‑Quality Image Placeholder (LQIP) для фоновых изображений

METHOD:
**Name:** lqip-bg-image
**When to apply:** На секциях с крупными фоновыми изображениями (hero, демо‑карточки), где важна первая визуальная реакция.
**Steps:**
1. Сгенерировать небольшую (≈10 × 10 px) версию фонового изображения, закодировать её в base64.
2. В HTML заменить `style="background-image:url('hero.jpg')"` на атрибут `data-bg="hero.jpg"` и добавить класс `bg-lqip`.
3. Добавить в CSS псевдо‑элемент `::before`, который будет показывать base64‑placeholder с `filter: blur(12px)` и `scale(1.05)`.
4. Добавить небольшой скрипт, который создаёт `Image()`, загружает оригинал из `data-bg` и после `load` заменяет `background-image` у элемента, убирая `::before`.
SAFE CSS:
```css
.bg-lqip{
position:relative;
overflow:hidden;
}
.bg-lqip::before{
content:"";
position:absolute;
inset:0;
background-image:url("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD…"); /* tiny placeholder */
background-size:cover;
background-position:center;
filter:blur(12px);
transform:scale(1.05);
transition:opacity .3s ease;
}
.bg-lqip.loaded::before{opacity:0;pointer-events:none;}
```
SAFE JS:
```js
document.querySelectorAll('.bg-lqip').forEach(el=>{
const img = new Image();
img.src = el.dataset.bg;
img.onload = ()=>{
el.style.backgroundImage = `url(${el.dataset.bg})`;
el.classList.add('loaded');
};
});
```

## Когда применять
Пользователь видит быстро загружающийся размазанный плейсхолдер, затем плавно появляется чёткое изображение → улучшение FCP/CLS, повышается восприятие скорости.

## Проверка
Включить DevTools → Network → Throttle → Slow 3G, открыть страницу и убедиться, что сначала появляется размытый placeholder, затем заменяется на оригинал без «мигания»; измерить FCP (должен снизиться).

## SAFE JS
```js
```js
document.querySelectorAll('.bg-lqip').forEach(el=>{
const img = new Image();
img.src = el.dataset.bg;
img.onload = ()=>{
el.style.backgroundImage = `url(${el.dataset.bg})`;
el.classList.add('loaded');
};
});
```
```
