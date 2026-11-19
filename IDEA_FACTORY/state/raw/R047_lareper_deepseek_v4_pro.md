# lareper/deepseek-v4-pro  2026-11-17 03:56:17
duration=2.4 error=- attempts=2

IDEA: FAQ — JSON-LD FAQPage с двумя видимыми вопросами и aria-controls
KNOB: В секции FAQ (~L660–705) заменить текущие `<p>`-ответы на `<details class="faq-item"><summary>…</summary><p>…</p></details>` (2–3 вопроса) и в конец `<body>` добавить `<script type="application/ld+json">` с `@type:"FAQPage"`, `mainEntity` из этих же вопросов/ответов. У каждого `<details>` добавить `id="faq-1"`, `aria-controls`.
EFFECT: Поисковик сможет показать вопросы/ответы прямо в выдаче (расширенный сниппет), а пользователь раскрывает ответ без перезагрузки — выше CTR и доверие.
RISK: Если разметка не совпадёт с видимым текстом — Google может пометить как спам; проверять в Rich Results Test.
ROLLBACK: `git checkout -- index.html` (или удалить добавленный `<script>` и вернуть `<p>`-блоки).
VERIFY: Открыть в Rich Results Test → проверить «FAQPage», кликнуть `<details>` на мобильной ширине 360px — раскрытие плавное, без сдвига.
PRIORITY: 1 — это и SEO, и UX, и сниппет, и доступность.
SITE_REQUEST: faq

IDEA: Мобильная версия — «первый экран без скролла» на 360px (hero-компрессия)
KNOB: В `@media (max-width: 480px)` для `.hero` (L93) уменьшить `padding: 130px 0 100px` до `padding: 96px 0 64px`, `h1` (L114) — `font-size: clamp(34px, 9vw, 44px)`, `.sub` (L122) — `margin: 18px 0 24px`, `.hero-note` (L141) — `font-size: 12.5px; margin-top: 12px`. Проверить, что CTA-кнопка и `.hero-note` видны без прокрутки.
EFFECT: На дешёвых Android (360px) посетитель сразу видит оффер, CTA и подпись — меньше отказов, выше шанс клика.
RISK: Если сжать слишком сильно — текст станет нечитаемым; проверять на реальном устройстве.
ROLLBACK: Вернуть прежние значения в `@media` (или `git checkout`).
VERIFY: DevTools → Device Toolbar → 360px (Galaxy S8) → скриншот — CTA и `.hero-note` в пределах первого экрана.
PRIORITY: 1 — мобильный трафик часто > 50%, а сейчас hero явно перегружен по высоте.
SITE_REQUEST: hero

IDEA: SEO — `<meta name="robots" content="index, follow">` + `canonical`
KNOB: В `<head>` после `<meta name="viewport">` добавить `<meta name="robots" content="index, follow">` и `<link rel="canonical" href="https://<домен>/">`. Если домен неизвестен — использовать относительный `href="/"`.
EFFECT: Поисковик не будет путаться с дублями (если сайт доступен по `www`/без `www`, с `/index.html`), а робот явно получит разрешение индексировать.
RISK: Если домен указан неверно — canonical навредит; лучше использовать относительный путь.
ROLLBACK: Удалить две строки.
VERIFY: Открыть исходник → найти `robots` и `canonical`; в Search Console → URL Inspection → «Просканировать как Google».
PRIORITY: 2 —
