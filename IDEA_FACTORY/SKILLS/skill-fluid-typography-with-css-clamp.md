---
name: SKILL — Fluid Typography with CSS clamp()
source: localhost:8080/ovh/gpt-oss-120b
round: 14
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Fluid Typography with CSS clamp()

METHOD: Внедрите глобальный набор CSS‑переменных `--fs-base`, `--fs-scale` и используйте `clamp()` для всех заголовков и текста, обеспечивая адаптивный размер шрифта от мобильных до десктопных экранов.
SAFE CSS:
```css
:root {
--fs-base: 1rem;          /* 16px */
--fs-scale: 1.2;          /* multiplier */
}
h1 { font-size: clamp(1.75rem, calc(var(--fs-base) * var(--fs-scale) * 2.5), 3rem); }
h2 { font-size: clamp(1.5rem, calc(var(--fs-base) * var(--fs-scale) * 2), 2.5rem); }
h3 { font-size: clamp(1.25rem, calc(var(--fs-base) * var(--fs-scale) * 1.5), 2rem); }
p, li { font-size: clamp(0.875rem, calc(var(--fs-base) * var(--fs-scale)), 1rem); }
```

## Когда применять
Текст выглядит оптимально на любом устройстве без медиа‑запросов, улучшает читаемость и восприятие качества.

## Проверка
Открыть страницу в DevTools, переключить размеры окна (375 px → 1440 px) и убедиться, что шрифты плавно масштабируются без резких скачков.

## SAFE CSS
```css
```css
:root {
--fs-base: 1rem;          /* 16px */
--fs-scale: 1.2;          /* multiplier */
}
h1 { font-size: clamp(1.75rem, calc(var(--fs-base) * var(--fs-scale) * 2.5), 3rem); }
h2 { font-size: clamp(1.5rem, calc(var(--fs-base) * var(--fs-scale) * 2), 2.5rem); }
h3 { font-size: clamp(1.25rem, calc(var(--fs-base) * var(--fs-scale) * 1.5), 2rem); }
p, li { font-size: clamp(0.875rem, calc(var(--fs-base) * var(--fs-scale)), 1rem); }
```
```
