---
name: SKILL — bg-lazyload-intersection
source: localhost:8080/ovh/gpt-oss-120b
round: 69
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — bg-lazyload-intersection

**Name:** `bg-lazyload-intersection`
**When to apply:** На лендингах, где крупные блоки используют CSS‑фон (hero‑секция, разделы с изображениями), и требуется снизить CLS и LCP без изменения HTML‑структуры.
**Steps:**
1. Для каждого элемента с `background-image` заменить URL на атрибут `data-bg="url(...)"` и задать временный `background-color` (или прозрачный).
2. Добавить в конец `<body>` скрипт‑наблюдатель (IntersectionObserver), который при появлении элемента в зоне видимости устанавливает `style.backgroundImage = 'url(...)'`.
3. При загрузке добавить класс `.bg-loaded` для возможных анимаций fade‑in.
4. При необходимости добавить fallback‑скрипт для старых браузеров (проверка `IntersectionObserver` и загрузка сразу).
**SAFE CSS:**
```css
/* bg-lazyload‑intersection */
[data-bg]{
background-image:none;
background-size:cover;
background-position:center;
}
[data-bg].bg-loaded{
transition:opacity .4s ease;
opacity:1;
}
```
**SAFE JS:**
```js
/* bg-lazyload‑intersection */
(function(){
const lazyBgs = document.querySelectorAll('[data-bg]');
if(!('IntersectionObserver' in window)){
lazyBgs.forEach(el=>el.style.backgroundImage=`url(${el.dataset.bg})`);
return;
}
const onIntersect = (entries,obs)=>{
entries.forEach(entry=>{
if(entry.isIntersecting){
const el=entry.target;
el.style.backgroundImage=`url(${el.dataset.bg})`;
el.classList.add('bg-loaded');
obs.unobserve(el);
}
});
};
const io=new IntersectionObserver(onIntersect,{rootMargin:'200px'});
lazyBgs.forEach(el=>io.observe(el));
})();
```

## Когда применять
Сокращает объём загружаемых ресурсов при первом рендере – ускоряет First Contentful Paint и уменьшает Cumulative Layout Shift, что положительно влияет на Core Web Vitals и конверсию.

## Проверка
Открыть страницу в DevTools → Network, включить «Disable cache», перезагрузить; убедиться, что крупные фоновые изображения не запрашиваются сразу, а только после прокрутки к их секции. Проверить визуально, что фон появляется без рывков.

## SAFE JS
```js
**
```js
/* bg-lazyload‑intersection */
(function(){
const lazyBgs = document.querySelectorAll('[data-bg]');
if(!('IntersectionObserver' in window)){
lazyBgs.forEach(el=>el.style.backgroundImage=`url(${el.dataset.bg})`);
return;
}
const onIntersect = (entries,obs)=>{
entries.forEach(entry=>{
if(entry.isIntersecting){
const el=entry.target;
el.style.backgroundImage=`url(${el.dataset.bg})`;
el.classList.add('bg-loaded');
obs.unobserve(el);
}
});
};
const io=new IntersectionObserver(onIntersect,{rootMargin:'200px'});
lazyBgs.forEach(el=>io.observe(el));
})();
```
```
