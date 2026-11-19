# localhost:8080/ovh/gpt-oss-120b  2026-11-17 05:10:55
duration=34.9 error=- attempts=1

IDEA: URL‑hash A/B‑тест копий Hero‑заголовка  
KNOB: METHOD: в консоли Chrome выполнить скрипт, который при загрузке страницы читает `location.hash` (например `#vA` или `#vB`) и заменяет `innerHTML` элемента `.hero h1` и/или `.hero p.sub` на заранее заданные варианты, хранящиеся в объекте `variants`. Пример кода:  

```js
(() => {
  const variants = {
    vA: {h1:'Сайт за 2 дня — клиенты находят вас в Яндексе', sub:'Быстрый запуск, максимум продаж'},
    vB: {h1:'Ваш бизнес онлайн за 48 часов', sub:'Получайте заявки уже сегодня'}
  };
  const hash = location.hash.replace('#','');
  if (variants[hash]) {
    const h1 = document.querySelector('.hero h1');
    const sub = document.querySelector('.hero p.sub');
    if (h1) h1.textContent = variants[hash].h1;
    if (sub) sub.textContent = variants[hash].sub;
  }
})();
```  

EFFECT: позволяет за 1‑2 минуты переключать варианты текста, собрать вручную метрики кликов по CTA (через `console.log` в обработчике) и сравнить CTR без изменения репозитория.  

RISK: скрипт действует только в текущей сессии браузера; при перезапуске страницы без хеша изменения исчезнут.  

ROLLBACK: закрыть вкладку или удалить скрипт из консоли; при коммите просто не сохранять изменения.  

VERIFY: открыть страницу, открыть DevTools → Console, вставить скрипт, добавить `#vA` к URL, убедиться в изменённом заголовке, кликнуть CTA и посмотреть `console.log` счётчик; повторить с `#vB`.  

PRIORITY: 2 – быстрый, не требует правок кода, даёт прямую метрику CTR, полезно для выбора лучшего месседжа.  

---  

IDEA: Локальный измеритель «время от клика CTA до появления подтверждения»  
KNOB: METHOD: в консоли выполнить скрипт, который добавит `PerformanceObserver` на событие `click` у всех элементов с классом `.btn-primary`. При клике фиксируется `performance.now()`. Затем наблюдатель ждёт появления элемента с классом `.final .hero-note` (или любого подтверждающего сообщения) и выводит разницу в миллисекундах. Пример:  

```js
(() => {
  const observer = new PerformanceObserver(list => {
    list.getEntries().forEach(e => console.log('CTA latency:', e.duration.toFixed(2), 'ms'));
  });
  document.querySelectorAll('.btn-primary').forEach(btn => {
    btn.addEventListener('click', () => {
      const start = performance.now();
      const poll = setInterval(() => {
        if (document.querySelector('.final .hero-note')) {
          const end = performance.now();
          observer.observe({entryTypes:['measure']});
          performance.measure('cta-latency', {start, end});
          clearInterval(poll);
        }
      }, 50);
    });
  });
})();
```  

EFFECT: показывает, насколько быстро пользователь получает визуальную обратную связь после нажатия CTA, позволяя сравнить альтернативные варианты (например, добавить анимацию или изменить порядок DOM).  

RISK: скрипт работает только в текущей вкладке; если страница уже содержит аналогичный `PerformanceObserver`, возможны конфликты.  

ROLLBACK: перезагрузить страницу; скрипт не сохраняется.  

VERIFY: открыть страницу, открыть консоль, вставить скрипт, кликнуть любой CTA, посмотреть в консоли вывод «CTA latency: XXX ms». Сравнить результаты между вариантами (например, добавить/убрать анимацию в CSS и повторить).  

PRIORITY: 1 – критичный показатель UX; небольшая задержка в обратной связи резко влияет на конверсию, проверка занимает ≤ 5 минут.  

---  

IDEA: Быстрый «heatmap‑мок» кликов через локальное хранилище  
KNOB: METHOD: в консоли выполнить скрипт, который на каждый клик по странице сохраняет координаты `clientX/Y` в `localStorage` (массив). После 30 секунд (или после закрытия вкладки) скрипт рисует полупрозрачный canvas‑оверлей с кругами, размер которых пропорционален количеству кликов в данной области. Пример:  

```js
(() => {
  const KEY = 'clickHeatmap';
  const data = JSON.parse(localStorage.getItem(KEY)||'[]');
  document.addEventListener('click', e => {
    data.push({x:e.clientX, y:e.clientY});
    localStorage.setItem(KEY, JSON.stringify(data));
  });
  const draw = () => {
    const canvas = document.createElement('canvas');
    canvas.style.position='fixed';canvas.style.top=0;canvas.style.left=0;
    canvas.width=window.innerWidth;canvas.height=window.innerHeight;
    canvas.style.pointerEvents='none';canvas.style.zIndex=9999;
    document.body.appendChild(canvas);
    const ctx = canvas.getContext('2d');
    data.forEach(p => {
      const rad = 20;
      const grad = ctx.createRadialGradient(p.x,p.y,0,p.x,p.y,rad);
      grad.addColorStop(0,'rgba(255,0,0,0.4)');
      grad.addColorStop(1,'rgba(255,0,0,0)');
      ctx.fillStyle=grad;
      ctx.beginPath();ctx.arc(p.x,p.y,rad,0,2*Math.PI);ctx.fill();
    });
  };
  setTimeout(draw, 30000); // 30 сек
})();
```  

EFFECT: визуализирует, где пользователи действительно кликают (например, на CTA, навигацию, «пустые» зоны). Позволяет быстро оценить, насколько размещённые ссылки/кнопки привлекают внимание и где стоит добавить или переместить CTA.  

RISK: хранит данные в `localStorage` – при повторных запусках будет накапливаться; может замедлить страницу, если клик будет слишком частым.  

ROLLBACK: очистить `localStorage.removeItem('clickHeatmap')` и перезагрузить страницу; удалить добавленный canvas через DevTools.  

VERIFY: открыть страницу, открыть консоль, вставить скрипт, кликать по разным элементам в течение 30 сек, после чего появится полупрозрачный overlay; визуально оценить концентрацию кликов.  

PRIORITY: 3 – полезно для быстрой диагностики расположения CTA и проверки гипотез о «привлекательности» элементов без изменения кода; занимает ≤ 5 минут.
