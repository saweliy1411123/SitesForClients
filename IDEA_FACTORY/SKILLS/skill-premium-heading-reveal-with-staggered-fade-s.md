---
name: SKILL — Premium Heading Reveal with Staggered Fade‑Scale
source: localhost:8080/ovh/gpt-oss-120b
round: 7
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Premium Heading Reveal with Staggered Fade‑Scale

METHOD: Create reusable skill **premium-heading-reveal**
```markdown
# premium-heading-reveal.md
## Название
Premium Heading Reveal with Staggered Fade‑Scale
## Когда применять
Для ключевых заголовков (h1, h2, h3) в hero‑секции и блоках‑преимуществ, где нужен эффект появления, подчеркивающий премиальность без JavaScript.
## Шаги
1. Добавьте к заголовкам класс `reveal-heading`.
2. Подключите файл `premium-heading-reveal.css` в `<head>`.
3. При необходимости задайте задержку через CSS‑переменную `--reveal-delay`.
## SAFE CSS:
```css
/* premium-heading-reveal.css */
.reveal-heading {
opacity: 0;
transform: translateY(20px) scale(0.96);
animation: headingReveal 0.8s forwards ease-out;
}
.reveal-heading[data-index] {
--reveal-delay: calc(var(--index, 0) * 0.12s);
animation-delay: var(--reveal-delay);
}
@keyframes headingReveal {
to {
opacity: 1;
transform: translateY(0) scale(1);
}
}
@media (prefers-reduced-motion: reduce) {
.reveal-heading {
animation: none;
opacity: 1;
transform: none;
}
}
```
## SAFE JS: *(optional – only to auto‑assign data-index for sequential headings)*
```js
/* premium-heading-reveal.js */
document.querySelectorAll('.reveal-heading').forEach((el, i) => {
el.dataset.index = i;
});
```
```

## Когда применять
Делает появление заголовков плавным и последовательным, усиливает восприятие «дорогого» дизайна, удерживает внимание пользователя в начале просмотра.

## Проверка
Откройте страницу, проверьте, что h1‑h3 появляются один за другим с лёгким подъёмом и увеличением; включите режим «reduce motion» — анимация должна исчезнуть, заголовки видны сразу.

## SAFE JS
```js
*(optional – only to auto‑assign data-index for sequential headings)*
```js
/* premium-heading-reveal.js */
document.querySelectorAll('.reveal-heading').forEach((el, i) => {
el.dataset.index = i;
});
```
```
```
