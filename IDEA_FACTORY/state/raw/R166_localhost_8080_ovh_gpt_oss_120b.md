# localhost:8080/ovh/gpt-oss-120b  2026-11-17 09:41:49
duration=25.3 error=- attempts=2

IDEA: Добавить атрибут `lang="ru"` в корневой `<html>`
KNOB: В файле `index.html` изменить открывающий тег `<html>` на `<html lang="ru">`
EFFECT: Явно указывает язык страницы для скрин‑ридеров и поисковых систем → улучшение доступности и SEO‑ранжирования
RISK: Практически отсутствует; единственный риск — возможный конфликт, если в дальнейшем планируется мультиязычность (тогда понадобится динамический `lang`)
ROLLBACK: `git checkout -- index.html` или удалить/откатить строку с атрибутом
VERIFY: Открыть страницу, открыть «View source», убедиться, что `lang="ru"` присутствует; запустить Lighthouse → проверка Accessibility (Language) должна быть «Pass»
PRIORITY: 1 — простая правка с высокой отдачей для SEO и доступности

IDEA: Предзагрузка соединений к Google Fonts (`rel=preconnect`)
KNOB: В `<head>` добавить две строки:  
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
``` 
EFFECT: Сокращает время DNS‑lookup и TLS‑handshake для шрифтов → ускорение First Contentful Paint и LCP
RISK: Практически нулевой; в старых браузерах тег игнорируется
ROLLBACK: Удалить только что добавленные `<link>`‑элементы
VERIFY: В DevTools → Network, включить «Disable cache», перезагрузить страницу и убедиться, что соединения к `fonts.googleapis.com` и `fonts.gstatic.com` открыты до загрузки CSS; измерить LCP до/после (можно через Performance panel)
PRIORITY: 2 — небольшие изменения, но заметный прирост скорости загрузки шрифтов

IDEA: Добавить JSON‑LD BreadcrumbList для улучшения сниппетов в поиске
KNOB: В `<head>` вставить следующий скрипт (пример для текущего сайта):  
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Главная",
      "item": "https://saveliy-perm.ru/"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Лендинг",
      "item": "https://saveliy-perm.ru/"
    }
  ]
}
</script>
``` 
EFFECT: Позволяет поисковикам выводить «хлебные крошки» в результатах → повышает CTR и SEO‑видимость
RISK: Требует поддерживать актуальность URL‑ов; если структура изменится, нужно будет обновить скрипт
ROLLBACK: Удалить блок `<script type="application/ld+json">…</script>`
VERIFY: Вставить код, сохранить, открыть страницу в Google Rich Results Test → проверка, что BreadcrumbList валидный
PRIORITY: 2 — средний эффект, простая статическая разметка

IDEA: Добавить мета‑тег `robots` для явного указания индексации
KNOB: В `<head>` добавить строку  
```html
<meta name="robots" content="index, follow">
``` 
EFFECT: Явно сообщает поисковикам, что страницу следует индексировать и следовать по ссылкам → устраняет возможные неопределённости в robots.txt
RISK: Минимальный; если в robots.txt уже есть противоположные директивы, может возникнуть конфликт (по приоритету meta‑тег победит)
ROLLBACK: Удалить добавленный `<meta>`‑тег
VERIFY: Открыть страницу, убедиться в наличии тега в source; проверить через SEO‑аудит (например, Screaming Frog) что статус «Allowed» для robots
PRIORITY: 3 — небольшая выгода, но хорошая практика

IDEA: SKILL — lazy-section-load
KNOB: **Name:** lazy-section-load  
**When to apply:** На статических лендингах с несколькими ниже‑заглавными секциями (hero, problem, steps, faq, price, final)  
**SAFE CSS:**  
```css
section {opacity:0;transform:translateY(20px);transition:opacity .4s ease,transform .4s ease}
section.in-view {opacity:1;transform:none}
```  
**SAFE JS:**  
```js
document.querySelectorAll('section').forEach(s=>{
  const obs=new IntersectionObserver((e,o)=>{e.forEach(i=>{if(i.isIntersecting){i.target.classList.add('in-view');o.unobserve(i.target)}})},{threshold:.1});
  obs.observe(s);
});
``` 
EFFECT: Отложенная отрисовка секций до момента, когда они попадают в viewport, уменьшает количество DOM‑элементов, рендерящихся сразу → сокращает время первой отрисовки и экономит ресурсы на мобильных устройствах
RISK: Требует поддержку IntersectionObserver (не работает в IE 11 без полифила); в старых браузерах все секции будут сразу видимы, что безопасно
ROLLBACK: Удалить добавленные стили и скрипт или откатить файл через `git checkout -- index.html`
VERIFY: Открыть страницу в мобильном режиме, открыть DevTools → Network → убедиться, что только первая секция загружается сразу; прокрутить вниз и наблюдать плавное появление секций (можно включить `console.log` в скрипте)
PRIORITY: 1 — значительное улучшение LCP и восприятия скорости без изменения контента.
