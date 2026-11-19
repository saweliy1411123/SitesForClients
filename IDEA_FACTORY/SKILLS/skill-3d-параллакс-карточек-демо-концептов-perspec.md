---
name: SKILL — 3D-параллакс карточек демо-концептов (perspective + rotateY по мыши/тапу)
source: lareper/glm-5.3-prime
round: 14
status: proposed
portable: true
tags: [static-landing, portable, 3d, responsive]
---

# SKILL — 3D-параллакс карточек демо-концептов (perspective + rotateY по мыши/тапу)

SKILL — **demo-card-3d-parallax**
### Название
demo-card-3d-parallax
### Когда применять
Любой лендинг с сеткой карточек (услуги, демо-концепты, шаги), где нужен «дорогой» премиальный вид без библиотек. Применять после базовой вёрстки, на десктопе — hover, на тач — лёгкий tilt при касании.
### Шаги
1. В CSS добавить переменную глубины и перспективу контейнеру сетки карточек.
2. Каждой карточке — transform-style: preserve-3d и слои контента с translateZ.
3. Крошечный SAFE JS: на pointermove вычислять rotateX/rotateY по позиции курсора, на pointerleave — сброс. prefers-reduced-motion — отключить.
4. Проверить на 375px: tilt не должен ломать скролл (touch-action: pan-y).
SAFE CSS:
```css
.cards-3d{perspective:1200px}
.card-3d{transform-style:preserve-3d;transition:transform .35s cubic-bezier(.2,.65,.3,1),box-shadow .35s;will-change:transform;touch-action:pan-y}
.card-3d .card-layer{transform:translateZ(28px)}
.card-3d .card-layer-deep{transform:translateZ(12px)}
.card-3d:hover,.card-3d:focus-within{box-shadow:0 24px 60px rgba(139,92,246,.18)}
@media (prefers-reduced-motion:reduce){.card-3d{transform:none!important;transition:none}}
```
SAFE JS:
```js
document.querySelectorAll('.card-3d').forEach(function(c){
var m=window.matchMedia('(prefers-reduced-motion: reduce)');
c.addEventListener('pointermove',function(e){
if(m.matches||e.pointerType==='touch')return;
var r=c.getBoundingClientRect();
var x=(e.clientX-r.left)/r.width-.5, y=(e.clientY-r.top)/r.height-.5;
c.style.transform='rotateY('+(x*10)+'deg) rotateX('+(-y*10)+'deg)';
});
c.addEventListener('pointerleave',function(){c.style.transform='';});
});
```

## Когда применять
карточки демо-концептов выглядят объёмными и «дорогими», растёт воспринимаемая ценность услуги и время на странице.

## Проверка
открыть index.improved.html, навести курсор на карточку демо — плавный наклон ≤10°, при Tab-фокусе и на 375px — без дрожания и без блокировки скролла (2–3 минуты).

## SAFE CSS
```css
```css
.cards-3d{perspective:1200px}
.card-3d{transform-style:preserve-3d;transition:transform .35s cubic-bezier(.2,.65,.3,1),box-shadow .35s;will-change:transform;touch-action:pan-y}
.card-3d .card-layer{transform:translateZ(28px)}
.card-3d .card-layer-deep{transform:translateZ(12px)}
.card-3d:hover,.card-3d:focus-within{box-shadow:0 24px 60px rgba(139,92,246,.18)}
@media (prefers-reduced-motion:reduce){.card-3d{transform:none!important;transition:none}}
```
```

## SAFE JS
```js
на pointermove вычислять rotateX/rotateY по позиции курсора, на pointerleave — сброс. prefers-reduced-motion — отключить.
4. Проверить на 375px: tilt не должен ломать скролл (touch-action: pan-y).
```
