---
name: SKILL — tilt-glass-3d (3D-карточки с perspective/rotateY/translateZ и стеклянным слоем)
source: lareper/glm-5.3-prime
round: 63
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — tilt-glass-3d (3D-карточки с perspective/rotateY/translateZ и стеклянным слоем)

SKILL — tilt-glass-3d
Название: tilt-glass-3d
Когда применять: на тёмных лендингах с карточками (цена, демо, шаги), где нужен «дорогой» 3D-эффект без библиотек; к `.price-card` (L334), демо-карточкам, карточкам шагов.
Шаги:
1. Обернуть содержимое карточки в `<div class="tilt-inner">…</div>` (или применить к существующему внутреннему контейнеру).
2. Добавить SAFE CSS и SAFE JS ниже.
3. Проверить на мобильных: transform отключён по `hover:hover` и `prefers-reduced-motion`.
SAFE CSS:
```css
.tilt-wrap{perspective:900px}
.tilt-inner{
transform-style:preserve-3d;
transition:transform .25s ease, box-shadow .25s ease;
will-change:transform;
}
@media(hover:hover) and (prefers-reduced-motion:no-preference){
.tilt-wrap:hover .tilt-inner{
transform:rotateY(6deg) rotateX(-4deg) translateZ(14px);
box-shadow:0 40px 90px rgba(139,92,246,.28);
}
.tilt-wrap:hover .tilt-shine{opacity:.5}
}
.tilt-shine{
position:absolute;inset:0;border-radius:inherit;pointer-events:none;
background:linear-gradient(115deg,transparent 30%,rgba(255,255,255,.14) 45%,transparent 60%);
opacity:0;transition:opacity .3s;
}
.tilt-inner>*{transform:translateZ(24px)}
@media(prefers-reduced-motion:reduce){
.tilt-inner{transition:none}
}
```
SAFE JS:
```js
document.querySelectorAll('.tilt-wrap').forEach(function(w){
var inner=w.querySelector('.tilt-inner');
if(!inner) return;
w.addEventListener('mousemove',function(e){
if(matchMedia('(prefers-reduced-motion: reduce)').matches) return;
var r=w.getBoundingClientRect();
var x=(e.clientX-r.left)/r.width-.5, y=(e.clientY-r.top)/r.height-.5;
inner.style.transform='rotateY('+(x*10)+'deg) rotateX('+(-y*8)+'deg) translateZ(12px)';
});
w.addEventListener('mouseleave',function(){ inner.style.transform=''; });
});
```

## Когда применять
карточки цены/демо воспринимаются как премиальный продукт — hover-глубина повышает вовлечённость и клики по CTA внутри карточки.

## Проверка
открыть index.improved.html, навести на price-card — плавный 3D-наклон + блик; Tab-навигация не ломается; в DevTools включить prefers-reduced-motion — эффект исчезает; проверить на 360px ширине.

## SAFE JS
```js
```js
document.querySelectorAll('.tilt-wrap').forEach(function(w){
var inner=w.querySelector('.tilt-inner');
if(!inner) return;
w.addEventListener('mousemove',function(e){
if(matchMedia('(prefers-reduced-motion: reduce)').matches) return;
var r=w.getBoundingClientRect();
var x=(e.clientX-r.left)/r.width-.5, y=(e.clientY-r.top)/r.height-.5;
inner.style.transform='rotateY('+(x*10)+'deg) rotateX('+(-y*8)+'deg) translateZ(12px)';
});
w.addEventListener('mouseleave',function(){ inner.style.transform=''; });
});
```
```
