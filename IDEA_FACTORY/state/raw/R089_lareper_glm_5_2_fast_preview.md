# lareper/glm-5.2-fast-preview  2026-11-17 06:01:51
duration=46.4 error=- attempts=1

IDEA: robots.txt + sitemap.xml для индексации лендинга
KNOB: создать в корне репозитория `robots.txt` (`User-agent: *\nAllow: /\nSitemap: https://<домен>/sitemap.xml`) и `sitemap.xml` с одним URL `<loc>https://<домен>/</loc>` и `<lastmod>` по дате коммита; домен подставить реальный после деплоя
EFFECT: поисковики быстрее и полнее индексируют страницу; sitemap — сигнал для Яндекса/Google, что это единственная каноничная страница
RISK: если домен в sitemap не совпадёт с реальным после деплоя, поисковик проигнорирует sitemap
ROLLBACK: `git checkout -- robots.txt sitemap.xml` или удалить оба файла
VERIFY: до деплоя — валидатор XML (открыть sitemap.xml в браузере, не должно быть ошибки парсинга); после деплоя — Яндекс.Вебмастер → «Обход роботом» за 5 минут
PRIORITY: 2 — сайт статический и одностраничный, эффект умеренный, но это база локального SEO, которой пока нет

IDEA: content-visibility:auto для секций ниже первого экрана
KNOB: в `<style>` добавить `@media (min-width:1px){ section:not(.hero){content-visibility:auto; contain-intrinsic-size:auto 800px;} }` — применить ко всем секциям кроме hero
EFFECT: браузер пропускает рендер/лейаут невидимых секций, ускоряется First Paint и время до интерактивного CTA на слабых мобильных устройствах
RISK: при неточной `contain-intrinsic-size` возможен скачок скроллбара (layout shift) при прокрутке
ROLLBACK: удалить добавленный CSS-блок одной правкой (`git checkout
