# lareper/glm-5.3-prime  2026-11-17 06:29:44
duration=35.2 error=- attempts=1

IDEA: SKILL — glass-nav-scroll (стеклянная «плавающая» навигация при скролле)
KNOB: SKILL — glass-nav-scroll
Name: `glass-nav-scroll`
When to apply: на любом лендинге с фиксированной шапкой `<nav>`/`<header>`, где навигация прилипает к верху и должна выглядеть премиально при скролле (эффект матового стекла + мягкая тень).
Steps:
1. Убедиться, что навигация имеет `position:fixed; top:0; width:100%`.
2. Вставить SAFE CSS в `<style>`.
3. Вставить SAFE JS перед `</body>`: класс `.nav-scrolled` добавляется после 40px скролла.
4. Проверить на мобильных (≤720px) — blur не должен ломать раскладку.
SAFE CSS:
```css
.nav{
  transition:background .35s ease, box-shadow .35s ease, backdrop-filter .35s ease;
  background:transparent;
}
.nav.nav-scrolled{
  background:rgba(12,12,20,.55);
  -webkit-backdrop-filter:blur(14px) saturate(1.3);
  backdrop-filter:blur(14px) saturate(1.3);
  box-shadow:0 8px 32px rgba(0,0,0,.35);
  border-bottom:1px solid rgba(255,255,255,.06);
}
@media (prefers-reduced-motion:reduce){
  .nav{transition:none}
}
```
SAFE JS:
```js
(function(){
  var nav=document.querySelector('.nav')||document.querySelector('header');
  if(!nav)return;
  var t=false;
  window.addEventListener('scroll',function(){
    if(t)return;t=true;
    requestAnimationFrame(function(){
      nav.classList.toggle('nav-scrolled',window.scrollY>40);
      t=false;
    });
  },{passive:true});
})();
```
EFFECT: премиальный вид при скролле, контент читается под шапкой, доверие «дорогого» сайта без библиотек
RISK: backdrop-filter может мерцать на старых Android WebView — деградация до полупрозрачного фона безопасна
ROLLBACK: git checkout -- index.html (или удалить добавленные блоки CSS/JS)
VERIFY: открыть index.html, проскроллить 100px — шапка получает стекло+тень; Tab по ссылкам — фокус виден; Lighthouse Performance не падает
PRIORITY: 2 — чисто визуальный апгрейд, но сильный сигнал «дорого» на первом экране
SKILL: glass-nav-scroll

IDEA: SKILL — stacked-depth-sections (карточки-«стопка» с translateZ при скролле)
KNOB: SKILL — stacked-depth-sections
Name: `stacked-depth-sections`
When to apply: на лендингах, где 3–4 смысловых блока идут подряд (шаги, преимущества) и хочется премиальной «глубины» без библиотек.
Steps:
1. Обернуть целевые карточки в контейнер `.stack`.
2. Вставить SAFE
