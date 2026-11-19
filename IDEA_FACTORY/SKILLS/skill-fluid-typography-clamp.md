---
name: SKILL — fluid-typography-clamp
source: localhost:8080/ovh/gpt-oss-120b
round: 139
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — fluid-typography-clamp

**Name:** fluid-typography-clamp
**When to apply:** На любом статическом лендинге, где используется фиксированное `font-size` в px/rem и требуется адаптивная типографика без множества медиазапросов.
**Steps:**
1. Добавить в глобальный CSS блок `SAFE CSS` (см. ниже).
2. При необходимости задать кастомные переменные `--fs-min` и `--fs-max` в `:root` для разных уровней заголовков.
3. На нужных элементах добавить класс `.fluid-text` (или `.fluid-h1`, `.fluid-h2` и т.д., если нужны отдельные диапазоны).
4. При тестировании проверить читаемость на ширине 320 px – 1440 px.
**SAFE CSS:**
```css
:root{
--fs-min: 0.875rem;   /* 14 px */
--fs-max: 1.25rem;    /* 20 px */
}
.fluid-text{
font-size: clamp(var(--fs-min), 1.2vw, var(--fs-max));
line-height: 1.4;
}
.fluid-h1{
--fs-min: 1.5rem;
--fs-max: 2.5rem;
font-size: clamp(var(--fs-min), 2vw, var(--fs-max));
line-height: 1.2;
}
.fluid-h2{
--fs-min: 1.25rem;
--fs-max: 2rem;
font-size: clamp(var(--fs-min), 1.8vw, var(--fs-max));
line-height: 1.3;
}
```

## Когда применять
Читабельный текст, автоматически подстраивающийся под любые экраны, повышает UX и SEO‑доступность без добавления новых медиазапросов.

## Проверка
Открыть страницу в Chrome, открыть DevTools → Device Toolbar, переключить между 320 px и 1440 px, убедиться, что размер текста плавно меняется в пределах заданных границ.

## SAFE CSS
```css
**
```css
:root{
--fs-min: 0.875rem;   /* 14 px */
--fs-max: 1.25rem;    /* 20 px */
}
.fluid-text{
font-size: clamp(var(--fs-min), 1.2vw, var(--fs-max));
line-height: 1.4;
}
.fluid-h1{
--fs-min: 1.5rem;
--fs-max: 2.5rem;
font-size: clamp(var(--fs-min), 2vw, var(--fs-max));
line-height: 1.2;
}
.fluid-h2{
--fs-min: 1.25rem;
--fs-max: 2rem;
font-size: clamp(var(--fs-min), 1.8vw, var(--fs-max));
line-height: 1.3;
}
```
```
