# localhost:8080/ovh/gpt-oss-120b  2026-11-17 04:16:58
duration=37.2 error=- attempts=1

IDEA: Добавить канонический URL  
KNOB: В `<head>` вставить `<link rel="canonical" href="https://saveliy.ru/">` (заменить на реальный домен)  
EFFECT: Предотвращает возможные дубли страниц в индексации, повышает SEO‑вес оригинальной страницы  
RISK: Неправильный URL‑каноник может «отклонить» страницу из индекса  
ROLLBACK: `git checkout -- index.html` (или удалить только добавленную строку)  
VERIFY: Открыть страницу в Chrome → DevTools → Elements, убедиться, что в `<head>` есть `<link rel="canonical">` с нужным href; проверить в Search Console → Coverage, что статус “Valid”  
PRIORITY: 1 – канонический тег критичен для SEO и не требует ресурсов  

IDEA: JSON‑LD WebSite с SearchAction для Яндекса  
KNOB: В конец `<head>` добавить `<script type="application/ld+json">` с объектом:  
```json
{
  "@context":"https://schema.org",
  "@type":"WebSite",
  "url":"https://saveliy.ru/",
  "potentialAction":{
    "@type":"SearchAction",
    "target":"https://yandex.ru/search/?text={search_term_string}",
    "query-input":"required name=search_term_string"
  }
}
```  
EFFECT: Позволяет поисковикам понять, что сайт предлагает услугу «лендинги», улучшает отображение в результатах поиска (Rich Snippet)  
RISK: Ошибочный JSON‑LD может вызвать предупреждения в валидаторе Rich Results  
ROLLBACK: `git checkout -- index.html` (удалить блок `<script type="application/ld+json">`)  
VERIFY: В консоли DevTools выполнить `JSON.parse(document.querySelector('script[type="application/ld+json"]').textContent)` – должно вернуть объект без ошибок; в Google Rich Results Test (или Яндекс Веб‑мастер) убедиться в отсутствии ошибок  
PRIORITY: 2 – значительное SEO‑повышение, но менее критично, чем канонический URL  

IDEA: Добавить `role="region"` + `aria-label` к каждому `<section>` для скрин‑ридеров  
KNOB: В каждый `<section>` добавить атрибуты, напр. `<section id="price" role="region" aria-label="Ценовое предложение">` (подобрать метку по смыслу)  
EFFECT: Улучшает навигацию для пользователей‑слепых, повышает оценку доступности (Accessibility) и может положительно сказаться на SEO‑рейтинге за счёт лучшей семантики  
RISK: Неправильные метки могут ввести в заблуждение, но риск минимален  
ROLLBACK: `git checkout -- index.html` (удалить добавленные атрибуты)  
VERIFY: Открыть страницу, включить Chrome Accessibility Tree (DevTools → Elements → Accessibility) – каждый `<section>` должен отображаться как «region» с указанным `label`  
PRIORITY: 2 – быстро реализуемо, повышает доступность без изменения визуального вида  

IDEA: Предзагрузка (preload) фонового изображения hero‑секции  
KNOB: В `<head>` добавить `<link rel="preload" as="image" href="path/to/hero-bg.jpg">` (заменить на реальный путь к фоновой картинке, если используется CSS‑background‑image) и в CSS добавить `background-image: url('path/to/hero-bg.jpg');` если ещё нет  
EFFECT: Уменьшает время до первого отображения hero‑фона, улучшает показатель Largest Contentful Paint (LCP) → ускоряет загрузку, повышает Core Web Vitals  
RISK: Если путь к изображению неверный, браузер будет пытаться загрузить несуществующий ресурс, что замедлит загрузку; также увеличит количество запросов, если изображение уже кэшировано  
ROLLBACK: `git checkout -- index.html` (удалить строку `<link rel="preload">`)  
VERIFY: В Chrome Network tab включить «Disable cache», перезагрузить страницу, убедиться, что запрос к изображению имеет статус 200 и помечен как preload; проверить LCP в Lighthouse (Performance) – должно снизиться  
PRIORITY: 3 – полезно для скорости, но зависит от наличия реального фонового изображения; если фон задаётся CSS‑gradient, идея не применима.
