# localhost:8080/ovh/gpt-oss-120b  2026-11-17 06:19:21
duration=37.7 error=- attempts=1

IDEA: Hero‑benefits‑list — четыре коротких пункта‑подсказки под <h1>  
KNOB: в `.hero .wrap` сразу после `<h1>` добавить `<ul class="hero‑benefits"><li>Первые заявки уже в 1‑й день</li><li>Оптимизировано под Яндекс Search</li><li>Мобильный адаптив — 100 % конверсия</li><li>Гарантия быстрого запуска</li></ul>` и в CSS задать `ul.hero‑benefits{display:flex;gap:1rem;flex-wrap:wrap;list-style:none;margin-top:1rem;font-size:clamp(14px,2vw,16px);color:var(--muted)}`.  
EFFECT: мгновенно повышает ясность оффера, повышает время‑на‑странице и CTR CTA за счёт визуального доказательства ценности.  
RISK: небольшое увеличение HTML‑размера (≈200 Б) и возможно «переполнение» на очень маленьких экранах.  
ROLLBACK: `git checkout -- index.html` (или удалить только вставку `<ul class="hero‑benefits">…</ul>`).  
VERIFY: открыть страницу, убедиться, что список виден под заголовком, проверить в DevTools → Elements, а также измерить CLS до/после (должен оставаться < 0.1).  
PRIORITY: 1 — ключевой блок первого экрана, влияет на восприятие оффера и SEO‑поведенческие сигналы.  

IDEA: FAQ‑accordion‑semantic — заменить текущие блоки `<div class="faq-item">` на `<details class="faq-item"><summary>Вопрос</summary>Ответ…</details>`  
KNOB: в секции `#faq` заменить каждый вопрос‑ответ на `<details class="faq-item"><summary>Текст вопроса</summary><p>Текст ответа</p></details>`; добавить в CSS `details.faq-item{margin-bottom:1rem;cursor:pointer} details[open] summary{font-weight:600}` и `summary{outline:none}`.  
EFFECT: улучшает семантику, ускоряет загрузку (меньше JavaScript), повышает доступность (скрин‑ридеры читают summary), упрощает мобильный UX (только один клик).  
RISK: если стили уже зависят от классов `.faq-item h3`, потребуется небольшая корректировка CSS.  
ROLLBACK: `git checkout -- index.html` (или вернуть оригинальные `<div>`‑блоки).  
VERIFY: в браузере кликнуть по каждому вопросу — ответ раскрывается; проверить отсутствие JS‑ошибок в Console; выполнить `document.querySelectorAll('details[open]').length` — ожидаем 0 до взаимодействия.  
PRIORITY: 1 — семантика и доступность критичны для SEO и конверсии в FAQ‑разделе.  

IDEA: FAQ‑JSON‑LD — добавить структурированную разметку FAQPage для поисковых подсказок  
KNOB: в `<head>` вставить `<script type="application/ld+json">{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"<вопрос 1>","acceptedAnswer":{"@type":"Answer","text":"<ответ 1>"}},…]}` (сгенерировать из текущих вопросов/ответов).  
EFFECT: повышает шанс появления в Google Rich Snippets, увеличивает органический CTR без изменения UI.  
RISK: требуется точное соответствие реальному контенту; ошибки в JSON‑LD могут вызвать предупреждения в Search Console.  
ROLLBACK: удалить вставленный `<script>`‑блок (или `git checkout -- index.html`).  
VERIFY: открыть Chrome DevTools → Console, выполнить `JSON.parse(document.querySelector('script[type="application/ld+json"]').textContent)` — должен быть валидный объект; в Search Console → Rich Results проверить валидность.  
PRIORITY: 2 — высокий SEO‑эффект, но не влияет напрямую на UI, поэтому средний приоритет.  

IDEA: Scroll‑progress‑indicator — полоска‑прогресса в верхней части страницы, показывающая, сколько контента уже просмотрено  
KNOB: добавить в `<body>` сразу после `<header>` элемент `<div class="scroll‑progress"><div class="scroll‑track"></div></div>`; в CSS:  
```css
/* SAFE CSS */
.scroll-progress{position:fixed;top:0;left:0;width:100%;height:4px;background:rgba(0,0,0,0.1);z-index:9999}
.scroll-track{height:100%;width:0;background:var(--blue);transition:width .2s ease}
```  
и в `<script>` внизу добавить:  
```js
document.addEventListener('scroll',()=>{const d=document.documentElement;const scrolled=(d.scrollTop||body.scrollTop)/(d.scrollHeight-d.clientHeight)*100;document.querySelector('.scroll-track').style.width=`${scrolled}%`;});
```  
EFFECT: визуальный индикатор вовлечённости, повышает восприятие «прогресса» и мотивирует к дальнейшему скроллингу, улучшает UX на длинных страницах.  
RISK: небольшая нагрузка на JS при каждом скролле (но микросекундная).  
ROLLBACK: удалить добавленные HTML‑/CSS‑/JS‑блоки или `git checkout -- index.html`.  
VERIFY: открыть страницу, прокручивать вниз — полоска должна заполняться; в Console проверить отсутствие ошибок.  
PRIORITY: 2 — модернизирует UX, но не критично для конверсии.  

IDEA: Skip‑link — скрытая ссылка в начале страницы для перехода сразу к главному контенту (повышает доступность)  
KNOB: в `<body>` сразу после открывающего `<header>` добавить `<a href="#main" class="skip-link">Перейти к содержимому</a>`; в CSS:  
```css
/* SAFE CSS */
.skip-link{position:absolute;top:-40px;left:0;background:#fff;color:#000;padding:8px;z-index:100;transition:top .3s}
.skip-link:focus{top:0}
```  
и обернуть основной контент (от первой `<section>` до конца) в `<main id="main">…</main>`.  
EFFECT: улучшает навигацию клавиатурой и скрин‑ридерами, повышает оценку доступности (WCAG 2.1 AA), может положительно сказаться на SEO‑рейтинге.  
RISK: требуется небольшое изменение структуры (добавление `<main>`), может потребовать корректировки стилей, если где‑то использовался `section`‑селектор без контекста.  
ROLLBACK: удалить `<a>` и `<main>`‑обёртку, либо `git checkout -- index.html`.  
VERIFY: нажать Tab при загрузке страницы — первая фокус‑точка должна быть на «Перейти к содержимому»; после нажатия Enter переход к `#main`. Проверить в Accessibility панели DevTools, что элемент отмечен как «skip link».  
PRIORITY: 1 — доступность критична, особенно для одностраничных лендингов, и не требует затрат.  

IDEA: Стоимость‑в‑долларах — добавить автоматический конвертер цены в USD для международных посетителей  
KNOB: в `.price-card .per` (где указана цена в RUB) добавить `<span class="price-rub">12 000 ₽</span><span class="price-usd" data-rub="12000"></span>`; в CSS: ` .price-usd{margin-left:.5rem;color:var(--muted);font-size:.9em;}`; в JS‑блоке внизу добавить:  
```js
fetch('https://api.exchangerate.host/latest?base=RUB&symbols=USD')
 .then(r=>r.json())
 .then(d=>{document.querySelectorAll('.price-usd').forEach(el=>{const rub=+el.dataset.rub;el.textContent=`≈ $${(rub*d.rates.USD).toFixed(0)}`});})
 .catch(()=>{});
```  
EFFECT: повышает доверие иностранных клиентов, раскрывает потенциальный рынок, улучшает восприятие цены без изменения основной бизнес‑модели.  
RISK: зависит от внешнего API (может быть недоступен); требуется подключение к сети, но без передачи личных данных.  
ROLLBACK: удалить добавленные `<span class="price-usd">` и JS‑скрипт (или `git checkout -- index.html`).  
VERIFY: открыть страницу, переключить VPN/локаль на не‑RU; убедиться, что рядом с ценой появляется «≈ $…». Проверить отсутствие ошибок в Console.  
PRIORITY: 3 — модный, но не критичный для локального бизнес‑офера; реализуется быстро, но имеет внешнюю зависимость.
