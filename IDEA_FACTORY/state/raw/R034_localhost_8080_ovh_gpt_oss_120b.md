# localhost:8080/ovh/gpt-oss-120b  2026-11-17 03:18:24
duration=25.9 error=- attempts=1

IDEA: SKILL — sr‑only utility class  
KNOB: **Name:** `sr-only`  
**When to apply:** На любой статический лендинг, где нужны скрытые от визуального восприятия, но читаемые скрин‑ридерами тексты (например, пояснения к иконкам, скрытые заголовки, aria‑labels).  
**Steps:**  
1. Добавить в файл `index.improved.html` (или отдельный CSS‑файл) блок ниже в секцию `<style>` или в подключённый CSS.  
2. Использовать класс `sr-only` в HTML‑разметке там, где требуется скрытый от глаз контент, но доступный для ассистивных технологий.  
**SAFE CSS:**  
```css
.sr-only {
  position: absolute !important;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}
```  
**SAFE JS:** *(не требуется)*  

EFFECT: Улучшает доступность (a11y) без визуального изменения дизайна, повышает SEO‑оценку за счёт корректных ARIA‑меток.  
RISK: Никакого — класс безопасен, не влияет на визуальный рендер.  
ROLLBACK: `git checkout -- index.improved.html` (или удалить строку с `.sr-only` из CSS).  
VERIFY: Открыть страницу, включить Chrome DevTools → Elements, проверить, что элемент с классом `sr-only` скрыт визуально, но виден в Accessibility tree. Быстро проверить, что скрин‑ридер (NVDA/VoiceOver) читает его.  
PRIORITY: 2 — важный для доступности, но не критичен для первой конверсии.  
SKILL: sr-only  

---  

IDEA: SKILL — scroll‑snap sections with navigation dots  
KNOB: **Name:** `scroll-snap-nav`  
**When to apply:** На одностраничных лендингах с несколькими вертикальными секциями, где нужен плавный переход между блоками и визуальная подсказка текущего положения (особенно на мобильных устройствах).  
**Steps:**  
1. В `<style>` добавить правила для контейнера `<body>` (или обёртки `<main>`) и секций.  
2. Добавить в конец `<body>` блок навигационных точек (`<nav class="snap-nav" aria-label="Навигация по секциям">…</nav>`).  
3. При желании подключить лёгкий JS‑скрипт, который будет обновлять активную точку при скролле.  
**SAFE CSS:**  
```css
/* Enable vertical scroll snapping */
html, body {
  height: 100%;
  scroll-behavior: smooth;
}
.main-scroll {
  scroll-snap-type: y mandatory;
  overflow-y: auto;
  height: 100vh;
}

/* Each section snaps */
.main-scroll > section {
  scroll-snap-align: start;
  min-height: 100vh;
}

/* Navigation dots */
.snap-nav {
  position: fixed;
  right: 1rem;
  top: 50%;
  transform: translateY(-50%);
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
  z-index: 1000;
}
.snap-nav a {
  width: 0.75rem;
  height: 0.75rem;
  background: #c3cad9;
  border-radius: 50%;
  display: block;
  transition: background 0.3s;
}
.snap-nav a.active,
.snap-nav a:hover {
  background: #8b5cf6;
}
```  
**SAFE JS:** (необязательно, но рекомендуется для подсветки активной точки)  
```js
document.addEventListener('DOMContentLoaded', () => {
  const sections = document.querySelectorAll('.main-scroll > section');
  const navLinks = document.querySelectorAll('.snap-nav a');

  const setActive = i => {
    navLinks.forEach((lnk, idx) => lnk.classList.toggle('active', idx === i));
  };

  const observer = new IntersectionObserver(
    entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const idx = [...sections].indexOf(entry.target);
          setActive(idx);
        }
      });
    },
    { root: null, threshold: 0.6 }
  );

  sections.forEach(sec => observer.observe(sec));
});
```  

EFFECT: Улучшает пользовательский опыт (UX) за счёт предсказуемого скроллинга, повышает вовлечённость и время на странице, упрощает навигацию без дополнительных кликов.  
RISK: Требует, чтобы все секции имели достаточную высоту (≥ 100 vh); на очень коротких экранах может возникнуть «залипание» – проверка нужна.  
ROLLBACK: Удалить блок `.main-scroll`‑правил и `<nav class="snap-nav">…</nav>`; вернуть оригинальный CSS (git checkout).  
VERIFY: Открыть страницу в мобильном режиме, прокручивать – секции должны «прилипать» к верхней границе; точки навигации меняют цвет в соответствии с текущей секцией. Проверить отсутствие горизонтального скролла.  
PRIORITY: 2 — повышает UX и конверсию, но не критично для SEO; реализуется быстро.  
SKILL: scroll-snap-nav
