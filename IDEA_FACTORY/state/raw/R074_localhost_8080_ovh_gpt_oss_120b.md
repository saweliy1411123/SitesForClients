# localhost:8080/ovh/gpt-oss-120b  2026-11-17 05:17:14
duration=41.7 error=- attempts=1

IDEA: Skip‑navigation link for keyboard users  
KNOB: В начало `<body>` добавить `<a href="#main" class="skip-link">Перейти к содержимому</a>`; в CSS `.skip-link{position:absolute;top:-40px;left:0;background:#fff;color:#000;padding:8px;z-index:100;transition:top .3s;} .skip-link:focus{top:0;}`; добавить `<main id="main">` вокруг основного контента.  
EFFECT: Улучшает WCAG‑AA, облегчает навигацию людям, использующим клавиатуру, потенциально повышает конверсию за счёт снижения барьера входа.  
RISK: При ошибке в CSS ссылка может «выскочить» наружу, нарушив визуальный поток.  
ROLLBACK: Удалить вставленный `<a>` и CSS‑правило (git checkout index.html).  
VERIFY: Открыть страницу, нажать Tab – ссылка должна появиться и перейти к `<main>`.  
PRIORITY: 2 – важный шаг к доступности, но не критичен для первой конверсии.  

IDEA: Breadcrumb‑structured data (JSON‑LD)  
KNOB: В `<head>` перед закрывающим тегом добавить:  
```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"BreadcrumbList",
  "itemListElement":[
    {"@type":"ListItem","position":1,"name":"Главная","item":"https://saveliy.ru/"},
    {"@type":"ListItem","position":2,"name":"Лендинги за 2 дня","item":"https://saveliy.ru/#price"},
    {"@type":"ListItem","position":3,"name":"Заказать демо","item":"https://saveliy.ru/#contact"}
  ]
}
</script>
```  
EFFECT: Позволяет поисковикам выводить хлебные крошки в сниппете, повышает CTR и SEO‑видимость.  
RISK: Неправильные URL могут вызвать ошибки в Search Console.  
ROLLBACK: Удалить `<script>`‑блок (git checkout index.html).  
VERIFY: В Google Rich Results Test убедиться, что BreadcrumbList валиден и без ошибок.  
PRIORITY: 2 – умеренный SEO‑бонус без риска для UX.  

IDEA: Указание языка страницы (`lang="ru"`)  
KNOB: В открывающем теге `<html>` добавить атрибут `lang="ru"`; дополнительно вставить в `<head>` `<meta http-equiv="Content-Language" content="ru-RU">`.  
EFFECT: Улучшает индексацию, помогает браузерам и вспомогательным технологиям корректно обрабатывать контент, повышает SEO.  
RISK: Отсутствует.  
ROLLBACK: Удалить атрибут и мета‑тег (git checkout index.html).  
VERIFY: Открыть исходный код, убедиться в наличии `lang="ru"` и соответствующего meta‑тега.  
PRIORITY: 1 – простое изменение с высокой отдачей.  

IDEA: ARIA‑live объявление метрики скорости загрузки  
KNOB: Внутри `.hero-note` обернуть элемент с ID `load-time` в `<span class="load-time-announcer" aria-live="polite"></span>`; в существующий JS (или добавить небольшой скрипт) установить `textContent` этого спана после расчёта времени.  
EFFECT: Пользователи скрин‑ридеров услышат «Сайт загружается за X мс», усиливая доверие к заявленному быстродействию.  
RISK: Требует небольшого JS‑кода; при отключённом JS метрика не отобразится.  
ROLLBACK: Удалить обёртку и скрипт (git checkout index.html).  
VERIFY: Открыть страницу с включённым экранным диктором (NVDA/VoiceOver) – должна прозвучать метрика после загрузки.  
PRIORITY: 3 – хорошее, но не критичное улучшение.  

IDEA: Таймер обратного отсчёта «Осталось мест» в hero‑блоке  
KNOB: После `.hero-note` добавить:  
```html
<div class="hero-countdown" aria-label="Осталось мест для бесплатного демо"></div>
```  
и подключить небольшой скрипт, который считает время до фиксированной даты (например, 48 ч) и обновляет `innerText` в формате «02 дн 12 ч 30 мин». CSS‑стиль: `.hero-countdown{font-size:1.2rem;color:#ff4;margin-top:12px;}`.  
EFFECT: Создаёт ощущение срочности, повышает конверсию за счёт FOMO.  
RISK: Требует поддержания актуальности даты; устаревший таймер может вызвать недоверие.  
ROLLBACK: Удалить HTML‑блок и скрипт (git checkout index.html).  
VERIFY: Перезагрузить страницу – таймер должен отображать оставшееся время и уменьшаться каждую минуту.  
PRIORITY: 2 – умеренный риск, но потенциальный рост заявок.  

IDEA: Кнопка «Наверх» (back‑to‑top)  
KNOB: В конец `<body>` добавить:  
```html
<button class="back-to-top" aria-label="Наверх">↑</button>
```  
CSS:  
```css
.back-to-top{position:fixed;right:16px;bottom:16px;padding:10px 14px;background:#8b5cf6;color:#fff;border:none;border-radius:4px;opacity:0;visibility:hidden;transition:opacity .3s;}
.back-to-top.show{opacity:1;visibility:visible;}
```  
JS: добавить слушатель scroll, который добавляет класс `show` при `window.scrollY>300`; по клику – `window.scrollTo({top:0,behavior:'smooth'});`.  
EFFECT: Улучшает юзабилити на длинных страницах, особенно на мобильных, снижая фрустрацию и повышая время на сайте.  
RISK: Минимальный JS‑вес.  
ROLLBACK: Удалить кнопку, CSS и JS (git checkout index.html).  
VERIFY: Прокрутить страницу вниз – кнопка появляется, клик возвращает в начало.  
PRIORITY: 3 – приятный UX‑апгрейд, но не критичен для конверсии.  

IDEA: Preconnect + preload для Google Fonts (ускорение FCP)  
KNOB: В `<head>` добавить `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>`; заменить текущий `<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap">` на:  
```html
<link rel="preload" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap" as="style" onload="this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap"></noscript>
```  
EFFECT: Уменьшает render‑blocking запросов, ускоряет First Contentful Paint, улучшает Core Web Vitals.  
RISK: Если onload не сработает, шрифты могут не загрузиться (но есть fallback в `<noscript>`).  
ROLLBACK: Восстановить оригинальный `<link>` и удалить `preconnect` (git checkout index.html).  
VERIFY: В DevTools → Network → задать throttling «Slow 3G», перезагрузить – шрифты должны начинать загружаться до рендеринга.  
PRIORITY: 2 – заметное улучшение скорости без риска контента.
