---
name: SKILL — lazy-bg-image
source: localhost:8081/big_only
round: 34
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — lazy-bg-image


name: lazy-bg-image
when: при наличии тяжёлых фоновых изображений, задаваемых через CSS `background-image` в секциях ниже первого экрана (например, демонстрационные блоки)
steps:
- В HTML заменить `style="background-image:url(...)"` на `data-bg="url(...)"` без применения `background-image` сразу.
- Добавить в CSS базовый фон‑цвет/градиент для placeholder.
- Вставить скрипт, который с помощью `IntersectionObserver` подменяет `data-bg` на `background-image` при появлении элемента в зоне видимости.
SAFE CSS:
.lazy-bg{background-color:#111;background-size:cover;background-position:center;transition:background-image .4s ease}
SAFE JS:
(()=>{if(!('IntersectionObserver' in window))return;const obs=new IntersectionObserver((entries,ob)=>{entries.forEach(e=>{if(e.isIntersecting){const el=e.target;const url=el.dataset.bg;el.style.backgroundImage=`url(${url})`;ob.unobserve(el)}})});document.querySelectorAll('[data-bg]').forEach(el=>obs.observe(el));})();

## Когда применять
ускоряется первоначальная загрузка страницы, уменьшается количество блокирующего загрузку трафика, улучшая LCP и показатель Core Web Vitals.

## Проверка
открыть страницу в Chrome DevTools → Network, убедиться, что фоновые изображения загружаются только после скролла к соответствующим секциям; проверить, что в старых браузерах (режим «Disable JavaScript») фон всё‑равно отображается (можно добавить fallback в CSS).

## SAFE CSS
```css
.lazy-bg{background-color:#111;background-size:cover;background-position:center;transition:background-image .4s ease}
```

## SAFE JS
```js
(()=>{if(!('IntersectionObserver' in window))return;const obs=new IntersectionObserver((entries,ob)=>{entries.forEach(e=>{if(e.isIntersecting){const el=e.target;const url=el.dataset.bg;el.style.backgroundImage=`url(${url})`;ob.unobserve(el)}})});document.querySelectorAll('[data-bg]').forEach(el=>obs.observe(el));})();
```
