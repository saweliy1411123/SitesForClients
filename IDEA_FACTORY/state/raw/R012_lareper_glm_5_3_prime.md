# lareper/glm-5.3-prime  2026-11-17 02:16:25
duration=29.9 error=- attempts=1

IDEA: Секция FAQ — aria-связь summary/answer и закрытие открытых details при открытии нового
KNOB: В секции FAQ (~L660–690) у каждого `<details>` добавить `name="faq"` (HTML-атрибут exclusive accordion) и на `<summary>` добавить `aria-expanded` через 3 строки JS: `document.querySelectorAll('details[name=faq]').forEach(d=>d.addEventListener('toggle',()=>{d.querySelector('summary').setAttribute('aria-expanded',d.open)}))`. Дополнительно `summary{cursor:pointer}` и `summary::-webkit-details-marker{display:none}` только если уже стилизовано классом `.plus`.
EFFECT: Скринридеры корректно объявляют состояние вопроса (открыт/закрыт); одновременное открытие всех ответов не «размывает» страницу — пользователь быстрее находит нужный ответ, меньше прокрутки на мобильном.
RISK: Атрибут `name` на `<details>` не поддерживается в старых Safari — деградация до обычного поведения, ничего не ломается.
ROLLBACK: git checkout -- index.html (или восстановить блок FAQ из копии index.improved.html.bak).
VERIFY: Открыть FAQ, Tab до первого summary, Enter — проверить открытие; открыть второй вопрос — первый должен закрыться; в DevTools → Accessibility tree проверить role=button и aria-expanded.
PRIORITY: 2 — нулевой риск, заметно для a11y и мобильного UX, но не двигает конверсию напрямую.

IDEA: Убрать render-blocking Google Fonts — self-host fallback через system-font stack
KNOB: В `<head>` (L~7, ссылки на fonts.googleapis.com) добавить `<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap">` с `onload="this.rel='stylesheet'"` + `<noscript>`-фолбэк; в CSS-переменную шрифта добавить фолбэк-стек `Manrope, -apple-system, 'Segoe UI', Roboto, sans-serif` (если ещё нет).
EFFECT: Текст рендерится сразу системным шрифтом, Manrope подгружается асинхронно — FCP/LCP на мобильных 3G падает на 300–700 мс, меньше отказов с медленного мобильного трафика из Яндекса.
RISK: Кратковременный FOUT — скачок метрик шрифта, при неправильном фолбэке заметный сдвиг текста (CLS).
ROLLBACK: git checkout -- index.html.
VERIFY: DevTools → Network → throttling Slow 4G, перезагрузить: шрифт не должен блокировать отрисовку; Lighthouse Performance до/после сравнить FCP.
PRIORITY: 1 — единственный render-blocking внешний ресурс на странице, прямой выигрыш в скорости без изменения контента.

IDEA: Проверка контраста фиолетового CTA и градиентного текста (WCAG AA)
KNOB: METHOD: Взять из CSS значения цветов `.btn-primary` (фон/текст) и `.grad-text` (L386, градиент на прозрачном тексте), прогнать пары через контрастный чекер (webaim.org/resources/contrastchecker или DevTools → Color picker показывает ratio). Целевой порог: 4.5:1 для текста, 3:1 для крупного. Если `.grad-text` на тёмном фоне даёт <4.5:1 — добавить в CSS дубль правила с однотонным цветом внутри `@media (prefers-contrast: more){.grad-text{background:none;color:#c4b5fd}}`.
EFFECT: Часть пользователей (низкое зрение, яркий солнечный свет на телефоне) реально читает заголовки и видит CTA — больше доходит до заявки; плюс соответствие WCAG AA как доверие для B2B-клиентов.
RISK: Почти нулевой — изменение
