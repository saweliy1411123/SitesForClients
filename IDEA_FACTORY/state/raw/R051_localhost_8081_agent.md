# localhost:8081/agent  2026-11-17 04:08:22
duration=97.7 error=- attempts=1

IDEA: Сравнение мобильного рендера «до/после» через CSS-инъекцию для проверки первого экрана
KNOB: METHOD: (1) Открыть index.html, DevTools → Device Toolbar → 360px. (2) В Console выполнить: `document.body.insertAdjacentHTML('afterbegin','<style>.hero{padding-top:96px}.hero p.sub{margin:16px 0 24px}.btn-primary{min-height:48px}</style>')`. (3) Сделать скриншот, сравнить с оригиналом. (4) Оценить, виден ли CTA без скролла.
EFFECT: Быстрая проверка гипотезы «уменьшение отступов hero улучшает видимость CTA на мобильных» без редактирования файла
RISK: Визуальная оценка субъективна, не заменяет реальный A/B-тест
ROLLBACK: Обновить страницу (Ctrl+R) — инъекция исчезнет
VERIFY: 5 минут: скриншот до/после, проверка видимости CTA на 360px
PRIORITY: 2 — быстрый способ проверить мобильную гипотезу перед внесением правок

IDEA: Проверка читаемости текста на фоне blob-градиентов через CSS-фильтр
KNOB: METHOD: (1) Открыть index.html, DevTools → Console. (2) Выполнить: `document.body.insertAdjacentHTML('afterbegin','<style>.hero{filter:grayscale(1) contrast(1.2)}</style>')`. (3) Оценить контраст текста h1/p.sub без цветовых отвлекающих факторов. (4) Убрать фильтр, сравнить.
EFFECT: Выявление проблем контраста, скрытых цветными градиентами, за 2 минуты
RISK: Искусственное обесцвечивание может показать ложные проблемы
ROLLBACK: Обновить страницу (Ctrl+R)
VERIFY: 2–3 минуты: визуальная проверка читаемости h1 и подзаголовка
PRIORITY: 3 — полезно, но не критично; контраст уже проверен ранее

IDEA: Тест «одна CTA-ссылка» — проверка фокуса внимания через временное скрытие элементов
KNOB: METHOD: (1) Открыть index.html, DevTools → Console. (2) Выполнить: `document.body.insertAdjacentHTML('afterbegin','<style>.hero .btn-primary{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);z-index:9999;width:80%;max-width:320px}</style>')`. (3) Прокрутить страницу, оценить, насколько часто взгляд возвращается к CTA. (4) Убрать стиль.
EFFECT: Проверка гипотезы «плавающая CTA повышает заметность» без изменения HTML
RISK: Тест не показывает реальное поведение пользователя, только визуальную заметность
ROLLBACK: Обновить страницу (Ctrl+R)
VERIFY: 5 минут: прокрутка страницы, субъективная оценка заметности CTA
PRIORITY: 3 — интересный эксперимент, но требует реального A/B для выводов

IDEA: Проверка скорости загрузки без Google Fonts (имитация офлайн/блокировки)
KNOB: METHOD: (1) DevTools → Network → Online → Offline (или заблокировать fonts.googleapis.com). (2) Перезагрузить index.html. (3) Замерить время до первого рендера и FCP. (4) Сравнить с обычной загрузкой.
EFFECT: Оценка влияния Google Fonts на скорость первого рендера и решение о self-hosting
RISK: Не учиты
