# localhost:8081/big_only  2026-11-17 17:16:44
duration=77.7 error=- attempts=1

IDEA: Benefit‑icons row under hero for instant offer clarity  
KNOB: Insert after `</header>` a `<section class="hero-benefits"><div class="benefit-item"><svg…></svg><p>2‑дневный запуск</p></div><div class="benefit‑item"><svg…></svg><p>SEO‑оптимизация</p></div><div class="benefit‑item"><svg…></svg><p>Поддержка 24/7</p></div></section>` and add CSS `.hero-benefits{display:flex;justify-content:center;gap:2rem;padding:1rem 0;background:rgba(var(--bg-rgb),0.6)} .benefit‑item{flex:1;text-align:center;font-size:clamp(14px,1.2vw,18px)} .benefit‑item svg{width:40px;height:40px;margin-bottom:0.5rem}`.  
EFFECT: Пользователь за 1‑2 секунды видит ключевые выгоды, повышается понятность оффера и коэффициент конверсии.  
RISK: Небольшой рост загрузки из‑за SVG‑иконок; требуется подобрать подходящие иконки.  
ROLLBACK: Удалить вставленный HTML‑блок и соответствующее CSS‑правило (git checkout HEAD -- path/to/file).  
VERIFY: Открыть страницу в десктоп‑ и мобильных режимах, убедиться, что блок отображается под хэдером, текст читаем‑ся, а Lighthouse ‘Performance’ не падает более 5 % от базовой версии.  
PRIORITY: 1 – высокий ROI при минимальном объёме работы.  

IDEA: Карусель логотипов клиентов для доверия  
KNOB: Перед секцией `#faq` добавить `<section class="client-logos"><div class="logo-track"><img src="logo1.svg" alt="Клиент 1"><img src="logo2.svg" alt="Клиент 2">…</div></section>` и CSS `.client-logos{overflow:hidden;padding:2rem 0;background:#fafafa}.logo-track{display:flex;gap:2rem;animation:scroll 20s linear infinite}@keyframes scroll{from{transform:translateX(0)}to{transform:translateX(-50%)}} .client-logos img{height:40px;object-fit:contain}`.  
EFFECT: Показ реальных клиентов усиливает социальное доказательство, повышает доверие и конверсию.  
RISK: Требуется собрать/оптимизировать логотипы; анимация может увеличить потребление CPU на слабых устройствах.  
ROLLBACK: Удалить HTML‑блок и CSS‑правила (git checkout HEAD -- path/to/file).  
VERIFY: Проверить в браузере, что логотипы плавно скроллятся, не вызывают «jank», и что время загрузки не превышает 3 сек.  
PRIORITY: 2 – средний эффект, но требует подготовки графики.  

IDEA: Плавающая кнопка «Позвонить» для мгновенного контакта  
KNOB: В конец `<body>` добавить `<a href="tel:+7XXXXXXXXXX" class="phone-cta" aria-label="Позвонить нам">📞</a>` и CSS `.phone-cta{position:fixed;right:1rem;bottom:1.5rem;width:56px;height:56px;background:var(--blue);color:#fff;border-radius:50%;display:flex;align-items:center;justify-content:center;box-shadow:0 4px 12px rgba(0,0,0,0.2);opacity:0;transition:opacity .3s} .phone-cta.visible{opacity:1}` плюс небольшой скрипт `window.addEventListener('scroll',()=>{if(window.scrollY>200)document.querySelector('.phone-cta').classList.add('visible');else document.querySelector('.phone-cta').classList.remove('visible');});`.  
EFFECT: Пользователь в любой момент может позвонить, что повышает коэффициент телефонных лидов.  
RISK: Кнопка может перекрывать важный контент на небольших экранах; необходимо протестировать на всех брейкпоинтах.  
ROLLBACK: Удалить HTML‑элемент, CSS‑правила и скрипт (git checkout HEAD -- path/to/file).  
VERIFY: Прокрутить страницу, убедиться, что кнопка появляется после 200 px, кликабельна и открывает телефонный диалог на мобильных устройствах; измерить увеличение `tel:`‑кликов в аналитике в течение 24 ч.  
PRIORITY: 1 – быстрый способ увеличить конверсию без серверных изменений.
