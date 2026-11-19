---
name: SKILL — svg-accessibility-enhancer
source: localhost:8080/ovh/gpt-oss-120b
round: 118
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — svg-accessibility-enhancer

**Name:** svg-accessibility-enhancer
**When to apply:** На любой странице, где используются инлайн‑SVG‑иконки (как в текущем `index.html`). Делает SVG‑элементы доступными для скрин‑ридеров без изменения визуального вида.
**Steps:**
1. С помощью скрипта найти все `<svg>` в документе.
2. Если у SVG уже есть `<title>` / `<desc>` – добавить `role="img"` и `aria-labelledby="titleId descId"` (при отсутствии `id`‑ов – сгенерировать уникальные).
3. Если SVG используется только как декоративный (например, в фоне блока) – добавить `aria-hidden="true"` и `focusable="false"`.
4. При необходимости добавить атрибут `role="presentation"` для полностью декоративных элементов.
**SAFE CSS:** *(не требуется, стили уже заданы)*
**SAFE JS:**
```js
(() => {
const svgs = document.querySelectorAll('svg:not([role])');
svgs.forEach((svg, i) => {
const hasDesc = svg.querySelector('title,desc');
if (hasDesc) {
const title = svg.querySelector('title');
const desc = svg.querySelector('desc');
const titleId = title?.id || `svgTitle${i}`;
const descId = desc?.id || `svgDesc${i}`;
if (title && !title.id) title.id = titleId;
if (desc && !desc.id) desc.id = descId;
svg.setAttribute('role', 'img');
svg.setAttribute('aria-labelledby', `${titleId} ${descId}`.trim());
} else {
svg.setAttribute('aria-hidden', 'true');
svg.setAttribute('focusable', 'false');
}
});
})();
```

## Когда применять
Скрин‑ридеры объявляют смысловые иконки, улучшая WCAG AA/AAA‑соответствие и потенциально повышая SEO (структурированные данные учитывают доступный контент).

## Проверка
Открыть DevTools → Accessibility, выбрать любой SVG‑элемент – в “Accessibility Tree” должно отображаться “img” с соответствующим именем или “ignored” для декоративных; также проверить, что нет предупреждений axe (категория “ARIA”).

## SAFE CSS
```css
** *(не требуется, стили уже заданы)*
**SAFE JS:**
```js
(() => {
const svgs = document.querySelectorAll('svg:not([role])');
svgs.forEach((svg, i) => {
const hasDesc = svg.querySelector('title,desc');
if (hasDesc) {
const title = svg.querySelector('title');
const desc = svg.querySelector('desc');
const titleId = title?.id || `svgTitle${i}`;
const descId = desc?.id || `svgDesc${i}`;
if (title && !title.id) title.id = titleId;
if (desc && !desc.id) desc.id = descId;
svg.setAttribute('role', 'img');
svg.setAttribute('aria-labelledby', `${titleId} ${descId}`.trim());
} else {
svg.setAttribute('aria-hidden', 'true');
svg.setAttribute('focusable', 'false');
}
});
})();
```
```

## SAFE JS
```js
**
```js
(() => {
const svgs = document.querySelectorAll('svg:not([role])');
svgs.forEach((svg, i) => {
const hasDesc = svg.querySelector('title,desc');
if (hasDesc) {
const title = svg.querySelector('title');
const desc = svg.querySelector('desc');
const titleId = title?.id || `svgTitle${i}`;
const descId = desc?.id || `svgDesc${i}`;
if (title && !title.id) title.id = titleId;
if (desc && !desc.id) desc.id = descId;
svg.setAttribute('role', 'img');
svg.setAttribute('aria-labelledby', `${titleId} ${descId}`.trim());
} else {
svg.setAttribute('aria-hidden', 'true');
svg.setAttribute('focusable', 'false');
}
});
})();
```
```
