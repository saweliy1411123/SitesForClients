# localhost:8080/ovh/gpt-oss-120b  2026-11-17 02:15:44
duration=49.3 error=- attempts=1

IDEA: Preload critical CSS to eliminate render‑blocking  
KNOB: В `<head>` добавить `<link rel="preload" as="style" href="style.css" onload="this.rel='stylesheet'">` и оставить существующий `<link rel="stylesheet" href="style.css">` как fallback  
EFFECT: Сокращение FCP ≈ 15‑20 % → быстрее отображение первого экрана, лучше Core Web Vitals  
RISK: Если путь к CSS неверен, стили не загрузятся → страница без стилей  
ROLLBACK: Удалить добавленную строку `<link rel="preload"...>` (git checkout index.html)  
VERIFY: Открыть DevTools → Network, убедиться, что файл CSS помечен как “preload” и применяется без ошибки; измерить FCP в Lighthouse (меньше, чем до)  
PRIORITY: 1 — критический фактор скорости и SEO  

IDEA: Перенести единственный скрипт в defer‑режим  
KNOB: В `<script src="..."></script>` добавить атрибут `defer` (или `async` если нет зависимостей)  
EFFECT: Скрипт будет загружаться параллельно и выполнится после построения DOM, уменьшая время до интерактивности (TTI)  
RISK: Если скрипт зависит от элементов, размещённых после него, может возникнуть ошибка → проверить порядок выполнения  
ROLLBACK: Удалить `defer` (git checkout index.html)  
VERIFY: В Console отсутствие ошибок; в Lighthouse → показатели “Avoid large layout shifts” и “Reduce JavaScript execution time” улучшатся  
PRIORITY: 1 — ускоряет загрузку и повышает Core Web Vitals  

IDEA: Добавить `rel="noopener noreferrer"` к внешним ссылкам (Telegram, VK)  
KNOB: Для всех `<a href="https://t.me/..." target="_blank">` добавить `rel="noopener noreferrer"`  
EFFECT: Повышение безопасности (защита от reverse‑tabnabbing) и небольшое улучшение SEO‑оценки по рекомендациям Google  
RISK: Нет, изменение безопасно  
ROLLBACK: Удалить атрибут `rel` (git checkout index.html)  
VERIFY: Проверить в DevTools → Elements, атрибут присутствует; выполнить клик, убедиться, что открывается новое окно без доступа к `window.opener`  
PRIORITY: 2 — безопасность и небольшое SEO‑повышение  

IDEA: Обернуть hero‑секцию в семантический `<header>` с ролью banner  
KNOB: Вокруг блока с h1, подзаголовком и CTA заменить `<section class="hero">` (или аналог) на `<header class="hero" role="banner">`  
EFFECT: Улучшение семантики для скрин‑ридеров и поисковых роботов, повышает доступность и SEO‑структуру страницы  
RISK: Никакого визуального изменения, если CSS использует только класс  
ROLLBACK: Вернуть прежний `<section>` (git checkout index.html)  
VERIFY: В DevTools проверить, что элемент теперь `<header>`; запустить axe‑core (bookmarklet) – отсутствие ошибок “Landmark region missing”  
PRIORITY: 2 — семантика и доступность  

IDEA: Добавить `aria-live="polite"` к фиксированной панели CTA, чтобы объявлять её появление скрин‑ридерам  
KNOB: В элемент `<div class="sticky-cta">` добавить атрибут `aria-live="polite"`  
EFFECT: Пользователи скрин‑ридеров получат уведомление о появлении CTA при прокрутке, повышая конверсию для людей с ограниченным зрением  
RISK: Небольшой риск «запутывающих» сообщений, если панель появляется часто; но панель появляется один раз → приемлемо  
ROLLBACK: Удалить атрибут (git checkout index.html)  
VERIFY: Включить VoiceOver/NVDA, прокрутить страницу, убедиться, что объявление появляется без лишних повторов  
PRIORITY: 2 — доступность и потенциальный рост конверсии  

IDEA: Добавить JSON‑LD `ContactPoint` для Telegram‑контакта (LocalBusiness)  
KNOB: В конец `<body>` вставить `<script type="application/ld+json">{"@context":"https://schema.org","@type":"LocalBusiness","name":"Савелий","areaServed":"Пермь","contactPoint":[{"@type":"ContactPoint","contactType":"customer service","telephone":"+7XXXXXXXXXX","availableLanguage":["Russian"],"url":"https://t.me/TrainersDontPlays"}]}</script>`  
EFFECT: Поисковые системы получают точную информацию о способе связи → улучшение локального SEO и появление в результатах “Связаться”  
RISK: Требует актуального номера телефона; если номер изменится, разметка будет устаревать → требуется поддержка владельцем  
ROLLBACK: Удалить скрипт (git checkout index.html)  
VERIFY: Прогнать страницу в Google Rich Results Test; увидеть успешно распознанный ContactPoint без ошибок  
PRIORITY: 1 — прямой SEO‑бонус для локального поиска  

IDEA: Добавить `prefetch` для будущих ресурсов демо‑скриншотов (если планируются)  
KNOB: В `<head>` добавить `<link rel="prefetch" href="assets/demo-1.png" as="image">` (аналогично для остальных)  
EFFECT: При переходе к секции демо‑концептов браузер уже начнёт загружать изображения, ускоряя их отображение → лучшее UX и потенциальный CLS‑положительный эффект  
RISK: Если ресурсов много, может увеличить трафик без необходимости; использовать только для критичных → ограничить 1‑2 файлами  
ROLLBACK: Удалить строки `<link rel="prefetch"...>` (git checkout index.html)  
VERIFY: В Network‑панели увидеть запросы `prefetch` сразу после загрузки страницы; измерить CLS до и после (меньше)  
PRIORITY: 3 — улучшение UX, но менее критично, чем скорость первой отрисовки  

IDEA: Добавить мета‑тег `viewport-fit=cover` для корректного отображения на iOS‑устройствах с вырезом (notch)  
KNOB: В существующий `<meta name="viewport" content="width=device-width, initial-scale=1">` добавить `, viewport-fit=cover` → `<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">`  
EFFECT: Полноэкранный контент будет правильно растягиваться под вырезы, улучшая мобильный UX и шанс снижения Bounce Rate  
RISK: Нет, совместимо со всеми современными браузерами  
ROLLBACK: Вернуть оригинальный мета‑тег (git checkout index.html)  
VERIFY: Открыть страницу на iPhone (или эмулятор), убедиться, что контент не обрезается под вырезом; проверка в DevTools → Device Toolbar  
PRIORITY: 3 — небольшое улучшение мобильного отображения, не критично для SEO, но повышает UX.
