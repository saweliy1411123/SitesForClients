# localhost:8081/big_only  2026-11-17 08:33:35
duration=17.9 error=- attempts=1

IDEA: Quick Variant Toggle Visual A/B Test  
KNOB: METHOD: inject script that reads `location.search` for `?v=`; if present adds class `.variant-a` or `.variant-b` to `<body>`; CSS for each variant defined inline or in `<style>`; toggle via `history.replaceState` and log current variant.  
EFFECT: Enables instant visual comparison of two design variants without rebuilding or redeploying, supporting rapid hypothesis validation.  
RISK: Requires manual creation of variant CSS; if selectors overlap existing styles may produce unexpected layout glitches.  
ROLLBACK: Remove the injected script and any `<style>` blocks; delete added classes from `<body>` (git checkout -- index.html).  
VERIFY: Open DevTools console, run the script, confirm `<body>` receives the correct class, observe changed styles, and capture a screenshot within 2 minutes.  
PRIORITY: 1 – fastest, lowest‑risk way to test visual changes directly on the landing page.  

IDEA: Click‑through Tracking per Variant via URL Parameter  
KNOB: METHOD: in console execute a short script that parses `location.search` for `variant=`; attaches `click` listeners to all elements with class `.btn-primary`; on click increments a counter stored in `localStorage` under key `ctaClicks_variantX`; logs counts after each click.  
EFFECT: Provides quantitative data on which URL‑variant (e.g., `?variant=1` vs `?variant=2`) drives more CTA clicks, allowing data‑driven decisions without backend integration.  
RISK: Counts only reflect the current browser session; results may be noisy with a single user and require manual reset of `localStorage`.  
ROLLBACK: Run `localStorage.removeItem('ctaClicks_variant1'); localStorage.removeItem('ctaClicks_variant2');` and detach listeners (`removeEventListener`) or simply refresh the page to discard the script.  
VERIFY: Reload page with `?variant=1`, run the script, click a CTA, note console output; repeat with `?variant=2` and compare counts—all within 2 minutes.  
PRIORITY: 2 – adds conversion insight with minimal effort, useful for testing copy or style variants.  

IDEA: Time‑to‑CTA‑Visible (TTV) Measurement  
KNOB: METHOD: in console create an `IntersectionObserver` targeting the primary CTA element (e.g., `document.querySelector('.final .btn-primary')`); on first intersection record `performance.now() - performance.timing.navigationStart` and log the elapsed milliseconds; optionally store in `sessionStorage` for later review.  
EFFECT: Measures how quickly the CTA appears in the viewport after page load, indicating layout efficiency and potential friction points.  
RISK: Results depend on initial scroll position; user‑initiated scrolling before the CTA appears can inflate the metric.  
ROLLBACK: Call `observer.disconnect()` and clear the stored value (`sessionStorage.removeItem('ttv')`); no changes to source files needed.  
VERIFY: Reload the page at the top, run the script, wait for the CTA to become visible, and check the console for a timestamp (aim for < 2000 ms) within 2 minutes.  
PRIORITY: 3 – valuable UX metric, slightly more complex but still executable quickly without code deployment.
