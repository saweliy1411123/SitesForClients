# lareper/deepseek-v4.1-flash  2026-11-17 06:22:38
duration=68.7 error=- attempts=1

IDEA: Добавить `aria-hidden="true"` декоративным blob-элементам и иконкам-стрелкам в CTA-кнопках
KNOB: В hero-секции (`.hero-blob`, `.hero-veil` и аналогичные декоративные элементы с `position:absolute`/`background`) и в `<span class="arr">→</span>` внутри `.btn-primary` (L462, L657, L705, L736) добавить атрибут `aria-hidden="true"`. Для стрелок также добавить `aria-label` не требуется, т.к. текст кнопки уже есть.
EFFECT: Скринридеры не будут зачитывать декоративные SVG/градиенты и стрелки, улучшится доступность для незрячих пользователей, чище accessibility-дерево, небольшой плюс к Lighthouse Accessibility.
RISK: Минимальный — атрибут не влияет на визуальное отображение; риск только если какой-то элемент окажется не декоративным, но по снимку все blob/стрелки декоративные.
ROLLBACK: `git checkout -- index.html` или удалить добавленные `aria-hidden` вручную.
VERIFY: Открыть DevTools → Accessibility-дерево (Esc → Accessibility), проверить, что blob-элементы и стрелки отсутствуют в дереве; также Lighthouse Accessibility score ≥95.
PRIORITY: 2 — улучшение a11y без изменения контента, быстрое и безопасное.
SITE_REQUEST: hero-veil
SKILL: a11y-decorative-aria-hidden
