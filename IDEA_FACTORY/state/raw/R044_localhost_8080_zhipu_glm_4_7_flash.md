# localhost:8080/zhipu/glm-4.7-flash  2026-11-17 03:46:53
duration=43.4 error=- attempts=1

IDEA: Метод «Mobile Viewport Stress Test» (проверка первого экрана на мобильных)
KNOB: METHOD: В Chrome DevTools включить Device Toolbar (F12 -> Ctrl+Shift+M), выбрать ширину 360px. Измерить высоту `hero` (L449) и `wrap` (L455). Если `hero.offsetHeight > window.innerHeight * 1.5`, значит оффер не виден сразу.
EFFECT: Выявляет риск, что на мобильных устройствах пользователю нужно скроллить мимо главного предложения, снижая конверсию.
RISK: Низкий.
ROLLBACK: Отмена Device Toolbar (Ctrl+Shift+M).
VERIFY: 3 минуты.
PRIORITY: 2 (Конверсия)

IDEA: Метод «Dead Link Detector» (поиск битых якорей)
KNOB: METHOD: В консоли DevTools выполнить: `[...document.querySelectorAll('a[href]')].filter(a => !a.getAttribute('href').startsWith('#') || !document.querySelector(a.getAttribute('href'))).forEach(a => console.log('Broken:', a.href))`. Проверить вывод.
EFFECT: Находит ссылки, ведущие на несуществующие разделы (например, `#contact` без секции с `id="contact"`), что вызывает раздражение при клике.
RISK: Низкий.
ROLLBACK: Закрыть консоль.
VERIFY: 2 минуты.
PRIORITY: 1 (UX)

IDEA: Метод «Dark Mode Contrast Audit» (проверка читаемости)
KNOB: METHOD: В Chrome DevTools -> Accessibility -> Compute Styles. Выбрать текст в `h1` (L455) и `p.sub` (L460). Использовать Eye Dropper для проверки соотношения яркости текста и фона (градиент `#8b5cf6` -> `#0a0a0f`). Цель: WCAG AA (4.5:1).
EFFECT: Гарантирует, что премиальный тёмный дизайн не нарушает законы доступности и не раздражает пользователей с ослабленным зрением.
RISK: Низкий.
ROLLBACK: Закрыть вкладку Accessibility.
VERIFY: 5 минут.
PRIORITY: 2 (Доступность)
