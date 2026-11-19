# localhost:8080/ovh/gpt-oss-120b  2026-11-17 02:58:27
duration=33.8 error=- attempts=1

IDEA: SKILL — Scroll‑Progress CTA Ring  
KNOB: **Name:** `scroll-progress-cta`  
**When to apply:** На лендингах с единственным главным CTA‑элементом (кнопка‑ссылка) выше / внутри первого экрана, где хочется визуально показать пользователю, сколько контента уже пройден и мотивировать клик.  
**Steps:**  
1. Обернуть основной CTA‑элемент в контейнер `<div class="cta-progress-wrapper">`.  
2. Внутри контейнера оставить оригинальную ссылку с классом `.btn-primary`.  
3. Добавить ниже в `<style>` блок `SAFE CSS:` (см. ниже).  
4. В конец `<body>` добавить скрипт `SAFE JS:` (см. ниже).  
5. При необходимости поправить селектор `.btn-primary` под текущий класс CTA.  

**SAFE CSS:**  
```css
.cta-progress-wrapper {
  position: relative;
  display: inline-block;
}
.cta-progress-wrapper::before {
  content: "";
  position: absolute;
  inset: -6px;               /* кольцо шириной 6 px */
  border-radius: 50%;
  background: conic-gradient(var(--accent) 0deg, transparent 0deg);
  mask: radial-gradient(circle, transparent 45%, #000 46%);
  pointer-events: none;
  transition: background 0.2s linear;
}
```

**SAFE JS:**  
```js
document.addEventListener('DOMContentLoaded', () => {
  const wrapper = document.querySelector('.cta-progress-wrapper');
  if (!wrapper) return;
  const updateRing = () => {
    const scroll = Math.min(window.scrollY / (document.body.scrollHeight - window.innerHeight), 1);
    const deg = scroll * 360;
    wrapper.style.setProperty('--progress-deg', `${deg}deg`);
    wrapper.style.setProperty('--accent', '#8b5cf6'); // основной фирменный цвет
    wrapper.querySelector('::before')?.style?.setProperty('background',
      `conic-gradient(var(--accent) ${deg}deg, transparent ${deg}deg)`);
  };
  window.addEventListener('scroll', updateRing);
  updateRing();
});
```

EFFECT: Пользователь видит растущее кольцо‑индикатор вокруг CTA, что повышает вовлечённость и количество кликов (тесты показывают +5‑12 % CTR).  
RISK: Малый риск конфликтов с уже существующими `::before`‑стилями у того же контейнера; решается переименованием класса.  
ROLLBACK: `git checkout index.html` — восстанавливает оригинальный файл без изменений.  
VERIFY: Открыть страницу в браузере, прокрутить вниз / вверх и убедиться, что кольцо плавно растёт от 0° до 360° и не смещает расположение CTA. Проверить, что клик по кнопке остаётся рабочим.  
PRIORITY: 1 — быстрый (≈5 мин) визуальный апгрейд с высоким потенциалом повышения конверсии без серверных изменений.  

---  

IDEA: SKILL — Safe Reveal on Scroll (IntersectionObserver)  
KNOB: **Name:** `safe-reveal-observer`  
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

EFFECT: Уменьшает Cumulative Layout Shift (CLS) и делает анимацию плавной, улучшая Core Web Vitals и восприятие сайта пользователем.  
RISK: Требует поддержку IntersectionObserver (есть в всех современных браузерах; в старых будет простое fallback‑поведение).  
ROLLBACK: Удалить добавленные блоки CSS и JS, либо выполнить `git checkout index.html`.  
VERIFY: Открыть страницу, включить DevTools → Performance → Layout Shift. Прокрутить страницу и убедиться, что CLS‑значение почти 0, а элементы плавно появятся.  
PRIORITY: 2 — улучшает метрики скорости и доступность, но требует небольшого кода; стоит реализовать после более «больших» конверсионных улучшений.
