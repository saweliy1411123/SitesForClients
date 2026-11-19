# lareper/glm-5.3-prime  2026-11-17 06:50:44
duration=13.2 error=- attempts=1

IDEA: SKILL — price-card-glare-sweep (блик света, пробегающий по премиум-карточке цены при hover)
KNOB: SKILL — price-card-glare-sweep
Name: `price-card-glare-sweep`
When to apply: на любом лендинге, где есть одна выделенная карточка цены (`.price-card`) и нужно ощущение «дорогого» продукта без картинок и библиотек.
Steps:
1. Убедиться, что карточка имеет `position:relative` и `overflow:hidden`.
2. Добавить псевдоэлемент-блик, который по умолчанию сдвинут за пределы карточки.
3. На hover/focus-within блик плавно проезжает по диагонали.
4. Обернуть анимации в `@media (prefers-reduced-motion: no-preference)`.
5. Проверить, что блик не перекрывает текст (pointer-events нет у псевдоэлементов по умолчанию — ок).

SAFE CSS:
```css
.price-card{position:relative;overflow:hidden}
@media (prefers-reduced-motion: no-preference){
.price-card::after{
content:'';position:absolute;top:-60%;left:-80%;
width:60%;height:220%;
background:linear-gradient(105deg,transparent 30%,rgba(255,255,255,.14) 48%,rgba(255,255,255,.05) 55%,transparent 70%);
transform:rotate(8deg) translateX(0);pointer-events:none;transition:transform .9s cubic-bezier(.22,.61,.36,1)}
.price-card:hover::after,.price-card:focus-within::after{transform:rotate(8deg) translateX(320%)}
}
```
EFFECT: карточка цены воспринимается как премиальный объект; hover-микровзаимодействие удерживает внимание на главном оффере, не отвлекая от текста.
RISK: на очень узких экранах блик может визуально «гулять» при скролле тач-устройств — ограничить hover-медиа при необходимости.
ROLLBACK: git checkout -- index.html (или удалить добавленный CSS-блок из index.improved.html).
VERIFY: открыть страницу, навести курсор на `.price-card` — блик должен проехать один раз; проверить Tab-фокус на кнопке внутри карточки; включить эмуляцию prefers-reduced-motion в DevTools → Rendering и убедиться, что анимации нет.
PRIORITY: 2 — чистая косметика, но дешёвая и работает именно на тему раунда «дорогой сайт» в самой конверсионной секции.

IDEA: SKILL — premium-tracking-headings (тонкий letter-spacing/word-spacing ритм для «дорогой» типографики)
KNOB: SKILL — premium-tracking-headings
Name: `premium-tracking-headings`
When to apply: на любом лендинге, где крупные заголовки (h1/h2) выглядят «плотно» и дёшево из-за дефолтного трекинга; особенно при отрицательном letter-spacing, доведённом до экстремума.
Steps:
1. Найти текущие значения letter-spacing у h1/h2 (у `.price-card .price` уже −.04em — экстремум).
2. Задать иерархию трекинга: чем крупнее текст — тем плотнее, но в пределах −.01…−.03em; крупным цифрам цены вернуть −.02em вместо −.04em.
3. Добавить `font-feature-settings:"k
