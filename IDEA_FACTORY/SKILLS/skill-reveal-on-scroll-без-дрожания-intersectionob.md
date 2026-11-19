---
name: SKILL — Reveal-on-scroll без дрожания (IntersectionObserver-стабилизатор для .reveal)
source: lareper/glm-5.2-fast-preview
round: 13
status: proposed
portable: true
tags: [static-landing, portable, responsive]
---

# SKILL — Reveal-on-scroll без дрожания (IntersectionObserver-стабилизатор для .reveal)

Название: **safe-reveal-observer**. Когда применять: любой лендинг, где элементы с классом .reveal анимируются, но анимация может сработать до попадания в вьюпорт или не сработать без JS — приводит к «пустым» секциям. Шаги: (1) добавить SAFE CSS, который показывает .reveal по умолчанию и скрывает только при наличии JS-класса .js-ready; (2) добавить SAFE JS с IntersectionObserver, добавляющий класс .in при входе в вьюпорт; (3) на <html> повесить класс js-ready первым скриптом. Гарантирует: без JS контент виден, с JS — плавное появление.
SAFE CSS:
```css
.js-ready .reveal{opacity:0;transform:translateY(18px);transition:opacity .6s ease,transform .6s ease;transition-delay:var(--d,0s)}
.js-ready .reveal.in{opacity:1;transform:none}
@media (prefers-reduced-motion: reduce){.js-ready .reveal{opacity:1;transform:none;transition:none}}
```
SAFE JS:
```js

## Когда применять


## Проверка


## SAFE CSS
```css
```css
.js-ready .reveal{opacity:0;transform:translateY(18px);transition:opacity .6s ease,transform .6s ease;transition-delay:var(--d,0s)}
.js-ready .reveal.in{opacity:1;transform:none}
@media (prefers-reduced-motion: reduce){.js-ready .reveal{opacity:1;transform:none;transition:none}}
```
```

## SAFE JS
```js
```js
```
