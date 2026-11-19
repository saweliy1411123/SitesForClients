# lareper/deepseek-v4-pro-0813  2026-11-17 07:24:37
duration=2.4 error=- attempts=2

IDEA: Мобильная навигация — горизонтальная прокрутка чипсами вместо скрытия
KNOB: В `@media(max-width:720px)` (L90) заменить `display:none` у `.nav-links` на горизонтальную прокручиваемую полосу: `.nav-links{display:flex;overflow-x:auto;gap:12px;padding:10px 16px;scrollbar-width:none}` + `.nav-links::-webkit-scrollbar{display:none}`; добавить `white-space:nowrap` для ссылок.
EFFECT: Пользователи на мобильных получают быструю навигацию по секциям без скрытия/поиска меню — снижение отказов и рост глубины просмотра.
RISK: Полоса может конфликтовать с существующим sticky-хедером по высоте (нужно проверить перекрытие контента).
ROLLBACK: `git checkout index.html` или вернуть `display:none` в медиа-запросе.
VERIFY: Открыть в DevTools (iPhone SE 375px), проверить видимость и прокрутку полосы, кликабельность ссылок, отсутствие перекрытия hero-контента.
PRIORITY: 1 — мобильный трафик доминирует, навигация сейчас полностью скрыта — критично для UX и SEO.
SITE_REQUEST: nav-links
