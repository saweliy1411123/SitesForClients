---
name: SKILL — section-fade-in-scroll
source: localhost:8080/ovh/gpt-oss-120b
round: 49
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — section-fade-in-scroll

METHOD: SKILL
**Name:** `section-fade-in-scroll`
**When to apply:** На любые секции `<section>` (кроме `.hero`), где нужен плавный вход при прокрутке, создающий ощущение «живого» лендинга.
**Steps:**
1. Добавить к целевым секциям класс `fade-section`.
2. Подключить CSS‑анимацию и JS‑обработчик ниже.
**SAFE CSS:**
```css
.fade-section{
opacity:0;
transform:translateY(30px);
transition:opacity .6s ease-out,transform .6s ease-out;
will-change:opacity,transform;
}
.fade-section.in-view{
opacity:1;
transform:translateY(0);
}
```
**SAFE JS:**
```js
const observer=new IntersectionObserver((entries)=>{
entries.forEach(entry=>{
if(entry.isIntersecting) entry.target.classList.add('in-view');
});
},{threshold:0.15});
document.querySelectorAll('.fade-section').forEach(el=>observer.observe(el));
```

## Когда применять
Уменьшает визуальный шум, делает скролл более динамичным, повышает время пребывания и воспринимаемую «премиальность».

## Проверка
Прокрутить страницу – секции должны плавно появляться; открыть DevTools → Disable JavaScript – секции сразу видимы (fallback).

## SAFE JS
```js
**
```js
const observer=new IntersectionObserver((entries)=>{
entries.forEach(entry=>{
if(entry.isIntersecting) entry.target.classList.add('in-view');
});
},{threshold:0.15});
document.querySelectorAll('.fade-section').forEach(el=>observer.observe(el));
```
```
