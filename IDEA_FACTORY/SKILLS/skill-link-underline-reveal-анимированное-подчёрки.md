---
name: SKILL — link‑underline‑reveal (анимированное подчёркивание ссылок‑CTA)
source: localhost:8080/ovh/gpt-oss-120b
round: 90
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — link‑underline‑reveal (анимированное подчёркивание ссылок‑CTA)

**Name:** `link-underline-reveal`
**When to apply:** На статических лендингах, где CTA‑ссылки оформлены как `<a class="btn-primary …">` и нужны визуальные подсказки при наведении/фокусе без JavaScript.
**Steps:**
1. В конец `<style>` добавить CSS‑правило, которое использует псевдо‑элемент `::after` для создания 2‑px линии, появляющейся слева‑направо.
2. Применить класс `underline-reveal` к любой ссылке‑CTA (например, добавить к существующим `btn-primary`).
**SAFE CSS:**
```css
/* ---------- link‑underline‑reveal ---------- */
.underline-reveal {
position: relative;
overflow: hidden;
}
.underline-reveal::after {
content: "";
position: absolute;
left: 0;
bottom: 0;
height: 2px;
width: 0;
background: var(--grad, #8b5cf6);
transition: width .25s ease;
}
.underline-reveal:hover::after,
.underline-reveal:focus-visible::after {
width: 100%;
}
```
**SAFE JS:** *(не требуется)*

## Когда применять
Делает интерактивные ссылки более заметными, усиливает ощущение «кликабельности», повышает коэффициент кликов (CTR) на CTA без добавления лишних элементов.

## Проверка
Открыть страницу, навести курсор и/или перейти клавишей Tab к ссылке‑CTA; убедиться, что подчеркивание анимировано от нуля до полной ширины. Проверить отсутствие смещения текста (должно оставаться на месте).

## SAFE JS
```js
** *(не требуется)*
```
