# localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct  2026-11-17 03:18:30
duration=31.6 error=- attempts=1

IDEA: SKILL — Scroll-Triggered Gradient Background
KNOB: 
### Название
scroll-triggered-gradient
### Когда применять
Любой лендинг с длинной прокруткой, где нужно улучшить визуальный интерес и выделить определенные секции.
### Шаги
1. Определить секции, где будет применяться градиент.
2. Добавить класс `scroll-gradient` к этим секциям.
3. В CSS добавить стили для `.scroll-gradient`.
### SAFE CSS:
```css
.scroll-gradient {
  background-image: linear-gradient(to bottom, #8b5cf6, #6a44f4);
  background-size: 100% 300px;
  background-position: 0% 100%;
}

.scroll-gradient.show-gradient {
  background-position: 0% 0%;
  transition: background-position 1s ease-out;
}
```
### SAFE JS:
```javascript
const gradientSections = document.querySelectorAll('.scroll-gradient');

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('show-gradient');
    } else {
      entry.target.classList.remove('show-gradient');
    }
  });
}, { threshold: 0.5 });

gradientSections.forEach((section) => {
  observer.observe(section);
});
```
EFFECT: Добавление градиентного фона к определенным секциям при прокрутке улучшает визуальный интерес и делает контент более привлекательным.
RISK: Нет значительных рисков, но необходимо проверить совместимость с другими стилями и скриптами.
ROLLBACK: Удалить добавленные классы и стили.
VERIFY: Проверить визуально, что градиент появляется при прокрутке к определенным секциям.
PRIORITY: 2, так как это улучшение визуального интереса и не влияет напрямую на конверсию или SEO.
SITE_REQUEST: gradient
