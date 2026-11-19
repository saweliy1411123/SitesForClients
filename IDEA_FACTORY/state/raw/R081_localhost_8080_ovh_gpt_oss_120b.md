# localhost:8080/ovh/gpt-oss-120b  2026-11-17 05:36:31
duration=34.0 error=- attempts=1

IDEA: Back‑to‑top sticky button with accessibility support  
KNOB: В конец `<body>` добавить `<a href="#" class="back-to-top" aria-label="Вернуться к началу страницы">↑</a>`; в CSS `.back-to-top{position:fixed;right:1rem;bottom:1rem;display:none;z-index:1000;padding:0.6rem 0.8rem;background:rgba(0,0,0,0.6);color:#fff;border-radius:0.4rem;transition:opacity .3s;} .back-to-top:focus-visible{outline:2px solid #fff;} @media (prefers-reduced-motion:reduce){.back-to-top{transition:none;}}` и JS `window.addEventListener('scroll',()=>{document.querySelector('.back-to-top').style.display=window.scrollY>400?'block':'none'});document.querySelector('.back-to-top').addEventListener('click',e=>{e.preventDefault();window.scrollTo({top:0,behavior:'smooth'});});`  
EFFECT: Уменьшает отток пользователей, повышает среднее время на странице и конверсию, особенно на длинных страницах.  
RISK: Минимальный риск конфликтов со стилями — может потребоваться корректировать z‑index.  
ROLLBACK: `git checkout -- index.html && git checkout -- index.improved.html` (если правки внесены в копию)  
VERIFY: Открыть страницу, прокрутить более 400 px — кнопка должна появиться; клик — плавный скролл к верху; проверить `tab`‑фокус.  
PRIORITY: 1 — высокий ROI за небольшие изменения, улучшает UX и SEO (повышает dwell‑time).  

IDEA: JSON‑LD Offer schema для блока цены  
KNOB: В конец `<body>` вставить `<script type="application/ld+json">{"@context":"https://schema.org","@type":"Offer","price":"29900","priceCurrency":"RUB","availability":"https://schema.org/InStock","url":"#price","seller":{"@type":"LocalBusiness","name":"Савелий","address":{"@type":"PostalAddress","addressLocality":"Пермь","addressCountry":"RU"}}}</script>`  
EFFECT: Позволяет поисковикам показать ценовое предложение в результатах, повышая CTR и доверие.  
RISK: Требует актуализации цены/валюты при изменении предложения (владельцу).  
ROLLBACK: Удалить вставленный `<script>`‑блок или выполнить `git checkout -- index.html`.  
VERIFY: В Chrome DevTools → «Structured Data Testing Tool» проверить наличие Offer без ошибок.  
PRIORITY: 1 — прямое SEO‑повышение и потенциальный рост заявок.  

IDEA: Preconnect + dns‑prefetch для Google Fonts и статических ресурсов  
KNOB: В `<head>` добавить строки:  
```html
<link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="dns-prefetch" href="//fonts.googleapis.com">
<link rel="dns-prefetch" href="//fonts.gstatic.com">
```  
EFFECT: Сокращает время первого рендеринга шрифтов, уменьшает CLS и ускоряет загрузку.  
RISK: Небольшой рост количества запросов в head; безвредно.  
ROLLBACK: Удалить добавленные `<link>`‑теги; `git checkout -- index.html`.  
VERIFY: В Chrome DevTools → Network → проверка, что запросы к fonts выполняются после preconnect без задержек; измерить LCP до/после.  
PRIORITY: 2 — быстрый выигрыш в Core Web Vitals без изменения UI.  

IDEA: Телефонный CTA в шапке для мгновенного звонка  
KNOB: Внутри `<header>` (или навигации) добавить `<a href="tel:+73412345678" class="header-phone btn-primary" aria-label="Позвонить сейчас">📞 8 (3412) 34‑56‑78</a>`; в CSS `.header-phone{margin-left:auto;padding:0.4rem 0.8rem;background:#8b5cf6;color:#fff;border-radius:0.4rem;}`  
EFFECT: Позволяет пользователям сразу связаться по телефону, повышая конверсию на мобильных.  
RISK: Требует наличия рабочего телефонного номера; может выглядеть избыточно, если уже есть CTA‑кнопка в hero.  
ROLLBACK: Удалить добавленный `<a>` и связанные стили; `git checkout -- index.html`.  
VERIFY: Открыть страницу на мобильном устройстве, кликнуть на телефонный линк — должно открыться приложение звонка. Проверить доступность через `Tab`.  
PRIORITY: 2 — модернизирует контактный путь, особенно для локального бизнеса.  

IDEA: Канонический URL для предотвращения дублей контента  
KNOB: В `<head>` добавить `<link rel="canonical" href="https://example.com/">` (заменить `example.com` на реальный домен).  
EFFECT: Укрепляет SEO‑вес страницы, предотвращает проблемы с дублированием, помогает поисковикам правильно индексировать.  
RISK: Неправильный URL может навредить; требует уточнения у владельца.  
ROLLBACK: Удалить строку `<link rel="canonical"...>`; `git checkout -- index.html`.  
VERIFY: В Chrome DevTools → «View source» убедиться в наличии тега; в Search Console проверить отсутствие ошибок.  
PRIORITY: 3 — важно для SEO, но менее критично для конверсии, поэтому отложено после быстрых UX‑улучшений.
