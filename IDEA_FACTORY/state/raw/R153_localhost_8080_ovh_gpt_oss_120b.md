# localhost:8080/ovh/gpt-oss-120b  2026-11-17 09:04:23
duration=29.6 error=- attempts=1

IDEA: SKILL — dark-mode-toggle  
KNOB: **Name:** `dark-mode-toggle`  
**When to apply:** На любом статическом лендинге, где нужен быстрый способ дать пользователю возможность переключать светлую/тёмную тему без серверных изменений.  
**Steps:**  
1. В `<head>` добавить переменные CSS‑цветов для светлой и тёмной схемы.  
2. В шапку (`<header class="hero">`) вставить кнопку‑переключатель:  
   ```html
   <button class="theme-toggle" aria-label="Переключить тему" aria-pressed="false">🌙</button>
   ```  
3. В конец `<body>` добавить небольшой скрипт, который:  
   - читает `localStorage.theme`; если есть – добавляет класс `dark` к `<html>`;  
   - при клике по `.theme-toggle` переключает класс `dark` и сохраняет выбор;  
   - обновляет `aria-pressed` и иконку кнопки.  
**SAFE CSS:**  
```css
:root {
  --bg-light: #ffffff;
  --bg-dark: #0a0a0f;
  --text-light: #111827;
  --text-dark: #e5e7eb;
  --accent-light: #8b5cf6;
  --accent-dark: #a78bfa;
}

/* Тёмная тема */
html.dark {
  --bg: var(--bg-dark);
  --text: var(--text-dark);
  --accent: var(--accent-dark);
}

/* Светлая тема (по‑умолчанию) */
html:not(.dark) {
  --bg: var(--bg-light);
  --text: var(--text-light);
  --accent: var(--accent-light);
}

/* Применяем переменные */
body {
  background: var(--bg);
  color: var(--text);
}
a, .btn-primary {
  background: var(--accent);
}

/* Кнопка‑переключатель */
.theme-toggle {
  position: fixed;
  bottom: 1rem;
  right: 1rem;
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: var(--accent);
  transition: transform .2s;
}
.theme-toggle:focus-visible {
  outline: 3px solid var(--accent);
}
.theme-toggle:hover { transform: scale(1.1); }
```
**SAFE JS:**  
```js
(() => {
  const html = document.documentElement;
  const btn = document.querySelector('.theme-toggle');
  const stored = localStorage.getItem('theme');
  if (stored === 'dark') html.classList.add('dark');
  const update = () => {
    const isDark = html.classList.toggle('dark');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
    btn.setAttribute('aria-pressed', isDark);
    btn.textContent = isDark ? '☀️' : '🌙';
  };
  btn.addEventListener('click', update);
})();
```
EFFECT: Пользователь получает контроль над цветовой схемой → повышается комфорт, время на сайте и SEO‑показатели (повышенный dwell time).  
RISK: Добавление кнопки может сместить существующий контент, если её позиция конфликтует с другими фиксированными элементами.  
ROLLBACK: `git checkout index.html` или удалить добавленные блоки CSS/JS и кнопку из HTML.  
VERIFY: Открыть страницу, кликнуть кнопку – фон и текст поменяются; перезагрузить – тема сохраняется; проверить, что контраст ≥ 4.5 : 1 в обеих схемах (DevTools → Accessibility).  
PRIORITY: 2 – улучшает UX и метрики без риска для конверсий, но не критично для первого экрана.  

IDEA: SKILL — gradient-underline-hover  
KNOB: **Name:** `gradient-underline-hover`  
**When to apply:** На любой лендинге, где ссылки‑CTA оформлены без рамок и требуется визуально выделить интерактивность без изменения HTML‑структуры.  
**Steps:**  
1. Добавить в глобальный CSS правило для селектора `.btn-primary, a.cta-link`.  
2. Использовать псевдо‑элемент `::after` для градиентной линии, которая появляется при `:hover` и `:focus-visible`.  
**SAFE CSS:**  
```css
/* Базовый стиль для интерактивных ссылок */
a.cta-link,
.btn-primary {
  position: relative;
  color: inherit;
  text-decoration: none;
}

/* Градиентный подчёркнутый эффект */
a.cta-link::after,
.btn-primary::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: -2px;
  height: 3px;
  width: 0;
  background: linear-gradient(90deg, #8b5cf6, #4ec9f0);
  transition: width .3s ease;
}

/* При наведении/фокусе анимация */
a.cta-link:hover::after,
a.cta-link:focus-visible::after,
.btn-primary:hover::after,
.btn-primary:focus-visible::after {
  width: 100%;
}

/* Увеличенный таргет для доступности */
@media (pointer: coarse) {
  a.cta-link,
  .btn-primary {
    min-height: 44px;
    min-width: 44px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
  }
}
```
EFFECT: Интерактивные ссылки получают заметный, но лёгкий визуальный отклик → рост кликабельности и лучшая восприятие бренда.  
RISK: Если уже есть `::after`‑стили для тех же селекторов, может произойти конфликт; требуется проверка специфичности.  
ROLLBACK: Удалить добавленный CSS‑блок (или откатить `git checkout index.html`).  
VERIFY: Открыть страницу, наведите курсор на любую кнопку/ссылку с классом `.cta-link` или `.btn-primary` – должна появиться плавно растущая градиентная линия; проверить, что она видна и не перекрывает текст.  
PRIORITY: 3 – небольшое улучшение UX без влияния на бизнес‑метрики, но легко реализуемое.
