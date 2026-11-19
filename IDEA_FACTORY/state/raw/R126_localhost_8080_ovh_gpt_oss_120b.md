# localhost:8080/ovh/gpt-oss-120b  2026-11-17 07:48:27
duration=39.2 error=- attempts=1

IDEA: SKILL — glassmorphic-cta-button  
KNOB: **Name:** `glassmorphic-cta-button`  
**When to apply:** На любой лендинг с CTA‑ссылками, где нужен премиальный, «прозрачный» вид кнопки.  
**SAFE CSS:**  
```css
/* glassmorphic CTA button */
.btn-primary.glass {
  background: rgba(255,255,255,0.12);
  backdrop-filter: blur(12px) saturate(180%);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  border: 1px solid rgba(255,255,255,0.3);
  color: var(--text);
  transition: background .3s, border .3s, transform .2s;
}
.btn-primary.glass:hover,
.btn-primary.glass:focus-visible {
  background: rgba(255,255,255,0.2);
  border-color: var(--grad);
  transform: translateY(-2px);
}
```
**SAFE JS:** *(не требуется)*  
EFFECT: Повышает восприятие премиальности CTA, усиливает доверие и кликабельность за счёт современного «стеклянного» дизайна.  
RISK: Требует поддержку `backdrop-filter` (не работает в старых Safari < 13); в неподдерживаемых браузерах будет обычный полупрозрачный фон.  
ROLLBACK: `git checkout -- index.improved.html` (удалить файл‑скилл) или просто удалить строку `.glass` из `<link rel="stylesheet">`.  
VERIFY: Открыть `index.improved.html`, убедиться, что кнопки с классом `btn-primary glass` получили полупрозрачный фон и мягкую тень; проверить в Chrome / Safari.  
PRIORITY: 1 – визуальный апгрейд «премиум», быстрый вёрсткой, сразу повышает конверсию.  

---  

IDEA: SKILL — card-3d-tilt-hover  
KNOB: **Name:** `card-3d-tilt-hover`  
**When to apply:** На карточках цены, шагов или демо‑концептов, где нужен интерактивный 3‑D‑эффект при наведении курсора.  
**SAFE CSS:**  
```css
/* 3D‑tilt container */
.tilt-card {
  perspective: 800px;
}
.tilt-card-inner {
  transition: transform .25s ease-out;
  transform-style: preserve-3d;
}
.tilt-card:hover .tilt-card-inner,
.tilt-card:focus-visible .tilt-card-inner {
  transform: rotateX(4deg) rotateY(-4deg);
}
```
**SAFE JS:** *(не требуется – эффект работает только на hover/focus)*  
EFFECT: Делает карточки «живыми», повышает вовлечённость и запоминаемость предложения, особенно на десктопе.  
RISK: На мобильных устройствах hover‑эффект не срабатывает; может слегка увеличить нагрузку на GPU, но без заметного замедления.  
ROLLBACK: Удалить классы `tilt-card` и `tilt-card-inner` из HTML/CSS или откатить файл через `git checkout`.  
VERIFY: В браузере на десктопе наведите курсор на любую карточку, должна появиться лёгкая наклонённость; проверка в DevTools → Elements.  
PRIORITY: 2 – сильный визуальный эффект, легко реализуется, но менее критичен, чем CTA‑апгрейд.  

---  

IDEA: SKILL — ambient-hero-gradient-flow  
KNOB: **Name:** `ambient-hero-gradient-flow`  
**When to apply:** В секции hero, где нужен фон‑градиент, медленно «текущий» по оси X/Y, создающий ощущение премиального движения без JavaScript.  
**SAFE CSS:**  
```css
/* ambient gradient animation */
.hero-bg-ambient {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg,
    #8b5cf6 0%,
    #34d399 35%,
    #22d3ee 70%,
    #8b5cf6 100%);
  background-size: 300% 300%;
  animation: ambientFlow 20s ease infinite;
  z-index: -1;
}
@keyframes ambientFlow {
  0%   {background-position: 0% 50%;}
  50%  {background-position: 100% 50%;}
  100% {background-position: 0% 50%;}
}
```
**SAFE JS:** *(не требуется)*  
EFFECT: Создаёт динамический, но ненавязчивый фон, усиливающий ощущение «дорогого» сайта и удерживает взгляд посетителя в верхней части страницы.  
RISK: Поскольку анимация бесконечна, может увеличить расход батареи на мобильных устройствах; рекомендуется добавить `prefers-reduced-motion`‑медиа‑запрос.  
ROLLBACK: Удалить элемент `<div class="hero-bg-ambient"></div>` и его CSS‑правила; откат через `git checkout`.  
VERIFY: Открыть страницу, убедиться в плавном смещении градиента в hero; проверить в Chrome DevTools → Computed → animation‑name.  
PRIORITY: 3 – улучшает восприятие бренда, но менее критично для конверсии.  

---  

IDEA: SKILL — premium-typography-variable  
KNOB: **Name:** `premium-typography-variable`  
**When to apply:** На всех заголовках (h1‑h3) и важных текстовых блоках, где доступен переменный шрифт Manrope (подключён уже).  
**SAFE CSS:**  
```css
/* enable variable font features */
h1, h2, h3 {
  font-family: 'Manrope', system-ui, sans-serif;
  font-variation-settings: "wght" 600;
  transition: font-variation-settings .3s ease;
}
h1:hover, h2:hover, h3:hover {
  font-variation-settings: "wght" 800;
}
```
**SAFE JS:** *(не требуется)*  
EFFECT: При наведении заголовок «толстеет», создавая ощущение интерактивности и высшего качества типографики без увеличения размеров шрифта.  
RISK: Не все браузеры поддерживают `font-variation-settings` (например, IE); в таких браузерах эффект будет проигнорирован.  
ROLLBACK: Удалить правила `font-variation-settings` из CSS; откат через `git checkout`.  
VERIFY: Наведите курсор на любой заголовок – его толщина должна плавно увеличиться; проверка в DevTools → Computed → font‑variation‑settings.  
PRIORITY: 3 – тонкое улучшение бренда, минимальный риск, легко проверяется.  

---  

IDEA: SKILL — scroll-triggered-depth-reveal  
KNOB: **Name:** `scroll-triggered-depth-reveal`  
**When to apply:** На блоках, которые появляются ниже первого экрана (например, секции «Три шага», «Демо‑концепты», «FAQ»).  
**SAFE CSS:**  
```css
/* initial hidden state */
.depth-reveal {
  opacity: 0;
  transform: translateZ(-40px);
  transition: opacity .6s ease-out, transform .6s ease-out;
  will-change: opacity, transform;
}

/* when in viewport */
.depth-reveal.in-view {
  opacity: 1;
  transform: translateZ(0);
}
```
**SAFE JS:**  
```js
(() => {
  const obs = new IntersectionObserver((entries)=> {
    entries.forEach(e=> e.target.classList.toggle('in-view', e.isIntersecting));
  }, {threshold: 0.15});
  document.querySelectorAll('.depth-reveal').forEach(el=> obs.observe(el));
})();
```
EFFECT: Элементы «выходят» из глубины при скролле, создавая ощущение 3‑D‑пространства и повышая вовлечённость пользователя.  
RISK: Добавляет небольшую нагрузку на CPU из‑за IntersectionObserver; на старых браузерах без поддержки скрипт просто не выполнится, элементы останутся скрытыми – рекомендуется добавить fallback‑класс `in-view` в HTML.  
ROLLBACK: Удалить все `.depth-reveal`‑классы и скрипт; откат через `git checkout`.  
VERIFY: Прокрутите страницу, элементы с классом `depth-reveal` должны плавно появиться; откройте DevTools → Console, убедитесь в отсутствии ошибок.  
PRIORITY: 2 – улучшает динамику страницы, поддерживается большинством современных браузеров, легко тестировать.
