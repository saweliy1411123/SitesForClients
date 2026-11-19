# lareper/glm-5.2  2026-11-17 07:30:30
duration=2.3 error=- attempts=2

IDEA: SKILL — hero-parallax-depth (слоистый параллакс blobs за мышью, глубина «дорогого» сайта)
KNOB: SKILL — hero-parallax-depth
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
EFFECT: hero ощущается объёмным и «дорогим», повышается воспринимаемый уровень продукта; ноль запросов и зависимостей.
RISK: на слабых устройствах постоянный rAF при движении мыши может слегка грузить CPU; эффект чисто декоративный.
ROLLBACK: git checkout -- index.improved.html (или удалить классы .plx и скрипт).
VERIFY: открыть копию файла, поводить мышью по hero — blobs должны плавно смещаться с разной амплитудой; в DevTools → Rendering → включить prefers-reduced-motion и убедиться, что движение исчезло; проверить на мобильной эмуляции, что слушатель не вешается.
PRIORITY: 2 — заметный премиум-эффект на первом экране, но не влияет напрямую на конверсию.
SKILL: hero-parallax-depth

IDEA: SKILL — grad-text-shimmer (живой блик по градиентному тексту h1)
KNOB: SKILL — grad-text-shimmer
Name: `grad-text-shimmer`
When to apply: на любом лендинге, где заголовок h1 содержит акцентный градиентный `<span>` (здесь `.grad-text` в h1, L459) и нужен тонкий премиальный акцент.
Steps:
1. К существующему правилу `.grad-text` (L115) добавить анимацию блика поверх градиента.
2. Вставить SAFE CSS.
3. Ничего в разметке менять не нужно — работает на текущем span.
SAFE CSS:
```css
