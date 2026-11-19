---
name: SKILL — theme-toggle (light/dark premium)
source: localhost:8080/ovh/gpt-oss-120b
round: 56
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — theme-toggle (light/dark premium)

METHOD: SKILL
**Name:** `theme-toggle`
**When to apply:** На любой статический лендинг, где требуется премиальная визуальная гибкость и пользователь может захотеть переключить светлую/тёмную схему без перезагрузки.
**SAFE CSS:**
```css
:root{
--bg:#ffffff;
--text:#111111;
--primary:#8b5cf6;
--muted:#6b7280;
--gradient:linear-gradient(135deg,var(--primary),#4ec9f0);
}
[data-theme="dark"]{
--bg:#111111;
--text:#f5f5f5;
--primary:#c084fc;
--muted:#9ca3af;
--gradient:linear-gradient(135deg,var(--primary),#4ec9f0);
}
body{
background:var(--bg);
color:var(--text);
transition:background .3s,color .3s;
}
.theme-toggle{
cursor:pointer;
display:inline-flex;
align-items:center;
gap:.5rem;
font-weight:600;
color:var(--primary);
}
.theme-toggle::after{
content:"🌙";
}
[data-theme="dark"] .theme-toggle::after{
content:"☀️";
}
```
**SAFE JS:**
```js
(() => {
const btn = document.querySelector('.theme-toggle');
if (!btn) return;
const setTheme = t => {
document.documentElement.dataset.theme = t;
localStorage.setItem('theme',t);
};
const stored = localStorage.getItem('theme');
if (stored) setTheme(stored);
btn.addEventListener('click',()=> {
const newT = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
setTheme(newT);
});
})();
```

## Когда применять
Позволяет пользователям быстро переключать цветовую схему, повышая восприятие премиальности и улучшая доступность в тёмных условиях.

## Проверка
Открыть страницу, кликнуть кнопку «theme‑toggle», убедиться в смене цветов и в сохранении выбора после перезагрузки.
