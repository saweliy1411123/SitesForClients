---
name: SKILL — gradient‑text‑hero
source: localhost:8080/ovh/gpt-oss-120b
round: 97
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — gradient‑text‑hero

**Name:** `gradient-text-hero`
**When to apply:** На любой статический лендинг с крупным заголовком в hero‑секции, где нужен визуальный акцент без добавления изображений.
**Steps:**
1. Добавить класс `gradient-text` к элементу `<h1>` (или другому блоку, требующему акцента).
2. Включить CSS‑правило из `SAFE CSS` ниже в глобальный `<style>` либо в отдельный файл стилей.
3. При желании задать индивидуальный градиент через CSS‑переменную `--gradient`.
4. (Опционально) Добавить небольшую анимацию плавного смещения градиента через `SAFE CSS`.
**SAFE CSS:**
```css
/* gradient‑text‑hero */
.gradient-text {
--gradient: linear-gradient(90deg, #8b5cf6, #3b82f6, #10b981, #f59e0b);
background: var(--gradient);
-webkit-background-clip: text;
background-clip: text;
color: transparent;
display: inline-block;
animation: gradient-slide 8s linear infinite;
}
/* плавный сдвиг градиента */
@keyframes gradient-slide {
0%   { background-position: 0% 50%; }
50%  { background-position: 100% 50%; }
100% { background-position: 0% 50%; }
}
/* адаптивность – отключаем анимацию на слабых устройствах */
@media (prefers-reduced-motion: reduce) {
.gradient-text { animation: none; }
}
```
**SAFE JS:** *(необязательно – только если нужен контроль над включением/выключением анимации)*
```js
// отключить анимацию, если пользователь предпочитает reduced‑motion
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
document.querySelectorAll('.gradient-text').forEach(el => {
el.style.animation = 'none';
});
}
```

## Когда применять


## Проверка


## SAFE JS
```js
** *(необязательно – только если нужен контроль над включением/выключением анимации)*
```js
// отключить анимацию, если пользователь предпочитает reduced‑motion
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
document.querySelectorAll('.gradient-text').forEach(el => {
el.style.animation = 'none';
});
}
```
```
