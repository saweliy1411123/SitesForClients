# lareper/glm-5.3  2026-11-17 07:09:27
duration=2.4 error=- attempts=1

IDEA: SKILL — hero-light-sweep (пробегающий световой блик по hero-панели, «дорогой» свет)
KNOB: SKILL — hero-light-sweep
Name: `hero-light-sweep`
When to apply: на любом статическом лендинге, где hero-секция имеет тёмный/градиентный фон или стеклянную панель — добавить мягкий диагональный световой блик, медленно проходящий по панели, чтобы первый экран выглядел премиально. Без внешних библиотек, чистый CSS.

Steps:
1. В hero-секции найти контейнер первого экрана (`.hero .wrap` или аналогичный) и добавить внутрь первым ребёнком `<div class="light-sweep" aria-hidden="true"></div>`.
2. Добавить CSS из блока SAFE CSS ниже (в конец `<style>`).
3. Убедиться, что у `.hero` есть `position:relative; overflow:hidden;`.
4. Проверить на мобильном: блик не должен перекрывать текст (z-index ниже контента).

SAFE CSS:
```css
.hero{position:relative;overflow:hidden}
.light-sweep{
  position:absolute;inset:-20%;
  pointer-events:none;z-index:0;
  background:linear-gradient(115deg,
    transparent 42%,
    rgba(255,255,255,.06) 48%,
    rgba(255,255,255,.14) 50%,
    rgba(255,255,255,.06) 52%,
    transparent 58%);
  transform:translateX(-60%);
  animation:lightSweep 9s ease-in-out infinite;
  will-change:transform;
}
@keyframes lightSweep{
  0%{transform:translateX(-60%) rotate(0deg)}
  50%{transform:translateX(60%) rotate(0deg)}
  100%{transform:translateX(-60%) rotate(0deg)}
}
@media (prefers-reduced-motion: reduce){
  .light-sweep{animation:none;opacity:.5;transform:translateX(0)}
}
```
(контент hero при необходимости поднять: `.hero .wrap{position:relative;z-index:1}`)

EFFECT: hero выглядит «дорогим» без картинок и библиотек; свет задаёт ощущение премиума, повышая воспринимаемую ценность услуги «лендинг за 2 дня» — визуальная метафора продукта на самом сайте.
RISK: на слабых мобильных GPU бесконечная анимация большого слоя может дать лёгкий джиттер — смягчается media-query и will-change.
ROLLBACK: `git checkout -- index.html` (или удалить div `.light-sweep` и блок CSS из копии index.improved.html).
VERIFY: (1) открыть index.improved.html, 10 секунд наблюдать hero — блик проходит плавно, текст читаем; (2) DevTools → Rendering → Emulate prefers-reduced-motion: reduce — анимация отключается; (3) Lighthouse Performance до/после — CLS = 0, FPS на мобильном эмуляторе ≥ 55.
PRIORITY: 2 — чисто декоративный премиум-эффект, но нулевой вес (только CSS), нулевой CLS и прямой «продающий» эффект на первом экране, где решается конверсия.
SKILL: hero-light-sweep

IDEA: SKILL — focus-glow-ring (премиальное световое кольцо на клавиатурном фокусе)
KNOB: SKILL — focus-glow-ring
Name: `focus-glow-ring`
When to apply: на любом лендинге, где есть ссылки-CTA, пункты меню и FAQ `<summary>` — заменить «стандартную» рамку фокуса на мягкое светящееся кольцо в фирменном цвете, чтобы навигация с клавиатуры выглядела продуманной и премиальной (a11y + стиль одновременно).

Steps:
1. В конец `<style>` добавить CSS из SAFE CSS.
2. Уб
