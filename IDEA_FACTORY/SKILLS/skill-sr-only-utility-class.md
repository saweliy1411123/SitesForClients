---
name: SKILL — sr‑only utility class
source: localhost:8080/ovh/gpt-oss-120b
round: 34
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — sr‑only utility class

**Name:** `sr-only`
**When to apply:** На любой статический лендинг, где нужны скрытые от визуального восприятия, но читаемые скрин‑ридерами тексты (например, пояснения к иконкам, скрытые заголовки, aria‑labels).
**Steps:**
1. Добавить в файл `index.improved.html` (или отдельный CSS‑файл) блок ниже в секцию `<style>` или в подключённый CSS.
2. Использовать класс `sr-only` в HTML‑разметке там, где требуется скрытый от глаз контент, но доступный для ассистивных технологий.
**SAFE CSS:**
```css
.sr-only {
position: absolute !important;
width: 1px;
height: 1px;
padding: 0;
margin: -1px;
overflow: hidden;
clip: rect(0, 0, 0, 0);
white-space: nowrap;
border: 0;
}
```
**SAFE JS:** *(не требуется)*

## Когда применять
Улучшает доступность (a11y) без визуального изменения дизайна, повышает SEO‑оценку за счёт корректных ARIA‑меток.

## Проверка
Открыть страницу, включить Chrome DevTools → Elements, проверить, что элемент с классом `sr-only` скрыт визуально, но виден в Accessibility tree. Быстро проверить, что скрин‑ридер (NVDA/VoiceOver) читает его.

## SAFE JS
```js
** *(не требуется)*
```
