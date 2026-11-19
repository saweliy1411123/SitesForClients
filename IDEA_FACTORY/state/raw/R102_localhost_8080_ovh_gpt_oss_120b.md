# localhost:8080/ovh/gpt-oss-120b  2026-11-17 06:41:01
duration=21.7 error=- attempts=1

IDEA: HERO‑LIVE‑LEADS‑COUNTER  
KNOB: В `<header class="hero">` добавить `<div class="lead-counter" aria-live="polite"></div>`; в `<script>` внизу страницы добавить JS, которое при появлении секции в viewport (IntersectionObserver) стартует счёт‑ап до числа ≈ 120 (примерное количество лидов за месяц) с `data-target="120"` и анимацией 1.5 с.  
EFFECT: Демонстрирует конкретный результат работы, повышает доверие и усиливает «социальное доказательство», стимулируя клик по CTA.  
RISK: Небольшой рост JS‑веса (≈ 1 KB) и возможный конфликт, если уже есть глобальный `IntersectionObserver`.  
ROLLBACK: `git checkout HEAD -- index.html` (откатить файл).  
VERIFY: Открыть страницу, прокрутить до hero, убедиться, что цифра плавно считает до 120 и обновляется в `aria-live`. Проверить, что скриншот в DevTools показывает правильный HTML‑элемент.  
PRIORITY: 2 – высокий эффект для первого экрана, но небольшие риски и лёгкая проверка.  
SITE_REQUEST: «counter»

---

IDEA: PAIN‑COLLAPSIBLE‑COST‑OF‑INACTION  
KNOB: В секции боли (идентификатор, вероятно `#pain`) добавить кнопку `<button class="cost-toggle" aria-expanded="false" aria-controls="cost-details">Показать стоимость бездействия</button>` и скрытый блок `<div id="cost-details" class="cost-details" hidden>…текст‑расчёт потерь…</div>`; в CSS добавить `.cost-details[hidden]{display:none}` и простую JS‑тоггл‑handler (без fetch).  
EFFECT: Позволяет пользователю раскрыть конкретные цифры потерь, усиливая мотивацию к действию, но без перегрузки страницы.  
RISK: Добавление интерактивного элемента требует проверки доступности (keyboard).  
ROLLBACK: `git checkout HEAD -- index.html`.  
VERIFY: Нажать кнопку – блок появляется/скрывается, атрибут `aria-expanded` меняется, проверка в Chrome DevTools → Accessibility.  
PRIORITY: 2 – улучшает конверсию в блоке боли, простой код.

---

IDEA: DEMO‑SCROLL‑SNAP‑CAROUSEL  
KNOB: В секции демо‑концептов (около L589) обернуть текущие концепты в `<div class="demo-carousel" role="region" aria-label="Демо‑концепты">`; добавить CSS `display:flex; overflow-x:auto; scroll-snap-type:x mandatory;` и каждому элементу класс `demo-card` с `scroll-snap-align:center; min-width:80%; margin-right:1rem;`. Добавить небольшую подсказку‑стрелку в виде `::after` для индикации прокрутки.  
EFFECT: Интерактивный просмотр демо‑концептов без JavaScript, повышает вовлечённость и удержание внимания.  
RISK: На старых браузерах (IE) scroll‑snap не поддерживается – будет обычный скролл.  
ROLLBACK: `git checkout HEAD -- index.html`.  
VERIFY: Открыть страницу, попытаться прокрутить секцию демо мышью/тапом – карточки «прилипают» к центру, проверка в DevTools → Styles.  
PRIORITY: 1 – значительный UX‑бонус при минимальном коде, легко измеряется через скролл‑тест.

---

IDEA: PRICE‑TOOLTIP‑BREAKDOWN  
KNOB: В `.price-card .price` добавить атрибут `data-tip="Включает разработку, хостинг на 1 год, базовую SEO‑оптимизацию"`; в CSS добавить `.price[data-tip]{position:relative; cursor:pointer;}` и `::after{content:attr(data-tip); position:absolute; bottom:120%; left:50%; transform:translateX(-50%); background:#222; color:#fff; padding:6px 10px; border-radius:4px; font-size:12px; white-space:nowrap; opacity:0; transition:opacity .2s; pointer-events:none;}` + `:hover::after{opacity:1;}`.  
EFFECT: Пользователь мгновенно видит, за что платит, снижает фрустрацию и повышает доверие к цене.  
RISK: Текст тултипа может быть слишком длинным на мобильных экранах – будет обрезаться.  
ROLLBACK: `git checkout HEAD -- index.html`.  
VERIFY: Навести курсор на цену – появится подсказка, проверить в мобильном режиме (DevTools → Toggle device toolbar).  
PRIORITY: 2 – небольшие правки, но повышают прозрачность оффера.

---

IDEA: FAQ‑VOICE‑READ‑OUT  
KNOB: В каждом элементе FAQ (например, `<div class="faq-item">`) добавить кнопку `<button class="faq-read" aria-label="Прослушать ответ">🔊</button>`; в `<script>` добавить обработчик, который берёт текст соседнего `.answer` и воспроизводит через `window.speechSynthesis.speak(new SpeechSynthesisUtterance(text))`.  
EFFECT: Доступность для пользователей с ограниченным зрением, повышает время взаимодействия и SEO‑оценку за счёт улучшенной семантики.  
RISK: На некоторых браузерах (Safari) SpeechSynthesis может требовать пользовательского взаимодействия; кнопка решает это, но может не работать в старых браузерах.  
ROLLBACK: `git checkout HEAD -- index.html`.  
VERIFY: Нажать кнопку – услышать озвучивание текста ответа, проверка в консоли отсутствия ошибок.  
PRIORITY: 3 – полезно для a11y, но эффект на конверсию менее очевиден; реализуемо без сторонних сервисов.
