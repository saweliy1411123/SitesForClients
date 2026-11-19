---
name: SKILL — parallax-depth-layers (тонкий параллакс фоновых слоёв без библиотек)
source: lareper/glm-5.2
round: 56
status: proposed
portable: true
tags: [static-landing, portable, responsive]
---

# SKILL — parallax-depth-layers (тонкий параллакс фоновых слоёв без библиотек)

SKILL — parallax-depth-layers
Название: parallax-depth-layers
Когда применять: на тёмных лендингах с декоративными фоновыми слоями (blob, particles, veil, radial-градиенты), где хочется «дорогой» глубины при скролле без внешних библиотек и без вреда для производительности.
Шаги:
1. Декоративным слоям (например `.blob`, `#particles`, `.final-bg`) добавить класс `.plx` и атрибут `data-depth="0.15"` (значение 0.05–0.3 — чем меньше, тем медленнее слой).
2. Обязательно `aria-hidden="true"` и `pointer-events:none` на этих слоях (декор не должен попадать в tab-порядок).
3. Вставить SAFE JS ниже в конец `<body>`: он двигает слои через `transform: translate3d` на `requestAnimationFrame`, слушая один `scroll`-хендлер (пассивный).
4. Проверить на мобильном: если экран узкий (<720px) — скрипт сам отключается (слои остаются статичными), чтобы не жечь батарею.
5. Для `prefers-reduced-motion` параллакс отключается через matchMedia.
SAFE CSS:
```css
.plx{will-change:transform;transform:translate3d(0,0,0)}
@media (prefers-reduced-motion: reduce){.plx{transform:none!important}}
@media (max-width:720px){.plx{transform:none!important}}
```
SAFE JS:
```js
(function(){
if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
if(innerWidth<720)return;
var els=[].slice.call(document.querySelectorAll('.plx'));
if(!els.length)return;
var ticking=false;
function upd(){
var y=scrollY;
els.forEach(function(el){
var d=parseFloat(el.dataset.depth||'0.15');
el.style.transform='translate3d(0,'+(y*d*-1).toFixed(1)+'px,0)';
});
ticking=false;
}
addEventListener('scroll',function(){
if(!ticking){ticking=true;requestAnimationFrame(upd);}
},{passive:true});
})();
```

## Когда применять
фон живёт при скролле, страница ощущается дорогой и «глубокой» (как у премиум-студий), ноль внешних зависимостей, <1 КБ JS.

## Проверка
открыть копию, проскроллить — фоновые blob двигаются медленнее контента; в DevTools → Rendering → FPS meter держится ~60; при Emulate prefers-reduced-motion слои статичны.

## SAFE CSS
```css
```css
.plx{will-change:transform;transform:translate3d(0,0,0)}
@media (prefers-reduced-motion: reduce){.plx{transform:none!important}}
@media (max-width:720px){.plx{transform:none!important}}
```
```

## SAFE JS
```js
```js
(function(){
if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
if(innerWidth<720)return;
var els=[].slice.call(document.querySelectorAll('.plx'));
if(!els.length)return;
var ticking=false;
function upd(){
var y=scrollY;
els.forEach(function(el){
var d=parseFloat(el.dataset.depth||'0.15');
el.style.transform='translate3d(0,'+(y*d*-1).toFixed(1)+'px,0)';
});
ticking=false;
}
addEventListener('scroll',function(){
if(!ticking){ticking=true;requestAnimationFrame(upd);}
},{passive:true});
})();
```
```
