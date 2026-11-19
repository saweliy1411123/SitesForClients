---
name: SKILL — Hero Clarity Boost
source: localhost:8081/big_only
round: 41
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Hero Clarity Boost

**Name:** `hero-clarity-boost`
**When to apply:** На лендингах с первым экраном (hero), где оффер и CTA находятся в одном блоке, но текст может быть перегружен.
**Steps:**
1. Вставить после `<h1>` в секции `.hero` список преимуществ:
```html
<ul class="hero-benefits">
<li>✅ Сайт за 2 дня — полностью готов к поиску</li>
<li>✅ Адаптив под любые экраны — мгновенный отклик</li>
<li>✅ Бесплатное демо‑макет — без обязательств</li>
</ul>
```
2. Добавить стили, чтобы список выглядел компактно и читабельно на мобильных и десктопах.
3. Увеличить контраст CTA‑кнопки и добавить `aria‑label`.
**SAFE CSS:**
```css
.hero-benefits{margin:1.2rem 0;padding:0;list-style:none;display:flex;flex-wrap:wrap;gap:0.8rem}
.hero-benefits li{font-size:0.92rem;color:var(--muted);display:flex;align-items:center}
.hero-benefits li::before{content:"✓";margin-right:0.4rem;color:var(--green);font-weight:600}
.btn-primary{min-height:48px;min-width:140px;padding:0.6rem 1.2rem;font-weight:600;background:var(--violet);border:none;border-radius:6px;transition:background .3s,transform .2s}
.btn-primary:hover{background:#7c3aed;transform:scale(1.03)}
```
**SAFE JS:** *(не требуется)*

## Когда применять
Улучшает восприятие оффера за 5 секунд, повышает CTR первой CTA‑кнопки, снижает показатель отказов.

## Проверка
Открыть страницу в Chrome, переключить DevTools → Device Toolbar → iPhone SE; убедиться, что список виден, CTA‑кнопка контрастна, а Lighthouse → SEO → First Contentful Paint < 1 s.

## SAFE CSS
```css
**
```css
.hero-benefits{margin:1.2rem 0;padding:0;list-style:none;display:flex;flex-wrap:wrap;gap:0.8rem}
.hero-benefits li{font-size:0.92rem;color:var(--muted);display:flex;align-items:center}
.hero-benefits li::before{content:"✓";margin-right:0.4rem;color:var(--green);font-weight:600}
.btn-primary{min-height:48px;min-width:140px;padding:0.6rem 1.2rem;font-weight:600;background:var(--violet);border:none;border-radius:6px;transition:background .3s,transform .2s}
.btn-primary:hover{background:#7c3aed;transform:scale(1.03)}
```
**SAFE JS:** *(не требуется)*
```

## SAFE JS
```js
** *(не требуется)*
```
