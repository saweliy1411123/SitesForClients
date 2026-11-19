# localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct  2026-11-17 07:42:22
duration=9.4 error=- attempts=1

IDEA: Мобильная навигация-меню
KNOB: В `@media(max-width:720px)` (L90) вместо `display:none` у `.nav-links` добавить кнопку-бургер в хедере и сделать навигацию горизонтально прокручиваемой
EFFECT: Улучшение навигации на мобильных устройствах
RISK: Риск дублирования кода
ROLLBACK: git checkout -- index.html
VERIFY: Проверить навигацию на мобильных устройствах
PRIORITY: 2
SITE_REQUEST: nav-links
