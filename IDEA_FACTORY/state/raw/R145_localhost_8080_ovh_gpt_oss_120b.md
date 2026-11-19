# localhost:8080/ovh/gpt-oss-120b  2026-11-17 08:42:02
duration=23.0 error=- attempts=1

IDEA: Добавить атрибут `lang="ru"` в корневой `<html>`  
KNOB: В файл `index.html` изменить открывающий тег `<html>` → `<html lang="ru">`  
EFFECT: Улучшит SEO (поиск по языку) и доступность (скрин‑ридеры определят язык)  
RISK: Никакого, небольшое изменение HTML‑структуры  
ROLLBACK: `git checkout -- index.html` (или `git revert HEAD` если уже закоммичено)  
VERIFY: Открыть страницу в браузере, открыть DevTools → Elements, убедиться, что `<html lang="ru">` присутствует; проверить в Lighthouse → Accessibility, Language attribute = pass  
PRIORITY: 1 – быстрый и безопасный выигрыш для SEO и a11y  
SITE_REQUEST: html  

IDEA: Предзагрузка шрифтов Google Fonts через `preconnect`  
KNOB: В `<head>` добавить две ссылки: `<link rel="preconnect" href="https://fonts.googleapis.com">` и `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>`  
EFFECT: Сократит время установления соединения, ускорит отрисовку текста → лучше LCP  
RISK: Никаких конфликтов, лишь небольшое увеличение HEAD‑размера  
ROLLBACK: Удалить добавленные строки или выполнить `git checkout -- index.html`  
VERIFY: В DevTools → Network, увидеть, что соединения к `fonts.googleapis.com` и `fonts.gstatic.com` открыты сразу (Status: pending → 200 без задержки) и измерить LCP до/после (можно через Lighthouse)  
PRIORITY: 1 – заметное ускорение первого контента без риска  

IDEA: Улучшить семантику CTA‑ссылок: добавить `role="button"` и `aria-label`  
KNOB: Для всех `<a>`‑элементов, стилизованных как кнопки (класс `.btn-primary`), добавить атрибуты `role="button"` и, если текст не описывает действие явно, `aria-label="Получить бесплатное демо"` (пример в финальном CTA)  
EFFECT: Повысит доступность для скрин‑ридеров и улучшит семантику, что положительно отразится на SEO‑оценке интерактивных элементов  
RISK: Требует проверки, что атрибуты не конфликтуют с существующими стилями  
ROLLBACK: Удалить добавленные атрибуты или `git checkout -- index.html`  
VERIFY: Включить Chrome Accessibility Tree (DevTools → Elements → Accessibility) и убедиться, что элемент имеет роль button и правильный label; протестировать клавиатурную навигацию (Tab → Enter)  
PRIORITY: 1 – небольшое изменение, сразу улучшает доступность  

IDEA: Добавить JSON‑LD схему `Organization` с контактами и соцсетями  
KNOB: В `<head>` после уже существующего `LocalBusiness`‑скрипта вставить новый `<script type="application/ld+json">` с объектом `@type":"Organization"`; включить `name`, `url`, `logo`, `contactPoint` (телефон, email) и `sameAs` (ссылки на соцсети)  
EFFECT: Расширит микроданные, поможет поисковикам лучше понять бизнес, может появиться в Knowledge Graph → рост кликов  
RISK: Требует точных данных, но нет риска «обмана», только необходимость правдивой информации  
ROLLBACK: Удалить вставленный скрипт или `git checkout -- index.html`  
VERIFY: Скопировать содержимое скрипта в https://search.google.com/structured-data/testing-tool и убедиться в отсутствии ошибок; проверить в Lighthouse → SEO → Structured Data  
PRIORITY: 2 – добавит ценность, но требует актуальных данных  

IDEA: Создать `sitemap.xml` и связать его в `robots.txt`  
KNOB: В корне проекта добавить файл `sitemap.xml` со списком единственной страницы (`<url><loc>https://example.com/</loc><priority>1.0</priority></url>`); в `robots.txt` добавить строку `Sitemap: https://example.com/sitemap.xml` (если файл уже существует, дополнить)  
EFFECT: Упростит индексацию для поисковых роботов, потенциально ускорит появление в результатах поиска  
RISK: Нужно убедиться, что URL корректный; в случае ошибки robots могут блокировать страницу  
ROLLBACK: Удалить `sitemap.xml` и строку из `robots.txt` или восстановить предыдущие версии через git  
VERIFY: В браузере открыть `https://example.com/sitemap.xml` и убедиться в корректном XML; в Google Search Console проверить статус Sitemap (можно быстро через “URL Inspection”)  
PRIORITY: 2 – небольшие файлы, но важны для SEO  

IDEA: Предзагрузка основного CSS‑файла через `preload`  
KNOB: В `<head>` заменить обычный `<link rel="stylesheet" href="style.css">` на `<link rel="preload" href="style.css" as="style" onload="this.rel='stylesheet'">` и добавить `<noscript><link rel="stylesheet" href="style.css"></noscript>` для поддержки без JS  
EFFECT: Уменьшит время блокировки рендеринга, ускорит First Paint, особенно на медленных соединениях  
RISK: Если пользователь отключил JS, стили могут не загрузиться без `<noscript>` (поэтому добавлен fallback)  
ROLLBACK: Вернуть оригинальный `<link rel="stylesheet">` или `git checkout -- index.html`  
VERIFY: В DevTools → Network фильтровать по `style.css`, увидеть статус `preload` → `200`; измерить `First Contentful Paint` до/после (Lighthouse)  
PRIORITY: 2 – улучшает скорость, но требует проверки fallback  

IDEA: Добавить `hreflang` для указания языка и региона  
KNOB: В `<head>` добавить `<link rel="alternate" hreflang="ru" href="https://example.com/">` (и, при необходимости, `x-default`)  
EFFECT: Помогает поисковым системам правильно обслуживать русскоязычных пользователей, улучшая SEO в гео‑таргетинге  
RISK: Неправильный URL может привести к дублированию; требуется проверка корректности ссылки  
ROLLBACK: Удалить добавленные `<link rel="alternate">` строки или `git checkout -- index.html`  
VERIFY: Проверить в Google Search Console → International Targeting → Hreflang; убедиться, что ссылка корректна и не вызывает ошибок  
PRIORITY: 3 – полезно, но менее критично, чем предыдущие улучшения.
