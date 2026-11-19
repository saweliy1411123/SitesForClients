---
name: Premium gradient sweep on hero heading
source: localhost:8081/big_only
round: 77
status: proposed
portable: true
tags: [static-landing, portable]
---

# Premium gradient sweep on hero heading

**SKILL — premium-hero-gradient-sweep**
**Name:** `premium-hero-gradient-sweep`
**When to apply:** На главном hero‑заголовке, где нужен премиальный визуальный акцент.
**SAFE CSS:**
```css
.hero h1 {
position: relative;
overflow: hidden;
color: transparent;
-webkit-background-clip: text;
background-clip: text;
background-image: linear-gradient(120deg, var(--blue) 30%, var(--purple) 70%);
background-size: 200% 100%;
animation: gradient-sweep 4s ease-in-out infinite;
}
@keyframes gradient-sweep {
0%   { background-position: 200% 0; }
50%  { background-position: 0 0; }
100% { background-position: 200% 0; }
}
```
**SAFE JS:** *(не требуется)*

## Когда применять
Привлекает внимание к главному офферу, усиливает ощущение премиальности и повышает время‑взгляда (dwell time).

## Проверка
Открыть страницу, убедиться, что заголовок анимирован плавным градиентом, измерить время до полной отрисовки в Chrome DevTools → Performance (не должно превышать 100 ms).

## SAFE JS
```js
** *(не требуется)*
```
