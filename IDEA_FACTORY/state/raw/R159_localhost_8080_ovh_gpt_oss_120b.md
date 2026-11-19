# localhost:8080/ovh/gpt-oss-120b  2026-11-17 09:21:25
duration=50.6 error=- attempts=1

IDEA: Preconnect & DNS‑prefetch для Google‑шрифтов  
KNOB: В `<head>` добавить сразу после существующих `<link>` строки  
```html
<link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
<link rel="dns-prefetch" href="https://fonts.gstatic.com">
```  
EFFECT: Сокращение времени установления соединения с CDN‑шрифтами → быстрее отрисовка текста, лучше Core Web Vitals (LCP).  
RISK: Небольшой рост заголовков HTTP‑запросов; без‑вредно.  
ROLLBACK: Удалить только добавленные две строки (git checkout -- index.html).  
VERIFY: Открыть DevTools → Network, включить “disable cache”, перезагрузить – увидеть, что запросы к fonts.googleapis.com/… уже инициированы до загрузки CSS.  
PRIORITY: 1 – низкая стоимость, высокий выигрыш для скорости и SEO.  

IDEA: Обернуть основной контент в `<main id="main">` и добавить ARIA‑леймарк  
KNOB: В `index.html` после закрывающего `</header>` (hero) вставить `<main id="main">` и перенести все секции (`#problem`, `#solution`, `#how`, `#works`, `#price`, `#faq`, `#final`) внутрь; в конце добавить `</main>`. Добавить атрибут `role="main"` к `<main>` (по‑молчанию уже main, но явно).  
EFFECT: Улучшает семантику для поисковых роботов и скрин‑ридеров, ускоряет навигацию клавиатурой, повышает SEO‑оценку структуры.  
RISK: Требует небольших правок в структуре; может сломать ссылки, если они полагались на прежний порядок (малый риск).  
ROLLBACK: Восстановить оригинальный файл из git (`git checkout -- index.html`).  
VERIFY: В Chrome DevTools → Elements увидеть `<main>` вокруг контента; использовать axe‑core (bookmarklet) – отсутствие ошибки “Landmark region missing”.  
PRIORITY: 1 – простая правка, сразу повышает доступность и SEO.  

IDEA: JSON‑LD FAQPage — микроразметка вопросов‑ответов  
KNOB: В `<head>` перед закрывающим `</head>` вставить скрипт  
```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Как быстро будет готов сайт?","acceptedAnswer":{"@type":"Answer","text":"За 2 дня после согласования ТЗ."}},
    {"@type":"Question","name":"Сколько стоит лендинг?","acceptedAnswer":{"@type":"Answer","text":"Одна фиксированная цена — {{price}} руб."}},
    {"@type":"Question","name":"Где будет размещён сайт?","acceptedAnswer":{"@type":"Answer","text":"На надёжном хостинге в России, с поддержкой Яндекс‑поиска."}}
  ]
}
</script>
```  
(заменить `{{price}}` на реальное значение).  
EFFECT: Позволяет поисковикам выводить расширенные сниппеты в результатах, повышая CTR.  
RISK: Требует актуализации при изменении вопросов; если JSON‑LD синтаксически ошибочен – может вызвать предупреждения в Search Console.  
ROLLBACK: Удалить вставленный `<script>` (git checkout -- index.html).  
VERIFY: В консоли выполнить `JSON.parse(document.querySelector('script[type="application/ld+json"]').innerHTML)` – отсутствие ошибок; в Rich Results Test от Google увидеть валидный FAQ.  
PRIORITY: 2 – важный SEO‑элемент, но требует проверки корректности текста.  

IDEA: Явный `role="navigation"` и `aria-label` для меню‑ссылок  
KNOB: Найти существующий контейнер навигации (вероятно `<nav class="nav-links">` или аналог) и добавить атрибуты  
```html
<nav class="nav-links" role="navigation" aria-label="Главное меню">
```  
EFFECT: Улучшает семантику и навигацию скрин‑ридеров, повышает SEO‑оценку структуры сайта.  
RISK: Минимальный – изменение атрибутов не влияет на визуальное отображение.  
ROLLBACK: Удалить добавленные атрибуты (git checkout -- index.html).  
VERIFY: В DevTools → Accessibility проверить, что элемент помечен как “navigation”.  
PRIORITY: 1 – быстрый апдейт, сразу повышает доступность.  

IDEA: `font-display: swap` через инлайн‑@font-face для ускоренного отображения текста  
KNOB: В `<style>` (или отдельный CSS‑файл) добавить перед импортом шрифтов:  
```css
@font-face {
  font-family: 'Manrope';
  src: url('https://fonts.gstatic.com/s/manrope/v13/...') format('woff2');
  font-weight: 400 700;
  font-display: swap;
}
```  
(использовать тот же URL, который генерирует Google Fonts). Затем заменить оригинальный `<link href="https://fonts.googleapis.com/css2?family=Manrope...">` на `<style>`‑блок выше и оставить `<link rel="preload" as="style" href="...">` если нужно.  
EFFECT: Текст будет виден сразу с системным шрифтом, а потом плавно заменён, снижается CLS и улучшает FCP/LCP.  
RISK: Потребуется корректный URL шрифта; если указать неверный – шрифт не загрузится.  
ROLLBACK: Восстановить оригинальный `<link>` к Google Fonts (git checkout -- index.html).  
VERIFY: В DevTools → Network фильтровать по “font”, увидеть, что запрос происходит после первой отрисовки; проверить метрику CLS (не должно увеличиваться).  
PRIORITY: 2 – небольшая работа, но заметно улучшает восприятие страницы и Core Web Vitals.
