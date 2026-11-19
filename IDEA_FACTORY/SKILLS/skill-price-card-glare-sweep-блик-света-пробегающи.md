---
name: SKILL — price-card-glare-sweep (блик света, пробегающий по премиум-карточке цены при hover)
source: lareper/glm-5.3-prime
round: 105
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — price-card-glare-sweep (блик света, пробегающий по премиум-карточке цены при hover)

SKILL — price-card-glare-sweep
Name: `price-card-glare-sweep`
When to apply: на любом лендинге, где есть одна выделенная карточка цены (`.price-card`) и нужно ощущение «дорогого» продукта без картинок и библиотек.
Steps:
1. Убедиться, что карточка имеет `position:relative` и `overflow:hidden`.
2. Добавить псевдоэлемент-блик, который по умолчанию сдвинут за пределы карточки.
3. На hover/focus-within блик плавно проезжает по диагонали.
4. Обернуть анимации в `@media (prefers-reduced-motion: no-preference)`.
5. Проверить, что блик не перекрывает текст (pointer-events нет у псевдоэлементов по умолчанию — ок).
SAFE CSS:
```css
.price-card{position:relative;overflow:hidden}
@media (prefers-reduced-motion: no-preference){
.price-card::after{
content:'';position:absolute;top:-60%;left:-80%;
width:60%;height:220%;
background:linear-gradient(105deg,transparent 30%,rgba(255,255,255,.14) 48%,rgba(255,255,255,.05) 55%,transparent 70%);
transform:rotate(8deg) translateX(0);pointer-events:none;transition:transform .9s cubic-bezier(.22,.61,.36,1)}
.price-card:hover::after,.price-card:focus-within::after{transform:rotate(8deg) translateX(320%)}
}
```

## Когда применять
карточка цены воспринимается как премиальный объект; hover-микровзаимодействие удерживает внимание на главном оффере, не отвлекая от текста.

## Проверка
открыть страницу, навести курсор на `.price-card` — блик должен проехать один раз; проверить Tab-фокус на кнопке внутри карточки; включить эмуляцию prefers-reduced-motion в DevTools → Rendering и убедиться, что анимации нет.
