---
name: SKILL — subtle‑entrance‑fade‑up
source: localhost:8080/ovh/gpt-oss-120b
round: 154
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — subtle‑entrance‑fade‑up

**Name:** `subtle-entrance-fade-up`
**When to apply:** На всех секционных блоках, которые появляются ниже «hero» (например, `.solution`, `.how`, `.works`, `.pricing`, `.faq`, `.final`).
**SAFE CSS:**
```css
.reveal-up {
opacity:0;
transform:translateY(24px);
transition:opacity .6s ease-out, transform .6s ease-out;
}
.reveal-up.visible {
opacity:1;
transform:none;
}
```
**SAFE JS:**
```js
document.addEventListener('DOMContentLoaded',()=>{
const obs = new IntersectionObserver((entries)=>{
entries.forEach(e=> e.isIntersecting && e.target.classList.add('visible'));
},{threshold:0.15});
document.querySelectorAll('.reveal-up').forEach(el=>obs.observe(el));
});
```

## Когда применять
Делает скролл‑появление мягким и «живым», усиливает чувство динамики и удерживает внимание пользователя, что повышает среднее время на странице.

## Проверка
Открыть страницу, прокрутить вниз – блоки должны плавно появляться; открыть DevTools → отключить JS – блоки сразу видимы (проверка fallback).

## SAFE JS
```js
**
```js
document.addEventListener('DOMContentLoaded',()=>{
const obs = new IntersectionObserver((entries)=>{
entries.forEach(e=> e.isIntersecting && e.target.classList.add('visible'));
},{threshold:0.15});
document.querySelectorAll('.reveal-up').forEach(el=>obs.observe(el));
});
```
```
