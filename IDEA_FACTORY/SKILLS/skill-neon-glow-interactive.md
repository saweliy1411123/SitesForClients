---
name: SKILL — neon-glow-interactive
source: localhost:8080/ovh/gpt-oss-120b
round: 35
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — neon-glow-interactive

METHOD: SKILL
**Name:** `neon-glow-interactive`
**When to apply:** Для интерактивных элементов (кнопки, ссылки, карточки) на темных премиальных лендингах, где нужен мягкий световой акцент при наведении/фокусе, но без мерцания и без JavaScript.
**Steps:**
1. Добавить всем интерактивным элементам класс `.neon`.
2. В CSS задать переменную `--neon-color` (по умолчанию `#4cc9f0`).
3. Применить `box-shadow` и `filter: drop-shadow` для создания «неонового» свечения, а также `transition` для плавного появления.
4. Добавить `:focus-visible` стиль, идентичный `:hover`, чтобы обеспечить доступность.
**SAFE CSS:**
```css
.neon {
--neon-color: #4cc9f0;
position: relative;
color: var(--neon-color);
text-decoration: none;
transition: box-shadow .3s ease, filter .3s ease;
}
.neon::after {
content: "";
position: absolute;
inset: -4px;
border-radius: inherit;
background: var(--neon-color);
opacity: 0;
transition: opacity .3s ease;
}
.neon:hover,
.neon:focus-visible {
box-shadow: 0 0 12px var(--neon-color), 0 0 24px var(--neon-color);
filter: drop-shadow(0 0 8px var(--neon-color));
}
.neon:hover::after,
.neon:focus-visible::after {
opacity: 0.15;
}
```
**SAFE JS:** *не требуется*

## Когда применять
Делает ссылки и кнопки более заметными на тёмном фоне, повышает восприятие «премиального» дизайна и улучшает кликабельность без навязывания.

## Проверка
Открыть страницу, навести курсор и переключить фокус (Tab) – проверять, что световой эффект появляется и исчезает плавно, а в `prefers-reduced-motion` он отключается (можно добавить `@media (prefers-reduced-motion: reduce) { .neon { transition: none; } }`).

## SAFE JS
```js
** *не требуется*
```
