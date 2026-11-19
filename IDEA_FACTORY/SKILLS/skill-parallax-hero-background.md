---
name: SKILL — Parallax Hero Background
source: localhost:8080/ovh/gpt-oss-120b
round: 14
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Parallax Hero Background

METHOD: Добавьте переиспользуемый скилл, который создаёт лёгкий вертикальный параллакс‑эффект для секции‑героя с помощью CSS‑переменной `--parallax` и небольшого JS‑скрипта, обновляющего её по `scroll`.
SAFE CSS:
```css
/* Parallax container – apply to <section class="hero"> */
.parallax-hero {
position: relative;
overflow: hidden;
perspective: 1px;
}
.parallax-hero::before {
content: "";
position: absolute;
inset: 0;
background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg"/>') center/cover;
transform: translateY(calc(var(--parallax, 0) * 0.3));
will-change: transform;
z-index: -1;
}
```
SAFE JS:
```js
document.addEventListener('scroll', () => {
const hero = document.querySelector('.parallax-hero');
if (!hero) return;
const rect = hero.getBoundingClientRect();
const offset = Math.max(0, -rect.top);
hero.style.setProperty('--parallax', offset + 'px');
});
```

## Когда применять
Визуальное усиление первого экрана, повышает восприятие премиальности и удерживает внимание посетителя.

## Проверка
Открыть страницу в Chrome, прокрутить вниз‑вверх и убедиться, что фон героя плавно смещается; сравнить скриншот до/после.

## SAFE JS
```js
```js
document.addEventListener('scroll', () => {
const hero = document.querySelector('.parallax-hero');
if (!hero) return;
const rect = hero.getBoundingClientRect();
const offset = Math.max(0, -rect.top);
hero.style.setProperty('--parallax', offset + 'px');
});
```
```
