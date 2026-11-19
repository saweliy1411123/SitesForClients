# lareper/glm-5.2-fast-preview  2026-11-17 06:07:07
duration=28.7 error=- attempts=1

IDEA: SKILL — fluid-type-scale (премиальная типографика на clamp с золотой шкалой)
KNOB: SKILL — fluid-type-scale
Name: `fluid-type-scale`
When to apply: на любом статическом лендинге, где размеры заголовков заданы отдельными clamp-значениями без единой системы — из-за этого h2 в разных секциях «прыгают» и типографика выглядит самодельной.
Steps:
1. В `<style>` в блок `:root` добавить CSS-переменные шкалы (см. SAFE CSS).
2. Заменить существующие `font-size: clamp(...)` у h1/h2/h3 на `var(--fs-h1)`, `var(--fs-h2)`, `var(--fs-h3)`; для body/lead — `var(--fs-body)`.
3. Добавить `letter-spacing:-.02em` крупным заголовкам и `line-height:1.15` h1/h2, `line-height:1.6` абзацам — «дорогой» ритм.
4. Проверить на 320px и 1440px, что ни один заголовок не переносится по одной букве.
SAFE CSS:
```css
:root{
--fs-h1:clamp(30px,5.2vw,58px);
--fs-h2:clamp(26px,4vw,44px);
--fs-h3:clamp(18px,2.2vw,22px);
--fs-body:clamp(15.5px,1.6vw,18px);
}
h1{font-size:var(--fs-h1);line-height:1.15;letter-spacing:-.02em}
h2{font-size:var(--fs-h2);line-height:1.18;letter-spacing:-.015em}
h3{font-size:var(--fs-h3);line-height:1.35}
p,li{font-size:var(--fs-body);line-height:1.6}
```
EFFECT: единая типографическая шкала — страница воспринимается как работа дизайнера, а не шаблон; меньше визуального шума, выше доверие к цене.
RISK: точечная замена clamp-значений в 937 строках может задеть специфичные размеры (`.price-card .price` 58px) — их оставить как есть.
ROLLBACK: `git checkout -- index.html` (или восстановить из копии index.improved.html.bak).
VERIFY: до/после открыть страницу на 320px, 768px, 1440px; убедиться, что h1/h2 во всех 7 секциях визуально одного размера внутри своего уровня (5 минут, скриншоты рядом).
PRIORITY: 2 — заметный премиум-эффект при низком риске, но требует аккуратной замены в CSS.
SITE_REQUEST: font-size

IDEA: SKILL — shimmer-border-card (живая переливающаяся рамка премиум-карточек)
KNOB: SKILL — shimmer-border-card
Name: `shimmer-border-card`
When to apply: на любом лендинге, где есть одна выделенная карточка (цена, тариф, оффер) и её нужно визуально «поднять» без картинок и библиотек.
Steps:
1. Обернуть целевую карточку (`.
