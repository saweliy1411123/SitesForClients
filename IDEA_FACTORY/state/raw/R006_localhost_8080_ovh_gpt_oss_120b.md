# localhost:8080/ovh/gpt-oss-120b  2026-11-17 01:56:51
duration=23.3 error=- attempts=1

IDEA: SKILL — Accessible Focus Outline for Interactive Elements  
KNOB: METHOD: Add a reusable accessibility skill that globally applies a high‑contrast focus‑visible outline to all interactive elements (links, buttons, and any element with `role="button"`).  
SAFE CSS:  
```css
/* Accessible focus outline – applies only when user navigates via keyboard */
a:focus-visible,
button:focus-visible,
[role="button"]:focus-visible {
  outline: 3px solid #8b5cf6;   /* brand accent */
  outline-offset: 4px;
  box-shadow: 0 0 0 2px #fff;  /* ensures visibility on dark backgrounds */
}

/* Ensure that focus styles are not overridden by existing :focus rules */
a:focus,
button:focus,
[role="button"]:focus {
  outline: none;
}
```  
EFFECT: Improves keyboard navigation visibility, boosting accessibility scores (WCAG 2.1 AA) and increasing conversion among users who rely on keyboard or assistive tech.  
RISK: Minimal – only adds visual styling; could clash with existing custom focus styles if they use `!important`.  
ROLLBACK: `git checkout -- index.html` (or remove the added CSS block).  
VERIFY: Open the page, press **Tab** to cycle through links/buttons; confirm a bright purple outline appears only on keyboard focus, not on mouse click. Use Chrome DevTools → Accessibility audit to see no violations.  
PRIORITY: 1 – quick, zero‑dependency win that immediately lifts accessibility compliance.  
SKILL: Accessible Focus Outline  

---  

IDEA: SKILL — Scroll‑Triggered Sticky CTA with Auto‑Hide on Down‑Scroll  
KNOB: METHOD: Add a sticky call‑to‑action bar that stays visible at the bottom of the viewport, automatically hides when the user scrolls down and re‑appears on scroll up. Includes pure CSS for positioning and a tiny, safe JS snippet for scroll direction detection.  
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
EFFECT: Keeps the primary CTA (“Сделаю демо …”) constantly in sight, increasing click‑through rates while staying unobtrusive during content consumption.  
RISK: Requires a single `.sticky-cta` element in the markup; if omitted the script does nothing. JS is lightweight (< 1 KB) and safe‑by‑design (no external calls).  
ROLLBACK: Delete the added `<div class="sticky-cta">…</div>` block, the CSS rules, and the JS snippet; or `git checkout -- index.html`.  
VERIFY: 1) Insert `<div class="sticky-cta"><a href="#contact">Сделаю демо бесплатно →</a></div>` before `</body>`. 2) Load page, scroll down – CTA should slide out of view. 3) Scroll up – CTA slides back in. 4) Test on mobile viewport (375 px) to ensure no overlap with native UI.  
PRIORITY: 2 – higher impact on conversions but slightly more effort; suitable after the quick accessibility win.  
SKILL: Scroll‑Triggered Sticky CTA
