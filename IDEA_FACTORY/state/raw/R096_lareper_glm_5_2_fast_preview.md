# lareper/glm-5.2-fast-preview  2026-11-17 06:22:01
duration=2.5 error=- attempts=1

IDEA: FAQPage JSON-LD разметка по реальным вопросам FAQ
KNOB: В `<head>` перед `</head>` добавить `<script type="application/ld+json">` с `@type: FAQPage`, где вопросы/ответы дословно скопированы из секции FAQ (L663–705) — без выдуманных новых вопросов.
EFFECT: Яндекс/Google могут показать расширенный сниппет с вопросами в выдаче — выше CTR по запросам «лендинг Пермь», «сайт за 2 дня».
RISK: Если разметка не совпадёт с видимым текстом FAQ — риск ручных санкций поисковиков.
ROLLBACK: `git checkout index.html`
VERIFY: Вставить JSON-LD в копию, открыть https://validator.schema.org — 0 ошибок; сверить тексты вопросов с L663–705.
PRIORITY: 1 — дешёвая правка head, прямой SEO-эффект для локального оффера.

IDEA: Уникальный alt/доступное имя для SVG-favicon и декоративных фонов
KNOB: Инлайн-SVG favicon (L12) уже без alt — ок; проверить, что все декоративные div (`.hero-veil`, blobs, `.final-veil`) получили `aria-hidden="true"` и `role="presentation"` — добавить недостающие атрибуты.
EFFECT: Скринридер не озвучивает мусор, порядок чтения чище — меньше отказов у пользователей с a11y-настройками.
RISK: Минимальный — атрибуты не меняют визуал.
ROLLBACK: `git checkout index.html`
VERIFY: В консоли: `[...document.querySelectorAll('.hero-veil,.final-veil,[class*=blob]')].filter(e=>!e.hasAttribute('aria-hidden'))` — пустой массив после правки.
PRIORITY: 2 — низкий риск, но эффект узкий.

IDEA: Сокращение веса Manrope — оставить только используемые веса
KNOB: В URL Google Fonts (L~13) `wght@400;500;600;700` — проверить в DevTools → Elements computed styles, какие веса реально используются; если 500 не встречается, убрать его из запроса: `wght@400;600;700`.
EFFECT: Меньше байт шрифтового CSS и woff2 — быстрее LCP на мобильных (шрифт — главный render-blocking ресурс).
RISK: Если вес всё же используется где-то, браузер подставит синтетический — изменится начертание.
ROLLBACK: `git checkout index.html`
VERIFY: В консоли: `['400','500','600','700'].map(w=>[w,!![...document.querySelectorAll('*')].find(e=>getComputedStyle(e).fontWeight===w)])` — вычеркнуть только неиспользуемые.
PRIORITY: 2 — микрооптимизация, но бесплатная и безопасная при проверке.

IDEA: `<html lang="ru">` + skip-link «к содержимому»
KNOB: (1) Проверить/установить `lang="ru"` на `<html>` (L1). (2) Первым элементом в `<body>` добавить `<a class="skip-link" href="#contact">Перейти к заявке</a>` с CSS: позиция absolute, уводится за экран, появляется при `:focus`.
EFFECT: Скринридеры корректно произносят русский текст; клавиатурные пользователи за 1 Tab попадают к CTA — быстрее конверсионный путь.
RISK: Skip-link должен вести на существующий id — иначе бесполезен.
ROLLBACK: `git checkout index.html`
VERIFY: Открыть страницу, нажать Tab — первая остановка фокуса должна показать skip-link; в DevTools → Elements проверить `lang` на `<html>`.
PRIORITY: 1 — базовый a11y, ноль визуального риска.

IDEA: Ленивая отрисовка ниже-ф
