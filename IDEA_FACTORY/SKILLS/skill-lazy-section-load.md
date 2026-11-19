---
name: SKILL — lazy-section-load
source: localhost:8080/ovh/gpt-oss-120b
round: 166
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — lazy-section-load

**Name:** lazy-section-load
**When to apply:** На статических лендингах с несколькими ниже‑заглавными секциями (hero, problem, steps, faq, price, final)
**SAFE CSS:**
```css
section {opacity:0;transform:translateY(20px);transition:opacity .4s ease,transform .4s ease}
section.in-view {opacity:1;transform:none}
```
**SAFE JS:**
```js
document.querySelectorAll('section').forEach(s=>{
const obs=new IntersectionObserver((e,o)=>{e.forEach(i=>{if(i.isIntersecting){i.target.classList.add('in-view');o.unobserve(i.target)}})},{threshold:.1});
obs.observe(s);
});
```

## Когда применять
Отложенная отрисовка секций до момента, когда они попадают в viewport, уменьшает количество DOM‑элементов, рендерящихся сразу → сокращает время первой отрисовки и экономит ресурсы на мобильных устройствах

## Проверка
Открыть страницу в мобильном режиме, открыть DevTools → Network → убедиться, что только первая секция загружается сразу; прокрутить вниз и наблюдать плавное появление секций (можно включить `console.log` в скрипте)

## SAFE CSS
```css
**
```css
section {opacity:0;transform:translateY(20px);transition:opacity .4s ease,transform .4s ease}
section.in-view {opacity:1;transform:none}
```
**SAFE JS:**
```js
document.querySelectorAll('section').forEach(s=>{
const obs=new IntersectionObserver((e,o)=>{e.forEach(i=>{if(i.isIntersecting){i.target.classList.add('in-view');o.unobserve(i.target)}})},{threshold:.1});
obs.observe(s);
});
```
```

## SAFE JS
```js
**
```js
document.querySelectorAll('section').forEach(s=>{
const obs=new IntersectionObserver((e,o)=>{e.forEach(i=>{if(i.isIntersecting){i.target.classList.add('in-view');o.unobserve(i.target)}})},{threshold:.1});
obs.observe(s);
});
```
```
