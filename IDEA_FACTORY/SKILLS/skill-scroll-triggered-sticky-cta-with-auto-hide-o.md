---
name: SKILL — Scroll‑Triggered Sticky CTA with Auto‑Hide on Down‑Scroll
source: localhost:8080/ovh/gpt-oss-120b
round: 6
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Scroll‑Triggered Sticky CTA with Auto‑Hide on Down‑Scroll

METHOD: Add a sticky call‑to‑action bar that stays visible at the bottom of the viewport, automatically hides when the user scrolls down and re‑appears on scroll up. Includes pure CSS for positioning and a tiny, safe JS snippet for scroll direction detection.
SAFE CSS:
```css
/* Sticky CTA container */
.sticky-cta {
position: fixed;
inset-block-end: 0;
inset-inline-start: 0;
inset-inline-end: 0;
background: #8b5cf6;
color: #fff;
padding: 12px 1rem;
text-align: center;
font-size: 1rem;
font-weight: 600;
transform: translateY(0);
transition: transform 0.3s ease-out;
z-index: 1000;
}
/* Hidden state – moved down out of view */
.sticky-cta.hidden {
transform: translateY(120%);
}
/* CTA link styling (preserve existing button look) */
.sticky-cta a {
color: inherit;
text-decoration: underline;
}
```
SAFE JS:
```js
/* Scroll‑direction detector – toggles .hidden on .sticky-cta */
(() => {
let lastY = window.scrollY;
const cta = document.querySelector('.sticky-cta');
if (!cta) return;
window.addEventListener('scroll', () => {
const currentY = window.scrollY;
if (currentY > lastY + 10) {
cta.classList.add('hidden');   // scrolling down → hide
} else if (currentY < lastY - 10) {
cta.classList.remove('hidden'); // scrolling up → show
}
lastY = currentY;
});
})();
```

## Когда применять
Keeps the primary CTA (“Сделаю демо …”) constantly in sight, increasing click‑through rates while staying unobtrusive during content consumption.

## Проверка
1) Insert `<div class="sticky-cta"><a href="#contact">Сделаю демо бесплатно →</a></div>` before `</body>`. 2) Load page, scroll down – CTA should slide out of view. 3) Scroll up – CTA slides back in. 4) Test on mobile viewport (375 px) to ensure no overlap with native UI.
