---
name: SKILL — ripple‑effect‑button
source: localhost:8080/ovh/gpt-oss-120b
round: 83
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — ripple‑effect‑button

**Name:** `ripple-effect-button`
**When to apply:** На любом статическом лендинге, где CTA‑кнопки реализованы через `<a class="btn-primary">` или `<button>` и требуется визуальная обратная связь при нажатии.
**Steps:**
1. Добавить в `<head>` (или в `index.improved.html`) ссылку на файл‑skill `ripple-effect-button.css`.
2. Убедиться, что все CTA‑кнопки используют класс `.btn-primary` (уже есть в проекте).
3. При желании добавить класс `.ripple` к отдельным кнопкам, если не хочется распространять эффект на все.
**SAFE CSS:**
```css
/* ripple‑effect‑button.css */
.btn-primary {
position: relative;
overflow: hidden;
}
.btn-primary::after {
content: "";
position: absolute;
left: 50%; top: 50%;
width: 0; height: 0;
background: rgba(255,255,255,0.3);
border-radius: 50%;
transform: translate(-50%,-50%);
transition: width .4s ease-out, height .4s ease-out, opacity .4s;
pointer-events: none;
}
.btn-primary:active::after {
width: 200px;
height: 200px;
opacity: 0;
}
```

## Когда применять
Пользователь видит мгновенный «водяной» всплеск при нажатии, что повышает ощущение интерактивности и может увеличить конверсию CTA‑кнопок.

## Проверка
Открыть страницу в браузере, кликнуть по любой кнопке `.btn-primary` и убедиться, что появляется круглая вспышка, исчезающая за ≈ 0.4 сек. Проверить, что клик всё равно переходит по ссылке.
