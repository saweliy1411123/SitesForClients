# lareper/glm-5.2-fast-preview  2026-11-17 05:22:43
duration=38.1 error=- attempts=1

IDEA: SKILL — sticky-reveal-cta (мобильный липкий CTA с safe-area, появлением по скроллу и скрытием у финального блока)
KNOB: SKILL — sticky-reveal-cta
Название: sticky-reveal-cta
Когда применять: на любом статическом лендинге, где главный CTA — якорная ссылка внизу страницы, а на мобильных пользователь прокручивает долго и может не долистать до финального блока. Особенно на лендингах без форм, где конверсия = один клик по CTA.

Шаги:
1. Найдите главную якорную ссылку-CTA (например `<a class="btn-primary" href="#contact">…</a>`).
2. Перед закрывающим `</body>` добавьте:
```html
<div class="sticky-cta" id="stickyCta" role="region" aria-label="Быстрое действие">
  <a class="btn-primary" href="#contact">Получить демо — бесплатно</a>
</div>
```
3. Вставьте SAFE CSS в конец `<style>` (см. ниже).
4. Вставьте SAFE JS перед `</body>` (см. ниже).
5. Проверьте: на десктопе бар не появляется; на мобильном появляется после 400px прокрутки и исчезает, когда финальный CTA виден.
6. Убедитесь, что бар не перекрывает контент: добавьте к `<footer>`/финальной секции `padding-bottom: 96px` на мобильных (правило уже в SAFE CSS).

SAFE CSS:
```css
.sticky-cta{
  position:fixed;left:0;right:0;bottom:0;z-index:999;
  display:none;justify-content:center;
  padding:10px 14px calc(10px + env(safe-area-inset-bottom,0px));
  background:rgba(10,10,15,.86);
  -webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);
  border-top:1px solid rgba(139,92,246,.35);
  transform:translateY(110%);
  transition:transform .35s cubic-bezier(.22,.8,.3,1);
}
.sticky-cta.is-visible{transform:translateY(0)}
.sticky-cta .btn-primary{width:100%;max-width:420px;justify-content:center;text-align:center}
.sticky-cta a:focus-visible{outline:2px solid #8b5cf6;outline-offset:3px}
@media (max-width:768px){
  .sticky-cta{display:flex}
  footer, .final{padding-bottom:96px}
}
@media (prefers-reduced-motion:reduce){
  .sticky-cta{transition:none}
}
```

SAFE JS:
```js
(function(){
  var bar=document.getElementById('stickyCta');
  var target=document.getElementById('contact');
  if(!bar) return;
  var ticking=false;
  function update(){
    ticking=false;
    var y=window.scrollY||window.pageYOffset;
    var nearEnd=false;
    if(target){
      var r=target.getBoundingClientRect();
      nearEnd=r.top < window.innerHeight && r.bottom > 0;
    }
    bar.classList.toggle('is-visible', y>400 && !nearEnd);
  }
  window.addEventListener('scroll',function(){
    if(!ticking){ticking=true;requestAnimationFrame(update);}
  },{passive:true});
  update();
})();
```

EFFECT: мобильный посетитель видит CTA в любой момент прокрутки — растёт доля дошедших до заявки; на десктопе ничего не меняется, у финального блока бар не мешает.
RISK: бар может визуально спорить с финальной секцией, если у неё светлый фон — проверить контраст на реальной странице.
ROLLBACK: git checkout -- index.improved.html (или удалить блок .sticky-cta и его CSS/JS из копии).
VERIFY: открыть копию в DevTools → iPhone SE (375px), прокрутить 500px — бар
