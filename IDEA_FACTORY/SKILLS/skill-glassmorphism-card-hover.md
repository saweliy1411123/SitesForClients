---
name: SKILL — glassmorphism-card-hover
source: localhost:8080/ovh/gpt-oss-120b
round: 77
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — glassmorphism-card-hover

**Name:** `glassmorphism-card-hover`
**When to apply:** На карточки цены и отзывы (`.price-card`, `.testimonial-card`) для создания премиального «стеклянного» эффекта.
**SAFE CSS:**
```css
.glass-card{
background:rgba(255,255,255,.07);
backdrop-filter:blur(12px);
border:1px solid rgba(255,255,255,.15);
border-radius:12px;
transition:transform .4s ease,box-shadow .4s ease;
}
.glass-card:hover,
.glass-card:focus-visible{
transform:translateY(-6px);
box-shadow:0 12px 24px rgba(0,0,0,.2);
}
```

## Когда применять
Усилит визуальную дифференциацию премиум‑предложения, повышая доверие и время на странице → потенциальный рост конверсии на 2‑3 %.

## Проверка
Открыть страницу в Chrome, Safari, Firefox; убедиться, что карточки имеют лёгкое размытие и поднимаются при ховере; в браузерах без поддержки проверить, что фон всё‑равно полупрозрачный и читаемый.
