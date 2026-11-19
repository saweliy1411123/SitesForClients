---
name: SKILL — Mobile VH Fix
source: localhost:8080/ovh/gpt-oss-120b
round: 48
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Mobile VH Fix

**Name:** mobile-vh-fix
**When to apply:** На одностраничных лендингах с полноэкранными секциями (например, `.hero`), где высота `100vh` приводит к обрезке контента на мобильных браузерах с динамической адресной строкой.
**Steps:**
1. В `<head>` добавить небольшой скрипт, который вычисляет реальную высоту окна и сохраняет её в CSS‑переменную `--vh`.
2. Заменить все `height: 100vh` и `min-height: 100vh` на `height: calc(var(--vh, 1vh) * 100)` и аналогично для `min-height`.
3. При изменении ориентации/размера окна пересчитывать переменную (`resize` и `orientationchange`).
4. Проверить визуально на Android / iOS‑эмуляторах, убедиться, что первый экран полностью виден без прокрутки.
**SAFE CSS:**
```css
/* mobile‑vh‑fix – использование CSS‑переменной для корректной высоты */
.hero {
min-height: calc(var(--vh, 1vh) * 100);
}
section.fullscreen {
height: calc(var(--vh, 1vh) * 100);
}
```
**SAFE JS:**
```js
/* mobile‑vh‑fix – вычисление реального vh */
(function () {
const setVH = () => {
const vh = window.innerHeight * 0.01;
document.documentElement.style.setProperty('--vh', `${vh}px`);
};
setVH();
window.addEventListener('resize', setVH);
window.addEventListener('orientationchange', setVH);
})();
```

## Когда применять
Устраняет «потерянный» контент на мобильных устройствах, улучшая пользовательский опыт и показатель CLS → потенциальный рост конверсий.

## Проверка
Открыть страницу на мобильном эмуляторе (Chrome DevTools → Device Toolbar), убедиться, что верхний и нижний край секций полностью видим без скролла; сравнить с версией без скрипта.

## SAFE JS
```js
**
```js
/* mobile‑vh‑fix – вычисление реального vh */
(function () {
const setVH = () => {
const vh = window.innerHeight * 0.01;
document.documentElement.style.setProperty('--vh', `${vh}px`);
};
setVH();
window.addEventListener('resize', setVH);
window.addEventListener('orientationchange', setVH);
})();
```
```
