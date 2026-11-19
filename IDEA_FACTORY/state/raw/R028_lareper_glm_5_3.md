# lareper/glm-5.3  2026-11-17 03:02:04
duration=2.3 error=- attempts=2

IDEA: SKILL — Premium Light Sweep (блик, пробегающий по карточке при hover)
KNOB: SKILL — light-sweep-card
### Название
light-sweep-card
### Когда применять
Любой лендинг с карточками (демо-концепты, тарифы, шаги), где нужен «дорогой» эффект света без библиотек. Применять к `.demo-card`, `.price-card`, `.step` и подобным блочным элементам.
### Шаги
1. Добавить CSS ниже в `<style>` (или в копию index.improved.html).
2. Убедиться, что у карточки есть `position:relative; overflow:hidden`.
3. Проверить на мобильном: эффект только по hover/focus-within, на тач-устройствах не мешает.
SAFE CSS:
.card-sweep{position:relative;overflow:hidden}
.card-sweep::after{content:"";position:absolute;top:0;left:-120%;width:60%;height:100%;background:linear-gradient(105deg,transparent,rgba(255,255,255,.14),transparent);transform:skewX(-18deg);transition:left .7s ease;pointer-events:none}
.card-sweep:hover::after,.card-sweep:focus-within::after{left:130%}
@media (prefers-reduced-motion:reduce){.card-sweep::after{display:none}}
EFFECT: премиальное ощущение «дорогого» сайта, карточки реагируют на курсор — выше воспринимаемая ценность услуги.
RISK: на слабых устройствах анимация left может дёргаться — ограничено hover и отключено при prefers-reduced-motion.
ROLLBACK: git checkout -- index.html (или удалить блок .card-sweep из CSS).
VERIFY: открыть index.improved.html, навести курсор на карточку демо — блик пробегает слева направо за ~0.7 с; проверить Tab-фокус тоже вызывает блик.
PRIORITY: 2 — чисто визуальный апгрейд, но дешёвый и безопасный.
SKILL: light-sweep-card

IDEA: SKILL — Cursor Spotlight Glow (мягкое пятно света за курсором на hero)
KNOB: SKILL — cursor-spotlight
### Название
cursor-spotlight
### Когда применять
Любой тёмный лендинг с hero-секцией; добавляет «дорогую» глубину без частиц и тяжёлых скриптов. Только desktop (pointer:fine).
### Шаги
1. Добавить CSS и JS ниже.
2. JS вешает один listener на hero, обновляет CSS-переменные — без таймеров и fetch.
SAFE CSS:
.spotlight-host{position:relative}
.spotlight-host::before{content:"";position:absolute;inset:0;pointer-events:none;z-index:1;background:radial-gradient(320px circle at var(--sx,50%) var(--sy,40%),rgba(139,92,246,.10),transparent 65%);opacity:0;transition:opacity .4s}
.spotlight-host:hover::before{opacity:1}
@media (prefers-reduced-motion:reduce){.spotlight-host::before{display:none}}
SAFE JS:
var h=document.querySelector('.spotlight-host');
if(h&&window.matchMedia('(pointer:fine)').matches){h.addEventListener('mousemove',function(e){var r=h.getBoundingClientRect();h.style.setProperty('--sx',(e.clientX-r.left)+'px');h.style.setProperty('--sy',(e.clientY-r.top)+'px');});}
EFFECT: hero выглядит живым
