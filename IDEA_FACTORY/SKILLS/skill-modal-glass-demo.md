---
name: SKILL — modal-glass-demo
source: localhost:8080/ovh/gpt-oss-120b
round: 49
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — modal-glass-demo

METHOD: SKILL
**Name:** `modal-glass-demo`
**When to apply:** Для показа PDF‑кейс‑стади или больших изображений из секции «Демо‑концепты», заменяя простую ссылку на лёгкий премиальный модальный просмотр.
**Steps:**
1. Вставить в конец `<body>` разметку модального окна (скрытый `<div id="demoModal">`).
2. Добавить к каждому ссылочному элементу‑триггеру атрибут `data-modal="#demoModal"` и класс `modal-trigger`.
3. Подключить CSS‑блок и JS‑скрипт ниже.
**SAFE CSS:**
```css
#demoModal{
position:fixed; inset:0; display:none; align-items:center; justify-content:center;
background:rgba(0,0,0,.6);
backdrop-filter:blur(8px);
z-index:1000;
}
#demoModal.show{display:flex;}
.modal-content{
background:#1a1a1a;
border-radius:12px;
padding:24px;
max-width:90vw; max-height:85vh;
box-shadow:0 12px 30px rgba(0,0,0,.4);
overflow:auto;
}
.modal-close{
position:absolute; top:12px; right:12px;
background:transparent; border:none; color:#fff; font-size:1.5rem;
cursor:pointer;
}
```
**SAFE JS:**
```js
document.addEventListener('click', e=>{
const t=e.target.closest('.modal-trigger');
if(t){
e.preventDefault();
const modal=document.querySelector(t.dataset.modal);
modal.classList.add('show');
}
if(e.target.matches('.modal-close')||e.target===document.getElementById('demoModal')){
document.getElementById('demoModal').classList.remove('show');
}
});
document.addEventListener('keydown', e=>{
if(e.key==='Escape') document.getElementById('demoModal').classList.remove('show');
});
```

## Когда применять
Позволяет пользователю просматривать демо‑материалы без ухода со страницы, усиливая доверие и время on‑site.

## Проверка
Кликнуть по любой ссылке‑триггеру в секции «Демо‑концепты» – открывается полупрозрачный модальный слой с контентом; закрыть крестом, клавишей Esc.
