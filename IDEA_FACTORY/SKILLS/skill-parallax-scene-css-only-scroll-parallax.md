---
name: SKILL — parallax‑scene (CSS‑only scroll‑parallax)
source: localhost:8080/ovh/gpt-oss-120b
round: 56
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — parallax‑scene (CSS‑only scroll‑parallax)

METHOD: SKILL
**Name:** `parallax-scene`
**When to apply:** На лендингах с крупными визуальными блоками (hero, демо‑концепты), где нужен лёгкий глубинный эффект без JS‑библиотек.
**SAFE CSS:**
```css
.parallax-layer{
position:absolute;
inset:0;
will-change:transform;
}
.parallax-container{
position:relative;
overflow:hidden;
perspective:1200px;
}
.parallax-container .bg{
transform:translateZ(-300px) scale(1.5);
}
.parallax-container .mid{
transform:translateZ(-150px) scale(1.2);
}
.parallax-container .front{
transform:translateZ(0);
}
```
**SAFE JS:**
```js
(() => {
const layers = document.querySelectorAll('.parallax-layer');
if (!layers.length) return;
const onScroll = () => {
const scrollY = window.scrollY;
layers.forEach(l => {
const depth = parseFloat(l.dataset.depth) || 0;
const movement = -(scrollY * depth);
l.style.transform = `translateY(${movement}px)`;
});
};
window.addEventListener('scroll', onScroll, {passive:true});
})();
```

## Когда применять
Создаёт ощущение глубины, повышает визуальную привлекательность, увеличивает среднее время на странице.

## Проверка
Открыть страницу, прокрутить; убедиться, что слои движутся с разной скоростью, без «тряски».

## SAFE JS
```js
**
```js
(() => {
const layers = document.querySelectorAll('.parallax-layer');
if (!layers.length) return;
const onScroll = () => {
const scrollY = window.scrollY;
layers.forEach(l => {
const depth = parseFloat(l.dataset.depth) || 0;
const movement = -(scrollY * depth);
l.style.transform = `translateY(${movement}px)`;
});
};
window.addEventListener('scroll', onScroll, {passive:true});
})();
```
```
