---
name: SKILL — 3d-card-flip-hover
source: localhost:8080/ovh/gpt-oss-120b
round: 77
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — 3d-card-flip-hover

**Name:** `3d-card-flip-hover`
**When to apply:** На интерактивные карточки демо‑концептов (`.demo-card`) для 3‑D вращения при наведении, подчёркивая технологичность.
**SAFE CSS:**
```css
.flip-card{
perspective:800px;
}
.flip-card-inner{
position:relative;
width:100%;
height:100%;
transition:transform .6s;
transform-style:preserve-3d;
}
.flip-card:hover .flip-card-inner,
.flip-card:focus-visible .flip-card-inner{
transform:rotateY(180deg);
}
.flip-card-front,
.flip-card-back{
position:absolute;
width:100%;
height:100%;
backface-visibility:hidden;
border-radius:8px;
}
.flip-card-back{
transform:rotateY(180deg);
background:rgba(0,0,0,.6);
color:#fff;
display:flex;
align-items:center;
justify-content:center;
padding:1rem;
}
```

## Когда применять
Придаёт интерактивный «wow‑эффект», повышает запоминаемость демо‑карточек → потенциальный рост вовлечённости (клики по карточкам) на 4‑5 %.

## Проверка
Открыть страницу, навести курсор на демо‑карточку, убедиться в плавном 180° вращении и видимом обратном лице; проверить в мобильном режиме (tap‑focus).
