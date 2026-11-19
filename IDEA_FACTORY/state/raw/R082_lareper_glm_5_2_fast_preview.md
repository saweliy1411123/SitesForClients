# lareper/glm-5.2-fast-preview  2026-11-17 05:40:09
duration=5.9 error=- attempts=2

IDEA: robots.txt + sitemap.xml для индексации лендинга
KNOB: создать рядом с index.html файл `robots.txt` (`User-agent: *\nAllow: /\nSitemap: https://<домен>/sitemap.xml`) и `sitemap.xml` с одним URL — после публикации на домен
EFFECT: поисковики быстрее и полнее индексируют страницу, sitemap ускоряет появление в Яндексе/Google
RISK: до публикации домен неизвестен — URL в sitemap будет заглушкой, нужно обновить после деплоя
ROLLBACK: удалить оба файла (`del robots.txt sitemap.xml`) или не коммитить
VERIFY: открыть robots.txt в браузере до деплоя — синтаксис; после деплоя — Яндекс.Вебмастер → «Проверка robots.txt» (2 мин)
PRIORITY: 2 — сайт статический и пока не опубликован, но это обязательный минимум SEO перед запуском

IDEA: canonical + meta robots для чистоты индексации
KNOB: в `<head>` (после og-тегов) добавить `<link rel="canonical" href="https://<домен>/">` и `<meta name="robots" content="index, follow, max-image-preview:large">`
EFFECT: исключает дубли (www/без www, копии index.improved.html при случайной публикации), даёт поисковикам явную инструкцию
RISK: неверный домен в canonical направит индексацию не туда — требует решения владельца (финальный URL)
ROLLBACK: git checkout -- index.html
VERIFY: Ctrl+U → проверить наличие тегов; после деплоя — «Проверка URL» в Google Search Console (3 мин)
PRIORITY: 2 — защита от дублей важна, но блокируется отсутствием домена

IDEA: touch-target ≥44px для всех ссылок-CTA и навигации на мобильных
KNOB: в CSS добавить `@media (max-width:768px){ a, .btn-primary, nav a{min-height:44px; min-width:44px; display:inline-flex; align-items:center} }` и проверить паддинги ссылок в `<nav>` (L441–444)
EFFECT: соответствие WCAG 2.5.8 / рекомендациям Apple и Google — меньше промахов по CTA с телефона, рост мобильной конверсии
RISK: увеличение min-height может «распыхать» навигацию на узких экранах — потребуется подгонка паддингов
ROLLBACK: git checkout -- index.html
VERIFY: DevTools → iPhone SE (375px) → Console: `[...document.querySelectorAll('a')].forEach(a=>{const r=a.getBoundingClientRect(); if(r.height<44) console.log(a.textContent.trim(), r.height)})` (3 мин)
PRIORITY: 1 — дёшево, напрямую влияет на мобильную конверсию и a11y-аудит

IDEA: aria-label и aria-current на навигации + подпись единственного script
KNOB: в `<nav>` (L440) добавить `aria-label="Основная навигация"`; активной/текущей ссылке якоря при скролле — `aria-current="true"`; существующему `<script>` (1 шт) добавить `defer` если он не критичен для первого рендера
EFFECT: скринридеры озвучивают навигацию корректно; defer убирает
