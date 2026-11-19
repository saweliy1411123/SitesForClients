# localhost:8080/ovh/gpt-oss-120b  2026-11-17 08:30:57
duration=27.0 error=- attempts=1

IDEA: ARIA‑landmarks и роли для семантики и доступности  
KNOB: В `<body>` добавить атрибуты `role="banner"` к `<header class="hero">`, `role="navigation"` к `<nav class="nav-links">`, `role="main"` к основной секции (`<section id="main">` — создать, если нет), `role="region"` и `aria-labelledby` к каждому крупному `<section>` (price, steps, faq, final). Добавить `<footer role="contentinfo">` в конец.  
EFFECT: Улучшит восприятие скрин‑ридерами, повысит SEO‑оценку за счёт семантики, упростит навигацию клавиатурой → рост конверсии у пользователей с ограниченными возможностями.  
RISK: Небольшой риск конфликтов со стилями, если CSS‑селекторы используют `section` без учёта новых атрибутов.  
ROLLBACK: `git checkout HEAD -- index.html` (или откатить конкретный коммит, если сохраняется в отдельной ветке).  
VERIFY: Открыть страницу в Chrome DevTools → вкладка **Accessibility**; убедиться, что каждый элемент отмечен соответствующим landmark. Проверить, что клавиша Tab перемещается между секциями логично.  
PRIORITY: 1 – фундаментальная улучшение доступности и SEO, быстро реализуемо без бэкенда.  

---  

IDEA: Добавить OG‑изображение для соцсетей  
KNOB: В `<head>` после существующих OG‑тегов вставить  
```html
<meta property="og:image" content="https://example.com/assets/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Сайт‑лендинг Савелия: 2‑дневный запуск, лиды из Яндекса">
```  
(изображение разместить в `assets/og-image.jpg`, размер ≈ 120 KB).  
EFFECT: При шаринге ссылки в соцсетях (ВКонтакте, Telegram, Facebook) будет отображаться привлекательный превью‑картинка → рост кликов и переходов, повышенная узнаваемость бренда.  
RISK: Требует загрузки нового файла‑изображения — небольшое увеличение общего веса, но без влияния на LCP, если изображение не загружается в первую очередь.  
ROLLBACK: Удалить добавленные строки и файл‑изображение (`git checkout HEAD -- index.html assets/og-image.jpg`).  
VERIFY: Открыть `https://developers.facebook.com/tools/debug/` или `https://vk.com/dev/debugger` и ввести URL; убедиться, что OG‑image показывается корректно.  
PRIORITY: 2 – повышает внешнюю конверсию, но менее критично, чем доступность.  

---  

IDEA: Блок «Мы в прессе» – медиа‑упоминания с микроданными Organization  
KNOB: После секции `.price-card` (L644+) вставить  
```html
<section class="media-mentions" aria-labelledby="media-title">
  <h2 id="media-title" class="reveal">Нас упомянули</h2>
  <ul class="media-list">
    <li><a href="https://example.com/article1" target="_blank" rel="noopener"
          itemscope itemtype="https://schema.org/Article">
          <img src="assets/media1.png" alt="Logo «Biz»" loading="lazy">
          <meta itemprop="author" content="Biz Magazine">
          <meta itemprop="datePublished" content="2024-08-12">
        </a></li>
    <!-- repeat 3‑4 раза -->
  </ul>
</section>
```  
и добавить в `<head>` JSON‑LD:  
```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"Organization",
  "name":"Савелий",
  "url":"https://saveliy-perm.ru",
  "sameAs":["https://vk.com/saveliy","https://t.me/saveliy"],
  "mentions":[
    {"@type":"Article","url":"https://example.com/article1","name":"Biz Magazine"},
    {"@type":"Article","url":"https://example.com/article2","name":"TechNews"}
  ]
}
</script>
```  
EFFECT: Показ реальных медиа‑упоминаний повышает доверие (социальное доказательство), улучшает SEO за счёт дополнительных внешних ссылок и разметки, стимулирует клики из поисковой выдачи.  
RISK: Требует согласования с владельцами упомянутых изданий; если ссылки недоступны, может выглядеть как «фейковый» PR.  
ROLLBACK: Удалить вставленную секцию и скрипт (`git checkout HEAD -- index.html`).  
VERIFY: Проверить в Google Search Console → Rich Results Test, что `Organization` и `mentions` распознаются; визуально убедиться, что логотипы корректно загружаются и ссылки открываются.  
PRIORITY: 3 – добавляет уровень доверия, но требует внешних ресурсов и согласования; можно отложить после базовых улучшений.
