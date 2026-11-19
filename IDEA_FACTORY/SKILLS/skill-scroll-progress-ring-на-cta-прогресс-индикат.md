---
name: SKILL — Scroll Progress Ring на CTA (прогресс-индикатор дочитывания вокруг кнопки)
source: lareper/glm-5.2-fast-preview
round: 13
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Scroll Progress Ring на CTA (прогресс-индикатор дочитывания вокруг кнопки)

Название: **scroll-progress-cta**. Когда применять: любой статический лендинг с одним якорным CTA (#contact) и длинной прокруткой — повышает мотивацию дочитать и кликнуть, показывает «вы у цели». Шаги: (1) добавить в CSS кольцевой индикатор через conic-gradient, привязанный к переменной --sp; (2) добавить крошечный JS, который на scroll обновляет --sp на <html>; (3) повесить класс .progress-ring на главную CTA-кнопку (например, .btn-primary в hero и final). Не трогает контент и вёрстку, только визуальный слой.
SAFE CSS:
```css
.progress-ring{position:relative;isolation:isolate}
.progress-ring::before{content:"";position:absolute;inset:-4px;border-radius:inherit;padding:2px;
background:conic-gradient(var(--grad,#8b5cf6 0%,#4cc9f0 calc(var(--sp,0)*1%)),rgba(255,255,255,.08) 0);
-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
-webkit-mask-composite:xor;mask-composite:exclude;z-index:-1;transition:background .1s linear}
.progress-ring:hover,.progress-ring:focus-visible{transform:scale(1.03)}
@media (prefers-reduced-motion: reduce){.progress-ring::before{transition:none}}
```
SAFE JS:
```js
(function(){
var d=document.documentElement;
function upd(){
var h=d.scrollHeight-d.clientHeight;
d.style.setProperty('--sp', h>0?Math.round(window.scrollY/h*100):0);
}
window.addEventListener('scroll',upd,{passive:true});
upd();
})();
```

## Когда применять
визуальный триггер завершённости («вы дочитали — жмите»), +кликабельность CTA в нижних секциях, премиальный вид без картинок и библиотек.

## Проверка
открыть копию index.improved.html, прокрутить страницу — кольцо вокруг CTA должно заполняться по мере скролла; проверить Tab-фокус и prefers-reduced-motion в DevTools.

## SAFE JS
```js
```js
(function(){
var d=document.documentElement;
function upd(){
var h=d.scrollHeight-d.clientHeight;
d.style.setProperty('--sp', h>0?Math.round(window.scrollY/h*100):0);
}
window.addEventListener('scroll',upd,{passive:true});
upd();
})();
```
```
