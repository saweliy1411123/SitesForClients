---
name: SKILL — scroll-reveal-fade-in
source: localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct
round: 132
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — scroll-reveal-fade-in


**Name:** scroll-reveal-fade-in
**When to apply:** На любом статическом лендинге, где есть секции с заголовками и текстом.
**Steps:**
1. Добавить класс `scroll-reveal` к каждой секции, которую нужно показывать при скролле.
2. Добавить CSS-правило `.scroll-reveal { opacity: 0; transition: opacity 0.5s; }`.
3. Добавить JS-код, который будет показывать секции при скролле.
SAFE CSS:
```css
.scroll-reveal {
opacity: 0;
transition: opacity 0.5s;
}
.scroll-reveal.visible {
opacity: 1;
}
```
SAFE JS:
```javascript
const scrollRevealElements = document.querySelectorAll('.scroll-reveal');
window.addEventListener('scroll', () => {
scrollRevealElements.forEach(element => {
const rect = element.getBoundingClientRect();
if (rect.top < window.innerHeight) {
element.classList.add('visible');
}
});
});
```

## Когда применять
Секции будут появляться при скролле, создавая эффект постепенного открытия контента.

## Проверка
Проверить, что секции появляются при скролле, и что эффект выглядит плавно и естественно.

## SAFE JS
```js
```javascript
const scrollRevealElements = document.querySelectorAll('.scroll-reveal');
window.addEventListener('scroll', () => {
scrollRevealElements.forEach(element => {
const rect = element.getBoundingClientRect();
if (rect.top < window.innerHeight) {
element.classList.add('visible');
}
});
});
```
```
