# lareper/glm-5.2  2026-11-17 06:07:13
duration=33.7 error=- attempts=1

SKILL — aurora-glass-hero (премиальное «стеклянное» свечение hero-панели с 3D-наклоном на мышь)

KNOB: SKILL — aurora-glass-hero
Название: `aurora-glass-hero`
Когда применять: на любом статическом лендинге, где hero-секция построена на тёмном фоне с градиентными blob-элементами (как `.hero` в index.html, L92–L142, L448–L455) — эффект «дорогого» сайта: стеклянная панель, плавное северное сияние внутри, лёгкий 3D-наклон панели за курсором. Не конфликтует с уже предложенными premium-parallax-hero / gradient-sweep (там двигается фон, здесь — стеклянная карточка с контентом).

Шаги:
1. В hero-разметке обернуть содержимое `.wrap` в `<div class="glass-panel">…</div>`.
2. Вставить SAFE CSS в `<style>`, SAFE JS — перед единственным `<script>`.
3. Проверить на мобильных: наклон отключён по `hover:none` и `prefers-reduced-motion`.

SAFE CSS:
```css
.glass-panel{
  position:relative;
  padding:clamp(28px,5vw,56px);
  border-radius:24px;
  background:rgba(255,255,255,.04);
  border:1px solid rgba(255,255,255,.09);
  backdrop-filter:blur(14px);
  -webkit-backdrop-filter:blur(14px);
  box-shadow:0 30px 80px rgba(0,0,0,.45), inset 0 1px 0 rgba(255,255,255,.08);
  transform-style:preserve-3d;
  transition:transform .25s ease-out, box-shadow .3s;
  max-width:820px;
}
.glass-panel::before{
  content:'';
  position:absolute; inset:-40%;
  background:
    radial-gradient(40% 35% at 25% 30%, rgba(139,92,246,.22), transparent 70%),
    radial-gradient(35% 30% at 75% 65%, rgba(76,201,240,.16), transparent 70%);
  animation:aurora-drift 14s ease-in-out infinite alternate;
  pointer-events:none;
  filter:blur(30px);
  z-index:-1;
}
@keyframes aurora-drift{
  0%{transform:translate(-3%,-2%) rotate(0deg)}
  100%{transform:translate(4%,3%) rotate(6deg)}
}
.glass-panel:hover{box-shadow:0 40px 110px rgba(139,92,246,.22), inset 0 1px 0 rgba(255,255,255,.12)}
@media (hover:none), (prefers-reduced-motion:reduce){
  .glass-panel{transform:none!important}
  .glass-panel::before{animation:none}
}
```

SAFE JS:
```js
(function(){
  var p=document.querySelector('.glass-panel');
  if(!p||window.matchMedia('(hover:none)').matches)return;
  if(window.matchMedia('(prefers-reduced-motion:reduce)').matches)return;
  var hero=p.closest('header')||p.parentElement;
  hero.addEventListener('mousemove',function(e){
    var r=hero.getBoundingClientRect();
    var x=(e.clientX-r.left)/r.width-.5, y=(e.clientY-r.top)/r.height-.5;
    p.style.transform='perspective(900px) rotateY('+(x*4)+'deg) rotateX('+(-y*3)+'deg) translateZ(0)';
  });
  hero.addEventListener('mouseleave',function(){p.style.transform='';});
})();
```

EFFECT: hero выглядит как премиальный продукт (стекло + живое свечение + микропараллакс) — растёт воспринимаемая ценность услуги «дорогой сайт», дольше задержка взгляда на первом экране.

RISK: backdrop-filter + blur может просадить
