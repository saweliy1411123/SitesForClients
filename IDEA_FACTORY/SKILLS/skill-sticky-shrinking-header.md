---
name: SKILL — Sticky Shrinking Header
source: localhost:8080/ovh/gpt-oss-120b
round: 14
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Sticky Shrinking Header

METHOD: Добавьте класс `.sticky-header` к `<header>` и скрипт, который при прокрутке более 80 px добавляет `shrink`‑модификатор, уменьшая высоту и размер логотипа.
SAFE CSS:
```css
.sticky-header {
position: sticky;
top: 0;
background: var(--bg);
transition: all .3s ease;
z-index: 1000;
}
.sticky-header.shrink {
padding: .5rem 1rem;
}
.sticky-header.shrink .logo {
height: 32px;
}
.logo { height: 48px; transition: height .3s ease; }
```
SAFE JS:
```js
window.addEventListener('scroll', () => {
const hdr = document.querySelector('.sticky-header');
if (!hdr) return;
hdr.classList.toggle('shrink', window.scrollY > 80);
});
```

## Когда применять
Постоянно видимый CTA‑header, экономит экранное пространство при чтении, усиливает восприятие профессионального дизайна.

## Проверка
Прокрутить страницу, убедиться, что header уменьшился после 80 px, и вернулся при возврате наверх.

## SAFE JS
```js
```js
window.addEventListener('scroll', () => {
const hdr = document.querySelector('.sticky-header');
if (!hdr) return;
hdr.classList.toggle('shrink', window.scrollY > 80);
});
```
```
