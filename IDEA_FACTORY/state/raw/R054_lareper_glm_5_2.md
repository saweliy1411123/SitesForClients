# lareper/glm-5.2  2026-11-17 04:19:00
duration=23.9 error=- attempts=2

IDEA: aria-hidden для декоративных слоёв (particles, blob, veil)
KNOB: Элементам `#particles` (L103), фоновым blob-слоям (L58, L195, L204, L284, L332) и `.hero-veil`/`.final-veil` добавить атрибут `aria-hidden="true"` (и `role="presentation"`, если это div с контентом-псевдографикой). Скринридеры сейчас могут объявлять пустые/декоративные блоки как «регионы» и замедлять чтение.
EFFECT: Чистая линейная навигация для скринридера — пользователь сразу попадает на h1 и оффер; плюс к Lighthouse Accessibility.
RISK: Если случайно пометить aria-hidden блок с реальным текстом — он исчезнет из дерева доступности.
ROLLBACK: `git checkout -- index.html` (правки вносить в index.improved.html).
VERIFY: DevTools → Elements → Accessibility tree: до/после — декоративные узлы не должны появляться; 2 минуты.
PRIORITY: 2 — дёшево, заметный a11y-выигрыш, не задето в куче (I-00255 касался только svg в боли).

IDEA: Создать robots.txt и sitemap.xml рядом с index.html
KNOB: Добавить два файла в корень
