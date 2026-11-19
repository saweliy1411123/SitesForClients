# localhost:8081/big_only  2026-11-17 08:14:54
duration=71.4 error=- attempts=1

IDEA: Метод «проверка читаемости на низком разрешении»
KNOB: METHOD: (1) Открыть index.html, F12 → Toggle device toolbar (375px). (2) В консоли выполнить: `document.body.style.filter = 'blur(2px)'; document.body.style.transform = 'scale(0.5)';`
EFFECT: Оценить читаемость контента на низком разрешении
RISK: Нет рисков
ROLLBACK: Отменить изменения в консоли
VERIFY: Проверить читаемость текста на низком разрешении
PRIORITY: 2, так как проверка читаемости является важным аспектом юзабилити и доступности
SITE_REQUEST: «hero»
