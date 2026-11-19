# lareper/glm-5.2-fast-preview  2026-11-17 07:03:56
duration=5.9 error=- attempts=1

IDEA: Минимальный размер тап-таргетов на мобильных (nav, FAQ, CTA)
KNOB: В `@media(max-width:720px)` добавить правила: `.nav-links a, .faq summary, .btn-primary, .sticky-cta a { min-height:48px; padding:12px 16px; }` — довести все кликабельные элементы до ≥48×48px (WCAG 2.5.8 / Google Mobile-Friendly).
EFFECT: Меньше промахов пальцем на телефоне → больше переходов по CTA и FAQ, прохождение мобильного аудита Google.
RISK: Увеличенные паддинги могут сдвинуть плотную сетку на узких экранах (<360px).
ROLLBACK: `git checkout -- index.improved.html` (правки только в копии) или удаление добавленного media-блока.
VERIFY: DevTools → Toggle device toolbar (375px) → инспектором проверить высоту каждой ссылки nav и summary: `[...document.querySelectorAll('a,summary')].filter(e=>e.getBoundingClientRect().height<44)`.
PRIORITY: 1 — прямой мобильный UX/конверсия, нулевой риск контента.

IDEA: `scroll-margin-top` для якорных секций под фиксированным хедером
KNOB: В `<style>` добавить `section[id], #top { scroll-margin-top: 90px; }` (значение = высота фиксированной nav + запас).
EFFECT: При клике по «Цена»/«Вопросы» заголовок секции не прячется под фиксированным меню — пользователь видит контекст, меньше «потерянных» переходов.
RISK: При неверном значении останется зазор или частичное перекрытие — подобрать под реальную высоту хедера.
ROLLBACK: Удалить одно CSS-правило / `git checkout -- index.improved.html`.
VERIFY: Открыть страницу, кликнуть каждую nav-ссылку (L441–L443, L717) и убедиться, что h2 секции полностью виден ниже хедера.
PRIORITY: 2 — заметный UX-фикс, но не блокирует конверсию.

IDEA: Фолбэк-шрифт с metric-совместимостью (устранение CLS от Manrope)
KNOB: В `@font-face`-фолбэке перед загрузкой Google Fonts добавить локальный fallback через `@font-face { font-family:'Manrope-fallback'; src:local('Arial'); size-adjust:~105%; ascent-override:~100%; }` и в `font-family` стека указать `'Manrope','Manrope-fallback',sans-serif` — цифры подобрать методом сравнения ширины h1.
EFFECT: Текст рендерится сразу метрически близким шрифтом → меньше скачка макета (CLS) при подмене на Manrope, лучше LCP-восприятие на мобильных.
RISK: Неточные override-значения дадут видимый сдвиг текста в момент подмены — нужно подобрать по скриншоту до/
