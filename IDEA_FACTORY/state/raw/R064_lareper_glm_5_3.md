# lareper/glm-5.3  2026-11-17 04:48:14
duration=50.8 error=- attempts=1

IDEA: Локальный self-host Manrope (woff2 рядом с index.html) — убрать зависимость от Google Fonts
KNOB: Скачать 4 начертания Manrope (400/500/600/700, subset cyrillic+latin) как `fonts/manrope-*.woff2` рядом с index.html; в `<head>` заменить `<link href="https://fonts.googleapis.com/css2?family=Manrope...">` на блок `@font-face` с `font-display:swap` и локальными путями; preconnect к fonts.googleapis.com удалить.
EFFECT: Устраняет render-blocking запрос на сторонний домен (~200–400 мс на мобильных), сайт работает офлайн/при блокировке Google (актуально для РФ-аудитории), FCP стабильнее — это же живое доказательство тезиса «быстро грузится».
RISK: Неверный unicode-range приведёт к загрузке всех 4 файлов вместо нужных; нужно проверить, что шрифт реально подтягивается локально.
ROLLBACK: `git checkout -- index.html` (файлы шрифтов не мешают).
VERIFY: DevTools → Network → фильтр Font: до — 4 запроса к fonts.gstatic.com; после — запросы к ./fonts/. Затем Network → Offline, перезагрузка — заголовок рендерится правильным шрифтом. Итог в консоли: `performance.getEntriesByType('resource').filter(r=>r.name.includes('fonts'))` — должно быть 0 внешних.
PRIORITY: 2 — заметный прирост скорости и надёжности для РФ, но не конверсионный.

IDEA: Контакт-блок в footer с явным именем/городом/часами ответа + LocalBusiness JSON-LD
KNOB: В финальной секции/футере (после L736) добавить компактный блок: «Савелий · Пермь · отвечаю в Telegram ежедневно 9:00–22:00» (взять реальные данные у владельца); в конец `<body>` — `<script type="application/ld+json">` с `@type: LocalBusiness` (name: Савелий, areaServed: Пермь, url, sameAs: https://t.me/TrainersDontPlays, priceRange по реальной цене со страницы).
EFFECT: Усиливает локальное SEO по запросам «лендинг Пермь», даёт доверие (живой человек, город, часы ответа) — снимает страх «напишу и никто не ответит».
RISK: Часы ответа и город — только подтверждённые владельцем данные, иначе это недостоверная информация.
ROLLBACK: `git checkout -- index.html`.
VERIFY: Rich Results Test (search.google.com/test/rich) на копию файла — валидный LocalBusiness без ошибок; визуально блок виден на мобильном 360px.
PRIORITY: 1 — прямой SEO+доверие эффект, дёшево, не дублирует существующие идеи (FAQPage/Service есть, LocalBusiness — нет).
SITE_REQUEST: footer

IDEA: Микро-«до/после» в hero: строка-переключатель «Ваш сайт сейчас → через 2 дня» (текстовый before/after без картинок)
KNOB: В hero после `.hero p.sub` (L122, вставка ~L463) добавить компактный блок `<div class="ba-strip" aria-hidden="false">` с двумя строками: «Сейчас: запись есть, но из Яндекса — тишина» → «Через 2 дня: сайт в поиске, заявки идут в вашу запись», разделённые стрелкой; CSS: две строки, вторая выделена градиентом `--blue`, лёгкий `@keyframes` fade-in.
EFFECT: Конкретизирует оффер в терминах результата клиента за 3 секунды сканирования hero — усиливает связку «боль → результат» до скролла, повышает CTR на глав
