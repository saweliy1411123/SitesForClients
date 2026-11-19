# localhost:8080/ovh/gpt-oss-120b  2026-11-17 07:40:44
duration=73.7 error=- attempts=1

IDEA: Добавить JSON‑LD @type LocalBusiness в <head> для локального SEO  
KNOB: Вставить сразу после существующих <meta> блок `<script type="application/ld+json">{"@context":"https://schema.org","@type":"LocalBusiness","name":"Савелий","url":"https://example.com","address":{"@type":"PostalAddress","addressLocality":"Пермь","addressCountry":"RU"},"telephone":"+7 123 456‑78‑90","sameAs":["https://vk.com/trainersdontplays"]}</script>`  
EFFECT: Поисковые системы смогут показывать фирму в блоке «Карты» и в локальных результатах, повышая доверие и приток органического трафика.  
RISK: Требует актуальных контактных данных; неверная информация может привести к штрафу за недостоверные сведения.  
ROLLBACK: Удалить вставленный `<script>`‑блок (git checkout index.html).  
VERIFY: Открыть страницу в Google Rich Results Test → убедиться, что найден объект LocalBusiness.  
PRIORITY: 2 – высокий SEO‑эффект при минимальных изменениях.  

---  

IDEA: Улучшить визуальное восприятие блока «Боль» с помощью иконок‑псевдо‑элементов и ARIA‑атрибутов  
KNOB: Обернуть каждый пункт боли (h3 + текст) в `<li class="pain-item">` внутри `<ul class="pain-list" role="list">`. Добавить перед заголовком каждой боли `<svg class="icon" aria-hidden="true" width="24" height="24"><use href="#icon-alert"/></svg>` (SVG‑символ уже присутствует в favicon‑sprite).  
EFFECT: Быстрое сканирование текста, повышенная наглядность и поддержка скрин‑ридеров за счёт `role="list"` и `aria-hidden`.  
RISK: Немного увеличит объём HTML и потребует наличия SVG‑символа #icon‑alert.  
ROLLBACK: Удалить добавленные `<ul>`, `<li>` и SVG‑разметку (git checkout index.html).  
VERIFY: Открыть страницу, убедиться, что каждый пункт имеет иконку; проверить в Chrome DevTools → Accessibility → убедиться, что список объявлен как list.  
PRIORITY: 2 – улучшает UX без влияния на дизайн.  

---  

IDEA: Прогресс‑бар над секцией «Три шага», заполняющийся при скролле  
KNOB: Вставить перед `<div class="steps">` элемент `<div class="steps-progress"><div class="fill"></div></div>`. Добавить в конец <body> небольшую JS‑функцию, которая измеряет `getBoundingClientRect()` секции #steps и обновляет ширину `.fill` в % от пройденного скролла. Добавить CSS: `.steps-progress{height:4px;background:#e5e7eb;position:sticky;top:0;z-index:10;}.steps-progress .fill{height:100%;background:var(--violet);width:0;transition:width .2s;}`.  
EFFECT: Пользователь видит, сколько контента уже просмотрено, усиливает вовлечённость и мотивирует дочитать до конца.  
RISK: Требует небольшого JS; в старых браузерах без поддержки IntersectionObserver может не работать (но работает в современных).  
ROLLBACK: Удалить вставленный HTML‑блок и скрипт (git checkout index.html).  
VERIFY: Прокрутить страницу, наблюдать плавный рост полоски; проверить в мобильном режиме.  
PRIORITY: 2 – заметный UX‑бонус, небольшая стоимость реализации.  

---  

IDEA: Добавить интерактивный overlay‑текст к каждому демо‑концепту, поясняющий, что это макет  
KNOB: Внутри контейнера каждого демо‑элемента (см. `<!-- ============ DEMO ============ -->`) добавить `<div class="demo-overlay" aria-hidden="true">Это макет, а не готовый сайт</div>` и CSS: `.demo-overlay{position:absolute;inset:0;background:rgba(0,0,0,0.6);color:#fff;display:flex;align-items:center;justify-content:center;font-size:14px;opacity:0;transition:opacity .2s;}.demo-item:hover .demo-overlay,.demo-item:focus-within .demo-overlay{opacity:1;}` (где `.demo-item` — родительский блок).  
EFFECT: Снижает риск недопонимания пользователем, повышает доверие и уменьшает количество вопросов‑возражений.  
RISK: Увеличивает объём CSS/HTML; при отключённом CSS overlay будет скрыт, но контент останется доступным.  
ROLLBACK: Удалить добавленные элементы и CSS‑правила (git checkout index.html).  
VERIFY: Навести курсор/фокус на демо‑карточку → увидеть полупрозрачный текст; проверить в мобильном режиме (tap).  
PRIORITY: 2 – улучшает прозрачность предложения без изменения цены.  

---  

IDEA: Включить схему Offer (JSON‑LD) для карточки цены, чтобы появлялись сниппеты с ценой  
KNOB: После блока `.price-card` добавить `<script type="application/ld+json">{"@context":"https://schema.org","@type":"Offer","price":"12000","priceCurrency":"RUB","url":"https://example.com#price","availability":"https://schema.org/InStock","seller":{"@type":"Person","name":"Савелий"}}`  
EFFECT: Поисковые системы могут показывать цену прямо в результатах поиска, повышая кликабельность.  
RISK: Цена должна быть актуальной; если меняется, скрипт надо обновлять.  
ROLLBACK: Удалить скрипт (git checkout index.html).  
VERIFY: Запустить Google Rich Results Test → убедиться, что найден объект Offer.  
PRIORITY: 2 – прямой SEO‑выигрыш, небольшие изменения.  

---  

IDEA: Добавить поле поиска в секцию FAQ для мгновенной фильтрации вопросов  
KNOB: Над `<div class="faq">` вставить `<input type="search" class="faq-search" placeholder="Поиск по вопросам…" aria-label="Поиск по FAQ">`. Добавить короткий скрипт в конец <body>, который на событие `input` скрывает/показывает `<details class="faq-item">` по совпадению текста в `<summary>`. CSS: `.faq-item {display:none;} .faq-item.show {display:block;}`.  
EFFECT: Пользователи быстро находят нужный ответ, уменьшают фрустрацию, повышают вероятность конверсии.  
RISK: Требует JS; в случае ошибки поиск может сломаться, но базовый контент останется видимым.  
ROLLBACK: Удалить `<input>` и скрипт (git checkout index.html).  
VERIFY: Ввести запрос в поле → убедиться, что список вопросов фильтруется в реальном времени.  
PRIORITY: 2 – улучшает UX, особенно на длинных
