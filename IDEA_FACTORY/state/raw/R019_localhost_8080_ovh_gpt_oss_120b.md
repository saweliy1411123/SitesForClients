# localhost:8080/ovh/gpt-oss-120b  2026-11-17 02:35:37
duration=22.8 error=- attempts=2

IDEA: Добавить мета‑тег robots «index, follow»  
KNOB: В `<head>` после существующих `<meta>` вставить `<meta name="robots" content="index, follow">`  
EFFECT: Убедится, что поисковые роботы индексируют страницу и учитывают ссылки, повышая шанс появления в результатах поиска.  
RISK: Минимальный – может конфликтовать с будущей политикой noindex, если владелец изменит стратегию.  
ROLLBACK: `git checkout HEAD -- index.html` (или удалить строку вручную)  
VERIFY: Открыть страницу в браузере → «View source» → убедиться, что тег присутствует; запустить Lighthouse → SEO‑раздел, проверка «Meta robots tag».  
PRIORITY: 1 – базовый SEO‑фактор, прост в реализации, быстрый выигрыш.  

IDEA: Внедрить разметку schema.org Service для локального SEO  
KNOB: В конец `<body>` добавить `<script type="application/ld+json">` с JSON‑LD:  
```json
{
  "@context":"https://schema.org",
  "@type":"Service",
  "name":"Лендинги за 2 дня",
  "provider":{"@type":"LocalBusiness","name":"Савелий","areaServed":"Пермь"},
  "offers":{"@type":"Offer","priceCurrency":"RUB","price":"0","availability":"https://schema.org/InStock"},
  "serviceType":"Создание лендингов",
  "url":"https://example.com/"
}
```  
EFFECT: Предоставит поисковикам точную информацию о предлагаемой услуге, улучшит видимость в локальном поиске и в блоке «Услуги».  
RISK: Требует согласования цены (указана 0 RUB как «демо бесплатно») – может потребоваться корректировка при изменении цены.  
ROLLBACK: `git checkout HEAD -- index.html`  
VERIFY: В DevTools → «Console» → выполнить `JSON.parse(document.querySelector('script[type="application/ld+json"]').innerHTML)` без ошибок; в Google Rich Results Test загрузить страницу и убедиться в валидности Service.  
PRIORITY: 2 – повышает SEO, но требует точных данных; небольшая работа, но ценность выше, чем у простого meta‑тега.  

IDEA: Скрыть декоративные SVG от скрин‑ридеров  
KNOB: Для всех inline‑SVG, используемых как фон/декор (поиск `data:image/svg+xml` в CSS/HTML), добавить атрибут `aria-hidden="true"` и `focusable="false"` (если в HTML) либо в CSS добавить `svg{pointer-events:none;}` если они только визуальны.  
EFFECT: Уменьшит «шум» для пользователей скрин‑ридеров, улучшит доступность без визуального изменения.  
RISK: Если какой‑то SVG несёт смысловую нагрузку, он станет недоступным; необходимо проверять каждый случай.  
ROLLBACK: Удалить добавленные атрибуты/правило из CSS.  
VERIFY: Включить режим «Screen Reader» (NVDA/VoiceOver) → переместиться к секции с SVG, убедиться, что они не объявляются; в DevTools → Elements → проверить наличие `aria-hidden`.  
PRIORITY: 3 – небольшое улучшение доступности, низкий риск, легко откатывается.  

IDEA: Добавить CSS‑свойство will‑change для анимированных элементов (magnetic‑кнопки, reveal)  
KNOB: В файле стилей (внутри `<style>` или подключённого CSS) добавить к селекторам `.magnetic, .reveal` правило `will-change: transform, opacity;`  
EFFECT: Подскажет браузеру, какие свойства будут анимированы, улучшит плавность анимаций и снизит CLS, особенно на мобильных устройствах.  
RISK: При избыточном использовании может увеличить потребление памяти; ограничиваем только анимируемые элементы.  
ROLLBACK: Удалить правило `will-change` из стилей.  
VERIFY: Открыть страницу в Chrome → DevTools → Performance → записать анимацию до и после; сравнить FPS и CLS; визуально убедиться в отсутствии замедления.  
PRIORITY: 3 – небольшое улучшение производительности, простая правка, небольшие риски.
