---
name: SKILL — «Мягкий подсвет-пульс CTA» (этичное привлечение внимания без dark patterns)
source: lareper/glm-5.2
round: 20
status: proposed
portable: true
tags: [static-landing, portable, animation, responsive]
---

# SKILL — «Мягкий подсвет-пульс CTA» (этичное привлечение внимания без dark patterns)

Название: **cta-soft-pulse**. Когда применять: любой лендинг с одной якорной CTA-кнопкой (`.btn-primary`), где нужно повысить заметность кнопки без мигания, таймеров и ложных дедлайнов. Шаги: (1) добавить к `.btn-primary` (L462 и финальная CTA) класс-модификатор `.pulse`; (2) лёгкая анимация тени-свечения 3 с цикл, пауза на hover/focus; (3) обязательно отключение при `prefers-reduced-motion`; (4) убедиться, что пульс не меняет размер/положение кнопки (только box-shadow — нет CLS).
SAFE CSS:
.pulse{animation:cta-pulse 3s ease-in-out infinite}
@keyframes cta-pulse{0%,100%{box-shadow:0 0 0 0 rgba(139,92,246,.45)}50%{box-shadow:0 0 0 12px rgba(139,92,246,0)}}
.pulse:hover,.pulse:focus-visible{animation:none;box-shadow:0 8px 30px rgba(139,92,246,.35)}
@media (prefers-reduced-motion: reduce){.pulse{animation:none}}
SAFE JS: (не требуется

## Когда применять


## Проверка


## SAFE CSS
```css
.pulse{animation:cta-pulse 3s ease-in-out infinite}
@keyframes cta-pulse{0%,100%{box-shadow:0 0 0 0 rgba(139,92,246,.45)}50%{box-shadow:0 0 0 12px rgba(139,92,246,0)}}
.pulse:hover,.pulse:focus-visible{animation:none;box-shadow:0 8px 30px rgba(139,92,246,.35)}
@media (prefers-reduced-motion: reduce){.pulse{animation:none}}
```
