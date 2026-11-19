# localhost:8080/ovh/gpt-oss-120b  2026-11-17 04:07:26
duration=41.7 error=- attempts=1

IDEA: Click‑Heatmap Console Logger  
KNOB: METHOD – В конец `<body>` добавить однострочный `<script>` :  
```js
(() => {
  const log = e => {
    const path = e.composedPath?.()[0] ?? e.target;
    console.log('CLICK', path.tagName, path.className, e.clientX, e.clientY);
  };
  document.addEventListener('click', log, {once: false});
  setTimeout(() => document.removeEventListener('click', log), 30000);
})();
```  
EFFECT: За 30 секунд фиксируются все клики, их целевые элементы и координаты – быстрый инсайт, какие блоки (CTA, ссылки, «боль») действительно привлекают внимание.  
RISK: Временно добавленный скрипт может слегка замедлить обработку событий, если забыть удалить.  
ROLLBACK: `git checkout -- index.html` или просто удалить вставленный `<script>`‑блок.  
VERIFY: Открыть страницу, открыть DevTools → Console, кликнуть по различным элементам – в консоли появятся записи; проверить, что клик по главному CTA логируется.  
PRIORITY: 1 – критично для подтверждения гипотезы о расположении CTA.

IDEA: URL‑Param Copy Switch for Instant A/B  
KNOB: METHOD – В `<head>` вставить скрипт, читающий параметр `?v=2` и переключающий класс `variant‑2` на `<body>`; в HTML добавить альтернативные тексты в атрибуты `data-alt` и показать их через CSS / JS. Пример:  
```js
(() => {
  const url = new URL(location);
  if (url.searchParams.get('v') === '2') document.body.classList.add('variant-2');
})();
```  
CSS:  
```css
.variant-2 h1::after{content:"Сайт за 2 дня — клиенты находят вас в Яндексе (тест)";}
.variant-2 .hero-note{display:none;}
```  
EFFECT: Позволяет мгновенно сравнивать два варианта заголовка или текста без деплоя, проверяя реакцию пользователей (через аналитику или быстрый опрос).  
RISK: Требует добавить `data‑alt`/CSS‑правила; если оставить, могут появиться лишние стили в продакшн‑версии.  
ROLLBACK: Удалить скрипт и связанные CSS‑правила; `git checkout -- index.html`.  
VERIFY: Открыть `index.html?v=2` и убедиться, что отображается альтернативный заголовок/текст; сравнить с обычным `index.html`.  
PRIORITY: 2 – быстрый способ тестировать копию, но менее критичен, чем проверка кликов.

IDEA: Scroll‑Funnel Visibility Logger  
KNOB: METHOD – В конец `<body>` добавить скрипт, использующий `IntersectionObserver` для всех `<section>` и выводящий в консоль порядок их появления:  
```js
(() => {
  const sections = document.querySelectorAll('section[id]');
  const order = [];
  const obs = new IntersectionObserver((e) => {
    e.forEach(i => {
      if (i.isIntersecting) {
        const id = i.target.id;
        if (!order.includes(id)) {
          order.push(id);
          console.log('SECTION VIEWED →', id);
        }
      }
    });
  }, {threshold: 0.5});
  sections.forEach(s => obs.observe(s));
  window.addEventListener('beforeunload', () => console.log('VIEW SEQUENCE:', order));
})();
```  
EFFECT: Позволяет увидеть, какие секции действительно видит пользователь в реальном порядке, проверяя гипотезу о том, что «Три шага» и «FAQ» находятся в «горячей» части воронки.  
RISK: Небольшой overhead от наблюдателя; при забытом удалении может оставаться в продакшн‑версии.  
ROLLBACK: Удалить скрипт; `git checkout -- index.html`.  
VERIFY: Открыть страницу, прокручивать её в обычном порядке, наблюдать в консоли сообщения «SECTION VIEWED → …»; убедиться, что порядок соответствует ожидаемому.  
PRIORITY: 2 – полезно для оптимизации структуры контента, но менее срочно, чем проверка кликов.
