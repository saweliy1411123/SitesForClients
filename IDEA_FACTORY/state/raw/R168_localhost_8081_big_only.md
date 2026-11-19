# localhost:8081/big_only  2026-11-17 09:46:37
duration=60.0 error=- attempts=1

IDEA: Preconnect & dns‑prefetch для Google‑Fonts  
KNOB: В `<head>` добавить `<link rel="preconnect" href="https://fonts.googleapis.com">` и `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>`; также добавить `<link rel="dns-prefetch" href="https://fonts.googleapis.com">` и `<link rel="dns-prefetch" href="https://fonts.gstatic.com">` рядом с текущим `<link href="https://fonts.googleapis.com/...">`.  
EFFECT: Сократит время установления соединения с CDN‑сервером, ускорит загрузку шрифтов → улучшит LCP и FCP.  
RISK: Минимальный – небольшое увеличение количества `<link>`‑элементов; не влияет на SEO.  
ROLLBACK: `git checkout index.html` (или удалить добавленные строки).  
VERIFY: Открыть страницу в Chrome DevTools → Network, включить “Disable cache”, перезагрузить и сравнить время до‑first‑byte шрифта (вкладка Timing).  
PRIORITY: 1 – быстрый и безопасный прирост скорости без кода.

---  

IDEA: JSON‑LD схема LocalBusiness для локального SEO  
KNOB: В `<head>` вставить `<script type="application/ld+json">` с объектом `@type": "LocalBusiness"` (name, address, telephone, url, openingHours, sameAs).  
EFFECT: Увеличит шансы появления в локальном поиске Яндекса/Google, улучшит видимость в “картах”.  
RISK: Требует подтверждения точных данных (адрес, часы); нет риска для безопасности.  
ROLLBACK: Удалить вставленный `<script>`‑блок (git revert или ручное удаление).  
VERIFY: В консоли DevTools выполнить `JSON.parse(document.querySelector('script[type="application/ld+json"]').textContent)` и убедиться в корректности структуры; затем проверить в Google Rich Results Test.  
PRIORITY: 2 – повышает SEO‑ценность, но требует согласования данных с владельцем.

---  

IDEA: Аккордеон‑FAQ на основе `<details>/<summary>` для лучшей доступности  
KNOB: В секции `#faq` заменить каждый пункт `<h3>` + текст на `<details class="faq-item"><summary class="faq-question">[вопрос]</summary><p class="faq-answer">[ответ]</p></details>`; добавить небольшие стили для плавного раскрытия.  
EFFECT: Позволит пользователям быстро находить ответы, уменьшит визуальный шум, повышает WCAG‑совместимость (клавиатурная навигация, ARIA‑автоматика).  
RISK: Требует небольших правок HTML; может немного изменить визуальный дизайн (но стили легко скорректировать).  
ROLLBACK: Восстановить оригинальные блоки из коммита (`git checkout index.html`).  
VERIFY: В браузере открыть страницу, нажать Tab до вопросов, убедиться в открытии/закрытии без мыши; проверить в DevTools “Accessibility” → “ARIA‑expanded”.  
PRIORITY: 2 – улучшает UX и доступность без нагрузки на производительность.

---  

IDEA: Полоска‑индикатор прогресса чтения страницы (scroll progress bar)  
KNOB: В начале `<body>` добавить `<div class="scroll-progress" aria-hidden="true"></div>`; в CSS задать фиксированную высоту 2 px, `background: var(--blue); width: 0; transition: width 0.2s ease;` и `position:fixed; top:0; left:0; z-index:9999;`. В небольшом безопасном JS добавить `window.addEventListener('scroll',()=>{const docHeight=document.documentElement.scrollHeight-window.innerHeight;const scrolled=window.scrollY/docHeight*100;document.querySelector('.scroll-progress').style.width=scrolled+'%'});`.  
EFFECT: Визуальный сигнал прогресса удерживает внимание, повышает вовлечённость и воспринимаемую «длина» страницы → потенциальный рост времени на сайте и конверсий.  
RISK: Добавляет 1 KB JS и небольшую CSS
