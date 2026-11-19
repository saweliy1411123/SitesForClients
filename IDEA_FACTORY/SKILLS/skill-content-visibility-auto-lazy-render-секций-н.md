---
name: SKILL — content‑visibility‑auto (lazy‑render секций ниже фолда)
source: localhost:8080/ovh/gpt-oss-120b
round: 90
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — content‑visibility‑auto (lazy‑render секций ниже фолда)

**Name:** `content-visibility-auto`
**When to apply:** На любой одностраничный лендинг, где ниже‑фолд контент тяжёлый (текст, карточки, изображения) и нужен быстрый First Contentful Paint.
**Steps:**
1. Открыть `index.html` и добавить в конец `<style>` блок ниже существующего CSS.
2. Вставить CSS‑правило, которое включает `content-visibility: auto` для всех секций, кроме первой (hero) и навигации.
3. При желании задать `contain-intrinsic-size` – пример ≈ 600 px, чтобы браузер оставил место до загрузки.
**SAFE CSS:**
```css
/* ---------- content‑visibility‑auto ---------- */
section:not(.hero):not(.nav) {
content-visibility: auto;
contain-intrinsic-size: 600px;
}
```
**SAFE JS:** *(не требуется)*

## Когда применять
Уменьшает количество DOM‑элементов, отрисовываемых до скролла, тем самым сокращая LCP и CLS → быстрее загрузка, лучше Core Web Vitals, повышается конверсия на мобильных.

## Проверка
Открыть страницу в Chrome, открыть DevTools → Performance, выполнить скролл до нижних секций и убедиться, что их `content‑visibility` = `auto` (вкладка Elements → Computed). Затем измерить LCP до и после (можно через `PerformanceObserver` в консоли).

## SAFE CSS
```css
**
```css
/* ---------- content‑visibility‑auto ---------- */
```

## SAFE JS
```js
** *(не требуется)*
```
