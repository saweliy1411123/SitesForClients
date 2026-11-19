# localhost:8080/ovh/gpt-oss-120b  2026-11-17 09:07:29
duration=48.0 error=- attempts=1

IDEA: SKILL — glassmorphic‑card‑hover  
KNOB: **Name:** `glassmorphic-card-hover`  
**When to apply:** На любых карточках цены, демо‑концептов или блоках‑шагов (`.price-card`, `.demo-item`, `.step`) для создания премиального «фрост‑гласса» при наведении.  

**SAFE CSS:**  
```css
.glass-card {
  background: rgba(255,255,255,0.08);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255,255,255,0.15);
  border-radius: 12px;
  transition: transform .28s ease, box-shadow .28s ease;
}
.glass-card:hover,
.glass-card:focus-visible {
  transform: translateY(-8px);
  box-shadow: 0 16px 36px rgba(0,0,0,0.18);
}
```
**SAFE JS:** _не требуется_  

EFFECT: Повышает восприятие сайта как «дорогого» за счёт современного стеклянного эффекта, усиливает интерактивность карточек и повышает CTR на цены/демо.  
RISK: Не поддерживается в старых браузерах без `backdrop-filter` (IE, старый Edge) – в них будет обычный фон без размытия.  
ROLLBACK: `git checkout index.html && rm -rf SKILLS/glassmorphic-card-hover.md` (удалить файл‑скилл и откатить изменения в index.improved.html).  
VERIFY: Открыть страницу в Chrome, навести курсор на любую карточку цены – должна появиться плавная подъём‑тень; проверить в режиме «Эмуляция старого браузера» (IE‑11) – эффект исчезнет, но дизайн сохранится.  
PRIORITY: 1 — ключевой визуальный элемент премиального позиционирования, быстрый ROI.  
SKILL: glassmorphic-card-hover  

---  

IDEA: SKILL — subtle‑entrance‑fade‑up  
KNOB: **Name:** `subtle-entrance-fade-up`  
**When to apply:** На всех секционных блоках, которые появляются ниже «hero» (например, `.solution`, `.how`, `.works`, `.pricing`, `.faq`, `.final`).  

**SAFE CSS:**  
```css
.reveal-up {
  opacity:0;
  transform:translateY(24px);
  transition:opacity .6s ease-out, transform .6s ease-out;
}
.reveal-up.visible {
  opacity:1;
  transform:none;
}
```
**SAFE JS:**  
```js
document.addEventListener('DOMContentLoaded',()=>{
  const obs = new IntersectionObserver((entries)=>{ 
    entries.forEach(e=> e.isIntersecting && e.target.classList.add('visible'));
  },{threshold:0.15});
  document.querySelectorAll('.reveal-up').forEach(el=>obs.observe(el));
});
```  

EFFECT: Делает скролл‑появление мягким и «живым», усиливает чувство динамики и удерживает внимание пользователя, что повышает среднее время на странице.  
RISK: При отключённом JavaScript анимации не сработают – элементы останутся скрытыми; добавлен fallback‑класс `visible` в CSS‑правилах, если необходимо, можно добавить `noscript`‑стиль `opacity:1`.  
ROLLBACK: `git checkout index.html && rm -rf SKILLS/subtle-entrance-fade-up.md` (удалить скилл).  
VERIFY: Открыть страницу, прокрутить вниз – блоки должны плавно появляться; открыть DevTools → отключить JS – блоки сразу видимы (проверка fallback).  
PRIORITY: 2 — улучшает UX без риска, легко измеряется в A/B.  
SKILL: subtle-entrance-fade-up  

---  

IDEA: SKILL — neumorphic‑cta‑button  
KNOB: **Name:** `neumorphic-cta-button`  
**When to apply:** На всех ссылках‑кнопках CTA (`.btn-primary`, `.btn-secondary`) для создания мягкого, «поднятого» ощущения, характерного для премиального дизайна.  

**SAFE CSS:**  
```css
.neumo-cta {
  background: var(--bg);
  color: var(--text);
  border-radius: 10px;
  padding: 0.75em 1.5em;
  box-shadow: 6px 6px 12px rgba(0,0,0,0.18),
              -6px -6px 12px rgba(255,255,255,0.12);
  transition: box-shadow .18s ease, transform .18s ease;
}
.neumo-cta:focus-visible,
.neumo-cta:hover {
  box-shadow: 4px 4px 8px rgba(0,0,0,0.12),
              -4px -4px 8px rgba(255,255,255,0.08);
}
.neumo-cta:active {
  transform: translateY(2px);
  box-shadow: inset 4px 4px 8px rgba(0,0,0,0.2),
              inset -4px -4px 8px rgba(255,255,255,0.1);
}
```
**SAFE JS:** _не требуется_  

EFFECT: Придаёт CTA «осязаемость» и повышает конверсию за счёт более заметного, приятного отклика на взаимодействие.  
RISK: На устройствах с низким DPI эффект может выглядеть переэкранным; можно отключить через `@media (prefers-reduced-motion: reduce)`.  
ROLLBACK: `git checkout index.html && rm -rf SKILLS/neumorphic-cta-button.md`.  
VERIFY: Нажать/навести на любую кнопку‑CTA – должна измениться тень и небольшое смещение; проверить в мобильном режиме (touch) – активный стиль срабатывает.  
PRIORITY: 3 — эстетический апгрейд, не критичен, но повышает восприятие качества.  
SKILL: neumorphic-cta-button  

---  

IDEA: SKILL — scroll‑parallax‑3d‑layer  
KNOB: **Name:** `scroll-parallax-3d-layer`  
**When to apply:** На декоративных фоновых элементах в секции `.hero` (например, `.hero-bg`, `.hero-blob`) и в секции `.final` для лёгкого 3‑D параллакса, реагирующего на движение мыши/скролл.  

**SAFE CSS:**  
```css
.parallax-layer {
  position:absolute;
  inset:0;
  transform-style:preserve-3d;
  will-change:transform;
}
```
**SAFE JS:**  
```js
document.addEventListener('mousemove',e=>{
  const layers = document.querySelectorAll('.parallax-layer');
  const {innerWidth:w, innerHeight:h}=window;
  const x = (e.clientX/w - 0.5)*2; // -1 .. 1
  const y = (e.clientY/h - 0.5)*2;
  layers.forEach(el=>{
    const depth = parseFloat(el.dataset.depth)||0.2;
    const tx = x*depth*15;
    const ty = y*depth*15;
    el.style.transform=`translate3d(${tx}px,${ty}px,0)`;
  });
});
```  

EFFECT: Добавляет лёгкую глубину и интерактивность, усиливая премиальный «технологичный» имидж без тяжёлых библиотек.  
RISK: На мобильных устройствах без мыши эффект может быть избыточным; в `@media (hover: none)` отключаем скрипт (проверка `window.matchMedia('(hover: none)').matches`).  
ROLLBACK: `git checkout index.html && rm -rf SKILLS/scroll-parallax-3d-layer.md`.  
VERIFY: Открыть страницу на десктопе, перемещать курсор – фоновые слои должны слегка смещаться; открыть в мобильном эмуляторе – движение не происходит, но фон остаётся.  
PRIORITY: 2 — визуальная «вау‑фактор», но требует небольшого JS, поэтому ставим средний приоритет.  
SKILL: scroll-parallax-3d-layer
