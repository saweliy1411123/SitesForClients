# lareper/deepseek-v4-pro-0813  2026-11-17 07:02:04
duration=2.4 error=- attempts=2

IDEA: Динамическая цена с выбором опций в карточке (интерактивный прайс)
KNOB: В `.price-card` (L644) заменить статичную строку цены (`<div class="price">12 000 ₽</div>` и т.п.) на интерактивный блок: `<div class="price-options" role="radiogroup" aria-label="Выбор тарифа"><label><input type="radio" name="price-opt" value="base" checked> <span>База — 12 000 ₽</span></label><label><input type="radio" name="price-opt" value="plus"> <span>Плюс — 18 000 ₽</span></label><label><input type="radio" name="price-opt" value="max"> <span>Макс — 25 000 ₽</span></label></div>`. Названия опций и цены — примерные, уточнить у владельца.
EFFECT: Посетитель сам выбирает подходящий объём работ, видит честную вилку цен, меньше боится «сюрпризов» и охотнее оставляет заявку; повышает воспринимаемую прозрачность.
RISK: Может перегрузить карточку, если опций больше 3; требует уточнения реальных тарифов у владельца (иначе вымысел).
ROLLBACK: `git checkout index.html` или удалить добавленный блок `.price-options`.
VERIFY: Открыть страницу, проверить, что радиокнопки переключаются и цена/описание меняются без перезагрузки; визуально не ломают карточку.
PRIORITY: 2 — усиливает ключевую секцию «Цена», но требует контентного решения владельца.
SITE_REQUEST: price-card
SKILL:
