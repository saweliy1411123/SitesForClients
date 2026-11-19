---
name: SKILL — hero-light-sweep (пробегающий световой блик по hero-панели, «дорогой» свет)
source: lareper/glm-5.2
round: 112
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — hero-light-sweep (пробегающий световой блик по hero-панели, «дорогой» свет)

SKILL — hero-light-sweep
Name: `hero-light-sweep`
When to apply: на любом статическом лендинге, где hero-секция имеет тёмный/градиентный фон или стеклянную панель — добавить мягкий диагональный световой блик, медленно проходящий по панели, чтобы первый экран выглядел премиально. Без внешних библиотек, чистый CSS.
Steps:
1. В hero-секции найти контейнер первого экрана (`.hero .wrap` или аналогичный) и добавить внутрь первым ребёнком `<div class="light-sweep" aria-hidden="true"></div>`.
2. Добавить CSS из блока SAFE CSS ниже (в конец `<style>`).
3. Убедиться, что у `.hero` есть `position:relative; overflow:hidden;`.
4. Проверить на мобильном: блик не должен перекрывать текст (z-index ниже контента).
SAFE CSS:
```css
.hero{position:relative;overflow:hidden}
.light-sweep{
position:absolute;inset:-20%;
pointer-events:none;z-index:0;
background:linear-gradient(115deg,
transparent 42%,
rgba(255,255,255,.06) 48%,
rgba(255,255,255,.14) 50%,
rgba(255,255,255,.06) 52%,
transparent 58%);
transform:translateX(-60%);
animation:lightSweep 9s ease-in-out infinite;
will-change:transform;
}
@keyframes lightSweep{
0%{transform:translateX(-60%) rotate(0deg)}
50%{transform:translateX(60%) rotate(0deg)}
100%{transform:translateX(-60%) rotate(0deg)}
}
@media (prefers-reduced-motion: reduce){
.light-sweep{animation:none;opacity:.5;transform:translateX(0)}
}
```
(контент hero при необходимости поднять: `.hero .wrap{position:relative;z-index:1}`)

## Когда применять
hero выглядит «дорогим» без картинок и библиотек; свет задаёт ощущение премиума, повышая воспринимаемую ценность услуги «лендинг за 2 дня» — визуальная метафора продукта на самом сайте.

## Проверка
(1) открыть index.improved.html, 10 секунд наблюдать hero — блик проходит плавно, текст читаем; (2) DevTools → Rendering → Emulate prefers-reduced-motion: reduce — анимация отключается; (3) Lighthouse Performance до/после — CLS = 0, FPS на мобильном эмуляторе ≥ 55.
