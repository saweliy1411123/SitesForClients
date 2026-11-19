---
name: SKILL — focus-ring-soft-glow (мягкое светящееся кольцо фокуса для всех интерактивных элементов)
source: localhost:8081/big_only
round: 75
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — focus-ring-soft-glow (мягкое светящееся кольцо фокуса для всех интерактивных элементов)

Полное тело скилла:
**Name:** `focus-ring-soft-glow`
**When to apply:** На любом статическом лендинге с тёмным фоном и интерактивными элементами (ссылки, CTA, навигация), где стандартный outline плохо виден или выглядит резко.
**Steps:**
1. Найти все интерактивные элементы: `a`, `.btn-primary`, `.nav-links a`, элементы с `tabindex`.
2. Добавить CSS-правила для `:focus-visible`, создающие мягкое свечение вместо стандартного outline.
3. Использовать `box-shadow` с полупрозрачным цветом акцента (взять `--blue` или `#8b5cf6`), чтобы кольцо было заметно, но не агрессивно.
4. Убедиться, что свечение не обрезается соседними элементами (проверить `overflow` у родительских контейнеров).
5. Сохранить видимость фокуса для клавиатурной навигации, но скрыть для мыши (`:focus:not(:focus-visible)`).
SAFE CSS:
```css
a:focus-visible,
.btn-primary:focus-visible,
.nav-links a:focus-visible,
[tabindex]:focus-visible {
outline: none;
box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.4), 0 0 20px rgba(139, 92, 246, 0.3);
border-radius: 8px;
}
a:focus:not(:focus-visible),
.btn-primary:focus:not(:focus-visible) {
outline: none;
box-shadow: none;
}
```
SAFE JS: (нет)

## Когда применять
Улучшенная доступность для пользователей с клавиатуры — фокус виден, но не режет глаз; премиальный вид на тёмном фоне; соответствует WCAG 2.4.7 (Focus Visible).

## Проверка
Открыть страницу, нажать Tab — увидеть мягкое фиолетовое свечение вокруг CTA и ссылок; кликнуть мышью — свечение не появляется.

## SAFE JS
```js
(нет)
```
