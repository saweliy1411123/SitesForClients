---
name: SKILL — Gradient Underline Hover for Section Headings
source: localhost:8080/ovh/gpt-oss-120b
round: 70
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Gradient Underline Hover for Section Headings

METHOD: SKILL
**Name:** gradient-underline-hover
**When to apply:** На заголовках h2 внутри секций, где требуется акцентировать название (например, «Три шага», «Цена», «FAQ»).
**Steps:**
1. Добавить к h2 класс `.underline-anim`.
2. В CSS создать псевдо‑элемент `::after` с градиентным `background-image`.
3. При `:hover`/`:focus-visible` анимировать `transform:scaleX(1)` от `scaleX(0)`.
SAFE CSS:
```css
h2.underline-anim{position:relative;overflow:hidden}
h2.underline-anim::after{
content:"";position:absolute;bottom:0;left:0;height:3px;width:100%;
background:linear-gradient(90deg,var(--blue),var(--purple));
transform:scaleX(0);transform-origin:left;transition:transform .35s ease
}
h2.underline-anim:hover::after,
h2.underline-anim:focus-visible::after{transform:scaleX(1)}
```
SAFE JS: *(не требуется)*

## Когда применять
При наведении/фокусе под заголовком появляется яркая градиентная линия, подчёркивающая важность секции и усиливающая восприятие «премиального» дизайна.

## Проверка
Открыть страницу, навести курсор на любой h2 с классом `.underline-anim` – должна появиться плавно анимированная градиентная линия; проверить доступность через клавиатуру (Tab → focus).

## SAFE JS
```js
*(не требуется)*
```
