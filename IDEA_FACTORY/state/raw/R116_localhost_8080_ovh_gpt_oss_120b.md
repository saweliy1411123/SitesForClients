# localhost:8080/ovh/gpt-oss-120b  2026-11-17 07:20:26
duration=34.4 error=- attempts=1

IDEA: Hero — тонкая фонова́я видеопетля (мягкий loop)  
KNOB: добавить в `.hero` элемент `<video class="hero-bg" autoplay muted loop playsinline poster="data:image/svg+xml,…">` с небольшим MP4 ≈ 30 KB; разместить под существующим `.hero-veil` и задать `position:absolute; inset:0; object-fit:cover; z-index:-1;`  
EFFECT: повышает визуальное вовлечение, удерживает внимание — рост CTR ≈ 5 % без заметного ухудшения LCP (видео preload = metadata)  
RISK: небольшое увеличение веса ≈ 30 KB, может замедлить LCP на медленных сетях  
ROLLBACK: `git checkout -- index.html` (удалить добавленные строки)  
VERIFY: открыть страницу в Chrome DevTools → Network, убедиться, что video‑запрос ≤ 30 KB, измерить LCP до/после (Performance → Metrics)  
PRIORITY: 1 — критичный визуальный апгрейд первого экрана  

IDEA: Hero — живой счётчик найденных клиентов (ARIA‑live)  
KNOB: после заголовка в `.hero` вставить `<div class="lead-counter" aria-live="polite">0 клиентов уже нашли нас</div>`; добавить скрипт, который при появлении в viewport (IntersectionObserver) анимирует цифры до 123 (пример) за 2 сек.  
EFFECT: создаёт социальное доказательство, повышает доверие — ожидаемый рост конверсий ≈ 3 %  
RISK: небольшое JS‑нагрузка ≈ 1 KB, возможен конфликт с уже существующим скриптом IntersectionObserver  
ROLLBACK: удалить блок и скрипт, `git checkout -- index.html`  
VERIFY: в консоли выполнить `document.querySelector('.lead-counter').textContent` после скролла, проверить, что цифра изменилась; измерить изменение CTR (быстрый A/B‑тест)  
PRIORITY: 1 — социальное доказательство на первом экране  

IDEA: Шаги — четырёхколоночный список «Что вы получите» под каждым заголовком  
KNOB: в секции «Три шага» (поиск `#steps` или ближайший `.step`) добавить после каждого `<h3>` список `<ul class="outcome-list"><li>…</li></ul>` с конкретными результатами (например, «Готовый прототип», «Подключённый домен»). Стилизовать через `.outcome-list{margin-top:8px;font-size:0.9rem;color:var(--muted)}`  
EFFECT: повышает прозрачность процесса, уменьшает фрустрацию, потенциальный рост конверсий ≈ 2 %  
RISK: увеличение объёма текста ≈ 200 B, может потребовать согласования с копирайтером  
ROLLBACK: `git checkout -- index.html` (удалить добавленные `<ul>`)  
VERIFY: открыть страницу, убедиться, что списки отображаются под каждым шагом, проверить читаемость (Chrome → Accessibility → Contrast)  
PRIORITY: 2 — улучшение ясности без технической нагрузки  

IDEA: FAQ — клиент‑сайд фильтр вопросов (поиск)  
KNOB: перед списком FAQ добавить `<input type="search" class="faq-search" placeholder="Найти вопрос…" aria-label="Поиск по FAQ">`; добавить небольшой скрипт, который на `input` скрывает/показывает `.faq-item` по совпадению `textContent.toLowerCase().includes(value)`; стилизовать `.faq-search{width:100%;padding:8px;margin-bottom:12px;border:1px solid var(--muted);border-radius:4px}`  
EFFECT: ускоряет поиск нужного ответа, повышает удовлетворённость — снижение отказов ≈ 4 %  
RISK: небольшое JS ≈ 1 KB, может конфликтовать с уже существующим скриптом‑аккордеоном  
ROLLBACK: удалить `<input>` и скрипт, `git checkout -- index.html`  
VERIFY: в консоли ввести `document.querySelectorAll('.faq-item').length` до/после ввода текста, убедиться, что количество скрытых элементов меняется; проверить, что поиск работает на мобильных (медиа‑запросы)  
PRIORITY: 2 — значительное улучшение UX, лёгкая реализация  

IDEA: Финальный CTA — кнопка «Скопировать ссылку на Telegram»  
KNOB: под основной CTA в `.final` добавить `<button class="copy-telegram btn-primary" type="button" aria-label="Скопировать ссылку на Telegram">Копировать ссылку <span class="arr">→</span></button>`; скрипт `navigator.clipboard.writeText('https://t.me/TrainersDontPlays')` с toast‑сообщением «Ссылка скопирована». Стилизовать как `.copy-telegram{margin-top:12px;}`  
EFFECT: упрощает пользовательский путь, особенно на десктопе, потенциальный рост конверсий ≈ 1‑2 %  
RISK: требует поддержки Clipboard API (не работает в старых браузерах) → fallback `alert`  
ROLLBACK: удалить кнопку и скрипт, `git checkout -- index.html`  
VERIFY: кликнуть кнопку, открыть консоль → `navigator.clipboard.readText()`; убедиться, что в буфере нужный URL; измерить изменение CTR (быстрый пользовательский опрос)  
PRIORITY: 3 — мелкий, но полезный апдейт  

IDEA: SEO — добавить JSON‑LD `LocalBusiness` со всеми данными компании (название, адрес в Перми, телефон, часы, URL)  
KNOB: в `<head>` перед закрывающим `</head>` вставить `<script type="application/ld+json">{"@context":"https://schema.org","@type":"LocalBusiness","name":"Савелий — лендинги для бизнеса в Перми","address":{"@type":"PostalAddress","addressLocality":"Пермь","addressRegion":"Пермский край"},"telephone":"+7 ...","url":"https://example.com","openingHours":"Mo-Fr 09:00-18:00"}</script>`  
EFFECT: усиливает локальное SEO, повышает шанс появления в Google & Yandex Local Pack, потенциальный рост органического трафика ≈ 5 %  
RISK: требуется актуальная контактная информация; неверные данные могут привести к штрафам поисковиков  
ROLLBACK: удалить скрипт, `git checkout -- index.html`  
VERIFY: в Search Console → Rich Results → проверить валидность схемы (тест‑разметки)  
PRIORITY: 1 — важно для локального поиска, почти без нагрузки  

IDEA: Доступность — визуальный индикатор внешних ссылок (иконка + aria‑label)  
KNOB: для всех `<a>` с `target="_blank"` добавить после текста `<span class="external-icon" aria-hidden="true">↗</span>` и атрибут `aria-label="Открыть в новой вкладке"`; стилизовать `.external-icon{margin-left:4px;font-size:0.8em;}`  
EFFECT: улучшает понимание пользователями, повышает соответствие WCAG 2.1 Guideline 1.4.1, потенциальный рост доверия ≈ 1 %  
RISK: небольшое визуальное изменение, может конфликтовать с текущим CSS‑классом `arr`  
ROLLBACK: удалить добавленные `<span>` и атрибуты, `git checkout -- index.html`  
VERIFY: в DevTools найти любой внешний `<a>` и убедиться в наличии иконки и `aria-label`; проверить, что скринридер объявляет «Открыть в новой вкладке»  
PRIORITY: 2 — значимый шаг к a11y без нагрузки.
