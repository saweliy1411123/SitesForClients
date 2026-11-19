# lareper/glm-5.3-prime  2026-11-17 05:25:19
duration=2.2 error=- attempts=1

IDEA: SKILL — depth-layer-parallax (многослойный 3D-параллакс фона секций с translateZ и scroll-слоями)
SKILL — depth-layer-parallax
Название: depth-layer-parallax
Когда применять: на любом тёмном лендинге с декоративными фоновыми слоями (blobs, veils, particles), где нужен «дорогой» эффект глубины без библиотек. Отличается от I-00423 (там только mouse-параллакс блобов hero): здесь — слои с разной скоростью по скроллу через CSS custom properties + один крошечный SAFE JS, работает на всех секциях и деградирует на touch.
Шаги:
1. Обернуть декоративные слои каждой секции в контейнер `<div class="depth-scene" aria-hidden="true">`.
2. Каждому слою задать `data-depth="0.2"` (0.1–0.5 — чем меньше, тем медленнее).
3. SAFE JS на scroll выставляет `--shift` = (scrollY − sectionTop) × depth, CSS применяет translate3d.
4. На `prefers-reduced-motion` и на touch — отключить (JS проверяет `matchMedia('(prefers-reduced-motion: reduce)')` и `'ontouchstart' in window`).
5. Проверка: прокрутить страницу — слои движутся с разной скоростью; на телефоне — статично, без джанка.

SAFE CSS:
```css
.depth-scene{position:absolute;inset:0;overflow:hidden;pointer-events:none;z-index:0}
.depth-layer{position:absolute;will-change:transform;transform:translate3d(0,var(--shift,0px),0)}
@media (prefers-reduced-motion: reduce){.depth-layer{transform:none!important}}
```

SAFE JS:
```js
(function(){
var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
if(reduce||('ontouchstart' in window))return;
var layers=[].slice.call(document.querySelectorAll('.depth-layer'));
var sections=[].slice.call(document.querySelectorAll('section, header'));
function upd(){
var sy=window.scrollY;
layers.forEach(function(l){
var s=l.closest('section')||l.closest('header');
if(!s)return;
var d=parseFloat(l.dataset.depth)||0.2;
var off=(sy-s.offsetTop)*d;
l.style.setProperty('--shift',off.toFixed(1)+'px');
});
}
addEventListener('scroll',function(){requestAnimationFrame(upd)},{passive:true});
upd();
})();
```

EFFECT: ощущение дорогого «глубокого» сайта, дольше удержание внимания, премиальность без единой внешней библиотеки; вес <1 КБ JS.
RISK: при большом числе слоёв возможен джанк на слабых телефонах — ограничить 2–3 слоями на секцию.
ROLLBACK: удалить блок `.depth-scene` и SAFE JS; либо `git checkout -- index.improved.html`.
VERIFY: открыть копию index.improved.html, прокрутить — фоновые слои смещаются медленнее контента; в DevTools → Rendering → Paint flashing нет постоянной перекраски всего экрана; на эмуляции touch эффекта нет.
PRIORITY: 2 — заметный премиум-эффект, но не влияет напрямую на конверсию; применять после контентных улучшений.
SITE_REQUEST: blob

IDEA: SKILL — premium-card-lift (объёмный подъём карточек с тенью и светом при hover/focus)
SKILL — premium-card-lift
Название: premium-card-lift
Когда применять: на любом лендинге с карточками (услуги, шаги, FAQ, цена), где нужен «дорогой» hover без 3D-tilt (дополняет, а не дублирует I-00425 tilt-glass-3d: здесь только подъём + свет сверху, без rotateY — спокойнее и уместнее для секций шагов и цены).
Шаги:
1. Найти селекторы карточ
