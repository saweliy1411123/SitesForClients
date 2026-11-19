# localhost:8080/ovh/gpt-oss-120b  2026-11-17 01:50:26
duration=29.7 error=- attempts=1

IDEA: Добавить JSON‑LD разметку FAQPage для секции FAQ  
KNOB: В конец `<body>` вставить `<script type="application/ld+json">…</script>` со списком вопросов и ответов, взятых из текущих `<h3>`/`<p>` в секции FAQ.  
EFFECT: Улучшит видимость в поиске (Google покажет расширенный сниппет), повысит CTR и подтверждает экспертизу.  
RISK: Если вопросы/ответы не совпадают с разметкой, может возникнуть предупреждение в Search Console.  
ROLLBACK: Удалить только добавленный `<script>`‑блок (git checkout -- index.html).  
VERIFY: Открыть https://search.google.com/structured-data/testing-tool/u/0/ и проверить отсутствие ошибок; убедиться, что в результатах появляется блок FAQ.  
PRIORITY: 1 — высокий SEO‑выигрыш без изменений контента.  

IDEA: Внедрить схему LocalBusiness (Service) для повышения локального SEO  
KNOB: В `<head>` добавить `<script type="application/ld+json">` с `@type: "LocalBusiness"`; заполнить `name: "Савелий"`, `address` (Пермь), `telephone`, `url`, `serviceType: "Создание лендингов"`, `areaServed`.  
EFFECT: Поисковые системы лучше ассоциируют сайт с регионом, повышая позиции в Яндекс и Google по запросам «лендинг в Перми».  
RISK: Нужно использовать только достоверные данные; неверный телефон/адрес вызовет штраф.  
ROLLBACK: Удалить скрипт‑блок (git checkout -- index.html).  
VERIFY: Прогнать страницу в Structured Data Testing Tool; убедиться в статусе “Valid”.  
PRIORITY: 1 — локальный SEO‑трафик критичен для бизнеса.  

IDEA: Ускорить загрузку шрифтов через preconnect и font-display swap  
KNOB: В `<head>` добавить `<link rel="preconnect" href="https://fonts.googleapis.com">` и `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>`. В уже подключаемом Google‑Fonts URL добавить `&display=swap`.  
EFFECT: Сократит время до первого отображения текста (CLS ↓, LCP ↓), улучшит Core Web Vitals.  
RISK: Небольшой рост количества запросов (2 preconnect), но без влияния на функциональность.  
ROLLBACK: Удалить добавленные `<link>`‑теги и вернуть оригинальный URL шрифта (git checkout -- index.html).  
VERIFY: В Chrome DevTools → Network → check “Initiator” for fonts; измерить LCP до/после (Lighthouse).  
PRIORITY: 1 — быстрый выигрыш в скорости без кода.  

IDEA: Добавить «skip‑to‑content» ссылку и aria‑метки для лучшей доступности  
KNOB: В начале `<body>` вставить `<a href="#main" class="skip-link">Перейти к содержимому</a>`; у главного контейнера добавить `id="main"` и `role="main"`. У CTA‑ссылок добавить `aria-label="Получить демо‑макет в Telegram"` и `role="button"` при необходимости.  
EFFECT: Улучшит навигацию клавиатурой для пользователей скрин‑ридеров, повысит показатель WCAG‑AA.  
RISK: Неправильный `href` может привести к «потерянному» фокусу; проверка обязательна.  
ROLLBACK: Удалить вставленную ссылку и атрибуты (git checkout -- index.html).  
VERIFY: Нажать Tab в браузере, убедиться, что первая ссылка видна и переводит в основной контент; проверить в Lighthouse “Accessibility”.  
PRIORITY: 2 — важный для инклюзивности, но не критичен к конверсии.  

IDEA: Заменить основной CTA‑ссылка на семантическую кнопку с клиент‑сайд редиректом в Telegram  
KNOB: В секции hero заменить `<a class="btn-primary magnetic" href="#contact">…</a>` на `<button class="btn-primary magnetic" id="cta-demo">…</button>` и добавить в конец `<script>` небольшую JS‑функцию: `document.getElementById('cta-demo').addEventListener('click',()=>{location.href='https://t.me/your_username';});`.  
EFFECT: Улучшит семантику (кнопка → действие), позволит добавить анимацию/отслеживание без изменения URL, повышает доступность (focus/enter).  
RISK: Требует небольшого JS; если пользователь отключил скрипты, CTA не сработает → добавить fallback `<noscript><a href="https://t.me/your_username">…</a></noscript>`.  
ROLLBACK: Вернуть оригинальный `<a>` (git checkout -- index.html).  
VERIFY: Кликнуть кнопку, убедиться в переходе в Telegram; отключить JS в браузере и проверить наличие fallback‑ссылки.  
PRIORITY: 2 — семантика и возможность аналитики, но не критично.  

IDEA: Добавить фиксированную панель‑CTA при прокрутке (sticky)  
KNOB: В конец `<body>` добавить `<div class="sticky-cta" aria-live="polite"><a href="https://t.me/your_username" class="btn-primary">Получить демо бесплатно</a></div>`; в CSS: `.sticky-cta{position:fixed;bottom:0;left:0;width:100%;background:#fff;box-shadow:0 -2px 8px rgba(0,0,0,0.1);display:flex;justify-content:center;padding:0.5rem;z-index:1000;}` и `@media (min-width:768px){.sticky-cta{display:none;}}`.  
EFFECT: Увеличит количество кликов по CTA на длинных страницах, особенно на мобильных устройствах.  
RISK: Может восприниматься как навязчивая реклама; нужно обеспечить достаточный контраст и возможность закрыть (добавить кнопку закрытия).  
ROLLBACK: Удалить вставленный HTML и CSS (git checkout -- index.html).  
VERIFY: Прокрутить страницу на мобильном эмуляторе, убедиться в появлении панели и её кликабельности; измерить CTR через быстрый локальный клик‑трекинг (консоль).  
PRIORITY: 3 — потенциальный рост конверсии, но требует UX‑тестов.  

IDEA: Добавить canonical и robots meta‑теги для управления индексацией  
KNOB: В `<head>` добавить `<link rel="canonical" href="https://example.com/">` (заменить на реальный URL) и `<meta name="robots" content="index,follow">`.  
EFFECT: Устранит дублирование URL, укрепит авторитет страницы в поиске.  
RISK: Если указать неправильный канонический URL, может потеряться трафик.  
ROLLBACK: Удалить теги (git checkout -- index.html).  
VERIFY: Открыть страницу в Chrome → View source → убедиться в наличии тегов; проверить в Google Search Console “URL Inspection”.  
PRIORITY: 2 — простая мера, повышающая SEO‑стабильность.  

IDEA: Добавить OG‑image для лучшего отображения в соцсетях  
KNOB: В `<head>` добавить `<meta property="og:image" content="https://example.com/assets/og-image.jpg">` и соответствующий `<meta property="og:image:alt" content="Савелий – лендинг за 2 дня">`. Подготовить небольшое (1.2 МБ) изображение с брендингом.  
EFFECT: При шаринге в соцсетях будет показываться привлекательный превью‑картинка, повышая кликабельность.  
RISK: Требуется загрузить файл на хост; если путь неверный, соцсети покажут пустой превью.  
ROLLBACK: Удалить мета‑теги (git checkout -- index.html).  
VERIFY: Использовать Facebook Sharing Debugger / Twitter Card Validator, проверить отображение.  
PRIORITY: 3 — повышает соц‑трафик, но не критично для текущего конверсионного пути.
