# localhost:8080/ovh/gpt-oss-120b  2026-11-17 09:32:05
duration=22.2 error=- attempts=1

IDEA: I-01001 — SEO Meta Completeness Audit  
KNOB: METHOD: (1) Открыть `index.html` в Chrome. (2) В консоли выполнить однострочник:  
```js
(() => {
  const required = [
    {tag:'title',msg:'<title> отсутствует'},
    {meta:'description',msg:'meta[name="description"] отсутствует'},
    {meta:'og:title',msg:'OG‑title отсутствует'},
    {meta:'og:description',msg:'OG‑description отсутствует'},
    {meta:'og:type',msg:'OG‑type отсутствует'},
    {meta:'viewport',msg:'meta[name="viewport"] отсутствует'}
  ];
  const missing = required.filter(r=>{
    if (r.tag) return !document.querySelector(r.tag);
    return !document.head.querySelector(`meta[property="${r.meta}"],meta[name="${r.meta}"]`);
  });
  console.table(missing.map(m=>({Issue:m.msg})));
})();
```  
EFFECT: Быстрая проверка наличия всех критических SEO‑тегов; позволяет сразу увидеть пробелы, повышая вероятность правильного индексации и CTR в поиске.  
RISK: Никаких изменений в коде, только чтение DOM; риск — ложные отрицательные результаты, если теги генерируются динамически (что здесь не так).  
ROLLBACK: Закрыть вкладку/консоль — изменений нет.  
VERIFY: После выполнения в консоли должна отобразиться пустая таблица — все теги присутствуют; любые строки — нужна доработка.  
PRIORITY: 1 — SEO‑теги критичны для видимости в Яндексе и Google, а проверка занимает ≤ 2 минуты.  

IDEA: I-01002 — Визуальный Contrast‑Ratio Audit  
KNOB: METHOD: (1) Открыть страницу в Chrome, включить DevTools → Console. (2) Вставить скрипт, который перебирает все видимые текстовые элементы и вычисляет контраст с фоном через Canvas API:  
```js
(() => {
  const toRGB = c => getComputedStyle(c).color;
  const contrast = (fg,bg)=> {
    const lum = c=>{c = c.slice(4,-1).split(',').map(v=>+v/255); c = c.map(v=>v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4));
      return 0.2126*c[0]+0.7152*c[1]+0.0722*c[2];};
    const L1 = lum(fg)+0.05, L2 = lum(bg)+0.05;
    return L1>L2?L1/L2:L2/L1;
  };
  const bad = [];
  document.querySelectorAll('p, h1, h2, h3, li, a').forEach(el=>{
    const style = getComputedStyle(el);
    if (style.display==='none' || style.visibility==='hidden') return;
    const fg = style.color, bg = style.backgroundColor;
    if (bg==='transparent' || bg==='rgba(0, 0, 0, 0)') return;
    const ratio = contrast(fg,bg);
    if (ratio < 4.5) bad.push({el,ratio:ratio.toFixed(2),fg,bg});
  });
  console.table(bad.map(b=>({Text:b.el.textContent.trim().slice(0,30)+'…',Ratio:b.ratio,FG:b.fg,BG:b.bg})));
})();
```  
EFFECT: Мгновенно выявляет элементы с низким контрастом (< 4.5 : 1), улучшая доступность и соответствие WCAG 2.1, что положительно сказывается на SEO и пользовательском опыте.  
RISK: Скрипт только читает стили; возможны ложные срабатывания для элементов с полупрозрачным фоном.  
ROLLBACK: Перезагрузить страницу — скрипт исчезнет.  
VERIFY: В консоли должна появиться таблица с элементами, у которых контраст ниже порога; отсутствие записей — все ок.  
PRIORITY: 2 — Доступность важна, но без визуальных проблем текущий сайт может уже работать; проверка занимает ~3 минуты.  

IDEA: I-01003 — Critical‑CSS Size Estimator  
KNOB: METHOD: (1) Открыть `index.html` в Chrome. (2) В консоли выполнить скрипт, который измерит общий размер всех стилей, загружаемых в `<head>` (inline + `<link rel="stylesheet">`), и оценит, сколько из них попадает в first‑paint:  
```js
(() => {
  const links = [...document.querySelectorAll('link[rel="stylesheet"]')];
  const inline = document.querySelectorAll('style');
  const fetchSize = url=>fetch(url,{method:'HEAD'}).then(r=>r.headers.get('content-length')||0);
  Promise.all(links.map(l=>fetchSize(l.href))).then(sizes=>{
    const total = sizes.reduce((a,s)=>a+Number(s),0) + [...inline].reduce((a,s)=>a+s.textContent.length,0);
    const critical = Math.min(total, 15000); // условный порог 15 KB
    console.log(`Total CSS size: ${(total/1024).toFixed(1)} KB`);
    console.log(`Estimated critical CSS (≤15 KB): ${(critical/1024).toFixed(1)} KB`);
    if (total>15000) console.warn('Рассмотрите инлайн‑critical‑CSS и отложенную загрузку остальных стилей.');
  });
})();
```  
EFFECT: Быстрая оценка объёма CSS, влияющего на First Contentful Paint; помогает решить, стоит ли внедрять инлайн‑critical‑CSS или `preload`‑link, ускоряя загрузку и повышая конверсию.  
RISK: Оценка приближённая, не учитывает кэш и динамический импорт; может потребоваться подтверждение более точными инструментами.  
ROLLBACK: Никаких изменений в коде; просто закрыть консоль/перезагрузить страницу.  
VERIFY: В консоли отобразятся два числа — общий размер CSS и «критический» размер; если общий > 15 KB — рекомендация к оптимизации.  
PRIORITY: 3 — Оптимизация скорости важна, но без измерений LCP текущий сайт может уже быть приемлем; проверка занимает ~2 минуты.
