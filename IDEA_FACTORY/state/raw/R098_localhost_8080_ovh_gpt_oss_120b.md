# localhost:8080/ovh/gpt-oss-120b  2026-11-17 06:27:58
duration=29.5 error=- attempts=1

IDEA: SKILL — premium‑typography‑shadow  
KNOB: **NAME:** premium-typography-shadow  
**WHEN TO APPLY:** На любом статическом лендинге, где нужен премиальный визуальный акцент заголовков (h1‑h3).  
**STEPS:**  
1. Добавить в `<head>` блок `<style id="skill-premium-typography">` (или отдельный файл).  
2. Применить к заголовкам класс `typography‑premium`.  
3. При желании включить переключатель «dark‑mode»‑совместимости через CSS‑переменные.  
**SAFE CSS:**  
```css
.typography-premium {
  font-weight: 700;
  letter-spacing: -0.02em;
  text-shadow: 0 2px 4px rgba(0,0,0,0.15), 0 0 12px rgba(255,255,255,0.12);
  background: linear-gradient(135deg, #8b5cf6 0%, #5a67d8 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
@media (prefers-color-scheme: dark) {
  .typography-premium {
    text-shadow: 0 2px 4px rgba(0,0,0,0.45), 0 0 12px rgba(255,255,255,0.08);
  }
}
```
**SAFE JS:** *(не требуется)*  
EFFECT: Повышает восприятие бренда как премиального, улучшает визуальный фокус на ключевых сообщениях → рост CTR на CTA‑кнопки.  
RISK: На очень старых браузерах (IE 11) градиент‑текст может отобразиться без эффекта, но дизайн сохранится.  
ROLLBACK: `git checkout HEAD -- index.improved.html && rm -f index.improved.html` (или удалить `<style id="skill-premium-typography">`).  
VERIFY: Открыть страницу в Chrome, убедиться, что h1/h2/h3 теперь имеют градиентный текст и лёгкую тень; сравнить скриншот до/после.  
PRIORITY: 1 – самое заметное визуальное улучшение, быстро реализуется, сразу влияет на восприятие.  
SITE_REQUEST: hero  
SKILL: premium-typography-shadow  

---  

IDEA: SKILL — parallax‑scroll‑hero‑bg  
KNOB: **NAME:** parallax-scroll-hero-bg  
**WHEN TO APPLY:** В секции hero, где уже есть фон‑градиент и «blob»‑элементы, но нужен более глубокий визуальный эффект скролла.  
**STEPS:**  
1. Обернуть фоновые слои hero в контейнер `<div class="hero-parallax">`.  
2. Добавить CSS‑переменную `--scroll-y` через небольший JS‑слушатель (не более 20 мс).  
3. Применить 3‑слойный трансформ: задний слой – медленнее, передний – быстрее.  
**SAFE CSS:**  
```css
.hero-parallax {
  perspective: 800px;
  overflow: hidden;
}
.hero-parallax .bg-layer {
  position: absolute;
  inset: 0;
  will-change: transform;
}
.hero-parallax .bg-layer.layer-1 { transform: translateZ(-30px) scale(1.2); }
.hero-parallax .bg-layer.layer-2 { transform: translateZ(-15px) scale(1.1); }
.hero-parallax .bg-layer.layer-3 { transform: translateZ(0); }
```
**SAFE JS:**  
```js
document.addEventListener('scroll', () => {
  const y = window.scrollY;
  document.querySelectorAll('.hero-parallax .bg-layer').forEach((el,i)=>{
    const speed = (i+1)*0.05;
    el.style.transform = `translateY(${y*speed}px)`;
  });
});
```
EFFECT: Создаёт ощущение глубины при прокрутке, усиливает «premium»‑впечатление и удерживает внимание в верхней части страницы → увеличение времени‑на‑странице (dwell time).  
RISK: Небольшой JS‑слушатель может добавить ~0.5 ms нагрузки; на слабых устройствах может слегка дрожать, но эффект отключается в `prefers-reduced-motion`.  
ROLLBACK: Удалить `<style id="skill-parallax-hero">` и `<script id="skill-parallax-hero-js">` либо выполнить `git checkout HEAD -- index.improved.html`.  
VERIFY: Прокрутить страницу, убедиться в плавном смещении фоновых слоёв; включить/выключить `prefers-reduced-motion` в DevTools → эффект исчезает.  
PRIORITY: 2 – повышает визуальный уровень без значительного кода, но требует небольшого JS.  
SITE_REQUEST: hero  
SKILL: parallax-scroll-hero-bg  

---  

IDEA: SKILL — 3d‑tilt‑price‑card  
KNOB: **NAME:** 3d-tilt-price-card  
**WHEN TO APPLY:** На карточках цены (`.price-card`) в секции «Цена», где нужен интерактивный премиальный эффект при наведении/касании.  
**STEPS:**  
1. Добавить к каждому `.price-card` класс `tilt‑card`.  
2. В CSS задать `perspective` и базовый `transform`.  
3. Добавить лёгкий JS‑слушатель `pointermove` для расчёта угла наклона (max 10°).  
**SAFE CSS:**  
```css
.tilt-card {
  perspective: 600px;
  transition: transform 0.3s ease;
}
.tilt-card:hover,
.tilt-card:focus-visible {
  transform: rotateX(5deg) rotateY(5deg);
}
```
**SAFE JS:**  
```js
document.querySelectorAll('.price-card.tilt-card').forEach(card=>{
  card.addEventListener('pointermove',e=>{
    const rect = card.getBoundingClientRect();
    const x = (e.clientX - rect.left) / rect.width - 0.5;
    const y = (e.clientY - rect.top) / rect.height - 0.5;
    const rotX = y * 10; // max 10°
    const rotY = -x * 10;
    card.style.transform = `perspective(600px) rotateX(${rotX}deg) rotateY(${rotY}deg)`;
  });
  card.addEventListener('pointerleave',()=>{ card.style.transform=''; });
});
```
EFFECT: Делает цену более «осязаемой», повышает вовлечённость и воспринимается как современный премиум‑дизайн → рост кликов по кнопке «Получить демо».  
RISK: На мобильных без указателя эффект будет отключён (pointerleave сразу); небольшая нагрузка при большом числе карточек, но их здесь только одна‑две.  
ROLLBACK: Удалить CSS‑правила и `<script id="skill-tilt-price-js">`; либо откатить файл через `git checkout`.  
VERIFY: Навести курсор на карточку цены, увидеть плавный наклон; проверить на мобильных (должен быть без наклона).  
PRIORITY: 3 – улучшает взаимодействие с важным элементом цены, но требует JS; ставим ниже, если время ограничено.  
SITE_REQUEST: price  
SKILL: 3d-tilt-price-card
