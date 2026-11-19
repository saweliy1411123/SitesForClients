# localhost:8080/ovh/gpt-oss-120b  2026-11-17 02:56:13
duration=66.0 error=- attempts=1

IDEA: Preconnect к Google Fonts для ускорения загрузки шрифтов  
KNOB: В `<head>` добавить `<link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>` и `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>` перед ссылкой на Google Fonts  
EFFECT: Сократит время первого рендеринга текста, уменьшит CLS и общий LCP – быстрее будет видно заголовки и текст  
RISK: Небольшой рост количества запросов – не критично, браузер кэширует соединения  
ROLLBACK: Удалить две строки из `index.html` (git checkout -- index.html)  
VERIFY: Открыть страницу в Chrome DevTools → Network → проверить, что запросы к fonts.googleapis.com и fonts.gstatic.com начинаются с `(pending)` сразу после загрузки HTML, измерить LCP до/после (Performance → Metrics) – разница должна быть ≥ 200 мс  
PRIORITY: 1 – быстрый win для скорости без риска  

IDEA: “Skip‑to‑content” ссылка для улучшения навигации клавиатурой  
KNOB: Сразу после открывающего `<body>` вставить `<a href="#main" class="skip-link">Перейти к содержимому</a>`; добавить `id="main"` к `<main>` (или к первому крупному контейнеру) и стили: `.skip-link{position:absolute;top:-40px;left:0;background:#fff;color:#000;padding:8px;z-index:100;transition:top .3s;} .skip-link:focus{top:0;}`  
EFFECT: Пользователи скрин‑ридеров и клавиатурные навигаторы мгновенно попадают в основной контент, повышается WCAG 2.1 AA по пункту 2.4.1 (блоки)  
RISK: Небольшой визуальный сдвиг при фокусе, но стили контролируются, конфликтов нет  
ROLLBACK: Удалить вставленную строку и атрибут `id` (git checkout -- index.html)  
VERIFY: Нажать `Tab` сразу после загрузки – фокус должен перейти на ссылку, нажать `Enter` – страница скроллится к основному контенту; проверить в axe‑core (bookmarklet) отсутствие ошибок 2.4.1  
PRIORITY: 1 – значительное улучшение доступности за 2 минуты  

IDEA: Добавление ARIA‑лейблов к навигационным ссылкам  
KNOB: В каждый `<a>` внутри навигации (`.nav-links a`) добавить `aria-label="Перейти к разделу <текст ссылки>"` (пример: `<a href="#price" aria-label="Перейти к разделу цены">Цена</a>`)  
EFFECT: Экранные читалки объявляют цель ссылки более явно, повышается понятность навигации, улучшение WCAG 2.1 AA 2.4.4  
RISK: Требует небольшого ручного редактирования всех ссылок, риск опечатки в тексте  
ROLLBACK: Откатить изменения в `index.html` (git checkout -- index.html)  
VERIFY: Запустить axe‑core, убедиться в отсутствии ошибок 2.4.4; проверить в TalkBack/VoiceOver, что читается полное описание ссылки  
PRIORITY: 2 – мелкое, но полезное для доступности  

IDEA: Явные ARIA‑лейтенды (navigation, main, footer)  
KNOB: Добавить `role="navigation"` к контейнеру навигации, `role="main"` к основному контенту (`<main>`), `role="contentinfo"` к футеру; при отсутствии `<main>` обернуть основной блок в `<main role="main">`  
EFFECT: Упрощает скрин‑ридурам структуру страницы, улучшает SEO‑понимание семантики, повышает WCAG 2.1 AA 1.3.1  
RISK: Нет конфликтов, только добавление атрибутов  
ROLLBACK: Удалить добавленные `role`‑атрибуты (git checkout -- index.html)  
VERIFY: В DevTools → Elements проверить наличие `role` на нужных элементах; в axe‑core отсутствие ошибок 1.3.1  
PRIORITY: 2 – низкая стоимость, хороший SEO‑эффект  

IDEA: Фокус‑видимость (focus‑visible) для всех интерактивных элементов  
KNOB: В глобальный CSS добавить:  
```css
:focus-visible{outline:3px solid var(--blue);outline-offset:2px}
a:focus-visible, button:focus-visible{outline:3px solid var(--blue)}
```  
EFFECT: Пользователи клавиатуры видят чёткий индикатор фокуса, соответствие WCAG 2.1 AA 2.4.7, повышает конверсию за счёт уверенного навигационного опыта  
RISK: Возможен конфликт с уже существующим `outline:none` в стилях; но правило будет переопределять только при `:focus-visible`  
ROLLBACK: Удалить блок CSS (git checkout -- index.html)  
VERIFY: Нажать `Tab` по странице – каждый элемент должен получать синий контур; проверить в axe‑core отсутствие ошибок 2.4.7  
PRIORITY: 2 – важно для доступности, быстро реализуемо  

IDEA: Отключение анимаций при `prefers-reduced-motion`  
KNOB: Обернуть все анимационные правила (например, `.reveal`, `.hero-note`, любые `@keyframes`) в медиа‑запрос:  
```css
@media (prefers-reduced-motion: reduce){ 
  .reveal,.hero-note{transition:none;animation:none;}
}
```  
EFFECT: Пользователи, указавшие предпочтение уменьшения движения, не будут страдать от всплывающих анимаций, соответствие WCAG 2.1 AA 1.4.3, улучшение восприятия на слабом железе  
RISK: Потеря визуального «показа» для части аудитории, но это безопасно  
ROLLBACK: Удалить медиа‑блок (git checkout -- index.html)  
VERIFY: В Chrome DevTools → Rendering → Emulate CSS media → `prefers-reduced-motion: reduce` и убедиться, что анимации исчезли; проверить в axe‑core отсутствие ошибок 1.4.3  
PRIORITY: 2 – социально‑ответственная улучшка без риска  

IDEA: JSON‑LD Offer schema для цены лендинга  
KNOB: В конец `<body>` добавить скрипт:  
```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"Offer",
  "priceCurrency":"RUB",
  "price":"0",
  "url":"https://example.com/#price",
  "availability":"https://schema.org/InStock",
  "itemOffered":{
    "@type":"Service",
    "name":"Лендинг за 2 дня",
    "description":"Одностраничный сайт под ваш бизнес, готовый к показу в Яндексе"
  }
}
</script>
```  
EFFECT: Поисковые системы лучше понимают коммерческое предложение, повышается шанс появления в блоке «Пакетные предложения», потенциальный рост CTR в SERP  
RISK: Требует точного указания цены (0 RUB – бесплатное демо) и URL; если цена изменится, потребуется правка – не критично  
ROLLBACK: Удалить скрипт (git checkout -- index.html)  
VERIFY: Скопировать страницу в Rich Results Test (Google) → проверить отсутствие ошибок и появление Offer в выводе; измерить изменение CTR (если есть аналитика)  
PRIORITY: 3 – SEO‑выгода, но менее критична, чем скорость/доступность  

IDEA: JSON‑LD HowTo schema для «Трёх шагов»  
KNOB: В конец `<body>` добавить скрипт:  
```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"HowTo",
  "name":"Как получить лендинг за 2 дня",
  "step":[
    {"@type":"HowToStep","url":"#step1","name":"Идея и ТЗ","text":"Вы присылаете идею и требования"},
    {"@type":"HowToStep","url":"#step2","name":"Создание демо","text":"Мы делаем демо‑макет"},
    {"@type":"HowToStep","url":"#step3","name":"Запуск и правки","text":"Публикуем и вносим правки"}
  ]
}
</script>
```  
EFFECT: Расширенные сниппеты «Как сделать…» могут появиться в поиске, повышая видимость и привлечение трафика из органических результатов  
RISK: Нужно поддерживать актуальность шагов; если контент изменится – требуется обновление, но это простая правка  
ROLLBACK: Удалить скрипт (git checkout -- index.html)  
VERIFY: В Rich Results Test проверить наличие HowTo‑разметки без ошибок; при наличии – ожидается возможность появления в поиске  
PRIORITY: 3 – SEO‑улучшение, но без гарантии мгновенного эффекта  

IDEA: Добавить OG‑image для соцсетей  
KNOB: В `<head>` добавить `<meta property="og:image" content="https://example.com/assets/og-image.jpg">` и `<meta property="og:image:width" content="1200">` `<meta property="og:image:height" content="630">` (изготовить лёгкое изображение‑превью)  
EFFECT: При шаринге в соцсетях будет отображаться привлекательный превью‑картинка, повышается CTR в соцсетях и потенциальный реферрерный трафик  
RISK: Требуется загрузить файл изображения – необходимо разместить в репозитории; размер должен быть < 200 KB для быстрой загрузки  
ROLLBACK: Удалить мета‑теги (git checkout -- index.html) и удалить файл‑изображение, если был добавлен в репо  
VERIFY: С помощью Facebook Sharing Debugger проверить, что картинка подтягивается; в Twitter Card Validator – аналогично; измерить
