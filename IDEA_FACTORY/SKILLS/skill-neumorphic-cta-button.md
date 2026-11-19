---
name: SKILL — neumorphic‑cta‑button
source: localhost:8080/ovh/gpt-oss-120b
round: 154
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — neumorphic‑cta‑button

**Name:** `neumorphic-cta-button`
**When to apply:** На всех ссылках‑кнопках CTA (`.btn-primary`, `.btn-secondary`) для создания мягкого, «поднятого» ощущения, характерного для премиального дизайна.
**SAFE CSS:**
```css
.neumo-cta {
background: var(--bg);
color: var(--text);
border-radius: 10px;
padding: 0.75em 1.5em;
box-shadow: 6px 6px 12px rgba(0,0,0,0.18),
-6px -6px 12px rgba(255,255,255,0.12);
transition: box-shadow .18s ease, transform .18s ease;
}
.neumo-cta:focus-visible,
.neumo-cta:hover {
box-shadow: 4px 4px 8px rgba(0,0,0,0.12),
-4px -4px 8px rgba(255,255,255,0.08);
}
.neumo-cta:active {
transform: translateY(2px);
box-shadow: inset 4px 4px 8px rgba(0,0,0,0.2),
inset -4px -4px 8px rgba(255,255,255,0.1);
}
```
**SAFE JS:** _не требуется_

## Когда применять
Придаёт CTA «осязаемость» и повышает конверсию за счёт более заметного, приятного отклика на взаимодействие.

## Проверка
Нажать/навести на любую кнопку‑CTA – должна измениться тень и небольшое смещение; проверить в мобильном режиме (touch) – активный стиль срабатывает.

## SAFE JS
```js
** _не требуется_
```
