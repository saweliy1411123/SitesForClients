---
name: SKILL — shimmer-placeholder
source: localhost:8080/ovh/gpt-oss-120b
round: 167
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — shimmer-placeholder

**Name:** `shimmer-placeholder`
**When to apply:** На страницах с изображениями, которые загружаются лениво (`loading="lazy"`), особенно при медленном соединении, чтобы уменьшить визуальное «мигание» контента.
**Steps:**
1. Обернуть каждое `<img>` в контейнер `<div class="shimmer-wrapper"><img …></div>`.
2. Добавить атрибут `loading="lazy"` к `<img>` (если его нет).
3. В CSS задать анимированный градиент‑шимер для `.shimmer-wrapper` и скрыть изображение до полной загрузки (`opacity:0`).
4. Добавить небольшую JS‑функцию, которая после события `load` у изображения удаляет класс `shimmer-active` у родителя, делая изображение видимым.
**SAFE CSS:**
```css
.shimmer-wrapper{
position:relative;
overflow:hidden;
background:#f0f0f0;
}
.shimmer-wrapper::before{
content:"";
position:absolute;
inset:0;
background:linear-gradient(90deg,
#f0f0f0 0%,
#e0e0e0 40%,
#f0f0f0 80%);
background-size:200% 100%;
animation:shimmer 1.5s infinite;
}
.shimmer-wrapper img{
display:block;
width:100%;
height:auto;
opacity:0;
transition:opacity .3s ease-in;
}
.shimmer-wrapper.loaded img{
opacity:1;
}
@keyframes shimmer{
0%{background-position: -200% 0;}
100%{background-position: 200% 0;}
}
```
**SAFE JS:**
```js
document.querySelectorAll('.shimmer-wrapper img').forEach(img=>{
img.addEventListener('load',()=> {
img.parentElement.classList.add('loaded');
});
});
```

## Когда применять
Пользователь видит плавный шимер‑заполнитель вместо пустого места, улучшая восприятие скорости загрузки и снижая показатель отказов.

## Проверка
Открыть страницу в медленном режиме (DevTools → Network → Throttling → Slow 3G), убедиться, что до полной загрузки изображения показывается анимированный шимер, после загрузки изображение появляется без мерцаний.

## SAFE JS
```js
**
```js
document.querySelectorAll('.shimmer-wrapper img').forEach(img=>{
img.addEventListener('load',()=> {
img.parentElement.classList.add('loaded');
});
});
```
```
