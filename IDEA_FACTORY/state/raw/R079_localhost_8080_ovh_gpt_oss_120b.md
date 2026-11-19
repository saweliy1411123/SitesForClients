# localhost:8080/ovh/gpt-oss-120b  2026-11-17 05:30:51
duration=26.9 error=- attempts=1

IDEA: URL‑param A/B‑тест копий текста в hero  
KNOB: METHOD: в консоли выполнить скрипт, который читает `location.search` и в зависимости от параметра `variant` меняет `textContent` нужных элементов. Пример:  
```js
const v = new URLSearchParams(location.search).get('variant')
if (v === '2') {
  document.querySelector('.hero h1').textContent = 'Новый заголовок: клиенты из Яндекса уже ждут вас'
  document.querySelector('.hero p.sub').textContent = 'Запустим сайт за 2 дня и начнём привлекать заявки сразу'
}
```  
EFFECT: мгновенно сравниваются варианты копий без изменения кода и без деплоя, позволяя оценить влияние текста на клики по CTA.  
RISK: изменения видны только в текущей сессии; результаты могут отличаться от поведения реального трафика.  
ROLLBACK: перезагрузить страницу без параметра (`?variant=`) — все возвращается к исходному состоянию.  
VERIFY: открыть страницу, добавить `?variant=2` к URL, убедиться, что заголовок и подзаголовок изменились; при желании измерить количество кликов по CTA через DevTools → Network → Event Listener в течение 2‑5 минут.  
PRIORITY: 1 – быстрый способ проверить гипотезу о копирайтинге, высокий бизнес‑impact.  

IDEA: Real‑time CLS & LCP logger в консоли  
KNOB: METHOD: выполнить в консоли следующий скрипт, создающий `PerformanceObserver` для метрик Core Web Vitals и выводящего их в консоль:  
```js
let cls = 0
new PerformanceObserver(list => {
  for (const entry of list.getEntries()) {
    if (!entry.hadRecentInput) cls += entry.value
  }
  console.log('CLS:', cls.toFixed(4))
}).observe({type:'layout-shift', buffered:true})

new PerformanceObserver(list => {
  for (const entry of list.getEntries()) {
    console.log('LCP:', (entry.startTime/1000).toFixed(2), 's')
  }
}).observe({type:'largest-contentful-paint', buffered:true})
```  
EFFECT: позволяет за 1‑2 минуты увидеть, как текущие анимации (blobs, reveal) влияют на CLS и LCP, и быстро оценить эффект отключения/изменения их.  
RISK: метрики измеряются только в текущей вкладке и при текущих условиях сети; не заменяют полное Lighthouse‑исследование.  
ROLLBACK: закрыть вкладку или перезагрузить страницу — скрипт исчезает, состояние страницы восстанавливается.  
VERIFY: открыть страницу, вставить скрипт, записать значения CLS (<0.1) и LCP (<2.5 s); затем временно отключить анимацию (например, `document.body.classList.add('no-blob')`) и сравнить новые цифры. Всё занимает ≤5 минут.  
PRIORITY: 2 – важные метрики скорости, которые напрямую влияют на SEO и конверсию, но менее срочны, чем тест копий.  

IDEA: Accessibility‑tree inspection for screen‑reader order  
KNOB: METHOD: в Chrome DevTools открыть панель **Accessibility** (Esc → «Accessibility»), включить «Show accessibility properties», выбрать корневой элемент `<body>` и просмотреть «Computed Accessible Name/Role Order». Проверить, что порядок элементов (h1 → h2 → CTA‑links → формы) соответствует визуальному порядку и нет пропусков. При необходимости добавить `role`, `aria‑label` или корректировать порядок в HTML.  
EFFECT: гарантирует корректный порядок озвучивания скрин‑ридерами, повышая доступность и удовлетворяя требования WCAG 2.1 AA, что также положительно сказывается на SEO.  
RISK: требует базовых навыков работы с панелью Accessibility; может не выявить визуальные проблемы, только логические.  
ROLLBACK: проверка не вносит изменений; если обнаружены проблемы — исправлять в коде, а затем повторить проверку.  
VERIFY: открыть страницу, открыть DevTools → Accessibility, скопировать дерево и убедиться, что первая позиция — h1, далее секционные h2, затем интерактивные ссылки/кнопки; процесс занимает ≤5 минут.  
PRIORITY: 3 – улучшает доступность и репутацию бренда, но имеет более низкий прямой бизнес‑impact по сравнению с копирайтом и метриками скорости.
