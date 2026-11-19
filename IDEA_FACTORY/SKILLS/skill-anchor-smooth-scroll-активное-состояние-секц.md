---
name: SKILL — «Anchor-smooth-scroll + активное состояние секций» (переносимая навигация к CTA)
source: lareper/glm-5.2
round: 34
status: proposed
portable: true
tags: [static-landing, portable, responsive]
---

# SKILL — «Anchor-smooth-scroll + активное состояние секций» (переносимая навигация к CTA)

Название: **smooth-anchor-nav**. Когда применять: любой одностраничный лендинг, где CTA и навигация — якорные ссылки (`href="#contact"` и т.п.), а секции длинные.
Шаги:
1. Убедиться, что у целевой секции есть `id` и `tabindex="-1"` (для фокуса при переходе).
2. В CSS включить плавный скролл с уважением к reduced-motion (см. SAFE CSS).
3. Добавить `scroll-margin-top` целевым секциям, чтобы sticky-шапка/панель не перекрывала заголовок.
4. SAFE JS: после клика по якорю передать фокус на целевую секцию (доступность для клавиатуры и скрин-ридеров).
5. Проверка: пройтись по странице только Tab+Enter — все якоря ведут к цели, фокус не «теряется», заголовок цели не уходит под sticky-элементы.
SAFE CSS:
```css
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
section[id]{scroll-margin-top:72px}
section[id]:focus{outline:none}
```
SAFE JS:
```js
document.querySelectorAll('a[href^="#"]').forEach(function(a){
a.addEventListener('click',function(){
var

## Когда применять


## Проверка


## SAFE CSS
```css
```css
html{scroll-behavior:smooth}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
section[id]{scroll-margin-top:72px}
section[id]:focus{outline:none}
```
```

## SAFE JS
```js
после клика по якорю передать фокус на целевую секцию (доступность для клавиатуры и скрин-ридеров).
5. Проверка: пройтись по странице только Tab+Enter — все якоря ведут к цели, фокус не «теряется», заголовок цели не уходит под sticky-элементы.
```
