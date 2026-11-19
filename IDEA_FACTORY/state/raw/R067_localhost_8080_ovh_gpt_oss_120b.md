# localhost:8080/ovh/gpt-oss-120b  2026-11-17 04:56:40
duration=64.7 error=- attempts=1

IDEA: Hero‑badge «2‑дня до запуска» с пульс‑анимацией  
KNOB: В блоке `.hero` добавить `<span class="hero-badge">2 дня до запуска</span>`; CSS `.hero-badge{position:absolute;top:1rem;right:1rem;background:#8b5cf6;color:#fff;padding:0.3em 0.6em;border-radius:0.5rem;animation:badge-pulse 2s infinite ease-in-out}` и `@keyframes badge-pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.08)}}`  
EFFECT: мгновенно подчёркивает ключевой конкурентный плюс, повышает визуальное внимание к офферу → рост CTR на CTA ≈ 5 %  
RISK: небольшое увеличение CSS‑объёма (≈ 0.5 KB) и потенциальный конфликт с уже существующими позициями `.hero` если они используют `position:relative`  
ROLLBACK: `git checkout -- index.html` (или удалить добавленные строки и стили)  
VERIFY: открыть страницу в Chrome, включить DevTools → Elements, убедиться, что badge отображается и анимируется; измерить количество кликов по CTA до/после в Google Analytics (или быстрый локальный A/B с двумя копиями)  
PRIORITY: 1 – быстрый визуальный апгрейд, минимум кода, высокий ROI  

---  

IDEA: Боль — SERP‑мокап с подсветкой вашего сайта в результатах Яндекса  
KNOB: После заголовка `h2` в секции боли вставить блок `<div class="serp-mock" aria-hidden="true"><div class="serp-line">Савелий — лендинги для бизнеса в Перми</div><div class="serp-url">saveliy.ru/…</div><div class="serp-desc">Создаём сайты за 2 дня, которые находятся в топе Яндекса.</div></div>`; CSS‑стили оформить в виде имитации поисковой строки (фон #fff, тени, шрифты Manrope, цвет #555)  
EFFECT: визуальное доказательство «вы уже в поиске», усиливает доверие и уменьшает скепсис → потенциальное снижение bounce‑rate на ≈ 3 %  
RISK: добавление дополнительного DOM‑элемента может слегка увеличить размер HTML (≈ 1 KB)  
ROLLBACK: `git checkout -- index.html` (удалить блок `.serp-mock` и связанные стили)  
VERIFY: открыть страницу, убедиться, что мокап корректно отображается на десктопе и мобильных ширинах; проверить, что он не мешает скринридерам (aria‑hidden)  
PRIORITY: 2 – повышает убедительность оффера, но требует визуального дизайна, поэтому отложить после badge  

---  

IDEA: Шаги — прогресс‑бар, заполняющийся по мере просмотра шагов  
KNOB: В секции `.steps` добавить `<div class="steps-progress"><div class="progress-fill"></div></div>`; в CSS `.steps-progress{height:4px;background:#e5e7eb;margin-bottom:1rem;position:relative}.progress-fill{width:0;height:100;background:#8b5cf6;transition:width .4s}`; добавить небольшой скрипт (≈ 30 строк) с `IntersectionObserver`, который при появлении каждого `.step-item` увеличивает `width` на 33%  
EFFECT: пользователь видит «прогресс», усиливает чувство завершённости, повышает время на странице → рост конверсии в форму ≈ 4 %  
RISK: небольшая зависимость от JS (не критично, работает без него, просто без прогресса)  
ROLLBACK: удалить добавленный `<div class="steps-progress">` и скрипт из `index.html` (или откатить commit)  
VERIFY: открыть страницу, прокручивать вниз, наблюдать плавное заполнение полосы; в консоли `document.querySelector('.progress-fill').style.width` должно увеличиваться; проверить, что полоса сбрасывается при перезагрузке  
PRIORITY: 1 – простая визуальная подсказка, легко измерима, высокий потенциал  

---  

IDEA: Демо‑карточки — CSS‑only carousel с автоплей и pause‑on‑hover  
KNOB: Обернуть текущие демо‑блоки в `<div class="demo-carousel">`; добавить CSS‑правила: `.demo-carousel{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;scroll-behavior:smooth}.demo-card{flex:0 0 80%;margin-right:1rem;scroll-snap-align:start;transition:transform .3s}.demo-carousel:hover{animation-play-state:paused}`; добавить небольшую keyframes‑анимацию `@keyframes carousel-scroll{0%{transform:translateX(0)}100%{transform:translateX(-calc(100% * N))}}` где N – кол‑во карточек, и применить её к контейнеру с `animation:carousel-scroll 20s linear infinite`.  
EFFECT: демонстрирует несколько концептов без прокрутки пользователем, повышает вовлечённость → увеличение среднего времени на странице ≈ 6 %  
RISK: если количество карточек изменится, анимация потребует пересчёта N; небольшое увеличение CSS‑объёма (~1 KB)  
ROLLBACK: удалить контейнер `.demo-carousel` и связанные стили/анимацию; вернуть оригинальную разметку  
VERIFY: открыть страницу, убедиться, что карточки скользят автоматически, останавливаются при наведении, работают на мобильных (touch‑scroll)  
PRIORITY: 2 – улучшает демонстрацию продукта, но требует точной настройки количества карточек  

---  

IDEA: Цена — «Гарантия возврата» badge с tooltip‑подсказкой  
KNOB: Внутри каждого `.price-card` после цены добавить `<span class="guarantee-badge" title="Если сайт не будет готов в 2 дня — возвращаем 100 % средств">Гарантия</span>`; CSS `.guarantee-badge{display:inline-block;background:#34d399;color:#fff;padding:0.2em 0.5em;border-radius:0.3rem;font-size:0.85em;margin-left:0.5rem;cursor:help;}`  
EFFECT: снижает страх риска у потенциальных клиентов, повышает доверие → рост заявок ≈ 3 %  
RISK: tooltip‑текст виден только при наведении; на мобильных может быть недоступен (можно добавить `aria-label`)  
ROLLBACK: удалить строку badge и CSS‑правило  
VERIFY: в браузере навести курсор на badge, увидеть подсказку; проверить, что badge отображается в мобильных viewports (при тапе)  
PRIORITY: 3 – небольшое улучшение, но требует проверки доступности, поэтому отложить после более приоритетных идей  

---  

IDEA: FAQ — поиск по вопросам в реальном времени  
KNOB: В секцию FAQ добавить `<input type="search" class="faq-search" placeholder="Найти вопрос…" aria-label="Поиск по FAQ">`; обернуть каждый вопрос‑ответ в `<div class="faq-item">`; добавить небольшой скрипт, который при вводе в `.faq-search` фильтрует `.faq-item` через `textContent.includes(searchTerm)` и скрывает не совпадающие (`style.display='none'`).  
EFFECT: ускоряет поиск нужной информации, повышает удовлетворённость → потенциальное снижение отказов ≈ 2 %  
RISK: требует небольшого JS (≈ 40 строк); если пользователь отключит JS, поиск не будет работать, но контент останется видимым  
ROLLBACK: удалить `<input>` и скрипт, вернуть оригинальные FAQ‑элементы  
VERIFY: в Chrome открыть страницу, ввести часть вопроса, убедиться, что список сокращается; отключить JS в DevTools и убедиться, что весь FAQ остаётся видимым  
PRIORITY: 2 – улучшает UX, но требует небольшого кода и тестов на доступность  

---  

IDEA: Финальный CTA — кнопка «Скопировать ссылку на Telegram» с toast‑уведомлением  
KNOB: В блоке `.final .btn-primary` добавить рядом кнопку `<button class="copy-cta" type="button" data-link="https://t.me/TrainersDontPlays">Копировать ссылку</button>`; CSS `.copy-cta{margin-left:0.5rem;background:transparent;color:var(--blue);border:none;cursor:pointer}`; JS `document.querySelectorAll('.copy-cta').forEach(btn=>{btn.addEventListener('click',()=>{navigator.clipboard.writeText(btn.dataset.link).then(()=>{showToast('Ссылка скопирована')});});});function showToast(msg){const el=document.createElement('div');el.className='toast';el.textContent=msg;document.body.appendChild(el);setTimeout(()=>el.remove(),2000);}`; CSS `.toast{position:fixed;bottom:1rem;right:1rem;background:#333;color:#fff;padding:0.5rem 1rem;border-radius:0.3rem;z-index:1000}`  
EFFECT: упрощает действие для пользователей, повышает вероятность перехода в мессенджер → рост конверсии ≈ 4 %  
RISK: требует доступа к Clipboard API (не работает в старых браузерах); возможные ограничения в iOS Safari без пользовательского взаимодействия (но клик считается)  
ROLLBACK: удалить кнопку и скрипт, оставить оригинальный CTA  
VERIFY: кликнуть кнопку, убедиться, что в буфер попала ссылка (Ctrl+V в любой текстовый редактор), увидеть toast; проверить в разных браузерах (Chrome, Safari)  
PRIORITY: 1 – небольшое изменение, высокая вероятность улучшения конверсии, легко откатывается.
