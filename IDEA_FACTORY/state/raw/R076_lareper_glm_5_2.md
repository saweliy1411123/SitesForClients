# lareper/glm-5.2  2026-11-17 05:22:41
duration=36.5 error=- attempts=1

IDEA: SKILL — sticky-thumb-cta (мобильная закреплённая CTA с safe-area и авто-скрытием у финального блока)
KNOB: Название: `sticky-thumb-cta`. Когда применять: на любом статическом лендинге, где главный CTA — якорная ссылка, а конверсия теряется на мобильных (CTA только вверху и в конце длинной страницы). Шаги: (1) В конец `<body>` добавить `<a class="sticky-cta" href="#contact">Получить демо бесплатно</a>` (якорь заменить на реальный id финальной секции). (2) Вставить SAFE CSS. (3) По желанию — SAFE JS, чтобы кнопка скрывалась, когда финальный CTA уже виден. (4) Проверить на 360px, что кнопка не перекрывает контент.
SAFE CSS:
.sticky-cta{position:fixed;left:16px;right:16px;bottom:calc(12px + env(safe-area-inset-bottom));z-index:999;display:flex;justify-content:center;align-items:center;padding:15px 20px;border-radius:14px;background:linear-gradient(135deg,#8b5cf6,#6d4aff);color:#fff;font-weight:700;font-size:16px;text-decoration:none;box-shadow:0 10px 30px rgba(139,92,246,.45);transform:translateY(0);transition:transform .3s ease,opacity .3s ease}
.sticky-cta:hover,.sticky-cta:focus-visible{transform:translateY(-2px);box-shadow:0 14px 40px rgba(139,92,246,.6)}
.sticky-cta.is-hidden{transform:translateY(120%);opacity:0;pointer-events:none}
@media (min-width:900px){.sticky-cta{left:auto;right:24px;bottom:24px;padding:13px 22px;border-radius:999px}}
@media (prefers-reduced-motion: reduce){.sticky-cta{transition:none}}
SAFE JS:
(function(){var cta=document.querySelector('.sticky-cta');var final=document.querySelector('#contact');if(!cta||!final)return;if(!('IntersectionObserver' in window))return;new IntersectionObserver(function(e){cta.classList.toggle('is-hidden',e[0].isIntersecting)},{threshold:0.2}).observe(final);})();
EFFECT: CTA всегда под большим пальцем на мобильных — меньше потери пользователей на длинном скролле, рост переходов к заявке; на десктопе — компактная круглая кнопка, не мешает.
RISK: Может перекрыть нижний контент/футер на маленьких экранах — нужен отступ и проверка на 360px.
ROLLBACK: git checkout -- index.improved.html (или удалить блок `.sticky-cta` и CSS).
VERIFY: (1) Скопировать файл, вставить блок, открыть в Chrome. (2) Toggle device toolbar → 360px: кнопка видна, скролл до финального CTA — кнопка исчезает (JS) или перекрытие отсутствует. (3) Tab: фокус-кольцо на кнопке видно. (4) Вернуться: git checkout.
PRIORITY: 1 — прямой эффект на конверсию мобильного трафика (а он основной, судя по тексту сайта), минимальный риск.
SITE_REQUEST: contact

IDEA: SKILL — faq-details-a11y (нативный аккордеон FAQ на `<details>` без JS)
KNOB: Название: `faq-details-a11y`. Когда применять: на любом лендинге, где FAQ сделан на div/h3 + JS-переключателях или скрытых параграфах — замена даёт нативную доступность, клавиатуру и SEO-дружелюбность без единой строки JS. Шаги: (1) Найти секцию FAQ (на этом сайте `#faq`, L663–705). (2) Каждый вопрос перепис
