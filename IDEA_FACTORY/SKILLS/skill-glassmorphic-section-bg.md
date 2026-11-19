---
name: SKILL — glassmorphic-section-bg
source: localhost:8080/ovh/gpt-oss-120b
round: 112
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — glassmorphic-section-bg

Добавить класс `glass-section` к каждой `<section>` (например, `<section id="price" class="glass-section">`) и в CSS задать стиль:
```css
/* SAFE CSS */
.glass-section {
position: relative;
background: rgba(255,255,255,0.12);
border-radius: 12px;
border: 1px solid rgba(255,255,255,0.18);
backdrop-filter: blur(12px) saturate(150%);
-webkit-backdrop-filter: blur(12px) saturate(150%);
padding: 2rem;
overflow: hidden;
}
.glass-section::before {
content:"";
position:absolute;
inset:0;
background:linear-gradient(135deg, rgba(255,255,255,0.08), rgba(255,255,255,0));
pointer-events:none;
}
```

## Когда применять
Придаёт каждой секции премиальный «стеклянный» вид, усиливает визуальную иерархию и повышает восприятие цены/доверия.

## Проверка
Открыть страницу в браузере, убедиться, что фон секций стал полупрозрачным с блёром, а текст остаётся читаемым; проверить на мобильных устройствах.
