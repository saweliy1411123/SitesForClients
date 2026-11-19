---
name: SKILL — variable‑font‑typography‑premium
source: localhost:8080/ovh/gpt-oss-120b
round: 140
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — variable‑font‑typography‑premium

**Name:** `variable-font-typography-premium`
**When to apply:** На любые заголовки h1‑h3 и ключевые блоки текста, где нужен плавный диапазон весов без загрузки нескольких файлов шрифтов.
**Steps:**
1. В `<head>` добавить `@font-face` для Manrope Variable (Google Fonts поддерживает `@font-face` с `font-variation-settings`).
2. Заменить текущие `font-weight` на `font-variation-settings: 'wght' <value>` через CSS‑переменные.
3. Использовать `clamp()` + `vw` для fluid‑typography, привязав к переменной `--fs-base`.
**SAFE CSS:**
```css
@font-face{
font-family:'Manrope';
src:url('https://fonts.gstatic.com/s/manrope/v13/1Ptug8zYS_SKggPNyC0ISg.woff2') format('woff2');
font-weight:100 900;
font-display:swap;
}
:root{
--fs-base:clamp(1rem,1.2vw,1.5rem);
}
h1,h2,h3{
font-family:'Manrope',sans-serif;
font-variation-settings:'wght' var(--weight,600);
font-size:var(--fs-base);
}
h1{--weight:800;}
h2{--weight:700;}
h3{--weight:600;}
```
**SAFE JS:** *(не требуется)*

## Когда применять
Сокращает количество запросов к шрифту, ускоряет рендер, а также даёт плавные переходы веса при интерактивных состояниях (например, при ховере — меняем `--weight`). Улучшает читаемость и ощущение «премиум‑типа».

## Проверка
Открыть DevTools → Computed → проверить, что `font-variation-settings` присутствует; переключить `--weight` в консоли и убедиться в плавном изменении толщины.

## SAFE JS
```js
** *(не требуется)*
```
