---
name: SKILL — frosted-hero-bg
source: localhost:8080/ovh/gpt-oss-120b
round: 35
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — frosted-hero-bg

METHOD: SKILL
**Name:** `frosted-hero-bg`
**When to apply:** Для секции hero, где нужен премиальный «стеклянный» фон, подчёркивающий главный оффер и CTA, без использования PNG‑изображений.
**Steps:**
1. Внутри `<header class="hero">` добавить элемент `<div class="hero-frost"></div>` сразу после контент‑обёртки.
2. Применить к нему `backdrop-filter: blur(12px) saturate(150%)` и полупрозрачный фон‑цвет.
3. Ограничить высоту/ширину элементом `inset: 0; position: absolute; z-index: -1;` чтобы покрывать весь hero.
4. Добавить fallback для браузеров без `backdrop-filter`: `background: rgba(10,10,15,0.85);`.
**SAFE CSS:**
```css
.hero {
position: relative;
overflow: hidden;
}
.hero-frost {
position: absolute;
inset: 0;
background: rgba(10,10,15,0.6);
backdrop-filter: blur(12px) saturate(150%);
-webkit-backdrop-filter: blur(12px) saturate(150%);
z-index: -1;
}
@supports not ((-webkit-backdrop-filter: blur(0)) or (backdrop-filter: blur(0))) {
.hero-frost { background: rgba(10,10,15,0.85); }
}
```
**SAFE JS:** *не требуется*

## Когда применять
Делает первый экран более «привлекательным» и современным, усиливает восприятие бренда как премиального, повышает читаемость текста на фоне динамичных слоёв.

## Проверка
Включить/выключить `backdrop-filter` в DevTools → CSS → toggle; убедиться, что текст остаётся контрастным, а FPS ≥ 55. Проверить в Chrome, Safari и Firefox.

## SAFE JS
```js
** *не требуется*
```
