# localhost:8080/ovh/gpt-oss-120b  2026-11-17 09:43:18
duration=29.1 error=- attempts=1

IDEA: SKILL — scroll-progress-indicator  
KNOB: **Name:** `scroll-progress-indicator`  
**When to apply:** На любой одностраничный лендинг с вертикальной прокруткой, где пользователь проходит более 2‑х экранов контента.  
**Steps:**  
1. В `<body>` сразу после открывающего тега добавить `<div class="scroll-progress" aria-hidden="true"></div>`.  
2. В конец `<body>` добавить скрипт, который слушает событие `scroll`, вычисляет процент прокрутки (`(window.scrollY + window.innerHeight) / document.documentElement.scrollHeight * 100`) и задаёт ширину `.scroll-progress` в % через `style.width`.  
3. При необходимости добавить атрибут `role="progressbar"` и `aria-valuemin="0" aria-valuemax="100"` для доступности.  

**SAFE CSS:**  
```css
.scroll-progress{
  position:fixed;
  top:0;
  left:0;
  height:4px;
  width:0;
  background:var(--blue);
  z-index:9999;
  transition:width .2s ease-out;
}
```

**SAFE JS:**  
```js
(function(){
  const bar=document.querySelector('.scroll-progress');
  if(!bar) return;
  const update=()=>{ 
    const scroll=window.scrollY+window.innerHeight;
    const height=document.documentElement.scrollHeight;
    const pct=Math.min(100,Math.round(scroll/height*100));
    bar.style.width=pct+'%';
    bar.setAttribute('aria-valuenow',pct);
  };
  window.addEventListener('scroll',update);
  update();
})();
```  

EFFECT: Пользователь сразу видит, сколько контента уже просмотрено, повышается вовлечённость и снижается показатель отказов.  
RISK: Добавление небольшого скрипта может конфликтовать с другими глобальными обработчиками scroll; при слишком частом скролле небольшое увеличение нагрузки ≈ 1 ms.  
ROLLBACK: Удалить `<div class="scroll-progress">` и вложенный `<script>`; либо выполнить `git checkout -- index.html` чтобы вернуть оригинал.  
VERIFY: Открыть страницу в браузере, прокрутить вниз – индикатор должен плавно заполняться от 0 % до 100 %; открыть DevTools → Console – ошибок не должно.  
PRIORITY: 2 – быстрый выигрыш в UX без изменения контента, легко тестировать.  
SKILL: scroll-progress-indicator  

---  

IDEA: SKILL — shimmer-placeholder  
KNOB: **Name:** `shimmer-placeholder`  
**When to apply:** На страницах с изображениями, которые загружаются лениво (`loading="lazy"`), особенно при медленном соединении, чтобы уменьшить визуальное «мигание» контента.  
**Steps:**  
1. Обернуть каждое `<img>` в контейнер `<div class="shimmer-wrapper"><img …></div>`.  
2. Добавить атрибут `loading="lazy"` к `<img>` (если его нет).  
3. В CSS задать анимированный градиент‑шимер для `.shimmer-wrapper` и скрыть изображение до полной загрузки (`opacity:0`).  
4. Добавить небольшую JS‑функцию, которая после события `load` у изображения удаляет класс `shimmer-active` у родителя, делая изображение видимым.  

**SAFE CSS:**  
```css
.shimmer-wrapper{
  position:relative;
  overflow:hidden;
  background:#f0f0f0;
}
.shimmer-wrapper::before{
  content:"";
  position:absolute;
  inset:0;
  background:linear-gradient(90deg,
    #f0f0f0 0%,
    #e0e0e0 40%,
    #f0f0f0 80%);
  background-size:200% 100%;
  animation:shimmer 1.5s infinite;
}
.shimmer-wrapper img{
  display:block;
  width:100%;
  height:auto;
  opacity:0;
  transition:opacity .3s ease-in;
}
.shimmer-wrapper.loaded img{
  opacity:1;
}
@keyframes shimmer{
  0%{background-position: -200% 0;}
  100%{background-position: 200% 0;}
}
```  

**SAFE JS:**  
```js
document.querySelectorAll('.shimmer-wrapper img').forEach(img=>{
  img.addEventListener('load',()=> {
    img.parentElement.classList.add('loaded');
  });
});
```  

EFFECT: Пользователь видит плавный шимер‑заполнитель вместо пустого места, улучшая восприятие скорости загрузки и снижая показатель отказов.  
RISK: Требует небольшого изменения HTML‑структуры; если на странице уже есть CSS‑правила, конфликт возможен, однако стили используют уникальные селекторы.  
ROLLBACK: Удалить обёртки `shimmer-wrapper` и связанные CSS/JS‑фрагменты; либо выполнить `git checkout -- index.html`.  
VERIFY: Открыть страницу в медленном режиме (DevTools → Network → Throttling → Slow 3G), убедиться, что до полной загрузки изображения показывается анимированный шимер, после загрузки изображение появляется без мерцаний.  
PRIORITY: 3 – более сложная интеграция, но значительно повышает perceived performance, особенно если в будущем планируется добавить графику.  
SKILL: shimmer-placeholder
