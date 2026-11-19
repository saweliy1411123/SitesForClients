# localhost:8080/ovh/gpt-oss-120b  2026-11-17 06:07:20
duration=41.3 error=- attempts=1

IDEA: SKILL — neon-glow-border  
KNOB: **Name:** `neon-glow-border`  
**When to apply:** На всех CTA‑кнопках (`.btn-primary`) и на карточках цены (`.price-card`) для придания премиального «неонового» обводки.  
**SAFE CSS:**  
```css
/* neon glow border */
.neon-glow {
  position: relative;
  overflow: hidden;
}
.neon-glow::before {
  content: "";
  position: absolute;
  inset: -2px;
  background: linear-gradient(45deg,
    #8b5cf6, #4ec9f0, #8b5cf6);
  filter: blur(6px);
  opacity: 0;
  transition: opacity .3s ease-in-out;
  z-index: -1;
}
.neon-glow:hover::before,
.neon-glow:focus-visible::before {
  opacity: 0.8;
}
.neon-glow {
  box-shadow: 0 0 10px rgba(139,92,246,.2);
}
```
**SAFE JS:** (необязательно)  
```js
// добавляем класс .neon-glow к нужным элементам один раз
document.querySelectorAll('.btn-primary,.price-card').forEach(el=>el.classList.add('neon-glow'));
```  
EFFECT: Усиление визуального восприятия CTA и ценовых карточек, повышает чувство эксклюзивности и привлекает внимание к конверсионным элементам.  
RISK: При слишком яркой настройке может ухудшить контраст для слабовидящих; нужно проверять WCAG AA.  
ROLLBACK: `git checkout HEAD -- index.html` (или удалить добавленные строки в CSS/JS).  
VERIFY: Открыть страницу, навести курсор на кнопку и карточку – должна появиться мягкая неоновая подсветка без смещения контента; проверить в режиме «prefers-reduced-motion» (должно быть отключено).  
PRIORITY: 1 – быстрый визуальный апгрейд, минимум кода, высокий ROI.  

---  

IDEA: SKILL — perspective-tilt-parallax  
KNOB: **Name:** `perspective-tilt-parallax`  
**When to apply:** На секциях с фоновыми иллюстрациями (например, `.hero`, `.final`) чтобы добавить лёгкий 3‑D‑параллакс‑эффект при скролле.  
**SAFE CSS:**  
```css
/* container with perspective */
.parallax-perspective {
  perspective: 800px;
  overflow: hidden;
}
.parallax-perspective .parallax-layer {
  transform: translateZ(var(--tz, 0));
  transition: transform .2s ease-out;
}
```
**SAFE JS:**  
```js
// лёгкий скролл‑тильт, без throttling (мало элементов)
document.addEventListener('scroll', () => {
  const scrollY = window.scrollY;
  document.querySelectorAll('.parallax-perspective .parallax-layer')
    .forEach(el => {
      const depth = parseFloat(el.dataset.depth) || 0;
      const tz = (scrollY * depth) * 0.05;
      el.style.setProperty('--tz', `${tz}px`);
    });
});
```  
EFFECT: Создаёт ощущение глубины и динамики, усиливая премиальный «тёплый» визуальный стиль без тяжёлых библиотек.  
RISK: На слабом железе может вызвать небольшие лаги; рекомендуется отключать при `prefers-reduced-motion: reduce`.  
ROLLBACK: Удалить добавленные классы `.parallax-perspective` и `.parallax-layer` и связанные скрипты; `git checkout HEAD -- index.html`.  
VERIFY: Прокрутить страницу, убедиться, что фоновые слои слегка смещаются в зависимости от скролла; включить/выключить `prefers-reduced-motion` в DevTools – эффект исчезает.  
PRIORITY: 2 – добавляет «wow‑factor», но требует небольшого JS, поэтому ставим средний приоритет.  

---  

IDEA: SKILL — glass-modal-fade  
KNOB: **Name:** `glass-modal-fade`  
**When to apply:** Для отображения дополнительной информации (например, «Подробный чек‑лист цены») в модальном окне с эффектом стеклянной морфологии.  
**SAFE CSS:**  
```css
/* backdrop glass effect */
.glass-modal {
  position: fixed;
  inset: 0;
  display: none;
  align-items: center;
  justify-content: center;
  background: rgba(255,255,255,.1);
  backdrop-filter: blur(12px) saturate(180%);
  -webkit-backdrop-filter: blur(12px) saturate(180%);
  z-index: 1000;
}
.glass-modal.active {display: flex;}
.glass-modal .content {
  background: rgba(255,255,255,.15);
  border-radius: 12px;
  padding: 2rem;
  max-width: 90%;
  max-height: 80vh;
  overflow-y: auto;
  box-shadow: 0 8px 32px rgba(0,0,0,.25);
  animation: fadeIn .3s ease-out forwards;
}
@keyframes fadeIn {
  from {opacity:0; transform:scale(.95);}
  to {opacity:1; transform:scale(1);}
}
```
**SAFE JS:**  
```js
// открытие/закрытие модального окна
document.addEventListener('click', e => {
  if (e.target.matches('[data-modal-open]')) {
    const id = e.target.dataset.modalOpen;
    document.getElementById(id).classList.add('active');
  }
  if (e.target.matches('.glass-modal') || e.target.matches('.glass-modal .close')) {
    e.target.closest('.glass-modal').classList.remove('active');
  }
});
```  
EFFECT: Позволяет показать детальную информацию без перехода на новую страницу, сохраняет стиль «luxury» через стеклянный фон, повышает время нахождения пользователя на сайте.  
RISK: Требует небольшого JS‑кода и корректного управления фокусом; без него может возникнуть проблема доступности.  
ROLLBACK: Удалить блоки `.glass-modal` и скрипт; `git checkout HEAD -- index.html`.  
VERIFY: Добавить кнопку `data-modal-open="priceInfo"` к любой секции, кликнуть – открывается полупрозрачное модальное окно; проверить, что скролл внутри окна работает и закрытие по клику вне контента.  
PRIORITY: 3 – полезно, но требует дополнительного тестирования доступности, поэтому отложим после более простых улучшений.
