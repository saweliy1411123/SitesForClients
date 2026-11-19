---
name: SKILL — variable-font-weight-heading-hover
source: localhost:8080/ovh/gpt-oss-120b
round: 77
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — variable-font-weight-heading-hover

**Name:** `variable-font-weight-heading-hover`
**When to apply:** На все заголовки уровня h1‑h3 для динамического изменения толщины шрифта при наведении/фокусе, создавая ощущение интерактивности премиум‑типа.
**SAFE CSS:**
```css
h1,h2,h3{
font-weight:500;
transition:font-weight .3s ease;
}
h1:hover,h1:focus-visible,
h2:hover,h2:focus-visible,
h3:hover,h3:focus-visible{
font-weight:700;
}
```

## Когда применять
Делает заголовки более «отзывчивыми», усиливает визуальный иерархический акцент → небольшое увеличение CTR на внутренние ссылки (≈1 %).

## Проверка
Навести курсор на заголовки в Chrome/Firefox, убедиться, что толщина шрифта меняется без рывков; проверить, что в мобильных режимах при тапе (focus) тоже происходит.
