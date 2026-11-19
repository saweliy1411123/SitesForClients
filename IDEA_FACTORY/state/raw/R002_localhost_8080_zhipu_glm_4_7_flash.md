# localhost:8080/zhipu/glm-4.7-flash  2026-11-17 01:46:23
duration=40.5 error=- attempts=1

IDEA: Проверка доступности фокуса (Keyboard Navigation)
METHOD: Открыть DevTools, проверить `:focus-visible` на всех ссылках (CTA). Нажать Tab.
KNOB: Добавить CSS `.cta-link:focus-visible { outline: 3px solid #8b5cf6; outline-offset: 4px; }` на все `<a>` с классом CTA.
EFFECT: Убедиться, что пользователи клавиатуры могут найти кнопку "Сделаю демо" и перейти по ней.
RISK: Нет.
ROLLBACK: Удалить CSS-правило.
VERIFY: Нажать Tab на клавиатуре. Есть ли фокус и подсветка на ссылках?
PRIORITY: 2 (UX/A11y)

IDEA: Симуляция мобильной верстки (Device Toolbar)
METHOD: F12 -> Toggle Device Toolbar (iPhone 12/Android).
KNOB: Проверить ширину 375px и высоту 667px.
EFFECT: Проверить, не ломается ли верстка, не скрывается ли контент и нет ли горизонтального скролла на узких экранах.
RISK: Нет.
ROLLBACK: Закрыть DevTools.
VERIFY: Все заголовки (h1-h3) читабельны без масштабирования?
PRIORITY: 1 (Critical)

IDEA: Тест схемы LocalBusiness (Schema.org)
METHOD: Добавить JSON-LD в `<head>`, запустить в Google Rich Results Test.
KNOB: Вставить скрипт с `@type: LocalBusiness`, `name: "Савелий"`, `areaServed: "Пермь"`. Прогнать через тест.
EFFECT: Проверить, понимает ли Google суть бизнеса (лендинги в Перми) для будущих сниппетов.
RISK: Нет (локальный тест).
ROLLBACK: Удалить тег `<script type="application/ld+json">`.
VERIFY: Результат теста — "LocalBusiness" или "Service"?
PRIORITY: 3 (SEO)
