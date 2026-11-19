# localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct  2026-11-17 04:40:34
duration=11.3 error=- attempts=1

IDEA: SKILL — scroll-snap-carousel
KNOB: 
**Name:** `scroll-snap-carousel`
**When to apply:** На лендингах с крупными визуальными блоками.
**SAFE CSS:**
```css
.scroll-snap-carousel {
  display: flex;
  flex-wrap: nowrap;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
}

.scroll-snap-carousel > * {
  flex: 0 0 100%;
  height: 100vh;
  scroll-snap-align: start;
}
```
**SAFE JS:** (нет)
EFFECT: Улучшение пользовательского опыта за счет визуальной карусели.
RISK: Требует решения владельца для адаптации к существующему контенту.
ROLLBACK: Удалить добавленный CSS-код.
VERIFY: Проверить визуальное качество и скорость загрузки карусели.
PRIORITY: 2, улучшает пользовательский опыт.
SITE_REQUEST: scroll-snap-carousel
SKILL: scroll-snap-carousel
