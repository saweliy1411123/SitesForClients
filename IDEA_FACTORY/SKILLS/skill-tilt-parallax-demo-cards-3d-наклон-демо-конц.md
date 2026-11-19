---
name: SKILL — tilt-parallax-demo-cards (3D-наклон демо-концептов с глубиной слоёв)
source: lareper/glm-5.3
round: 91
status: proposed
portable: true
tags: [static-landing, portable, 3d, responsive]
---

# SKILL — tilt-parallax-demo-cards (3D-наклон демо-концептов с глубиной слоёв)

Полное тело скилла:
**Name:** `tilt-parallax-demo-cards`
**When to apply:** На сетках карточек (демо-концепты, шаги), где нужен «объём» без библиотек. Шаги: (1) обернуть содержимое карточки во внутренний слой `.card-inner`; (2) повесить на контейнер `perspective`; (3) hover — `rotateY/rotateX` + `translateZ` внутреннего слоя; (4) SAFE JS — лёгкий tilt по позиции курсора, только pointermove на десктопе (`matchMedia('(hover:hover)')`), отключение при `prefers-reduced-motion`; (5) на тач-устройствах tilt не активен, остаётся только hover-подъём.
SAFE CSS:
```
.card-tilt{perspective:900px;}
.card-tilt .card-inner{transition:transform .25s ease;transform-style:preserve-3d;will-change:transform;}
.card-tilt:hover .card-inner{transform:translateZ(18px);}
@media (prefers-reduced-motion: reduce){.card-tilt .card-inner{transition:none;transform:none!important;}}
```
SAFE JS:
```
document.querySelectorAll('.card-tilt').forEach(function(c){
if(!matchMedia('(hover:hover)').matches) return;
var inner=c.querySelector('.card-inner'); if(!inner) return;
c.addEventListener('pointermove',function(e){
var r=c.getBoundingClientRect();
var x=(e.clientX-r.left)/r.width-.5, y=(e.clientY-r.top)/r.height-.5;
inner.style.transform='rotateY('+(x*8)+'deg) rotateX('+(-y*8)+'deg) translateZ(12px)';
});
c.addEventListener('pointerleave',function(){

## Когда применять


## Проверка


## SAFE CSS
```css
```
.card-tilt{perspective:900px;}
.card-tilt .card-inner{transition:transform .25s ease;transform-style:preserve-3d;will-change:transform;}
.card-tilt:hover .card-inner{transform:translateZ(18px);}
@media (prefers-reduced-motion: reduce){.card-tilt .card-inner{transition:none;transform:none!important;}}
```
```
