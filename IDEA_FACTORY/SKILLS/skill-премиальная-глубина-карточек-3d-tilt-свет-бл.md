---
name: SKILL — «Премиальная глубина карточек» (3D tilt + свет-блик, безопасный переносимый скилл)
source: lareper/glm-5.2
round: 21
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — «Премиальная глубина карточек» (3D tilt + свет-блик, безопасный переносимый скилл)


```
SKILL — premium-3d-tilt-glow
### Название
premium-3d-tilt-glow
### Когда применять
Любой лендинг с карточками (услуги, демо-концепты, шаги, FAQ-обёртки), где нужно ощущение «дорогого» сайта без библиотек. Применять после базовой вёрстки; отключать на тач-устройствах и при prefers-reduced-motion.
### Шаги
1. Добавить SAFE CSS в `<style>` (или в улучшенную копию).
2. Повесить класс `tilt-card` на карточки (например, блоки демо-концептов и шагов).
3. Вставить SAFE JS в конец `<body>` — он сам навешивает слушатели на `.tilt-card`, ничего не ломает, если элементов нет.
4. Проверить на мобильном: эффект отключён (matchMedia hover:hover), скролл не дёргается.
SAFE CSS:
.tilt-card{
transform-style:preserve-3d;
transition:transform .25s ease, box-shadow .25s ease;
will-change:transform;
position:relative;
}
.tilt-card::after{
content:"";
position:absolute; inset:0;
border-radius:inherit;
background:radial-gradient(320px circle at var(--gx,50%) var(--gy,50%),
rgba(255,255,255,.10), transparent 60%);
opacity:0;
transition:opacity .25s ease;
pointer-events:none;
}
.tilt-card:hover::after,.tilt-card:focus-within::after{opacity:1}
@media (hover:hover) and (prefers-reduced-motion:no-preference){
.tilt-card:hover{box-shadow:0 18px 40px rgba(0,0,0,.35)}
}
@media (prefers-reduced-motion:reduce){
.tilt-card{transition:none}
.tilt-card::after{display:none}
}
SAFE JS:
(function(){
if(!window.matchMedia('(hover:hover)').matches) return;
if(window.matchMedia('(prefers-reduced-motion:reduce)').matches) return;
document.querySelectorAll('.tilt-card').forEach(function(card){
card.addEventListener('mousemove',function(e){
var r=card.getBoundingClientRect();
var x=(e.clientX-r.left)/r.width-.5, y=(e.clientY-r.top)/r.height-.5;
card.style.transform='perspective(700px) rotateY('+(x*8)+'deg) rotateX('+(-y*8)+'deg) translateZ(6px)';
card.style.setProperty('--gx',((x+.5)*100)+'%');
card.style.setProperty('--gy',((y+.5)*100)+'%');
});
card.addEventListener('mouseleave',function(){
card.style.transform='';
});
});
})();
```

## Когда применять
Карточки демо-концептов и шагов ощущаются «дорогими» — глубина, блик под курсором, мягкая тень; повышает воспринимаемый уровень услуг и время взаимодействия с секцией демо.

## Проверка
Открыть копию index.improved.html в Chrome, навести на карточку демо — наклон и блик; Tab-фокус показывает блик через focus-within; DevTools → Rendering → prefers-reduced-motion: reduce — эффект исчезает; проверить на телефоне — наклона нет.

## SAFE JS
```js
(function(){
if(!window.matchMedia('(hover:hover)').matches) return;
if(window.matchMedia('(prefers-reduced-motion:reduce)').matches) return;
document.querySelectorAll('.tilt-card').forEach(function(card){
card.addEventListener('mousemove',function(e){
var r=card.getBoundingClientRect();
var x=(e.clientX-r.left)/r.width-.5, y=(e.clientY-r.top)/r.height-.5;
card.style.transform='perspective(700px) rotateY('+(x*8)+'deg) rotateX('+(-y*8)+'deg) translateZ(6px)';
card.style.setProperty('--gx',((x+.5)*100)+'%');
card.style.setProperty('--gy',((y+.5)*100)+'%');
});
card.addEventListener('mouseleave',function(){
card.style.transform='';
});
});
})();
```
```
