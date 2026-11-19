# localhost:8081/big_only  2026-11-17 07:49:42
duration=22.7 error=- attempts=2

IDEA: 3D‑tilt hero‑section on mouse move  
KNOB: METHOD: add a tiny script that listens to `mousemove` on the `.hero` container and sets `style.transform = perspective(1000px) rotateX(${(y/height-0.5)*10}deg) rotateY(${(x/width-0.5)*10}deg)`; add CSS `transition: transform .2s ease-out; will-change: transform;` to `.hero`.  
EFFECT: создаёт премиальный интерактивный эффект, увеличивает время пребывания и воспринимаемую ценность сайта.  
RISK: небольшое падение FPS на слабых устройствах, возможный дискомфорт у чувствительных к движению пользователей.  
ROLLBACK: удалить добавленный `<script>` и CSS‑правило; `git checkout index.html` откатит изменения.  
VERIFY: открыть страницу в Chrome, перемещать курсор по hero‑секции, убедиться в плавном наклоне; в DevTools проверить FPS > 30.  
PRIORITY: 1 – высокий, потому что влияет на первое впечатление и конверсию.  

---  

IDEA: Анимированная градиентная рамка у CTA‑кнопок  
KNOB: в CSS для `.btn-primary` добавить псевдо‑элемент `::before` с `content:''; position:absolute; inset:0; border-radius:inherit; padding:2px; background:linear-gradient(45deg,#8b5cf6,#34d399,#60a5fa); background-size:200% 200%; animation:gradientBorder 4s linear infinite;` и `pointer-events:none;`; установить `position:relative; overflow:hidden;`.  
EFFECT: привлекает внимание к кнопкам‑призывам, повышает CTR без изменения текста.  
RISK: небольшое увеличение CSS‑файла; при слишком низком контрасте может ухудшить читаемость (проверить).  
ROLLBACK: удалить блок `::before` и `@keyframes gradientBorder`; `git checkout index.html`.  
VERIFY: навести курсор на кнопку, увидеть плавно меняющуюся границу; кликнуть – действие не нарушено.  
PRIORITY: 2 – средний, улучшает конверсию при небольших затратах.  

---  

IDEA: Ленивая загрузка фонового изображения hero с LQIP‑заполнителем  
KNOB: заменить текущий CSS‑фон hero на `<img class="hero-bg" loading="lazy" src="data:image/webp;base64,..." data-src="hero-high.webp" alt="">`; добавить небольшой JS, который при `load` заменяет `src` на `data-src` и добавляет класс `loaded` для плавного перехода (`opacity`‑анимация).  
EFFECT: сокращает размер первоначального HTML/CSS, ускоряет LCP → быстрее первая отрисовка, лучше для мобильных пользователей.  
RISK: если JS отключён, пользователь увидит только размытый placeholder; требуется задать фиксированную высоту, чтобы избежать CLS.  
ROLLBACK: вернуть прежний CSS‑фон; удалить `<img>` и скрипт; `git checkout index.html`.  
VERIFY: включить throttling = Slow 3G в DevTools, измерить LCP до и после; убедиться в отсутствии смещения контента.  
PRIORITY: 1 – высокий, напрямую влияет на Core Web Vitals и SEO.  

---  

IDEA: BreadcrumbList JSON‑LD для улучшения SEO  
KNOB: вставить в `<head>` перед закрывающим `</head>` скрипт типа `application/ld+json` с объектом `{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Главная","item":"https://example.com/"},{"@type":"ListItem","position":2,"name":"Услуги","item":"https://example.com/#price"},{"@type":"ListItem","position":3,"name":"FAQ","item":"https://example.com/#faq"}]}`.  
EFFECT: повышает шанс появления в результатах поиска в виде «хлебных крошек», улучшает видимость и кликабельность сниппета.  
RISK: требуется поддерживать актуальность URL‑ов; неправильные ссылки могут вызвать предупреждения в инструментах Google.  
ROLLBACK: удалить `<script type="application/ld+json">`‑блок; `git checkout index.html`.  
VERIFY: запустить Google Rich Results Test, убедиться в отсутствии ошибок и корректном отображении BreadcrumbList.  
PRIORITY: 2 – средний, SEO‑выгода без влияния на UI.  

---  

IDEA: SKILL — gradient‑focus‑ring (градиентный кольцевой контур фокуса)  
KNOB: **Name:** `gradient-focus-ring`  
**When to apply:** На любой странице с интерактивными элементами (`a`, `.btn-primary`, `summary`) где нужен яркий, но лёгкий визуальный индикатор фокуса.  
**SAFE CSS:**  
```css
:focus-visible {
  outline: none;
  position: relative;
}
:focus-visible::after {
  content: '';
  position: absolute;
  inset: -4px;
  border-radius: 6px;
  background: conic-gradient(from 90deg, var(--grad) 0%, transparent 120deg);
  animation: focusRingSpin 1.2s linear infinite;
  mask: radial-gradient(circle, white 70%, transparent);
}
@keyframes focusRingSpin {
  to { transform: rotate(360deg); }
}
```  
**SAFE JS:** (необязательно)  
```js
// optional: add class for browsers without :focus-visible support
document.querySelectorAll('a, .btn-primary, summary').forEach(el=>{
  el.addEventListener('focus',()=>el.classList.add('focus-visible'));
  el.addEventListener('blur',()=>el.classList.remove('focus-visible'));
});
```  
EFFECT: улучшает доступность, делая фокус явно видимым, одновременно подчёркивая премиальный дизайн.  
RISK: небольшое увеличение CSS‑файла; в старых браузерах без `:focus-visible` может не сработать (JS‑fallback покрывает).  
ROLLBACK: удалить файл/блок `gradient-focus-ring.css` и JS‑скрипт; `git checkout index.html`.  
VERIFY: перейти по клавише Tab к любой ссылке/кнопке, увидеть анимированный градиентный кольцевой контур; убедиться, что он исчезает при потере фокуса.  
PRIORITY: 3 – низкий, но повышает A11Y и воспринимаемую «премиальность».
