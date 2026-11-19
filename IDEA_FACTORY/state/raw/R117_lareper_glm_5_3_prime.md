# lareper/glm-5.3-prime  2026-11-17 07:24:51
duration=36.5 error=- attempts=1

IDEA: FAQPage JSON-LD сгенерированный из реальных FAQ-текстов страницы
KNOB: METHOD: (1) SITE_REQUEST «faq» — получить фактическую разметку FAQ-секции и тексты вопросов/ответов. (2) В `<head>` добавить `<script type="application/ld+json">` с @type FAQPage, где mainEntity — точные тексты вопросов и ответов, уже существующие на странице (без выдуманных). (3) Проверить в console: `JSON.parse(document.querySelector('script[type="application/ld+json"]').textContent)` — валидность. (4) Прогнать через Google Rich Results Test (или Яндекс.Вебмастер валидатор микроразметки) на локальной копии.
EFFECT: расширенный сниппет с вопросами в Яндексе/Google по запросам «лендинг пермь цена», больше кликов из поиска без изменения контента.
RISK: если разметка FAQ реализована JS-аккордеоном и ответы не в DOM, поисковик может не сопоставить schema с видимым контентом.
ROLLBACK: git checkout index.html
VERIFY: Rich Results Test / Яндекс.Вебмастер → «Проверка микроразметки» → 0 ошибок FAQPage; 3–5 минут.
PRIORITY: 1 — единственный крупный SEO-выигрыш, которого нет в куче (Breadcrumb/Service/LocalBusiness есть, FAQPage нет), а FAQ-секция уже существует.
SITE_REQUEST: faq

IDEA: Ленивая загрузка Google Fonts через media=print swap с сохранением FOUT-контроля
KNOB: В `<head>` заменить блокирующий `<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope...">` на пару: `<link rel="preload" as="style" href="...">` + `<link rel="stylesheet" href="..." media="print" onload="this.media='all'">` + `<noscript><link rel="stylesheet" href="..."></noscript>`. Preconnect к fonts.googleapis.com/fonts.gstatic.com уже есть — не трогать.
EFFECT: устранение render-blocking запроса шрифтов → LCP первого экрана быстрее на 200–500 мс на мобильных, что напрямую влияет на «быстро грузится» из оффера.
RISK: краткий FOUT (мигание системного шрифта) — при медленной сети заголовок на секунду отрисуется fallback-шрифтом.
ROLLBACK: git checkout index.html
VERIFY: DevTools → Network → перезагрузка с throttling Fast 3G: стилизованный рендер начинается до загрузки fonts.css; Lighthouse Performance до/после — 5 минут.
PRIORITY: 2 — заметный прирост скорости, но требует визуальной проверки FOUT; preload Manrope 600/700 (I-00672) частично пересекается — объединить в один коммит.

IDEA: Скрытая на мобильных навигация — чипсы-якоря с overflow-x (новое значение: семантика + a11y вместо только стиля)
KNOB: В `@media(max-width:720px)` (L90) заменить `.nav-links{display:none}` на: `.nav-links{display:flex;overflow-x:auto;-webkit-overflow-scrolling:touch;gap:12px;padding:8px 16px;position:fixed;top:0;left:0;right:0;background:var(--bg);z-index:50}` + `.nav-links a{white-space:nowrap;padding:8px 14px;border:1px solid rgba(255,255,255,.12);border-radius:99px;min-height:44px;display:flex;align-items:center}`. HTML не менять — ссылки уже в DOM (L438), просто станут видимыми и доступными с клавиатуры на мобильных.
EFFECT: на телефонах (основной трафик локального бизнеса) появляется навигация к цене/FAQ
