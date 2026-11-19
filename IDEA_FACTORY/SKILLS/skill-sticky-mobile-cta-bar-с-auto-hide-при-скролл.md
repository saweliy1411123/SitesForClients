---
name: SKILL — Sticky Mobile CTA Bar с auto-hide при скролле вниз
source: lareper/glm-5.2-fast-preview
round: 27
status: proposed
portable: true
tags: [static-landing, portable, responsive]
---

# SKILL — Sticky Mobile CTA Bar с auto-hide при скролле вниз

Название: **smart-sticky-cta**. Когда применять: любой одностраничный лендинг с одним якорным CTA, где мобильный пользователь должен дойти до кнопки без прокрутки к финальной секции. Шаги: (1) перед `</body>` вставить `<a href="#contact" class="sticky-cta-bar" aria-label="Получить бесплатное демо">Бесплатное демо — за 2 дня</a>`; (2) добавить SAFE CSS; (3) добавить SAFE JS — панель прячется при скролле вниз (не мешает чтению) и показывается при скролле вверх или после 600px прокрутки; (4) на десктопе (>1024px) скрыть через media query; (5) проверить, что не перекрывает footer (добавить `padding-bottom` к body на мобильных).
SAFE CSS:
.sticky-cta-bar{position:fixed;left:12px;right:12px;bottom:12px;z-index:90;display:none;justify-content:center;align-items:center;padding:14px 20px;border-radius:14px;background:linear-gradient(135deg,#8b5cf6,#6d28d9);color:#fff;font-weight:600;text-decoration:none;box-shadow:0 8px 24px rgba(139,92,246,.35);transform:translateY(120%);transition:transform .3s ease,opacity .3s ease;opacity:0}
.sticky-cta-bar.is-visible{transform:translateY(0);opacity:1}
@media(max-width:1024px){.sticky-cta-bar{display:flex}body{padding-bottom:72px}}
@media(prefers-reduced-motion:reduce){.sticky-cta-bar{transition:none;transform:none;opacity:1}}
@media(min-width:1025px){.sticky-cta-bar{display:none!important}}
SAFE JS:
(function(){var bar=document.querySelector('.sticky-cta-bar');if(!bar)return;var last=0;window.addEventListener('scroll',function(){var y=window.scrollY;if(y>600&&y<last){bar.classList.add('is-visible');}else if(y>last+10||y<=600){bar.classList.remove('is-visible');}last=y;},{passive:true});})();

## Когда применять
мобильный посетитель в любой момент в одном тапе от заявки; рост конверсии с мобильного трафика без изменения контента.

## Проверка
открыть копию на телефоне/DevTools iPhone SE (375px): проскроллить вниз — панель скрыта; вверх — появилась; Tab — фокус на ней виден; Lighthouse mobile — CLS не вырос.

## SAFE CSS
```css
.sticky-cta-bar{position:fixed;left:12px;right:12px;bottom:12px;z-index:90;display:none;justify-content:center;align-items:center;padding:14px 20px;border-radius:14px;background:linear-gradient(135deg,#8b5cf6,#6d28d9);color:#fff;font-weight:600;text-decoration:none;box-shadow:0 8px 24px rgba(139,92,246,.35);transform:translateY(120%);transition:transform .3s ease,opacity .3s ease;opacity:0}
.sticky-cta-bar.is-visible{transform:translateY(0);opacity:1}
@media(max-width:1024px){.sticky-cta-bar{display:flex}body{padding-bottom:72px}}
@media(prefers-reduced-motion:reduce){.sticky-cta-bar{transition:none;transform:none;opacity:1}}
@media(min-width:1025px){.sticky-cta-bar{display:none!important}}
```
