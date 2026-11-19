---
name: SKILL — premium-typography-hover
source: localhost:8081/big_only
round: 147
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — premium-typography-hover

**Name:** `premium-typography-hover`
**When to apply:** На любые крупные заголовки (h1, h2) и ссылки‑CTA, где нужен премиальный визуальный отклик
**SAFE CSS:**
```css
/* premium-typography-hover */
h1, h2, .btn-primary {
font-variation-settings: "wght" 500;
transition: font-variation-settings 250ms ease, transform 250ms ease;
}
h1:hover, h2:hover, .btn-primary:hover,
h1:focus-visible, h2:focus-visible, .btn-primary:focus-visible {
font-variation-settings: "wght" 700;
transform: translateY(-2px);
}
```

## Когда применять
При наведении/фокусе заголовки плавно «утолщаются», создавая ощущение премиального качества и усиливая визуальный клик‑трэкинг → потенциальный рост CTR на CTA‑элементы

## Проверка
Открыть страницу, навести курсор на h1/h2/CTA — должно наблюдаться плавное утолщение текста и небольшое поднятие; в DevTools → Computed проверить `font-variation-settings` меняется с 500 на 700
