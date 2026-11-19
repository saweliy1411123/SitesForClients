# localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct  2026-11-17 05:42:23
duration=45.4 error=- attempts=1

IDEA: SKILL — scroll-then-animate
KNOB: 
**Name:** `scroll-then-animate`
**When to apply:** На любом статическом лендинге, где есть секции с анимацией, которые должны быть запущены при скролле.
**Safe CSS:**
```css
@keyframes slideIn {
  from { transform: translateY(100px); }
  to { transform: translateY(0); }
}

.scroll-then-animate {
  animation: slideIn 0.5s ease-in-out;
  opacity: 0;
  transition: opacity 0.5s;
}

.scroll-then-animate.show {
  opacity: 1;
  animation: slideIn 0.5s ease-in-out;
}
```
**Safe JS:**
```javascript
const elements = document.querySelectorAll('.scroll-then-animate');
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('show');
    }
  });
}, { threshold: 0.5 });
elements.forEach((element) => {
  observer.observe(element);
});
```
VERIFY: Проверить за 2–10 минут до внесения, открыв index.html в Chrome → F12 → Elements → найдя секции с анимацией, проверить, запускаются ли они при скролле.
PRIORITY: 2, потому что этот скилл улучшает пользовательский опыт на любом статическом лендинге.
SITE_REQUEST: скролл-анимация
