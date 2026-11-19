# localhost:8080/ovh/gpt-oss-120b  2026-11-17 08:14:20
duration=36.9 error=- attempts=1

IDEA: METHOD — Unused CSS selector audit  
KNOB: METHOD: В консоли DevTools выполнить скрипт, который перебирает все правила из `<style>` и `<link rel="stylesheet">`, для каждого `rule.selectorText` делает `document.querySelectorAll(rule.selectorText)`. Если массив пуст — логировать селектор как «неиспользуемый».  
EFFECT: Быстрая диагностика «мёртвого» CSS — уменьшит размер стилей, ускорит рендер и снизит риск конфликтов.  
RISK: Нет (только чтение DOM, без изменений).  
ROLLBACK: Закрыть консоль / перезагрузить страницу (изменения не сохраняются).  
VERIFY: Запустить скрипт, убедиться, что в консоли выводятся только селекторы, не находящие элементы (если список пуст — всё ОК).  
PRIORITY: 2 — важно для скорости, но не критично для конверсии.  

---  

IDEA: METHOD — First Contentful Paint measurement  
KNOB: METHOD: В консоли DevTools выполнить однострочник:  

```js
new PerformanceObserver(list=>{
  list.getEntriesByName('first-contentful-paint')
      .forEach(e=>console.log('FCP:', e.startTime.toFixed(2), 'ms'));
}).observe({type:'paint',buffered:true});
```  

EFFECT: Мгновенный вывод FCP — позволит сравнить варианты hero‑копий/стилей без деплоя, оценить восприятие скорости.  
RISK: Нет (только чтение Perf API).  
ROLLBACK: Закрыть консоль / перезагрузить страницу.  
VERIFY: После выполнения скрипта в консоли появится строка `FCP: <value> ms`. При смене вариантов (например, изменяя текст в dev‑инспекторе) повторить — разница будет видна.  
PRIORITY: 1 — ключевой показатель восприятия скорости, быстрый и лёгкий способ сравнения гипотез.  

---  

IDEA: METHOD — Layout‑Shift (CLS) audit для hero‑раздела  
KNOB: METHOD: В консоли DevTools выполнить скрипт, который слушает `layout-shift` и выводит только те события, где `entry.value>0` и `entry.sources.some(s=>s.node && s.node.closest('.hero'))`.  

```js
new PerformanceObserver(obs=>{
  obs.getEntries()
    .filter(e=>e.value>0 && e.sources.some(s=>s.node?.closest('.hero')))
    .forEach(e=>console.log('CLS hero shift:', e.value.toFixed(4)));
}).observe({type:'layout-shift',buffered:true});
```  

EFFECT: Позволит мгновенно увидеть, вызывают ли анимации/blobs в hero‑секции визуальные сдвиги, которые ухудшают Core Web Vitals, и сравнить варианты (например, отключив анимацию).  
RISK: Нет (только наблюдатель).  
ROLLBACK: Закрыть консоль / перезагрузить страницу.  
VERIFY: Открыть страницу, посмотреть в консоли сообщения `CLS hero shift: …`. При отсутствии вывода — сдвигов нет; при появлении — нужно оптимизировать.  
PRIORITY: 1 — CLS напрямую влияет на ранжирование и пользовательский опыт; быстрый способ выявить проблемные анимации.
