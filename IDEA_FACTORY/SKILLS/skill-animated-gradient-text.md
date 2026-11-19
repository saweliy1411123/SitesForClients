---
name: SKILL — Animated Gradient Text
source: localhost:8080/ovh/gpt-oss-120b
round: 14
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Animated Gradient Text

METHOD: Создайте класс `.gradient-text` с анимированным градиентом через `background-clip` и `@keyframes`. Применяется к элементам, где нужен премиальный визуальный акцент (например, к слову «за 2 дня» в h1).
SAFE CSS:
```css
.gradient-text {
background: linear-gradient(45deg, #8b5cf6, #ec4899, #f59e0b);
background-size: 300% 300%;
-webkit-background-clip: text;
color: transparent;
animation: gradientShift 8s ease infinite;
}
@keyframes gradientShift {
0%   { background-position: 0% 50%; }
50%  { background-position: 100% 50%; }
100% { background-position: 0% 50%; }
}
```

## Когда применять
Привлекает внимание к ключевому сообщению, усиливает ощущение «дорогого» бренда без дополнительных изображений.

## Проверка
Открыть страницу, убедиться, что градиент плавно меняется; проверить в Chrome DevTools, отключив `prefers-reduced-motion` (должна работать).
