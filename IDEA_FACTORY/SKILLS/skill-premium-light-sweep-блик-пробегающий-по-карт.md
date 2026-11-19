---
name: SKILL — Premium Light Sweep (блик, пробегающий по карточке при hover)
source: lareper/glm-5.2
round: 28
status: proposed
portable: true
tags: [static-landing, portable, responsive]
---

# SKILL — Premium Light Sweep (блик, пробегающий по карточке при hover)

SKILL — light-sweep-card
### Название
light-sweep-card
### Когда применять
Любой лендинг с карточками (демо-концепты, тарифы, шаги), где нужен «дорогой» эффект света без библиотек. Применять к `.demo-card`, `.price-card`, `.step` и подобным блочным элементам.
### Шаги
1. Добавить CSS ниже в `<style>` (или в копию index.improved.html).
2. Убедиться, что у карточки есть `position:relative; overflow:hidden`.
3. Проверить на мобильном: эффект только по hover/focus-within, на тач-устройствах не мешает.
SAFE CSS:
.card-sweep{position:relative;overflow:hidden}
.card-sweep::after{content:"";position:absolute;top:0;left:-120%;width:60%;height:100%;background:linear-gradient(105deg,transparent,rgba(255,255,255,.14),transparent);transform:skewX(-18deg);transition:left .7s ease;pointer-events:none}
.card-sweep:hover::after,.card-sweep:focus-within::after{left:130%}
@media (prefers-reduced-motion:reduce){.card-sweep::after{display:none}}

## Когда применять
премиальное ощущение «дорогого» сайта, карточки реагируют на курсор — выше воспринимаемая ценность услуги.

## Проверка
открыть index.improved.html, навести курсор на карточку демо — блик пробегает слева направо за ~0.7 с; проверить Tab-фокус тоже вызывает блик.

## SAFE CSS
```css
.card-sweep{position:relative;overflow:hidden}
.card-sweep::after{content:"";position:absolute;top:0;left:-120%;width:60%;height:100%;background:linear-gradient(105deg,transparent,rgba(255,255,255,.14),transparent);transform:skewX(-18deg);transition:left .7s ease;pointer-events:none}
.card-sweep:hover::after,.card-sweep:focus-within::after{left:130%}
@media (prefers-reduced-motion:reduce){.card-sweep::after{display:none}}
```
