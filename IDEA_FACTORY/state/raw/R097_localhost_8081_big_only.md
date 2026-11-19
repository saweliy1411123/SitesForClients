# localhost:8081/big_only  2026-11-17 06:25:23
duration=80.7 error=- attempts=1

IDEA: Cost‑loss counter with ARIA‑live в секции «Боль»  
KNOB: SKILL:  
**Name:** `cost-loss-counter`  
**When to apply:** На любой странице, где в блоке боли нужно визуализировать финансовый ущерб от отсутствия сайта.  
**Steps:**  
1. В нужном месте (после описания боли) добавить HTML‑блок:  
   ```html
   <div class="cost-counter" aria-live="polite">
     Потеря потенциальных клиентов: <span>0</span>
   </div>
   ```  
2. В секцию `<style>` добавить безопасный CSS (SAFE CSS).  
3. В конец `<body>` добавить безопасный JS (SAFE JS), который будет плавно увеличивать число до целевого значения.  
**SAFE CSS:**  
```css
.cost-counter{
  margin-top:1rem;
  font-size:1.2rem;
  color:var(--muted);
}
```
**SAFE JS:**  
```js
(function(){
  const el=document.querySelector('.cost-counter span');
  if(!el) return;
  let current=0;
  const target=120;               // пример: 120 потенциальных клиентов в месяц
  const step=Math.ceil(target/100);
  const interval=setInterval(()=>{
    current+=step;
    if(current>=target){
      current=target;
      clearInterval(interval);
    }
    el.textContent=current;
  },200);
})();
```  
EFFECT: Пользователь сразу видит конкретный ущерб, усиливается чувство срочности → рост конверсии в CTA.  
RISK: Минимальное влияние на производительность (мало‑нагрузочный скрипт).  
ROLLBACK: `git checkout -- index.html` (или откатить отдельный коммит, если применялся).  
VERIFY: Открыть страницу, убедиться, что блок появляется под секцией боли, число растёт от 0 до целевого, а атрибут `aria-live="polite"` присутствует в DOM.  
PRIORITY: 2 — умеренный эффект на конверсию, быстрый и безопасный к внедрению.  

IDEA: Переключатель темы (light / dark) через CSS‑переменные  
KNOB: SKILL:  
**Name:** `theme-switcher-css-variable`  
**When to apply:** На любой статический лендинг, где уже реализована поддержка светлой и тёмной темы (см. `@media (prefers-color-scheme: dark)`), но нужен ручной пользовательский переключатель.  
**Steps:**  
1. В `<header>` (или рядом с навигацией) добавить кнопку‑переключатель:  
   ```html
   <button class="theme-toggle" aria-label="Переключить тему">🌓</button>
   ```  
2. В `<style>` объявить набор CSS‑переменных для обеих тем и правило, которое их применяет в зависимости от атрибута `data-theme` у `<html>`.  
3. В конец `<body>` добавить небольшой скрипт, меняющий атрибут `data-theme` при клике.  
**SAFE CSS:**  
```css
:root{
  --bg:#fff;
  --text:#0a0a0f;
  --accent:#8b5cf6;
}
[data-theme="dark"]{
  --bg:#111;
  --text:#e8eaf2;
  --accent:#c084fc;
}
body{
  background:var(--bg);
  color:var(--text);
}
.theme-toggle{
  background:none;
  border:none;
  cursor:pointer;
  font-size:1.4rem;
  padding:0.4rem;
}
```
**SAFE JS:**  
```js
(function(){
  const btn=document.querySelector('.theme-toggle');
  if(!btn) return;
  btn.addEventListener('click',()=>{
    const html=document.documentElement;
    const cur=html.getAttribute('data-theme')||'light';
    html.setAttribute('data-theme', cur==='dark'?'light':'dark');
  });
})();
```  
EFFECT: Пользователь может явно выбрать предпочтительную цветовую схему, повышается удобство и удовлетворённость → потенциальный рост времени на сайте и SEO‑оценки (повышенный показатель Core Web Vitals).  
RISK: Возможен конфликт с уже существующим `prefers-color-scheme`‑медиа‑правилом, но при правильном порядке правил конфликт минимален.  
ROLLBACK: Удалить добавленную кнопку, CSS‑правила и JS‑скрипт; либо выполнить `git checkout -- index.html`.  
VERIFY: Открыть страницу, кликнуть кнопку – фон и цвета текста должны переключаться между светлой и тёмной схемой; проверить, что в `<html>` меняется атрибут `data-theme`.  
PRIORITY: 1 — высокий эффект на UX и SEO, небольшие затраты, легко тестируемо.
