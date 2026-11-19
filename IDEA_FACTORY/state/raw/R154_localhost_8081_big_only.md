# localhost:8081/big_only  2026-11-17 09:07:24
duration=43.2 error=- attempts=1

IDEA: Preconnect & DNS‑prefetch для доменов шрифтов Google  
KNOB: В `<head>` добавить ссылки `<link rel="preconnect" href="https://fonts.googleapis.com">` и `<link rel="dns-prefetch" href="https://fonts.gstatic.com">` перед загрузкой Google Fonts.  
EFFECT: Сокращение времени до первого рендеринга текста (FOIT) ≈ 30‑50 мс, улучшение Core Web Vitals.  
RISK: Минимальный – небольшое увеличение HEAD‑размера; не влияет на работу браузеров без поддержки preconnect.  
ROLLBACK: `git checkout -- index.html` (или удалить добавленные строки).  
VERIFY: Открыть страницу в Chrome DevTools → Network, включить “Disable cache”, измерить время загрузки запросов к `fonts.googleapis.com`/`fonts.gstatic.com` до и после изменения (должно исчезнуть задержка DNS).  
PRIORITY: 1 — ускорение LCP и CLS, критично для SEO и конверсии.  

IDEA: Добавить `font-display: swap` к запросу Google Fonts  
KNOB: Изменить URL импорта шрифтов в `<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap">` → добавить параметр `&display=swap` (если отсутствует) или изменить существующий на `swap`.  
EFFECT: Текст будет отображаться сразу системным шрифтом, потом заменяться на Manrope без «белого пятна», повышая восприятие скорости.  
RISK: Возможна короткая «перепрыгивание» шрифта, но это лучше, чем отсутствие текста.  
ROLLBACK: `git checkout -- index.html` (откатить изменение URL).  
VERIFY: В DevTools → Network → Font, убедиться, что запрос имеет `display=swap`; в Performance смотреть, что FOIT исчез.  
PRIORITY: 1 — прямое влияние на First Contentful Paint и пользовательский опыт.  

IDEA: Сжимающийся фиксированный хедер при скролле  
KNOB: Добавить класс `.sticky-header` к `<header class="hero">`; в CSS задать `position:fixed; top:0; width:100%; transition:transform .3s;` и `transform:translateY(-100%);` по умолчанию, а при скролле `transform:translateY(0);` через небольшую JS‑функцию, меняющую класс `scrolled`.  
EFFECT: Пользователь всегда видит навигацию, но она не занимает много места; повышает удобство мобильных пользователей и время на странице.  
RISK: Требует небольшого JS; может конфликтовать с текущим скролл‑поведением, если уже есть обработчики.  
ROLLBACK: `git checkout -- index.html` (удалить добавленные блоки CSS/JS).  
VERIFY: На мобильном и десктопе открыть страницу, прокрутить вниз — хедер должен появиться/исчезнуть плавно; проверить отсутствие «jump» в layout (CLS).  
PRIORITY: 2 — улучшает UX, но не критично для SEO.  

IDEA: Расширенные ARIA‑ландмарки и фокус‑менеджмент для секций  
KNOB: В `<body>` добавить `role="main"` к главному контейнеру (например, `<main id="main">`), `role="contentinfo"` к футеру (если есть), `tabindex="-1"` ко всем `<section id="...">` для возможности фокусировать их при переходах по якорям; также добавить `aria-label` к навигационным ссылкам, где текст не ясен.  
EFFECT: Улучшает навигацию скрин‑ридеров, повышает доступность и удовлетворяет WCAG 2.1 AA, что положительно сказывается на SEO (Google учитывает доступность).  
RISK: Небольшой риск конфликтов с уже существующими ролями; требуется аккуратное добавление без дублирования.  
ROLLBACK: `git checkout -- index.html` (удалить добавленные атрибуты).  
VERIFY: В Chrome DevTools → Accessibility, включить “Accessibility Tree”, убедиться, что роли/label отображаются; выполнить быстрый тест Tab‑navigation, проверив, что фокус переходит к секциям без скроллинга.  
PRIORITY: 2 — важный, но не критичный для конверсии; повышает репутацию бренда.
