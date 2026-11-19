---
name: SKILL — Focus‑Visible Outline
source: localhost:8080/ovh/gpt-oss-120b
round: 48
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Focus‑Visible Outline

**Name:** focus-visible-outline
**When to apply:** На любой статический лендинг, где интерактивные ссылки/кнопки (a, .btn‑primary) должны быть доступными для клавиатурных пользователей.
**Steps:**
1. Добавить в глобальный CSS селектор `:focus-visible` для всех интерактивных элементов.
2. Сбросить стандартные outline‑ы и задать кастомный контрастный стиль, сохраняющий визуальную согласованность с дизайном.
3. При необходимости добавить класс `.no‑focus-visible` к элементам, где визуальный фокус нежелателен (например, при клике мышью).
4. Тестировать в Chrome/Firefox с включённым `Tab`‑навигацией и в режимах высокой контрастности.
**SAFE CSS:**
```css
/* focus-visible‑outline – улучшение доступности */
a:focus-visible,
button:focus-visible,
[role="button"]:focus-visible,
.btn-primary:focus-visible {
outline: 3px solid var(--blue);
outline-offset: 2px;
border-radius: 4px;
}
/* Сброс стандартного outline, если нужен только кастомный */
a:focus,
button:focus,
[role="button"]:focus,
.btn-primary:focus {
outline: none;
}
/* Класс для отключения кастомного фокуса (опционально) */
.no-focus-visible:focus-visible {
outline: none;
}
```
**SAFE JS:** *(не требуется)*

## Когда применять
Улучшает восприятие сайта пользователями клавиатуры → повышает показатель Accessibility и потенциально конверсию за счёт снижения барьера выхода.

## Проверка
Открыть страницу, нажать `Tab` — виден новый синий контур на всех ссылках/кнопках; отключить стили в DevTools – визуальный стиль исчезает.

## SAFE CSS
```css
**
```css
/* focus-visible‑outline – улучшение доступности */
a:focus-visible,
```

## SAFE JS
```js
** *(не требуется)*
```
