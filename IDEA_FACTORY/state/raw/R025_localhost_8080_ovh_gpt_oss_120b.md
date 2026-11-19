# localhost:8080/ovh/gpt-oss-120b  2026-11-17 02:53:22
duration=61.1 error=- attempts=1

IDEA: Scroll‑cue arrow в hero‑секции  
KNOB: В конец `<header class="hero">` добавить `<div class="scroll-cue" aria-hidden="true"></div>` и в CSS `.scroll-cue{position:absolute;bottom:1rem;left:50%;transform:translateX(-50%);width:24px;height:24px;background:url('data:image/svg+xml,…') no‑repeat center;animation:bounce 2s infinite}`  
EFFECT: Пользователи сразу видят визуальный подсказку, что контент ниже, повышая глубину скролла и вовлечённость.  
RISK: Небольшой рост CSS‑веса; если анимация будет слишком навязчивой – может раздражать.  
ROLLBACK: `git checkout index.html` (удалить добавленные строки).  
VERIFY: Открыть страницу в мобильном режиме, убедиться, что стрелка видна и анимируется, и скролл вниз работает без смещения контента.  
PRIORITY: 1 – быстрый визуальный сигнал, повышающий показатель «скролл дальше» без кода‑бэка.  

IDEA: Предзагрузка и предсоединение к Google Fonts  
KNOB: В `<head>` добавить сразу после существующего `<link href="https://fonts.googleapis.com/css2?family=Manrope…">` две строки:  
```html
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap" onload="this.rel='stylesheet'">
```  
EFFECT: Уменьшит время до первого отображения текста, улучшит CLS и общий LCP.  
RISK: Если браузер не поддерживает `onload`‑переключение, шрифт может не загрузиться (но fallback‑шрифт уже есть).  
ROLLBACK: Удалить две строки из `<head>`.  
VERIFY: В Chrome DevTools → Network → filter “font”, проверить, что запрос к `fonts.gstatic.com` происходит раньше рендера; измерить LCP до/после (можно в Lighthouse).  
PRIORITY: 1 – ускорение критичного ресурса без изменения кода страницы.  

IDEA: Добавить meta‑тег canonical  
KNOB: В `<head>` после остальных `<meta>` вставить `<link rel="canonical" href="https://example.com/">` (заменить на реальный URL).  
EFFECT: Укрепит SEO, предотвратит дублирование контента, укажет поисковикам на основной URL.  
RISK: Ошибочный URL может привести к потере индексации.  
ROLLBACK: Удалить строку `<link rel="canonical"...>`.  
VERIFY: Открыть страницу, посмотреть в «View Page Source», убедиться в наличии тега; в Google Search Console проверить отсутствие ошибок «duplicate content».  
PRIORITY: 2 – небольшое изменение, но важный SEO‑фактор.  

IDEA: Open Graph image для соцсетей  
KNOB: В `<head>` добавить `<meta property="og:image" content="https://example.com/assets/og-image.jpg">` (URL к готовому 1200×630 px изображению).  
EFFECT: При шаринге в соцсетях будет отображаться привлекательный превью‑картинка, повышая CTR.  
RISK: Требуется подготовить изображение; если ссылка сломана, соцсети покажут пустой превью.  
ROLLBACK: Удалить строку `<meta property="og:image"...>`.  
VERIFY: Скопировать URL в «Sharing Debugger» (Facebook) или «Twitter Card Validator», убедиться, что картинка появляется.  
PRIORITY: 2 – повышает конверсию из соцсетей, простая правка.  

IDEA: JSON‑LD разметка FAQPage  
KNOB: В конец `<body>` добавить скрипт:  
```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Как быстро запускается сайт?","acceptedAnswer":{"@type":"Answer","text":"За 2 дня после предоставления материалов."}},
    {"@type":"Question","name":"Сколько стоит демо‑лендинг?","acceptedAnswer":{"@type":"Answer","text":"Бесплатно, без обязательств."}}
    /* добавить остальные вопросы */
  ]
}
</script>
```  
EFFECT: Поисковые системы могут вывести блоки вопросов‑ответов прямо в результатах, увеличивая видимость и кликабельность.  
RISK: Нужно поддерживать актуальность вопросов; если текст изменится, JSON‑LD может стать несоответствующим.  
ROLLBACK: Удалить весь `<script type="application/ld+json">…</script>` из тела.  
VERIFY: В Google Search Console → Rich Results Test ввести URL, убедиться, что разметка проходит без ошибок.  
PRIORITY: 2 – SEO‑выгода, небольшая нагрузка.  

IDEA: ARIA‑label для навигационных ссылок  
KNOB: В каждый `<a>` внутри навигации (например, `.nav-links a`) добавить атрибут `aria-label` с описанием пункта (e.g., `<a href="#price" aria-label="Перейти к разделу цены">Цена</a>`).  
EFFECT: Улучшит доступность для скрин‑ридеров, повышая WCAG‑соответствие.  
RISK: Неправильные описания могут ввести в заблуждение; требуется проверить каждый пункт.  
ROLLBACK: Удалить добавленные `aria-label` атрибуты.  
VERIFY: В Chrome DevTools → Accessibility, убедиться, что каждый элемент имеет читаемый label; можно использовать axe‑core bookmarklet для быстрой проверки.  
PRIORITY: 2 – небольшое изменение, но значимый шаг к доступности.  

IDEA: Поиск по FAQ (фильтр)  
KNOB: В секцию FAQ добавить над списком `<input type="search" id="faq-search" placeholder="Поиск по вопросам…" aria-label="Поиск по FAQ">` и небольшую JS‑функцию, которая скрывает `<details>` не содержащие запрос:  
```html
<script>
document.getElementById('faq-search').addEventListener('input', e=>{
  const term=e.target.value.toLowerCase();
  document.querySelectorAll('.faq-item').forEach(d=>{
    const q=d.querySelector('summary').textContent.toLowerCase();
    d.style.display = q.includes(term)||!term ? '' : 'none';
  });
});
</script>
```  
EFFECT: Пользователи быстрее находят нужный ответ, повышая удовлетворённость и снижая отток.  
RISK: Добавление JS (≈200 B) может слегка увеличить размер; если пользователь отключил JS, поиск не будет работать (не критично).  
ROLLBACK: Удалить `<input>` и `<script>` блок.  
VERIFY: Ввести запрос в поле, убедиться, что вопросы фильтруются в реальном времени.  
PRIORITY: 3 – улучшает UX, но менее критично, чем вышеуказанные изменения.
