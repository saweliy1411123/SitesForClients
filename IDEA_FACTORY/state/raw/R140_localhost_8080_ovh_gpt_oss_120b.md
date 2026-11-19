# localhost:8080/ovh/gpt-oss-120b  2026-11-17 08:28:21
duration=38.1 error=- attempts=1

IDEA: SKILL — glassmorphic‑sticky‑header  
KNOB: **Name:** `glassmorphic-sticky-header`  
**When to apply:** На любой одностраничный лендинг, где в шапке находятся ссылки‑якоря и нужен премиальный, «прозрачный» вид без потери читаемости.  
**Steps:**  
1. Вставить сразу после `<body>` элемент `<nav class="glass-header" aria-label="Главное меню">…</nav>` (скопировать существующий блок навигации).  
2. Добавить CSS‑правила (см. ниже) для фиксированного позиционирования, backdrop‑filter и плавного перехода opacity.  
3. Добавить небольшой скрипт, который при скролле > 50 px добавляет/убирает класс `scrolled`.  
**SAFE CSS:**  
```css
.glass-header{
  position:fixed;
  inset-inline:0;
  top:0;
  height:64px;
  display:flex;
  align-items:center;
  justify-content:center;
  backdrop-filter:blur(12px);
  background:rgba(255,255,255,0.12);
  border-bottom:1px solid rgba(255,255,255,0.15);
  transition:background .3s ease, border-color .3s ease;
  z-index:1000;
}
.glass-header.scrolled{
  background:rgba(255,255,255,0.24);
  border-color:rgba(255,255,255,0.25);
}
.glass-header a{
  color:var(--text);
  margin:0 12px;
  font-weight:500;
}
.glass-header a:focus-visible{
  outline:3px solid var(--blue);
  outline-offset:2px;
}
```  
**SAFE JS:**  
```js
document.addEventListener('scroll',()=>{
  const hdr=document.querySelector('.glass-header');
  if(window.scrollY>50) hdr.classList.add('scrolled');
  else hdr.classList.remove('scrolled');
});
```  
EFFECT: Делает шапку визуально «премиальной», сохраняет её доступной на всех скроллах, повышает восприятие бренда и удерживает навигацию в поле зрения.  
RISK: На старых браузерах без поддержки `backdrop-filter` будет обычный полупрозрачный фон; эффект всё‑равно будет приемлем.  
ROLLBACK: `git checkout -- index.html && git checkout -- style.css` (удалить добавленные строки и `<nav>`).  
VERIFY: Открыть страницу, прокрутить > 50 px — шапка должна плавно поменять фон и стать чуть более непрозрачной; проверить, что ссылки остаются кликабельными.  
PRIORITY: 2 — небольшие изменения, быстрый выигрыш в восприятии премиальности без влияния на основную конверсию.  

---  

IDEA: SKILL — variable‑font‑typography‑premium  
KNOB: **Name:** `variable-font-typography-premium`  
**When to apply:** На любые заголовки h1‑h3 и ключевые блоки текста, где нужен плавный диапазон весов без загрузки нескольких файлов шрифтов.  
**Steps:**  
1. В `<head>` добавить `@font-face` для Manrope Variable (Google Fonts поддерживает `@font-face` с `font-variation-settings`).  
2. Заменить текущие `font-weight` на `font-variation-settings: 'wght' <value>` через CSS‑переменные.  
3. Использовать `clamp()` + `vw` для fluid‑typography, привязав к переменной `--fs-base`.  
**SAFE CSS:**  
```css
@font-face{
  font-family:'Manrope';
  src:url('https://fonts.gstatic.com/s/manrope/v13/1Ptug8zYS_SKggPNyC0ISg.woff2') format('woff2');
  font-weight:100 900;
  font-display:swap;
}
:root{
  --fs-base:clamp(1rem,1.2vw,1.5rem);
}
h1,h2,h3{
  font-family:'Manrope',sans-serif;
  font-variation-settings:'wght' var(--weight,600);
  font-size:var(--fs-base);
}
h1{--weight:800;}
h2{--weight:700;}
h3{--weight:600;}
```
**SAFE JS:** *(не требуется)*  
EFFECT: Сокращает количество запросов к шрифту, ускоряет рендер, а также даёт плавные переходы веса при интерактивных состояниях (например, при ховере — меняем `--weight`). Улучшает читаемость и ощущение «премиум‑типа».  
RISK: Требуется поддержка переменных шрифтов (Chrome ≥ 84, Safari ≥ 14, Firefox ≥ 71) – старые браузеры упадут к обычному весу.  
ROLLBACK: Удалить блок `@font-face` и CSS‑правила, вернуть прежние `font-weight` = 400/600.  
VERIFY: Открыть DevTools → Computed → проверить, что `font-variation-settings` присутствует; переключить `--weight` в консоли и убедиться в плавном изменении толщины.  
PRIORITY: 1 — экономит ~30 KB запросов шрифтов, сразу повышает метрику LCP и воспринимается как «дорогой» дизайн.  

---  

IDEA: SKILL — scroll‑tilt‑cards  
KNOB: **Name:** `scroll-tilt-cards`  
**When to apply:** На любые блоки‑карточки (`.price-card`, `.step`, `.pain-card`) где нужен лёгкий 3‑D‑эффект, но без нагрузки от постоянного отслеживания мыши.  
**Steps:**  
1. Добавить к каждому элементу класс `tilt-card`.  
2. В CSS задать начальное `transform: perspective(800px) rotateX(0deg) rotateY(0deg);` и `transition`.  
3. Добавить небольшую JS‑функцию, использующую `IntersectionObserver` для вычисления процента видимости и изменяющую угол наклона в зависимости от позиции скролла.  
**SAFE CSS:**  
```css
.tilt-card{
  transform:perspective(800px) rotateX(0deg) rotateY(0deg);
  transition:transform .4s ease-out;
  will-change:transform;
}
```  
**SAFE JS:**  
```js
const tiltCards=document.querySelectorAll('.tilt-card');
const obs=new IntersectionObserver(entries=>{
  entries.forEach(e=>{
    if(e.isIntersecting){
      const rect=e.target.getBoundingClientRect();
      const tiltX= (rect.top-window.innerHeight/2)/window.innerHeight*10; // -10..10
      const tiltY= (rect.left-window.innerWidth/2)/window.innerWidth*10;
      e.target.style.transform=`perspective(800px) rotateX(${tiltX}deg) rotateY(${tiltY}deg)`;
    }
  });
},{threshold:[0,0.5,1]});
tiltCards.forEach(c=>obs.observe(c));
```  
EFFECT: Создаёт лёгкое ощущение глубины при скролле, усиливает премиальный визуальный слой, не требует постоянного прослушивания `mousemove`.  
RISK: На слабых устройствах может появиться небольшая задержка при пересчёте transform; можно отключить через `prefers-reduced-motion`.  
ROLLBACK: Удалить класс `tilt-card` и скрипт‑observer; вернуть оригинальные стили.  
VERIFY: Прокрутить страницу, наблюдать лёгкое наклонение карточек; открыть DevTools → Performance → ensure no long tasks > 50 ms.  
PRIORITY: 2 — визуальный апгрейд с минимальной нагрузкой, повышает восприятие «дорогого» сайта.  

---  

IDEA: SKILL — pulse‑cta‑hover‑glow  
KNOB: **Name:** `pulse-cta-hover-glow`  
**When to apply:** На все ссылки‑CTA, оформленные как кнопки (`.btn-primary`, `.cta-row a`).  
**Steps:**  
1. Добавить к CTA класс `pulse-cta`.  
2. В CSS задать анимацию «pulse» (scale + box‑shadow) с `animation-timing-function: ease-out`.  
3. При `:focus-visible` добавить более яркую подсветку для доступности.  
**SAFE CSS:**  
```css
.pulse-cta{
  position:relative;
  overflow:hidden;
}
.pulse-cta::after{
  content:"";
  position:absolute;
  inset:0;
  border-radius:inherit;
  background:radial-gradient(circle at center, var(--blue) 0%, transparent 70%);
  opacity:0;
  transform:scale(0);
  transition:opacity .2s,transform .3s;
}
.pulse-cta:hover::after,
.pulse-cta:focus-visible::after{
  opacity:.25;
  transform:scale(1.2);
}
@keyframes pulse{
  0%{transform:scale(1);box-shadow:0 0 0 0 rgba(139,92,246,.0);}
  70%{transform:scale(1.05);box-shadow:0 0 0 12px rgba(139,92,246,.0);}
  100%{transform:scale(1);box-shadow:0 0 0 0 rgba(139,92,246,.0);}
}
.pulse-cta:hover{
  animation:pulse .8s ease
