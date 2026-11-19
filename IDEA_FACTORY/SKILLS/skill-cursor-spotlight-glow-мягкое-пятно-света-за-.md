---
name: SKILL — Cursor Spotlight Glow (мягкое пятно света за курсором на hero)
source: lareper/glm-5.2
round: 28
status: proposed
portable: true
tags: [static-landing, portable, responsive]
---

# SKILL — Cursor Spotlight Glow (мягкое пятно света за курсором на hero)

SKILL — cursor-spotlight
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

## Когда применять
hero выглядит живым

## Проверка


## SAFE CSS
```css
.spotlight-host{position:relative}
.spotlight-host::before{content:"";position:absolute;inset:0;pointer-events:none;z-index:1;background:radial-gradient(320px circle at var(--sx,50%) var(--sy,40%),rgba(139,92,246,.10),transparent 65%);opacity:0;transition:opacity .4s}
.spotlight-host:hover::before{opacity:1}
@media (prefers-reduced-motion:reduce){.spotlight-host::before{display:none}}
```

## SAFE JS
```js
var h=document.querySelector('.spotlight-host');
if(h&&window.matchMedia('(pointer:fine)').matches){h.addEventListener('mousemove',function(e){var r=h.getBoundingClientRect();h.style.setProperty('--sx',(e.clientX-r.left)+'px');h.style.setProperty('--sy',(e.clientY-r.top)+'px');});}
```
