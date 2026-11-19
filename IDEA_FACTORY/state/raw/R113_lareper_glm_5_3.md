# lareper/glm-5.3  2026-11-17 07:12:11
duration=40.2 error=- attempts=1

IDEA: Мобильная якорная навигация «чипсами» вместо скрытого меню
KNOB: В `@media(max-width:720px)` (L90) заменить `display:none` у `.nav-links` на горизонтальную прокручиваемую полосу: `display:flex;overflow-x:auto;gap:14px;font-size:13px;white-space:nowrap;-webkit-overflow-scrolling:touch`, ссылки — компактные «чипсы» (padding:8px 14px;border:1px solid var(--border);border-radius:999px). Пункты те же, что в L438 (Демо, Цена, Вопросы и т.д.).
EFFECT: На телефоне (основной трафик локального бизнеса) пользователь в любой момент видит путь к цене/демо/FAQ вместо пустого хедера — меньше прокрутки «вслепую», больше переходов к CTA-секциям.
RISK: Полоса чипсов может спореть с логотипом по ширине на узких экранах (<360px) — нужно проверить переносы.
ROLLBACK: `git checkout -- index.html` (или правка только media-блока L90 обратно на `display:none`).
VERIFY: DevTools → Toggle device toolbar → iPhone SE/360px: чипсы видны
