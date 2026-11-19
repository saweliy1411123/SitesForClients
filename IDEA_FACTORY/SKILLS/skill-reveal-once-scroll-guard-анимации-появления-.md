---
name: SKILL — reveal-once-scroll-guard (анимации появления без «мигания» и без CLS, с отключением при reduced-motion)
source: lareper/glm-5.2-fast-preview
round: 111
status: proposed
portable: true
tags: [static-landing, portable, responsive]
---

# SKILL — reveal-once-scroll-guard (анимации появления без «мигания» и без CLS, с отключением при reduced-motion)

SKILL — `reveal-once-scroll-guard`
**Name:** `reveal-once-scroll-guard`
**When to apply:** На любом статическом лендинге, где секции/карточки имеют классы `reveal`/`zoom` и анимируются при скролле через IntersectionObserver. Проблема, которую решает: элементы «мигают» при быстрой прокрутке, повторно проигрывают анимацию, вызывают сдвиг макета (CLS) и не отключаются для пользователей с `prefers-reduced-motion`. Переносим на любой сайт, где есть класс-триггер появления.
**Steps:**
1. Найти в JS класс-триггер (здесь `reveal`), убедиться, что анимация задаётся через `transform`/`opacity` (не через `height`/`top` — иначе CLS).
2. Добавить SAFE CSS: стартовое состояние, класс `.is-visible`, transition только на `opacity` и `transform`, `will-change` только до завершения, полный блок `@media (prefers-reduced-motion: reduce)`.
3. Добавить SAFE JS: один IntersectionObserver, `once: true` (элемент появляется один раз), порог 0.15, guard от двойного добавления класса.
4. Проверить: быстрая прокрутка вверх-вниз — анимация не повторяется; Lighthouse CLS = 0; при включённом reduced-motion контент виден сразу.
5. Откат: удалить добавленный CSS/JS-блок из копии `index.improved.html`.
**SAFE CSS:**
```css
.reveal{opacity:0;transform:translateY(24px);transition:opacity .6s ease,transform .6s cubic-bezier(.2,.7,.3,1);will-change:opacity,transform}
.reveal.zoom{transform:scale(.94)}
.reveal.is-visible{opacity:1;transform:none;will-change:auto}
@media (prefers-reduced-motion: reduce){
.reveal,.reveal.zoom{opacity:1;transform:none;transition:none;will-change:auto}
}
```
**SAFE JS:**
```js
(function(){
var els=document.querySelectorAll('.reveal');
if(!('IntersectionObserver' in window)||window.matchMedia('(prefers-reduced-motion: reduce)').matches){
els.forEach(function(e){e.classList.add('is-visible')});return;
}
var io=new IntersectionObserver(function(entries){
entries.forEach(function(en){
if(en.isIntersecting&&!en.target.classList.contains('is-visible')){
en.target.classList.add('is-visible');io.unobserve(en.target);
}
});
},{threshold:0.15,once:true});
els.forEach(function(e){io.observe(e)});
})();
```

## Когда применять
плавное премиальное появление секций без повторов и сдвигов макета; CLS≈0, ниже воспринимаемая «дешёвость» страницы, стабильный рендер на слабых телефонах.

## Проверка
(1) открыть index.improved.html, быстро проскроллить вниз и вверх — секции не мигают повторно; (2) DevTools → Rendering → Emulate prefers-reduced-motion: reduce — весь контент виден сразу; (3) Lighthouse → CLS = 0 за ~3 минуты.

## SAFE CSS
```css
стартовое состояние, класс `.is-visible`, transition только на `opacity` и `transform`, `will-change` только до завершения, полный блок `@media (prefers-reduced-motion: reduce)`.
3. Добавить SAFE JS: один IntersectionObserver, `once: true` (элемент появляется один раз), порог 0.15, guard от двойного добавления класса.
4. Проверить: быстрая прокрутка вверх-вниз — анимация не повторяется; Lighthouse CLS = 0; при включённом reduced-motion контент виден сразу.
5. Откат: удалить добавленный CSS/JS-блок из копии `index.improved.html`.
**SAFE CSS:**
```css
.reveal{opacity:0;transform:translateY(24px);transition:opacity .6s ease,transform .6s cubic-bezier(.2,.7,.3,1);will-change:opacity,transform}
.reveal.zoom{transform:scale(.94)}
.reveal.is-visible{opacity:1;transform:none;will-change:auto}
@media (prefers-reduced-motion: reduce){
.reveal,.reveal.zoom{opacity:1;transform:none;transition:none;will-change:auto}
}
```
**SAFE JS:**
```js
(function(){
var els=document.querySelectorAll('.reveal');
if(!('IntersectionObserver' in window)||window.matchMedia('(prefers-reduced-motion: reduce)').matches){
els.forEach(function(e){e.classList.add('is-visible')});return;
}
var io=new IntersectionObserver(function(entries){
entries.forEach(function(en){
if(en.isIntersecting&&!en.target.classList.contains('is-visible')){
en.target.classList.add('is-visible');io.unobserve(en.target);
}
});
},{threshold:0.15,once:true});
els.forEach(function(e){io.observe(e)});
})();
```
```

## SAFE JS
```js
один IntersectionObserver, `once: true` (элемент появляется один раз), порог 0.15, guard от двойного добавления класса.
4. Проверить: быстрая прокрутка вверх-вниз — анимация не повторяется; Lighthouse CLS = 0; при включённом reduced-motion контент виден сразу.
5. Откат: удалить добавленный CSS/JS-блок из копии `index.improved.html`.
**SAFE CSS:**
```css
.reveal{opacity:0;transform:translateY(24px);transition:opacity .6s ease,transform .6s cubic-bezier(.2,.7,.3,1);will-change:opacity,transform}
.reveal.zoom{transform:scale(.94)}
.reveal.is-visible{opacity:1;transform:none;will-change:auto}
@media (prefers-reduced-motion: reduce){
.reveal,.reveal.zoom{opacity:1;transform:none;transition:none;will-change:auto}
}
```
**SAFE JS:**
```js
(function(){
var els=document.querySelectorAll('.reveal');
if(!('IntersectionObserver' in window)||window.matchMedia('(prefers-reduced-motion: reduce)').matches){
els.forEach(function(e){e.classList.add('is-visible')});return;
}
var io=new IntersectionObserver(function(entries){
entries.forEach(function(en){
if(en.isIntersecting&&!en.target.classList.contains('is-visible')){
en.target.classList.add('is-visible');io.unobserve(en.target);
}
});
},{threshold:0.15,once:true});
els.forEach(function(e){io.observe(e)});
})();
```
```
