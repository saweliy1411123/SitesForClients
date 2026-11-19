# lareper/glm-5.3-prime  2026-11-17 06:45:37
duration=10.0 error=- attempts=2

IDEA: robots.txt + sitemap.xml для индексации лендинга
KNOB: создать в корне репозитория `robots.txt` (Allow all, `Sitemap: <URL>/sitemap.xml`) и `sitemap.xml` с одним `<url>` для `/index.html` (loc, lastmod, priority 1.0). Файл index.html не трогаем.
EFFECT: Яндекс/Google гарантированно находят и обходят страницу; корректный lastmod ускоряет переобход после правок.
RISK: без публичного домена URL в sitemap будут фиктивными — требует решения владельца (реальный адрес сайта).
ROLLBACK: `del robots.txt sitemap.xml` (файлы новые, index.html не изменён).
VERIFY: 2 минуты — открыть robots.txt/sitemap.xml в браузере, проверить валидность XML (Яндекс Вебмастер → «Проверка robots/sitemap», без деплоя — локально глазами).
PRIORITY: 2 — базовый SEO-фундамент, но эффект только при публикации на домене.

IDEA: Service JSON-LD с реальными данными оффера (дополнение к LocalBusiness)
KNOB: в `<head>` рядом с уже запланированным LocalBusiness (I-00613) добавить второй блок `<script type="application/ld+json">` с `@type: Service`, `serviceType: "Разработка лендингов"`, `areaServed: "Пермь"`, `offers.priceSpecification` — только цифры и факты, которые реально есть на странице (цена из секции #price, срок «2 дня»).
EFFECT: расширенные сниппеты в Яндексе (услуга + цена + город), рост CTR из поиска без изменения видимого контента.
RISK: расхождение разметки с фактическим текстом страницы — поисковый фильтр за структурированный спам.
ROLLBACK: `git checkout -- index.html` (правка только в index.improved.html).
VERIFY: 3 минуты — вставить JSON-LD в validator.schema.org и в Яндекс.Вебмастер → «Валидатор микроразметки»; убедиться, что ошибки нулевые.
PRIORITY: 2 — усиливает локальное SEO, дешёво, но вторично после LocalBusiness.

IDEA: prefers-reduced-motion — отключение reveal/blob-анимаций
KNOB: в CSS добавить `@media (prefers-reduced-motion: reduce){ *,*::before,*::after{animation-duration:.01ms !important;animation-iteration-count:1 !important;transition-duration:.01ms !important} .reveal{opacity:1;transform:none} }`.
EFFECT: доступность для пользователей с вестибулярными нарушениями; соответствие WCAG 2.3.3; нет риска для остальных.
RISK: практически нулевой — правило затрагивает только пользователей с включённой настройкой ОС.
ROLLBACK: `git checkout -- index.html`.
VERIFY: 3 минуты — DevTools → Rendering → Emulate prefers-reduced-motion: reduce, перезагрузить страницу, убедиться, что контент виден сразу без анимаций.
PRIORITY: 1 — одна строка CSS, закрывает реальный барьер доступности, нулевой риск.

IDEA: aria-hidden на иконочных SVG внутри контента (не фоновых)
KNOB: SITE_REQUEST: `<svg` — найти все инлайновые SVG-иконки в пунктах списка цены/шагов; каждому декоративному добавить `aria-hidden="true" focusable="false"`, если ещё нет.
EFFECT: скринридер не зачитывает «графика, без названия» перед каждым пунктом; чище семантика списков.
RISK: если какой-то SVG несёт смысл (иконка-статус), его скрытие уберёт информацию — проверять каждый.
ROLLBACK: `git checkout -- index.html`.
VERIFY: 2 минуты — включить VoiceOver/NVDA или расшир
