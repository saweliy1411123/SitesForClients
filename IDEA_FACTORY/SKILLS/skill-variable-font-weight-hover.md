---
name: SKILL — Variable Font‑Weight Hover
source: localhost:8080/ovh/gpt-oss-120b
round: 70
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Variable Font‑Weight Hover

METHOD: SKILL
**Name:** variable-font-weight-hover
**When to apply:** На всех заголовках h1‑h3 на премиальных лендингах, где нужен интерактивный типографический акцент без JavaScript.
**Steps:**
1. В `:root` объявить CSS‑переменную `--h-weight` со значением `500`.
2. Добавить к заголовкам правило `font-weight: var(--h-weight); transition: font-weight 0.25s ease;`.
3. В `:hover, :focus-visible` установить `--h-weight: 700;`.
4. При отсутствии поддержки `transition` для `font-weight` (IE) будет обычный переход без анимации – приемлемо.
SAFE CSS:
```css
:root{--h-weight:500}
h1,h2,h3{font-weight:var(--h-weight);transition:font-weight .25s ease}
h1:hover,h1:focus-visible,
h2:hover,h2:focus-visible,
h3:hover,h3:focus-visible{--h-weight:700}
```
SAFE JS: *(не требуется)*

## Когда применять
Делает заголовки более «живыми», усиливает восприятие премиального бренда и повышает CTR на CTA, расположенные рядом.

## Проверка
Открыть страницу в Chrome/Firefox, навести курсор на любой h1‑h3 – вес шрифта должен плавно перейти 500 → 700 за ≈ 0.25 с; проверить отсутствие JS‑ошибок в консоли.

## SAFE CSS
```css
```css
:root{--h-weight:500}
h1,h2,h3{font-weight:var(--h-weight);transition:font-weight .25s ease}
h1:hover,h1:focus-visible,
h2:hover,h2:focus-visible,
h3:hover,h3:focus-visible{--h-weight:700}
```
```

## SAFE JS
```js
*(не требуется)*
```
