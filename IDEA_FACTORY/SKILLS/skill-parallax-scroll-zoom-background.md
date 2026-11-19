---
name: SKILL — Parallax Scroll‑Zoom Background
source: localhost:8080/ovh/gpt-oss-120b
round: 70
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Parallax Scroll‑Zoom Background

METHOD: SKILL
**Name:** parallax-scroll-zoom
**When to apply:** На секциях с крупным фон‑изображением (например, `.hero`) где нужен лёгкий глубинный эффект без внешних библиотек.
**Steps:**
1. Добавить к секции атрибут `data-bg="url(...)"` (заменить текущий `background-image`).
2. В `<style>` задать начальное состояние `background-size: 100%; background-position: center;`.
3. Подключить небольшой безопасный JS‑скрипт, использующий `IntersectionObserver` и `requestAnimationFrame` для изменения `background-size` от `100%` до `115%` по мере прокрутки.
SAFE CSS:
```css
.parallax-zoom{background-image:var(--bg);background-size:100%;background-position:center;transition:background-size .3s ease-out}
```
SAFE JS:
```js
document.querySelectorAll('.parallax-zoom').forEach(el=>{
const img=el.dataset.bg;el.style.setProperty('--bg',`url(${img})`);
const onScroll=()=>{const rect=el.getBoundingClientRect();const perc=1-Math.min(Math.max(rect.top/window.innerHeight,0),1);
el.style.backgroundSize=100+15*perc+'%'}
window.addEventListener('scroll',()=>requestAnimationFrame(onScroll));
});
```

## Когда применять
Создаёт ощущение глубины и «живости» при скролле, усиливает премиальный визуальный стиль и удерживает внимание пользователя.

## Проверка
Открыть страницу, пролистать вниз – фон секции `.hero` должен плавно увеличиваться от 100% до 115% по мере прокрутки; проверить отсутствие «jank» в DevTools Performance.

## SAFE CSS
```css
```css
.parallax-zoom{background-image:var(--bg);background-size:100%;background-position:center;transition:background-size .3s ease-out}
```
```

## SAFE JS
```js
```js
document.querySelectorAll('.parallax-zoom').forEach(el=>{
const img=el.dataset.bg;el.style.setProperty('--bg',`url(${img})`);
const onScroll=()=>{const rect=el.getBoundingClientRect();const perc=1-Math.min(Math.max(rect.top/window.innerHeight,0),1);
el.style.backgroundSize=100+15*perc+'%'}
window.addEventListener('scroll',()=>requestAnimationFrame(onScroll));
});
```
```
