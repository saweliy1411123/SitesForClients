---
name: scroll-reveal-fade-in
source: localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct
round: 146
status: proposed
portable: true
tags: [static-landing, portable]
---

# scroll-reveal-fade-in


**Name:** scroll-reveal-fade-in
**When to apply:** На любом статическом лендинге, где есть секции с информацией.
**SAFE CSS:**
```css
.scroll-reveal {
opacity: 0;
transition: opacity 0.5s;
}
.scroll-reveal.revealed {
opacity: 1;
}
```
**SAFE JS:**
```javascript
const sections = document.querySelectorAll('.section');
const options = {
threshold: 0.5
};
const observer = new IntersectionObserver((entries) => {
entries.forEach((entry) => {
if (entry.isIntersecting) {
entry.target.classList.add('revealed');
}
});
}, options);
sections.forEach((section) => {
observer.observe(section);
});
```

## Когда применять
Повышение читаемости и вовлеченности пользователя за счет плавного появления секций при скролле.

## Проверка
Проверить за 2–10 минут, просматривая страницу и наблюдая за эффектом появления секций.
