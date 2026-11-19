# lareper/glm-5.2-fast-preview  2026-11-17 07:48:28
duration=2.3 error=- attempts=1

IDEA: SKILL — tilt-3d-cards (3D-наклон карточек за курсором с глубиной)
KNOB: SKILL — `tilt-3d-cards`
**When to apply:** на любом лендинге с карточками (цена, шаги, боль, демо), где нужен «дорогой» эффект глубины без библиотек.

**Steps:**
1. Добавить CSS (ниже) в `<style>`.
2. Добавить SAFE JS (ниже) перед `</body>` — он вешает perspective-наклон на элементы с классом `.tilt`.
3. На странице добавить класс `tilt` к карточкам: `.price-card` (L334), карточкам боли (L520, L542), шагам в `.steps` (L565+), демо-концептам (~L589).
4. На мобильных (≤720px) эффект отключается автоматически через media query — остаётся плоский hover-lift.

**SAFE CSS:**
```css
.tilt{transform-style:preserve-3d;transition:transform .18s ease-out,box-shadow .3s ease;will-change:transform}
.tilt:hover{box-shadow:0 30px 80px rgba(139,92,246,.25)}
.tilt .tilt-inner{transform:translateZ(24px)}
@media(max-width:720px){.tilt{transform:none!important}}
@media(prefers-reduced-motion:reduce){.tilt{transform:none!important;transition:none}}
```

**SAFE JS:**
```js
(function(){
if(matchMedia('(max-width:720px)').matches||matchMedia('(prefers-reduced-motion:reduce)').matches)return;
document.querySelectorAll('.tilt').forEach(function(c){
c.addEventListener('mousemove',function(e){
var r=c.getBoundingClientRect();
var x=(e.clientX-r.left)/r.width-.5;
var y=(e.clientY-r.top)/r.height-.5;
c.style.transform='perspective(900px) rotateY('+(x*8)+'deg) rotateX('+(-y*8)+'deg)';
});
c.addEventListener('mouseleave',function(){c.style.transform='';});
});
})();
```

EFFECT: премиальное ощущение «дорогого» продукта — карточки реагируют на курсор объёмом; усиливает доверие к цене и демо-концептам без единой внешней библиотеки.
RISK: при большом числе tilt-элементов возможны микроподлагивания на слабых устройствах — mitigировано отключением на мобильных и reduced-motion.
ROLLBACK: `git checkout -- index.improved.html` (CSS/JS попадают только в улучшенную копию; оригинал не трогается).
VERIFY: открыть index.improved.html, навести курсор на карточку цены и шаг — карточка плавно наклоняется к курсору; сузить окно до ≤720px — наклон исчезает; Tab-навигация не ломается (эффект только на hover мыши).
PRIORITY: 2 — заметный визуальный апгрейд под тему «дорогой сайт», нулевой риск для контента и SEO, но вторичен по отношению к конверсионным правкам.
SITE_REQUEST: price-card
