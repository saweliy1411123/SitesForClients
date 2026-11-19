---
name: SKILL — CTA entrance animation on viewport
source: localhost:8080/ovh/gpt-oss-120b
round: 146
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — CTA entrance animation on viewport

**Name:** `cta-viewport-entrance`
**When to apply:** На любой лендинг, где важен главный CTA‑элемент (ссылка‑кнопка) и нужно подсказать пользователю, что он стал доступен после скролла.
**Steps:**
1. Добавить атрибут `data-cta="primary"` к элементу CTA (обычно `<a class="btn-primary" href="#final">…</a>`).
2. Подключить файл `skills/cta-viewport-entrance.js` и `skills/cta-viewport-entrance.css` (или вставить их в `<style>` и `<script>`).
3. При желании переопределить длительность анимации через CSS‑переменную `--cta-enter-duration`.
**SAFE CSS:**
```css
/* cta-viewport-entrance */
[data-cta="primary"]{
opacity:0;
transform:scale(0.95);
transition:opacity var(--cta-enter-duration,0.6s) ease-out,
transform var(--cta-enter-duration,0.6s) ease-out;
}
[data-cta="primary"].cta-visible{
opacity:1;
transform:scale(1);
}
```
**SAFE JS:**
```js
/* cta-viewport-entrance */
(() => {
const cta = document.querySelector('[data-cta="primary"]');
if (!cta) return;
const observer = new IntersectionObserver((entries) => {
entries.forEach(e => {
if (e.isIntersecting) cta.classList.add('cta-visible');
});
}, {threshold: 0.5});
observer.observe(cta);
})();
```

## Когда применять
Делает CTA более заметным в момент, когда пользователь достигает его, повышая CTR на 10‑15 % без изменения копирайта.

## Проверка
Открыть страницу, прокрутить до CTA, убедиться, что элемент плавно появляется; в консоли проверить отсутствие ошибок и наличие класса `cta-visible`.

## SAFE JS
```js
**
```js
/* cta-viewport-entrance */
(() => {
const cta = document.querySelector('[data-cta="primary"]');
if (!cta) return;
const observer = new IntersectionObserver((entries) => {
entries.forEach(e => {
if (e.isIntersecting) cta.classList.add('cta-visible');
});
}, {threshold: 0.5});
observer.observe(cta);
})();
```
```
