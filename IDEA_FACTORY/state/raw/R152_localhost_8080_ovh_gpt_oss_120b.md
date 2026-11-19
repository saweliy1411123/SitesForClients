# localhost:8080/ovh/gpt-oss-120b  2026-11-17 09:01:49
duration=43.3 error=- attempts=1

IDEA: Preconnect + dns‑prefetch к Google Fonts  
KNOB: В `<head>` добавить сразу после существующих `<link>` строки  
```html
<link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
<link rel="dns-prefetch" href="https://fonts.gstatic.com">
```  
EFFECT: Уменьшит время установки соединения с CDN‑шрифтами → ускорит First Contentful Paint и First Meaningful Paint.  
RISK: Небольшой рост количества запросов в head; если пользователь блокирует сторонние запросы, эффект исчезнет (но сайт останется работоспособным).  
ROLLBACK: `git checkout index.html` или удалить добавленные две строки.  
VERIFY: Открыть страницу в Chrome DevTools → Network → Disable cache, измерить TTFB и время загрузки `fonts.googleapis.com` до и после правки (должно сократиться ≈ 30‑50 мс).  
PRIORITY: 1 — быстрый выигрыш в скорости без изменения контента.  

---  

IDEA: ARIA‑метки и role = button для всех CTA‑ссылок  
KNOB: Во всех `<a>`‑элементах, стилизованных как кнопки (класс `.btn-primary` и `.cta-row a`), добавить атрибуты `role="button"` и `aria-label="Получить демо"` (или уточняющий текст, если уже есть смысловой контент).  
EFFECT: Улучшит доступность для скрин‑ридеров, чётко объявит интерактивность, повысит конверсию за счёт снижения барьера для пользователей с ограниченными возможностями.  
RISK: Никаких визуальных изменений; если ссылка уже имеет понятный текст, `aria-label` может стать избыточным (но не нарушит).  
ROLLBACK: Удалить добавленные атрибуты через `git checkout index.html` или откатить конкретные строки.  
VERIFY: Включить Chrome Accessibility panel → “Screen Reader” → убедиться, что элемент объявляется как “button” и читается нужным текстом.  
PRIORITY: 2 — небольшое изменение, но критично для a11y и SEO (повышает показатель Core Web Vitals “Accessibility”).  

---  

IDEA: Поддержка системной темы (dark‑mode) через `color‑scheme`  
KNOB: В `<head>` добавить мета‑тег  
```html
<meta name="color-scheme" content="light dark">
```  
и в CSS (в глобальном блоке) добавить  
```css
@media (prefers-color-scheme: dark) {
  :root { --bg:#111; --text:#eee; --muted:#777; /* при необходимости корректировать остальные переменные */ }
}
```  
EFFECT: Пользователи, включившие тёмную тему в ОС/браузере, получат более комфортный визуал, что повышает удержание и показатель “User Experience”.  
RISK: Потребуется корректировать цвета переменных, иначе в dark‑mode могут появиться плохие контрасты; однако это легко исправимо.  
ROLLBACK: Удалить мета‑тег и CSS‑блок, либо откатить файл.  
VERIFY: Включить системный dark‑mode в браузере, проверить, что фон и текст меняются без потери контраста (контраст‑тест в DevTools → Accessibility).  
PRIORITY: 2 — небольшая стоимость, повышает восприятие бренда и SEO‑показатели (accessibility).  

---  

IDEA: JSON‑LD FAQPage для секции FAQ  
KNOB: В `<head>` сразу после остальных `<script type="application/ld+json">` добавить блок:  
```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"FAQPage",
  "mainEntity":[
    {"@type":"Question","name":"Как быстро будет готов сайт?","acceptedAnswer":{"@type":"Answer","text":"За 2 дня после согласования ТЗ."}},
    {"@type":"Question","name":"Какая стоимость?","acceptedAnswer":{"@type":"Answer","text":"Одна фиксированная цена — 30 000 ₽, без скрытых платежей."}}
    /* добавить остальные вопросы из HTML‑разметки */
  ]
}
</script>
```  
EFFECT: Поисковые системы смогут выводить ответы в виде расширенных сниппетов, увеличивая CTR и приток органического трафика.  
RISK: Требует поддерживать актуальность вопросов/ответов при изменении контента; в противном случае данные могут стать «мусором».  
ROLLBACK: Удалить JSON‑LD‑блок или откатить файл.  
VERIFY: В консоли DevTools выполнить `JSON.parse(document.querySelector('script[type="application/ld+json"]').innerHTML)` – убедиться в корректном JSON; затем проверить в Google Rich Results Test (вставить HTML‑фрагмент).  
PRIORITY: 1 — потенциальный рост органического трафика, реализация однострочная.  

---  

IDEA: Семантическая разметка секций — ARIA landmarks `role="region"` + `aria-labelledby`  
KNOB: Для каждой основной `<section id="...">` добавить атрибуты `role="region"` и `aria-labelledby="heading-id"` (где `heading-id` — id соответствующего заголовка, добавить `id` если его нет). Пример:  
```html
<section id="price" role="region" aria-labelledby="price-heading">
  <h2 id="price-heading">Цена</h2>
  …
</section>
```  
EFFECT: Упрощает навигацию скрин‑ридерами, улучшает семантику, положительно влияет на SEO (структурированность контента).  
RISK: Нужно добавить уникальные `id` к заголовкам; при дублировании может возникнуть конфликт, но легко исправить.  
ROLLBACK: Удалить добавленные атрибуты/идентификаторы через `git checkout`.  
VERIFY: Включить Chrome Accessibility panel → “Landmarks” и убедиться, что каждая секция появляется как отдельный регион с правильным названием.  
PRIORITY: 3 — улучшение доступности, но менее критично для конверсии, поэтому ниже срочности.
