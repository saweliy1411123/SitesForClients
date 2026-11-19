---
name: SKILL — премиум-база + 3D
source: baseline
round: 0
status: proposed
portable: true
tags: [static-landing, portable, animation, 3d, responsive]
---

# SKILL — премиум-база + 3D

Базовый переносимый слой: типографика, анимации появления, стеклянные карточки, 3D-наклон по hover, доступный фокус, мобильный запас и лёгкий scroll-reveal.

## Когда применять
К любому статическому лендингу как безопасный слой поверх существующих стилей. Тексты и структура не меняются.

## SAFE CSS
```css
:root { --premium-ease: cubic-bezier(.2,.8,.2,1); --premium-violet: #8b5cf6; }
html { scroll-behavior: smooth; }
body { -webkit-font-smoothing: antialiased; text-rendering: optimizeLegibility; }
.wrap { max-width: 1180px; }
h1,h2,h3 { letter-spacing: -.035em; }
h1 { font-size: clamp(2.6rem,6vw,4.8rem); line-height: 1.03; }
.lead { font-size: clamp(1.05rem,1.8vw,1.25rem); line-height: 1.7; opacity: .88; }
@keyframes factoryRise { from { opacity: 0; transform: translateY(24px); } to { opacity: 1; transform: none; } }
.hero h1 { animation: factoryRise .9s var(--premium-ease) both; }
.hero .lead,.hero-note { animation: factoryRise .9s .12s var(--premium-ease) both; }
.btn-primary,.nav-cta { border-radius: 999px; transition: transform .25s var(--premium-ease), box-shadow .25s var(--premium-ease); }
.btn-primary:hover,.nav-cta:hover { transform: translateY(-2px); box-shadow: 0 18px 48px rgba(139,92,246,.3); }
.step,.stack-card,.proof-item,.cover,.work-placeholder { border: 1px solid rgba(255,255,255,.09); border-radius: 22px; transform-style: preserve-3d; perspective: 1000px; transition: transform .45s var(--premium-ease), border-color .35s, box-shadow .45s; }
.step:hover,.stack-card:hover,.proof-item:hover,.cover:hover,.work-placeholder:hover { transform: rotateY(-6deg) rotateX(4deg) translateZ(14px); border-color: rgba(139,92,246,.5); box-shadow: 0 26px 70px rgba(0,0,0,.35); }
.shine::after { content: ""; position: absolute; inset: 0; border-radius: inherit; background: linear-gradient(115deg, transparent 35%, rgba(255,255,255,.14) 50%, transparent 65%); transform: translateX(-120%); transition: transform .8s var(--premium-ease); pointer-events: none; }
.shine:hover::after { transform: translateX(120%); }
a:focus-visible,button:focus-visible { outline: 2px solid #a78bfa; outline-offset: 3px; }
::selection { background: rgba(139,92,246,.35); }
@media(max-width:720px){ section { padding: 64px 0; } .wrap { padding: 0 18px; } .step:hover,.stack-card:hover,.proof-item:hover,.cover:hover { transform: none; } }
@media(prefers-reduced-motion:reduce){ * { animation-duration: .01ms !important; transition-duration: .01ms !important; } }
```

## SAFE JS
```js
var els = document.querySelectorAll('.reveal');
els.forEach(function(el){
  el.style.transition = 'opacity .7s ease, transform .7s ease';
  el.style.opacity = '0';
  el.style.transform = 'translateY(18px)';
});
var io = new IntersectionObserver(function(entries){
  entries.forEach(function(entry){
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'none';
      io.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });
els.forEach(function(el){ io.observe(el); });
```

## Проверка
Сравнить `git diff --no-index index.html index.improved.html`, открыть копию в браузере, проверить мобильную ширину и `prefers-reduced-motion`.
