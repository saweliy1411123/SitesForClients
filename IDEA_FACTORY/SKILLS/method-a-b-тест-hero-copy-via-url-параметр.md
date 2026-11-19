---
name: METHOD: A/B‑тест hero‑copy via URL‑параметр
source: localhost:8080/ovh/gpt-oss-120b
round: 119
status: proposed
portable: true
tags: [static-landing, portable]
---

# METHOD: A/B‑тест hero‑copy via URL‑параметр

**Name:** glassmorphic-cta-button
**When to apply:** На любой лендинг, где CTA‑кнопки оформлены как ссылки `<a class="btn-primary">`.
**SAFE CSS:**
```css
.btn-primary.glassy {
background: rgba(255,255,255,0.15);
backdrop-filter: blur(8px);
border: 1px solid rgba(255,255,255,0.25);
border-radius: 8px;
color: #fff;
padding: 0.75rem 1.5rem;
display: inline-flex;
align-items: center;
gap: 0.5rem;
transition: background 0.3s, transform 0.2s;
}
.btn-primary.glassy:hover,
.btn-primary.glassy:focus-visible {
background: rgba(255,255,255,0.25);
transform: translateY(-2px);
}
.btn-primary.glassy .arr {
transition: transform 0.2s;
}
.btn-primary.glassy:hover .arr {
transform: translateX(4px);
}
```
**SAFE JS:** *(необязательно, но добавляет копирование текста при клике)*
```js
document.querySelectorAll('.btn-primary.glassy').forEach(btn=>{
btn.addEventListener('click',e=>{
if(e.shiftKey){ // Shift‑click копирует ссылку в буфер
navigator.clipboard.writeText(btn.href);
btn.textContent='Ссылка скопирована!';
}
});
});
```

## Когда применять
Делает CTA визуально премиальными, повышает доверие и улучшает конверсию за счёт яркого, но лёгкого эффекта.

## Проверка
Добавить класс к одной ссылке, открыть страницу, убедиться в прозрачном фоне и плавном hover‑эффекте; проверить, что в старых браузерах кнопка остаётся обычной.

## SAFE JS
```js
** *(необязательно, но добавляет копирование текста при клике)*
```js
document.querySelectorAll('.btn-primary.glassy').forEach(btn=>{
btn.addEventListener('click',e=>{
if(e.shiftKey){ // Shift‑click копирует ссылку в буфер
navigator.clipboard.writeText(btn.href);
btn.textContent='Ссылка скопирована!';
}
});
});
```
```
