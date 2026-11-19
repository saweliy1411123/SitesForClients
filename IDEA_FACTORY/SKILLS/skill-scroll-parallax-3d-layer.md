---
name: SKILL — scroll‑parallax‑3d‑layer
source: localhost:8080/ovh/gpt-oss-120b
round: 154
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — scroll‑parallax‑3d‑layer

**Name:** `scroll-parallax-3d-layer`
**When to apply:** На декоративных фоновых элементах в секции `.hero` (например, `.hero-bg`, `.hero-blob`) и в секции `.final` для лёгкого 3‑D параллакса, реагирующего на движение мыши/скролл.
**SAFE CSS:**
```css
.parallax-layer {
position:absolute;
inset:0;
transform-style:preserve-3d;
will-change:transform;
}
```
**SAFE JS:**
```js
document.addEventListener('mousemove',e=>{
const layers = document.querySelectorAll('.parallax-layer');
const {innerWidth:w, innerHeight:h}=window;
const x = (e.clientX/w - 0.5)*2; // -1 .. 1
const y = (e.clientY/h - 0.5)*2;
layers.forEach(el=>{
const depth = parseFloat(el.dataset.depth)||0.2;
const tx = x*depth*15;
const ty = y*depth*15;
el.style.transform=`translate3d(${tx}px,${ty}px,0)`;
});
});
```

## Когда применять
Добавляет лёгкую глубину и интерактивность, усиливая премиальный «технологичный» имидж без тяжёлых библиотек.

## Проверка
Открыть страницу на десктопе, перемещать курсор – фоновые слои должны слегка смещаться; открыть в мобильном эмуляторе – движение не происходит, но фон остаётся.

## SAFE JS
```js
**
```js
document.addEventListener('mousemove',e=>{
const layers = document.querySelectorAll('.parallax-layer');
const {innerWidth:w, innerHeight:h}=window;
const x = (e.clientX/w - 0.5)*2; // -1 .. 1
const y = (e.clientY/h - 0.5)*2;
layers.forEach(el=>{
const depth = parseFloat(el.dataset.depth)||0.2;
const tx = x*depth*15;
const ty = y*depth*15;
el.style.transform=`translate3d(${tx}px,${ty}px,0)`;
});
});
```
```
