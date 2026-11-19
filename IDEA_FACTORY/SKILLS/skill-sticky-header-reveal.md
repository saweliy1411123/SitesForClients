---
name: SKILL — sticky-header-reveal
source: localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct
round: 118
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — sticky-header-reveal


**Name:** sticky-header-reveal
**When to apply:** На лендингах с крупной hero-секцией и фиксированным верхним меню.
**SAFE CSS:**
```css
.sticky-header {
position: fixed;
top: 0;
left: 0;
width: 100%;
background-color: var(--bg);
box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
z-index: 1000;
transform: translateY(-100%);
transition: transform 0.3s ease-in-out;
}
.sticky-header.reveal {
transform: translateY(0);
}
.sticky-header nav {
display: flex;
justify-content: space-between;
align-items: center;
padding: 1rem;
}
.sticky-header nav a {
color: var(--text);
text-decoration: none;
transition: color 0.2s ease-in-out;
}
.sticky-header nav a:hover {
color: var(--link-hover);
}
```
**SAFE JS:**
```javascript
const header = document.querySelector('.sticky-header');
window.addEventListener('scroll', () => {
const scrollPosition = window.scrollY;
if (scrollPosition > 200) {
header.classList.add('reveal');
} else {
header.classList.remove('reveal');
}
});
```

## Когда применять
Улучшает навигацию и пользовательский опыт на лендингах с крупной hero-секцией и фиксированным верхним меню.

## Проверка
Проверить визуальное отображение и функциональность фиксированного меню на разных устройствах и разрешениях.
