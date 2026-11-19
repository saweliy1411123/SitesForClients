# lareper/glm-5.3  2026-11-17 02:18:15
duration=2.3 error=- attempts=1

IDEA: SKILL — Scroll Progress Ring на CTA (прогресс-индикатор дочитывания вокруг кнопки)
KNOB: Название: **scroll-progress-cta**. Когда применять: любой статический лендинг с одним якорным CTA (#contact) и длинной прокруткой — повышает мотивацию дочитать и кликнуть, показывает «вы у цели». Шаги: (1) добавить в CSS кольцевой индикатор через conic-gradient, привязанный к переменной --sp; (2) добавить крошечный JS, который на scroll обновляет --sp на <html>; (3) повесить класс .progress-ring на главную CTA-кнопку (например, .btn-primary в hero и final). Не трогает контент и вёрстку, только визуальный слой.

SAFE CSS:
```css
.progress-ring{position:relative;isolation:isolate}
.progress-ring::before{content:"";position:absolute;inset:-4px;border-radius:inherit;padding:2px;
background:conic-gradient(var(--grad,#8b5cf6 0%,#4cc9f0 calc(var(--sp,0)*1%)),rgba(255,255,255,.08) 0);
-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);
-webkit-mask-composite:xor;mask-composite:exclude;z-index:-1;transition:background .1s linear}
.progress-ring:hover,.progress-ring:focus-visible{transform:scale(1.03)}
@media (prefers-reduced-motion: reduce){.progress-ring::before{transition:none}}
```

SAFE JS:
```js
(function(){
  var d=document.documentElement;
  function upd(){
    var h=d.scrollHeight-d.clientHeight;
    d.style.setProperty('--sp', h>0?Math.round(window.scrollY/h*100):0);
  }
  window.addEventListener('scroll',upd,{passive:true});
  upd();
})();
```

EFFECT: визуальный триггер завершённости («вы дочитали — жмите»), +кликабельность CTA в нижних секциях, премиальный вид без картинок и библиотек.
RISK: conic-gradient с mask-composite не поддерживается в старых Safari — кольцо просто не отрисуется, кнопка останется обычной (деградация безопасная).
ROLLBACK: git checkout -- index.html (или удалить класс .progress-ring и блоки CSS/JS).
VERIFY: открыть копию index.improved.html, прокрутить страницу — кольцо вокруг CTA должно заполняться по мере скролла; проверить Tab-фокус и prefers-reduced-motion в DevTools.
PRIORITY: 2 — заметный конверсионный и визуальный апгрейд, нулевой риск контента.
SITE_REQUEST: reveal

IDEA: SKILL — Reveal-on-scroll без дрожания (IntersectionObserver-стабилизатор для .reveal)
KNOB: Название: **safe-reveal-observer**. Когда применять: любой лендинг, где элементы с классом .reveal анимируются, но анимация может сработать до попадания в вьюпорт или не сработать без JS — приводит к «пустым» секциям. Шаги: (1) добавить SAFE CSS, который показывает .reveal по умолчанию и скрывает только при наличии JS-класса .js-ready; (2) добавить SAFE JS с IntersectionObserver, добавляющий класс .in при входе в вьюпорт; (3) на <html> повесить класс js-ready первым скриптом. Гарантирует: без JS контент виден, с JS — плавное появление.

SAFE CSS:
```css
.js-ready .reveal{opacity:0;transform:translateY(18px);transition:opacity .6s ease,transform .6s ease;transition-delay:var(--d,0s)}
.js-ready .reveal.in{opacity:1;transform:none}
@media (prefers-reduced-motion: reduce){.js-ready .reveal{opacity:1;transform:none;transition:none}}
```

SAFE JS:
```js

