# localhost:8080/ovh/gpt-oss-120b  2026-11-17 08:53:17
duration=31.3 error=- attempts=1

IDEA: Instant accessibility audit with axe‑core  
KNOB: METHOD: открываем страницу в Chrome DevTools → консоль, вставляем однострочник `let s=document.createElement('script');s.src='https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.9.1/axe.min.js';s.onload=()=>axe.run((err,r)=>console.table(r.violations));document.head.appendChild(s);` – скрипт загружает axe‑core и выводит в консоль таблицу всех найденных нарушений a11y.  
EFFECT: мгновенно получает список проблем WCAG 2.1 (контраст, отсутствие ARIA‑атрибутов, недоступные элементы), позволяя быстро оценить, какие правки приоритетнее.  
RISK: подключение внешнего CDN‑скрипта (может быть недоступно в офлайн‑среде).  
ROLLBACK: удалить только что добавленный `<script>`‑элемент (`document.querySelector('script[src*="axe.min.js"]').remove();`).  
VERIFY: после вставки в консоль должна появиться таблица `violations` с `id`, `description`, `impact`; отсутствие ошибок – положительный результат.  
PRIORITY: 1 – доступность критична для SEO и конверсии, а проверка занимает ≈ 2 минуты.  

IDEA: Measure Largest Contentful Paint of primary CTA  
KNOB: METHOD: в консоли выполнить `new PerformanceObserver((list)=>{list.getEntries().forEach(e=>{if(e.element && e.element.closest('.cta') ) console.log('CTA LCP:',e.startTime);});}).observe({type:'largest-contentful-paint', buffered:true});` – наблюдатель фиксирует LCP‑события и выводит время, когда в viewport попадает элемент с классом `.cta` (или ссылкой `#final`).  
EFFECT: показывает, насколько быстро пользователь видит главный призыв к действию; позволяет сравнивать варианты дизайна (например, изменение позиционирования CTA).  
RISK: если на странице нет элементов с `.cta`, наблюдатель ничего не выведет – потребует уточнения селектора.  
ROLLBACK: просто перезагрузить страницу (очистка PerformanceObserver).  
VERIFY: после перезагрузки и скроллинга до CTA в консоли появляется строка `CTA LCP: <ms>`; сравнить значения между вариантами.  
PRIORITY: 2 – быстрая метрика UX, влияет на конверсию, но менее критична, чем доступность.  

IDEA: Keyboard‑navigation order audit  
KNOB: METHOD: в консоли выполнить скрипт, который программно имитирует нажатие Tab 10 раз, собирает `document.activeElement` после каждого нажатия и выводит список селекторов в порядке фокусировки:  

```js
(async()=>{let order=[];for(let i=0;i<15;i++){await new Promise(r=>setTimeout(r,100));document.dispatchEvent(new KeyboardEvent('keydown',{key:'Tab'}));order.push(document.activeElement.outerHTML); }console.table(order);})();
```  

EFFECT: быстро выявляет «потерянные» ссылки/кнопки, неправильный порядок фокуса и отсутствие `:focus-visible`‑стилей, что улучшает конверсию с клавиатуры и SEO‑оценку.  
RISK: имитация Tab может не покрыть все интерактивные элементы, если их количество > 15 – требует увеличить цикл вручную.  
ROLLBACK: перезагрузка страницы (сбросит фокус).  
VERIFY: в консоли появляется таблица `order` со строками‑HTML текущих фокусируемых элементов; проверяем, что первая строка — логотип/навигация, а последняя — CTA.  
PRIORITY: 3 – полезно для доступности, но менее ощутимое влияние на конверсию по сравнению с LCP‑CTA; проверка занимает ≈ 5 минут.
