# localhost:8080/ovh/gpt-oss-120b  2026-11-17 04:35:25
duration=52.3 error=- attempts=1

IDEA: Добавить атрибут `lang="ru"` в `<html>`  
KNOB: В открывающий тег `<html>` добавить `lang="ru"` (например: `<html lang="ru">`)  
EFFECT: Улучшит SEO (поисковые системы учитывают язык) и доступность (скрин‑ридеры сразу знают язык страницы)  
RISK: Минимальный — требуется небольшое изменение в начале файла, не ломает разметку  
ROLLBACK: `git checkout -- index.html` (или откатить конкретную строку)  
VERIFY: Открыть страницу в Chrome DevTools → Elements, убедиться, что атрибут `lang="ru"` присутствует в корневом элементе  
PRIORITY: 1 – быстрый фикс с высоким SEO‑и‑a11y‑выигрышем  

IDEA: Обеспечить безопасность внешних ссылок (`rel="noopener noreferrer"`)  
KNOB: Во всех `<a>` с `target="_blank"` добавить `rel="noopener noreferrer"` (например: `<a href="https://t.me/..." target="_blank" rel="noopener noreferrer">`)  
EFFECT: Защищает от атак типа reverse‑tabnabbing, повышает доверие к сайту  
RISK: Никакого визуального изменения, но требуется убедиться, что не конфликтует с существующим JavaScript‑обработчиком  
ROLLBACK: `git checkout -- index.html` (если правка в нескольких местах – восстановить файл из коммита)  
VERIFY: В консоли DevTools выполнить `document.querySelectorAll('a[target="_blank"]').forEach(a=>console.assert(a.rel.includes('noopener') && a.rel.includes('noreferrer')))` – все должны пройти проверку  
PRIORITY: 2 – безопасность важна, но изменение небольшое  

IDEA: Добавить семантические роли к шапке и подвалу  
KNOB: В элемент `<header class="hero">` добавить `role="banner"`; в `<footer>` добавить `role="contentinfo"`  
EFFECT: Улучшает навигацию скрин‑ридеров, упрощает аудит доступности, небольшое SEO‑подкрепление через landmarks  
RISK: Если уже есть ARIA‑role, может привести к дублированию – проверить отсутствие конфликтов  
ROLLBACK: Удалить добавленные атрибуты или откатить файл  
VERIFY: В DevTools → Accessibility panel убедиться, что элементы отмечены как “Banner” и “Content info”  
PRIORITY: 2 – небольшая правка, повышает a11y без риска  

IDEA: Обогатить навигационные ссылки ARIA‑метками  
KNOB: Во все ссылки навигации (`<nav>` → `<a>`) добавить `aria-label="Перейти к секции …"` с названием секции; текущей секции добавить `aria-current="page"`  
EFFECT: Пользователи скрин‑ридеров получают ясные подсказки, повышается восприятие структуры страницы  
RISK: Требует точного совпадения названий секций; возможен человеческий опечаточный риск  
ROLLBACK: Удалить добавленные атрибуты или откатить файл  
VERIFY: В консоли выполнить `document.querySelectorAll('nav a').forEach(a=>console.assert(a.hasAttribute('aria-label')))` и проверить `aria-current` у текущего пункта  
PRIORITY: 3 – полезно, но менее критично, чем предыдущие  

IDEA: Перенести скрипт в конец `<body>` и добавить `defer`  
KNOB: В `<script>` (единственный) изменить на `<script src="script.js" defer></script>` и разместить перед закрывающим `</body>` (если скрипт встроен, вынести в отдельный файл `script.js` и подключить с `defer`)  
EFFECT: Уменьшит блокировку рендеринга, ускорит First Contentful Paint, особенно на мобильных устройствах  
RISK: Если скрипт зависит от элементов, объявленных после него, `defer` гарантирует их загрузку после парсинга – проверка обязательна  
ROLLBACK: Восстановить оригинальный `<script>` из репозитория (`git checkout -- index.html`)  
VERIFY: В Chrome DevTools → Network убедиться, что скрипт загружается как “deferred”; измерить FCP до/после через Lighthouse  
PRIORITY: 2 – ускорение загрузки стоит усилий, но риск низок  

IDEA: Добавить Open Graph изображение для соцсетей  
KNOB: В `<head>` вставить `<meta property="og:image" content="https://saveliy.ru/assets/og-image.jpg">` (изображение‑превью, 1200×630 px)  
EFFECT: При шаринге в соцсетях будет отображаться красивый превью‑картинка, повышая кликабельность ссылок  
RISK: Нужно разместить файл изображения на сервер; отсутствие файла приведёт к 404‑ошибке в соцсетях  
ROLLBACK: Удалить мета‑тег или откатить файл  
VERIFY: С помощью Facebook Sharing Debugger проверить, что изображение подхватывается корректно  
PRIORITY: 3 – улучшает соц‑трафик, но не критично для текущих целей  

IDEA: Добавить микрокопию под основной CTA‑кнопкой о «без спама»  
KNOB: После первой `.btn-primary` в hero (строка 462) добавить `<p class="cta-note">Мы не будем присылать вам спам, только демо‑прототип.</p>` и стилизовать `.cta-note{font-size:0.9rem;color:var(--muted);margin-top:4px;}`  
EFFECT: Снижает психологический барьер кликнуть, повышает доверие, небольшое влияние на конверсию  
RISK: Добавит небольшой объём текста, может слегка увеличить высоту hero‑секции – проверить на мобильных экранах  
ROLLBACK: Удалить добавленный `<p>` и стили  
VERIFY: В браузере проверить, что текст виден и не ломает макет; провести быстрый A/B‑тест с `#v2`‑хешем (см. I-00296) для сравнения CTR  
PRIORITY: 2 – низкая стоимость, потенциальный рост конверсии  

IDEA: Реализовать CSS‑scroll‑snap карусель отзывов в секции «Отзывы и работы»  
KNOB: Обернуть существующие карточки отзывов в `<div class="testimonial-carousel" tabindex="0">`; добавить CSS:  
SAFE CSS:  
```css
.testimonial-carousel{
  display:flex;overflow-x:auto;scroll-snap-type:x mandatory;
  -webkit-overflow-scrolling:touch;
}
.testimonial-carousel > *{
  flex:0 0 80%;margin-right:1rem;scroll-snap-align:start;
}
.testimonial-carousel::-webkit-scrollbar{display:none;}
```  
EFFECT: Позволит пользователям быстро просматривать отзывы без JavaScript, повышая вовлечённость и доверие  
RISK: Требует корректной разметки карточек; если их слишком мало, карусель будет выглядеть пустой  
ROLLBACK: Удалить обёртку и стили (`git checkout -- index.html`)  
VERIFY: Прокрутить секцию в браузере, убедиться, что карточки «прилипают» к краю; проверить на мобильных устройствах, что свайп работает  
PRIORITY: 3 – улучшает UI, но не критично для конверсии  

IDEA: Lazy‑load фоновые изображения hero‑секции через IntersectionObserver  
KNOB: Заменить CSS‑фон hero (`background-image:url(...)`) на атрибут `data-bg="url(...)"`; добавить небольшой inline‑скрипт (deferred) который, при появлении hero в viewport, задаёт `style.backgroundImage = element.dataset.bg`  
EFFECT: Сократит объём данных, загружаемых при первом рендере, ускорит LCP, особенно на медленных соединениях  
RISK: Требует небольшого JS; если скрипт не выполнится, фон останется пустым – необходимо fallback‑стиль (цвет)  
ROLLBACK: Удалить `data-bg` и скрипт, вернуть прежний CSS‑фон (`git checkout -- index.html`)  
VERIFY: Открыть страницу в сети «Slow 3G» (DevTools → Network → Throttling) и убедиться, что фон загружается после скроллинга к hero; измерить LCP до/после через Lighthouse  
PRIORITY: 2 – ускоряет LCP, важный метрик для SEO и UX  

IDEA: Добавить `aria-hidden="true"` к декоративным SVG‑элементам (particles, blobs)  
KNOB: Во все `<svg>`/`<div id="particles">` и элементы с классом `blob`, `veil` добавить `aria-hidden="true"`  
EFFECT: Уменьшит «шум» для скрин‑ридеров, улучшит доступность без визуального изменения  
RISK: Никакого визуального влияния, только риск пропустить какой‑то интерактивный SVG (проверить)  
ROLLBACK: Удалить атрибуты (`git checkout -- index.html`)  
VERIFY: В DevTools → Accessibility проверить, что элементы помечены как «Ignored»; использовать экранный ридер (NVDA/VoiceOver) и убедиться, что они не озвучиваются  
PRIORITY: 3 – небольшое улучшение a11y, низкая сложность  

IDEA: Добавить `type="module"` и `defer` к единственному скрипту для лучшей загрузки  
KNOB: Если скрипт встроен, вынести в отдельный файл `main.js`; в `<script src="main.js" type="module" defer></script>` разместить перед `</body>`  
EFFECT: Позволит браузеру загрузить скрипт асинхронно, использовать модульную область, уменьшит риск конфликтов глобальных переменных  
RISK: Возможные ошибки, если скрипт использует `document.write` или ожидает синхронных переменных – требуется тестировать  
ROLLBACK: Восстановить оригинальный `<script>` (git checkout)  
VERIFY: Открыть страницу, открыть консоль – не должно быть ошибок `Uncaught ReferenceError`; измерить время загрузки скрипта в Network (должен быть “deferred”)  
PRIORITY: 2 – улучшает загрузку и поддерживаемость, умеренный риск  

IDEA: Добавить `hreflang="ru"` в `<head>` для указания языка целевой аудитории  
KNOB: В `<head>` вставить `<link rel="alternate" hreflang="ru" href="https://saveliy.ru/">`  
EFFECT: Помогает поисковикам правильно индексировать страницу для русскоязычных пользователей, потенциально повышает ранжирование в локальном поиске  
RISK: Нужен корректный URL; если сайт будет иметь другие локали, потребуется расширить список – сейчас безопасно  
ROLLBACK: Удалить тег `<link rel="alternate"...>`  
VERIFY: Проверить в инструментах Яндекса/Google Search Console
