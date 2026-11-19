# lareper/glm-5.3  2026-11-17 04:36:11
duration=12.2 error=- attempts=1

IDEA: Hero — вторая CTA-ссылка «Показать пример цены» (снятие ценового возражения до скролла)
KNOB: В hero после `.btn-primary` (L462) добавить текстовую ссылку `<a class="link-ghost" href="#price">Узнать цену — от X ₽ за 2 дня</a>`; CSS: `.link-ghost{color:var(--muted);text-decoration:underline;text-underline-offset:4px;margin-left:16px}`. Точное «от X ₽» взять из `.price-card` (L642+), не выдумывать.
EFFECT: «Холодные» посетители, которых отпугивает неизвестность цены, сразу видят вилку и доходят до секции цены вместо выхода.
RISK: Если цена в карточке формулирована не как «от X ₽», появится расхождение — нужно синхронизировать формулировки.
ROLL
