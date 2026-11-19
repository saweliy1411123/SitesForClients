# localhost:8080/ovh/gpt-oss-120b  2026-11-17 05:58:38
duration=60.4 error=- attempts=1

IDEA: I-00601 Add Open Graph image meta tag for richer social sharing  
KNOB: В `<head>` добавить  
```html
<meta property="og:image" content="https://example.com/assets/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
```  
EFFECT: При публикации ссылки в соцсетях будет отображаться привлекательный превью‑картинка → рост CTR из соцсетей.  
RISK: Требуется разместить реальное изображение — если путь неверный, будет битый превью.  
ROLLBACK: `git checkout HEAD -- index.html` или удалить добавленные три строки.  
VERIFY: Открыть страницу, открыть DevTools → Network → проверить запрос `og:image`; либо воспользоваться Facebook Sharing Debugger, убедиться, что картинка отображается.  
PRIORITY: 2 – низкая сложность, средний SEO‑эффект.

IDEA: I-00602 Добавить ARIA‑метки role="button" и aria‑label ко всем CTA‑ссылкам  
KNOB: Для каждой `<a class="btn-primary …">` добавить атрибуты `role="button"` и уникальный `aria-label` (например, `aria-label="Получить демо бесплатно"`).  
EFFECT: Улучшит доступность для скрин‑ридеров, повысит соответствие WCAG 2.1 AA.  
RISK: Нужно править несколько мест; риск забыть один из CTA.  
ROLLBACK: `git checkout HEAD -- index.html` или удалить атрибуты.  
VERIFY: Запустить axe‑core (или Chrome Lighthouse → Accessibility) и убедиться, что у всех CTA есть `role="button"` и `aria-label`.  
PRIORITY: 1 – критичный пункт доступности.

IDEA: I-00603 Визуализировать «стоимость бездействия» в блоке боли через простой счётчик  
KNOB: После третьего `<h3>` в секции боли вставить  
```html
<div class="cost-counter" aria-live="polite">
  <strong>Каждый день без сайта — ≈ <span id="lost-clients">3</span> потенциальных клиента</strong>
</div>
<script>
  (function(){
    const el=document.getElementById('lost-clients');
    let n=3;
    setInterval(()=>{ n+=1; el.textContent=n; },5000);
  })();
</script>
```  
EFFECT: Явная цифра усиливает чувство срочности → рост конверсии в CTA.  
RISK: Добавление небольшого JS может слегка увеличить LCP; нужно убедиться, что скрипт лёгкий.  
ROLLBACK: Удалить блок `<div class="cost-counter">…</div>` и `<script>`‑блок.  
VERIFY: Открыть страницу, убедиться, что цифра увеличивается каждые 5 сек., проверить, что в DevTools → Performance → LCP не растёт более 100 мс.  
PRIORITY: 2 – умеренный UX‑эффект, лёгкая реализация.

IDEA: I-00604 Пронумеровать шаги в секции «Три шага» с помощью CSS‑счётчика  
KNOB: В CSS добавить  
```css
.steps {counter-reset: step;}
.steps h3::before{
  counter-increment: step;
  content: counter(step) ". ";
  font-weight:700;
  margin-right:.4rem;
}
```  
и в HTML убедиться, что шаги находятся внутри контейнера с классом `.steps`.  
EFFECT: Чёткая нумерация повышает сканируемость и запоминаемость процесса.  
RISK: Возможен конфликт с уже существующими стилями `h3`; потребуется небольшая корректировка.  
ROLLBACK: Удалить добавленные правила CSS.  
VERIFY: В браузере проверить, что перед каждым заголовком шага появляется цифра 1‑3.  
PRIORITY: 3 – небольшой визуальный апгрейд, низкая сложность.

IDEA: I-00605 Добавить лёгкий CSS‑слайдер отзывов (только flex + scroll‑snap)  
KNOB: Обернуть текущие отзывы (см. `SITE_REQUEST "отзывы"`) в контейнер  
```html
<div class="testimonials">
  <div class="testimonial">…</div>
  <div class="testimonial">…</div>
  <div class="testimonial">…</div>
</div>
```  
и в CSS добавить  
```css
.testimonials{
  display:flex; overflow-x:auto; scroll-snap-type:x mandatory;
  gap:1rem; padding:1rem 0;
}
.testimonial{
  flex:0 0 80%; scroll-snap-align:center;
  background:#fff; border-radius:8px; padding:1rem;
}
```  
EFFECT: Динамический блок соц‑доказательств без JS повышает доверие и удерживает внимание.  
RISK: На очень узких экранах может выглядеть срезанным; потребуется медиазапросы.  
ROLLBACK: Удалить контейнер и CSS‑правила.  
VERIFY: Прокрутить горизонтально, убедиться, что каждый отзыв «прилипает» к центру.  
PRIORITY: 2 – средний UX‑эффект, без нагрузки JS.

IDEA: I-00606 Внедрить видимую хлебную крошку + JSON‑LD Breadcrumb‑разметку  
KNOB: Сразу после `<header>` вставить  
```html
<nav class="breadcrumb" aria-label="Хлебные крошки">
  <a href="/">Главная</a> / <span>Лендинг</span>
</nav>
```  
и в конец `<body>` добавить  
```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"BreadcrumbList",
  "itemListElement":[
    {"@type":"ListItem","position":1,"name":"Главная","item":"https://example.com/"},
    {"@type":"ListItem","position":2,"name":"Лендинг","item":"https://example.com/landing"}
  ]
}
</script>
```  
EFFECT: Улучшает навигацию для пользователей и даёт поисковикам структурированные подсказки → потенциальный рост в SERP.  
RISK: Нужны корректные URL‑адреса; если сайт будет перенесён, ссылки могут стать неверными.  
ROLLBACK: Удалить вставленный `<nav>` и `<script>`.  
VERIFY: Проверить в Google Rich Results Test, что Breadcrumb распознан.  
PRIORITY: 2 – полезно для SEO, умеренная сложность.

IDEA: I-00607 Добавить роль region + aria‑labelledby к каждому `<section>` для скрин‑ридеров  
KNOB: Для каждой секции добавить атрибуты, например:  
```html
<section id="pain" role="region" aria-labelledby="pain-heading">
  <h2 id="pain-heading">Запись есть — клиентов из поиска нет</h2>
  …
</section>
```  
(повторить для всех семи секций).  
EFFECT: Позволяет пользователям скрин‑ридеров быстро перемещаться между логическими блоками, повышая доступность.  
RISK: Требует уникальных `id`‑ов для заголовков; возможна конфликтность при дублировании.  
ROLLBACK: Удалить добавленные атрибуты.  
VERIFY: В DevTools → Accessibility проверить, что каждая секция отображается как «region» с правильным названием.  
PRIORITY: 1 – высокий приоритет для соответствия WCAG 2.1 AA.

IDEA: I-00608 Добавить JSON‑LD Offer‑разметку к ценовому блоку  
KNOB: В конец `<body>` добавить скрипт:  
```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"Offer",
  "url":"https://example.com/#price",
  "priceCurrency":"RUB",
  "price":"19990",
  "priceValidUntil":"2027-12-31",
  "availability":"https://schema.org/InStock",
  "itemOffered":{
    "@type
