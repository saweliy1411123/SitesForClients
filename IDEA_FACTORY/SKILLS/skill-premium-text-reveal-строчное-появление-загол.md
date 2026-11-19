---
name: SKILL — premium-text-reveal (строчное появление заголовков с blur+translateZ)
source: lareper/glm-5.2
round: 63
status: proposed
portable: true
tags: [static-landing, portable, 3d, responsive]
---

# SKILL — premium-text-reveal (строчное появление заголовков с blur+translateZ)

SKILL — premium-text-reveal
Название: premium-text-reveal
Когда применять: на любом лендинге с крупными заголовками (h1/h2), где нужна «дорогая» анимация появления без библиотек — текст всплывает построчно из лёгкого блюра с 3D-наклоном.
Шаги:
1. В HTML обернуть строки заголовка в `<span class="tr-line"><span class="tr-inner">…текст…</span></span>` (одна строка = один span; для h1 с `<br>` — по спану на каждую часть).
2. В CSS добавить стили: внешние span — `overflow:hidden; display:block; perspective:600px;`, внутренние — начальное состояние `opacity:0; transform:translateY(28px) rotateX(-12deg) translateZ(-20px); filter:blur(6px);`.
3. Задать каскадную задержку через `--d` (как у существующих `.reveal`), переход `transition: all .9s cubic-bezier(.16,1,.3,1)`.
4. Появление — по классу `.visible` на родителе (совместимо с уже существующим IntersectionObserver-кодом `.reveal.visible`, L147) либо добавить мини-JS-наблюдатель.
5. Обернуть всё в `@media (prefers-reduced-motion: no-preference)`, чтобы при reduced-motion текст был сразу видим.
SAFE CSS:
```
@media (prefers-reduced-motion: no-preference){
.tr-line{display:block;overflow:hidden;perspective:600px}
.tr-inner{display:inline-block;opacity:0;transform:translateY(28px) rotateX(-12deg) translateZ(-20px);filter:blur(6px);transition:opacity .9s cubic-bezier(.16,1,.3,1),transform .9s cubic-bezier(.16,1,.3,1),filter .9s cubic-bezier(.16,1,.3,1);transition-delay:var(--d,0s)}
.visible .tr-inner,.tr-line.visible .tr-inner{opacity:1;transform:none;filter:blur(0)}
}
@media (prefers-reduced-motion: reduce){
.tr-inner{opacity:1;transform:none;filter:none}
}
```
SAFE JS:
```
document.querySelectorAll('.tr-line').forEach(function(el){
if('IntersectionObserver' in window){
new IntersectionObserver(function(en,obs){en.forEach(function(e){if(e.isIntersecting){e.target.classList.add('visible');obs.unobserve(e.target);}});},{threshold:.4}).observe(el);
}else{el.classList.add('visible');}
});
```

## Когда применять
заголовки появляются «как в дорогих студийных портфолио» — построчно, с глубиной и расфокусом; усиливает премиальное восприятие услуги «лендинг за 2 дня» без единой библиотеки.

## Проверка
открыть index.improved.html, проскроллить к h2 «Три шага» — строки появляются каскадом; в DevTools включить prefers-reduced-motion: reduce — текст виден сразу без анимации; проверить на 360px, что переносы не ломаются.

## SAFE CSS
```css
```
@media (prefers-reduced-motion: no-preference){
.tr-line{display:block;overflow:hidden;perspective:600px}
.tr-inner{display:inline-block;opacity:0;transform:translateY(28px) rotateX(-12deg) translateZ(-20px);filter:blur(6px);transition:opacity .9s cubic-bezier(.16,1,.3,1),transform .9s cubic-bezier(.16,1,.3,1),filter .9s cubic-bezier(.16,1,.3,1);transition-delay:var(--d,0s)}
.visible .tr-inner,.tr-line.visible .tr-inner{opacity:1;transform:none;filter:blur(0)}
}
@media (prefers-reduced-motion: reduce){
.tr-inner{opacity:1;transform:none;filter:none}
}
```
```

## SAFE JS
```js
```
document.querySelectorAll('.tr-line').forEach(function(el){
if('IntersectionObserver' in window){
new IntersectionObserver(function(en,obs){en.forEach(function(e){if(e.isIntersecting){e.target.classList.add('visible');obs.unobserve(e.target);}});},{threshold:.4}).observe(el);
}else{el.classList.add('visible');}
});
```
```
