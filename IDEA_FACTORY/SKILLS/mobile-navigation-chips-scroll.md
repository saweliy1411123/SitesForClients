---
name: Mobile navigation chips scroll
source: localhost:8080/ovh/gpt-oss-120b
round: 133
status: proposed
portable: true
tags: [static-landing, portable]
---

# Mobile navigation chips scroll

SKILL — mobile-nav-chips
Name: mobile-nav-chips
When to apply: В медиазапросе `@media(max-width:720px)` заменить скрытие `.nav-links` на горизонтально прокручиваемый набор «чипов»‑якорей, чтобы пользователь мог быстро перейти к секциям.
SAFE CSS:
```css
@media(max-width:720px){
.nav-links{
display:flex;
overflow-x:auto;
-webkit-overflow-scrolling:touch;
gap:12px;
padding:8px;
scrollbar-width:none;
}
.nav-links::-webkit-scrollbar{display:none;}
.nav-links a{
flex:0 0 auto;
padding:6px 12px;
background:rgba(255,255,255,.08);
border-radius:9999px;
font-size:14px;
white-space:nowrap;
}
.nav-links a:focus-visible{
outline:2px solid var(--blue);
}
}
```
SAFE JS: *(не требуется)*

## Когда применять
Улучшает доступность навигации на мобильных, повышает вероятность быстрого перехода к нужному разделу, снижает показатель отказов.

## Проверка
В мобильном режиме (Chrome DevTools) открыть страницу, убедиться, что меню отображается как горизонтальная прокрутка, ссылки работают, а скролл плавный.

## SAFE JS
```js
*(не требуется)*
```
