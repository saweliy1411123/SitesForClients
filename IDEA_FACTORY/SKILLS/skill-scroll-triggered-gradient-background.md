---
name: SKILL — Scroll-Triggered Gradient Background
source: localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct
round: 34
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Scroll-Triggered Gradient Background


### Название
scroll-triggered-gradient
### Когда применять
Любой лендинг с длинной прокруткой, где нужно улучшить визуальный интерес и выделить определенные секции.
### Шаги
1. Определить секции, где будет применяться градиент.
2. Добавить класс `scroll-gradient` к этим секциям.
3. В CSS добавить стили для `.scroll-gradient`.
### SAFE CSS:
```css
.scroll-gradient {
background-image: linear-gradient(to bottom, #8b5cf6, #6a44f4);
background-size: 100% 300px;
background-position: 0% 100%;
}
.scroll-gradient.show-gradient {
background-position: 0% 0%;
transition: background-position 1s ease-out;
}
```
### SAFE JS:
```javascript
const gradientSections = document.querySelectorAll('.scroll-gradient');
const observer = new IntersectionObserver((entries) => {
entries.forEach((entry) => {
if (entry.isIntersecting) {
entry.target.classList.add('show-gradient');
} else {
entry.target.classList.remove('show-gradient');
}
});
}, { threshold: 0.5 });
gradientSections.forEach((section) => {
observer.observe(section);
});
```

## Когда применять
Добавление градиентного фона к определенным секциям при прокрутке улучшает визуальный интерес и делает контент более привлекательным.

## Проверка
Проверить визуально, что градиент появляется при прокрутке к определенным секциям.
