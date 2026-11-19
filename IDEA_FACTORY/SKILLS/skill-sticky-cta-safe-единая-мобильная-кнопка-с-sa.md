---
name: SKILL — sticky-cta-safe (единая мобильная кнопка с safe-area, скрытием у финального CTA и корректным фокусом)
source: lareper/glm-5.3
round: 76
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — sticky-cta-safe (единая мобильная кнопка с safe-area, скрытием у финального CTA и корректным фокусом)

В конец `<body>` (перед единственным `<script>`) добавить:
```html
<a class="sticky-cta" href="#contact" aria-label="Получить бесплатное демо — перейти к контакту">Получить демо бесплатно</a>
```
Шаги применения (переносимо на любой лендинг):
1. Найти селектор финального CTA-секции (здесь `.final`) и якорь контакта (здесь `#contact`) — подставить свои значения в CSS/HTML ниже.
2. Вставить HTML перед закрывающим `</body>`.
3. Вставить SAFE CSS в конец `<style>`.
4. Проверить на 360px и 375px, что кнопка не перекрывает контент и исчезает у финального CTA.
SAFE CSS:
```css
.sticky-cta{
display:none;
}
@media (max-width:768px){
.sticky-cta{
display:flex;
align-items:center;
justify-content:center;
position:fixed;
left:16px;
right:16px;
bottom:calc(14px + env(safe-area-inset-bottom,0px));
z-index:999;
padding:15px 20px;
border-radius:14px;
background:linear-gradient(135deg,#8b5cf6,#6d4aff);
color:#fff;
font-weight:700;
font-size:16px;
text-decoration:none;
box-shadow:0 12px 40px rgba(139,92,246,.45);
transform:translateY(120%);
transition:transform .35s ease, opacity .35s ease;
opacity:0;
}
.sticky-cta.is-visible{
transform:translateY(0);
opacity:1;
}
.sticky-cta:focus-visible{
outline:3px solid #fff;
outline-offset:3px;
}
.sticky-cta.is-hidden-at-final{
transform:translateY(120%);
opacity:0;
pointer-events:none;
}
}
@media (prefers-reduced-motion: reduce){
.sticky-cta{transition:none;transform:none;opacity:1;}
}
```
SAFE JS:
```js
(function(){
var cta=document.querySelector('.sticky-cta');
if(!cta)return;
var finalSection=document.querySelector('.final')||document.querySelector('footer');
function update(){
var scrolled=window.scrollY>400;
var nearFinal=false;
if(finalSection){
var r=finalSection.getBoundingClientRect();
nearFinal=r.top<window.innerHeight;
}
cta.classList.toggle('is-visible',scrolled&&!nearFinal);
cta.classList.toggle('is-hidden-at-final',nearFinal);
}
window.addEventListener('scroll',update,{passive:true});
update();
})();
```

## Когда применять
на мобильных (основной трафик по брифу) CTA всегда под большим пальцем — меньше потери лидов на длинном скролле; кнопка исчезает у финального блока, не создавая дубля.

## Проверка
(1) DevTools → iPhone SE 375px; (2) прокрутить 500px — кнопка появилась; (3) доскроллить до `.final` — исчезла; (4) Tab — фокус-кольцо видно; (5) Console: `document.querySelector('.sticky-cta')` не null.

## SAFE JS
```js
```js
(function(){
var cta=document.querySelector('.sticky-cta');
if(!cta)return;
var finalSection=document.querySelector('.final')||document.querySelector('footer');
function update(){
var scrolled=window.scrollY>400;
var nearFinal=false;
if(finalSection){
var r=finalSection.getBoundingClientRect();
nearFinal=r.top<window.innerHeight;
}
cta.classList.toggle('is-visible',scrolled&&!nearFinal);
cta.classList.toggle('is-hidden-at-final',nearFinal);
}
window.addEventListener('scroll',update,{passive:true});
update();
})();
```
```
