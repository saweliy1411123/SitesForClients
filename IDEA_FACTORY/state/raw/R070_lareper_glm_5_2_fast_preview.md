# lareper/glm-5.2-fast-preview  2026-11-17 05:05:04
duration=45.3 error=- attempts=1

IDEA: SKILL — aurora-border-cards (премиальная анимированная градиентная рамка для карточек цены/демо)
KNOB: SKILL — aurora-border-cards
Название: aurora-border-cards
Когда применять: на тёмных лендингах с карточками (цена, демо, шаги), где нужно ощущение «дорогого» продукта без картинок и библиотек. Рамка медленно переливается градиентом по периметру, реагирует на hover/focus, отключается при prefers-reduced-motion.

Шаги:
1. В копии index.improved.html обернуть каждую карточку (`.price-card`, демо-карточки) в `<div class="aurora-frame">…</div>` либо применить класс напрямую к карточке.
2. Вставить SAFE CSS в конец `<style>`.
3. (Опционально) SAFE JS — пауза анимации, когда карточка вне вьюпорта (экономия батареи).
4. Проверить на 375px: рамка не создаёт overflow.

SAFE CSS:
```css
.aurora-frame{position:relative;border-radius:22px;padding:1.5px;background:linear-gradient(120deg,rgba(139,92,246,.0),rgba(139,92,246,.0));overflow:hidden;isolation:isolate}
.aurora-frame::before{content:'';position:absolute;inset:-120%;z-index:-1;background:conic-gradient(from 0deg,transparent 0deg,rgba(139,92,246,.55) 60deg,rgba(76,201,240,.45) 120deg,transparent 180deg,rgba(139,92,246,.35) 260deg,transparent 360deg);animation:aurora-spin 9s linear infinite;opacity:0;transition:opacity .5s ease}
.aurora-frame:hover::before,.aurora-frame:focus-within::before{opacity:1}
.aurora-frame>.price-card,.aurora-frame>*{border-radius:21px;background:var(--card,#141420)}
@keyframes aurora-spin{to{transform:rotate(1turn)}}
@media (prefers-reduced-motion: reduce){.aurora-frame::before{animation:none;opacity:.35}}
```

SAFE JS:
```js
(function(){
  var els=document.querySelectorAll('.aurora-frame');
  if(!('IntersectionObserver' in window))return;
  var io=new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      e.target.style.setProperty('--aurora-play',e.isIntersecting?'running':'paused');
      e.target.querySelectorAll('*').forEach(function(c){});
      e.target.classList.toggle('aurora-off',!e.isIntersecting);
    });
  },{threshold:.05});
  els.forEach(function(el){io.observe(el)});
})();
```
+ дополнение в CSS: `.aurora-off::before{animation-play-state:paused}`

EFFECT: карточка цены и демо-концепты выглядят как у премиум-продуктов (Linear/Stripe-стиль); hover-реакция усиливает ощущение интерактивности и «дорогого» сайта — прямой аргумент в оффере «премиум-услуги выглядят дёшево» из секции боли.
RISK: conic-gradient + rotate на слабых мобильных GPU может поднять нагрузку; mitigated паузой вне вьюпорта и reduced-motion.
ROLLBACK: удалить блок `.aurora-frame` HTML и SAFE CSS/JS из index.improved.html, либо `git checkout -- index.improved.html`.
VERIFY: (1) открыть index.improved.html, навести на карточку цены — рамка начинает переливаться за <1 сек; (2) Tab до кнопки внутри карточки — focus-within включает рамку; (3) DevTools → 375px — нет горизонтального скролла; (4) Emulate prefers-reduced-motion в Rendering-панели — анимация остановлена. 5 минут.
PRIORITY: 2 — чисто визуальный апгрейд, но напрямую зак
