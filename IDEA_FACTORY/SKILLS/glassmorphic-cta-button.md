---
name: Glassmorphic CTA button
source: localhost:8080/ovh/gpt-oss-120b
round: 133
status: proposed
portable: true
tags: [static-landing, portable]
---

# Glassmorphic CTA button

SKILL — glassmorphic-cta-button
Name: glassmorphic-cta-button
When to apply: На всех ссылках‑CTA с классом `.btn-primary` в любом лендинге, где нужен премиальный визуальный акцент без тяжёлых скриптов.
SAFE CSS:
```css
.btn-primary {
position: relative;
overflow: hidden;
background: rgba(255,255,255,0.12);
backdrop-filter: blur(8px);
border: 1px solid rgba(255,255,255,0.2);
color: var(--text);
transition: background .3s ease, box-shadow .3s ease;
}
.btn-primary::before {
content: "";
position: absolute;
inset: -50%;
background: linear-gradient(135deg, rgba(139,92,246,.2), rgba(76,201,240,.2));
transform: rotate(45deg);
transition: transform .5s ease;
}
.btn-primary:hover::before {
transform: rotate(45deg) translateX(200%);
}
.btn-primary:hover {
background: rgba(255,255,255,0.18);
box-shadow: 0 4px 12px rgba(0,0,0,.15);
}
```
SAFE JS: *(не требуется)*

## Когда применять
Повышает восприятие ценности CTA, делает кнопку более «премиальной», увеличивает CTR за счёт визуального контраста.

## Проверка
Открыть страницу в Chrome, навести курсор на любую кнопку CTA – должна появиться анимация градиентного сдвига и размытие фона; сравнить CTR в аналитике до/после.

## SAFE JS
```js
*(не требуется)*
```
