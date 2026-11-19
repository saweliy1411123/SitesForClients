# localhost:8080/ovh/gpt-oss-120b  2026-11-17 02:18:13
duration=31.1 error=- attempts=1

IDEA: SKILL — Accessible Focus Outline for Interactive Elements  
KNOB: METHOD: Create a reusable “focus‑visible” skill that globally applies a high‑contrast outline to every keyboard‑focusable element (links, buttons, inputs, custom interactive blocks). The skill is stored as `SKILLS/focus-visible.md` and injected into any static landing page via a single `<link rel="stylesheet" href="focus-visible.css">` tag.  

**Skill body (focus-visible.md)**  
```markdown
# Accessible Focus Outline  
## Когда применять  
- На любом сайте, где интерактивные элементы реализованы только через `<a>`‑ссылки или кастомные блоки без нативных `<button>`/`<input>`.  
- Чтобы обеспечить соответствие WCAG 2.1 AA (2.4.7 Focus Visible) без изменения существующего HTML.  

## Шаги внедрения  
1. Скопировать `focus-visible.css` в корень проекта.  
2. В `<head>` добавить `<link rel="stylesheet" href="focus-visible.css">`.  
3. При необходимости переопределить переменные `--focus-color` и `--focus-width` в локальном CSS.  

## SAFE CSS:  
```css
:root {  
  --focus-color: #ffb800; /* ярко‑желтый, контраст > 4.5 */  
  --focus-width: 3px;  
  --focus-offset: 2px;  
}

/* Применяем только когда браузер поддерживает :focus-visible */  
*:focus-visible {  
  outline: var(--focus-width) solid var(--focus-color);  
  outline-offset: var(--focus-offset);  
}

/* Фоллбэк для браузеров без :focus-visible */  
*:focus:not(:focus-visible) {  
  outline: none;  
}

/* Сброс для элементов, где уже есть кастомный outline */  
button:focus-visible, a:focus-visible, [role="button"]:focus-visible, [tabindex]:focus-visible {  
  outline: var(--focus-width) solid var(--focus-color) !important;  
  outline-offset: var(--focus-offset) !important;  
}
```  

## SAFE JS (опционально) – принудительный :focus-visible в Safari ≤14  
```js
// Добавляем класс .js-focus-visible к элементам, получившим фокус клавиатурой
document.addEventListener('keydown', e => {
  if (e.key === 'Tab') {
    document.body.classList.add('js-keyboard');
  }
});
document.addEventListener('focusin', e => {
  if (document.body.classList.contains('js-keyboard')) {
    e.target.classList.add('focus-visible');
  }
});
document.addEventListener('focusout', e => e.target.classList.remove('focus-visible'));
```  

EFFECT: Улучшает доступность для пользователей клавиатуры и скрин‑ридеров, повышает доверие и может положительно влиять на SEO‑оценку (Core Web Vitals‑accessibility).  

RISK: Возможен конфликт с уже существующими кастомными outline‑стилями, что может привести к двойному отображению рамки.  

ROLLBACK: Удалить `focus-visible.css` и строку `<link …>` из `<head>` (или выполнить `git checkout -- focus-visible.css index.html`).  

VERIFY: Открыть страницу, нажать `Tab` несколько раз – каждый интерактивный элемент должен получить яркую жёлтую рамку; проверить контраст через DevTools → Accessibility; убедиться, что при клике мышью рамка не появляется.  

PRIORITY: 2 – важна для всех сайтов, но не критична для первой версии лендинга, поэтому ставим средний приоритет.  

---  

IDEA: SKILL — Magnetic Button Effect (Hover‑Magnet)  
KNOB: METHOD: Создать переносимый «магнитный» эффект для CTA‑кнопок, который слегка притягивает курсор к центру кнопки и возвращает её в исходное положение при уходе курсора. Файл `magnetic-button.css` + небольшой `magnetic-button.js` подключается одной строкой `<script src="magnetic-button.js" defer></script>` и классом `.magnetic` к любой ссылке/кнопке.  

**Skill body (magnetic-button.md)**  
```markdown
# Magnetic Button  
## Когда применять  
- Для CTA‑кнопок в hero‑секции, фиксированных панелей и любых ярких ссылок, где требуется визуальная «привлекательность» без ущерба производительности.  
- На статических лендингах без сложных JS‑фреймворков.  

## Шаги внедрения  
1. Скопировать `magnetic-button.css` и `magnetic-button.js` в корень проекта.  
2. В `<head>` добавить `<link rel="stylesheet" href="magnetic-button.css">`.  
3. В конце `<body>` добавить `<script src="magnetic-button.js" defer></script>`.  
4. Добавить класс `magnetic` к любой `<a>`/`<button>` элементу, который должен иметь эффект.  

## SAFE CSS:  
```css
/* Базовый стиль кнопки, сохраняет существующий .btn-primary */  
.btn-primary.magnetic {  
  position: relative;  
  overflow: hidden;  
  transition: transform 0.2s ease-out;  
}

/* Плавный переход при возврате */  
.btn-primary.magnetic:hover {  
  transform: translate3d(0, 0, 0);  
}
```  

## SAFE JS:  
```js
// Магнитный эффект без внешних библиотек, работает в современных браузерах
document.querySelectorAll('.magnetic').forEach(btn => {
  const strength = 30; // пикселей отклонения
  const rect = btn.getBoundingClientRect();

  const move = e => {
    const x = e.clientX - (rect.left + rect.width / 2);
    const y = e.clientY - (rect.top + rect.height / 2);
    const dx = (x / rect.width) * strength;
    const dy = (y / rect.height) * strength;
    btn.style.transform = `translate(${dx}px, ${dy}px)`;
  };

  const reset = () => {
    btn.style.transform = 'translate(0,0)';
  };

  btn.addEventListener('mousemove', move);
  btn.addEventListener('mouseleave', reset);
});
```  

EFFECT: Увеличивает визуальное вовлечение и воспринимаемую «интерактивность» кнопок, повышая CTR на CTA‑элементы без добавления тяжёлых библиотек.  

RISK: На слабых устройствах (старый смартфон) может слегка повысить нагрузку CPU из‑за частых `mousemove`‑событий.  

ROLLBACK: Удалить `magnetic-button.css`, `magnetic-button.js` и соответствующие `<link>`/`<script>` строки; либо выполнить `git checkout -- magnetic-button.* index.html`.  

VERIFY: Открыть страницу в Chrome, навести курсор на кнопку с классом `magnetic` – должна наблюдаться небольшая «притягивающая» анимация; протестировать на мобильном (должно работать без эффекта, т.к. `mousemove` не вызывается).  

PRIORITY: 1 – небольшое изменение, которое сразу повышает конверсию CTA, поэтому ставим высокий приоритет.
