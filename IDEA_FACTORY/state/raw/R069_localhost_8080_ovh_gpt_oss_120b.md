# localhost:8080/ovh/gpt-oss-120b  2026-11-17 05:02:15
duration=43.2 error=- attempts=1

IDEA: SKILL — focus-visible-enhancer  
SKILL: focus-visible-enhancer  
KNOB: **Name:** `focus-visible-enhancer`  
**When to apply:** На любом статическом лендинге, где есть интерактивные элементы (`<a>`, `<button>`, элементы с `role="button"`), но отсутствуют чёткие визуальные индикаторы фокуса – для соответствия WCAG 2.1 AA.  
**Steps:**  
1. Вставить в глобальный CSS блок `:focus-visible`‑стилей (см. `SAFE CSS`).  
2. Добавить лёгкий полифил JS, который при первом нажатии клавиши Tab добавляет класс `js-keyboard` к `<html>` и переключает `:focus-visible`‑обработку в браузерах без поддержки.  
3. При клике мышью/касании удалить класс `js-keyboard`, чтобы вернуть привычные стили hover.  
4. Проверить, что существующие кастомные `:focus`‑стили не конфликтуют (при необходимости уточнить селекторы).  

**SAFE CSS:**  
```css
/* focus-visible‑enhancer */
html.js-keyboard a:focus-visible,
html.js-keyboard button:focus-visible,
html.js-keyboard [role="button"]:focus-visible,
html.js-keyboard .btn-primary:focus-visible {
  outline: 2px solid var(--blue);
  outline-offset: 2px;
  box-shadow: 0 0 0 3px rgba(139,92,246,.3);
}
```

**SAFE JS:**  
```js
/* focus-visible‑enhancer polyfill */
(function(){
  const onKeyDown = e=>{ if(e.key==="Tab"){ document.documentElement.classList.add('js-keyboard'); } };
  const onMouseDown = ()=>{ document.documentElement.classList.remove('js-keyboard'); };
  window.addEventListener('keydown', onKeyDown, {once:true});
  window.addEventListener('mousedown', onMouseDown);
  window.addEventListener('touchstart', onMouseDown);
})();
```  

EFFECT: Улучшает доступность – пользователи клавиатуры сразу видят, какой элемент активен; повышает соответствие WCAG 2.1 AA, что может положительно сказаться на SEO и доверии.  
RISK: Возможен конфликт с уже существующими кастомными `:focus`‑стилями; в редких случаях браузеры без `:focus-visible` могут отобразить двойной outline.  
ROLLBACK: `git checkout index.improved.html` или удалить добавленные блоки CSS/JS из `index.improved.html`.  
VERIFY: Открыть страницу, нажать Tab — должен появиться синий outline на первой ссылке/кнопке; переключить на мышь — outline исчезает. Проверить в Chrome + Firefox.  
PRIORITY: 2 – важно для доступности и соответствия требованиям, но не критично для первой конверсии.  

---  

IDEA: SKILL — bg-lazyload-intersection  
SKILL: bg-lazyload-intersection  
KNOB: **Name:** `bg-lazyload-intersection`  
**When to apply:** На лендингах, где крупные блоки используют CSS‑фон (hero‑секция, разделы с изображениями), и требуется снизить CLS и LCP без изменения HTML‑структуры.  
**Steps:**  
1. Для каждого элемента с `background-image` заменить URL на атрибут `data-bg="url(...)"` и задать временный `background-color` (или прозрачный).  
2. Добавить в конец `<body>` скрипт‑наблюдатель (IntersectionObserver), который при появлении элемента в зоне видимости устанавливает `style.backgroundImage = 'url(...)'`.  
3. При загрузке добавить класс `.bg-loaded` для возможных анимаций fade‑in.  
4. При необходимости добавить fallback‑скрипт для старых браузеров (проверка `IntersectionObserver` и загрузка сразу).  

**SAFE CSS:**  
```css
/* bg-lazyload‑intersection */
[data-bg]{
  background-image:none;
  background-size:cover;
  background-position:center;
}
[data-bg].bg-loaded{
  transition:opacity .4s ease;
  opacity:1;
}
```

**SAFE JS:**  
```js
/* bg-lazyload‑intersection */
(function(){
  const lazyBgs = document.querySelectorAll('[data-bg]');
  if(!('IntersectionObserver' in window)){
    lazyBgs.forEach(el=>el.style.backgroundImage=`url(${el.dataset.bg})`);
    return;
  }
  const onIntersect = (entries,obs)=>{
    entries.forEach(entry=>{
      if(entry.isIntersecting){
        const el=entry.target;
        el.style.backgroundImage=`url(${el.dataset.bg})`;
        el.classList.add('bg-loaded');
        obs.unobserve(el);
      }
    });
  };
  const io=new IntersectionObserver(onIntersect,{rootMargin:'200px'});
  lazyBgs.forEach(el=>io.observe(el));
})();
```  

EFFECT: Сокращает объём загружаемых ресурсов при первом рендере – ускоряет First Contentful Paint и уменьшает Cumulative Layout Shift, что положительно влияет на Core Web Vitals и конверсию.  
RISK: При отключённом JavaScript фон может не загрузиться; требуется fallback‑логика (встроена). Возможна небольшая задержка появления фоновых изображений при медленном скролле.  
ROLLBACK: Удалить атрибуты `data-bg` и вернуть оригинальные `background-image` в CSS/HTML; либо откатить `index.improved.html` через `git checkout`.  
VERIFY: Открыть страницу в DevTools → Network, включить «Disable cache», перезагрузить; убедиться, что крупные фоновые изображения не запрашиваются сразу, а только после прокрутки к их секции. Проверить визуально, что фон появляется без рывков.  
PRIORITY: 1 – прямое влияние на скорость загрузки, а значит на пользовательский опыт и SEO; быстрый выигрыш без серверных изменений.
