---
name: SKILL — focus-visible-gradient-ring
source: localhost:8080/ovh/gpt-oss-120b
round: 125
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — focus-visible-gradient-ring

**Name:** `focus-visible-gradient-ring`
**When to apply:** На любой лендинге, где есть интерактивные ссылки, кнопки и элементы‑сводки (`<summary>`), чтобы улучшить доступность и добавить премиальный визуальный акцент при клавиатурной навигации.
**Steps:**
1. Убедиться, что в корневом `:root` объявлена переменная `--grad` (используется в проекте).
2. В CSS‑файл (или в `<style>`) добавить правила из `SAFE CSS` ниже.
3. При желании, в конец `<body>` можно добавить небольшой скрипт из `SAFE JS` (необязательно) для поддержки старых браузеров, не поддерживающих `:focus-visible`.
**SAFE CSS:**
```css
a:focus-visible,
button:focus-visible,
summary:focus-visible{
outline:none;
box-shadow:0 0 0 3px var(--grad);
border-radius:4px;
transition:box-shadow .2s ease-in-out;
}
```
**SAFE JS (optional):**
```js
(() => {
const style = document.createElement('style');
style.textContent = 'a:focus,button:focus,summary:focus{outline:none;box-shadow:0 0 0 3px var(--grad);border-radius:4px;}';
document.head.appendChild(style);
})();
```

## Когда применять
Ясный визуальный индикатор фокуса повышает доступность (WCAG 2.1 AA) и усиливает восприятие бренда как «премиального». Это может увеличить конверсию за счёт снижения количества «потерянных» пользователей, навигирующих клавиатурой.

## Проверка
Открыть страницу, перейти к любой ссылке/кнопке с помощью клавиши Tab – вокруг элемента должен появиться градиентный светящийся контур; убедиться, что контур исчезает при потере фокуса и нет ошибок в консоли.

## SAFE CSS
```css
**
```css
a:focus-visible,
```
