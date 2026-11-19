---
name: SKILL — sticky-header-shrink (шапка сжимается при скролле, не съедает первый экран)
source: lareper/glm-5.3-prime
round: 55
status: proposed
portable: true
tags: [static-landing, portable, responsive]
---

# SKILL — sticky-header-shrink (шапка сжимается при скролле, не съедает первый экран)

Название: sticky-header-shrink. Когда применять: любой одностраничник с фиксированной шапкой поверх полноэкранного hero (здесь `.hero{min-height:100vh}` + nav). Шаги: (1) убедиться, что шапка имеет `position:fixed` и класс, напр. `.nav`; (2) добавить SAFE CSS в `<style>`; (3) добавить SAFE JS перед `</body>` — один IntersectionObserver на sentinel-элемент перед hero-контентом; (4) проверить, что якоря (`#contact`, `#demo`) не прячутся под сжатой шапкой (при необходимости `scroll-padding-top`).
SAFE CSS:
.nav{transition:padding .25s ease,background .25s ease,box-shadow .25s ease}
.nav.is-compact{padding-top:8px;padding-bottom:8px;background:rgba(10,10,15,.85);backdrop-filter:blur(12px);box-shadow:0 1px 0 rgba(255,255,255,.06)}
html{scroll-padding-top:72px}
@media (prefers-reduced-motion: reduce){.nav{transition:none}}
SAFE JS:
(function(){
var nav=document.querySelector('.nav')||document.querySelector('header');
if(!nav)return;
var s=document.createElement('div');
s.style.cssText='position:absolute;top:0;height:40px;width:1px;pointer-events:none';
document.body.prepend(s);
new IntersectionObserver(function(e){
nav.classList.toggle('is-compact',!e[0].isIntersecting);
},{rootMargin:'-40px 0px 0px 0px'}).observe(s);
})();

## Когда применять
hero получает больше воздуха на мобильных, шапка становится читаемой при скролле (стекло + тень), якоря не прыгают под шапку — выше доверие и дольше скролл до CTA.

## Проверка
открыть страницу, проскроллить 100px — шапка сжалась и получила фон; Tab-навигацией пройти ссылки, кликнуть якорь — заголовок секции виден под шапкой; 3 минуты.

## SAFE CSS
```css
.nav{transition:padding .25s ease,background .25s ease,box-shadow .25s ease}
.nav.is-compact{padding-top:8px;padding-bottom:8px;background:rgba(10,10,15,.85);backdrop-filter:blur(12px);box-shadow:0 1px 0 rgba(255,255,255,.06)}
html{scroll-padding-top:72px}
@media (prefers-reduced-motion: reduce){.nav{transition:none}}
```

## SAFE JS
```js
(function(){
var nav=document.querySelector('.nav')||document.querySelector('header');
if(!nav)return;
var s=document.createElement('div');
s.style.cssText='position:absolute;top:0;height:40px;width:1px;pointer-events:none';
document.body.prepend(s);
new IntersectionObserver(function(e){
nav.classList.toggle('is-compact',!e[0].isIntersecting);
},{rootMargin:'-40px 0px 0px 0px'}).observe(s);
})();
```
