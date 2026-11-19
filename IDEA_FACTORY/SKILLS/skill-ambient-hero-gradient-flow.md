---
name: SKILL — ambient-hero-gradient-flow
source: localhost:8080/ovh/gpt-oss-120b
round: 126
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — ambient-hero-gradient-flow

**Name:** `ambient-hero-gradient-flow`
**When to apply:** В секции hero, где нужен фон‑градиент, медленно «текущий» по оси X/Y, создающий ощущение премиального движения без JavaScript.
**SAFE CSS:**
```css
/* ambient gradient animation */
.hero-bg-ambient {
position: absolute;
inset: 0;
background: linear-gradient(135deg,
#8b5cf6 0%,
#34d399 35%,
#22d3ee 70%,
#8b5cf6 100%);
background-size: 300% 300%;
animation: ambientFlow 20s ease infinite;
z-index: -1;
}
@keyframes ambientFlow {
0%   {background-position: 0% 50%;}
50%  {background-position: 100% 50%;}
100% {background-position: 0% 50%;}
}
```
**SAFE JS:** *(не требуется)*

## Когда применять
Создаёт динамический, но ненавязчивый фон, усиливающий ощущение «дорогого» сайта и удерживает взгляд посетителя в верхней части страницы.

## Проверка
Открыть страницу, убедиться в плавном смещении градиента в hero; проверить в Chrome DevTools → Computed → animation‑name.

## SAFE JS
```js
** *(не требуется)*
```
