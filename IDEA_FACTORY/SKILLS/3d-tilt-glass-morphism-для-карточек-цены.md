---
name: 3D‑tilt glass‑morphism для карточек цены
source: localhost:8081/big_only
round: 77
status: proposed
portable: true
tags: [static-landing, portable]
---

# 3D‑tilt glass‑morphism для карточек цены

**SKILL — tilt-glass-price-card**
**Name:** `tilt-glass-price-card`
**When to apply:** На блоках `.price-card` в секции цены, где нужен премиальный 3‑D‑эффект и стеклянный вид.
**SAFE CSS:**
```css
.price-card {
perspective: 800px;
background: rgba(255,255,255,0.07);
backdrop-filter: blur(12px);
border: 1px solid rgba(255,255,255,0.2);
transform-style: preserve-3d;
transition: transform 0.35s ease, box-shadow 0.35s ease;
}
.price-card:hover,
.price-card:focus-visible {
transform: rotateY(8deg) rotateX(4deg) translateZ(20px);
box-shadow: 0 12px 30px rgba(0,0,0,0.25);
}
.price-card::before {
content:"";
position:absolute;
inset:0;
border-radius:inherit;
background: linear-gradient(135deg, rgba(255,255,255,0.15), transparent);
pointer-events:none;
}
```
**SAFE JS:** *(не требуется)*

## Когда применять
Делает цену более «осязаемой», повышает доверие и запоминаемость предложения, усиливает восприятие премиального бренда.

## Проверка
Открыть страницу на десктопе и мобильном, проверить плавность анимации (Chrome DevTools → Rendering → FPS > 55).

## SAFE JS
```js
** *(не требуется)*
```
