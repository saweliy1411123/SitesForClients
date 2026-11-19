# lareper/glm-5.2  2026-11-17 07:24:29
duration=2.3 error=- attempts=2

IDEA: FAQ как details/summary — нативная доступность без JS и SEO-текст в DOM
KNOB: Секция FAQ (перед финальным CTA, ~L690+): заменить JS-раскрытие (если div+клик) на `<details class="faq-item"><summary>Вопрос</summary><p>Ответ</p></details>`; summary стилизовать как текущий элемент (cursor:pointer, list-style кастомный маркер, min-height 48px)
EFFECT: Ответы FAQ всегда в DOM и доступны поисковикам и скринридерам, работает без JS, клавиатурная навигация из коробки — плюс к SEO и a11y
RISK: Внешний вид маркера details отличается от текущего дизайна — нужен CSS для ::marker/summary::-webkit-details-marker
ROLLBACK: git checkout -- index.html (правки в index.improved.html, оригинал не трогаем)
VERIFY: Открыть файл, Tab до FAQ — пробел раскрывает вопрос; в консоли `document.querySelectorAll('details').length` и Ctrl+F по тексту ответа при закрытом состоянии; Lighthouse a11y ≥ до
PRIORITY: 1 — FAQ сейчас либо невидим для SEO, либо требует JS; правка дешёвая и безопасная
SITE_REQUEST: faq

IDEA: Инерционный prefetch якорных секций не нужен — вместо этого content-visibility для отложенных секций
KNOB: В `<style>` добавить `.price, .final, section:not(.hero){content-visibility:auto;contain-intrinsic-size:auto 800px;}` (по одному классу/селектору на секции ниже первого экрана)
EFFECT: Браузер пропускает рендер/лейаут невидимых секций — быстрее первый рендер и скролл на слабых мобильных, без изменения визуала
RISK: Возможен скачок скроллбара (CLS) при неточном contain-intrinsic-size — подобрать высоту по факту
ROLLBACK: git checkout -- index.improved.html
VERIFY: До/после в консоли: `new PerformanceObserver(l=>console.log(l.getEntries()))` на largest-contentful-paint; прокрутить страницу — нет визуальных прыжков
PRIORITY: 2 — заметно на мобильных, но требует подбора intrinsic-size

IDEA: Локальный fallback-шрифт с font-display и метрически близким стеком против FOIT
KNOB: В `<style>` к `body`/заголовкам добавить `font-family:'Manrope',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;` (если ещё нет) и убедиться, что Google Fonts URL содержит `display=swap` (снимок показывает, что содержит — тогда только стек fallback)
EFFECT: Текст виден мгновенно системным шрифтом до загрузки Manrope — меньше «пустого» текста, лучше LCP и воспринимаемая скорость
RISK: Кратковременная подмена шрифта (FOUT) заметна как «мигание» — приемлемо против невидимого текста
ROLLBACK: git checkout -- index.improved.html
VERIFY: DevTools → Network → throttling Slow 3G, перезагрузка: текст читаем сразу, не ждёт шрифта
PRIORITY: 2 — дешёвая страховка скорости на слабой сети

IDEA: Видимый фокус-стиль для всех интерактивных элементов с сохранением дизайна
KNOB: В `<style>` добавить `a:focus-visible,button:focus-visible,summary:focus-visible{outline:2px solid #8b5cf6;outline-offset:3px;border-radius:4px;}` и убедиться, что нет глобального `outline:none`
EFFECT: Клавиатурные пользователи и скринридер-аудитория видят, где фокус — WCAG AA, плюс Lighthouse a11y
RISK: Почти нулевой; при мыши-клике outline не показ
