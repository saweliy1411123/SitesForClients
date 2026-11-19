# lareper/glm-5.2  2026-11-17 06:01:47
duration=43.2 error=- attempts=1

IDEA: Preconnect + display=swap уже есть — добавить `<link rel="preload">` конкретного woff2 Manrope 700
KNOB: В `<head>` после preconnect-ссылок (fonts.googleapis.com, fonts.gstatic.com) добавить `<link rel="preload" as="font" type="font/woff2" crossorigin href="https://fonts.gstatic.com/s/manrope/v15/xn7gYHE41ni1AdIRggexSg.woff2">` (URL взять из Network-панели при загрузке — файл с weight 700, он используется в h1/h2/CTA).
EFFECT: Убирает FOUT/невидимый текст заголовков на 100–300 мс при медленном соединении — первый экран читается сразу, LCP заголовка быстрее.
RISK: Preload не того файла (не тот unicode-range/weight) даст двойную загрузку шрифта и лишний запрос.
ROLLBACK: `git checkout index.html`
VERIFY: F12 → Network → фильтр Font → перезагрузка: убедиться, что woff2 для weight 700 один и грузится с приоритетом High, а не после CSS.
PRIORITY: 2 — заметно на мобильных, но эффект ограничен одним файлом шрифта.

IDEA: `content-visibility: auto` для секций ниже фолда
KNOB: В `<style>` добавить `section{content-visibility:auto;contain-intrinsic-size:auto 600px;}` и исключить первую секцию hero селектором `section:first-of-type{content-visibility:visible;}`.
EFFECT: Браузер не рендерит невидимые секции (цена, FAQ, final) до скролла — быстрее первичная отрисовка и меньше работы при ресайзе на телефонах.
RISK: Внутри секций с якорями (#price, #contact) возможен скачок скролла при переходе по хэшу до инициализации секции.
ROLLBACK: `git checkout index.html`
VERIFY: Открыть локально, DevTools → Rendering → включить Frame Rendering Stats, проскроллить все 7 секций — проверить отсутствие «прыжков» и что переход по `#contact` из nav попадает точно в секцию.
PRIORITY: 2 — дешёвая скорость-победа для страницы на 937 строк без сборки.

IDEA: Проверка контраста `--muted`-текста на тёмном фоне (a11y WCAG AA)
KNOB: METHOD: (1) В консоли выполнить: `[...document.querySelectorAll('p,li,span')].filter(e=>getComputedStyle(e).color).slice(0,50).forEach(e=>{const c=getComputedStyle(e).color;console.log(c,e.className||e.tagName)})` — выписать все используемые цвета текста. (2) Каждый hex прогнать через чек-лист: серый текст на `--bg` должен иметь ratio ≥4.5:1 (обычный) или ≥3:1 (≥18px bold). (3) Особое внимание `--muted` в `.price-card .per` (L350) и `.hero-note`. (4) Если ratio < 4.5 — осветлить переменную на 1–2 ступени.
EFFECT: Гарантия, что слабовидящие пользователи и пользователи на телефоне при ярком свете читают цену и примечания; устранение типичного a11y-провала тёмных лендингов.
RISK: Осветление muted-цвета может снизить визуальную иерархию — менять точечно, не глобально.
ROLLBACK: `git checkout index.html`
VERIFY: DevTools → Ctrl+Shift+P → «Show Rendering» → Emulate vision deficiencies → blurred vision / contrast loss: текст цены и hero-note остаётся читаемым.
PRIORITY: 1 — цена — ключевая конверсионная точка, нечитаемый текст напрямую бьёт по заявкам.

IDEA: `<noscript>`-фол
