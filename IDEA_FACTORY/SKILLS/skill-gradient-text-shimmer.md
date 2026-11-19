---
name: SKILL — gradient-text-shimmer
source: localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct
round: 139
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — gradient-text-shimmer


**Name:** gradient-text-shimmer
**When to apply:** На любом лендинге, где заголовок h1 содержит градиентный текст.
**SAFE CSS:**
```css
.grad-text {
background: linear-gradient(90deg, #8b5cf6, #34d399);
-webkit-background-clip: text;
background-clip: text;
color: transparent;
animation: shimmer 5s infinite;
}
@keyframes shimmer {
0% {
background-position: 0 0;
}
100% {
background-position: 100% 0;
}
}
```
**SAFE JS:** Нет

## Когда применять
Добавляет анимированный градиентный блеск к тексту заголовка h1, делая его более привлекательным и заметным.

## Проверка
Проверить визуально, что градиентный блеск появился на заголовке h1 и анимация работает корректно.

## SAFE JS
```js
** Нет
```
