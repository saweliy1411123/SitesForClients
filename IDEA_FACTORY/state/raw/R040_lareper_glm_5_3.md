# lareper/glm-5.3  2026-11-17 03:35:08
duration=32.3 error=- attempts=1

IDEA: Проверка и фиксация `lang="ru"` и семантического `<main>`-landmark (аудит одним запросом)
KNOB: SITE_REQUEST «lang» — проверить наличие `<html lang="ru">` и тега `<main>` в разметке; если `<main>` отсутствует, обернуть секции от hero до final CTA в `<main id="main">` (не меняя классы/стили).
EFFECT: Скрин-ридеры и поисковики корректно определяют язык и основной контент; это базовый SEO/a11y-фактор, влияет на индексацию и Lighthouse Accessibility score.
RISK: Оборачивание в `<main>` может сломать CSS-селекторы вида `body > section`, если такие есть.
ROLLBACK: git checkout -- index.html
VERIFY: В консоли DevTools: `document.documentElement.lang` и `!!document.querySelector('main')` — 30 секунд.
PRIORITY: 1 — базовый a11y/SEO-фикс с нулевой стоимостью, но нужно подтверждение по снимку (в снимке `<main>` не виден).
SITE_REQUEST: lang

IDEA: Единый sitemap.xml + robots.txt для статического лендинга
KNOB: Создать в корне репозитория `robots.txt` (`User-agent: * / Allow: / / Sitemap: https://<домен>/sitemap.xml`) и `sitemap.xml` с одним URL `<loc>https://<домен>/</loc>` + `<lastmod>` = дата коммита. Домен подставить реальный (требует решения владельца, если сайт ещё не задеплоен).
EFFECT: Поисковики быстрее и полнее индексируют страницу; корректный canonical-сигнал при деплое; это гигиена SEO для лендинга услуг.
RISK: Если домен ещё неизвестен, sitemap с плейсхолдером бесполезен и может запутать при деплое.
ROLLBACK: Удалить оба файла: `git clean -f robots.txt sitemap.xml` или просто удалить вручную.
VERIFY: Открыть `robots.txt` в браузере после деплоя — 1 минута; до деплоя — валидация XML в любом онлайн-валидаторе — 2 минуты.
PRIORITY: 2 — полезно, но блокируется наличием реального домена (требует решения владельца).

IDEA: Сжатие и инлайн критического CSS для шрифтов Manrope (font-display + subset)
KNOB: В `<link>` Google Fonts (снимок: `family=Manrope:wght@400;500;600;700&display=swap`) добавить `&text=` параметр нельзя (динамический текст), но можно сократить веса до `400;600;700` (вес 500, вероятно, избыточен — проверить использованием через DevTools → Search «500» в CSS). Также добавить `<link rel="preload" as="style">` перед таблицей стилей шрифтов.
EFFECT: Меньше байт шрифта → быстрее LCP первого экрана; на мобильных 3G экономия 100–300 мс.
RISK: Если вес 500 используется где-то в CSS, текст откатится на 400 и станет чуть тоньше.
ROLLBACK: git checkout -- index.html
VERIFY: DevTools → Network → Font: посмотреть, сколько весов реально загружается и используется (панель Coverage) — 3 минуты.
PRIORITY: 2 — заметный, но умеренный выигрыш в скорости; безопасно при проверке.

IDEA: Мобильный аудит отступов hero (safe-area-inset для sticky CTA на iPhone)
KNOB: В CSS для `.sticky-cta` (L409–418) добавить `padding-bottom: calc(12px + env(safe-area-inset-bottom));` — чтобы мобильная CTA-панель не перекрывалась жестовой полосой iPhone.
EFFECT: На iPhone с «чёлкой» кнопка
