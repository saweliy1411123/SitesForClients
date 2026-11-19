# localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct  2026-11-17 02:37:59
duration=10.9 error=- attempts=1

IDEA: SKILL — Dark Mode Toggle
KNOB: 
### Название
Dark Mode Toggle
### Когда применять
При необходимости добавления переключателя темного режима
### Шаги
1. Добавить CSS-переменные для цветов темы
2. Добавить переключатель-кнопку, меняющую `data-theme` на `<html>`
3. Обновить стили элементов в зависимости от активной темы
SAFE CSS:
```css
:root {
  --bg: #0a0a0f;
  --text: #fff;
}

[data-theme="dark"] {
  background-color: var(--bg);
  color: var(--text);
}

[data-theme="light"] {
  background-color: #fff;
  color: #000;
}

.toggle-button {
  position: absolute;
  top: 10px;
  right: 10px;
}

.toggle-button:checked + .toggle-content {
  background-color: var(--bg);
  color: var(--text);
}
```
SAFE JS:
```javascript
const toggleButton = document.querySelector('.toggle-button');
const htmlElement = document.querySelector('html');

toggleButton.addEventListener('change', () => {
  htmlElement.dataset.theme = htmlElement.dataset.theme === 'dark' ? 'light' : 'dark';
});
```
PRIORITY: 2
SITE_REQUEST: «toggle»
