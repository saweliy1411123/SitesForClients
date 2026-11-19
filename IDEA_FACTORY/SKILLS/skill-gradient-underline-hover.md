---
name: SKILL — gradient-underline-hover
source: localhost:8080/ovh/gpt-oss-120b
round: 153
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — gradient-underline-hover

**Name:** `gradient-underline-hover`
**When to apply:** На любой лендинге, где ссылки‑CTA оформлены без рамок и требуется визуально выделить интерактивность без изменения HTML‑структуры.
**Steps:**
1. Добавить в глобальный CSS правило для селектора `.btn-primary, a.cta-link`.
2. Использовать псевдо‑элемент `::after` для градиентной линии, которая появляется при `:hover` и `:focus-visible`.
**SAFE CSS:**
```css
/* Базовый стиль для интерактивных ссылок */
a.cta-link,
.btn-primary {
position: relative;
color: inherit;
text-decoration: none;
}
/* Градиентный подчёркнутый эффект */
a.cta-link::after,
.btn-primary::after {
content: "";
position: absolute;
left: 0;
bottom: -2px;
height: 3px;
width: 0;
background: linear-gradient(90deg, #8b5cf6, #4ec9f0);
transition: width .3s ease;
}
/* При наведении/фокусе анимация */
a.cta-link:hover::after,
a.cta-link:focus-visible::after,
.btn-primary:hover::after,
.btn-primary:focus-visible::after {
width: 100%;
}
/* Увеличенный таргет для доступности */
@media (pointer: coarse) {
a.cta-link,
.btn-primary {
min-height: 44px;
min-width: 44px;
display: inline-flex;
align-items: center;
justify-content: center;
}
}
```

## Когда применять
Интерактивные ссылки получают заметный, но лёгкий визуальный отклик → рост кликабельности и лучшая восприятие бренда.

## Проверка
Открыть страницу, наведите курсор на любую кнопку/ссылку с классом `.cta-link` или `.btn-primary` – должна появиться плавно растущая градиентная линия; проверить, что она видна и не перекрывает текст.
