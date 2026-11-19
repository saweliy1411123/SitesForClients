---
name: SKILL — «Премиальный параллакс-наклон hero-фона» (parallax-hero-tilt)
source: lareper/glm-5.2
round: 35
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — «Премиальный параллакс-наклон hero-фона» (parallax-hero-tilt)

SKILL — parallax-hero-tilt
### Название
parallax-hero-tilt
### Когда применять
Тёмный лендинг с декоративными фоновыми слоями (blob-градиенты, частицы) в hero. Даёт ощущение глубины и «дорогого» сайта без библиотек.
### Шаги
1. Найти декоративные слои hero (`.blob.b1/.b2/.b3`, L96–98).
2. Добавить SAFE CSS (плавный transform, will-change).
3. Добавить SAFE JS: на `mousemove` по hero сдвигать слои с разными коэффициентами (parallax), только на устройствах с `matchMedia('(pointer:fine)')` и без `prefers-reduced-motion`.
4. На мобильных — статичный фон (параллакс отключён), чтобы не ж

## Когда применять


## Проверка


## SAFE JS
```js
на `mousemove` по hero сдвигать слои с разными коэффициентами (parallax), только на устройствах с `matchMedia('(pointer:fine)')` и без `prefers-reduced-motion`.
4. На мобильных — статичный фон (параллакс отключён), чтобы не ж
```
