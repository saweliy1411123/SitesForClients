# localhost:8080/ovh/gpt-oss-120b  2026-11-17 05:07:32
duration=27.3 error=- attempts=1

IDEA: Ясный подзаголовок‑бенефиты под h1 в hero  
KNOB: В секцию `.hero` (после `<h1>`) добавить `<ul class="hero-benefits"><li>Получаете первых клиентов из Яндекса за 2 дня</li><li>Полный сайт — только контент и дизайн</li><li>Гарантированный запуск без технических проблем</li></ul>` и стилизовать список (margin‑top 12px, font‑size 14‑16px, цвет var(--muted), маркеры‑круги).  
EFFECT: За 5 секунд пользователь видит конкретные выгоды, повышается восприятие ценности и конверсия CTA.  
RISK: Небольшой рост объёма HTML ≈ 200 байт, может слегка увеличить FCP.  
ROLLBACK: `git checkout -- index.html` (или удалить добавленные строки).  
VERIFY: Открыть страницу, убедиться, что список отображается под заголовком, проверить, что он не ломает layout на мобильных (DevTools → toggle device).  
PRIORITY: 1 — критично для первой секунды восприятия оффера.  
SITE_REQUEST: hero  

---  

IDEA: Кнопка «Позвонить сейчас» — tel: CTA для мгновенного контакта  
KNOB: В блок `.cta-row` (L462‑L470) добавить рядом с существующей ссылкой кнопку: `<a class="btn-primary btn-call" href="tel:+7XXXXXXXXXX" aria-label="Позвонить Савелию сейчас">📞 Позвонить</a>`; в CSS добавить `.btn-call{margin-left:8px; background:var(--blue);}` и обеспечить контраст (color #fff).  
EFFECT: Упрощает путь к звонку, особенно на мобильных, повышает конверсию лидов.  
RISK: Требует актуального телефонного номера от владельца; возможна потеря кликов, если номер неверный.  
ROLLBACK: Удалить добавленную кнопку и связанные стили (`git checkout -- index.html`).  
VERIFY: На мобильном устройстве кликнуть кнопку – должна открыться звонилка; проверить, что стили совпадают с другими CTA.  
PRIORITY: 2 — быстрый прирост конверсии без изменения контента.  
SITE_REQUEST: cta-row  

---  

IDEA: Schema.org LocalBusiness для доверия и локального SEO  
KNOB: В конец `<body>` вставить `<script type="application/ld+json">{"@context":"https://schema.org","@type":"LocalBusiness","name":"Савелий — лендинги для бизнеса в Перми","url":"https://saveliy.ru/","logo":"https://saveliy.ru/logo.png","telephone":"+7XXXXXXXXXX","address":{"@type":"PostalAddress","streetAddress":"Улица, дом","addressLocality":"Пермь","postalCode":"614000","addressCountry":"RU"},"openingHours":"Mo-Fr 09:00-18:00","sameAs":["https://vk.ru/trainersdontplays","https://t.me/TrainersDontPlays"]}</script>` (заполнить реальными данными).  
EFFECT: Укрепляет доверие поисковых систем и пользователей, улучшает локальный поиск в Яндексе и Google.  
RISK: Неправильные данные могут вызвать штрафы; требует согласования с владельцем о точных контактах.  
ROLLBACK: Удалить скрипт из HTML (`git checkout -- index.html`).  
VERIFY: В Chrome DevTools → Console выполнить `JSON.parse(document.querySelector('script[type="application/ld+json"]').innerText)` и убедиться, что объект корректен; проверить в Rich Results Test.  
PRIORITY: 3 — повышает доверие и SEO, но не критично для мгновенной конверсии.
