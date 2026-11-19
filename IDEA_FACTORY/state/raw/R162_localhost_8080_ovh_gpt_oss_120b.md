# localhost:8080/ovh/gpt-oss-120b  2026-11-17 09:29:29
duration=33.8 error=- attempts=1

IDEA: Добавить чёткий подзаголовок‑преимущество под h1 в hero‑секции  
KNOB: В `<header class="hero">` сразу после `<h1 class="reveal">…</h1>` вставить `<p class="hero-subtitle">Готовый сайт за 2 дня + полная SEO‑оптимизация под Яндекс</p>` и в CSS добавить `.hero-subtitle{font-size:clamp(18px,3vw,22px);color:#e5e7eb;margin-top:12px;max-width:560px}`  
EFFECT: Ускорит понимание оффера при первом взгляде, повышая конверсию первой CTA‑кнопки  
RISK: Требует согласования нового текста с владельцем бренда  
ROLLBACK: `git checkout -- index.html` (или удалить добавленные строки)  
VERIFY: Открыть страницу в браузере, убедиться, что под заголовком появился подзаголовок, что он виден на всех брейкпоинтах, и что высота hero‑секции не ломает позицию CTA  
PRIORITY: 1 — самый быстрый способ увеличить ясность предложения без технических рисков  

IDEA: Добавить визуальный «Гарантия возврата денег 100 %» рядом с ценой  
KNOB: Внутри `.price-card` после блока `<div class="price-fine">…</div>` добавить `<div class="guarantee-badge" role="img" aria-label="Гарантия возврата денег 100%">✅ Гарантия возврата 100 %</div>` и в CSS добавить `.guarantee-badge{margin-top:12px;padding:8px 12px;background:linear-gradient(90deg,#34d399,#10b981);color:#fff;border-radius:6px;font-weight:600;font-size:14px;text-align:center}`  
EFFECT: Усилит доверие к цене, уменьшит страх перед покупкой, повысит коэффициент конверсии в блоке цены  
RISK: Нужно убедиться, что действительно предоставляется такая гарантия; иначе риск юридический  
ROLLBACK: `git checkout -- index.html` (удалить добавленный div и CSS)  
VERIFY: Проверить в браузере, что рядом с ценой появился зелёный бейдж, и что он корректно отображается на мобильных устройствах (тестировать в DevTools)  
PRIORITY: 2 — значимый trust‑сигнал, но требует согласования юридической части  

IDEA: Добавить секцию «Кейсы клиентов» с карточками‑примерами и микроданными Schema.org CreativeWork  
KNOB: После секции цены (`</section>` с id="price") вставить новую секцию `<section id="cases" class="cases"><h2 class="reveal">Кейсы наших клиентов</h2><div class="case-grid">…</div></section>`; каждая карточка: `<article class="case-card" itemscope itemtype="https://schema.org/CreativeWork"><h3 itemprop="name">Сайт для ресторана «Вкусно»</h3><p itemprop="description">Увеличили заявки на 30 % за месяц</p><a href="#" class="btn-primary" itemprop="url">Посмотреть демо</a></article>`; добавить базовый CSS `.cases{padding:80px 0;background:#f9fafb}.case-grid{display:grid;gap:24px;grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}.case-card{background:#fff;padding:24px;border-radius:8px;box-shadow:0 4px 12px rgba(0,0,0,.05)}`  
EFFECT: Предоставит социальное доказательство через реальные проекты, улучшит SEO через структурированные данные и повысит доверие потенциальных клиентов  
RISK: Нужно подготовить реальные кейсы и ссылки; без них карточки могут выглядеть пустыми — риск потери доверия  
ROLLBACK: `git checkout -- index.html` (удалить секцию и CSS‑правила)  
VERIFY: Открыть страницу, убедиться, что секция «Кейсы» появляется после цены, карточки отображаются в сетке, ссылки кликабельны, и в консоли `view source` присутствуют микроданные `itemscope`/`itemtype`  
PRIORITY: 3 — высокий потенциал доверия, но требует контент‑подготовки и тестирования.
