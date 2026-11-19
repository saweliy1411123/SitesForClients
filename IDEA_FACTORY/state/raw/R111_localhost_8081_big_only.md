# localhost:8081/big_only  2026-11-17 07:07:30
duration=101.1 error=- attempts=1

IDEA: SKILL — scroll-reveal-progress-bar (прогресс-бар скролла с градиентом и glow-эффектом)
KNOB: Полное тело скилла:
**Name:** `scroll-reveal-progress-bar`
**When to apply:** На любом статическом лендинге с вертикальным скроллом, где нужно визуально показать прогресс чтения и повысить вовлечённость.
**Steps:**
1. В `<body>` сразу после `<header>` добавить `<div class="scroll-progress" aria-hidden="true"><span></span></div>`.
2. В `<style>` добавить CSS (см. SAFE CSS).
3. Если нужен JS — добавить SAFE JS для обновления ширины.
**SAFE CSS:**
```css
.scroll-progress{position:fixed;top:0;left:0;width:100%;height:4px;z-index:9999;background:transparent;pointer-events:none}
.scroll-progress span{display:block;height:100%;width:0;background:linear-gradient(90deg,#8b5cf6,#ec4899,#f59e0b);border-radius:0 2px 2px 0;box-shadow:0 0 12px rgba(139,92,246,.6);transition:width .1s linear;will-change:width}
```
**SAFE JS:**
```js
(function(){var bar=document.querySelector('.scroll-progress span');if(!bar)return;function update(){var h=document.documentElement;var max=h.scrollHeight-h.clientHeight;var p=max>0?(h.scrollTop||document.body.scrollTop)/max*100:0;bar.style.width=p+'%';}window.addEventListener('scroll',update,{passive:true});window.addEventListener('resize',update);update();})();
```
EFFECT: Визуальный индикатор прогресса чтения — пользователь видит, сколько осталось, что повышает удержание и снижает bounce-rate; добавляет премиальный «дорогой» вид.
RISK: Может отвлекать от контента, если ширина/цвет слишком яркие; при `prefers-reduced-motion` стоит скрывать.
ROLLBACK: Удалить `<div class="scroll-progress">` и CSS/JS блок.
VERIFY: Открыть index.html, проскроллить — полоска плавно заполняется от 0 до 100%.
PRIORITY: 2 — улучшает UX и восприятие, но не критично для конверсии.
SKILL: scroll-reveal-progress-bar

IDEA: SKILL — card-hover-lift-and-shadow (премиальное поднятие карточек с мягкой тенью при наведении)
KNOB: Полное тело скилла:
**Name:** `card-hover-lift-and-shadow`
**When to apply:** На любом лендинге с карточками (услуги, цены, демо-концепты, шаги), где нужно усилить интерактивность и «дорогой» отклик на hover.
**Steps:**
1. Найти все карточки (`.price-card`, `.demo-card`, `.step-card` и т.п.).
2. Добавить CSS-правила для `:hover` и `:focus-visible`.
3. Для плавности добавить `transition` в базовое состояние.
**SAFE CSS:**
```css
.price-card,.demo-card,.step-card{transition:transform .35s cubic-bezier(.22,.61,.36,1),box-shadow .35s ease;will-change:transform}
.price-card:hover,.demo-card:hover,.step-card:hover{transform:translateY(-8px) scale(1.02);box-shadow:0 24px 60px rgba(0,0,0,.18),0 8px 24px rgba(139,92,246,.12)}
.price-card:focus-visible,.demo-card:focus-visible,.step-card:focus-visible
