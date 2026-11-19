---
name: Depth‑hover 3D card
source: localhost:8080/ovh/gpt-oss-120b
round: 133
status: proposed
portable: true
tags: [static-landing, portable]
---

# Depth‑hover 3D card

SKILL — depth-hover-card
Name: depth-hover-card
When to apply: На любые карточки (`.price-card`, `.step`, `.demo-card`) где нужен интерактивный 3D‑эффект при наведении.
SAFE CSS:
```css
.card-3d {
perspective: 600px;
transform-style: preserve-3d;
transition: transform .3s ease;
}
```
SAFE JS:
```js
document.querySelectorAll('.card-3d').forEach(c=>{
c.addEventListener('mousemove',e=>{
const r=c.getBoundingClientRect();
const x=((e.clientX-r.left)/r.width-0.5)*20;
const y=((e.clientY-r.top)/r.height-0.5)*20;
c.style.transform=`rotateY(${x}deg) rotateX(${ -y }deg)`;
});
c.addEventListener('mouseleave',()=>c.style.transform='rotateY(0) rotateX(0)');
});
```

## Когда применять
Делает карточки «живыми», повышает вовлечённость и запоминаемость предложения, что может увеличить конверсии в цене/демо.

## Проверка
На ПК переместить курсор по карточке – она должна наклоняться; на мобильном проверить отсутствие ошибок в консоли.

## SAFE JS
```js
```js
document.querySelectorAll('.card-3d').forEach(c=>{
c.addEventListener('mousemove',e=>{
const r=c.getBoundingClientRect();
const x=((e.clientX-r.left)/r.width-0.5)*20;
const y=((e.clientY-r.top)/r.height-0.5)*20;
c.style.transform=`rotateY(${x}deg) rotateX(${ -y }deg)`;
});
c.addEventListener('mouseleave',()=>c.style.transform='rotateY(0) rotateX(0)');
});
```
```
