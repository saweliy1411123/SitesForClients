# lareper/glm-5.3-prime  2026-11-17 05:00:23
duration=20.0 error=- attempts=1

IDEA: Аудит и фикс горизонтального overflow на мобильных (блобы/широкие элементы)
KNOB: METHOD: (1) Открыть index.html, DevTools → Toggle device toolbar → iPhone SE (375px). (2) В Console выполнить: `document.documentElement.scrollWidth > document.documentElement.clientWidth` — если true, найти виновника: `document.querySelectorAll('*').forEach(el=>{if(el.scrollWidth>document.documentElement.clientWidth)console.log(el.className)})`. (3) Типичный кандидат — blob-слои с отрицательными координатами (L58, L195 и т.п.). (4) Фикс: на `body`/секции добавить `overflow-x:clip` (не hidden — не ломает position:sticky).
EFFECT: Убирается горизонтальный дёргающийся скролл на телефонах — главный источник ощущения «кривой сайт» на мобильных, где живёт большинство трафика лендинга.
RISK: `overflow-x:hidden` на предке может сломать sticky-элементы — использовать `clip`.
ROLLBACK: git checkout -- index.html (правка только в CSS-блоке).
VERIFY: Тот же однострочник в консоли до/после: должен вернуть false на 360px и 375px.
PRIORITY: 1 — частый реальный баг на лендингах с blob-декором, проверка за 2 минуты.

IDEA: WCAG-контраст вторичного текста (var(--muted)) на тёмном фоне
KNOB: METHOD: (1) В Console выполнить: `getComputedStyle(document.querySelector('.hero-note')).color` и взять фон секции. (2) Прогнать пару через любой contrast-чекер (DevTools → Elements → цвет в Styles показывает ratio). (3) Если ratio < 4.5 для основного текста (или < 3 для крупного) — поднять светлоту `--muted` в `:root` на 1–2 ступени (например, с #8a8a99 до #a0a0b0), не меняя бренд-цвета.
EFFECT: Текст «отвечаю в течение часа», подписи цен и футер становятся читаемы при ярком солнце на телефоне и для слабовидящих — меньше потерянных контактов.
RISK: Слишком светлый muted потеряет иерархию с основным текстом — двигать по 1 ступени.
ROLLBACK: git checkout -- index.html.
VERIFY: Тот же скрипт + скриншот на 375px при полной яркости экрана.
PRIORITY: 2 — влияет на читаемость ключевых microcopy (сроки, условия), но требует ручной сверки пар цветов.

IDEA: Минимальная
