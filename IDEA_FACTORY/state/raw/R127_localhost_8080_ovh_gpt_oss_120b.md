# localhost:8080/ovh/gpt-oss-120b  2026-11-17 07:50:57
duration=22.3 error=- attempts=1

IDEA: Sticky floating CTA‑button — «Получить демо» в правом нижнем углу  
KNOB: В `<body>` добавить `<a href="#final" class="sticky-cta btn-primary" role="button" aria-label="Получить бесплатное демо сайта">Получить демо</a>`; в CSS добавить  
```css
.sticky-cta{
  position:fixed;right:1rem;bottom:1rem;
  background:var(--grad);color:#fff;
  padding:.75rem 1.2rem;border-radius:8px;
  box-shadow:0 4px 12px rgba(0,0,0,.15);
  transition:transform .2s,opacity .2s;
  z-index:1000;
}
.sticky-cta:hover{transform:translateY(-3px)}
@media(max-width:720px){
  .sticky-cta{right:.5rem;bottom:.5rem;padding:.6rem .9rem}
}
```  
EFFECT: Увеличит видимость основного CTA на всех скроллах, особенно на мобильных, повышая конверсию запросов.  
RISK: Может слегка замедлить рендер из‑за дополнительного элемента, но влияние минимально.  
ROLLBACK: `git checkout -- index.html` (или удалить только добавленные строки).  
VERIFY: Открыть страницу, прокрутить вниз — кнопка должна оставаться в правом нижнем углу, клик по ней вести к секции #final; проверить в DevTools отсутствие перекрытия контента.  
PRIORITY: 1 — быстрый, low‑risk апдейт с высоким потенциалом конверсии.  

---  

IDEA: Блок «Отзывы клиентов»‑карусель с микроданными Review (schema.org)  
KNOB: После секции `.price-card` (L644) вставить  
```html
<section id="testimonials" class="testimonials">
  <h2 class="reveal">Что говорят клиенты</h2>
  <div class="carousel">
    <blockquote class="review">
      <p>«Сайт за 2 дня принес мне 15 новых заявок уже в первую неделю!»</p>
      <footer>Иван Иванов, <cite>Салон красоты «Люкс»</cite></footer>
    </blockquote>
    <blockquote class="review">
      <p>«Быстрая загрузка и отличная позиция в Яндексе – клиенты приходят сами.»</p>
      <footer>Мария Петрова, <cite>Кофейня «Арома»</cite></footer>
    </blockquote>
  </div>
</section>
```  
CSS (добавить в файл):  
```css
.testimonials{padding:80px 0;text-align:center}
.carousel{display:flex;overflow-x:auto;gap:2rem;scroll-snap-type:x mandatory}
.review{flex:0 0 80%;scroll-snap-align:center;background:#fff;
        border-radius:12px;padding:1.5rem;box-shadow:0 4px 12px rgba(0,0,0,.1)}
```  
В `<head>` добавить JSON‑LD:  
```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"Review",
  "author":{"@type":"Person","name":"Иван Иванов"},
  "reviewBody":"Сайт за 2 дня принес мне 15 новых заявок уже в первую неделю!",
  "reviewRating":{"@type":"Rating","ratingValue":"5"},
  "itemReviewed":{"@type":"Service","name":"Лендинг за 2 дня"}
}
</script>
```  
(повторить для остальных отзывов).  
EFFECT: Доверие — социальное доказательство повышает конверсию, а schema.org Review улучшает SEO в поиске.  
RISK: Требует реальных отзывов; использование вымышленных может нарушать честность.  
ROLLBACK: Удалить вставленные блоки и скрипт; `git checkout -- index.html`.  
VERIFY: В браузере увидеть плавный горизонтальный скролл отзывов, кликнуть — нет переложения; в Chrome DevTools → Structured Data Testing Tool проверить наличие Review.  
PRIORITY: 2 — важный trust‑signal, но требует реальных отзывов; умеренный effort.  

---  

IDEA: Breadcrumb‑навигация + JSON‑LD BreadcrumbList для SEO и пользовательской ориентации  
KNOB: В начале `<body>` (после `<header>`) добавить  
```html
<nav aria-label="Навигация по сайту" class="breadcrumbs">
  <ul>
    <li><a href="/">Главная</a></li>
    <li><a href="#price">Цена</a></li>
    <li aria-current="page">Демо</li>
  </ul>
</nav>
```  
CSS:  
```css
.breadcrumbs{font-size:.875rem;margin:1rem 0}
.breadcrumbs ul{display:flex;gap:.4rem;list-style:none}
.breadcrumbs li::after{content:"›";margin-left:.4rem}
.breadcrumbs li:last-child::after{content:"";margin:0}
.breadcrumbs a{color:var(--muted);text-decoration:none}
.breadcrumbs a:hover{color:var(--text)}
```  
В `<head>` добавить JSON‑LD:  
```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"BreadcrumbList",
  "itemListElement":[
    {"@type":"ListItem","position":1,"name":"Главная","item":"/"},
    {"@type":"ListItem","position":2,"name":"Цена","item":"#price"},
    {"@type":"ListItem","position":3,"name":"Демо","item":"#demo"}
  ]
}
</script>
```  
EFFECT: Улучшает восприятие структуры страницы пользователями и повышает шанс появления в поисковых сниппетах «хлебные крошки», тем самым повышая кликабельность из SERP.  
RISK: Небольшой рост HTML‑веса; если ссылки изменятся, нужно будет поддерживать актуальность.  
ROLLBACK: Удалить `<nav class="breadcrumbs">` и JSON‑LD; `git checkout -- index.html`.  
VERIFY: Открыть страницу, увидеть горизонтальный список «Главная › Цена › Демо», в Chrome DevTools → Rich Results Test подтвердить BreadcrumbList.  
PRIORITY: 3 — низкоуровневый SEO‑улучшающий элемент, небольшие усилия, но полезен в долгосрочной перспективе.
