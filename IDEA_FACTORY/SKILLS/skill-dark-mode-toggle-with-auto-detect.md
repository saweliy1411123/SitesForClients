---
name: SKILL — Dark‑Mode Toggle with Auto‑Detect
source: localhost:8080/ovh/gpt-oss-120b
round: 14
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — Dark‑Mode Toggle with Auto‑Detect

METHOD: Добавьте CSS‑переменные для цветов темы и переключатель‑кнопку, меняющую `data-theme` на `<html>`. При загрузке проверяется `prefers‑color‑scheme`.
SAFE CSS:
```css
:root {
--bg: #ffffff;
--text: #111111;
--accent: #8b5cf6;
}
[data-theme="dark"] {
--bg: #111111;
--text: #f5f5f5;
--accent: #c084fc;
}
body { background: var(--bg); color: var(--text); }
a.btn-primary { background: var(--accent); }
```
SAFE JS:
```js
(function(){
const root = document.documentElement;
const saved = localStorage.getItem('theme');
const prefersDark = matchMedia('(prefers-color-scheme: dark)').matches;
const theme = saved || (prefersDark ? 'dark' : 'light');
root.dataset.theme = theme;
document.getElementById('theme-toggle').addEventListener('click',()=> {
const newTheme = root.dataset.theme === 'dark' ? 'light' : 'dark';
root.dataset.theme = newTheme;
localStorage.setItem('theme', newTheme);
});
})();
```

## Когда применять
Позволяет пользователям выбирать тёмную тему, повышает восприятие сайта как современного и заботящегося о зрительном комфорте, потенциально увеличивает время на странице.

## Проверка
Открыть страницу, кликнуть кнопку, убедиться в смене цветов; проверить автодетекцию, переключив системную тему в настройках OS.

## SAFE CSS
```css
```css
:root {
--bg: #ffffff;
--text: #111111;
--accent: #8b5cf6;
}
[data-theme="dark"] {
--bg: #111111;
--text: #f5f5f5;
--accent: #c084fc;
}
body { background: var(--bg); color: var(--text); }
a.btn-primary { background: var(--accent); }
```
```
