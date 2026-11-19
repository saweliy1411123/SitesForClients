---
name: SKILL — scroll-snap-carousel
source: localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct
round: 62
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — scroll-snap-carousel


**Name:** `scroll-snap-carousel`
**When to apply:** На лендингах с крупными визуальными блоками.
**SAFE CSS:**
```css
.scroll-snap-carousel {
display: flex;
flex-wrap: nowrap;
overflow-x: auto;
scroll-snap-type: x mandatory;
}
.scroll-snap-carousel > * {
flex: 0 0 100%;
height: 100vh;
scroll-snap-align: start;
}
```
**SAFE JS:** (нет)

## Когда применять
Улучшение пользовательского опыта за счет визуальной карусели.

## Проверка
Проверить визуальное качество и скорость загрузки карусели.

## SAFE JS
```js
** (нет)
```
