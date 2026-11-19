---
name: SKILL — gradient‑focus‑ring (градиентный кольцевой контур фокуса)
source: localhost:8081/big_only
round: 126
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — gradient‑focus‑ring (градиентный кольцевой контур фокуса)

**Name:** `gradient-focus-ring`
**When to apply:** На любой странице с интерактивными элементами (`a`, `.btn-primary`, `summary`) где нужен яркий, но лёгкий визуальный индикатор фокуса.
**SAFE CSS:**
```css
:focus-visible {
outline: none;
position: relative;
}
:focus-visible::after {
content: '';
position: absolute;
inset: -4px;
border-radius: 6px;
background: conic-gradient(from 90deg, var(--grad) 0%, transparent 120deg);
animation: focusRingSpin 1.2s linear infinite;
mask: radial-gradient(circle, white 70%, transparent);
}
@keyframes focusRingSpin {
to { transform: rotate(360deg); }
}
```
**SAFE JS:** (необязательно)
```js
// optional: add class for browsers without :focus-visible support
document.querySelectorAll('a, .btn-primary, summary').forEach(el=>{
el.addEventListener('focus',()=>el.classList.add('focus-visible'));
el.addEventListener('blur',()=>el.classList.remove('focus-visible'));
});
```

## Когда применять
улучшает доступность, делая фокус явно видимым, одновременно подчёркивая премиальный дизайн.

## Проверка
перейти по клавише Tab к любой ссылке/кнопке, увидеть анимированный градиентный кольцевой контур; убедиться, что он исчезает при потере фокуса.
