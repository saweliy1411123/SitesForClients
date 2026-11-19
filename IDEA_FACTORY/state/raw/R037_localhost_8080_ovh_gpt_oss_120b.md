# localhost:8080/ovh/gpt-oss-120b  2026-11-17 03:26:42
duration=25.7 error=- attempts=1

IDEA: Quick CTA‑path audit via one‑liner console script  
KNOB: METHOD – In Chrome DevTools console run the snippet:  
```js
(() => {
  const cta = '#contact';
  const links = [...document.querySelectorAll('a[href]')];
  const good = links.filter(l => l.getAttribute('href').startsWith(cta) || l.getAttribute('href').startsWith('tel:'));
  const bad = links.filter(l => !good.includes(l));
  console.table({total: links.length, good: good.length, bad: bad.length});
  console.group('Bad links');
  bad.forEach(l => console.log(l.outerHTML));
  console.groupEnd();
})();
```  
EFFECT: Instantly shows whether every clickable element routes to the intended contact CTA (or phone), exposing dead‑ends or misleading links before any code change.  
RISK: None – read‑only script, no DOM mutation.  
ROLLBACK: No file change; simply close the console.  
VERIFY: After running, confirm that `bad` count is 0; if not, note the offending selectors for later fixing.  
PRIORITY: 1 – ensures the core conversion funnel works; fastest sanity check.  

---  

IDEA: Data‑variant copy swap for instant A/B testing (CSS‑only toggle)  
KNOB: Add two sibling elements for any copy you want to test, e.g.:  
```html
<h2 data-variant="a" class="hero-sub">Сайт за 2 дня – клиенты в Яндексе</h2>
<h2 data-variant="b" class="hero-sub hidden">Получите готовый сайт за 48 ч – первые заявки уже сегодня</h2>
```  
Add CSS:  
```css
[data-variant] {display:none}
[data-variant].show {display:block}
```  
Add a 2‑line script at the end of `<body>`:  
```js
const v = location.hash.replace('#','')||'a';
document.querySelectorAll('[data-variant]').forEach(el=>el.classList.toggle('show',el.dataset.variant===v));
```  
EFFECT: Changing the URL hash to `#a` or `#b` instantly swaps copy without rebuilding or redeploying, enabling rapid A/B of headlines, sub‑headings, benefit lists, etc.  
RISK: Requires adding temporary markup; if left unchecked it may affect SEO (duplicate visible text).  
ROLLBACK: Delete the added `[data-variant]` elements, CSS block, and script (single git revert or file edit).  
VERIFY: Open page, append `#a` or `#b` in address bar, observe which variant is visible; confirm only one is shown.  
PRIORITY: 2 – low‑cost way to test messaging variations before committing to design.  

---  

IDEA: 48 px tap‑target overlay for fast mobile accessibility audit  
KNOB: Inject a temporary `<style>` block (or add to existing CSS) that draws a semi‑transparent 48 px circle around every interactive element:  
```css
/* DEBUG: tap‑target overlay – remove before launch */
a, button, [role="button"], .magnetic {
  position:relative;
}
a::after, button::after, [role="button"]::after, .magnetic::after{
  content:"";
  position:absolute;
  inset:-12px;               /* 48 px total (12 px each side) */
  border:2px dashed rgba(255,0,0,.4);
  border-radius:50%;
  pointer-events:none;
}
```  
EFFECT: Provides an immediate visual cue of whether clickable elements meet the recommended 48 px minimum touch area on mobile, catching spacing issues without manual measurement.  
RISK: Purely visual; does not affect functionality, but must be removed before production to avoid UI clutter.  
ROLLBACK: Delete the added CSS block (single git revert or file edit).  
VERIFY: Open the page on a mobile device or emulator, look for any red circles clipped by the viewport or overlapping other elements; adjust padding/margins accordingly.  
PRIORITY: 3 – improves mobile usability, a key conversion factor, but less urgent than funnel integrity.
