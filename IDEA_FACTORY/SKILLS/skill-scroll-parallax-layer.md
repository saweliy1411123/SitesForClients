---
name: SKILL — scroll‑parallax‑layer
source: localhost:8080/ovh/gpt-oss-120b
round: 147
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — scroll‑parallax‑layer

SKILL: **Name:** `scroll-parallax-layer`
**When to apply:** К декоративным элементам в секции hero (blobs, фоновые SVG) и к любым фоновым блокам, где нужен лёгкий параллакс при прокрутке.
**Steps:** 1️⃣ Добавить атрибут `data-speed="0.3"` (значение 0–1) к каждому элементу. 2️⃣ Добавить класс `parallax-layer`. 3️⃣ Включить CSS и небольшой JS‑скрипт ниже.
SAFE CSS:
```css
.parallax-layer{
will-change:transform;
}
```
SAFE JS:
```js
document.addEventListener('scroll',()=>{
const y = window.scrollY;
document.querySelectorAll('.parallax-layer').forEach(el=>{
const s = parseFloat(el.dataset.speed)||0.5;
el.style.transform=`translateY(${y*s}px)`;
});
});
```

## Когда применять
Создаёт ощущение глубины и динамики без тяжёлых библиотек, усиливая премиальный «живой» образ сайта.

## Проверка
Прокрутить страницу; декоративные элементы должны медленно смещаться относительно скролла; проверить плавность в Chrome DevTools → Performance.

## SAFE CSS
```css
```css
.parallax-layer{
will-change:transform;
}
```
```

## SAFE JS
```js
```js
document.addEventListener('scroll',()=>{
const y = window.scrollY;
document.querySelectorAll('.parallax-layer').forEach(el=>{
const s = parseFloat(el.dataset.speed)||0.5;
el.style.transform=`translateY(${y*s}px)`;
});
});
```
```
