# lareper/glm-5.3  2026-11-17 06:56:00
duration=2.3 error=- attempts=1

IDEA: Метод «консольный мульти-вариант через query-параметр» — тест 3 вариантов текста CTA в одной вкладке
KNOB: METHOD: (1) Открыть index.html локально, F12 → Console. (2) Выполнить скрипт: `const v=new URLSearchParams(location.search).get('v')||'A'; const map={'A':'Сделаю демо под ваш сайт — бесплатно','B':'Бесплатное демо за 2 дня — без обязательств','C':'Посмотрите демо вашего сайта — бесплатно'}; document.querySelectorAll('.btn-primary').forEach(b=>{b.dataset.orig=b.textContent; if(map[v])b.textContent=map[v]}); console.log('Вариант',v)`. (3) Открыть три вкладки: `index.html?v=A`, `?v=B`, `?v=C`. (4) Прогнать пятисекундный тест (I-00616) на каждом, записать, какой CTA понятнее без контекста. (5) Победителя вносить в файл.
EFFECT: Выбор формулировки CTA по наблюдаемой реакции людей, а не по вкусу; занимает 5–10 минут, ноль правок файлов.
RISK: Субъективность ручного теста — нужны 3+ респондента, иначе результат шумный.
ROLLBACK: Скрипт живёт только в консоли; при случайном сохранении — `git checkout -- index.html`.
VERIFY: Открыть `index.html?v=B` — текст CTA изменился только в этой вкладке; перезагрузка без параметра возвращает оригинал.
PRIORITY: 1 — дешёвый способ выбрать главную фразу оффера до любых правок.

IDEA: Метод «замер видимости финального CTA» — сколько скролла нужно до оффера
KNOB: METHOD: (1) Открыть index.html, F12 → Console. (2) Выполнить: `const f=document.querySelector('.final'); new IntersectionObserver(e=>console.log('final CTA виден при скролле', Math.round(window.scrollY)+'px', e[0].isIntersecting)).observe(f)`. (3) Медленно проскроллить страницу, записать px, при котором финальный CTA и `.sticky-cta` появляются. (4) Сравнить с высотой страницы (`document.body.scrollHeight`). Если CTA виден позже 70% высоты — гипотеза «пользователи не доскролливают до оффера» подтверждена, усиливает I-00644/I-00652.
EFFECT: Количественное обоснование (или снятие) гипотезы о раннем sticky-CTA; 3 минуты.
RISK: Ручной скролл не воспроизводит реальное поведение пользователей — это верхняя оценка, а не статистика.
ROLLBACK: Только чтение DOM; откат не требуется.
VERIFY: Повторить в режиме инкогнито с эмуляцией мобильного экрана (DevTools → Toggle device toolbar) — цифры должны быть сопоставимы.
PRIORITY: 2 — полезно, если sticky-CTA ещё не внедрён; после внедрения ценность падает.

IDEA: Метод «перехват якорной навигации» — проверка, куда реально ведут CTA-пути
KNOB: METHOD: (1) F12 → Console на index.html. (2) Выполнить: `document.querySelectorAll('a[href^="#"]').forEach(a=>a.addEventListener('click',e=>{e.preventDefault();console.log('Переход:',a.textContent.trim(),'→',a.getAttribute('href'),'| секция существует:',!!document.querySelector(a.getAttribute('href')))}))`. (3) Прокликать все ссылки меню, hero и финального блока. (4) Любой `false` в логе — битый якорь (пустой путь к заявке). (5) Заодно проверить, что все CTA ведут либо на `#contact`/Telegram, либо
