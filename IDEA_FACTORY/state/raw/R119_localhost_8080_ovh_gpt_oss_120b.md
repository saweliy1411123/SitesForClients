# localhost:8080/ovh/gpt-oss-120b  2026-11-17 07:29:22
duration=35.5 error=- attempts=1

IDEA: Hero headline gradient animation  
KNOB: Добавить к `<h1 class="reveal">` CSS‑правило `background: linear-gradient(90deg, #8b5cf6, #34d399, #8b5cf6); -webkit-background-clip: text; color: transparent; animation: hueShift 8s infinite linear;` и `@keyframes hueShift { from {background-position: 0% 0%;} to {background-position: 100% 0%;} }`  
EFFECT: Привлекает внимание к главному офферу, повышает восприятие премиальности и потенциально увеличивает CTR первой CTA.  
RISK: Возможен небольшой рост CLS из‑за изменения размеров текста при загрузке шрифта.  
ROLLBACK: `git checkout -- index.html` (или откатить изменения в `index.improved.html`).  
VERIFY: Открыть страницу в Chrome, включить DevTools → Elements, убедиться, что `<h1>` имеет `background-clip: text` и анимацию работает без мерцания; измерить CLS через Lighthouse (должен оставаться ≤ 0.1).  
PRIORITY: 1 — визуальный «wow‑factor» на первом экране, быстрый ROI.  

---  

IDEA: Parallax hero background layers  
KNOB: Внутри `<header class="hero">` добавить две абсолютные обёртки: `<div class="hero-bg hero-bg‑far"></div>` и `<div class="hero-bg hero-bg‑near"></div>`. В CSS задать `position:absolute; inset:0; background-image:url(...); background-size:cover; transform:translateZ(0);` и `will-change:transform;`. Добавить скрипт‑listener `window.addEventListener('scroll',()=>{ const y=window.scrollY; document.querySelector('.hero-bg-far').style.transform=\`translateY(\${y*0.3}px)\`; document.querySelector('.hero-bg-near').style.transform=\`translateY(\${y*0.6}px)\`; });` (SAFE JS, без throttling).  
EFFECT: Создаёт ощущение глубины, усиливает премиальный имидж и удерживает пользователя в зоне hero‑экран.  
RISK: На слабых устройствах может появиться небольшая задержка скролла (падение FPS).  
ROLLBACK: Удалить только вставленные `<div>` и JS‑блок; `git checkout -- index.html`.  
VERIFY: Прокрутить страницу, убедиться в плавном смещении слоёв; в Chrome DevTools → Performance проверить, что FPS ≥ 55.  
PRIORITY: 2 — повышает восприятие бренда, но требует проверки производительности.  

---  

IDEA: Glassmorphic price‑card  
KNOB: В CSS для селектора `.price-card` добавить `background: rgba(255,255,255,0.12); backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.18); box-shadow: 0 8px 32px rgba(0,0,0,0.25);` и `border-radius: 12px;`; удалить текущий сплошной фон, если он есть.  
EFFECT: Делает блок цены визуально «прозрачным», усиливает премиальный стиль и улучшает контраст с фоном, повышая читаемость.  
RISK: На браузерах без поддержки `backdrop-filter` (IE, старый Edge) эффект будет отсутствовать, но контент останется читаемым.  
ROLLBACK: Откатить изменения в `.price-card` через `git checkout -- index.html`.  
VERIFY: Открыть страницу в Chrome, Safari и Firefox; убедиться, что карточка имеет полупрозрачный фон и размытие; в браузерах без `backdrop-filter` проверять, что фон стал обычным (не ломает дизайн).  
PRIORITY: 2 — визуальная дифференциация цены, низкий риск.  

---  

IDEA: 3D flip price‑card on hover (detail view)  
KNOB: Обернуть содержимое `.price-card` в `<div class="price-card-inner">` с двумя дочерними `<div class="price-card-front">` и `<div class="price-card-back">` (back содержит разбивку цены). В CSS: `.price-card { perspective: 800px; } .price-card-inner { transition: transform 0.6s; transform-style: preserve-3d; } .price-card:hover .price-card-inner { transform: rotateY(180deg); } .price-card-front, .price-card-back { backface-visibility: hidden; position:absolute; inset:0; } .price-card-back { transform: rotateY(180deg); }`  
EFFECT: Позволяет пользователю увидеть детали цены без перегрузки основной карточки, повышая прозрачность оффера и доверие.  
RISK: Добавление вложенной разметки может слегка увеличить размер HTML и потребовать корректировки текущих стилей (например, padding).  
ROLLBACK: Удалить блоки `.price-card-inner`, `.price-card-front`, `.price-card-back` и вернуть оригинальный HTML; `git checkout -- index.html`.  
VERIFY: Навести курсор на цену, убедиться в плавном 3D‑перевороте; проверить, что текст остаётся читаемым; измерить CLS (не должен заметно измениться).  
PRIORITY: 3 — улучшает доверие, но требует более тщательной проверки совместимости.  

---  

IDEA: METHOD: A/B‑тест hero‑copy via URL‑параметр  
KNOB: METHOD: В конец `<body>` добавить скрипт, который читает `?copy=alt` и, если параметр присутствует, заменяет текст внутри `<h1>` и `<p class="sub">` на альтернативные варианты (например, «Ваш бизнес в Яндексе за 48 часов»). Скрипт использует `document.querySelector` и `textContent`.  
EFFECT: Позволяет быстро сравнивать разные формулировки оффера без деплоя, измеряя CTR первой CTA.  
RISK: Требует согласования у владельца о наборе альтернативных копий; при ошибке может оставить пустой текст.  
ROLLBACK: Удалить добавленный скрипт; `git checkout -- index.html`.  
VERIFY: Открыть `index.html?copy=alt` в браузере, убедиться, что заголовок и подзаголовок изменились; проверить, что без параметра копия остаётся оригинальной.  
PRIORITY: 2 — быстрый способ оптимизировать конверсию, низкая стоимость реализации.  

---  

SKILL — glassmorphic-cta-button  
KNOB: **Name:** glassmorphic-cta-button  
**When to apply:** На любой лендинг, где CTA‑кнопки оформлены как ссылки `<a class="btn-primary">`.  
**SAFE CSS:**  
```css
.btn-primary.glassy {
  background: rgba(255,255,255,0.15);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255,255,255,0.25);
  border-radius: 8px;
  color: #fff;
  padding: 0.75rem 1.5rem;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  transition: background 0.3s, transform 0.2s;
}
.btn-primary.glassy:hover,
.btn-primary.glassy:focus-visible {
  background: rgba(255,255,255,0.25);
  transform: translateY(-2px);
}
.btn-primary.glassy .arr {
  transition: transform 0.2s;
}
.btn-primary.glassy:hover .arr {
  transform: translateX(4px);
}
```  
**SAFE JS:** *(необязательно, но добавляет копирование текста при клике)*  
```js
document.querySelectorAll('.btn-primary.glassy').forEach(btn=>{
  btn.addEventListener('click',e=>{
    if(e.shiftKey){ // Shift‑click копирует ссылку в буфер
      navigator.clipboard.writeText(btn.href);
      btn.textContent='Ссылка скопирована!';
    }
  });
});
```  
EFFECT: Делает CTA визуально премиальными, повышает доверие и улучшает конверсию за счёт яркого, но лёгкого эффекта.  
RISK: На браузерах без `backdrop-filter` кнопка будет выглядеть менее «стеклянно», но останется читаемой.  
ROLLBACK: Удалить класс `glassy` из всех CTA‑ссылок и убрать CSS‑файл/блок; `git checkout -- index.html`.  
VERIFY: Добавить класс к одной ссылке, открыть страницу, убедиться в прозрачном фоне и плавном hover‑эффекте; проверить, что в старых браузерах кнопка остаётся обычной.  
PRIORITY: 1 — быстрый визуальный апгрейд, легко измеримый через клики CTA.
