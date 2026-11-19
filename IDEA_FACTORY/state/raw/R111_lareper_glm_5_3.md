# lareper/glm-5.3  2026-11-17 07:07:13
duration=2.4 error=- attempts=1

IDEA: SKILL — sticky-cta-reveal с честным появлением после hero (для уже существующего .sticky-cta)
KNOB: SKILL — `sticky-cta-reveal`
**Name:** `sticky-cta-reveal`
**When to apply:** На любом одностраничном лендинге, где главный CTA — якорная ссылка и на мобильных пользователь после скролла теряет доступ к кнопке. На этом сайте `.sticky-cta` уже есть в разметке (L735) и в CSS (L410–418), но по умолчанию `display:none` — скилл «оживляет» её без изменения разметки.
**Steps:**
1. Найти существующий блок `.sticky-cta` в разметке (он уже есть внизу страницы).
2. Добавить CSS: панель скрыта за нижним краем экрана, показывается только когда пользователь проскроллил первый экран (IntersectionObserver на hero-секции — без таймеров и fetch).
3. Не показывать панель, когда в зоне видимости финальный CTA-блок (иначе дублирование кнопки).
4. Проверить, что панель не перекрывает контент: добавить `padding-bottom` на `body` при показе.
5. Уважать `prefers-reduced-motion` — без анимации, мгновенный показ.

**SAFE CSS:**
```css
.sticky-cta{
  display:none;
}
@media (max-width:720px){
  .sticky-cta{
    display:block;
    position:fixed;
    left:0;right:0;bottom:0;
    z-index:50;
    padding:10px 14px calc(10px + env(safe-area-inset-bottom));
    background:rgba(15,15,22,.92);
    backdrop-filter:blur(12px);
    border-top:1px solid rgba(139,92,246,.25);
    transform:translateY(110%);
    transition:transform .3s ease;
  }
  .sticky-cta.is-visible{transform:translateY(0)}
  body.has-sticky-cta{padding-bottom:78px}
  @media (prefers-reduced-motion:reduce){
    .sticky-cta{transition:none}
  }
}
```

**SAFE JS:**
```js
(function(){
  var hero=document.querySelector('.hero');
  var bar=document.querySelector('.sticky-cta');
  var final=document.querySelector('.final');
  if(!hero||!bar) return;
  var io=new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      var heroGone=!e.isIntersecting;
      var finalVisible=false;
      if(final){
        var r=final.getBoundingClientRect();
        finalVisible=r.top<window.innerHeight&&r.bottom>0;
      }
      var show=heroGone&&!finalVisible;
      bar.classList.toggle('is-visible',show);
      document.body.classList.toggle('has-sticky-cta',show);
    });
  },{threshold:0});
  io.observe(hero);
  if(final) io.observe(final);
})();
```
EFFECT: на мобильных CTA всегда под рукой после первого экрана — больше переходов к демо/цене без прокрутки назад; существующая разметка используется, ничего не добавляется в HTML.
RISK: панель может перекрыть нижний контент на коротких экранах — компенсируется `padding-bottom` на body; при ошибке селектора `.final` кнопка дублируется с финальным CTA.
ROLLBACK: `git checkout -- index.improved.html` (изменения идут только в копию index.improved.html).
VERIFY: (1) Открыть index.improved.html в DevTools → режим iPhone. (2) Прокрутить ниже hero — панель въезжает снизу за 0.3 с. (3) Доскроллить до финального CTA — панель уезжает. (4) Tab-навигация: панель получает фокус, `padding-bottom` не обрезает футер. (5) Lighthouse → нет CLS-скачка при появлении.
PRIORITY:
