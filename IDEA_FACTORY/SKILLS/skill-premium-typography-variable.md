---
name: SKILL — premium-typography-variable
source: localhost:8080/ovh/gpt-oss-120b
round: 126
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — premium-typography-variable

**Name:** `premium-typography-variable`
**When to apply:** На всех заголовках (h1‑h3) и важных текстовых блоках, где доступен переменный шрифт Manrope (подключён уже).
**SAFE CSS:**
```css
/* enable variable font features */
h1, h2, h3 {
font-family: 'Manrope', system-ui, sans-serif;
font-variation-settings: "wght" 600;
transition: font-variation-settings .3s ease;
}
h1:hover, h2:hover, h3:hover {
font-variation-settings: "wght" 800;
}
```
**SAFE JS:** *(не требуется)*

## Когда применять
При наведении заголовок «толстеет», создавая ощущение интерактивности и высшего качества типографики без увеличения размеров шрифта.

## Проверка
Наведите курсор на любой заголовок – его толщина должна плавно увеличиться; проверка в DevTools → Computed → font‑variation‑settings.

## SAFE JS
```js
** *(не требуется)*
```
