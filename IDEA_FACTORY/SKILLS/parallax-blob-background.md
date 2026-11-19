---
name: Parallax blob background
source: localhost:8080/ovh/gpt-oss-120b
round: 133
status: proposed
portable: true
tags: [static-landing, portable]
---

# Parallax blob background

SKILL — parallax-blob-layer
Name: parallax-blob-layer
When to apply: В секции `.hero` (или любой full‑width секции) для создания глубины с лёгким движением при наведении/скролле.
SAFE CSS:
```css
.hero {
perspective: 800px;
overflow: hidden;
}
.hero .blob-layer {
position: absolute;
inset: 0;
pointer-events: none;
background-repeat: no-repeat;
background-size: cover;
will-change: transform;
}
.blob-layer--far  { background-image: url('data:image/svg+xml,…'); transform: translateZ(-30px) scale(1.2); }
.blob-layer--mid  { background-image: url('data:image/svg+xml,…'); transform: translateZ(-15px) scale(1.1); }
.blob-layer--near { background-image: url('data:image/svg+xml,…'); transform: translateZ(0); }
```
SAFE JS:
```js
document.addEventListener('mousemove',e=>{
const {innerWidth:w,innerHeight:h}=window;
const x=(e.clientX/w-0.5)*2;
const y=(e.clientY/h-0.5)*2;
document.querySelectorAll('.blob-layer').forEach(el=>{
const depth=el.dataset.depth||0;
el.style.transform=`translate3d(${x*depth*10}px,${y*depth*10}px,0)`;
});
});
```

## Когда применять
Создаёт ощущение трёхмерного пространства, усиливает эмоциональное вовлечение и удержание внимания на первом экране.

## Проверка
Открыть страницу, переместить курсор – фон‑слои должны плавно смещаться в разных направлениях; проверить отсутствие лагов в DevTools → Performance.

## SAFE JS
```js
```js
document.addEventListener('mousemove',e=>{
const {innerWidth:w,innerHeight:h}=window;
const x=(e.clientX/w-0.5)*2;
const y=(e.clientY/h-0.5)*2;
document.querySelectorAll('.blob-layer').forEach(el=>{
const depth=el.dataset.depth||0;
el.style.transform=`translate3d(${x*depth*10}px,${y*depth*10}px,0)`;
});
});
```
```
