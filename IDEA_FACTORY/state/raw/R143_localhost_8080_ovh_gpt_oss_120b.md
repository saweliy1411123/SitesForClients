# localhost:8080/ovh/gpt-oss-120b  2026-11-17 08:36:26
duration=21.3 error=- attempts=1

IDEA: I-00790 Critique — Offer‑summary badge слишком мелкий и несемантичный  
KNOB: NONE (не вносить изменений)  
EFFECT: Выявляет, что микроскопический badge в hero не имеет достаточного контрастного цвета, не поддерживает `aria-label`, и может быть проигнорирован пользователями и поисковыми ботами → потенциально снижает восприятие оффера.  
RISK: Нет (только аналитика)  
ROLLBACK: НЕ ПРИМЕНЯЕТСЯ  
VERIFY: Открыть страницу в браузере, включить DevTools → проверить размер, контраст и наличие `aria-label` у нового элемента.  
PRIORITY: 2 — важно отметить, но правка может быть отложена до более критичных улучшений.  

IDEA: I-00806 Critique — Мобильная навигация‑бургер конфликтует с текущим `display:none` и ломает уже существующую простую навигацию  
KNOB: NONE (не вносить изменений)  
EFFECT: Указывает, что добавление бургер‑меню без полной реализации (скрипты, ARIA) приведёт к нерабочей навигации на мобильных, ухудшит UX и может вызвать ошибки валидации.  
RISK: Нет (только аналитика)  
ROLLBACK: НЕ ПРИМЕНЯЕТСЯ  
VERIFY: Включить мобильный режим в DevTools, проверить отсутствие меню‑кнопки и отсутствие скрытого контента.  
PRIORITY: 2 — нужно решить до внедрения любого мобильного меню.  

---  

IDEA: Add rel=canonical tag — уникальная ссылка для поисковых систем  
KNOB: В <head> вставить `<link rel="canonical" href="https://saveliy-perm.ru/">` (заменить на реальный домен) сразу перед закрывающим `</head>`  
EFFECT: Убирает риск дублирования контента, усиливает сигнал основной версии страницы для Яндекса и Google → улучшение SEO‑видимости.  
RISK: Неправильно указан URL может привести к перенаправлению индексации на чужой ресурс.  
ROLLBACK: Удалить добавленную строку (`git checkout index.html`)  
VERIFY: Открыть страницу, посмотреть исходный код → наличие `<link rel="canonical"...>`; проверить в Search Console, что canonical распознан.  
PRIORITY: 1 — высокий, быстрый выигрыш без риска.  

IDEA: Preload critical CSS и Google Font — ускорить рендер первой краски  
KNOB: В <head> добавить сразу после существующего `<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">` строку:  
```html
<link rel="preload" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap" as="style" onload="this.rel='stylesheet'">
<noscript><link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet"></noscript>
```  
и перед закрывающим `</head>` вставить:  
```html
<link rel="preload" href="styles/critical.css" as="style" onload="this.rel='stylesheet'">
<noscript><link href="styles/critical.css" rel="stylesheet"></noscript>
```  
(где `critical.css` содержит стили hero, nav и типографию).  
EFFECT: Убирает render‑blocking запросы, ускоряет LCP и First Contentful Paint → лучше показатели Core Web Vitals и более высокий CTR.  
RISK: Если файл `critical.css` недоступен, стили могут не примениться; требуется обеспечить fallback через `<noscript>`.  
ROLLBACK: Удалить добавленные `<link rel="preload">` и `<noscript>`‑блоки (`git checkout index.html`).  
VERIFY: В DevTools → Network → проверка, что запросы к шрифту и critical.css имеют статус 200 и `priority: high`; измерить LCP до/после через Lighthouse.  
PRIORITY: 1 — высокий, быстрый техничный выигрыш без изменения контента.
