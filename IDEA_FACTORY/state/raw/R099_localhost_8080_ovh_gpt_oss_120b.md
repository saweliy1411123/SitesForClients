# localhost:8080/ovh/gpt-oss-120b  2026-11-17 06:31:28
duration=28.2 error=- attempts=1

IDEA: Ясный «Что вы получите»‑лист под заголовком hero  
KNOB: Внутри `<header class="hero">` сразу после `<h1>` добавить `<ul class="hero-benefits"><li>Landing‑page за 2 дня</li><li>Оптимизация под Яндекс поиск</li><li>Подключение аналитики и формы обратной связи</li></ul>`; стилизовать список в одну колонку, шрифт Manrope, цвет var(--muted).  
EFFECT: Пользователь за 1‑2 секунды видит конкретный результат, повышается восприятие ценности и конверсия CTA.  
RISK: Небольшое увеличение HTML‑размера (≈200 Б); может потребовать небольшую правку CSS‑файла.  
ROLLBACK: `git checkout -- index.html` (или удалить только добавленные строки).  
VERIFY: Открыть страницу, измерить время до первого взаимодействия (LCP) в Chrome DevTools → Performance; убедиться, что список виден без скролла и не ломает верстку.  
PRIORITY: 1 — критично для ясности оффера, быстрый выигрыш в конверсии.  
SITE_REQUEST: hero  

---  

IDEA: Scroll‑triggered sticky CTA‑кнопка «Получить демо бесплатно»  
KNOB: Добавить в `<body>` элемент `<a href="#contact" class="btn-primary sticky-cta-scroll" role="button" aria-label="Получить демо бесплатно">Получить демо бесплатно <span class="arr">→</span></a>`; в CSS задать `.sticky-cta-scroll{position:fixed;bottom:-100px;right:20px;transition:bottom .4s;z-index:1000}` и `.sticky-cta-scroll.show{bottom:20px}`; подключить небольшой скрипт в конец `<body>`:  

```js
/* SAFE JS */
const cta=document.querySelector('.sticky-cta-scroll');
const hero=document.querySelector('.hero');
const observer=new IntersectionObserver(e=>{cta.classList.toggle('show',!e[0].isIntersecting);},{threshold:0});
observer.observe(hero);
```  

EFFECT: CTA появляется, когда пользователь уже увидел контент, повышая шансы клика без навязчивости.  
RISK: Требует JavaScript (маленький скрипт ≈1 KB); может конфликтовать с уже существующим `.sticky-cta`‑стилем.  
ROLLBACK: Удалить добавленный `<a>` и скрипт; либо `git checkout -- index.html`.  
VERIFY: Открыть страницу, прокрутить вниз; убедиться, что кнопка плавно появляется после выхода из hero; кликнуть – должна вести к секции `#contact`.  
PRIORITY: 2 — средний приоритет: улучшает конверсию без больших изменений.  

---  

IDEA: JSON‑LD BreadcrumbList для локального SEO и доверия  
KNOB: В `<head>` перед закрывающим `</head>` вставить скрипт‑блок:  

```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"BreadcrumbList",
  "itemListElement":[
    {"@type":"ListItem","position":1,"name":"Главная","item":"https://example.com/"},
    {"@type":"ListItem","position":2,"name":"Лендинги в Перми","item":"https://example.com/landing-perm"}
  ]
}
</script>
```  

(заменить `example.com` на реальный домен).  
EFFECT: Поисковые системы отображают «хлебные крошки» в результатах, повышая кликабельность и воспринимаемую надёжность.  
RISK: Требует корректного URL; если домен меняется, понадобится обновление.  
ROLLBACK: Удалить скрипт‑блок из `<head>`; `git checkout -- index.html`.  
VERIFY: В Chrome DevTools → Console выполнить `JSON.parse(document.querySelector('script[type="application/ld+json"]').innerHTML)`; убедиться в корректной структуре; проверить в Google Rich Results Test.  
PRIORITY: 3 — низкий приоритет, но полезен для SEO и доверия.
