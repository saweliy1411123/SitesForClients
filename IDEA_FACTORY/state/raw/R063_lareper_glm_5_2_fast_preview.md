# lareper/glm-5.2-fast-preview  2026-11-17 04:44:39
duration=23.9 error=- attempts=2

IDEA: SKILL — tilt-glass-3d (3D-карточки с perspective/rotateY/translateZ и стеклянным слоем)
KNOB: SKILL — tilt-glass-3d
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
EFFECT: карточки цены/демо воспринимаются как премиальный продукт — hover-глубина повышает вовлечённость и клики по CTA внутри карточки.
RISK: на слабых мобильных GPU постоянные transform могут дрожать — эффект ограничен `hover:hover` и reduced-motion, но требует теста на реальном телефоне.
ROLLBACK: `git checkout -- index.improved.html` (или удалить добавленные классы/блоки CSS+JS из копии).
VERIFY: открыть index.improved.html, навести на price-card — плавный 3D-наклон + блик; Tab-навигация не ломается; в DevTools включить prefers-reduced-motion — эффект исчезает; проверить на 360px ширине.
PRIORITY: 2 — усиливает «дорогой сайт» на ключевой секции цены, но не критично для конверсии.
SITE_REQUEST: price-card

IDEA: SKILL — light-sweep-heading (световой блик по заголовку секции)
KNOB: SKILL — light-sweep-heading
Название: light-sweep-heading
Когда применять: на заголовках h2 секций («Лендинг, который приводит…», «Три шага…», цена) на тёмных лендингах — тонкий пробегающий свет даёт «премиальность» без JS.
Шаги: добавить класс `.sweep` к выбранным
