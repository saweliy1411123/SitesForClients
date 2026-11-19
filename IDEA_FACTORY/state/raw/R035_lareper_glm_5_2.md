# lareper/glm-5.2  2026-11-17 03:21:39
duration=55.6 error=- attempts=1

IDEA: SKILL — «Премиальный заголовок-градиент с анимацией текста» (gradient-heading-premium)
KNOB: SKILL — gradient-heading-premium
### Название
gradient-heading-premium
### Когда применять
Любой тёмный лендинг, где h1/h2 должны выглядеть «дорого»: премиальные услуги, портфолио, агентства. Применять к 1–2 ключевым заголовкам (h1 hero и один h2), не ко всем — иначе эффект дешевеет.
### Шаги
1. В `<head>`/`<style>` добавить блок SAFE CSS.
2. На целевой заголовок навесить класс `grad-heading` (например, h1 в hero).
3. Опционально: градиентный текст + подчёркивающая линия с медленной анимацией (уже есть базовый вариант на L116 — этот скилл даёт более тонкий, текстовый вариант с shimmer).
4. Проверить контраст: градиентные цвета должны давать ≥4.5:1 к фону `#0a0a0f`.
5. Обернуть в `@media (prefers-reduced-motion: reduce)` отключение анимации.
SAFE CSS:
```
.grad-heading{
  background:linear-gradient(120deg,#f5f3ff 0%,#a78bfa 35%,#67e8f9 70%,#f5f3ff 100%);
  background-size:200% 100%;
  -webkit-background-clip:text;
  background-clip:text;
  -webkit-text-fill-color:transparent;
  color:#a78bfa;
  animation:grad-shimmer 6s linear infinite;
}
@keyframes grad-shimmer{0%{background-position:0% 50%}100%{background-position:200% 50%}}
@media (prefers-reduced-motion: reduce){.grad-heading{animation:none}}
.grad-heading:focus-visible{outline:3px solid #67e8f9;outline-offset:4px;-webkit-text-fill-color:#f5f3ff}
```
EFFECT: h1 выглядит премиально без картинок и шрифтов-загрузок; усиливает восприятие «дорогого» оффера; нулевой вес (чистый CSS).
RISK: прозрачный текст на градиенте может потерять контраст на светлых/декоративных фонах — применять только на тёмном hero с проверкой контраста.
ROLLBACK: удалить класс `grad-heading` и блок CSS; либо `git checkout -- index.html`.
VERIFY: (1) открыть копию index.improved.html, убедиться что h1 читается целиком за 3 сек; (2) DevTools → Rendering → Emulate vision deficiencies → blurred vision — текст остаётся читаемым; (3) Lighthouse accessibility ≥95.
PRIORITY: 2 — чисто визуальный «премиум»-эффект с нулевой ценой по производительности, но не влияет на конверсию напрямую.

IDEA: SKILL — «Премиальный параллакс-наклон hero-фона» (parallax-hero-tilt)
KNOB: SKILL — parallax-hero-tilt
### Название
parallax-hero-tilt
### Когда применять
Тёмный лендинг с декоративными фоновыми слоями (blob-градиенты, частицы) в hero. Даёт ощущение глубины и «дорогого» сайта без библиотек.
### Шаги
1. Найти декоративные слои hero (`.blob.b1/.b2/.b3`, L96–98).
2. Добавить SAFE CSS (плавный transform, will-change).
3. Добавить SAFE JS: на `mousemove` по hero сдвигать слои с разными коэффициентами (parallax), только на устройствах с `matchMedia('(pointer:fine)')` и без `prefers-reduced-motion`.
4. На мобильных — статичный фон (параллакс отключён), чтобы не ж
