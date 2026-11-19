# lareper/glm-5.3  2026-11-17 03:16:33
duration=45.9 error=- attempts=1

IDEA: Клавиатурный доступ для интерактивного div с onclick
KNOB: L524 `<div class="visual" onclick="...scrollIntoView...">` — заменить на `<a href="#contact" class="visual" aria-label="Перейти к форме контакта">` (или добавить `tabindex="0" role="button"` + обработчик keydown Enter), чтобы элемент был доступен с клавиатуры и читался скрин-ридером
EFFECT: доступность (WCAG 2.1.1), кликабельная зона работает по Tab+Enter, меньше отказов мобильных/клавиатурных пользователей
RISK: стили `.visual` рассчитаны на div — может потребоваться `display:block` и сброс текстового подчёркивания ссылки
ROLLBACK: `git checkout -- index.html`
VERIFY: открыть страницу, нажать Tab — элемент должен получать фокус и срабатывать по Enter; проверить в DevTools Accessibility tree
PRIORITY: 1 — прямое нарушение доступности интерактивного элемента, правка на одну строку

IDEA: prefers-reduced-motion для particles/reveal/magnetic
KNOB: в `<style>` добавить блок `@media (prefers-reduced-motion: reduce){ #particles{display:none} .reveal{transition:none;opacity:1;transform:none} .magnetic{transform:none} *{animation-duration:.01ms!important} }`
EFFECT: пользователи с вестибулярными нарушениями не получают анимации; плюс Lighthouse a11y-балл
RISK: частицы и reveal-эффекты исчезнут у части пользователей — визуально проще, но не сломается
ROLLBACK: `git checkout -- index.html`
VERIFY: DevTools → Rendering → Emulate CSS media feature prefers-reduced-motion → убедиться, что анимации отключены и контент виден
PRIORITY: 2 — стандартная a11y-практика, нулевой риск для контента

IDEA: og:image + og:image:alt для шаринга в мессенджерах
KNOB: в `<head>` добавить `<meta property="og:image" content="https://<домен>/og-cover.png">` (1200×630, тёмный фон, h1-текст, бренд-цвет #8b5cf6) и `<meta property="og:image:alt" content="Савелий — лендинги для бизнеса в Перми за 2 дня">`; домен подставить реальный (требует решения владельца — картинку нужно создать и захостить)
EFFECT: при отправке ссылки в Telegram/WhatsApp/ВК появляется карточка с картинкой → выше CTR на ссылку
RISK: без реального домена и файла мета-тег будет вести на несуществующий URL — добавить только после размещения
ROLLBACK: `git checkout -- index.html`
VERIFY: вставить URL в https://developers.facebook.com/tools/debug/ или просто
