# lareper/deepseek-v4-pro-0813  2026-11-17 04:05:32
duration=88.7 error=- attempts=1

IDEA: Оффер-уточнение: «Telegram» → «В Telegram за 2 минуты» + микро-срок ответа
KNOB: В hero-CTA (L462 `<a class="btn-primary magnetic" href="#contact">`) заменить текст кнопки на «Написать в Telegram — отвечу за 2 минуты»; под кнопкой в `.hero-note` (L465) добавить строку «Сейчас онлайн — отвечаю быстро» (если это правда).
EFFECT: Снижает страх «долго ждать ответа», повышает кликабельность CTA и конверсию в заявку.
RISK: Если ответ будет дольше 2 минут — потеря доверия; требует честности владельца.
ROLLBACK: git checkout index.html (или вернуть прежний текст кнопки).
VERIFY: Открыть файл, Ctrl+F «Написать в Telegram» — проверить новый текст; мысленно оценить, не выглядит ли обещание ложным.
PRIORITY: 1 — прямо влияет на конверсию первого экрана.
SITE_REQUEST: hero

IDEA: Доверие: «Сейчас работаю над 3 проектами» — строка-статус в hero
KNOB: В `.hero-note` (L465) после фразы про демо добавить `<span class="hero-status">· сейчас работаю над 3 проектами для пермских бизнесов</span>` (цифру менять честно).
EFFECT: Создаёт ощущение востребованности и социального доказательства, повышает доверие к исполнителю.
RISK: Если цифра не будет обновляться — потеря доверия; нужна честность.
ROLLBACK: git checkout index.html.
VERIFY: Найти фразу «сейчас работаю» в файле; проверить, что она не конфликтует с другими обещаниями.
PRIORITY: 2 — усиливает доверие, но не критично.
SITE_REQUEST: hero-note

IDEA: Конверсия: «Что вы получите» — 3 пункта с галочками прямо под CTA в hero
KNOB: В hero после `.hero-note` (L465) добавить `<ul class="hero-checkmarks"><li>Готовый сайт за 2 дня</li><li>Виден в Яндексе</li><li>Бесплатное демо до оплаты</li></ul>` + CSS `.hero-checkmarks{list-style:none;display:flex;gap:16px;flex-wrap:wrap;margin-top:16px;font-size:14px;color:var(--muted)} .hero-checkmarks li::before{content:'✓';color:var(--blue);margin-right:6px}`.
EFFECT: Усиливает оффер, снимает возражения «а что я получу», повышает ясность и конверсию.
RISK: Может перегрузить первый экран на мобильных (нужно компактно).
ROLLBACK: git checkout index.html.
VERIFY: Открыть файл, найти `.hero-checkmarks` — проверить, что блок не ломает вёрстку.
PRIORITY: 2 — улучшает конверсию, но требует аккуратной вёрстки.
SITE_REQUEST: hero
