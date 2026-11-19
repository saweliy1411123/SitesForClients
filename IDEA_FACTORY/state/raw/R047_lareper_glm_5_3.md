# lareper/glm-5.3  2026-11-17 03:55:53
duration=23.4 error=- attempts=1

IDEA: FAQ `<details>` с FAQPage JSON-LD и видимым первым ответом (не скрытым по умолчанию)
KNOB: Секция FAQ (~L660–705): каждый вопрос обернуть в `<details class="faq-item" open?>` с `<summary>Вопрос</summary><p>Ответ</p>`; к секции добавить `<script type="application/ld+json">` с `FAQPage` (Question/Answer — тексты берутся дословно из существующего контента). Первый элемент оставить `open`, чтобы контент индексировался и был виден без JS.
EFFECT: Компактнее на мобильном, меньше «стены текста»; Google может показать расширенный сниппет в Яндексе/Google по вопросам о цене и сроках — рост CTR из поиска.
RISK: Скрытые в `<details>` ответы часть поисковиков индексируют хуже — компенсируется открытым первым элементом и дословным JSON-LD.
ROLLBACK: `git checkout -- index.html` (правки вносить в копии index.improved.html).
VERIFY: (1) Rich Results Test / validator.schema.org — вставить URL или HTML, убедиться «FAQPage — без ошибок». (2) Мобайл 360px: тап по каждому summary — раскрытие, фокус с клавиатуры (Tab+Enter) работает.
PRIORITY: 1 — нулевой риск, чистый SEO+a11y-выигрыш на уже существующем контенте.

IDEA: Само-аудит заголовков и landmarks одним консольным сниппетом + фикс `<main>`
KNOB: METHOD: (1) В консоли выполнить: `console.table([...document.querySelectorAll('h1,h2,h3')].map(h=>({tag:h.tagName,text:h.textContent.trim().slice(0,60)})))` — проверить иерархию (h1→h2→h3 без пропусков). (2) Проверить наличие `<main>`: `!!document.querySelector('main')`. (3) Если `<main>` нет — обернуть контент между `<header class="hero">` (L449) и футером в `<main id="main">`; к первой ссылке навигации добавить skip-link `<a class="sr-only-focusable" href="#main">К содержанию</a>`.
EFFECT: Корректная семантика для скринридеров и поисковиков; skip-link ускоряет клавиатурную навигацию — прямой a11y-сигнал.
RISK: Перенос блоков внутрь `<main>` может сдвинуть CSS-селекторы типа `body > section` — проверить рендер до/после.
ROLLBACK: `git checkout -- index.html`.
VERIFY: DevTools → Accessibility pane → «Landmarks»: должны появиться banner/main/contentinfo; вкладка только с Tab — skip-link первым фокусом.
PRIORITY: 2 — важно, но требует аккуратной проверки рендера.

IDEA: Preconnect + `media="print"`-трюк для Google Fonts (устранение render-blocking)
KNOB: В `<head>` (снимок: 4 `<link>`, fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700): (1) добавить `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>`; (2) заменить основной font-link на `media="print" onload="this.media='all'"` + `<noscript>`-фолбэк с обычным линком.
EFFECT: Шрифты перестают блокировать первый рендер — FCP/LCP на мобильном падает ориентировочно на 200–500 мс; preconnect экономит DNS+TLS до fonts.gstatic.com.
RISK: Без noscript-фолбэка при выключенном JS шрифт не загрузится — фолбэк обязателен; кратковременный FOUT закрывается `display=swap` (уже есть).
ROLLBACK: `git checkout -- index.html`.
VERIFY: DevTools → Network → thrott
