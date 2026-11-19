# lareper/glm-5.2  2026-11-17 05:46:46
duration=2.3 error=- attempts=2

IDEA: SKILL — 3D tilt-glass на карточках цены (perspective + rotateY + translateZ + блик)
KNOB: SKILL — tilt-glass-price-card
Название: tilt-glass-price-card
Когда применять: на любом лендинге с карточками цены/оффера, где нужен «дорогой» вид без библиотек; работает на десктопе, отключается на тач и при prefers-reduced-motion.

Шаги:
1. Найти контейнер карточек (здесь `.price-card`, L334).
2. Вставить SAFE CSS в `<style>`.
3. Вставить SAFE JS перед закрывающим `</body>` (без fetch/eval/innerHTML).
4. Проверить hover мышью: карточка наклоняется к курсору, блик следует за ним; на тач — просто hover-подъём.

SAFE CSS:
```css
.price-tilt-wrap{perspective:900px}
.price-card{transform-style:preserve-3d;transition:transform .25s ease,box-shadow .25s ease;will-change:transform}
.price-card:hover,.price-card:focus-within{box-shadow:0 34px 100px rgba(139,92,246,.35)}
.price-card::after{content:'';position:absolute;inset:0;border-radius:inherit;pointer-events:none;
background:radial-gradient(300px circle at var(--mx,50%) var(--my,0%),rgba(255,255,255,.12),transparent 60%);
opacity:0;transition:opacity .25s ease}
.price-card:hover::after,.price-card:focus-within::after{opacity:1}
.price-card .flag,.price-card h3{transform:translateZ(24px)}
.price-card .price{transform:translateZ(38px)}
@media (max-width:768px){.price-card{transform:none!important}}
@media (prefers-reduced-motion: reduce){.price-card{transition:none;transform:none!important}.price-card::after{display:none}}
```

SAFE JS:
```js
document.querySelectorAll('.price-card').forEach(function(card){
  card.addEventListener('pointermove',function(e){
    if(e.pointerType!=='mouse')return;
    var r=card.getBoundingClientRect();
    var x=(e.clientX-r.left)/r.width, y=(e.clientY-r.top)/r.height;
    card.style.setProperty('--mx',(x*100)+'%');
    card.style.setProperty('--my',(y*100)+'%');
    card.style.transform='rotateY('+((x-.5)*8)+'deg) rotateX('+((.5-y)*8)+'deg)';
  });
  card.addEventListener('pointerleave',function(){card.style.transform='';});
});
```

EFFECT: карточка цены воспринимается как премиальный интерактивный объект; глубина и блик усиливают внимание к офферу и CTA, повышая вовлечённость без внешних библиотек.
RISK: наклон может дёргаться при быстром курсоре и мешать чтению мелкого текста — амплитуда ограничена 8°, на тач и reduced-motion отключено.
ROLLBACK: git checkout -- index.html (или удалить добавленные блоки CSS/JS из index.improved.html).
VERIFY: (1) Открыть index.improved.html, навести мышь на .price-card — плавный наклон ≤8° и блик за курсором. (2) Tab-навигация: focus-within даёт тот же эффект без движения мыши. (3) DevTools → iPhone 375px — transform:none, нет дрожания. (4) Emulate prefers-reduced-motion — анимации выключены. (5) Console — нет ошибок.
PRIORITY: 2 — чисто премиальный визуал, влияет на восприятие, но не на смысл оффера; безопасно и дёшево.
SITE_REQUEST: price-card
SKILL: tilt-glass-price-card

IDEA: SKILL — spotlight-text (последовательное «проявление» слов h2 при появлении секции)
KNOB: SKILL — spotlight-word-reveal
Название: spotlight-word
