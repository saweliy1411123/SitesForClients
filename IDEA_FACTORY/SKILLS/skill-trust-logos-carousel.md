---
name: SKILL — trust-logos-carousel
source: localhost:8080/ovh/gpt-oss-120b
round: 55
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — trust-logos-carousel

**Name:** `trust-logos-carousel`
**When to apply:** На любой лендинг, где требуется показать логотипы партнёров/клиентов для повышения доверия.
**Steps:**
1. Вставить после секции цены (`.price-card`) блок‑контейнер:
```html
<section id="trust" class="trust" role="region" aria-label="Нам доверяют">
<h2 class="reveal">Нам доверяют</h2>
<div class="trust-carousel" aria-roledescription="carousel">
<!-- повторить для каждого логотипа -->
<div class="trust-item"><img src="logo1.svg" alt="Логотип партнёра 1" loading="lazy"></div>
<div class="trust-item"><img src="logo2.svg" alt="Логотип партнёра 2" loading="lazy"></div>
<div class="trust-item"><img src="logo3.svg" alt="Логотип партнёра 3" loading="lazy"></div>
<!-- … -->
</div>
</section>
```
2. Добавить в `<head>` (или в конец `<style>`) следующий CSS (SAFE CSS):
SAFE CSS:
```css
.trust {padding:80px 0;background:#111;color:#fff;text-align:center}
.trust h2 {margin-bottom:40px;font-size:clamp(28px,5vw,36px)}
.trust-carousel {
display:flex;gap:40px;overflow-x:auto;scroll-snap-type:x mandatory;
-webkit-overflow-scrolling:touch;scroll-behavior:smooth;
}
.trust-item {
flex:0 0 auto;scroll-snap-align:center;opacity:.6;transition:opacity .3s;
}
.trust-item:hover,
.trust-item:focus-within {opacity:1}
.trust-item img {max-height:48px;max-width:120px;display:block;margin:auto}
/* hide scrollbar in WebKit */
.trust-carousel::-webkit-scrollbar {display:none}
```
3. (Опционально) Добавить небольшую JS‑анимацию автопрокрутки, но это не требуется – пользователь может скроллить вручную.

## Когда применять
Показ логотипов партнёров усиливает социальное доказательство, повышает доверие и, как правило, улучшает конверсию CTA‑кнопок.

## Проверка
Открыть страницу в браузере, убедиться, что блок «Нам доверяют» появился, логотипы отображаются, можно прокручивать горизонтально, и при наведении/фокусе они становятся ярче. Проверить, что на мобильных ширина 360 px логотипы не вылезают за экран.
