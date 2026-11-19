# localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct  2026-11-17 07:26:35
duration=35.7 error=- attempts=1

IDEA: SKILL — sticky-header-reveal
KNOB: 
**Name:** sticky-header-reveal
**When to apply:** На лендингах с крупной hero-секцией и фиксированным верхним меню.
**SAFE CSS:**
```css
.sticky-header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background-color: var(--bg);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  z-index: 1000;
  transform: translateY(-100%);
  transition: transform 0.3s ease-in-out;
}

.sticky-header.reveal {
  transform: translateY(0);
}

.sticky-header nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
}

.sticky-header nav a {
  color: var(--text);
  text-decoration: none;
  transition: color 0.2s ease-in-out;
}

.sticky-header nav a:hover {
  color: var(--link-hover);
}
```
**SAFE JS:**
```javascript
const header = document.querySelector('.sticky-header');

window.addEventListener('scroll', () => {
  const scrollPosition = window.scrollY;
  if (scrollPosition > 200) {
    header.classList.add('reveal');
  } else {
    header.classList.remove('reveal');
  }
});
```
EFFECT: Улучшает навигацию и пользовательский опыт на лендингах с крупной hero-секцией и фиксированным верхним меню.
RISK: Нет значительных рисков, но может потребоваться корректировка стилей и скриптов для адаптации к конкретному дизайну лендинга.
ROLLBACK: Удалить добавленный CSS и JS-код.
VERIFY: Проверить визуальное отображение и функциональность фиксированного меню на разных устройствах и разрешениях.
PRIORITY: 2
SKILL: sticky-header-reveal
