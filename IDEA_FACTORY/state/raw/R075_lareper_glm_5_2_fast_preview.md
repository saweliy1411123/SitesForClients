# lareper/glm-5.2-fast-preview  2026-11-17 05:19:55
duration=2.5 error=- attempts=1

IDEA: FAQPage JSON-LD разметка для rich results в Яндексе/Google
KNOB: В конец `<body>` (рядом с будущим Service JSON-LD) добавить `<script type="application/ld+json">` с `@type: FAQPage` и `mainEntity` — по 3–5 реальных вопросов/ответов, скопированных дословно из секции FAQ (L663–705), без выдуманных фактов.
EFFECT: Шанс расширенного сниппета (вопросы прямо в выдаче) → выше CTR по запросам «лендинг Пермь вопросы/цена».
RISK: Если текст ответов в JSON-LD разойдётся с видимым текстом — поисковик может игнорировать разметку.
ROLLBACK: `git checkout -- index.html` (или удалить блок скрипта в копии).
VERIFY: Вставить JSON в validator.schema.org → 0 ошибок; в Rich Results Test URL — тип FAQPage распознан.
PRIORITY: 1 — дёшево, усиливает уже существующую секцию FAQ и локальное SEO.

IDEA: Skip-link «Перейти к содержимому» для клавиатуры и скринридеров
KNOB: Первым элементом внутри `<body>` добавить `<a class="skip-link" href="#main">Перейти к содержимому</a>`; на `<main>` (или обёртку контента после `<header class="hero">`) повесить `id="main" tabindex="-1"`; CSS: `.skip-link{position:absolute;left:-9999px} .skip-link:focus{left:16px;top:16px;z-index:100;padding:10px 16px;background:var(--blue);color:#fff;border-radius:8px}`.
EFFECT: Пользователи клавиатуры (и мобильные с внешней клавиатурой) пропускают навигацию — первый Tab сразу к контенту; плюс WCAG 2.4.1.
RISK: Минимальный — нужен корректный `id="main"` и видимый фокус, иначе линк «мёртвый».
ROLLBACK: Удалить добавленную ссылку и CSS-блок.
VERIFY: Открыть страницу, нажать Tab — первым фокусом должен стать skip-link; второй Tab/Enter — прокрутка к контенту.
PRIORITY: 2 — стандартный a11y-паттерн, 10 минут работы.

IDEA: prefers-reduced-motion — отключение reveal/blob-анимаций
KNOB: В `<style>` добавить медиа-блок: `@media (prefers-reduced-motion: reduce){ *,*::before,*::after{animation-duration:.01ms !important;animation-iteration-count:1 !important;transition-duration:.01ms !important} .reveal{opacity:1;transform:none} }` — охватывает blobs, reveal/zoom-переходы (L461, L644 и др.).
EFFECT: Пользователи с вестибулярной чувствительностью видят контент сразу без движения; контент не «застревает» прозрачным, если JS reveal не сработал.
RISK: Пропадает «живость» для этой группы пользователей — визуально страница статичнее.
ROLLBACK: Удалить один медиа-блок из CSS.
VERIFY: DevTools → Ctrl+Shift+P → «Emulate prefers-reduced-motion: reduce» → перезагрузить: блобы и reveal-анимации отключены, весь текст вид
