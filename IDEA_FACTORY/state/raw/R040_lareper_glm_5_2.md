# lareper/glm-5.2  2026-11-17 03:35:51
duration=75.0 error=- attempts=1

IDEA: Проверка hreflang/robots/sitemap-готовности и «паразитных» внешних ссылок в head
KNOB: METHOD: (1) Открыть index.html, DevTools → Console, выполнить: `console.log([...document.querySelectorAll('link[rel], meta[name], meta[property]')].map(e=>e.rel||e.name||e.getAttribute('property')+' → '+(e.href||e.content)))`. (2) Сверить наличие: canonical (есть ли реальный домен у владельца), robots meta, favicon/apple-touch-icon. (3) Проверить, что 4 `<link>` — это только preconnect/fonts, без случайных внешних ссылок. (4) Если canonical ещё нет (I-00165 в куче) — зафиксировать, что нужен реальный домен от владельца, не example.com.
EFFECT: Полная картина head-тегов за 2 минуты; исключает публикацию с битым/заглушечным canonical и подтверждает готовность к индексации.
RISK: Низкий — только чтение, ничего не меняется.
ROLLBACK: Не требуется (read-only проверка).
VERIFY: Сама проверка занимает ~2 минуты; результат — чек-лист из 5 пунктов (canonical/robots/favicon/og:image/лишние link).
PRIORITY: 2 — быстрая диагностика перед любыми SEO-правками, предотвращает публикацию заглушек.
SITE_REQUEST: link

IDEA: Мобильный тест «первый экран без скролла = оффер + CTA» на 360px
KNOB: METHOD: (1) Открыть index.html в DevTools → device toolbar → ширина 360px (Galaxy S8/Android Go — самый узкий реальный сценарий). (2) Сделать скриншот viewport (Ctrl+Shift+P → «Capture screenshot»), НЕ скролля. (3) Проверить по чек-листу: виден ли h1 целиком, видна ли кнопка CTA (L462) или sticky-cta (L409), не перекрывает ли sticky-cta контент hero, читается ли `.hero-note` (L465). (4) Повторить на 320px (iPhone SE 1st gen) — минимальная поддерживаемая ширина.
EFFECT: Гарантия, что на самых узких устройствах первый экран продаёт без взаимодействия; ловит перекрытия sticky-CTA и обрезку h1, невидимые на 375px.
RISK: Низкий — только визуальная проверка.
ROLLBACK: Не требуется.
VERIFY: 2 скриншота + чек-лист из 5 пунктов, ~4 минуты.
PRIORITY: 1 — мобильный трафик основной для локального бизнеса, а 320–360px часто пропускают при тестах на 375px.

IDEA: Аудит якорных ссылок на несуществующие id (битые навигации)
KNOB: METHOD: (1) В консоли на живой странице выполнить: `[...document.querySelectorAll('a[href^="#"]')].filter(a=>!document.getElementById(a.hash.slice(1))).map(a=>a.href+' | text: '+a.textContent.trim())` — пустой массив = все якоря валидны. (2) Отдельно проверить `#contact` (цель всех CTA), `#faq` (L442), `#top` (L449). (3) Убедиться, что у целевых секций есть `tabindex="-1"` для корректного фокуса при переходе с клавиатуры — если нет, пометить как задачу.
EFFECT: Ловит битые якоря (молчаливо ломают конверсию — клик «успешен», но ничего не происходит) и закрывает a11y-пробел фокуса на секциях.
RISK: Низкий — read-only.
ROLLBACK: Не требуется.
VERIFY: Одна команда в консоли, ~2 минуты.
P
