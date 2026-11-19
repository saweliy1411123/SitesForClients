---
name: SKILL — section-scroll-snap
source: localhost:8080/ovh/gpt-oss-120b
round: 139
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — section-scroll-snap

**Name:** section-scroll-snap
**When to apply:** На одностраничных лендингах с несколькими вертикальными секциями, где желателен «прокрутка‑привязка» (scroll‑snap) для создания плавного, контролируемого скроллинга на мобильных и десктоп‑устройствах.
**Steps:**
1. Обернуть все основные `<section>` в контейнер `<div class="snap-container">`.
2. Добавить каждому `<section>` класс `.snap-section`.
3. Включить глобальный `scroll-behavior: smooth;`.
4. Добавить CSS‑правила `SAFE CSS` (см. ниже).
5. Проверить, что ссылки‑якоря (например, в навигации) корректно скроллят к нужным секциям.
**SAFE CSS:**
```css
html{
scroll-behavior: smooth;
}
.snap-container{
overflow-y: auto;
height: 100vh;
scroll-snap-type: y mandatory;
}
.snap-section{
scroll-snap-align: start;
min-height: 100vh;
/* optional: keep existing padding/margin */
}
```

## Когда применять
Пользователи ощущают более «погружающий» опыт, легче воспринимают структуру страницы, снижается количество «потерянных» скроллов и повышается время, проведённое на странице.

## Проверка
В Chrome открыть страницу, включить мобильный режим, прокручивать мышью/трекпадом – каждая секция должна «прилипать» к верхней части окна; клик по навигационным ссылкам‑якорям должен плавно вести к секции без «прыжков».
