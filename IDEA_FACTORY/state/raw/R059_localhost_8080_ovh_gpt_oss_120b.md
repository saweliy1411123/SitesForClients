# localhost:8080/ovh/gpt-oss-120b  2026-11-17 04:32:05
duration=18.8 error=- attempts=1

IDEA: Критика текущей кучи идей  
KNOB: Обзор всех предложений I‑00273…I‑00392; выявить дубли (например, hero‑clarity‑boost, hero‑clarity‑fix, hero‑clarity‑boost), избыточные методы без измеримых KPI (exit‑intent, carousel, парраллкс‑анимации), предложения, требующие бекенда (click‑heatmap, exit‑intent, соц‑счётчики) и идеи, уже покрытые базовыми практиками (preconnect‑fonts, skip‑to‑content).  
EFFECT: Уменьшит шум в бэклоге, сосредоточит внимание на реально ценных улучшениях, ускорит процесс принятия решений.  
RISK: Возможна пропущенная уникальная идея; требуется внимательность при удалении.  
ROLLBACK: Восстановить удалённые строки из git (`git checkout HEAD~1 -- index.html`).  
VERIFY: Сгенерировать список уникальных идей (скриптом) и сравнить с оригиналом; убедиться, что оставшиеся покрывают все категории (SEO, A11y, Speed, Conversion).  
PRIORITY: 1 – критично для планирования дальнейших работ.  

---  

IDEA: Замена I‑0045 «Accessible CTA Buttons instead of anchor‑links» на более безопасный и семантичный вариант  
KNOB: Заменить все ссылки‑CTA `<a class="btn-primary …" href="#contact">…</a>` на `<button type="button" class="btn-primary" data-scroll-target="#contact">…</button>` и добавить небольшую JS‑обёртку, которая при клике скроллит к target (`document.querySelector(target).scrollIntoView({behavior:'smooth'});`).  
EFFECT: Улучшит доступность (кнопка воспринимается скрин‑ридером как действие), устранит потенциальные проблемы с SEO‑индексацией (поисковые боты не воспринимают кнопку как ссылку), повысит консистентность UI.  
RISK: Требует небольшого JS‑скрипта (≈30 Б) и может конфликтовать с существующим `onclick` в hero‑visual; необходимо убедиться, что стили `.btn-primary` работают с `<button>`.  
ROLLBACK: `git checkout -- index.html && git apply revert-cta.patch` (или просто откатить изменения в файле).  
VERIFY: Открыть страницу, проверить, что Tab‑перемещение попадает на кнопку, скролл работает, а в DevTools → Accessibility кнопка имеет роль `button`.  
PRIORITY: 2 – высокое влияние на A11y и небольшие затраты.  

---  

IDEA: Замена I‑0044 «Preconnect + font-display swap for Google Fonts» на полную оптимизацию шрифтов через `font-display: optional` и локальное кэширование  
KNOB: 1) В `<head>` заменить текущие `<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">` на `<link rel="preload" href="fonts/Manrope-400.woff2" as="font" type="font/woff2" crossorigin>` (и аналогично для остальных весов) + `<style>@font-face{font-family:'Manrope';src:url('fonts/Manrope-400.woff2') format('woff2');font-weight:400;font-display:optional;}</style>`.  
2) Добавить `rel="preconnect"` к `https://fonts.gstatic.com` и `https://fonts.googleapis.com`.  
EFFECT: Уменьшит количество запросов к Google, ускорит First Contentful Paint (FCP) за счёт предзагрузки шрифтов, уменьшит блокирующее рендеринг время, улучшит метрику LCP.  
RISK: Требует загрузки файлов шрифтов в проект (≈150 KB) и корректного пути; если файлы не найдены, текст будет отображаться системным шрифтом.  
ROLLBACK: Удалить добавленные `<link rel="preload">` и `<style>`‑блок; восстановить оригинальный `<link href="https://fonts.googleapis.com/...">`.  
VERIFY: В Chrome DevTools → Network проверить, что шрифты загружаются как `preload` (status 200) и нет блокирующего CSS; измерить FCP до/после через Lighthouse.  
PRIORITY: 1 – значительное ускорение загрузки без изменения контента, быстрый ROI.
