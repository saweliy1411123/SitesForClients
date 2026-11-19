---
name: SKILL — Ambient hero blur background
source: localhost:8080/ovh/gpt-oss-120b
round: 146
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Ambient hero blur background

**Name:** `ambient-hero-blur`
**When to apply:** На любой лендинг, где в `<header class="hero">` используется градиентный фон и хочется добавить лёгкую, не‑дистрактивную анимацию без JavaScript.
**Steps:**
1. В `<head>` добавить ссылку на файл `skills/ambient-hero-blur.css` (или вставить содержимое в `<style>`).
2. В HTML‑разметке добавить класс `ambient-blur` к контейнеру hero: `<header class="hero ambient-blur" id="top">`.
3. При желании переопределить цвета в CSS‑переменных `--blur-color-1` / `--blur-color-2`.
**SAFE CSS:**
```css
/* ambient-hero-blur */
:root {
--blur-color-1: rgba(139,92,246,0.4);
--blur-color-2: rgba(76,201,240,0.4);
}
.ambient-blur::before,
.ambient-blur::after {
content:"";
position:absolute;
inset:0;
pointer-events:none;
background:radial-gradient(circle at 30% 30%, var(--blur-color-1), transparent 70%),
radial-gradient(circle at 70% 70%, var(--blur-color-2), transparent 70%);
filter:blur(80px);
opacity:0;
animation:ambientBlurFade 12s infinite ease-in-out;
}
.ambient-blur::after {
animation-delay:6s;
}
@keyframes ambientBlurFade{
0%,100%{opacity:0}
50%{opacity:1}
}
```
**SAFE JS:** *(не требуется)*

## Когда применять
Увеличивает визуальную привлекательность hero‑секции, удерживая внимание посетителя и снижая показатель bounce‑rate без дополнительного кода.

## Проверка
Открыть страницу в браузере, включить DevTools → Performance → записать 5 секунд; убедиться, что анимация видна и не появляется CLS‑спайк (Layout Shift < 0.1).

## SAFE JS
```js
** *(не требуется)*
```
