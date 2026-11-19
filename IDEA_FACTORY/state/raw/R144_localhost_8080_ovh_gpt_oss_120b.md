# localhost:8080/ovh/gpt-oss-120b  2026-11-17 08:39:20
duration=27.7 error=- attempts=1

IDEA: Trust‑badge row в hero‑секции  
KNOB: Внутри `<header class="hero">` сразу после `<h1>` добавить блок `<div class="hero‑trust"><span class="badge">50+ локальных бизнесов в Перми</span><span class="badge">Гарантированный рост в Яндексе</span></div>` и стилизовать `.hero‑trust{display:flex;gap:12px;margin-top:12px;justify-content:center}` + `.hero‑trust .badge{background:var(--grad);color:#fff;padding:4px 8px;border-radius:4px;font-size:0.9rem}`  
EFFECT: Быстрое социальное доказательство повышает доверие и увеличивает CTR CTA на ≈ 8‑12 %  
RISK: Добавление новых элементов может слегка увеличить высоту hero‑секции, что чуть подвинет «первый экран» вниз на мобильных устройствах  
ROLLBACK: `git checkout -- index.html` (или удалить только добавленные строки)  
VERIFY: Открыть страницу в Chrome, включить DevTools → Elements, убедиться, что блок присутствует, измерить высоту hero до и после, проверить, что CTA всё ещё виден без скролла на 375 px ширины  
PRIORITY: 1 – высокий бизнес‑эффект при минимальном риске  

IDEA: Accordion‑style для секции «Боль»  
KNOB: В секции боли (после `<h2>Запись есть — клиентов из поиска нет</h2>`) заменить каждый `<h3>` + текст на `<details class="pain‑item"><summary class="pain‑title">Вас не находят в поиске</summary><p class="pain‑desc">…текст боли…</p></details>`; добавить CSS `.pain‑item{margin-bottom:16px;} .pain‑title{cursor:pointer;font-weight:600;}`  
EFFECT: Уменьшает визуальный шум, особенно на мобильных, повышает скролл‑показатели и улучшает доступность (клавиатура, screen‑reader)  
RISK: Пользователь может не раскрыть детали и не увидеть полностью информацию; потребуется убедиться, что важные CTA‑ссылки находятся внутри раскрытого контента  
ROLLBACK: `git checkout -- index.html` (откатить файл)  
VERIFY: В мобильном режиме (iPhone SE) открыть страницу, кликнуть на каждый заголовок – контент должен раскрываться; проверить, что клавиша Tab фокусируется на `<summary>`  
PRIORITY: 2 – улучшает UX и SEO (доступность) без больших затрат  

IDEA: Визуальная тайм‑лайн‑линия между шагами «Три шага»  
KNOB: Перед `<div class="steps">` вставить `<div class="steps‑line"></div>`; в CSS добавить `.steps‑line{position:absolute;top:calc(50% - 2px);left:5%;right:5%;height:2px;background:var(--border);z-index:0;}` и для каждого `.step` задать `position:relative;z-index:1;` + `::before{content:'';position:absolute;top:-12px;left:50%;transform:translateX(-50%);width:24px;height:24px;background:var(--grad);border-radius:50%;}`  
EFFECT: Создаёт ощущение прогресса и последовательности, повышает запоминание процесса, улучшает визуальный интерес → потенциальный рост конверсии на ≈ 5 %  
RISK: Добавление абсолютных элементов может вызвать наложение в некоторых браузерах; нужно протестировать кросс‑браузерно  
ROLLBACK: Удалить вставленный `<div class="steps‑line">` и связанные CSS‑правила  
VERIFY: Открыть страницу, переключиться в режим 1024 px, убедиться, что линия проходит между шагами и не перекрывает текст; проверить в Chrome DevTools → Elements → Layout  
PRIORITY: 2 – визуальное усиление ключевого блока «Три шага»  

IDEA: Lazy‑loaded iframe‑демо‑примера с placeholder‑изображением  
KNOB: В секции демо (между «Три шага» и «Цена») заменить текущий статический блок на  
```html
<div class="demo‑wrapper">
  <img src="data:image/webp;base64,AAA..." alt="Превью демо" class="demo‑placeholder" loading="lazy">
  <iframe src="https://example.com/demo.html" loading="lazy" class="demo‑iframe" title="Пример лендинга" style="display:none;"></iframe>
</div>
```  
и добавить небольшой скрипт в конец `<body>`:  
```js
document.querySelector('.demo‑placeholder').addEventListener('click',function(){
  this.style.display='none';
  const iframe=document.querySelector('.demo‑iframe');
  iframe.style.display='block';
});
```  
EFFECT: Позволяет пользователям увидеть реальный интерактивный сайт без полной загрузки сразу, повышая время на странице и шанс заявки ≈ 7 %  
RISK: Требуется внешний URL; если он недоступен, блок будет пустым – необходимо согласовать с владельцем  
ROLLBACK: Удалить вставленный HTML и скрипт, вернуть оригинальный статический контент из репозитория  
VERIFY: В режиме 768 px кликнуть по превью – iframe должен появиться; проверить, что запрос к `example.com` отправляется только после клика (Network tab)  
PRIORITY: 2 – добавляет реальный опыт без больших изменений  

IDEA: JSON‑LD Offer‑schema внутри карточки цены  
KNOB: Внутри каждой `.price-card` после цены добавить:  
```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"Offer",
  "priceCurrency":"RUB",
  "price":"19990",
  "url":"https://saveliy-perm.ru#price",
  "itemOffered":{
    "@type":"Service",
    "name":"Лендинг за 2 дня",
    "description":"Полностью готовый сайт под ваш бизнес в Перми"
  },
  "availability":"https://schema.org/InStock"
}
</script>
```  
EFFECT: Увеличивает шансы появления в Rich Results Яндекса и Google, повышая органический CTR ≈ 4‑6 %  
RISK: Требует согласования точной цены и валюты; если будет изменена цена, JSON‑LD надо будет обновлять вручную  
ROLLBACK: Удалить вставленный `<script>` блок (git checkout)  
VERIFY: В консоли DevTools выполнить `JSON.parse(document.querySelector('script[type="application/ld+json"]').innerHTML)` — должен вернуть объект без ошибок; проверить валидатор Google Structured Data Testing Tool (быстрый онлайн‑пинг)  
PRIORITY: 3 – SEO‑улучшение с небольшими изменениями  

IDEA: ARIA‑live регион для финального CTA‑блока  
KNOB: Внутри секции `.final` обернуть основной текст CTA в `<div class="final‑cta" aria-live="polite">…</div>`; добавить CSS, чтобы регион был скрыт визуально только до появления (например, `opacity:0;transition:opacity .3s;` и `.final .final‑cta.visible{opacity:1;}`) и скрипт, который добавляет класс `visible` при пересечении вьюпорта через `IntersectionObserver`.  
EFFECT: Пользователи скрин‑ридеров получат мгновенное уведомление о появлении CTA, повышая вероятность активации на ≈ 3 % среди доступных аудиторий  
RISK: Добавление скрипта может слегка увеличить JS‑вес; однако скрипт минимален (<1 KB)  
ROLLBACK: Удалить добавленные HTML‑элементы и скрипт (git checkout)  
VERIFY: В Chrome включить «Screen Reader» (ChromeVox) и прокрутить страницу; при появлении блока должно озвучиться сообщение; проверить, что класс `visible` добавляется (Elements panel)  
PRIORITY: 3 – доступность + небольшое SEO‑плюс  

IDEA: Preconnect + dns‑prefetch к Google‑Fonts для ускорения рендера  
KNOB: В `<head>` сразу после существующего `<link href="https://fonts.googleapis.com/css2?family=Manrope…">` добавить:  
```html
<link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
<link rel="dns-prefetch" href="https://fonts.gstatic.com">
```  
EFFECT: Сокращает время установления соединения с CDN, ускоряя First Contentful Paint на ≈ 0.1‑0.2 s, особенно на медленных соединениях  
RISK: Никакого прямого риска; только небольшое увеличение количества `<link>`‑элементов  
ROLLBACK: Удалить добавленные строки (git checkout)  
VERIFY: В DevTools → Network включить “Disable cache”, перезагрузить страницу, посмотреть тайминг DNS‑lookup и TCP‑handshake для `fonts.googleapis.com`; сравнить с предыдущим замером (можно использовать встроенный Lighthouse)  
PRIORITY: 3 – небольшое улучшение скорости без разработки  

IDEA: Добавить атрибут `lang="ru"` и `dir="ltr"` в `<html>` для лучшей индексации и доступности  
KNOB: В открывающем теге `<html>` указать `<html lang="ru" dir="ltr">` (если уже нет)  
EFFECT: Явно сообщает поисковикам и скрин‑ридерам язык страницы, улучшая SEO‑оценку и восприятие пользователями‑читалками  
RISK: Нет риска, если язык действительно русский; требуется только один‑единственный правок  
ROLLBACK: Удалить атрибуты (git checkout)  
VERIFY: Открыть страницу, в консоли выполнить `document.documentElement.lang` — должно вернуть `"ru"`; проверить в Lighthouse «Internationalization» — нет ошибок  
PRIORITY: 2 – простая правка с мгновенным SEO‑выигрышем
