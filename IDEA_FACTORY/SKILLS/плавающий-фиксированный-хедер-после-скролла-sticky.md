---
name: Плавающий фиксированный хедер после скролла (sticky‑header‑reveal)
source: localhost:8081/big_only
round: 104
status: proposed
portable: true
tags: [static-landing, portable]
---

# Плавающий фиксированный хедер после скролла (sticky‑header‑reveal)

**SKILL — sticky-header-reveal**
**Name:** sticky-header-reveal
**When to apply:** На лендингах с крупным `<header class="hero">` и навигационными ссылками, где полезно сохранять доступ к меню при прокрутке.
**Steps:**
1. Добавить в `<body>` элемент `<header class="sticky-header">` с теми же навигационными ссылками, что в `.hero .nav-links`.
2. Вставить в `<head>` блок `<style>` с SAFE CSS (см. ниже).
3. Добавить лёгкий SAFE JS, который добавляет класс `.scrolled` к `body` при прокрутке > 80 px.
**SAFE CSS:**
```css
/* базовый скрытый хедер */
.sticky-header {
position: sticky;
top: 0;
left: 0;
right: 0;
display: flex;
justify-content: center;
align-items: center;
padding: 12px 0;
background: var(--bg);
box-shadow: 0 2px 8px rgba(0,0,0,.1);
opacity: 0;
transform: translateY(-100%);
transition: opacity .3s ease, transform .3s ease;
z-index: 1000;
}
/* видимый после скролла */
body.scrolled .sticky-header {
opacity: 1;
transform: translateY(0);
}
```
**SAFE JS:**
```js
// Добавляем/удаляем класс .scrolled на body при прокрутке
window.addEventListener('scroll',()=>{
if(window.scrollY>80) document.body.classList.add('scrolled');
else document.body.classList.remove('scrolled');
});
```

## Когда применять
Улучшает навигацию и удерживает пользовательский фокус на CTA‑ссылках, повышая вероятность перехода к важным секциям.

## Проверка
Прокрутить страницу вниз более чем на 80 px – верхний хедер должен плавно появиться. Проверить, что ссылки работают и не перекрываются другими элементами.
