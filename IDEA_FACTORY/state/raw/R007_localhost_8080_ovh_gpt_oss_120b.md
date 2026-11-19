# localhost:8080/ovh/gpt-oss-120b  2026-11-17 02:00:25
duration=32.4 error=- attempts=1

IDEA: SKILL — Glassmorphism Card with 3D Tilt Hover  
KNOB: METHOD: Create reusable skill **glass-tilt-card**  
```markdown
# glass-tilt-card.md
## Название
Glassmorphism Card with 3D Tilt Hover

## Когда применять
Для визуально‑привлекательных блоков‑карточек (услуги, отзывы, демо‑концепты) на премиальном лендинге, где нужен лёгкий 3D‑эффект и «стеклянный» фон без тяжёлых библиотек.

## Шаги
1. Добавьте в HTML любой контейнер с классом `glass-card` и вложенный контент.
2. Подключите файл `glass-tilt-card.css` в `<head>`.
3. (Опционально) подключите `glass-tilt-card.js` в конце `<body>` для интерактивного наклона по курсору.
4. При необходимости переопределите переменные `--card-bg`, `--card-blur`, `--card-radius`.

## SAFE CSS:
```css
/* glass-tilt-card.css */
.glass-card {
  position: relative;
  padding: 1.5rem;
  border-radius: var(--card-radius, 12px);
  background: var(--card-bg, rgba(255,255,255,0.12));
  backdrop-filter: blur(var(--card-blur, 8px));
  box-shadow: 0 8px 32px rgba(0,0,0,0.12);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  transform-style: preserve-3d;
  perspective: 800px;
}
.glass-card::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: linear-gradient(135deg, rgba(255,255,255,0.25), rgba(255,255,255,0));
  pointer-events: none;
}
.glass-card:hover {
  transform: rotateX(4deg) rotateY(6deg) scale(1.02);
  box-shadow: 0 12px 48px rgba(0,0,0,0.2);
}
@media (prefers-reduced-motion: reduce) {
  .glass-card,
  .glass-card:hover {
    transition: none;
    transform: none;
  }
}
```

## SAFE JS:
```js
/* glass-tilt-card.js */
document.querySelectorAll('.glass-card').forEach(card => {
  const rect = () => card.getBoundingClientRect();
  const update = e => {
    const {width, height, left, top} = rect();
    const x = ((e.clientX - left) / width - 0.5) * 12;   // ±6deg
    const y = ((e.clientY - top) / height - 0.5) * -12; // ±6deg
    card.style.transform = `rotateX(${y}deg) rotateY(${x}deg) scale(1.02)`;
  };
  const reset = () => {
    card.style.transform = '';
  };
  card.addEventListener('mousemove', update);
  card.addEventListener('mouseleave', reset);
});
```
```  

EFFECT: Делает карточки визуально «премиальными», повышает время на странице и воспринимаемую ценность, стимулирует клик за счёт интерактивного отклика.  
RISK: Малый‑медленный JS‑цикл может слегка увеличить нагрузку на слабые устройства; пользователь с отключённым JS не получит 3D‑наклон (но останется статичный дизайн).  
ROLLBACK: `git rm src/skills/glass-tilt-card.css src/skills/glass-tilt-card.js && git checkout -- index.html` (удалить файлы и вернуть оригинал).  
VERIFY: Откройте страницу в браузере, наведите курсор на элемент с классом `glass-card` — должен появиться лёгкий наклон и блеск; включите `prefers-reduced-motion` в системе — анимация должна исчезнуть.  
PRIORITY: 2 — высокий визуальный эффект для премиального позиционирования, но требует небольших ресурсов, поэтому ставим средний приоритет.  
SKILL: glass-tilt-card  

---  

IDEA: SKILL — Premium Heading Reveal with Staggered Fade‑Scale  
KNOB: METHOD: Create reusable skill **premium-heading-reveal**  
```markdown
# premium-heading-reveal.md
## Название
Premium Heading Reveal with Staggered Fade‑Scale

## Когда применять
Для ключевых заголовков (h1, h2, h3) в hero‑секции и блоках‑преимуществ, где нужен эффект появления, подчеркивающий премиальность без JavaScript.

## Шаги
1. Добавьте к заголовкам класс `reveal-heading`.
2. Подключите файл `premium-heading-reveal.css` в `<head>`.
3. При необходимости задайте задержку через CSS‑переменную `--reveal-delay`.

## SAFE CSS:
```css
/* premium-heading-reveal.css */
.reveal-heading {
  opacity: 0;
  transform: translateY(20px) scale(0.96);
  animation: headingReveal 0.8s forwards ease-out;
}
.reveal-heading[data-index] {
  --reveal-delay: calc(var(--index, 0) * 0.12s);
  animation-delay: var(--reveal-delay);
}
@keyframes headingReveal {
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}
@media (prefers-reduced-motion: reduce) {
  .reveal-heading {
    animation: none;
    opacity: 1;
    transform: none;
  }
}
```

## SAFE JS: *(optional – only to auto‑assign data-index for sequential headings)*
```js
/* premium-heading-reveal.js */
document.querySelectorAll('.reveal-heading').forEach((el, i) => {
  el.dataset.index = i;
});
```
```  

EFFECT: Делает появление заголовков плавным и последовательным, усиливает восприятие «дорогого» дизайна, удерживает внимание пользователя в начале просмотра.  
RISK: При отключённом JavaScript некоторые заголовки могут не получить `data-index`, но анимация всё равно сработает без задержки; воздействие минимально.  
ROLLBACK: `git rm src/skills/premium-heading-reveal.css src/skills/premium-heading-reveal.js && git checkout -- index.html`.  
VERIFY: Откройте страницу, проверьте, что h1‑h3 появляются один за другим с лёгким подъёмом и увеличением; включите режим «reduce motion» — анимация должна исчезнуть, заголовки видны сразу.  
PRIORITY: 2 — улучшает восприятие премиального бренда, легко внедряется, не замедляет загрузку.  
SKILL: premium-heading-reveal
