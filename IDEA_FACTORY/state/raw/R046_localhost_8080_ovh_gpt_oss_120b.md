# localhost:8080/ovh/gpt-oss-120b  2026-11-17 03:52:46
duration=62.0 error=- attempts=1

IDEA: Добавить «skip‑to‑content» ссылку вверху страницы  
KNOB: В начало `<body>` вставить `<a href="#main" class="skip-link">Перейти к содержимому</a>`; добавить CSS `.skip-link{position:absolute;top:-40px;left:0;background:#fff;color:#000;padding:8px;z-index:100;transition:top .3s;} .skip-link:focus{top:0;}` и установить `id="main"` на `<main>` (если его нет)  
EFFECT: Улучшает доступность для клавиатурных и скрин‑ридер пользователей, повышает SEO‑оценку Accessibility  
RISK: Минимальный визуальный сдвиг, если `<main>` уже имеет id – конфликт (можно выбрать другое имя)  
ROLLBACK: Удалить добавленные строки и CSS‑правило (git checkout -- index.html)  
VERIFY: Открыть страницу, нажать Tab – ссылка должна стать видимой и при клике прокрутить к основному контенту  
PRIORITY: 1 – высокая ценность для доступности без влияния на дизайн  

IDEA: Показать визуальный индикатор «прокрутите вниз» в hero‑секции  
KNOB: Внутри `.hero .wrap` добавить `<div class="scroll-indicator" aria-hidden="true"></div>`; CSS: `.scroll-indicator{position:absolute;bottom:20px;left:50%;transform:translateX(-50%);width:24px;height:40px;border:2px solid #fff;border-radius:12px;animation:scroll 2s infinite;}` `@keyframes scroll{0%{opacity:0.8;transform:translate(-50%,0);} 50%{opacity:0.4;transform:translate(-50%,10px);} 100%{opacity:0.8;transform:translate(-50%,0);}}`  
EFFECT: Подсказывает пользователям, что ниже есть контент, повышая вовлечённость и время на странице  
RISK: Возможна небольшая нагрузка на рендер, но незначительная  
ROLLBACK: Удалить HTML‑блок и CSS‑правила (git checkout -- index.html)  
VERIFY: На мобильных и десктоп‑экранах индикатор виден внизу hero и анимируется  
PRIORITY: 2 – умеренный UX‑улучшение, легко реализуемо  

IDEA: Вывести модальное окно при выходе (exit‑intent) с предложением бесплатного аудита  
KNOB: В конец `<body>` добавить скрипт, который отслеживает `mouseleave` у `document` и вставляет `<div class="exit-modal" role="dialog" aria-modal="true"><div class="exit-content"><p>Не уходите! Получите бесплатный аудит сайта.</p><a href="#contact" class="btn-primary">Записаться</a><button class="exit-close" aria-label="Закрыть">✕</button></div></div>`; CSS: `.exit-modal{position:fixed;inset:0;background:rgba(0,0,0,.6);display:none;align-items:center;justify-content:center;} .exit-modal.show{display:flex;} .exit-content{background:#fff;padding:24px;border-radius:8px;text-align:center;}` и JS‑обработчик `document.addEventListener('mouseleave',e=>{if(e.clientY<0){document.querySelector('.exit-modal').classList.add('show');}}); document.querySelector('.exit-close').onclick=()=>{document.querySelector('.exit-modal').classList.remove('show');};`  
EFFECT: Увеличивает шанс конверсии за счёт повторного привлечения уходящего пользователя  
RISK: Может раздражать пользователей, потенциальный рост показателя bounce; требует согласия владельца на использование модального окна  
ROLLBACK: Удалить вставленный HTML/JS/CSS (git checkout -- index.html)  
VERIFY: При покидании окна браузера (курсор к верхней границе) появляется модальное окно, закрывается кнопкой ✕  
PRIORITY: 2 – потенциальный прирост конверсий, но требует осторожного тестирования  

IDEA: Превратить блоки демо‑концептов в лёгкий CSS‑карусель с snap‑scroll  
KNOB: Обернуть все демо‑карточки в контейнер `<div class="demo-carousel" tabindex="0">`; добавить CSS: `.demo-carousel{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:24px;scroll-behavior:smooth;} .demo-carousel > *{flex:0 0 80%;scroll-snap-align:center;}` и небольшие стили для скрытия скролл‑баров `::-webkit-scrollbar{display:none;}`  
EFFECT: Позволяет пользователям просматривать несколько демо‑примеров без вертикальной прокрутки, улучшая восприятие и удержание внимания  
RISK: На старых браузерах (IE) может не работать, но большинство современных поддерживают  
ROLLBACK: Удалить обёртку и CSS‑правила (git checkout -- index.html)  
VERIFY: На десктопе и мобильных устройствах можно горизонтально листать демо‑карточки, они «прилипают» к центру  
PRIORITY: 1 – повышает интерактивность без JS, быстрый выигрыш в UX  

IDEA: Добавить `<link rel="canonical" href="https://example.com/">` в `<head>`  
KNOB: Вставить сразу после существующих `<meta>` строк `<link rel="canonical" href="https://saveliy-perm.ru/">` (заменить на реальный домен)  
EFFECT: Предотвращает дублирование контента в поисковых системах, улучшает локальное SEO  
RISK: Неправильный URL может навредить индексации; требует подтверждения у владельца правильного канонического адреса  
ROLLBACK: Удалить строку (git checkout -- index.html)  
VERIFY: Проверить в исходном коде наличие тега, открыть страницу в браузере → View Source → убедиться в корректном href  
PRIORITY: 2 – небольшое изменение, но важное для SEO  

IDEA: Добавить глобальный стиль `:focus-visible` для всех интерактивных элементов  
KNOB: В конец CSS добавить правило `a:focus-visible, button:focus-visible, .btn-primary:focus-visible{outline:2px solid var(--blue);outline-offset:2px;}` и убедиться, что все ссылки и кнопки используют `tabindex` по умолчанию  
EFFECT: Улучшает навигацию клавиатурой, повышая доступность и показатель Lighthouse Accessibility  
RISK: Возможен конфликт с уже установленными outline‑стилями; но правило специфично к `:focus-visible`  
ROLLBACK: Удалить добавленное правило (git checkout -- index.html)  
VERIFY: Нажать Tab, увидеть яркую рамку вокруг фокусируемых элементов, убедиться, что она исчезает при клике мышью  
PRIORITY: 1 – высокое влияние на доступность без визуального ущерба  

IDEA: В секции «Боль» добавить небольшую иллюстрацию «поисковой выдачи без вашего сайта» с доступным alt‑текстом  
KNOB: Перед первым `<h3>` в блоке боли вставить `<svg class="search-mock" aria-hidden="true" width="200" height="100" viewBox="0 0 200 100"><rect width="200" height="100" fill="#f0f0f0"/><text x="10" y="55" fill="#999" font-family="Manrope" font-size="14">Ваш бизнес не найден</text></svg>`; добавить CSS `.search-mock{margin-bottom:16px;}` и `aria-label="Пример отсутствия сайта в поисковой выдаче"` на родительский `<section>`  
EFFECT: Визуально подкрепляет проблему, повышая эмоциональное восприятие и конверсию  
RISK: Увеличивает размер HTML/CSS, но минимально (SVG инлайн)  
ROLLBACK: Удалить SVG‑блок и связанные стили (git checkout -- index.html)  
VERIFY: Открыть страницу, увидеть графическое изображение в секции боли, проверить, что скрин‑ридеры игнорируют его (aria‑hidden) и при необходимости читают `aria-label` родительского блока  
PRIORITY: 2 – визуальное усиление проблемы, умеренный трудозатрат  

IDEA: Добавить «Back to top» кнопку, появляющуюся после прокрутки 600 px  
KNOB: В конец `<body>` вставить `<button class="back-to-top" aria-label="Наверх">↑</button>`; CSS: `.back-to-top{position:fixed;right:20px;bottom:20px;background:var(--violet);color:#fff;border:none;border-radius:50%;width:48px;height:48px;display:none;align-items:center;justify-content:center;cursor:pointer;}` `window.addEventListener('scroll',()=>{document.querySelector('.back-to-top').style.display = window.scrollY>600?'flex':'none';});` `document.querySelector('.back-to-top').addEventListener('click',()=>{window.scrollTo({top:0,behavior:'smooth'});});`  
EFFECT: Упрощает навигацию, повышает пользовательский опыт, потенциально увеличивает время на сайте  
RISK: Требует небольшого JS, но без сторонних зависимостей; может конфликтовать с другими фиксированными элементами  
ROLLBACK: Удалить HTML‑элемент и JS‑блок, а также CSS‑правила (git checkout -- index.html)  
VERIFY: Прокрутить страницу вниз – кнопка появляется, клик возвращает в начало без резкого скачка  
PRIORITY: 3 – полезно, но менее критично для основной конверсии
