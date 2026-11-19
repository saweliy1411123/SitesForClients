---
name: SKILL — fade‑in‑on‑scroll
source: localhost:8080/ovh/gpt-oss-120b
round: 83
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — fade‑in‑on‑scroll

**Name:** `fade-in-on-scroll`
**When to apply:** На любой одностраничной посадочной странице, где есть секции/элементы, которые появляются ниже «скрола» (например, `.hero`, `.steps`, `.price-card`, `.final`). Позволяет добавить лёгкую анимацию появления, улучшая восприятие динамичности без JavaScript‑библиотек.
**Steps:**
1. Добавить файл‑skill `fade-in-on-scroll.css` и `fade-in-on-scroll.js` в `<head>` (CSS) и перед закрывающим `</body>` (JS).
2. На нужных элементах добавить класс `.fade-in`.
3. JS автоматически будет наблюдать за элементами и добавлять класс `.visible` при их появлении в viewport.
**SAFE CSS:**
```css
/* fade-in-on-scroll.css */
.fade-in {
opacity: 0;
transform: translateY(20px);
transition: opacity .6s ease-out, transform .6s ease-out;
}
.fade-in.visible {
opacity: 1;
transform: translateY(0);
}
```
**SAFE JS:**
```js
/* fade-in-on-scroll.js */
document.addEventListener('DOMContentLoaded', () => {
const observer = new IntersectionObserver((entries) => {
entries.forEach(entry => {
if (entry.isIntersecting) entry.target.classList.add('visible');
});
}, {threshold: 0.1});
document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
});
```

## Когда применять
Элементы плавно «въезжают» в поле зрения, создавая ощущение живой страницы, что удерживает внимание и повышает время на сайте.

## Проверка
Открыть страницу, прокрутить вниз; элементы с классом `.fade-in` должны плавно появиться. В консоли нет ошибок. В старом браузере (например, режим «Internet Explorer 11» в Edge) контент отображается без анимации.

## SAFE JS
```js
**
```js
/* fade-in-on-scroll.js */
document.addEventListener('DOMContentLoaded', () => {
const observer = new IntersectionObserver((entries) => {
entries.forEach(entry => {
if (entry.isIntersecting) entry.target.classList.add('visible');
});
}, {threshold: 0.1});
document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
});
```
```
