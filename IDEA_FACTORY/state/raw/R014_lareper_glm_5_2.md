# lareper/glm-5.2  2026-11-17 02:22:27
duration=6.0 error=- attempts=2

IDEA: SKILL — 3D-параллакс карточек демо-концептов (perspective + rotateY по мыши/тапу)
KNOB: SKILL — **demo-card-3d-parallax**
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
EFFECT: карточки демо-концептов выглядят объёмными и «дорогими», растёт воспринимаемая ценность услуги и время на странице.
RISK: на слабых мобильных устройствах постоянные transform могут давать рывки — эффект ограничен hover и отключается при reduced-motion.
ROLLBACK: `git checkout -- index.html` (правки вносятся в index.improved.html, оригинал не трогаем).
VERIFY: открыть index.improved.html, навести курсор на карточку демо — плавный наклон ≤10°, при Tab-фокусе и на 375px — без дрожания и без блокировки скролла (2–3 минуты).
PRIORITY: 2 — чисто визуальный апгрейд «премиальности», делается после конверсионных правок.
SITE_REQUEST: демо-концепты

IDEA: SKILL — Премиальная типографика: контрастная пара заголовков + оптические кернинг-правила
KNOB: SKILL — **premium-typography-pair**
### Название
premium-typography-pair
### Когда применять
Любой лендинг на одном шрифте (Manrope), где заголовки выглядят «плоско». Даёт дорогой вид за счёт иерархии, а не нового шрифта.
### Шаги
1. Заголовкам h1/h2 — отрицательный letter-spacing (-0.02…-0.03em) и font-weight 700→800 контраст.
2. Основному
