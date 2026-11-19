# localhost:8080/ovh/gpt-oss-120b  2026-11-17 09:24:26
duration=65.7 error=- attempts=1

IDEA: SKILL — Counter‑Up Animate  
KNOB: **Name:** `counter-up-animate`  
**When to apply:** На любой статический лендинг, где есть цифры‑статистики (например, «100+ проектов», «+30 % рост»), которые должны привлечь внимание при появлении в зоне видимости.  
**Steps:**  
1. В HTML‑разметке обернуть каждое число в элемент `<span class="counter" data-target="1234">0</span>`.  
2. Добавить файл `skills/counter-up-animate.css` и подключить его в `<head>` (или инлайн‑вставить в `index.improved.html`).  
3. Добавить файл `skills/counter-up-animate.js` и подключить его в конце `<body>` (defer).  
4. Скрипт создаёт `IntersectionObserver`, который при вхождении элемента в viewport запускает анимацию плавного увеличения от 0 до `data-target` за 1.5 с.  

**SAFE CSS:**  
```css
.counter {
  display: inline-block;
  font-variant-numeric: tabular-nums;
  font-weight: 600;
  color: var(--blue);
  transition: color .3s;
}
.counter[data-target]::after {
  content: '+';
  margin-left: .1em;
  opacity: .6;
}
```

**SAFE JS:**  
```js
document.addEventListener('DOMContentLoaded', () => {
  const counters = document.querySelectorAll('.counter[data-target]');
  const options = {threshold: 0.6};
  const animate = el => {
    const target = +el.dataset.target;
    const duration = 1500;
    const start = performance.now();
    const step = now => {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      el.textContent = Math.floor(progress * target);
      if (progress < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animate(entry.target);
        obs.unobserve(entry.target);
      }
    });
  }, options);
  counters.forEach(c => observer.observe(c));
});
```

RISK: Требует небольшого JavaScript‑кода; в случае отключения JS цифры останутся «0», но смысл блока не критичен.  
ROLLBACK: `git checkout -- skills/counter-up-animate.css skills/counter-up-animate.js index.improved.html` (или удалить добавленные файлы).  
VERIFY: Открыть страницу в браузере, прокрутить до блока со счётчиком, убедиться, что число плавно растёт от 0 до указанного значения; в консоли проверить отсутствие ошибок.  
PRIORITY: 1 — визуальный «wow‑эффект», усиливающий восприятие цифр и повышающий конверсию без изменения контента.  

---  

IDEA: SKILL — Testimonial Carousel (Vanilla)  
KNOB: **Name:** `testimonial-carousel`  
**When to apply:** На лендингах, где есть раздел отзывов/кейсов (в текущем сайте – секция «Отзывы и работы»), но без готовой карусели. Позволяет показать несколько отзывов в компактном виде, улучшая доверие и удерживая внимание.  
**Steps:**  
1. В HTML‑разметке заменить список отзывов на контейнер `<div class="testimonial-carousel" role="region" aria-label="Отзывы клиентов">` и вложить отдельные `<article class="testimonial">`‑элементы.  
2. Добавить файл `skills/testimonial-carousel.css` и подключить его.  
3. Добавить файл `skills/testimonial-carousel.js` (defer) – простой автопрокручивающий скрипт с поддержкой клавиатурной навигации (arrow‑keys) и `aria-live` для объявлений.  

**SAFE CSS:**  
```css
.testimonial-carousel {
  position: relative;
  overflow: hidden;
  max-width: 720px;
  margin: 0 auto;
}
.testimonial {
  min-width: 100%;
  box-sizing: border-box;
  padding: 1.5rem;
  opacity: 0;
  transition: opacity .4s ease;
}
.testimonial.active {
  opacity: 1;
}
.testimonial::before {
  content: "“";
  font-size: 3rem;
  line-height: 0;
  color: var(--muted);
  position: absolute;
  left: 1rem;
  top: .5rem;
}
.carousel-nav {
  position: absolute;
  inset: 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  pointer-events: none;
}
.carousel-nav button {
  pointer-events: all;
  background: var(--bg);
  border: none;
  border-radius: 50%;
  width: 2.4rem;
  height: 2.4rem;
  font-size: 1.2rem;
  color: var(--blue);
  cursor: pointer;
  transition: background .2s;
}
.carousel-nav button:hover { background: var(--muted); }
```

**SAFE JS:**  
```js
document.addEventListener('DOMContentLoaded', () => {
  const carousel = document.querySelector('.testimonial-carousel');
  if (!carousel) return;
  const items = carousel.querySelectorAll('.testimonial');
  let idx = 0;
  const show = i => {
    items.forEach((el, n) => el.classList.toggle('active', n === i));
    carousel.setAttribute('aria-live', 'polite');
  };
  const next = () => { idx = (idx + 1) % items.length; show(idx); };
  const prev = () => { idx = (idx - 1 + items.length) % items.length; show(idx); };
  // initial
  show(idx);
  // auto‑rotate
  const auto = setInterval(next, 8000);
  // navigation
  const nav = document.createElement('div');
  nav.className = 'carousel-nav';
  nav.innerHTML = `<button aria-label="Предыдущий отзыв" class="prev">&larr;</button>
                   <button aria-label="Следующий отзыв" class="next">&rarr;</button>`;
  carousel.appendChild(nav);
  nav.querySelector('.next').addEventListener('click', () => { clearInterval(auto); next(); });
  nav.querySelector('.prev').addEventListener('click', () => { clearInterval(auto); prev(); });
  // keyboard
  document.addEventListener('keydown', e => {
    if (e.key === 'ArrowRight') { clearInterval(auto); next(); }
    if (e.key === 'ArrowLeft')  { clearInterval(auto); prev(); }
  });
});
```

RISK: Добавляет небольшую JS‑нагрузку и требует корректной разметки; при отключённом JS отзывы будут просто отображаться в вертикальном списке, что не ухудшит доступность.  
ROLLBACK: `git checkout -- skills/testimonial-carousel.css skills/testimonial-carousel.js index.improved.html` (или удалить файлы и вернуть оригинальный блок отзывов).  
VERIFY: Открыть страницу, убедиться, что один отзыв виден, остальные скрыты; нажать стрелки и клавиши ←/→ – переключение работает; проверить, что в мобильном режиме отзывы адаптивно масштабируются.  
PRIORITY: 2 — повышает доверие через социальное доказательство, но не критично для ближайшего конверсийного улучшения.
