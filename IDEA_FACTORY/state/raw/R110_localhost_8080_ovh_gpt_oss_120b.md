# localhost:8080/ovh/gpt-oss-120b  2026-11-17 07:03:35
duration=32.2 error=- attempts=1

IDEA: Добавить канонический URL‑тег  
KNOB: В `<head>` сразу после `<title>` вставить `<link rel="canonical" href="https://saveliy-perm.ru/">` (заменить на реальный домен)  
EFFECT: Укрепит сигнал поисковикам о единственном источнике контента, уменьшит риск дублей и улучшит SEO‑вес страницы  
RISK: Требует подтверждения, что указанный URL — действительно основной адрес сайта (иначе может вызвать каннибализацию)  
ROLLBACK: `git checkout -- index.html` (или удалить строку в файле)  
VERIFY: Открыть страницу, посмотреть в исходном коде наличие тега, в Lighthouse → SEO проверить “Canonical link element” — должен быть без ошибок  
PRIORITY: 1 — высокий ROI для SEO, простая однострочная правка  

IDEA: Обеспечить безопасные внешние ссылки  
KNOB: Для всех `<a>` с `href` на внешние ресурсы (Telegram‑ссылка в L462, L657, L705) добавить атрибуты `rel="noopener noreferrer"`  
EFFECT: Защищает от атак типа tab‑nabbing, ускоряет загрузку за счёт отказа от создания нового контекста → улучшение безопасности и небольшое ускорение → положительный сигнал SEO  
RISK: Никаких визуальных изменений, но если ссылка используется в рамках окна‑попапа, поведение может измениться (не актуально)  
ROLLBACK: `git checkout -- index.html` (удалить добавленные атрибуты)  
VERIFY: В DevTools выполнить `document.querySelectorAll('a[rel="noopener noreferrer"]').length` — должно соответствовать количеству внешних ссылок; проверить отсутствие консольных ошибок при клике  
PRIORITY: 2 — низкая стоимость, высокая безопасность  

IDEA: Визуальная хлебная крошка + JSON‑LD BreadcrumbList  
KNOB: После закрывающего `</header>` добавить блок  
```html
<nav aria-label="Хлебные крошки" class="breadcrumbs">
  <a href="/">Главная</a> / <span>Лендинг</span>
</nav>
```  
и в `<head>` перед `</head>` вставить  
```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"BreadcrumbList",
  "itemListElement":[
    {"@type":"ListItem","position":1,"name":"Главная","item":"https://saveliy-perm.ru/"},
    {"@type":"ListItem","position":2,"name":"Лендинг","item":"https://saveliy-perm.ru/#"}
  ]
}
</script>
```  
EFFECT: Улучшает навигацию пользователей, повышает шанс появления в поисковой выдаче в виде «хлебных крошек», положительно влияет на SEO‑оценку структуры сайта  
RISK: Требует корректного указания URL‑ов; неверный путь может запутать поисковик  
ROLLBACK: `git checkout -- index.html` (удалить вставленные блоки)  
VERIFY: В Lighthouse → SEO проверить “Breadcrumb structured data”; в браузере увидеть навигационную цепочку и кликнуть по ней  
PRIORITY: 1 — значительный SEO‑эффект, небольшие изменения  

IDEA: Добавить мета‑тег robots для контроля индексации  
KNOB: В `<head>` после остальных `<meta>` добавить `<meta name="robots" content="index, follow">`  
EFFECT: Явно указывает поисковикам индексировать страницу и следовать по ссылкам, устраняя возможные недоразумения с настройками по умолчанию, повышает уверенность в SEO‑стратегии  
RISK: Если в дальнейшем понадобится закрыть страницу от индексации, придётся менять тег (не критично)  
ROLLBACK: `git checkout -- index.html` (удалить строку)  
VERIFY: В DevTools открыть «View source», убедиться в наличии тега; в Lighthouse → SEO проверить отсутствие предупреждения о robots‑теге  
PRIORITY: 2 — низкая сложность, полезно для полного индексационного контроля  

IDEA: Предзагрузка DNS и шрифтов для ускорения LCP  
KNOB: В `<head>` добавить перед существующими `<link rel="preconnect">` строки:  
```html
<link rel="dns-prefetch" href="//fonts.googleapis.com">
<link rel="dns-prefetch" href="//fonts.gstatic.com">
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Manrope:wght@600;700&display=swap" crossorigin>
```  
EFFECT: Сократит время установления соединения с CDN‑шрифтами, ускорит отрисовку текста в hero‑секции → улучшит LCP и Core Web Vitals → положительно отразится на SEO и пользовательском опыте  
RISK: Если указать неверный URL, браузер может попытаться загрузить несуществующий ресурс (не критично)  
ROLLBACK: `git checkout -- index.html` (удалить добавленные строки)  
VERIFY: В Chrome → Network посмотреть, что запросы DNS‑prefetch и preload выполнены; в Lighthouse → Performance проверить улучшение LCP (скрытый в пределах 2 сек)  
PRIORITY: 2 — умеренный эффект на скорость, простая правка  

IDEA: Добавить роль навигации и ARIA‑метку к меню  
KNOB: Найти `<nav class="nav">` (или аналог) и изменить на `<nav class="nav" role="navigation" aria-label="Главное меню">`  
EFFECT: Явно сообщает скрин‑ридерам о навигационном блоке, улучшает доступность и соответствует WCAG 2.1 AA → потенциально повышает SEO‑оценку доступности  
RISK: Если уже есть `role="navigation"` в другом месте, может возникнуть дублирование (не критично)  
ROLLBACK: `git checkout -- index.html` (откатить изменение)  
VERIFY: В DevTools выполнить `document.querySelector('nav[role="navigation"]').getAttribute('aria-label')` — должно вернуть «Главное меню»; в axe‑core (или Lighthouse → Accessibility) отсутствие ошибок «nav missing landmark»  
PRIORITY: 2 — высокая ценность для a11y, минимальная стоимость  

IDEA: Установить атрибут `title` на все CTA‑ссылки для лучшего контекстного описания  
KNOB: Для каждой ссылки с классом `.btn-primary` (пример в L462, L657, L705) добавить `title="Получить бесплатное демо‑макет"` (или соответствующий короткий текст)  
EFFECT: Улучшает понимание цели ссылки пользователями скрин‑ридеров и при наведении, повышает доверие и потенциально CTR → положительно влияет на конверсию и SEO‑поведенческие сигналы  
RISK: Длинные title могут перегрузить экран‑чтец; использовать короткие, проверенные тексты  
ROLLBACK: `git checkout -- index.html` (удалить атрибуты)  
VERIFY: Навести курсор – появится всплывающая подсказка; в DevTools выполнить `document.querySelectorAll('a.btn-primary[title]').length` — должно совпадать с количеством CTA‑ссылок; в axe‑core проверка «link purpose» должна быть пройдена  
PRIORITY: 3 — мера улучшения UX, но менее критична чем SEO‑теги; реализуется быстро.
