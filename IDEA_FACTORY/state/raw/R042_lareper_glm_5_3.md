# lareper/glm-5.3  2026-11-17 03:41:31
duration=65.6 error=- attempts=1

IDEA: SKILL — fluid-type-scale (премиальная типографика с clamp)
KNOB: SKILL — fluid-type-scale
Название: fluid-type-scale
Когда применять: любой лендинг, где заголовки заданы фиксированными px и на мобильных выглядят либо огромными, либо мелкими; обязательный шаг «дорогого» вида — плавная типографическая шкала.
Шаги:
1. Найти в CSS все font-size у h1/h2/h3/lead (.sub, .lead) и зафиксировать текущие значения.
2. Заменить их на clamp с тремя точками: минимум (мобильный), «резиновое» значение в vw, максимум (десктоп).
3. Задать единую шкалу: h1 clamp(2rem,5vw,3.5rem); h2 clamp(1.5rem,3.5vw,2.5rem); h3 clamp(1.1rem,2vw,1.4rem); body 16–17px; line-height 1.15 для заголовков, 1.6 для текста.
4. Добавить letter-spacing: -0.02em крупным заголовкам (премиальный «плотный» вид) и max-width ~60ch абзацам.
5. Проверить на 360px, 768px, 1440px — заголовки не переносятся по одной букве, h1 помещается в 3 строки максимум.
SAFE CSS:
```
h1{font-size:clamp(2rem,5vw,3.5rem);line-height:1.12;letter-spacing:-0.02em}
h2{font-size:clamp(1.5rem,3.5vw,2.5rem);line-height:1.15;letter-spacing:-0.015em}
h3{font-size:clamp(1.1rem,2vw,1.4rem);line-height:1.25}
p{line-height:1.6;max-width:62ch}
@media (prefers-reduced-motion: reduce){*{letter-spacing:normal}}
```
EFFECT: страница выглядит спроектированной, а не «растянутым шаблоном»; выше воспринимаемая цена услуги, меньше отказ на мобильных.
RISK: слишком агрессивный vw на промежуточных ширинах может дать неудачные переносы — подбирать точки вручную.
ROLLBACK: git checkout -- index.html (или работа в копии index.improved.html).
VERIFY: DevTools → responsive 360/768/1440, скриншоты до/после; проверить, что h1 ≤3 строк на 360px.
PRIORITY: 1 — типографика даёт максимальный «премиальный» эффект при нулевом весе.
SITE_REQUEST: font-size

IDEA: SKILL — glass-card-premium (стеклянные карточки с backdrop-filter)
KNOB: SKILL — glass-card-premium
Название: glass-card-premium
Когда применять: тёмный лендинг с цветными фоновыми блобами (
