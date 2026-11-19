---
name: SKILL — hero-parallax-depth (слоистый параллакс blobs за мышью, глубина «дорогого» сайта)
source: lareper/glm-5.2-fast-preview
round: 119
status: proposed
portable: true
tags: [static-landing, portable, responsive]
---

# SKILL — hero-parallax-depth (слоистый параллакс blobs за мышью, глубина «дорогого» сайта)

SKILL — hero-parallax-depth
Name: `hero-parallax-depth`
When to apply: на любом лендинге с hero-секцией, где есть фоновые декоративные слои (blobs, градиенты, орнаменты) и нужен премиальный эффект глубины без библиотек.
Steps:
1. В hero найти декоративные фоновые элементы (blobs/veil) и добавить им классы `plx` и data-атрибут глубины: `data-depth="0.03"` (фоновые), `data-depth="0.06"` (средние).
2. Вставить SAFE CSS и SAFE JS ниже.
3. На тач-устройствах эффект автоматически не активен (JS проверяет `matchMedia('(hover:hover)')`).
SAFE CSS:
```css
.plx{will-change:transform;transition:transform .25s cubic-bezier(.2,.6,.2,1)}
@media (prefers-reduced-motion:reduce){.plx{transition:none;transform:none!important}}
```
SAFE JS:
```js
(function(){
if(!matchMedia('(hover:hover)').matches||matchMedia('(prefers-reduced-motion:reduce)').matches)return;
var els=document.querySelectorAll('.plx'),hx=0,hy=0,cx=0,cy=0,raf=null;
document.querySelector('.hero').addEventListener('mousemove',function(e){
hx=(e.clientX/innerWidth-.5)*2;hy=(e.clientY/innerHeight-.5)*2;
if(!raf)raf=requestAnimationFrame(step);});
function step(){cx+=(hx-cx)*.08;cy+=(hy-cy)*.08;
els.forEach(function(el){var d=parseFloat(el.dataset.depth||.04);
el.style.transform='translate3d('+(cx*d*100)+'px,'+(cy*d*100)+'px,0)';});
if(Math.abs(hx-cx)>.001||Math.abs(hy-cy)>.001){raf=requestAnimationFrame(step);}else{raf=null;}}
})();
```

## Когда применять
hero ощущается объёмным и «дорогим», повышается воспринимаемый уровень продукта; ноль запросов и зависимостей.

## Проверка
открыть копию файла, поводить мышью по hero — blobs должны плавно смещаться с разной амплитудой; в DevTools → Rendering → включить prefers-reduced-motion и убедиться, что движение исчезло; проверить на мобильной эмуляции, что слушатель не вешается.

## SAFE CSS
```css
```css
.plx{will-change:transform;transition:transform .25s cubic-bezier(.2,.6,.2,1)}
@media (prefers-reduced-motion:reduce){.plx{transition:none;transform:none!important}}
```
```

## SAFE JS
```js
```js
(function(){
if(!matchMedia('(hover:hover)').matches||matchMedia('(prefers-reduced-motion:reduce)').matches)return;
var els=document.querySelectorAll('.plx'),hx=0,hy=0,cx=0,cy=0,raf=null;
document.querySelector('.hero').addEventListener('mousemove',function(e){
hx=(e.clientX/innerWidth-.5)*2;hy=(e.clientY/innerHeight-.5)*2;
if(!raf)raf=requestAnimationFrame(step);});
function step(){cx+=(hx-cx)*.08;cy+=(hy-cy)*.08;
els.forEach(function(el){var d=parseFloat(el.dataset.depth||.04);
el.style.transform='translate3d('+(cx*d*100)+'px,'+(cy*d*100)+'px,0)';});
if(Math.abs(hx-cx)>.001||Math.abs(hy-cy)>.001){raf=requestAnimationFrame(step);}else{raf=null;}}
})();
```
```
