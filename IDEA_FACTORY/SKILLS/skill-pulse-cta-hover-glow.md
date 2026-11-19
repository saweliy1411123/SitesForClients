---
name: SKILL — pulse‑cta‑hover‑glow
source: localhost:8080/ovh/gpt-oss-120b
round: 140
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — pulse‑cta‑hover‑glow

**Name:** `pulse-cta-hover-glow`
**When to apply:** На все ссылки‑CTA, оформленные как кнопки (`.btn-primary`, `.cta-row a`).
**Steps:**
1. Добавить к CTA класс `pulse-cta`.
2. В CSS задать анимацию «pulse» (scale + box‑shadow) с `animation-timing-function: ease-out`.
3. При `:focus-visible` добавить более яркую подсветку для доступности.
**SAFE CSS:**
```css
.pulse-cta{
position:relative;
overflow:hidden;
}
.pulse-cta::after{
content:"";
position:absolute;
inset:0;
border-radius:inherit;
background:radial-gradient(circle at center, var(--blue) 0%, transparent 70%);
opacity:0;
transform:scale(0);
transition:opacity .2s,transform .3s;
}
.pulse-cta:hover::after,
.pulse-cta:focus-visible::after{
opacity:.25;
transform:scale(1.2);
}
@keyframes pulse{
0%{transform:scale(1);box-shadow:0 0 0 0 rgba(139,92,246,.0);}
70%{transform:scale(1.05);box-shadow:0 0 0 12px rgba(139,92,246,.0);}
100%{transform:scale(1);box-shadow:0 0 0 0 rgba(139,92,246,.0);}
}
.pulse-cta:hover{
animation:pulse .8s ease

## Когда применять


## Проверка

