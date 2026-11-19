---
name: SKILL — Safe Reveal on Scroll (IntersectionObserver)
source: localhost:8080/ovh/gpt-oss-120b
round: 27
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Safe Reveal on Scroll (IntersectionObserver)

**Name:** `safe-reveal-observer`
**When to apply:** Для любой статической одностраничной посадочной, где элементы появляются при прокрутке (класс `.reveal`). Позволяет избавиться от «всплывающих» сдвигов и ускорить рендеринг за счёт отложенной инициализации.
**Steps:**
1. Убедиться, что все анимируемые блоки имеют класс `reveal`.
2. Добавить в глобальный CSS базовые стили для скрытого состояния (см. ниже).
3. В конец `<body>` вставить скрипт `SAFE JS:` (см. ниже).
4. При необходимости добавить атрибут `data-delay` для кастомных задержек.
**SAFE CSS:**
```css
.reveal {
opacity: 0;
transform: translateY(20px);
transition: opacity .4s ease, transform .4s ease;
will-change: opacity, transform;
}
.reveal.visible {
opacity: 1;
transform: none;
}
```
**SAFE JS:**
```js
document.addEventListener('DOMContentLoaded', () => {
const targets = document.querySelectorAll('.reveal');
if (!('IntersectionObserver' in window)) {
// fallback: сразу показываем
targets.forEach(el => el.classList.add('visible'));
return;
}
const observer = new IntersectionObserver((entries, obs) => {
entries.forEach(entry => {
if (entry.isIntersecting) {
entry.target.classList.add('visible');
obs.unobserve(entry.target);
}
});
}, {threshold: 0.15});
targets.forEach(el => observer.observe(el));
});
```

## Когда применять
Уменьшает Cumulative Layout Shift (CLS) и делает анимацию плавной, улучшая Core Web Vitals и восприятие сайта пользователем.

## Проверка
Открыть страницу, включить DevTools → Performance → Layout Shift. Прокрутить страницу и убедиться, что CLS‑значение почти 0, а элементы плавно появятся.
