# localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct  2026-11-17 08:04:58
duration=24.3 error=- attempts=1

IDEA: SKILL — scroll-reveal-fade-in
KNOB: 
**Name:** scroll-reveal-fade-in
**When to apply:** На любом статическом лендинге, где есть секции с заголовками и текстом.
**Steps:** 
1. Добавить класс `scroll-reveal` к каждой секции, которую нужно показывать при скролле.
2. Добавить CSS-правило `.scroll-reveal { opacity: 0; transition: opacity 0.5s; }`.
3. Добавить JS-код, который будет показывать секции при скролле.
SAFE CSS: 
```css
.scroll-reveal {
  opacity: 0;
  transition: opacity 0.5s;
}

.scroll-reveal.visible {
  opacity: 1;
}
```
SAFE JS: 
```javascript
const scrollRevealElements = document.querySelectorAll('.scroll-reveal');

window.addEventListener('scroll', () => {
  scrollRevealElements.forEach(element => {
    const rect = element.getBoundingClientRect();
    if (rect.top < window.innerHeight) {
      element.classList.add('visible');
    }
  });
});
```
EFFECT: Секции будут появляться при скролле, создавая эффект постепенного открытия контента.
RISK: Может потребоваться корректировка CSS-правил и JS-кода для правильной работы на разных устройствах и браузерах.
ROLLBACK: Удалить класс `scroll-reveal` и соответствующие CSS-правила и JS-код.
VERIFY: Проверить, что секции появляются при скролле, и что эффект выглядит плавно и естественно.
PRIORITY: 2, так как это улучшение пользовательского опыта, но не критическое для функциональности сайта.
SITE_REQUEST: None
SKILL: scroll-reveal-fade-in
