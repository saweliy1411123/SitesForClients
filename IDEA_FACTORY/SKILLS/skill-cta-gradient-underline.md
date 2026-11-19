---
name: SKILL — cta-gradient-underline
source: localhost:8080/ovh/gpt-oss-120b
round: 49
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — cta-gradient-underline

METHOD: SKILL
**Name:** `cta-gradient-underline`
**When to apply:** На все ссылки‑CTA (`.btn-primary`, `.fab-demo`, `.hero a`) для придания им «светящегося» подчеркивания при наведении, усиливающего интерактивность.
**Steps:**
1. Добавить к CTA‑элементам класс `gradient-underline`.
2. Подключить CSS‑блок ниже.
**SAFE CSS:**
```css
.gradient-underline{
position:relative;
color:inherit;
text-decoration:none;
}
.gradient-underline::after{
content:"";
position:absolute;
left:0; bottom:-2px;
width:100%; height:2px;
background:linear-gradient(90deg,var(--blue),var(--purple));
transform:scaleX(0);
transform-origin:left;
transition:transform .35s ease;
}
.gradient-underline:hover::after,
.gradient-underline:focus-visible::after{
transform:scaleX(1);
}
.gradient-underline:focus-visible{
outline:none;
box-shadow:0 0 0 3px rgba(139,92,246,.3);
}
```

## Когда применять
Делает CTA более заметными, повышает коэффициент клика (CTR) за счёт анимированного градиентного подчеркивания, сохраняет чистый дизайн без лишних изображений.

## Проверка
Навести курсор на любую кнопку/ссылку‑CTA – появится плавное градиентное подчеркивание; проверить в Chrome DevTools → Elements, убедиться в наличии `::after`.
