---
name: SKILL — Magnetic Button Effect (Hover‑Magnet)
source: localhost:8080/ovh/gpt-oss-120b
round: 13
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Magnetic Button Effect (Hover‑Magnet)

METHOD: Создать переносимый «магнитный» эффект для CTA‑кнопок, который слегка притягивает курсор к центру кнопки и возвращает её в исходное положение при уходе курсора. Файл `magnetic-button.css` + небольшой `magnetic-button.js` подключается одной строкой `<script src="magnetic-button.js" defer></script>` и классом `.magnetic` к любой ссылке/кнопке.
**Skill body (magnetic-button.md)**
```markdown
# Magnetic Button
## Когда применять
- Для CTA‑кнопок в hero‑секции, фиксированных панелей и любых ярких ссылок, где требуется визуальная «привлекательность» без ущерба производительности.
- На статических лендингах без сложных JS‑фреймворков.
## Шаги внедрения
1. Скопировать `magnetic-button.css` и `magnetic-button.js` в корень проекта.
2. В `<head>` добавить `<link rel="stylesheet" href="magnetic-button.css">`.
3. В конце `<body>` добавить `<script src="magnetic-button.js" defer></script>`.
4. Добавить класс `magnetic` к любой `<a>`/`<button>` элементу, который должен иметь эффект.
## SAFE CSS:
```css
/* Базовый стиль кнопки, сохраняет существующий .btn-primary */
.btn-primary.magnetic {
position: relative;
overflow: hidden;
transition: transform 0.2s ease-out;
}
/* Плавный переход при возврате */
.btn-primary.magnetic:hover {
transform: translate3d(0, 0, 0);
}
```
## SAFE JS:
```js
// Магнитный эффект без внешних библиотек, работает в современных браузерах
document.querySelectorAll('.magnetic').forEach(btn => {
const strength = 30; // пикселей отклонения
const rect = btn.getBoundingClientRect();
const move = e => {
const x = e.clientX - (rect.left + rect.width / 2);
const y = e.clientY - (rect.top + rect.height / 2);
const dx = (x / rect.width) * strength;
const dy = (y / rect.height) * strength;
btn.style.transform = `translate(${dx}px, ${dy}px)`;
};
const reset = () => {
btn.style.transform = 'translate(0,0)';
};
btn.addEventListener('mousemove', move);
btn.addEventListener('mouseleave', reset);
});
```

## Когда применять
Увеличивает визуальное вовлечение и воспринимаемую «интерактивность» кнопок, повышая CTR на CTA‑элементы без добавления тяжёлых библиотек.

## Проверка
Открыть страницу в Chrome, навести курсор на кнопку с классом `magnetic` – должна наблюдаться небольшая «притягивающая» анимация; протестировать на мобильном (должно работать без эффекта, т.к. `mousemove` не вызывается).

## SAFE JS
```js
```js
// Магнитный эффект без внешних библиотек, работает в современных браузерах
document.querySelectorAll('.magnetic').forEach(btn => {
const strength = 30; // пикселей отклонения
const rect = btn.getBoundingClientRect();
const move = e => {
const x = e.clientX - (rect.left + rect.width / 2);
const y = e.clientY - (rect.top + rect.height / 2);
const dx = (x / rect.width) * strength;
const dy = (y / rect.height) * strength;
btn.style.transform = `translate(${dx}px, ${dy}px)`;
};
const reset = () => {
btn.style.transform = 'translate(0,0)';
};
btn.addEventListener('mousemove', move);
btn.addEventListener('mouseleave', reset);
});
```
```
