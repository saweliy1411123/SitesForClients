---
name: SKILL — card-3d-tilt-hover
source: localhost:8080/ovh/gpt-oss-120b
round: 49
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — card-3d-tilt-hover

METHOD: SKILL
**Name:** `card-3d-tilt-hover`
**When to apply:** На карточках `.price-card`, `.demo-item` (или любой `.card`) для придания премиального 3‑D‑ощущения при наведении.
**Steps:**
1. Добавить к нужным элементам класс `card-3d`.
2. Подключить CSS‑блок ниже (автоподключение через `<style>` или отдельный файл).
**SAFE CSS:**
```css
.card-3d{
perspective:800px;
transform-style:preserve-3d;
transition:transform .35s ease,var(--shadow) .35s ease;
will-change:transform;
}
.card-3d:hover{
transform:rotateX(4deg) rotateY(6deg) scale(1.02);
box-shadow:0 20px 40px rgba(0,0,0,.25);
}
.card-3d::before{
content:"";
position:absolute;
inset:0;
border-radius:inherit;
background:linear-gradient(135deg,rgba(255,255,255,.12),transparent);
pointer-events:none;
}
```
**SAFE JS:** (необязательно – только если требуется отключить эффект при `prefers-reduced-motion`)
```js
if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){
document.querySelectorAll('.card-3d').forEach(el=>el.style.transition='none');
}
```

## Когда применять
Увеличивает восприятие «премиальности» и удерживает внимание на цене/демо‑карточках, повышая CTR на CTA внутри карточек.

## Проверка
Открыть страницу, наведите курсор на любую `.price-card` – должна появиться лёгкая 3‑D‑наклонка и тень; проверить в Chrome DevTools → Emulation → `prefers-reduced-motion`.

## SAFE JS
```js
** (необязательно – только если требуется отключить эффект при `prefers-reduced-motion`)
```js
if(window.matchMedia('(prefers-reduced-motion: reduce)').matches){
document.querySelectorAll('.card-3d').forEach(el=>el.style.transition='none');
}
```
```
