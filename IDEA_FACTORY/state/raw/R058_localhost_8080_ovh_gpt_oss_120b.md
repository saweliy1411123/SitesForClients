# localhost:8080/ovh/gpt-oss-120b  2026-11-17 04:29:01
duration=45.1 error=- attempts=1

IDEA: Duplicate‑ID & Missing‑ARIA Audit  
KNOB: METHOD: Открыть страницу в Chrome → DevTools → Console и выполнить скрипт:  
```js
(() => {
  // Duplicate IDs
  const ids = [...document.querySelectorAll('[id]')].map(el=>el.id);
  const dup = ids.filter((id,i)=>ids.indexOf(id)!==i);
  console.group('🔎 Duplicate IDs');
  dup.length ? console.table([...new Set(dup)]) : console.log('Нет дубликатов');
  console.groupEnd();

  // Интерактивные элементы без aria-label/aria-labelledby
  const interactive = [...document.querySelectorAll('a,button,[role="button"],[tabindex]')];
  const missingAria = interactive.filter(el=>!el.hasAttribute('aria-label') && !el.hasAttribute('aria-labelledby'));
  console.group('🔎 Interactive elements missing ARIA label');
  missingAria.length ? console.table(missingAria.map(el=>({tag:el.tagName, text:el.textContent.trim()}))) : console.log('Все имеют ARIA');
  console.groupEnd();
})();
```  
EFFECT: Быстро выявляет две частые проблемы — дублирующие id (нарушают семантику и могут ломать скрипты) и интерактивные ссылки/кнопки без описательных ARIA‑меток, повышая доступность и SEO.  
RISK: Нет (только чтение DOM).  
ROLLBACK: Не меняет файлы — просто закрыть консоль.  
VERIFY: После вставки скрипта в консоль увидеть две группировки — «Duplicate IDs» и «Interactive elements missing ARIA label»; отсутствие ошибок подтверждает чистый код.  
PRIORITY: 2 — важный для доступности и поисковой индексации, но не критичен для первой конверсии.  

---  

IDEA: First‑Contentful‑Paint & Time‑to‑Interactive Quick KPI  
KNOB: METHOD: В Chrome DevTools → Console выполнить:  
```js
(() => {
  const [fcp] = performance.getEntriesByName('first-contentful-paint');
  const tti = performance.timing.domContentLoadedEventEnd - performance.timing.navigationStart;
  console.log(`⏱ FCP: ${fcp ? Math.round(fcp.startTime) : 'N/A'} ms`);
  console.log(`⏱ Approx. TTI (DOMContentLoaded): ${tti} ms`);
})();
```  
EFFECT: Предоставляет мгновенные метрики — когда пользователь видит первый контент и когда DOM готов к интерактиву, позволяя оценить скорость загрузки без Lighthouse.  
RISK: Нет (чтение API браузера).  
ROLLBACK: Не вносит изменений; просто закрыть консоль.  
VERIFY: Откройте страницу, обновите (F5) и сразу выполните скрипт; в консоли появятся значения FCP и TTI, сравните их с целевыми (< 1000 ms FCP, < 1500 ms TTI).  
PRIORITY: 1 — скорость критична для SEO и удержания пользователей; быстрый KPI помогает решать, нужен ли дальнейший оптимизационный спринт.  

---  

IDEA: CTA Contrast‑Ratio Checker  
KNOB: METHOD: В консоли DevTools выполнить скрипт, указывая селектор CTA (по умолчанию `.btn-primary`):  
```js
(() => {
  const selector = '.btn-primary';
  const elems = document.querySelectorAll(selector);
  const toRgb = c => {
    const ctx = document.createElement('canvas').getContext('2d');
    ctx.fillStyle = c; return ctx.fillStyle;
  };
  const luminance = rgb => {
    const [r,g,b] = rgb.match(/\w\w/g).map(v=>parseInt(v,16)/255).map(v=>v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4));
    return 0.2126*r + 0.7152*g + 0.0722*b;
  };
  const contrast = (c1,c2)=> {
    const L1 = luminance(toRgb(c1)) + 0.05;
    const L2 = luminance(toRgb(c2)) + 0.05;
    return L1 > L2 ? L1/L2 : L2/L1;
  };
  elems.forEach(el=>{
    const fg = getComputedStyle(el).color;
    const bg = getComputedStyle(el).backgroundColor;
    const ratio = contrast(fg,bg).toFixed(2);
    console.log(`CTA "${el.textContent.trim()}" contrast: ${ratio}:1`);
  });
})();
```  
EFFECT: Мгновенно проверяет, удовлетворяют ли кнопки CTA WCAG 2.1 (минимум 4.5:1 для текста, 3:1 для крупного текста), улучшая читаемость и конверсию.  
RISK: Нет (только чтение стилей).  
ROLLBACK: Не меняет код; просто закрыть консоль.  
VERIFY: После выполнения скрипта в консоли появятся строки с коэффициентом контраста; если любой ниже 4.5, рекомендуется скорректировать цвета.  
PRIORITY: 3 — полезно для финальной полировки и соответствия доступности, но менее срочно, чем скорость или дубли‑id.
