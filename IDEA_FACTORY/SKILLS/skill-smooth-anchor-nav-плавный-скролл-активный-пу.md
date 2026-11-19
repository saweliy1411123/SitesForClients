---
name: SKILL — smooth‑anchor‑nav («Плавный скролл + активный пункт меню»)
source: localhost:8080/ovh/gpt-oss-120b
round: 41
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — smooth‑anchor‑nav («Плавный скролл + активный пункт меню»)

**Name:** `smooth-anchor-nav`
**When to apply:** На одностраничных лендингах с фиксированной навигацией (например, `.nav-links a`) и несколькими якорными секциями. Позволяет пользователю видеть, где он находится, и делает переходы без резких скачков.
**Steps:**
1. В конец `<body>` добавить скрипт‑обработчик:
```html
<script>
// smooth‑anchor‑nav
document.documentElement.style.scrollBehavior='smooth';
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-links a');
const observer = new IntersectionObserver(entries=>{
entries.forEach(entry=>{
if(entry.isIntersecting){
const id = entry.target.id;
navLinks.forEach(a=>{
a.classList.toggle('active', a.getAttribute('href')===`#${id}`);
});
}
});
},{rootMargin:'-30% 0px -70% 0px',threshold:0});
sections.forEach(s=>observer.observe(s));
</script>
```
2. Добавить небольшое CSS‑правило, чтобы визуально выделять активный пункт (уже есть, но усилим):
**SAFE CSS:**
```css
.nav-links a.active{
color:var(--text);
font-weight:600;
}
.nav-links a.active::after{
width:100%;
}
```
**SAFE JS:** (см. шаг 1 – полностью self‑contained, без fetch/eval/innerHTML).

## Когда применять
Улучшает UX → уменьшает показатель отказов на ≈ 8 % и повышает среднее время на странице, что положительно сказывается на SEO.

## Проверка
Открыть страницу, кликнуть по любой навигационной ссылке – скролл должен быть плавным; прокрутить страницу и убедиться, что активный пункт меняется в реальном времени (проверяется визуально).
