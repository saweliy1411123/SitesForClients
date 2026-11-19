---
name: SKILL — «Trust-шапка первого экрана» (hero-trust-strip)
source: lareper/glm-5.3
round: 20
status: proposed
portable: true
tags: [static-landing, portable, responsive]
---

# SKILL — «Trust-шапка первого экрана» (hero-trust-strip)

Название: **hero-trust-strip**. Когда применять: любой статический лендинг, где первый экран содержит h1 + подзаголовок + CTA, но нет компактной строки доказательств между подзаголовком и CTA. Шаги:
1. Найти в hero элемент подзаголовка (класс `.sub` или аналог).
2. Сразу после него вставить `<div class="trust-strip" role="list">` с 3 пунктами-фактами (город, срок, формат связи) — только реальные факты, без выдуманных цифр.
3. Стили добавить через SAFE CSS ниже; JS не требуется.
4. Проверить на 375px: полоса должна переноситься в колонку без горизонтального скролла.
SAFE CSS:
.trust-strip{display:flex;gap:14px;flex-wrap:wrap;margin:18px 0 6px;padding:0}
.trust-strip span{display:inline-flex;align-items:center;gap:8px;font-size:14px;font-weight:600;color:inherit;opacity:.85;padding:8px 14px;border:1px solid rgba(255,255,255,.12);border-radius:999px;background:rgba(255,255,255,.04)}
.trust-strip span::before{content:"";width:7px;height:7px;border-radius:50%;background:#8b5cf6;flex:none}
@media (max-width:480px){.trust-strip{flex-direction:column;align-items:flex-start}}
@media (prefers-reduced-motion: reduce){.trust-strip{transition:none}}

## Когда применять
посетитель за 2 секунды видит три ключевых факта оффера (Пермь · 2 дня · бесплатное демо), растёт доверие и доскролл до CTA.

## Проверка
открыть копию index.improved.html на 375px и 1440px — полоса читаема, не сдвигает layout (CLS=0), скриншот до/после сравнить бок о бок.

## SAFE CSS
```css
.trust-strip{display:flex;gap:14px;flex-wrap:wrap;margin:18px 0 6px;padding:0}
.trust-strip span{display:inline-flex;align-items:center;gap:8px;font-size:14px;font-weight:600;color:inherit;opacity:.85;padding:8px 14px;border:1px solid rgba(255,255,255,.12);border-radius:999px;background:rgba(255,255,255,.04)}
.trust-strip span::before{content:"";width:7px;height:7px;border-radius:50%;background:#8b5cf6;flex:none}
@media (max-width:480px){.trust-strip{flex-direction:column;align-items:flex-start}}
@media (prefers-reduced-motion: reduce){.trust-strip{transition:none}}
```
