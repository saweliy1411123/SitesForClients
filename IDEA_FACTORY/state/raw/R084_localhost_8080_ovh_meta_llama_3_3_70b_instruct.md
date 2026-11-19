# localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct  2026-11-17 05:45:28
duration=14.6 error=- attempts=1

IDEA: premium-parallax-hero
KNOB: 
**Name:** `premium-parallax-hero`
**When to apply:** На любом статическом лендинге, где герой-секция имеет большой фон.
**SAFE CSS:**
```css
.hero {
  background-size: 150% auto;
  background-position: 50% 50%;
}
.hero::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to bottom, var(--bg), var(--bg));
  background-size: 150% auto;
  background-position: 50% 50%;
  transform: translateZ(-10px);
  transition: transform 0.5s ease;
}
.hero:hover::before {
  transform: translateZ(0);
}
```
EFFECT: Создаст премиальный параллакс-эффект в герой-секции.
RISK: Может не работать корректно на всех устройствах и браузерах.
ROLLBACK: Удалить добавленный CSS-код.
VERIFY: Проверить работу параллакс-эффекта в разных браузерах и на разных устройствах.
PRIORITY: 2
SITE_REQUEST: parallax
SKILL: premium-parallax-hero
