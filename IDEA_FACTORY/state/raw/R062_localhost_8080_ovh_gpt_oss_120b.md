# localhost:8080/ovh/gpt-oss-120b  2026-11-17 04:40:54
duration=31.0 error=- attempts=1

IDEA: SKILL — Fluid Typography with CSS `clamp()`
KNOB: METHOD:
**Name:** fluid-typography-clamp  
**When to apply:** На любом статическом лендинге, где в CSS заданы фиксированные `font-size` / `line-height`.  
**Steps:**  
1. В `<head>` добавить корневые переменные `--fs-min` и `--fs-max` для каждого типографического уровня (h1 – h6, p, .hero‑note).  
2. Заменить каждое фиксированное `font-size: XXpx;` на  
   ```css
   font-size: clamp(var(--fs-min), 1.5vw, var(--fs-max));
   ```  
3. При необходимости задать `line-height` через `clamp()` аналогично.  
4. Тестировать на разных ширинах, скорректировать min/max‑значения.  

SAFE CSS:
```css
:root{
  --fs-h1-min:2.5rem; --fs-h1-max:4rem;
  --fs-h2-min:2rem;   --fs-h2-max:3rem;
  --fs-h3-min:1.5rem; --fs-h3-max:2.25rem;
  --fs-p-min:1rem;    --fs-p-max:1.25rem;
}
h1{font-size:clamp(var(--fs-h1-min),5vw,var(--fs-h1-max));}
h2{font-size:clamp(var(--fs-h2-min),4vw,var(--fs-h2-max));}
h3{font-size:clamp(var(--fs-h3-min),3vw,var(--fs-h3-max));}
p, .hero-note{font-size:clamp(var(--fs-p-min),2.5vw,var(--fs-p-max));}
```

SAFE JS: *(нет)*
EFFECT: Текст плавно подстраивается под ширину экрана → лучшая читаемость, снижается CLS, повышается Core Web Vitals и SEO.  
RISK: Неправильно подобранные min/max могут исказить дизайн на экстремальных ширинах.  
ROLLBACK: `git checkout -- index.html` или удалить добавленные CSS‑правила и вернуть оригинальные `font-size`‑значения.  
VERIFY: Открыть страницу, включить DevTools → «Responsive Design Mode», менять ширину от 320 px до 1920 px – проверяется, что размер текста меняется плавно и остаётся в заданных границах; проверить метрику CLS (должна оставаться 0).  
PRIORITY: 2 – высокий UX‑эффект за небольшие правки, улучшает SEO и конверсию.  
SKILL: fluid-typography-clamp



IDEA: SKILL — Low‑Quality Image Placeholder (LQIP) для фоновых изображений
KNOB: METHOD:
**Name:** lqip-bg-image  
**When to apply:** На секциях с крупными фоновыми изображениями (hero, демо‑карточки), где важна первая визуальная реакция.  
**Steps:**  
1. Сгенерировать небольшую (≈10 × 10 px) версию фонового изображения, закодировать её в base64.  
2. В HTML заменить `style="background-image:url('hero.jpg')"` на атрибут `data-bg="hero.jpg"` и добавить класс `bg-lqip`.  
3. Добавить в CSS псевдо‑элемент `::before`, который будет показывать base64‑placeholder с `filter: blur(12px)` и `scale(1.05)`.  
4. Добавить небольшой скрипт, который создаёт `Image()`, загружает оригинал из `data-bg` и после `load` заменяет `background-image` у элемента, убирая `::before`.  

SAFE CSS:
```css
.bg-lqip{
  position:relative;
  overflow:hidden;
}
.bg-lqip::before{
  content:"";
  position:absolute;
  inset:0;
  background-image:url("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD…"); /* tiny placeholder */
  background-size:cover;
  background-position:center;
  filter:blur(12px);
  transform:scale(1.05);
  transition:opacity .3s ease;
}
.bg-lqip.loaded::before{opacity:0;pointer-events:none;}
```

SAFE JS:
```js
document.querySelectorAll('.bg-lqip').forEach(el=>{
  const img = new Image();
  img.src = el.dataset.bg;
  img.onload = ()=>{
    el.style.backgroundImage = `url(${el.dataset.bg})`;
    el.classList.add('loaded');
  };
});
```

EFFECT: Пользователь видит быстро загружающийся размазанный плейсхолдер, затем плавно появляется чёткое изображение → улучшение FCP/CLS, повышается восприятие скорости.  
RISK: Требует генерации base64‑placeholder; если забыть добавить класс `bg-lqip`, изображение может не загрузиться.  
ROLLBACK: Удалить добавленные атрибуты `data-bg`, класс `bg-lqip`, CSS‑правила и JS‑блок; вернуть оригинальный `background-image`.  
VERIFY: Включить DevTools → Network → Throttle → Slow 3G, открыть страницу и убедиться, что сначала появляется размытый placeholder, затем заменяется на оригинал без «мигания»; измерить FCP (должен снизиться).  
PRIORITY: 1 – критичный фактор первой визуальной реакции, особенно на мобильных, и почти без кода.  
SKILL: lqip-bg-image
