# localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct  2026-11-17 01:56:52
duration=24.5 error=- attempts=1

IDEA: SKILL — Быстрая доступность
KNOB: 
### Название
Быстрая доступность
### Когда применять
При необходимости улучшения доступности сайта
### Конкретные шаги
1. Добавить атрибут `aria-label` к ссылкам, не имеющим описательного текста.
2. Обернуть основной контент в семантический `<main id="main">`.
3. Добавить `font-display: swap` и предзагрузку шрифтов Google Fonts.
### SAFE CSS:
```css
@media (prefers-reduced-motion: reduce) {
  animation: none !important;
}

main {
  display: block;
}

.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background-color: #fff;
  color: #000;
  padding: 10px;
  z-index: 100;
}

.skip-link:focus {
  top: 0;
}
```
### SAFE JS:
```javascript
// добавить обработчик события focus на кнопку "Перейти к содержимому"
document.addEventListener('DOMContentLoaded', function() {
  const skipLink = document.querySelector('.skip-link');
  skipLink.addEventListener('click', function() {
    const main = document.getElementById('main');
    main.focus();
  });
});
```
PRIORITY: 1
SITE_REQUEST: доступность
SKILL: Быстрая доступность
