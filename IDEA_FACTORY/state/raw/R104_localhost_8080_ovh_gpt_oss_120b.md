# localhost:8080/ovh/gpt-oss-120b  2026-11-17 06:47:04
duration=32.1 error=- attempts=1

IDEA: SKILL — prefers-reduced-motion-disable  
KNOB: **Name:** prefers-reduced-motion-disable  
**When to apply:** На любом статическом лендинге, где присутствуют CSS‑анимации (переходы, keyframes, scroll‑reveal).  
**Steps:**  
1. Добавить в корневой `:root` переменную `--anim-duration` со значением `1s`.  
2. Везде, где используется `animation-duration` или `transition-duration`, заменить фиксированные значения на `var(--anim-duration)`.  
3. Добавить медиазапрос `@media (prefers-reduced-motion: reduce)` — устанавливающий `--anim-duration: 0s;` и `animation-name: none;`.  
4. (Опционально) добавить класс `.no-anim` для элементов, где анимация критична, и переопределять её вручную.  

**SAFE CSS:**  
```css
:root{--anim-duration:1s}
*{transition-duration:var(--anim-duration)!important;
  animation-duration:var(--anim-duration)!important}
@media (prefers-reduced-motion:reduce){
  :root{--anim-duration:0s}
  *{animation:none!important;
    transition:none!important}
}
```

**SAFE JS:** (не требуется)  

EFFECT: Пользователи, включившие «prefers‑reduced‑motion», не увидят анимаций → повышается доступность и соответствие WCAG 2.1 AA/AAA.  

RISK: При полном отключении анимаций некоторые визуальные подсказки могут исчезнуть, но это безопасно для большинства элементов.  

ROLLBACK: `git checkout -- index.html` или удалить добавленные строки CSS из файла.  

VERIFY: В Chrome DevTools включить имитацию «prefers‑reduced‑motion» (Settings → Rendering → Emulate CSS media) и убедиться, что все анимации и переходы прекращаются без ошибок.  

PRIORITY: 1 – критически важно для доступности и SEO‑рейтингов (Google учитывает доступность).  

SKILL: prefers-reduced-motion-disable  

---  

IDEA: SKILL — lazy-bg-image  
KNOB: **Name:** lazy-bg-image  
**When to apply:** На лендингах, где крупные фоновые изображения задаются через `background-image` (например, hero‑секция, демо‑карты).  
**Steps:**  
1. В HTML добавить класс `lazy-bg` к элементам с отложенной загрузкой и атрибут `data-bg="url(...)"`.  
2. В CSS задать базовый цвет/градиент‑заполнитель и `background-size: cover; background-position: center;`.  
3. В JS создать `IntersectionObserver`, который при появлении элемента в зоне видимости задаёт `element.style.backgroundImage = 'url(' + element.dataset.bg + ')'`.  
4. Добавить полифилл для старых браузеров (optional).  

**SAFE CSS:**  
```css
.lazy-bg{
  background-color:#f3f4f6;/*fallback*/
  background-size:cover;
  background-position:center;
  transition:background-image .3s ease-in-out;
}
```

**SAFE JS:**  
```js
document.addEventListener('DOMContentLoaded',()=>{
  const lazyEls=document.querySelectorAll('.lazy-bg[data-bg]');
  if('IntersectionObserver' in window){
    const obs=new IntersectionObserver((entries,ob)=>{entries.forEach(e=>{
      if(e.isIntersecting){
        const el=e.target;
        el.style.backgroundImage=`url(${el.dataset.bg})`;
        ob.unobserve(el);
      }
    });});
    lazyEls.forEach(el=>obs.observe(el));
  }else{
    // fallback: load immediately
    lazyEls.forEach(el=>el.style.backgroundImage=`url(${el.dataset.bg})`);
  }
});
```

EFFECT: Отложенная загрузка тяжёлых фоновых изображений уменьшает LCP и CLS, ускоряя первую отрисовку и экономя трафик мобильных пользователей.  

RISK: При отключённом JavaScript фон может не появиться – нужен нейтральный fallback‑цвет, который уже указан.  

ROLLBACK: Удалить добавленный скрипт и CSS‑правила; либо выполнить `git checkout -- index.html`.  

VERIFY: Открыть страницу в Chrome, открыть Network‑панель, включить «Disable JavaScript», убедиться, что фон‑цвет виден; затем включить JS, прокрутить страницу, убедиться, что запросы к изображениям происходят только после появления соответствующего блока.  

PRIORITY: 2 – значительное улучшение скорости и метрик Core Web Vitals, но не критично для контент‑понимания.  

SKILL: lazy-bg-image
