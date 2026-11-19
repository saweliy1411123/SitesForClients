---
name: Cost‑loss counter with ARIA‑live в секции «Боль»
source: localhost:8081/big_only
round: 97
status: proposed
portable: true
tags: [static-landing, portable]
---

# Cost‑loss counter with ARIA‑live в секции «Боль»

SKILL:
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

## Когда применять
Пользователь сразу видит конкретный ущерб, усиливается чувство срочности → рост конверсии в CTA.

## Проверка
Открыть страницу, убедиться, что блок появляется под секцией боли, число растёт от 0 до целевого, а атрибут `aria-live="polite"` присутствует в DOM.
