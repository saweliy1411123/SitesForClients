---
name: SKILL — parallax-scroll-layers
source: localhost:8080/ovh/gpt-oss-120b
round: 35
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — parallax-scroll-layers

METHOD: SKILL
**Name:** `parallax-scroll-layers`
**When to apply:** На лендингах, где есть несколько визуальных слоёв (фон, иллюстрации, карточки) и требуется лёгкий глубинный эффект при прокрутке, не используя тяжёлые JS‑библиотеки.
**Steps:**
1. Добавить в HTML контейнер‑обёртку `data-parallax` вокруг слоёв, которым нужен эффект (например, `.bg-layer`, `.mid-layer`, `.fg-layer`).
2. В CSS задать каждому слою начальное `transform: translateZ(0)` и `will-change: transform`.
3. Внизу файла добавить безопасный JS, который на событии `scroll` (с `requestAnimationFrame`) считает процент прокрутки и обновляет `transform: translateY(var(--offset))` для каждого слоя, используя коэффициенты глубины (например, 0.3, 0.6, 0.9).
4. Добавить `@media (prefers-reduced-motion: reduce)`‑правило, которое отключает скрипт (ставит `transform: none`).
**SAFE CSS:**
```css
[data-parallax] {
perspective: 1000px;
overflow: hidden;
}
[data-parallax] > .layer {
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
will-change: transform;
}
.layer-bg   { --depth: 0.2; }
.layer-mid  { --depth: 0.5; }
.layer-fg   { --depth: 0.8; }
```
**SAFE JS:**
```js
(() => {
const layers = document.querySelectorAll('[data-parallax] .layer');
if (!layers.length) return;
const onScroll = () => {
const scrollY = window.scrollY;
layers.forEach(l => {
const depth = parseFloat(getComputedStyle(l).getPropertyValue('--depth'));
l.style.transform = `translateY(${scrollY * depth}px)`;
});
};
const raf = () => { onScroll(); requestAnimationFrame(raf); };
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
requestAnimationFrame(raf);
})();
```

## Когда применять
Создаёт ощущение глубины и динамичности без тяжёлых библиотек, усиливая премиальный визуальный стиль и удерживая внимание посетителя.

## Проверка
Открыть страницу в браузере, включить DevTools → Performance, прокрутить и убедиться, что FPS ≥ 55 и нет «long tasks». Проверить, что при `prefers-reduced-motion` слой не движется.

## SAFE JS
```js
**
```js
(() => {
const layers = document.querySelectorAll('[data-parallax] .layer');
if (!layers.length) return;
const onScroll = () => {
const scrollY = window.scrollY;
layers.forEach(l => {
const depth = parseFloat(getComputedStyle(l).getPropertyValue('--depth'));
l.style.transform = `translateY(${scrollY * depth}px)`;
});
};
const raf = () => { onScroll(); requestAnimationFrame(raf); };
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
requestAnimationFrame(raf);
})();
```
```
