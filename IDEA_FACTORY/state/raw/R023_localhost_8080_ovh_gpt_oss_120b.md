# localhost:8080/ovh/gpt-oss-120b  2026-11-17 02:46:38
duration=19.7 error=- attempts=1

IDEA: Tab‑order & focus‑visibility audit (quick keyboard test)  
KNOB: METHOD: Add a temporary overlay `<div class="focus‑audit" style="position:fixed;bottom:0;right:0;padding:4px;background:#000;color:#fff;font-size:12px;z-index:9999">Press Tab to check focus order</div>` and ensure every interactive element (`<a>`, `<button>`, `[role="button"]`) has a visible `:focus` style (e.g., `outline:2px solid var(--blue);`). No code changes required beyond this visual cue.  
EFFECT: Confirms that users navigating via keyboard can see where focus moves, preventing drop‑offs for accessibility‑oriented visitors and improving WCAG 2.1 AA compliance.  
RISK: Minimal – only adds a non‑intrusive visual hint; may slightly shift layout if focus outline wasn’t previously defined.  
ROLLBACK: Delete the overlay `<div>` and the added `:focus` rule (git checkout index.html).  
VERIFY: Open the page locally, press Tab repeatedly, watch the overlay and ensure each focusable element receives a clear outline; note any missing outlines or illogical order (e.g., jumping from hero CTA to footer). Completed in ≤2 min.  
PRIORITY: 1 – Accessibility fixes have high impact on conversion and legal compliance with virtually no cost.  

---  

IDEA: CSS Coverage audit for render‑blocking/unused styles  
KNOB: METHOD: In Chrome DevTools open **Coverage** panel (Ctrl Shift P → “Show Coverage”), click **Start instrumenting coverage**, reload the page, then stop after load. Record total CSS bytes vs. used bytes. If unused > 15 % add a comment `/* TODO: remove unused selectors */` next to the block.  
EFFECT: Identifies dead CSS that inflates payload, allowing quick pruning to improve LCP and CLS without altering markup.  
RISK: None – analysis‑only; removing code later must be done carefully to avoid breaking styles.  
ROLLBACK: No file changes made; if later you delete selectors, revert with `git checkout index.html`.  
VERIFY: Run the Coverage scan, note the percentage of unused CSS; if > 15 % log the selectors for removal. The whole process takes ≤5 min.  
PRIORITY: 2 – Speed gains directly affect Core Web Vitals, boosting SEO and user retention, but impact is moderate compared to accessibility.  

---  

IDEA: URL‑parameter‑driven copy toggle for instant A/B testing  
KNOB: METHOD: Add a tiny script at the end of `<body>`:  

```html
<script>
  const params = new URLSearchParams(location.search);
  if (params.get('v') === '2') {
    document.querySelector('h1').textContent = 'Сайт для вашего бизнеса — через 2 дня, клиенты находят вас в Яндексе';
    document.querySelector('.hero-note b').textContent = 'демо‑макет с вашими услугами и ценами за 2 дня';
  }
</script>
```

No other files changed.  
EFFECT: Enables a zero‑deployment A/B test: compare original copy (v=1) vs. revised copy (v=2) by simply changing the URL, measuring click‑through on the CTA via console or screen‑recording.  
RISK: Requires manual URL change; if left in production it could expose test copy to users unintentionally.  
ROLLBACK: Remove the script block (git checkout index.html).  
VERIFY: Open `index.html?v=2` locally, confirm the h1 and hero‑note text have swapped; click the CTA and observe any difference in click count (log via `console.log` inside the script). Takes ≤3 min.  
PRIORITY: 3 – Provides fast, data‑driven copy validation with negligible overhead; lower priority than accessibility and performance but valuable for conversion optimisation.
