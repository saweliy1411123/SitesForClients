---
name: SKILL — glassmorphic‑sticky‑header
source: localhost:8080/ovh/gpt-oss-120b
round: 140
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — glassmorphic‑sticky‑header

**Name:** `glassmorphic-sticky-header`
**When to apply:** На любой одностраничный лендинг, где в шапке находятся ссылки‑якоря и нужен премиальный, «прозрачный» вид без потери читаемости.
**Steps:**
1. Вставить сразу после `<body>` элемент `<nav class="glass-header" aria-label="Главное меню">…</nav>` (скопировать существующий блок навигации).
2. Добавить CSS‑правила (см. ниже) для фиксированного позиционирования, backdrop‑filter и плавного перехода opacity.
3. Добавить небольшой скрипт, который при скролле > 50 px добавляет/убирает класс `scrolled`.
**SAFE CSS:**
```css
.glass-header{
position:fixed;
inset-inline:0;
top:0;
height:64px;
display:flex;
align-items:center;
justify-content:center;
backdrop-filter:blur(12px);
background:rgba(255,255,255,0.12);
border-bottom:1px solid rgba(255,255,255,0.15);
transition:background .3s ease, border-color .3s ease;
z-index:1000;
}
.glass-header.scrolled{
background:rgba(255,255,255,0.24);
border-color:rgba(255,255,255,0.25);
}
.glass-header a{
color:var(--text);
margin:0 12px;
font-weight:500;
}
.glass-header a:focus-visible{
outline:3px solid var(--blue);
outline-offset:2px;
}
```
**SAFE JS:**
```js
document.addEventListener('scroll',()=>{
const hdr=document.querySelector('.glass-header');
if(window.scrollY>50) hdr.classList.add('scrolled');
else hdr.classList.remove('scrolled');
});
```

## Когда применять
Делает шапку визуально «премиальной», сохраняет её доступной на всех скроллах, повышает восприятие бренда и удерживает навигацию в поле зрения.

## Проверка
Открыть страницу, прокрутить > 50 px — шапка должна плавно поменять фон и стать чуть более непрозрачной; проверить, что ссылки остаются кликабельными.
