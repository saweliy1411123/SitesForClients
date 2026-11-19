# localhost:8081/big_only  2026-11-17 04:47:39
duration=23.0 error=- attempts=2

IDEA: Добавить JSON‑LD LocalBusiness для локального SEO и доверия  
KNOB: В конец `<head>` вставить `<script type="application/ld+json">` с объектом `@type":"LocalBusiness"` (name, url, address, telephone, openingHours, priceRange, sameAs)  
EFFECT: Повышает видимость в локальном поиске Яндекса/Google, усиливает доверие за счёт официальных данных о компании  
RISK: Требует уточнения реального адреса и часов работы у владельца — иначе будет неверная разметка  
ROLLBACK: `git checkout -- index.html` (или удалить вставленный `<script>`)  
VERIFY: Открыть страницу, открыть DevTools → вкладка «Console», убедиться, что скрипт отрабатывает без ошибок; проверить через Google Rich Results Test, что найдено `LocalBusiness`‑разметка  
PRIORITY: 1 — высокий SEO‑эффект и доверие, небольшие изменения кода  

IDEA: «Sticky CTA» – фиксированная кнопка‑призыв внизу экрана на мобильных устройствах  
KNOB: В конец `<body>` добавить `<a class="sticky-cta btn-primary magnetic" href="#contact">Получить демо бесплатно <span class="arr">→</span></a>`; в CSS добавить медиазапрос `@media (max-width:720px){ .sticky-cta{position:fixed;bottom:0;left:0;right:0;display:flex;justify-content:center;z-index:100;}` и стили для плавного появления (`transform:translateY(100%);transition:transform .3s; .sticky-cta.visible{transform:translateY(0);}`) + JS‑скрипт, который добавляет класс `visible` после скролла > 100 px  
EFFECT: Увеличивает конверсию, так как CTA всегда доступна, особенно на длинных мобильных скроллах  
RISK: Может конфликтовать с уже существующим фиксированным `nav`‑шапкой; требует проверки z‑index  
ROLLBACK: `git checkout -- index.html` (удалить добавленные строки и стили)  
VERIFY: На мобильном эмуляторе открыть страницу, прокрутить > 100 px — кнопка должна появиться; клик — плавный скролл к форме/контакту; проверить отсутствие перекрытия контента  
PRIORITY: 2 — средний технический Aufwand, но сильный рост конверсий на мобильных  

IDEA: Ясный блок «Что вы получите» под заголовком h1 – три коротких выгоды в виде списка  
KNOB: После `<h1>` в секции hero добавить `<ul class="hero-benefits"><li>Быстрый запуск за 2 дня</li><li>Позиция в Яндексе уже через неделю</li><li>Поддержка и правки в течение месяца</li></ul>`; в CSS задать `.hero-benefits{display:flex;gap:1rem;justify-content:center;margin-top:1rem;list-style:none;font-size:clamp(14px,2vw,18px);color:#c3cad9}` и стили для адаптивности  
EFFECT: Увеличивает ясность оффера сразу на первом экране, помогает пользователю быстро понять выгоды → рост CTR на CTA  
RISK: Нужно согласовать точные формулировки выгоды с владельцем, иначе будет неточность  
ROLLBACK: `git checkout -- index.html` (удалить добавленный `<ul>` и CSS)  
VERIFY: Открыть страницу, убедиться, что список отображается под заголовком, проверить, что текст не обрезается на мобильных размерах, измерить CTR CTA до/после (можно через быстрый A/B‑тест, заменив файл на `index.a.html`/`index.b.html`)  
PRIORITY: 3 — небольшие правки, но повышают восприятие оффера; полезно после внедрения более «технических» улучшений.
