# localhost:8080/ovh/gpt-oss-120b  2026-11-17 06:01:44
duration=39.6 error=- attempts=1

IDEA: Preconnect & DNS‑prefetch для Google‑Fonts  
KNOB: В `<head>` добавить сразу после существующих `<link>` строки  
```html
<link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="dns-prefetch" href="https://fonts.googleapis.com">
<link rel="dns-prefetch" href="https://fonts.gstatic.com">
```  
EFFECT: Сократит время установления соединения, ускорит загрузку шрифтов → улучшит LCP и Core Web Vitals.  
RISK: Минимальный; может не сработать в очень старых браузерах (но они уже не учитываются в SEO).  
ROLLBACK: Удалить четыре строки из `<head>` (git checkout index.html).  
VERIFY: Открыть DevTools → Network, включить “Disable cache”, перезагрузить страницу и убедиться, что запросы к fonts.googleapis.com и fonts.gstatic.com начинаются с статус (initiated) → preconnect (вкладка “Timing”).  
PRIORITY: 1 – быстрый выигрыш в скорости без изменения контента.  

IDEA: font-display: swap для шрифтов Manrope  
KNOB: В `<head>` заменить текущий `<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap">` на `<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap" onload="this.rel='stylesheet'">` и добавить `<style> @font-face{font-family:'Manrope';src:url(https://fonts.gstatic.com/s/manrope/v14/...-Regular.woff2) format('woff2');font-display:swap;}</style>` (указать только `font-display:swap` в CSS‑правиле).  
EFFECT: Уменьшит FOIT (flash of invisible text), ускорит первый отрисовочный текст → повышает CLS и пользовательский опыт.  
RISK: Если указать неверный URL в @font-face, шрифт может не подгрузиться; но основной `<link>` остаётся как fallback.  
ROLLBACK: Удалить добавленный `<style>` и вернуть оригинальный `<link>` (git checkout index.html).  
VERIFY: В Chrome DevTools → Network → Font, посмотреть, что шрифт загружается с `font-display:swap` (вкладка “Headers” → “font-display”). Можно также включить “Rendering → Show paint flashing” и убедиться, что текст появляется сразу.  
PRIORITY: 2 – небольшие изменения, но заметный эффект для SEO‑метрик.  

IDEA: meta‑тег robots «index, follow»  
KNOB: В `<head>` добавить сразу после `<meta name="theme-color"...>` строку  
```html
<meta name="robots" content="index, follow">
```  
EFFECT: Явно указывает поисковикам индексировать страницу, повышает уверенность в корректном SEO‑сканировании.  
RISK: Если владелец использует отдельный robots.txt, может быть конфликт, но конфликтный тег переопределит директиву.  
ROLLBACK: Удалить строку (git checkout index.html).  
VERIFY: Открыть страницу в Google Search Console → URL Inspection → увидеть, что “Meta robots tag” = index, follow.  
PRIORITY: 2 – простая правка, повышает SEO‑доверие.  

IDEA: Breadcrumb‑structured data (JSON‑LD) для локального SEO  
KNOB: В конец `<body>` (перед закрывающим `</body>`) вставить скрипт:  
```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"BreadcrumbList",
  "itemListElement":[
    {"@type":"ListItem","position":1,"name":"Главная","item":"https://example.com/"},
    {"@type":"ListItem","position":2,"name":"Лендинг","item":"https://example.com/#price"}
  ]
}
</script>
```  
(заменить `example.com` на реальный домен).  
EFFECT: Позволит поисковикам показывать хлебные крошки в сниппете, улучшит CTR и локальное SEO.  
RISK: Требует корректного URL; если домен меняется, понадобится обновление.  
ROLLBACK: Удалить скрипт (git checkout index.html).  
VERIFY: В Chrome DevTools → Console выполнить `JSON.parse(document.querySelector('script[type="application/ld+json"]').innerText)` и убедиться в корректной структуре; затем проверить в Google Rich Results Test.  
PRIORITY: 2 – небольшая добавка, но может повысить видимость в поиске.  

IDEA: rel="noopener noreferrer" для всех внешних ссылок  
KNOB: В файле заменить каждую внешнюю ссылку (`target="_blank"`) добавить атрибуты `rel="noopener noreferrer"` (например, ссылка в секции «Написать в Telegram»).  
EFFECT: Улучшает безопасность и SEO (предотвращает передачу реферера, ускоряет загрузку).  
RISK: Если кто‑то полагается на `window.opener` в сторонних скриптах, они перестанут работать (маловероятно).  
ROLLBACK: Откатить изменения в Git (git checkout index.html).  
VERIFY: В DevTools → Elements найти внешнюю ссылку, убедиться в наличии `rel="noopener noreferrer"`.  
PRIORITY: 1 – безопасность + небольшое SEO‑преимущество, быстрая правка.  

IDEA: defer атрибут для единственного скрипта  
KNOB: В конце `<body>` изменить `<script src="...">` (или inline) на `<script defer>/* существующий код */</script>` (если скрипт inline, просто добавить `defer`).  
EFFECT: Позволит браузеру параллельно парсить HTML, отложив выполнение скрипта до полной загрузки DOM → ускорит First Contentful Paint.  
RISK: Если скрипт зависит от синхронного выполнения до загрузки контента, может сломаться; но в текущем статическом лендинге скрипт, скорее всего, отвечает за анимацию и безопасен.  
ROLLBACK: Удалить `defer` (git checkout index.html).  
VERIFY: В DevTools → Network → JS, убедиться, что скрипт загружается с атрибутом defer и не блокирует парсинг; измерить FCP до/после (Lighthouse).  
PRIORITY: 2 – простая оптимизация, повышающая скорость.  

IDEA: role="contentinfo" + <address> с aria‑label в футере  
KNOB: Обернуть контактный блок в футере (после L736) в `<footer role="contentinfo"><address aria-label="Контактные данные">Савелий · Пермь · <a href="https://t.me/..." rel="noopener noreferrer">Telegram</a></address></footer>` (если уже есть `<footer>`, добавить `role="contentinfo"` и `<address aria-label="Контактные данные">`).  
EFFECT: Улучшает семантику и доступность для скрин‑ридеров, повышает SEO‑оценку по accessibility.  
RISK: Никаких.  
ROLLBACK: Удалить добавленные атрибуты/теги (git checkout index.html).  
VERIFY: В DevTools → Accessibility, убедиться, что элемент имеет роль “contentinfo” и адрес отмечен как “landmark”.  
PRIORITY: 3 – небольшое улучшение доступности, но менее критично, чем скорость.
