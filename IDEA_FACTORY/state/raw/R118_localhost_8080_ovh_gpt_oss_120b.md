# localhost:8080/ovh/gpt-oss-120b  2026-11-17 07:26:24
duration=24.0 error=- attempts=1

IDEA: SKILL — dark-mode-toggle  
KNOB: **Name:** dark-mode-toggle  
**When to apply:** На любом статическом лендинге, где уже используются CSS‑переменные для цветов (как в текущем `index.html`). Позволяет пользователю переключать светлую/тёмную тему, повышая читаемость и удовлетворённость UX.  
**Steps:**  
1. В `<head>` добавить блок `<style id="dark-mode-vars">` с переменными‑цветами для тёмной темы (`--bg-dark`, `--text-dark`, `--violet-dark` и пр.).  
2. В `<body>` сразу после открывающего тега вставить кнопку‑переключатель:  
   ```html
   <button class="dark-toggle" aria-label="Переключить тёмную тему" title="Тёмная тема">
     🌙
   </button>
   ```  
3. Добавить CSS‑правило, которое при наличии класса `dark` на `<html>` переопределяет переменные:  
   ```css
   html.dark {
     --bg: var(--bg-dark);
     --text: var(--text-dark);
     --violet: var(--violet-dark);
   }
   ```  
4. Добавить небольшой скрипт, который:  
   - читает `localStorage.getItem('darkMode')`;  
   - при клике по `.dark-toggle` переключает класс `dark` у `<html>` и сохраняет новое значение;  
   - при загрузке страницы применяет сохранённую тему.  
5. При желании добавить медиазапрос `@media (prefers-color-scheme: dark)` для автодефолтного включения.  

**SAFE CSS:**  
```css
/* dark‑mode variables */
:root {
  --bg-dark: #111827;
  --text-dark: #e5e7eb;
  --violet-dark: #a78bfa;
}

/* toggle button */
.dark-toggle {
  position: fixed;
  bottom: 1rem;
  right: 1rem;
  background: var(--violet);
  color: #fff;
  border: none;
  border-radius: 50%;
  width: 44px;
  height: 44px;
  font-size: 1.2rem;
  cursor: pointer;
  z-index: 1000;
  transition: background .3s;
}
.dark-toggle:hover { background: var(--violet-dark); }
```

**SAFE JS:**  
```js
(() => {
  const key = 'darkMode';
  const html = document.documentElement;
  const btn = document.querySelector('.dark-toggle');

  const apply = (on) => {
    html.classList.toggle('dark', on);
    localStorage.setItem(key, on ? '1' : '');
  };

  // init from storage or system preference
  const stored = localStorage.getItem(key);
  const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  apply(stored ? true : prefersDark);

  btn?.addEventListener('click', () => apply(!html.classList.contains('dark')));
})();
```

EFFECT: Пользователь может переключать темы, что повышает комфорт чтения, улучшает показатель Core Web Vitals (меньше «blink» при смене цветов) и может увеличить конверсию за счёт более приятного UX.  

RISK: Добавление небольшого JS; при конфликте имен переменных возможны неожиданные цветовые изменения (требует проверки, что все цвета берутся из переменных).  

ROLLBACK: `git checkout index.html` или удалить блоки `<style id="dark-mode-vars">`, кнопку `.dark-toggle` и скрипт‑блок.  

VERIFY: Открыть страницу в браузере, кликнуть кнопку‑переключатель – фон, текст и акценты должны смениться; перезагрузить – выбранная тема сохраняется; проверить в DevTools → Computed, что переменные изменились.  

PRIORITY: 2 – высокий пользовательский эффект при минимальном объёме кода и низком риске.  

---  

IDEA: SKILL — svg-accessibility-enhancer  
KNOB: **Name:** svg-accessibility-enhancer  
**When to apply:** На любой странице, где используются инлайн‑SVG‑иконки (как в текущем `index.html`). Делает SVG‑элементы доступными для скрин‑ридеров без изменения визуального вида.  
**Steps:**  
1. С помощью скрипта найти все `<svg>` в документе.  
2. Если у SVG уже есть `<title>` / `<desc>` – добавить `role="img"` и `aria-labelledby="titleId descId"` (при отсутствии `id`‑ов – сгенерировать уникальные).  
3. Если SVG используется только как декоративный (например, в фоне блока) – добавить `aria-hidden="true"` и `focusable="false"`.  
4. При необходимости добавить атрибут `role="presentation"` для полностью декоративных элементов.  

**SAFE CSS:** *(не требуется, стили уже заданы)*  

**SAFE JS:**  
```js
(() => {
  const svgs = document.querySelectorAll('svg:not([role])');
  svgs.forEach((svg, i) => {
    const hasDesc = svg.querySelector('title,desc');
    if (hasDesc) {
      const title = svg.querySelector('title');
      const desc = svg.querySelector('desc');
      const titleId = title?.id || `svgTitle${i}`;
      const descId = desc?.id || `svgDesc${i}`;
      if (title && !title.id) title.id = titleId;
      if (desc && !desc.id) desc.id = descId;
      svg.setAttribute('role', 'img');
      svg.setAttribute('aria-labelledby', `${titleId} ${descId}`.trim());
    } else {
      svg.setAttribute('aria-hidden', 'true');
      svg.setAttribute('focusable', 'false');
    }
  });
})();
```

EFFECT: Скрин‑ридеры объявляют смысловые иконки, улучшая WCAG AA/AAA‑соответствие и потенциально повышая SEO (структурированные данные учитывают доступный контент).  

RISK: При ошибочном определении декоративных SVG может появиться лишний шум в озвучке; требуется проверка вручную для критически важных иконок.  

ROLLBACK: Удалить добавленный `<script>`‑блок и, при необходимости, откатить изменения в файле через `git checkout index.html`.  

VERIFY: Открыть DevTools → Accessibility, выбрать любой SVG‑элемент – в “Accessibility Tree” должно отображаться “img” с соответствующим именем или “ignored” для декоративных; также проверить, что нет предупреждений axe (категория “ARIA”).  

PRIORITY: 1 – критическая доступность, небольшие изменения, мгновенный выигрыш в SEO и пользовательском опыте.
