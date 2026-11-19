# lareper/glm-5.2  2026-11-17 05:39:26
duration=28.1 error=- attempts=1

IDEA: robots.txt + sitemap.xml для статического лендинга
KNOB: Создать рядом с index.html два файла: `robots.txt` с `User-agent: *\nAllow: /\nSitemap: https://<домен>/sitemap.xml` и `sitemap.xml` с единственным URL `<loc>https://<домен>/</loc>` (домен уточнить у владельца). Сам index.html не меняется.
EFFECT: Поисковики быстрее и полнее индексируют единственную страницу; корректный sitemap убирает риск «страница не найдена краулером» при деплое.
RISK: Если домен ещё не определён/изменится, sitemap будет указывать на несуществующий URL — требует решения владельца (реальный домен).
ROLLBACK: Удалить оба файла: `del robots.txt sitemap.xml` (index.html не затронут).
VERIFY: За 2 минуты: открыть `https://<домен>/robots.txt` после деплоя локально — проверить синтаксис любым валидатором (yandex.ru/support/webmaster) или глазами: два блока, без лишних символов.
PRIORITY: 2 — базовая SEO-гигиена, эффект отложенный, но нулевая цена и нулевой риск для кода.

IDEA: Canonical + meta robots «index, follow» от явных дублей
KNOB: В `<head>` (после og-тегов, ~L7–L13) добавить `<link rel="canonical" href="https://<домен>/">` и `<meta name="robots" content="index, follow, max-image-preview:large">`.
EFFECT: Защита от дублей (www/без www, http/https, хостинг-превью-URL), склейка сигналов на один канонический адрес — чище выдача по запросу «лендинг Пермь за 2 дня».
RISK: Неверный canonical (опечатка в домене) может исключить страницу из индекса — требует решения владельца (подтвердить домен).
ROLLBACK: Удалить две добавленные строки из `<head>`; либо `git checkout -- index.html`.
VERIFY: За 2 минуты: Ctrl+U → найти canonical; затем DevTools → Console → `document.querySelector('link[rel=canonical]')` не null и href начинается с https.
PRIORITY: 2 — важно при публикации на хостинге с превью-URL, сейчас (локальный файл) эффект нулевой.

IDEA: Видимый фокус и aria-label для навигации и якорных ссылок
KNOB: В CSS добавить `.nav a:focus-visible,.btn-primary:focus-visible,a:focus-visible{outline:2px solid var(--blue);outline-offset:3px;border-radius:4px}`; в `<nav>` (~L440–445) добавить `aria-label="Основная навигация"`, а ссылкам-якорям без текста (если есть иконочные) — `aria-label`.
EFFECT: Клавиатурные пользователи и скринридеры видят, где фокус и куда ведёт ссылка; плюс к Lighthouse Accessibility score → доверие и SEO-сигнал.
RISK: Минимальный — нестандартный outline может чуть отличаться визуально от текущего стиля фокуса.
ROLLBACK: `git checkout -- index.html`.
VERIFY: За 3 минуты: открыть страницу, нажимать Tab — каждый интерактивный элемент должен получить видимое кольцо фокуса; в DevTools → Lighthouse → Accessibility посмотреть, что нет пунктов «focus-not-visible» / «link-name».
PRIORITY: 1 — дёшево
