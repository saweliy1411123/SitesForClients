---
name: SKILL — 3D tilt-glass на карточках цены (perspective + rotateY + translateZ + блик)
source: lareper/glm-5.3-prime
round: 84
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — 3D tilt-glass на карточках цены (perspective + rotateY + translateZ + блик)

SKILL — tilt-glass-price-card
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

## Когда применять
карточка цены воспринимается как премиальный интерактивный объект; глубина и блик усиливают внимание к офферу и CTA, повышая вовлечённость без внешних библиотек.

## Проверка
(1) Открыть index.improved.html, навести мышь на .price-card — плавный наклон ≤8° и блик за курсором. (2) Tab-навигация: focus-within даёт тот же эффект без движения мыши. (3) DevTools → iPhone 375px — transform:none, нет дрожания. (4) Emulate prefers-reduced-motion — анимации выключены. (5) Console — нет ошибок.

## SAFE JS
```js
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
```
