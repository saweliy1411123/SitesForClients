---
name: SKILL — parallax‑scroll‑hero‑bg
source: localhost:8080/ovh/gpt-oss-120b
round: 98
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — parallax‑scroll‑hero‑bg

**NAME:** parallax-scroll-hero-bg
**WHEN TO APPLY:** В секции hero, где уже есть фон‑градиент и «blob»‑элементы, но нужен более глубокий визуальный эффект скролла.
**STEPS:**
1. Обернуть фоновые слои hero в контейнер `<div class="hero-parallax">`.
2. Добавить CSS‑переменную `--scroll-y` через небольший JS‑слушатель (не более 20 мс).
3. Применить 3‑слойный трансформ: задний слой – медленнее, передний – быстрее.
**SAFE CSS:**
```css
.hero-parallax {
perspective: 800px;
overflow: hidden;
}
.hero-parallax .bg-layer {
position: absolute;
inset: 0;
will-change: transform;
}
.hero-parallax .bg-layer.layer-1 { transform: translateZ(-30px) scale(1.2); }
.hero-parallax .bg-layer.layer-2 { transform: translateZ(-15px) scale(1.1); }
.hero-parallax .bg-layer.layer-3 { transform: translateZ(0); }
```
**SAFE JS:**
```js
document.addEventListener('scroll', () => {
const y = window.scrollY;
document.querySelectorAll('.hero-parallax .bg-layer').forEach((el,i)=>{
const speed = (i+1)*0.05;
el.style.transform = `translateY(${y*speed}px)`;
});
});
```

## Когда применять
Создаёт ощущение глубины при прокрутке, усиливает «premium»‑впечатление и удерживает внимание в верхней части страницы → увеличение времени‑на‑странице (dwell time).

## Проверка
Прокрутить страницу, убедиться в плавном смещении фоновых слоёв; включить/выключить `prefers-reduced-motion` в DevTools → эффект исчезает.

## SAFE JS
```js
**
```js
document.addEventListener('scroll', () => {
const y = window.scrollY;
document.querySelectorAll('.hero-parallax .bg-layer').forEach((el,i)=>{
const speed = (i+1)*0.05;
el.style.transform = `translateY(${y*speed}px)`;
});
});
```
```
