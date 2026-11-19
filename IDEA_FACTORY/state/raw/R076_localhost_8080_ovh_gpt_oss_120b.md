# localhost:8080/ovh/gpt-oss-120b  2026-11-17 05:22:28
duration=23.5 error=- attempts=1

IDEA: SKILL — dark-mode-toggle  
KNOB: **Name:** `dark-mode-toggle`  
**When to apply:** На статических лендингах, где бренд‑цвета работают в светлой и тёмной палитре, чтобы повысить доступность и современный имидж.  
**Steps:**  
1. В `<header>` (или сразу после `<body>`) добавить кнопку‑переключатель:  
   ```html
   <button class="theme-toggle" aria-label="Переключить тему" type="button">🌙</button>
   ```  
2. В `<style>` (или в отдельный CSS‑файл) объявить переменные цветов для светлой темы и задать их как `var(--c‑bg)`, `var(--c‑text)` и т.д.  
3. Добавить правила для темного режима под атрибут `[data-theme="dark"]`.  
4. В конце `<body>` вставить безопасный скрипт, который:  
   - читает `localStorage.getItem('theme')`;  
   - при загрузке ставит `document.documentElement.dataset.theme = stored` (если есть);  
   - при клике на `.theme-toggle` переключает значение между `light` и `dark`, сохраняет в `localStorage` и обновляет атрибут.  

**SAFE CSS:**  
```css
:root{
  --c-bg:#ffffff;
  --c-text:#111111;
  --c-primary:#8b5cf6;
}
[data-theme="dark"]{
  --c-bg:#111111;
  --c-text:#f0f0f0;
  --c-primary:#a78bfa;
}
body{
  background:var(--c-bg);
  color:var(--c-text);
  transition:background .3s, color .3s;
}
.theme-toggle{
  background:none;
  border:none;
  font-size:1.5rem;
  cursor:pointer;
  color:var(--c-primary);
  transition:color .3s;
}
.theme-toggle:focus-visible{
  outline:2px solid var(--c-primary);
  outline-offset:2px;
}
```  

**SAFE JS:**  
```js
(() => {
  const root = document.documentElement;
  const btn = document.querySelector('.theme-toggle');
  const stored = localStorage.getItem('theme');
  if (stored) root.dataset.theme = stored;
  btn?.addEventListener('click', () => {
    const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next;
    localStorage.setItem('theme', next);
  });
})();
```  

EFFECT: Улучшает восприятие сайта у пользователей, предпочитающих тёмный режим; повышает показатель доступности (WCAG 2.1 AA) и может увеличить время пребывания на странице.  
RISK: Добавление кнопки может слегка изменить визуальный баланс первого экрана; небольшая задержка при первом переключении из‑за чтения `localStorage`.  
ROLLBACK: `git checkout index.improved.html` или удалить добавленные строки/файлы (кнопка, CSS‑переменные, скрипт).  
VERIFY: Открыть страницу в браузере, кликнуть кнопку – фон и текст должны поменяться; перезагрузить – выбранная тема сохраняется; проверить, что нет «шипения» (CLS) и что фокус‑индикатор виден.  
PRIORITY: 2 – небольшие изменения, быстрый ROI за счёт улучшения UX и SEO‑оценки доступности.  

---  

IDEA: SKILL — scroll-progress-bar  
KNOB: **Name:** `scroll-progress-bar`  
**When to apply:** На одностраничных лендингах, где пользователь прокручивает контент от начала до конца; индикатор прогресса повышает ориентацию и мотивирует дочитывать страницу.  
**Steps:**  
1. В начале `<body>` добавить пустой элемент‑контейнер:  
   ```html
   <div class="scroll-progress" aria-hidden="true"></div>
   ```  
2. В CSS задать фиксированную высоту, ширину 0 % и стили оформления.  
3. В безопасном JS‑скрипте отследить событие `scroll`, вычислить процент прокрутки (`(scrollY / (document.body.scrollHeight - innerHeight)) * 100`) и установить `style.width` у `.scroll-progress`.  

**SAFE CSS:**  
```css
.scroll-progress{
  position:fixed;
  top:0; left:0;
  height:4px;
  width:0%;
  background:linear-gradient(90deg,var(--c-primary),#a78bfa);
  z-index:9999;
  transition:width .1s ease-out;
}
```  

**SAFE JS:**  
```js
(() => {
  const bar = document.querySelector('.scroll-progress');
  const update = () => {
    const scroll = window.scrollY;
    const height = document.body.scrollHeight - innerHeight;
    const perc = height ? (scroll / height) * 100 : 0;
    bar.style.width = perc + '%';
  };
  window.addEventListener('scroll', update);
  window.addEventListener('resize', update);
  update();
})();
```  

EFFECT: Пользователь видит визуальный индикатор, сколько контента осталось, что повышает вовлечённость и может улучшить конверсию (меньше «потери» на середине страницы).  
RISK: На очень коротких страницах индикатор будет почти сразу заполнен; небольшое увеличение JS‑веса (~1 KB).  
ROLLBACK: Удалить строку `<div class="scroll-progress">`, CSS‑блок и JS‑скрипт; либо выполнить `git checkout index.improved.html`.  
VERIFY: Прокрутить страницу – индикатор должен плавно заполняться от 0 % до 100 %; проверить, что он остаётся вверху при скролле и не перекрывает важные элементы.  
PRIORITY: 1 – быстрый, заметный UX‑улучшение без изменения контента; положительно влияет на метрики поведения (scroll depth) и может быть измерено через A/B‑тест.
