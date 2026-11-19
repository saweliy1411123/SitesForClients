---
name: Typed‑out подзаголовок в hero‑секции
source: localhost:8081/big_only
round: 77
status: proposed
portable: true
tags: [static-landing, portable]
---

# Typed‑out подзаголовок в hero‑секции

**SKILL — hero-typed-subtitle**
**Name:** `hero-typed-subtitle`
**When to apply:** В hero‑блоке после `<p class="sub">`, где хочется добавить динамичность без тяжёлых библиотек.
**SAFE CSS:**
```css
.hero .typed-subtitle {
display:inline-block;
border-right:2px solid currentColor;
white-space:nowrap;
overflow:hidden;
font-family:inherit;
font-size:inherit;
animation: caret-blink 0.7s steps(1) infinite;
}
@keyframes caret-blink {
0%,100% { border-color:transparent; }
50% { border-color:currentColor; }
}
```
**SAFE JS:**
```js
(() => {
const txt = "Получите первых клиентов из Яндекса за 2 дня";
const el = document.querySelector('.hero .typed-subtitle');
if (!el) return;
let i = 0;
const interval = setInterval(() => {
el.textContent = txt.slice(0, ++i);
if (i === txt.length) clearInterval(interval);
}, 60);
})();
```

## Когда применять
Добавляет живой элемент, удерживает внимание, повышает воспринимаемую динамичность предложения.

## Проверка
Отключить JS в браузере → убедиться, что отображается статический fallback‑текст; включить → проверить корректность печати без задержек > 200 ms.
