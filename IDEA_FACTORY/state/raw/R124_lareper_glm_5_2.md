# lareper/glm-5.2  2026-11-17 07:42:41
duration=27.8 error=- attempts=1

IDEA: Schema.org LocalBusiness/Service JSON-LD с городом и услугой
KNOB: В `<head>` перед `</head>` добавить `<script type="application/ld+json">` с типом `Service` (provider: Person «Савелий», areaServed: «Пермь», serviceType: «Создание лендингов», offers с ценой из `.price-card`). Не LocalBusiness, т.к. нет адреса/часов — вымысел исключён.
EFFECT: Расширенный сниппет в Яндексе/Google, выше шанс попадания в локальную выдачу «лендинг Пермь».
RISK: Несовпадение данных schema с видимым контентом — поисковая система может игнорировать разметку.
ROLLBACK: `git checkout index.html` (файл не коммитить до проверки).
VERIFY: Вставить JSON в validator.schema.org — 0 ошибок; Rich Results Test на копии файла.
PRIORITY: 1 — SEO-ядро темы, дешёво, без фейков (все данные уже на странице).
SITE_REQUEST: offers

IDEA: Ленивое отключение reveal-анимаций при prefers-reduced-motion
KNOB: В `<style>` добавить `@media (prefers-reduced-motion: reduce){ .reveal, .magnetic, [class*="blob"]{animation:none!important;transition:none!important;opacity:1!important;transform:none!important} }`.
EFFECT: Страница читаема и не «прыгает» для пользователей с вестибулярными нарушениями; проходит базовый a11y-аудит.
RISK: Практически нулевой — меняется только анимация, не контент.
ROLLBACK: `git checkout index.html`.
VERIFY: DevTools → Rendering → Emulate prefers-reduced-motion: reduce — контент виден сразу без анимаций за 2 минуты.
PRIORITY: 1 — критично для a11y, одна строка CSS.

IDEA: Явные размеры/резерв места для градиентных blobs — устранение CLS
KNOB: Для абсолютных декоративных элементов hero (`.hero-bg`, blobs, `.final-bg`) задать в CSS `contain: layout paint` и `will-change: transform` только на десктопе; на мобильных (`@media(max-width:720px)`) ограничить количество видимых blobs до одного через `display:none` у остальных.
EFFECT: Ниже CLS и меньше нагрузка на GPU на слабых телефонах — быстрее ощущение загрузки.
RISK: Может измениться визуальная насыщенность фона на мобильных.
ROLLBACK: `git checkout index.html`.
VERIFY: Lighthouse → CLS до/после на копии файла, 3 минуты.
PRIORITY: 2 — заметно на мобильных, но эффект умеренный.

IDEA: rel="canonical" и robots meta для чистоты индексации
KNOB: В `<head>` добавить `<link rel="canonical" href="https://<домен-владельца>/">` и `<meta name="robots" content="index, follow">`; плейсхолдер домена пометить комментарием «вписать реальный домен».
EFFECT: Защита от дублей при хостинге на нескольких зеркалах, корректная индексация.
RISK: Неверный домен в canonical — страница может выпасть из индекса; требует решения владельца (нужен реальный URL).
ROLLBACK: `git checkout index.html`.
VERIFY: Открыть исходник, проверить наличие тега; после хостинга — «Проверить URL» в Яндекс.Вебмастере.
PRIORITY: 2 — важно при публикации, пока не срочно.

IDEA: Метод — аудит контраста всех текстов одним проходом
KNOB: METHOD: (1) Открыть index.html, консоль: `[...document.querySelectorAll('body *')].filter(e=>e.childNodes.length&&e.textContent.trim()&&getComputedStyle(e).color).
