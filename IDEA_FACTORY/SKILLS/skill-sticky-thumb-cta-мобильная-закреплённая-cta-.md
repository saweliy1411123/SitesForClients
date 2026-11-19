---
name: SKILL — sticky-thumb-cta (мобильная закреплённая CTA с safe-area и авто-скрытием у финального блока)
source: lareper/glm-5.2
round: 76
status: proposed
portable: true
tags: [static-landing, portable, responsive]
---

# SKILL — sticky-thumb-cta (мобильная закреплённая CTA с safe-area и авто-скрытием у финального блока)

Название: `sticky-thumb-cta`. Когда применять: на любом статическом лендинге, где главный CTA — якорная ссылка, а конверсия теряется на мобильных (CTA только вверху и в конце длинной страницы). Шаги: (1) В конец `<body>` добавить `<a class="sticky-cta" href="#contact">Получить демо бесплатно</a>` (якорь заменить на реальный id финальной секции). (2) Вставить SAFE CSS. (3) По желанию — SAFE JS, чтобы кнопка скрывалась, когда финальный CTA уже виден. (4) Проверить на 360px, что кнопка не перекрывает контент.
SAFE CSS:
.sticky-cta{position:fixed;left:16px;right:16px;bottom:calc(12px + env(safe-area-inset-bottom));z-index:999;display:flex;justify-content:center;align-items:center;padding:15px 20px;border-radius:14px;background:linear-gradient(135deg,#8b5cf6,#6d4aff);color:#fff;font-weight:700;font-size:16px;text-decoration:none;box-shadow:0 10px 30px rgba(139,92,246,.45);transform:translateY(0);transition:transform .3s ease,opacity .3s ease}
.sticky-cta:hover,.sticky-cta:focus-visible{transform:translateY(-2px);box-shadow:0 14px 40px rgba(139,92,246,.6)}
.sticky-cta.is-hidden{transform:translateY(120%);opacity:0;pointer-events:none}
@media (min-width:900px){.sticky-cta{left:auto;right:24px;bottom:24px;padding:13px 22px;border-radius:999px}}
@media (prefers-reduced-motion: reduce){.sticky-cta{transition:none}}
SAFE JS:
(function(){var cta=document.querySelector('.sticky-cta');var final=document.querySelector('#contact');if(!cta||!final)return;if(!('IntersectionObserver' in window))return;new IntersectionObserver(function(e){cta.classList.toggle('is-hidden',e[0].isIntersecting)},{threshold:0.2}).observe(final);})();

## Когда применять
CTA всегда под большим пальцем на мобильных — меньше потери пользователей на длинном скролле, рост переходов к заявке; на десктопе — компактная круглая кнопка, не мешает.

## Проверка
(1) Скопировать файл, вставить блок, открыть в Chrome. (2) Toggle device toolbar → 360px: кнопка видна, скролл до финального CTA — кнопка исчезает (JS) или перекрытие отсутствует. (3) Tab: фокус-кольцо на кнопке видно. (4) Вернуться: git checkout.

## SAFE CSS
```css
.sticky-cta{position:fixed;left:16px;right:16px;bottom:calc(12px + env(safe-area-inset-bottom));z-index:999;display:flex;justify-content:center;align-items:center;padding:15px 20px;border-radius:14px;background:linear-gradient(135deg,#8b5cf6,#6d4aff);color:#fff;font-weight:700;font-size:16px;text-decoration:none;box-shadow:0 10px 30px rgba(139,92,246,.45);transform:translateY(0);transition:transform .3s ease,opacity .3s ease}
.sticky-cta:hover,.sticky-cta:focus-visible{transform:translateY(-2px);box-shadow:0 14px 40px rgba(139,92,246,.6)}
.sticky-cta.is-hidden{transform:translateY(120%);opacity:0;pointer-events:none}
@media (min-width:900px){.sticky-cta{left:auto;right:24px;bottom:24px;padding:13px 22px;border-radius:999px}}
@media (prefers-reduced-motion: reduce){.sticky-cta{transition:none}}
```

## SAFE JS
```js
(function(){var cta=document.querySelector('.sticky-cta');var final=document.querySelector('#contact');if(!cta||!final)return;if(!('IntersectionObserver' in window))return;new IntersectionObserver(function(e){cta.classList.toggle('is-hidden',e[0].isIntersecting)},{threshold:0.2}).observe(final);})();
```
