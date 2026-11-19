# localhost:8080/ovh/gpt-oss-120b  2026-11-17 04:01:44
duration=61.2 error=- attempts=1

IDEA: SKILL — card-3d-tilt-hover  
KNOB: METHOD: SKILL  
**Name:** `card-3d-tilt-hover`  
**When to apply:** На карточках `.price-card`, `.demo-item` (или любой `.card`) для придания премиального 3‑D‑ощущения при наведении.  
**Steps:**  
1. Добавить к нужным элементам класс `card-3d`.  
2. Подключить CSS‑блок ниже (автоподключение через `<style>` или отдельный файл).  
**SAFE CSS:**  
```css
.card-3d{
  perspective:800px;
  transform-style:preserve-3d;
  transition:transform .35s ease,var(--shadow) .35s ease;
  will-change:transform;
}
.card-3d:hover{
  transform:rotateX(4deg) rotateY(6deg) scale(1.02);
  box-shadow:0 20px 40px rgba(0,0,0,.25);
}
.card-3d::before{
  content:"";
  position:absolute;
  inset:0;
  border-radius:inherit;
  background:linear-gradient(135deg,rgba(255,255,255,.12),transparent);
  pointer-events:none;
}
```  
**SAFE JS:** (необязательно – только если требуется отключить эффект при `prefers-reduced-motion`)  
```js
if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){
  document.querySelectorAll('.card-3d').forEach(el=>el.style.transition='none');
}
```  
EFFECT: Увеличивает восприятие «премиальности» и удерживает внимание на цене/демо‑карточках, повышая CTR на CTA внутри карточек.  
RISK: На старых браузерах без поддержки `transform-style:preserve-3d` эффект будет простым скейлом; визуально не сломает страницу.  
ROLLBACK: `git checkout -- index.html` (или удалить добавленный класс и стили).  
VERIFY: Открыть страницу, наведите курсор на любую `.price-card` – должна появиться лёгкая 3‑D‑наклонка и тень; проверить в Chrome DevTools → Emulation → `prefers-reduced-motion`.  
PRIORITY: 1 – быстрый визуальный апгрейд, высокий ROI без риска.  

---  

IDEA: SKILL — modal-glass-demo  
KNOB: METHOD: SKILL  
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
EFFECT: Позволяет пользователю просматривать демо‑материалы без ухода со страницы, усиливая доверие и время on‑site.  
RISK: Требует небольшого JS‑вставки; если пользователь отключит JS, ссылка просто не откроет модал (не ломает навигацию).  
ROLLBACK: Удалить добавленные `<div id="demoModal">…</div>`, ссылки‑триггеры и стили/скрипт; `git checkout -- index.html`.  
VERIFY: Кликнуть по любой ссылке‑триггеру в секции «Демо‑концепты» – открывается полупрозрачный модальный слой с контентом; закрыть крестом, клавишей Esc.  
PRIORITY: 2 – повышает конверсию, но требует небольших правок HTML/JS.  

---  

IDEA: SKILL — section-fade-in-scroll  
KNOB: METHOD: SKILL  
**Name:** `section-fade-in-scroll`  
**When to apply:** На любые секции `<section>` (кроме `.hero`), где нужен плавный вход при прокрутке, создающий ощущение «живого» лендинга.  
**Steps:**  
1. Добавить к целевым секциям класс `fade-section`.  
2. Подключить CSS‑анимацию и JS‑обработчик ниже.  
**SAFE CSS:**  
```css
.fade-section{
  opacity:0;
  transform:translateY(30px);
  transition:opacity .6s ease-out,transform .6s ease-out;
  will-change:opacity,transform;
}
.fade-section.in-view{
  opacity:1;
  transform:translateY(0);
}
```  
**SAFE JS:**  
```js
const observer=new IntersectionObserver((entries)=>{
  entries.forEach(entry=>{
    if(entry.isIntersecting) entry.target.classList.add('in-view');
  });
},{threshold:0.15});
document.querySelectorAll('.fade-section').forEach(el=>observer.observe(el));
```  
EFFECT: Уменьшает визуальный шум, делает скролл более динамичным, повышает время пребывания и воспринимаемую «премиальность».  
RISK: На устройствах с отключённым JS эффект не будет работать, но секция останется видимой (opacity 0 → будет скрыта). Чтобы избежать, добавить `opacity:1` в базовый стиль как fallback (необязательно).  
ROLLBACK: Удалить добавленные классы и блоки CSS/JS; `git checkout -- index.html`.  
VERIFY: Прокрутить страницу – секции должны плавно появляться; открыть DevTools → Disable JavaScript – секции сразу видимы (fallback).  
PRIORITY: 2 – легко реализуемо, заметный визуальный эффект, умеренный риск без JS.  

---  

IDEA: SKILL — cta-gradient-underline  
KNOB: METHOD: SKILL  
**Name:** `cta-gradient-underline`  
**When to apply:** На все ссылки‑CTA (`.btn-primary`, `.fab-demo`, `.hero a`) для придания им «светящегося» подчеркивания при наведении, усиливающего интерактивность.  
**Steps:**  
1. Добавить к CTA‑элементам класс `gradient-underline`.  
2. Подключить CSS‑блок ниже.  
**SAFE CSS:**  
```css
.gradient-underline{
  position:relative;
  color:inherit;
  text-decoration:none;
}
.gradient-underline::after{
  content:"";
  position:absolute;
  left:0; bottom:-2px;
  width:100%; height:2px;
  background:linear-gradient(90deg,var(--blue),var(--purple));
  transform:scaleX(0);
  transform-origin:left;
  transition:transform .35s ease;
}
.gradient-underline:hover::after,
.gradient-underline:focus-visible::after{
  transform:scaleX(1);
}
.gradient-underline:focus-visible{
  outline:none;
  box-shadow:0 0 0 3px rgba(139,92,246,.3);
}
```  
EFFECT: Делает CTA более заметными, повышает коэффициент клика (CTR) за счёт анимированного градиентного подчеркивания, сохраняет чистый дизайн без лишних изображений.  
RISK: На очень старых браузерах `linear-gradient` в `background` может не поддерживаться; в таком случае подчеркивание будет отсутствовать, но функциональность ссылки сохранится.  
ROLLBACK: Удалить класс `gradient-underline` и CSS‑блок; `git checkout -- index.html`.  
VERIFY: Навести курсор на любую кнопку/ссылку‑CTA – появится плавное градиентное подчеркивание; проверить в Chrome DevTools → Elements, убедиться в наличии `::after`.  
PRIORITY: 3 – небольшое визуальное улучшение, низкий риск, но менее критично, чем 3D‑карточки.
