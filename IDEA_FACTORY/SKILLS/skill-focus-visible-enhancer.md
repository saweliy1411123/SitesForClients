---
name: SKILL — focus-visible-enhancer
source: localhost:8080/ovh/gpt-oss-120b
round: 69
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — focus-visible-enhancer

**Name:** `focus-visible-enhancer`
**When to apply:** На любом статическом лендинге, где есть интерактивные элементы (`<a>`, `<button>`, элементы с `role="button"`), но отсутствуют чёткие визуальные индикаторы фокуса – для соответствия WCAG 2.1 AA.
**Steps:**
1. Вставить в глобальный CSS блок `:focus-visible`‑стилей (см. `SAFE CSS`).
2. Добавить лёгкий полифил JS, который при первом нажатии клавиши Tab добавляет класс `js-keyboard` к `<html>` и переключает `:focus-visible`‑обработку в браузерах без поддержки.
3. При клике мышью/касании удалить класс `js-keyboard`, чтобы вернуть привычные стили hover.
4. Проверить, что существующие кастомные `:focus`‑стили не конфликтуют (при необходимости уточнить селекторы).
**SAFE CSS:**
```css
/* focus-visible‑enhancer */
html.js-keyboard a:focus-visible,
html.js-keyboard button:focus-visible,
html.js-keyboard [role="button"]:focus-visible,
html.js-keyboard .btn-primary:focus-visible {
outline: 2px solid var(--blue);
outline-offset: 2px;
box-shadow: 0 0 0 3px rgba(139,92,246,.3);
}
```
**SAFE JS:**
```js
/* focus-visible‑enhancer polyfill */
(function(){
const onKeyDown = e=>{ if(e.key==="Tab"){ document.documentElement.classList.add('js-keyboard'); } };
const onMouseDown = ()=>{ document.documentElement.classList.remove('js-keyboard'); };
window.addEventListener('keydown', onKeyDown, {once:true});
window.addEventListener('mousedown', onMouseDown);
window.addEventListener('touchstart', onMouseDown);
})();
```

## Когда применять
Улучшает доступность – пользователи клавиатуры сразу видят, какой элемент активен; повышает соответствие WCAG 2.1 AA, что может положительно сказаться на SEO и доверии.

## Проверка
Открыть страницу, нажать Tab — должен появиться синий outline на первой ссылке/кнопке; переключить на мышь — outline исчезает. Проверить в Chrome + Firefox.
