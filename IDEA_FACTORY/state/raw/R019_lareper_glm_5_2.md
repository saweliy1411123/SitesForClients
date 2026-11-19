# lareper/glm-5.2  2026-11-17 02:36:36
duration=27.6 error=- attempts=2

IDEA: robots.txt + sitemap.xml для индексации
KNOB: создать в корне репозитория `robots.txt` (`User-agent: * / Allow: / / Sitemap: https://<домен>/sitemap.xml`) и `sitemap.xml` с одним URL `/`. Домен уточнить у владельца — в снапшоте его нет.
EFFECT: поисковики быстрее и корректнее индексируют лендинг; sitemap — базовый сигнал для Яндекса/Google.
RISK: без реального домена sitemap будет указывать на несуществующий URL — требует решения владельца (какой домен).
ROLLBACK: удалить два новых файла (`del robots.txt sitemap.xml`) — index.html не затрагивается.
VERIFY: открыть `robots.txt` в валидаторе Яндекса Вебмастер (или просто прочитать за 2 минуты); проверить, что URL в sitemap отвечает 200.
PRIORITY: 2 — база SEO, но нужен домен от владельца.

IDEA: content-visibility для секций ниже первого экрана
KNOB: в CSS добавить `section:not(.hero){content-visibility:auto;contain-intrinsic-size:auto 800px;}` — браузер не рендерит офскрин-секции до прокрутки.
EFFECT: быстрее первичный рендер на мобильных (7 секций, из них 6 ниже фолда), лучше LCP/INP на слабых телефонах.
RISK: при резком скролле возможен микросдвиг, если `contain-intrinsic-size` сильно не совпадает с реальной высотой секции.
ROLLBACK: `git checkout index.html` (правка только в CSS-блоке `<style>`).
VERIFY: DevTools → Performance → Record со скроллом до/после; сравнить Scripting/Rendering время первых 2 секунд.
PRIORITY: 2 — заметный прирост скорости без изменения контента.

IDEA: сократить набор весов Manrope (700 → убрать неиспользуемый)
KNOB: SITE_REQUEST «font-weight» — проверить, используется ли weight 700 (или 400/500). В `<link>` Google Fonts оставить только реально применяемые веса, например `wght@400;600`.
EFFECT: меньше байт шрифта и меньше вариантов подмены (FOUT) — быстрее отрисовка текста, особенно на 3G.
RISK: если вес используется в CSS, текст станет тоньше/жирнее — визуальный сдвиг.
ROLLBACK: вернуть исходный `<link>`: `git checkout index.html`.
VERIFY: в DevTools → Searching по `font-weight` найти все значения; сверить с запрошенными весами за 3 минуты.
PRIORITY: 2 — дешёвая победа по скорости, нулевой риск при сверке.

IDEA: meta color-scheme + og:locale/og:url
KNOB: в `<head>` добавить `<meta name="color-scheme" content="dark">` (сайт тёмный: bg `#0a0a0f`), `<meta property="og:locale" content="ru_RU">` и `<meta property="og:url" content="https://<домен>/">`.
EFFECT:
