---
name: SKILL — scroll‑tilt‑cards
source: localhost:8080/ovh/gpt-oss-120b
round: 140
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — scroll‑tilt‑cards

**Name:** `scroll-tilt-cards`
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

## Когда применять
Создаёт лёгкое ощущение глубины при скролле, усиливает премиальный визуальный слой, не требует постоянного прослушивания `mousemove`.

## Проверка
Прокрутить страницу, наблюдать лёгкое наклонение карточек; открыть DevTools → Performance → ensure no long tasks > 50 ms.

## SAFE JS
```js
**
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
```
