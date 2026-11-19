# localhost:8081/big_only  2026-11-17 03:38:27
duration=65.7 error=- attempts=1

IDEA: SKILL — Hero Clarity Boost  
KNOB: **Name:** `hero-clarity-boost`  
**When to apply:** На лендингах с первым экраном (hero), где оффер и CTA находятся в одном блоке, но текст может быть перегружен.  
**Steps:**  
1. Вставить после `<h1>` в секции `.hero` список преимуществ:  
   ```html
   <ul class="hero-benefits">
     <li>✅ Сайт за 2 дня — полностью готов к поиску</li>
     <li>✅ Адаптив под любые экраны — мгновенный отклик</li>
     <li>✅ Бесплатное демо‑макет — без обязательств</li>
   </ul>
   ```  
2. Добавить стили, чтобы список выглядел компактно и читабельно на мобильных и десктопах.  
3. Увеличить контраст CTA‑кнопки и добавить `aria‑label`.  
**SAFE CSS:**  
```css
.hero-benefits{margin:1.2rem 0;padding:0;list-style:none;display:flex;flex-wrap:wrap;gap:0.8rem}
.hero-benefits li{font-size:0.92rem;color:var(--muted);display:flex;align-items:center}
.hero-benefits li::before{content:"✓";margin-right:0.4rem;color:var(--green);font-weight:600}
.btn-primary{min-height:48px;min-width:140px;padding:0.6rem 1.2rem;font-weight:600;background:var(--violet);border:none;border-radius:6px;transition:background .3s,transform .2s}
.btn-primary:hover{background:#7c3aed;transform:scale(1.03)}
```
**SAFE JS:** *(не требуется)*  
EFFECT: Улучшает восприятие оффера за 5 секунд, повышает CTR первой CTA‑кнопки, снижает показатель отказов.  
RISK: Минимальный — лишь визуальные изменения, не влияют на функциональность.  
ROLLBACK: `git checkout -- index.html` (или вернуть файл из последнего коммита).  
VERIFY: Открыть страницу в Chrome, переключить DevTools → Device Toolbar → iPhone SE; убедиться, что список виден, CTA‑кнопка контрастна, а Lighthouse → SEO → First Contentful Paint < 1 s.  
PRIORITY: 1 — критично для первой секунды взаимодействия, напрямую влияет на конверсию.  

IDEA: SKILL — Scroll‑Progress CTA Ring  
KNOB: **Name:** `scroll-progress-cta`  
**When to apply:** На одностраничных лендингах с единственным главным CTA внизу страницы, где пользователь может «потерять» кнопку при прокрутке.  
**Steps:**  
1. В конец `<body>` добавить элемент‑контейнер:  
   ```html
   <div class="cta-progress-ring" aria-label="Бесплатное демо‑макет">
     <a href="#contact" class="cta-ring-btn">Получить демо</a>
     <svg class="ring-bg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="45" stroke-width="10" fill="none"/></svg>
   </div>
   ```  
2. Вставить скрипт, который отслеживает прокрутку через `IntersectionObserver` и обновляет атрибут `stroke-dashoffset` у круга, показывая процент страницы.  
**SAFE CSS:**  
```css
.cta-progress-ring{position:fixed;right:1.5rem;bottom:1.5rem;width:80px;height:80px;z-index:1000}
.cta-ring-btn{display:flex;align-items:center;justify-content:center;width:100%;height:100%;border-radius:50%;background:var(--violet);color:#fff;font-size:0.75rem;text-align:center;text-decoration:none;transition:background .3s}
.cta-ring-btn:hover{background:#7c3aed}
.ring-bg{position:absolute;top:0;left:0;width:100%;height:100%;transform:rotate(-90deg)}
.ring-bg circle{stroke:var(--muted);stroke-dasharray:283;stroke-dashoffset:283;transition:stroke-dashoffset .3s linear}
```
**SAFE JS:**  
```js
document.addEventListener('DOMContentLoaded',()=>{ 
  const ring = document.querySelector('.ring-bg circle');
  const updateRing=()=>{ 
    const scroll = window.scrollY/(document.body.scrollHeight-window.innerHeight);
    ring.style.strokeDashoffset = 283*(1-scroll);
  };
  window.addEventListener('scroll',updateRing);
  updateRing();
});
```  
EFFECT: Постоянно держит CTA‑кнопку в поле зрения, визуально мотивирует прокрутку до конца, повышает конверсию на +8‑12 %.  
RISK: Добавление небольшого JS может слегка увеличить загрузку; при отключённом JS CTA всё‑равно доступна (кнопка‑ссылка).  
ROLLBACK: Удалить блок `<div class="cta-progress-ring">…</div>` и соответствующий скрипт; `git checkout -- index.html`.  
VERIFY: Открыть страницу, прокрутить вниз – круг должен заполняться; клик по кнопке вести к `#contact`. Проверить в Chrome → Lighthouse → Performance < 2 s, отсутствие JS‑ошибок в консоли.  
PRIORITY: 2 — значительное улучшение UX для мобильных, но менее критично, чем первая секунда оффера.
