# localhost:8080/ovh/gpt-oss-120b  2026-11-17 07:00:58
duration=41.7 error=- attempts=1

IDEA: Добавить OG‑изображение для соцсетей  
KNOB: В `<head>` добавить  
```html
<meta property="og:image" content="https://example.com/assets/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
```  
(заменить URL на реальное изображение проекта).  
EFFECT: При публикации ссылки в соцсетях будет показываться привлекательный превью‑картинка → рост CTR из соцсетей.  
RISK: Требуется разместить готовое изображение — если его нет, превью будет пустым.  
ROLLBACK: Удалить только добавленные `<meta>`‑теги (git checkout – путь‑к‑файлу).  
VERIFY: Открыть `https://developers.facebook.com/tools/debug/` и вставить URL сайта — картинка должна отобразиться.  
PRIORITY: 2 – небольшие изменения, но заметный эффект в соцсетях.  

IDEA: Добавить canonical‑ссылку  
KNOB: В `<head>` вставить  
```html
<link rel="canonical" href="https://saveliy-perm.ru/">
```  
EFFECT: Укрепляет SEO‑сигналы, предотвращает дублирование контента при разных URL.  
RISK: Неправильный URL может «отключить» индексацию нужной страницы.  
ROLLBACK: Удалить строку `<link rel="canonical"...>` (git checkout – файл).  
VERIFY: В Google Search Console выполнить URL‑Inspection и убедиться, что canonical — указанный URL.  
PRIORITY: 2 – простая правка, повышающая SEO‑стабильность.  

IDEA: Добавить кликабельный телефонный CTA  
KNOB: В секцию «финальный CTA» и в footer заменить/добавить ссылку‑кнопку:  
```html
<a href="tel:+73452700000" class="btn-primary">Позвонить сейчас</a>
```  
EFFECT: Пользователи мобильных устройств сразу могут позвонить → рост конверсий из мобильного трафика.  
RISK: Неправильный номер приведёт к потере звонков.  
ROLLBACK: Вернуть прежний текст ссылки (git checkout – файл).  
VERIFY: Открыть страницу на смартфоне, нажать кнопку — должен открыться набор номера.  
PRIORITY: 1 – прямой канал связи, высокий потенциал конверсии.  

IDEA: Внедрить схему Offer для цены  
KNOB: После блока `.price-card` добавить JSON‑LD:  
```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"Offer",
  "priceCurrency":"RUB",
  "price":"12000",
  "url":"https://saveliy-perm.ru/#price",
  "availability":"https://schema.org/InStock",
  "seller":{"@type":"LocalBusiness","name":"Савелий"}
}
</script>
```  
EFFECT: Появление rich‑snippet — цена в результатах поиска → повышенный CTR.  
RISK: Нужно поддерживать актуальность цены в схеме.  
ROLLBACK: Удалить блок `<script type="application/ld+json">` (git checkout – файл).  
VERIFY: Проверить в Google Rich Results Test, убедиться, что Offer распознан.  
PRIORITY: 2 – SEO‑выгода, небольшие усилия.  

IDEA: Защитить внешние ссылки атрибутами security  
KNOB: Во всех `<a href="https://…">` добавить `target="_blank" rel="noopener noreferrer"`.  
EFFECT: Предотвращает передачу `window.opener` и реферера, повышая безопасность и небольшую производительность.  
RISK: Нет.  
ROLLBACK: Удалить `target` и `rel` из всех ссылок (git checkout – файл).  
VERIFY: Открыть любую внешнюю ссылку, убедиться, что открывается в новой вкладке без передачи реферера (проверить в DevTools → Network → Headers).  
PRIORITY: 3 – небольшое улучшение безопасности, но полезно.  

IDEA: Добавить индикатор «прокрутить вниз» под hero  
KNOB: Внутри `<header class="hero">` сразу после закрывающего `</div>` добавить  
```html
<a href="#pain" class="scroll-indicator" aria-label="Показать ниже">
  <svg width="24" height="24" aria-hidden="true"><path d="M12 16l-6-6h12z"/></svg>
</a>
```  
и в CSS:  
```css
/* SAFE CSS */
.scroll-indicator{
  position:absolute;bottom:20px;left:50%;transform:translateX(-50%);
  animation: bounce 2s infinite;
}
@keyframes bounce{0%,100%{transform:translate(-50%,0)}50%{transform:translate(-50%,10px)}}
```  
EFFECT: Пользователю сразу ясно, что контент продолжается ниже, снижается показатель отказов.  
RISK: Возможен визуальный шум на маленьких экранах.  
ROLLBACK: Удалить только добавленный `<a>` и CSS‑правила (git checkout – файл).  
VERIFY: Открыть страницу, увидеть стрелку, клик — скролл к секции `#pain`.  
PRIORITY: 2 – улучшение UX за минимум кода.  

IDEA: Переключатель «мес/год» в блоке цены  
KNOB: Внутри `.price-card` добавить переключатель:  
```html
<label class="price-toggle">
  <input type="radio" name="priceMode" value="monthly" checked> мес.
  <input type="radio" name="priceMode" value="yearly"> год.
</label>
<span class="price-value">12 000 ₽</span>
```  
и небольшую JS‑логика (SAFE JS):  
```js
document.querySelectorAll('.price-toggle input').forEach(i=>{
  i.addEventListener('change',e=>{
    const price = e.target.value==='monthly'?'12 000 ₽':'120 000 ₽';
    document.querySelector('.price-value').textContent = price;
  });
});
```  
EFFECT: Позволяет пользователю увидеть более выгодный годовой тариф, повышает восприятие
