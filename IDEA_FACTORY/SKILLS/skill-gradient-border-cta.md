---
name: SKILL — gradient‑border‑cta
source: localhost:8080/ovh/gpt-oss-120b
round: 147
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — gradient‑border‑cta

SKILL: **Name:** `gradient-border-cta`
**When to apply:** К любой ссылке‑кнопке с классом `.btn-primary` (главный CTA) для создания анимированной градиентной рамки.
**Steps:** 1️⃣ Заменить класс `.btn-primary` на `btn-gradient-border` (или добавить оба). 2️⃣ Добавить CSS ниже.
SAFE CSS:
```css
.btn-gradient-border{
position:relative;
overflow:hidden;
border:2px solid transparent;
background:var(--bg);
color:var(--blue);
transition:color .3s;
}
.btn-gradient-border::before{
content:"";
position:absolute;
inset:-2px;
background:linear-gradient(45deg,var(--grad-start),var(--grad-end));
z-index:-1;
transition:transform .4s;
transform:scaleX(0);
transform-origin:left;
}
.btn-gradient-border:hover::before,
.btn-gradient-border:focus-visible::before{
transform:scaleX(1);
}
.btn-gradient-border:hover,
.btn-gradient-border:focus-visible{
color:#fff;
}
```

## Когда применять
Динамичная градиентная рамка привлекает внимание к CTA, усиливает ощущение «дорогого» дизайна и повышает кликабельность.

## Проверка
Навести курсор на кнопку – градиентная рамка должна «заполняться» слева направо; проверить, что текст остаётся читаемым.
