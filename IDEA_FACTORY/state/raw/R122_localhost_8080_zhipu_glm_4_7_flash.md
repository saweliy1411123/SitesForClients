# localhost:8080/zhipu/glm-4.7-flash  2026-11-17 07:37:50
duration=67.1 error=- attempts=1

IDEA: Scroll-Aware Step Highlighter
KNOB: Replace static "explicit result" text ideas with a JS-driven progress bar above `.steps` (L565). Use `IntersectionObserver` to highlight the active step as the user scrolls.
EFFECT: Visualizes progress, reduces cognitive load, guides attention to the current step without cluttering the UI.
RISK: Adds ~100 lines of JS, potential FOUC if not handled.
ROLLBACK: Remove the `<div class="step-progress">` and the JS script block.
VERIFY: Open DevTools, scroll through the "Three steps" section, check console for errors and visual highlighting.
PRIORITY: 2 (UX improvement over static text additions).
SITE_REQUEST: steps

IDEA: Dynamic FAQ Schema.org (FAQPage)
KNOB: Replace generic "Add JSON-LD" with a specific FAQPage schema. Insert `<script type="application/ld+json">` in `<head>` that parses questions from the FAQ section (L664+) and answers from the DOM.
EFFECT: Enables Google FAQ rich snippets, potentially increasing CTR by 20-30% in SERP.
RISK: Schema must match content exactly; mismatched answers get rejected.
ROLLBACK: Delete the `<script type="application/ld+json">` block.
VERIFY: Run URL through Google Rich Results Test.
PRIORITY: 1 (High impact SEO).
SITE_REQUEST: faq
