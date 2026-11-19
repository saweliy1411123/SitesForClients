# localhost:8080/ovh/gpt-oss-120b  2026-11-17 03:32:27
duration=38.3 error=- attempts=1

IDEA: Structured‑Data Offer Schema for Hero CTA  
KNOB: В конец `<head>` добавить `<script type="application/ld+json">` с объектом `@type":"Offer"` (offerDescription из <h1>, price из price‑card, availability "InStock", url из href‑ссылки CTA).  
EFFECT: Повышает видимость в поиске (rich snippet), усиливает доверие и кликабельность.  
RISK: Требует корректных данных — если цена изменится, JSON‑LD надо обновлять.  
ROLLBACK: `git checkout index.html` (или удалить добавленный `<script>`).  
VERIFY: Открыть страницу в Chrome DevTools → «Structured Data Testing Tool», убедиться в валидности Offer.  
PRIORITY: 1 – быстрый ROI, улучшает SEO без кода‑бэкенда.  
SITE_REQUEST: hero  

---  

IDEA: Accessible SVG Icons with ARIA‑label для блока боли  
KNOB: В секции «Боль» (h2 «Запись есть — клиентов из поиска нет») добавить к каждому `<svg>` атрибут `aria-label="Иконка …"` и `role="img"`; при необходимости обернуть в `<span class="sr-only">…</span>` для описания.  
EFFECT: Улучшает доступность для скрин‑ридеров, повышает восприятие доверия.  
RISK: Увеличит размер HTML ≈ 30 Б, но незначительно.  
ROLLBACK: Удалить добавленные `aria-label`/`role`/`<span>` элементы.  
VERIFY: Включить «Screen Reader» в Chrome DevTools → проверка читаемости элементов.  
PRIORITY: 2 – низкая сложность, важна для a11y и SEO.  
SITE_REQUEST: боль  

---  

IDEA: CSS‑Counter Step Numbers в секции «Три шага»  
KNOB: В `.steps` добавить `counter-reset: step;` и к каждому элементу шага (`.step-item`) задать `counter-increment: step;` и псевдо‑элемент `::before {content: counter(step);}` стилизовать как круг.  
EFFECT: Визуальная нумерация упрощает восприятие процесса, повышает конверсию.  
RISK: Если структура HTML изменится, счётчик может «сломаться».  
ROLLBACK: Удалить добавленные CSS‑правила.  
VERIFY: Открыть страницу, убедиться, что перед каждым шагом появляется номер.  
PRIORITY: 2 – мало кода, заметный UX‑эффект.  
SITE_REQUEST: steps  

---  

IDEA: Lazy‑loaded Video‑Preview для каждого демо‑концепта  
KNOB: В секции «Демо‑концепты» под каждый блок добавить `<video preload="metadata" poster="thumb.jpg" class="demo-video" muted loop playsinline><source src="demo.mp4" type="video/mp4"></video>` и в CSS `video{opacity:0;transition:opacity .3s}` + JS‑интерсекшон Observer для установки `src` при появлении в viewport.  
EFFECT: Демонстрирует реальный результат, увеличивает время на странице лишь при просмотре, повышает конверсию.  
RISK: Требует размещения видеоматериалов – может увеличить хостинг‑расходы.  
ROLLBACK: Удалить `<video>`‑блоки и скрипт‑observer.  
VERIFY: Открыть страницу, прокрутить до демо‑блока, убедиться, что видео стартует только после появления в зоне видимости.  
PRIORITY: 2 – сильный визуальный аргумент, но требует контента.  
SITE_REQUEST: демо  

---  

IDEA: Money‑Back Guarantee Badge в ценообразовании  
KNOB: Внутри `.price-card` под кнопкой CTA добавить `<div class="guarantee-badge"><svg …></svg> <span>Гарантия возврата денег 30 дней</span></div>` и стилизовать badge (фон #fff, border 1px solid var(--blue), небольшая тень).  
EFFECT: Снимает страх перед покупкой, повышает доверие и конверсию.  
RISK: Требует реального условия возврата; если не предоставляется – юридический риск.  
ROLLBACK: Удалить добавленный `<div class="guarantee-badge">`.  
VERIFY: Визуально проверить наличие бейджа и корректность текста.  
PRIORITY: 1 – прямой сигнал доверия, быстрый клик‑through.  

---  

IDEA: Accordion FAQ на <details>/<summary>  
KNOB: В секции FAQ заменить текущий список вопросов на набор `<details class="faq-item"><summary>Вопрос?</summary><p>Ответ.</p></details>`; добавить базовый CSS для плавный переход и индикатор «+».  
EFFECT: Уменьшает высоту страницы на мобильных, улучшает сканируемость, повышает UX.  
RISK: Старые браузеры (IE) не поддерживают <details>, но их доля <1 % в целевой аудитории.  
ROLLBACK: Вернуть оригинальный HTML‑список вопросов.  
VERIFY: Открыть страницу на мобильном, кликнуть вопрос – должен раскрыться.  
PRIORITY: 2 – незначительные изменения, улучшает мобильный UX.  
SITE_REQUEST: FAQ  

---  

IDEA: Persistent Bottom CTA для моб‑версии с auto‑hide при скролле вниз  
KNOB: Добавить в конец `<body>` `<div class="mobile-cta sticky-bottom" role="region" aria-label="Бесплатное демо"><a href="#contact" class="btn-primary">Получить демо бесплатно</a></div>`; в CSS `position:fixed;bottom:0;width:100%;transform:translateY(0);transition:transform .3s;` + JS‑IntersectionObserver для скрытия, когда пользователь скроллит вниз более 200 px и показывать при скролле вверх.  
EFFECT: Поддерживает CTA в поле зрения, повышает конверсию на мобильных, не мешает контенту.  
RISK: Требует небольшого JS‑кода; если отключить JS, элемент будет всегда виден (не критично).  
ROLLBACK: Удалить добавленный `<div>` и JS‑файл/скрипт.  
VERIFY: На мобильном открыть страницу, прокрутить вниз – CTA исчезнет, прокрутить вверх – появится.  
PRIORITY: 1 – мощный мобильный драйвер конверсий.  
SITE_REQUEST: cta  

---  

IDEA: “Skip‑to‑Content” ссылка для быстрого перехода к основному контенту  
KNOB: Сразу после открывающего `<body>` вставить `<a href="#main" class="skip-link">Перейти к содержимому</a>`; добавить CSS `.skip-link{position:absolute;top:-40px;left:0;background:#fff;color:#000;padding:8px;z-index:1000;transition:top .3s;} .skip-link:focus{top:0;}` и в основной контент добавить `<main id="main">`.  
EFFECT: Улучшает навигацию клавиатурой и доступность, положительно влияет на SEO‑оценку.  
RISK: Минимальный; может слегка увеличить HTML‑размер.  
ROLLBACK: Удалить `<a>` и CSS‑правило, вернуть прежнюю структуру.  
VERIFY: Нажать Tab сразу после загрузки страницы – ссылка должна появиться в фокусе; клик – перейти к `<main>`.  
PRIORITY: 2 – быстрый a11y‑апгрейд, полезен для всех пользователей.  
SITE_REQUEST: main
