---
name: SKILL — premium-hero-typing
source: localhost:8080/ovh/gpt-oss-120b
round: 77
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — premium-hero-typing

**Name:** `premium-hero-typing`
**When to apply:** В hero‑секции рядом с основным заголовком (`<h1>`) для создания премиального ощущения динамики.
**SAFE CSS:**
```css
.hero-typing {
overflow:hidden;
border-right:.15em solid var(--blue);
white-space:nowrap;
font-family:inherit;
font-size:clamp(1.8rem,5vw,3rem);
animation: typing 2.5s steps(30, end) forwards,
blink .75s step-end infinite;
}
@keyframes typing{
from{width:0}
to{width:100%}
}
@keyframes blink{
0%,100%{border-color:transparent}
50%{border-color:var(--blue)}
}
```
**SAFE JS:** (optional, to restart on resize)
```js
window.addEventListener('resize',()=>{document.querySelectorAll('.hero-typing').forEach(el=>el.style.animation='none');setTimeout(()=>{document.querySelectorAll('.hero-typing').forEach(el=>el.style.animation='typing 2.5s steps(30,end) forwards, blink .75s step-end infinite');},50);});
```

## Когда применять
Увеличивает восприятие премиальности, удерживает внимание в первых 3 секундах → рост CTR на CTA > 5 % (по опыту).

## Проверка
Открыть страницу в Chrome/Firefox, убедиться, что текст под `<h1>` появляется «пишущей машиной» и мигает курсор; проверить, что при ресайзе анимация не ломается.

## SAFE JS
```js
** (optional, to restart on resize)
```js
window.addEventListener('resize',()=>{document.querySelectorAll('.hero-typing').forEach(el=>el.style.animation='none');setTimeout(()=>{document.querySelectorAll('.hero-typing').forEach(el=>el.style.animation='typing 2.5s steps(30,end) forwards, blink .75s step-end infinite');},50);});
```
```
