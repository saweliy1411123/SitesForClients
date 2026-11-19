---
name: Переключатель темы (light / dark) через CSS‑переменные
source: localhost:8081/big_only
round: 97
status: proposed
portable: true
tags: [static-landing, portable]
---

# Переключатель темы (light / dark) через CSS‑переменные

SKILL:
**Name:** `theme-switcher-css-variable`
**When to apply:** На любой статический лендинг, где уже реализована поддержка светлой и тёмной темы (см. `@media (prefers-color-scheme: dark)`), но нужен ручной пользовательский переключатель.
**Steps:**
1. В `<header>` (или рядом с навигацией) добавить кнопку‑переключатель:
```html
<button class="theme-toggle" aria-label="Переключить тему">🌓</button>
```
2. В `<style>` объявить набор CSS‑переменных для обеих тем и правило, которое их применяет в зависимости от атрибута `data-theme` у `<html>`.
3. В конец `<body>` добавить небольшой скрипт, меняющий атрибут `data-theme` при клике.
**SAFE CSS:**
```css
:root{
--bg:#fff;
--text:#0a0a0f;
--accent:#8b5cf6;
}
[data-theme="dark"]{
--bg:#111;
--text:#e8eaf2;
--accent:#c084fc;
}
body{
background:var(--bg);
color:var(--text);
}
.theme-toggle{
background:none;
border:none;
cursor:pointer;
font-size:1.4rem;
padding:0.4rem;
}
```
**SAFE JS:**
```js
(function(){
const btn=document.querySelector('.theme-toggle');
if(!btn) return;
btn.addEventListener('click',()=>{
const html=document.documentElement;
const cur=html.getAttribute('data-theme')||'light';
html.setAttribute('data-theme', cur==='dark'?'light':'dark');
});
})();
```

## Когда применять
Пользователь может явно выбрать предпочтительную цветовую схему, повышается удобство и удовлетворённость → потенциальный рост времени на сайте и SEO‑оценки (повышенный показатель Core Web Vitals).

## Проверка
Открыть страницу, кликнуть кнопку – фон и цвета текста должны переключаться между светлой и тёмной схемой; проверить, что в `<html>` меняется атрибут `data-theme`.

## SAFE JS
```js
**
```js
(function(){
const btn=document.querySelector('.theme-toggle');
if(!btn) return;
btn.addEventListener('click',()=>{
const html=document.documentElement;
const cur=html.getAttribute('data-theme')||'light';
html.setAttribute('data-theme', cur==='dark'?'light':'dark');
});
})();
```
```
