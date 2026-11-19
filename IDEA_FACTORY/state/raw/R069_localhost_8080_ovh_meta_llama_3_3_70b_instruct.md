# localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct  2026-11-17 05:01:44
duration=11.9 error=- attempts=1

IDEA: scroll-snap-carousel
KNOB: METHOD: SKILL — scroll-snap-carousel
**Name:** `scroll-snap-carousel`
**When to apply:** На лендингах с крупными визуальными блоками.
**SAFE CSS:**
```css
.demo-carousel {
  display: flex;
  overflow: hidden;
  scroll-snap-type: x mandatory;
}
.demo-carousel > * {
  flex: 0 0 100%;
  scroll-snap-align: start;
}
```
**SAFE JS:** (необязательно)
```javascript
// нет
```
EFFECT: Улучшение пользовательского опыта за счет создания интерактивного каруселя для демонстрации демо-карточек.
RISK: Нет рисков.
ROLLBACK: Удалить добавленный CSS-код.
VERIFY: Проверить работу каруселя, просматривая страницу на разных устройствах.
PRIORITY: 2, потому что улучшает пользовательский опыт и делает контент более доступным.
SITE_REQUEST: нет
SKILL: scroll-snap-carousel
