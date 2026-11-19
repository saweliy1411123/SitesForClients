# lareper/glm-5.3  2026-11-17 06:01:56
duration=51.4 error=- attempts=1

IDEA: Декоративные blob-фоны как aria-hidden для скринридеров
KNOB: Ко всем декоративным элементам фона (`.final-bg`, `.final-veil`, blob-элементы в hero — классы из `@keyframes blob*`, см. L380–384) добавить атрибут `aria-hidden="true"` и `tabindex="-1"`, чтобы скринридер их не озвучивал.
EFFECT: Чистая последовательность чтения для незрячих пользователей — только контент, без шума «изображение, градиент»; плюс к Lighthouse Accessibility.
RISK: Минимальный — чисто атрибутивная правка, на визуал не влияет.
ROLLBACK: `git checkout -- index.html`
VERIFY: DevTools → Elements → найти .final-bg, убедиться что aria-hidden стоит; вкладка Accessibility tree — элемент исчез из дерева.
PRIORITY: 3 (полировка a11y, быстрый выигрыш без риска)

IDEA: Мобильное меню вместо скрытых nav-links
KNOB: Сейчас `@media(max-width:720px){.nav-links{display:none}}` (L90) — на мобильных навигация исчезает полностью. Добавить компактное раскрывающееся меню: чекбокс-хак (`<input type="checkbox" id="nav-toggle" class="nav-toggle">` + `<label for="nav-toggle" aria-label="Открыть меню">≡</label>`) без JS, ссылки «Цена», «Демо», «FAQ» остаются доступными на телефоне.
EFFECT: Мобильный пользователь получает прямой путь к цене/FAQ/CTA из шапки — меньше прокрутки, выше шанс дойти до заявки.
RISK: Дополнительный CSS-блок может конфликтовать с существующей высотой nav (68px) — нужно аккуратно позиционировать выпадающий список.
ROLLBACK: `git checkout -- index.html`
VERIFY: DevTools → Toggle device toolbar → iPhone-профиль → клик по ≡ → меню открывается/закрывается, ссылки кликабельны, Tab-фокус доходит.
PRIORITY: 1 (реально потерянный конверсионный путь на мобильных, где основной трафик)

IDEA: robots.txt + sitemap.xml для индексации
KNOB: Создать рядом с index.html два файла: `robots.txt` (`User-agent: *\nAllow: /\nSitemap: https://<домен>/sitemap.xml`) и `sitemap.xml` с единственным URL главной. Домен подставить после размещения — пометить в комментарии.
EFFECT: Поисковики корректно индексируют единственную страницу и не находят служебные файлы (IDEA_FACTORY, index.improved.html) как дубли.
RISK: Требует решения владельца — реальный домен неизвестен до публикации; без домена файлы создаются с placeholder.
ROLLBACK: Удалить два файла: `del robots.txt sitemap.xml` (или git clean).
VERIFY: Открыть robots.txt локально в браузере — синтаксис валиден; после публикации — Яндекс.Вебмастер → «Проверка robots.txt».
PRIORITY: 2 (нужно для SEO, но блокируется наличием домена)

IDE
