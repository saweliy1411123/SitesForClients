---
name: SKILL — scroll-then-animate
source: localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct
round: 83
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — scroll-then-animate


**Name:** `scroll-then-animate`
**When to apply:** На любом статическом лендинге, где есть секции с анимацией, которые должны быть запущены при скролле.
**Safe CSS:**
```css
@keyframes slideIn {
from { transform: translateY(100px); }
to { transform: translateY(0); }
}
.scroll-then-animate {
animation: slideIn 0.5s ease-in-out;
opacity: 0;
transition: opacity 0.5s;
}
.scroll-then-animate.show {
opacity: 1;
animation: slideIn 0.5s ease-in-out;
}
```
**Safe JS:**
```javascript
const elements = document.querySelectorAll('.scroll-then-animate');
const observer = new IntersectionObserver((entries) => {
entries.forEach((entry) => {
if (entry.isIntersecting) {
entry.target.classList.add('show');
}
});
}, { threshold: 0.5 });
elements.forEach((element) => {
observer.observe(element);
});
```

## Когда применять


## Проверка
Проверить за 2–10 минут до внесения, открыв index.html в Chrome → F12 → Elements → найдя секции с анимацией, проверить, запускаются ли они при скролле.

## SAFE JS
```js
**
```javascript
const elements = document.querySelectorAll('.scroll-then-animate');
const observer = new IntersectionObserver((entries) => {
entries.forEach((entry) => {
if (entry.isIntersecting) {
entry.target.classList.add('show');
}
});
}, { threshold: 0.5 });
elements.forEach((element) => {
observer.observe(element);
});
```
```
