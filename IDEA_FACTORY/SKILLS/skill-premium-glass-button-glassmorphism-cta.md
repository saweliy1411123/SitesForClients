---
name: SKILL — premium‑glass‑button (glassmorphism CTA)
source: localhost:8080/ovh/gpt-oss-120b
round: 56
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — premium‑glass‑button (glassmorphism CTA)

METHOD: SKILL
**Name:** `premium-glass-button`
**When to apply:** Для всех CTA‑кнопок (`.btn-primary`, `.sticky-cta .btn-primary`) на темных или градиентных фонах, где нужен современный стеклянный вид.
**SAFE CSS:**
```css
.glass-btn{
position:relative;
overflow:hidden;
border:1px solid rgba(255,255,255,.2);
background:rgba(255,255,255,.1);
backdrop-filter:blur(8px);
color:var(--primary);
padding:.75rem 1.5rem;
border-radius:12px;
transition:background .3s,transform .2s;
}
.glass-btn::after{
content:"";
position:absolute;
inset:0;
background:linear-gradient(45deg,rgba(255,255,255,.15),transparent);
opacity:0;
transition:opacity .3s;
}
.glass-btn:hover{
background:rgba(255,255,255,.2);
transform:translateY(-2px);
}
.glass-btn:hover::after{
opacity:1;
}
```
**SAFE JS:** *(не требуется)*

## Когда применять
Придаёт CTA‑кнопкам премиальный «стеклянный» вид, усиливает визуальный клик‑эффект, повышает конверсию за счёт более заметного CTA.

## Проверка
Добавить класс `glass-btn` к любой существующей кнопке, открыть страницу, убедиться в появлении полупрозрачного фонового блёра и плавного hover‑эффекта.

## SAFE JS
```js
** *(не требуется)*
```
