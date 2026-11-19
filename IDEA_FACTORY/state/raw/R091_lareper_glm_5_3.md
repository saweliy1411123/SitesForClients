# lareper/glm-5.3  2026-11-17 06:06:57
duration=18.5 error=- attempts=1

IDEA: SKILL — luxury-serif-display (премиальная дисплейная типографика заголовков)
KNOB: Полное тело скилла:
**Name:** `luxury-serif-display`
**When to apply:** На любом лендинге, где заголовки h1/h2 набраны одним гротеском и выглядят «плоско». Шаги: (1) в `<head>` добавить второй display-шрифт (Playfair Display / Prata через Google Fonts, только вес 700, `display=swap`); (2) применить его только к h1 и `.grad-text`-частям заголовков — гротеск остаётся для текста; (3) добавить `letter-spacing:-.02em` и `font-feature-settings:"liga"`; (4) проверить на мобильных, что размер не ломает строки.
SAFE CSS:
```
h1, .final h2, .price-card h3{
  font-family:'Playfair Display', Georgia, serif;
  letter-spacing:-.02em;
  font-feature-settings:"liga" 1;
}
@media(max-width:480px){ h1{font-size:clamp(28px,7vw,40px);} }
```
EFFECT: визуально «дорогой» контраст serif-заголовков на фоне гротескного текста — классический приём премиум-брендов; рост воспринимаемой ценности услуги без изменения контента.
RISK: добавляется второй шрифт (~+20 КБ) — замедлит первый рендер при медленном интернете.
ROLLBACK: `git checkout -- index.improved.html` (оригинал не трогается).
VERIFY: открыть index.improved.html, сравнить hero и секцию цены с оригиналом; в DevTools → Network убедиться, что шрифт грузится один раз; сузить окно до 375px — заголовки не переносятся по буквам.
PRIORITY: 2 — сильный визуальный апгрейд «дорогого» вида, но с ценой в байтах.
SITE_REQUEST: Playfair

IDEA: SKILL — tilt-parallax-demo-cards (3D-наклон демо-концептов с глубиной слоёв)
KNOB: Полное тело скилла:
**Name:** `tilt-parallax-demo-cards`
**When to apply:** На сетках карточек (демо-концепты, шаги), где нужен «объём» без библиотек. Шаги: (1) обернуть содержимое карточки во внутренний слой `.card-inner`; (2) повесить на контейнер `perspective`; (3) hover — `rotateY/rotateX` + `translateZ` внутреннего слоя; (4) SAFE JS — лёгкий tilt по позиции курсора, только pointermove на десктопе (`matchMedia('(hover:hover)')`), отключение при `prefers-reduced-motion`; (5) на тач-устройствах tilt не активен, остаётся только hover-подъём.
SAFE CSS:
```
.card-tilt{perspective:900px;}
.card-tilt .card-inner{transition:transform .25s ease;transform-style:preserve-3d;will-change:transform;}
.card-tilt:hover .card-inner{transform:translateZ(18px);}
@media (prefers-reduced-motion: reduce){.card-tilt .card-inner{transition:none;transform:none!important;}}
```
SAFE JS:
```
document.querySelectorAll('.card-tilt').forEach(function(c){
  if(!matchMedia('(hover:hover)').matches) return;
  var inner=c.querySelector('.card-inner'); if(!inner) return;
  c.addEventListener('pointermove',function(e){
    var r=c.getBoundingClientRect();
    var x=(e.clientX-r.left)/r.width-.5, y=(e.clientY-r.top)/r.height-.5;
    inner.style.transform='rotateY('+(x*8)+'deg) rotateX('+(-y*8)+'deg) translateZ(12px)';
  });
  c.addEventListener('pointerleave',function(){
