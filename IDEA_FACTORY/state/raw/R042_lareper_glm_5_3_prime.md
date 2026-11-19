# lareper/glm-5.3-prime  2026-11-17 03:42:01
duration=35.5 error=- attempts=1

IDEA: SKILL — Glass Depth Cards (многослойное стекло + 3D-погружение карточек)
KNOB: SKILL — glass-depth-cards
Название: glass-depth-cards
Когда применять: любой тёмный лендинг с карточками (демо-концепты, шаги, цена), где нужен «дорогой» эффект глубины без библиотек. Отличие от tilt-glow: карточка не просто наклоняется, а состоит из слоёв на разной translateZ — фон-стекло, контент, декоративный блик — что даёт настоящий параллакс внутри карточки при движении мыши.

Шаги:
1. Обернуть карточки в контейнер с `perspective` (родитель), карточке задать `transform-style: preserve-3d`.
2. Внутри карточки выделить 2–3 слоя: `.gdc-bg` (стекло), `.gdc-content`, `.gdc-shine` (декор).
3. Крошечный JS: на `mousemove` по карточке вычислять rotateX/rotateY (макс ±6°) и записывать в CSS-переменные; на `mouseleave` — сброс с transition.
4. На touch-устройствах и `prefers-reduced-motion` — отключить (только статичное стекло).

SAFE CSS:
```css
.gdc-wrap{perspective:900px}
.gdc{position:relative;transform-style:preserve-3d;transform:rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg));transition:transform .25s ease;border-radius:20px;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.12);backdrop-filter:blur(14px);overflow:hidden}
.gdc:hover{box-shadow:0 24px 60px rgba(139,92,246,.18)}
.gdc-content{transform:translateZ(40px)}
.gdc-shine{position:absolute;inset:0;transform:translateZ(70px);pointer-events:none;background:radial-gradient(240px circle at var(--mx,50%) var(--my,50%),rgba(255,255,255,.10),transparent 60%)}
@media (prefers-reduced-motion:reduce){.gdc{transform:none!important}.gdc-shine{display:none}}
```

SAFE JS:
```js
document.querySelectorAll('.gdc').forEach(function(c){
  if(matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  c.addEventListener('mousemove',function(e){
    var r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width,y=(e.clientY-r.top)/r.height;
    c.style.setProperty('--ry',((x-.5)*12)+'deg');
    c.style.setProperty('--rx',((.5-y)*12)+'deg');
    c.style.setProperty('--mx',(x*100)+'%');
    c.style.setProperty('--my',(y*100)+'%');
  });
  c.addEventListener('mouseleave',function(){c.style.setProperty('--rx','0deg');c.style.setProperty('--ry','0deg');});
});
```

EFFECT: карточки демо-концептов и цены выглядят объёмными и «премиальными»; блик следует за курсором — усиливает ощущение дорогого продукта, повышает вовлечённость и время на секции.
RISK: backdrop-filter + 3D-трансформы могут подтормаживать на слабых Android — обязателен graceful-fallback и reduced-motion.
ROLLBACK: `git checkout -- index.html` (правки только в index.improved.html).
VERIFY: (1) Применить к копии index.improved.html, открыть в Chrome, поводить мышью по карточке демо — наклон и блик следуют за курсором, слои «плавают» с разной глубиной. (2) Включить эмуляцию prefers-reduced-motion (DevTools → Rendering) — анимация отключается, карточка статична. (3) Проверить на 360px — без наклона, стекло сохранено.
P
