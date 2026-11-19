# lareper/glm-5.3  2026-11-17 02:38:55
duration=66.9 error=- attempts=1

IDEA: SKILL — «Trust-шапка первого экрана» (hero-trust-strip)
KNOB: Название: **hero-trust-strip**. Когда применять: любой статический лендинг, где первый экран содержит h1 + подзаголовок + CTA, но нет компактной строки доказательств между подзаголовком и CTA. Шаги:
1. Найти в hero элемент подзаголовка (класс `.sub` или аналог).
2. Сразу после него вставить `<div class="trust-strip" role="list">` с 3 пунктами-фактами (город, срок, формат связи) — только реальные факты, без выдуманных цифр.
3. Стили добавить через SAFE CSS ниже; JS не требуется.
4. Проверить на 375px: полоса должна переноситься в колонку без горизонтального скролла.
SAFE CSS:
.trust-strip{display:flex;gap:14px;flex-wrap:wrap;margin:18px 0 6px;padding:0}
.trust-strip span{display:inline-flex;align-items:center;gap:8px;font-size:14px;font-weight:600;color:inherit;opacity:.85;padding:8px 14px;border:1px solid rgba(255,255,255,.12);border-radius:999px;background:rgba(255,255,255,.04)}
.trust-strip span::before{content:"";width:7px;height:7px;border-radius:50%;background:#8b5cf6;flex:none}
@media (max-width:480px){.trust-strip{flex-direction:column;align-items:flex-start}}
@media (prefers-reduced-motion: reduce){.trust-strip{transition:none}}
EFFECT: посетитель за 2 секунды видит три ключевых факта оффера (Пермь · 2 дня · бесплатное демо), растёт доверие и доскролл до CTA.
RISK: дублирование фактов, уже написанных в .sub — текст пунктов нужно согласовать, чтобы не было повторов слово в слово.
ROLLBACK: git checkout -- index.improved.html (или удалить вставленный div и блок CSS).
VERIFY: открыть копию index.improved.html на 375px и 1440px — полоса читаема, не сдвигает layout (CLS=0), скриншот до/после сравнить бок о бок.
PRIORITY: 2 — заметный конверсионный выигрыш при нулевом риске, но ниже правок CTA/оффера.
SITE_REQUEST: hero-note

IDEA: SKILL — «Мягкое свечение CTA при появлении в вьюпорте» (cta-glow-pulse)
KNOB: Название: **cta-glow-pulse**. Когда применять: любой лендинг, где главный CTA — ссылка `.btn-primary` (или аналог), находится ниже первого экрана (final-секция), и нужно привлечь внимание без агрессивных миганий. Шаги:
1. Добавить SAFE CSS в `<style>`.
2. Добавить SAFE JS в конец `<body>`: IntersectionObserver вешает класс `.is-visible` на CTA, когда он входит во вьюпорт; анимация пульса проигрывается 2 раза и останавливается (не бесконечная — уважает внимание и reduced-motion).
3. Не менять разметку кнопки — только классы.
4. Проверить: при `prefers-reduced-motion: reduce` анимация полностью отключена.
SAFE CSS:
.btn-primary{position:relative}
@keyframes cta-glow{0%,100%{box-shadow:0 0 0 0 rgba(139,92,246,0)}50%{box-shadow:0 0 0 10px rgba(139,92,246,.25)}}
.btn-primary.is-visible{animation:cta-glow 1.2s ease-in-out 2}
@media (prefers-reduced-motion: reduce){.btn-primary.is-visible{animation:none}}
SAFE JS:
document.querySelectorAll('.btn-primary').forEach(function(b){
  if(!('IntersectionObserver
