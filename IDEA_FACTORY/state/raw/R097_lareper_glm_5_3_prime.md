# lareper/glm-5.3-prime  2026-11-17 06:26:24
duration=40.9 error=- attempts=1

IDEA: SKILL — count-up-proof-numbers (оживание цифр-доказательств при появлении в вьюпорте)
KNOB: SKILL — `count-up-proof-numbers`
Когда применять: на любом статическом лендинге, где есть блок цифр-доказательств (`.proof-item .num`, счётчики «2 дня», «N клиентов», цены) — анимированный отсчёт повышает внимание к ключевым числам оффера и работает без внешних библиотек.
Шаги:
1. Найти элементы с числами (например `.proof-item .num`), убедиться, что число записано как чистый текст с возможным суффиксом («12», «2 дня» → отделить число от текста через `<span data-count="12">12</span> дня`).
2. Добавить класс `data-countup` на каждый такой span; начальное значение в разметке оставить равным финальному (если JS отключён — цифры уже верные, деградации нет).
3. Вставить SAFE JS: IntersectionObserver запускает анимацию один раз, длительность ~900ms, easing ease-out, `prefers-reduced-motion` уважается.
4. Проверить на мобильном: цифры не прыгают по ширине — задать `font-variant-numeric: tabular-nums`.
SAFE CSS:
```css
[data-countup]{font-variant-numeric:tabular-nums;font-feature-settings:"tnum"}
@media (prefers-reduced-motion: reduce){
  [data-countup]{transition:none!important;animation:none!important}
}
```
SAFE JS:
```js
(function(){
  var els=document.querySelectorAll('[data-countup]');
  if(!els.length)return;
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function run(el){
    var target=parseInt(el.getAttribute('data-countup'),10);
    if(isNaN(target)||reduce){el.textContent=target;return;}
    var start=null;
    function step(ts){
      if(!start)start=ts;
      var p=Math.min((ts-start)/900,1);
      p=1-Math.pow(1-p,3);
      el.textContent=Math.round(target*p);
      if(p<1)requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  var io=new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(e.isIntersecting){run(e.target);io.unobserve(e.target);}
    });
  },{threshold:.5});
  els.forEach(function(el){io.observe(el);});
})();
```
EFFECT: цифры оффера («2 дня», сроки, цена) притягивают взгляд, повышают запоминаемость оффера; нулевой вес (нет библиотек), безопасная деградация без JS.
RISK: если число содержит нецифровые символы в самом span, анимация не запустится — число нужно выносить в атрибут.
ROLLBACK: удалить добавленный `<script>` и атрибуты `data-countup`, либо `git checkout -- index.improved.html`.
VERIFY: открыть копию index.improved.html, проскроллить к блоку цифр — числа отсчитывают снизу вверх один раз; отключить JS (DevTools → Ctrl+Shift+P → Disable JavaScript) — цифры видны сразу и корректны.
PRIORITY: 2 — заметный визуальный/конверсионный выигрыш при минимальном риске, но не критично для первого экрана.
SITE_REQUEST: proof-item


