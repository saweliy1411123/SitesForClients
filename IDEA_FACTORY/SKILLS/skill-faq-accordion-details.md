---
name: SKILL — faq-accordion-details
source: localhost:8080/ovh/gpt-oss-120b
round: 111
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — faq-accordion-details

**Name:** `faq-accordion-details`
**When to apply:** На любой лендинг‑странице с секцией FAQ, где требуется улучшить семантику, доступность и анимацию раскрытия ответов.
**Steps:**
1. В секции `#faq` заменить каждый блок `<div class="faq-item">` на `<details class="faq-item"><summary class="faq-question">…</summary><div class="faq-answer">…</div></details>`.
2. Добавить стили для плавного раскрытия/сворачивания и визуального маркера.
3. При желании добавить небольшой скрипт, который закрывает все остальные `<details>` при открытии нового (необязательно, сохраняет чистый HTML).
**SAFE CSS:**
```css
/* faq-accordion-details */
details.faq-item{
border-bottom:1px dashed var(--border);
padding:12px 0;
}
details.faq-item summary{
cursor:pointer;
list-style:none;
font-weight:600;
display:flex;
align-items:center;
gap:8px;
}
details.faq-item summary::-webkit-details-marker{
display:none;
}
details.faq-item summary::after{
content:"▸";
transition:transform .2s;
}
details[open].faq-item summary::after{
transform:rotate(90deg);
}
details.faq-item .faq-answer{
margin-top:8px;
animation:fadeIn .3s ease-out;
}
@keyframes fadeIn{
from{opacity:0;transform:translateY(-4px);}
to{opacity:1;transform:none;}
}
```
**SAFE JS (optional):**
```js
/* faq-accordion-details – закрывать остальные при открытии */
document.querySelectorAll('details.faq-item').forEach(d=>{
d.addEventListener('toggle',()=>{ if(d.open){
document.querySelectorAll('details.faq-item').forEach(o=>{ if(o!==d) o.open=false; });
}});
});
```

## Когда применять
Улучшает доступность (поддержка клавиатуры, ARIA‑поведение), повышает доверие поисковиков (semantic HTML) и делает раскрытие ответов визуально приятным, что может увеличить время на странице и CTR к CTA‑блокам.

## Проверка
Открыть страницу, кликнуть по каждому вопросу – ответы должны плавно открываться/закрываться, а клавиша Tab должна фокусировать заголовки вопросов.
