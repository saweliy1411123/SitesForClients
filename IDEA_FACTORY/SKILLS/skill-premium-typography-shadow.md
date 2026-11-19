---
name: SKILL — premium‑typography‑shadow
source: localhost:8080/ovh/gpt-oss-120b
round: 98
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — premium‑typography‑shadow

**NAME:** premium-typography-shadow
**WHEN TO APPLY:** На любом статическом лендинге, где нужен премиальный визуальный акцент заголовков (h1‑h3).
**STEPS:**
1. Добавить в `<head>` блок `<style id="skill-premium-typography">` (или отдельный файл).
2. Применить к заголовкам класс `typography‑premium`.
3. При желании включить переключатель «dark‑mode»‑совместимости через CSS‑переменные.
**SAFE CSS:**
```css
.typography-premium {
font-weight: 700;
letter-spacing: -0.02em;
text-shadow: 0 2px 4px rgba(0,0,0,0.15), 0 0 12px rgba(255,255,255,0.12);
background: linear-gradient(135deg, #8b5cf6 0%, #5a67d8 100%);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
}
@media (prefers-color-scheme: dark) {
.typography-premium {
text-shadow: 0 2px 4px rgba(0,0,0,0.45), 0 0 12px rgba(255,255,255,0.08);
}
}
```
**SAFE JS:** *(не требуется)*

## Когда применять
Повышает восприятие бренда как премиального, улучшает визуальный фокус на ключевых сообщениях → рост CTR на CTA‑кнопки.

## Проверка
Открыть страницу в Chrome, убедиться, что h1/h2/h3 теперь имеют градиентный текст и лёгкую тень; сравнить скриншот до/после.

## SAFE JS
```js
** *(не требуется)*
```
