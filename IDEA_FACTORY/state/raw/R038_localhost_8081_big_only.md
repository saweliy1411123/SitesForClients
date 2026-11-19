# localhost:8081/big_only  2026-11-17 03:29:27
duration=23.5 error=- attempts=1

IDEA: I-00130‑R1 Replace content‑visibility with IntersectionObserver‑lazy‑load for non‑critical sections  
KNOB: Add a small inline script at end of <body> that observes each `<section>` (except `.hero`) and adds class `in-view` when it enters the viewport; in CSS set `.section:not(.hero){opacity:0;transform:translateY(20px);transition:opacity .4s ease,transform .4s ease;} .section.in-view{opacity:1;transform:none;}` – content stays in DOM for SEO, becomes visible on scroll.  
EFFECT: Улучшает восприятие скорости (появление контента по мере прокрутки), снижает CLS и не скрывает контент от поисковых роботов.  
RISK: Добавляет ~200 Б JS (IntersectionObserver поддерживается в большинстве браузеров); при отключённом JS контент будет сразу виден (fallback).  
ROLLBACK: Удалить добавленный `<script>` и CSS‑правила; `git checkout index.html` откатит изменения.  
VERIFY: Открыть страницу, включить DevTools → Network, прокрутить вниз – новые секции должны появляться → проверить, что `view source` содержит весь HTML (SEO).  
PRIORITY: 2 – умеренный прирост скорости, низкий риск, легко откатывается.  

IDEA: I-00146‑R1 Заменить exit‑intent модальное окно на не‑интрузивный top‑banner CTA  
KNOB: Вставить перед основным контентом `<div class="top-banner" role="region" aria-label="Бесплатное демо"><span>Получите бесплатное демо сайта</span><a class="btn-primary" href="#contact">Заказать</a><button class="banner-close" aria-label="Закрыть баннер">✕</button></div>`; добавить CSS `position:sticky;top:0;background:var(--bg);padding:12px;display:flex;justify-content:space-between;align-items:center;z-index:1000;` и скрипт, скрывающий баннер по клику на кнопку закрытия.  
EFFECT: Повышает конверсию за счёт постоянного, но ненавязчивого призыва к действию, избегая темных паттернов и резких модальных прерываний.  
RISK: Возможен небольшой сдвиг контента при загрузке; резервировать место (margin‑top) чтобы избежать Layout Shift.  
ROLLBACK: Удалить вставленный HTML‑блок и связанные CSS/JS; `git checkout index.html`.  
VERIFY: Перезагрузить страницу, убедиться, что баннер отображается вверху, закрывается без остатка, и что основной контент не «прыгает» после закрытия.  
PRIORITY: 1 – высокий потенциал повышения конверсии при минимальном риске UX.
