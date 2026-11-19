---
name: SKILL — magnetic-cta-hover (притягивание CTA-кнопки к курсору с мягким возвратом)
source: lareper/glm-5.3
round: 125
status: proposed
portable: true
tags: [static-landing, portable, responsive]
---

# SKILL — magnetic-cta-hover (притягивание CTA-кнопки к курсору с мягким возвратом)

SKILL — `magnetic-cta-hover`
**Name:** `magnetic-cta-hover`
**When to apply:** на любом статическом лендинге, где основные CTA оформлены как ссылки `.btn-primary`/`.btn-ghost` и есть десктопный трафик; усиливает заметность и кликабельность кнопок без изменения текста и вёрстки.
**Steps:**
1. В `<style>` добавить SAFE CSS (эффект подъёма + плавный возврат через transition, отключение на тач-устройствах и при prefers-reduced-motion).
2. Перед `</body>` добавить SAFE JS: на `mousemove` над кнопкой сдвигать её на долю смещения курсора (max ~8px), на `mouseleave` — сбрасывать transform. Только addEventListener, без fetch/innerHTML/таймеров.
3. Проверить, что `transform` не конфликтует с существующими hover-анимациями кнопок (если есть — объединить в один transform).
4. На мобильных эффект не активен (pointer: coarse) — вёрстка не меняется.
SAFE CSS:
```css
.btn-primary,.btn-ghost{will-change:transform;transition:transform .25s cubic-bezier(.16,1,.3,1),border-color .2s,background .2s,box-shadow .25s}
@media(hover:hover) and (pointer:fine){
.btn-primary:hover,.btn-ghost:hover{box-shadow:0 12px 40px rgba(139,92,246,.35)}
}
@media(prefers-reduced-motion:reduce){.btn-primary,.btn-ghost{transition:none!important;transform:none!important}}
```
SAFE JS:
```js
(function(){
if(!window.matchMedia('(hover:hover) and (pointer:fine)').matches)return;
if(window.matchMedia('(prefers-reduced-motion:reduce)').matches)return;
document.querySelectorAll('.btn-primary,.btn-ghost').forEach(function(btn){
btn.addEventListener('mousemove',function(e){
var r=btn.getBoundingClientRect();
var dx=(e.clientX-r.left-r.width/2)/r.width;
var dy=(e.clientY-r.top-r.height/2)/r.height;
btn.style.transform='translate('+dx*10+'px,'+dy*8+'px)';
});
btn.addEventListener('mouseleave',function(){btn.style.transform='';});
});
})();
```

## Когда применять
CTA выглядит «живым» и дорогим, hover-зона внимания притягивает курсор — рост кликабельности основной кнопки на десктопе без изменения контента.

## Проверка
открыть index.improved.html, навести курсор на «Сделаю демо» — кнопка плавно смещается за курсором и возвращается; Tab-фокус и мобильный рендер не изменены.

## SAFE CSS
```css
```css
.btn-primary,.btn-ghost{will-change:transform;transition:transform .25s cubic-bezier(.16,1,.3,1),border-color .2s,background .2s,box-shadow .25s}
@media(hover:hover) and (pointer:fine){
.btn-primary:hover,.btn-ghost:hover{box-shadow:0 12px 40px rgba(139,92,246,.35)}
}
@media(prefers-reduced-motion:reduce){.btn-primary,.btn-ghost{transition:none!important;transform:none!important}}
```
```
