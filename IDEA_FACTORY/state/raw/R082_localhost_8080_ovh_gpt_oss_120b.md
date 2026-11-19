# localhost:8080/ovh/gpt-oss-120b  2026-11-17 05:39:37
duration=39.2 error=- attempts=1

IDEA: Preconnect к доменам шрифтов Google  
KNOB: В `<head>` добавить сразу перед текущим `<link href="https://fonts.googleapis.com/...">` две строки  
```html
<link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```  
EFFECT: Уменьшит время DNS‑lookup и TLS‑handshake для загрузки шрифтов Manrope → ускорит FCP/LCP, повысит Core Web Vitals.  
RISK: Практически отсутствует; старые браузеры просто игнорируют тег.  
ROLLBACK: Удалить только эти две строки (git checkout HEAD~1 index.html || git restore index.html).  
VERIFY: В Chrome DevTools → Network, включить «Slow 3G», измерить `Time to First Paint` до и после; ожидать сокращения ≈ 100‑200 мс.  
PRIORITY: 1 — самый быстрый выигрыш в скорости без риска.  

---  

IDEA: Канонический URL — защита от дублей  
KNOB: В `<head>` добавить  
```html
<link rel="canonical" href="https://example.com/">
```  
(заменить `example.com` на реальный домен).  
EFFECT: Укажет поисковикам единственный «правильный» URL, улучшит SEO‑вес страниц и предотвратит каннибализацию.  
RISK: Если сайт будет доступен по нескольким доменам, необходимо убедиться, что они действительно дублируют контент.  
ROLLBACK: Удалить строку `<link rel="canonical"...>` (git checkout HEAD~1 index.html).  
VERIFY: В консоли Chrome выполнить `document.querySelector('link[rel=canonical]').href` – должно вернуть ваш основной URL. Затем проверить в Google Search Console → Coverage, отсутствие «duplicate»‑ошибок.  
PRIORITY: 2 — важно для SEO, но требует подтверждения корректного домена.  

---  

IDEA: OG‑изображение для соцсетей  
KNOB: В `<head>` добавить мета‑тег  
```html
<meta property="og:image" content="https://example.com/assets/og-preview.jpg">
```  
(изображение ≈ 1200×630 px, оптимизировано, размещено рядом с index.html).  
EFFECT: При шаринге в соцсетях будет показано привлекательное превью, повышая CTR и узнаваемость бренда.  
RISK: Нужно загрузить реальное изображение — отсутствие файла приведёт к 404‑ошибке в соцсетях.  
ROLLBACK: Удалить строку `<meta property="og:image"...>` (git checkout HEAD~1 index.html).  
VERIFY: В Facebook Sharing Debugger или VK Share Checker ввести URL страницы, убедиться, что изображение отображается без ошибок.  
PRIORITY: 2 — мощный сигнал для соцсетей, простая реализация.  

---  

IDEA: Явные ARIA‑лейблы для навигации  
KNOB: В `<nav>` добавить атрибуты `role="navigation"` и `aria-label="Главное меню"`; каждому пункту меню добавить `aria-current="page"` для активного якоря.  
EFFECT: Улучшит навигацию для скрин‑ридеров, повышая доступность (WCAG 2.1 AA).  
RISK: Неправильный `aria-current` может запутать пользователей; использовать только для текущего якоря.  
ROLLBACK: Удалить атрибуты (git restore index.html).  
VERIFY: Открыть страницу в Chrome → DevTools → Accessibility, убедиться, что навигация помечена как «navigation» и имеет читаемый лейбл. Тестировать Tab‑перемещение – фокус должен попадать в меню.  
PRIORITY: 2 — доступность критична, но изменения небольшие.  

---  

IDEA: Обертка основного контента в `<main id="main">` и улучшение фокус‑скролла для якорей  
KNOB: Обернуть все секции после hero (от первой `<section>` до конца) в `<main id="main">`; добавить каждому целевому элементу (например, `<section id="price">`) атрибут `tabindex="-1"` для возможности фокус‑перемещения после клика на якорную ссылку.  
EFFECT: Семантическое разграничение улучшит SEO (поисковики лучше понимают основной контент) и доступность (скрин‑ридеры сразу попадают в основной контент). `tabindex="-1"` позволяет программно фокусировать секцию, делая переход по якорям более заметным.  
RISK: Неправильный закрывающий тег может сломать разметку; требуется проверить валидность HTML.  
ROLLBACK: Восстановить оригинальный файл (git checkout HEAD~1 index.html).  
VERIFY: В Chrome DevTools → Elements убедиться, что `<main>` присутствует и содержит нужные секции; нажать на любую якорную ссылку и проверить, что фокус переходит к целевой секции (вкладка Elements → `:focus`).  
PRIORITY: 1 — семантика и доступность сразу дают SEO‑бонус и улучшают UX.  

---  

IDEA: Предзагрузка критического CSS‑файла и `font-display: swap` в @font-face  
KNOB: В `<head>` добавить  
```html
<link rel="preload" as="style" href="styles.css" onload="this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="styles.css"></noscript>
```  
и в уже существующем `<style>` (или в отдельном файле) добавить  
```css
@font-face{
  font-family:'Manrope';
  src:url('https://fonts.gstatic.com/s/manrope/v14/...-Regular.woff2') format('woff2');
  font-weight:400;
  font-display:swap;
}
```  
EFFECT: `preload` ускорит загрузку основного CSS, а `font-display:swap` устранит блокировку рендеринга шрифтов → снижается CLS и ускоряется LCP.  
RISK: Если `styles.css` уже инлайн‑встроен, двойная загрузка может увеличить трафик; убедиться, что ссылка указывает на отдельный файл (можно вынести критический CSS в отдельный файл).  
ROLLBACK: Удалить обе вставки (git restore index.html).  
VERIFY: В DevTools → Network проверить, что CSS загружается как `preload` (status 200, `rel=preload`), и измерить CLS/LCP до и после (Lighthouse → Performance).  
PRIORITY: 1 — значительное улучшение Core Web Vitals с минимальными изменениями.  

---  

IDEA: Темная тема по предпочтениям пользователя  
KNOB: В `<style>` добавить медиа‑правило  
```css
@media (prefers-color-scheme: dark) {
  :root{
    --bg:#111;
    --text:#eee;
    --muted:#aaa;
    --grad:linear-gradient(135deg,#8b5cf6,#0da5c5);
  }
}
```  
и убедиться, что все цвета в CSS используют переменные `var(--bg)`, `var(--text)` и т.д. (при необходимости добавить их в текущий набор).  
EFFECT: Пользователи, включившие темный режим, увидят адаптированный дизайн, повышая комфорт и удовлетворённость → косвенно улучшает поведенческие метрики (время на сайте).  
RISK: Нужно проверить, что контраст в темной теме удовлетворяет WCAG AA (тёмный фон + светлый текст).  
ROLLBACK: Удалить медиа‑правило (git checkout HEAD~1 index.html).  
VERIFY: В Chrome DevTools → Rendering включить «Emulate CSS media feature prefers-color-scheme: dark», убедиться, что фон и текст меняются без визуальных артефактов. Проверить контраст через axe‑core (встроенный в DevTools).  
PRIORITY: 3 — не критично для SEO, но повышает UX для части аудитории.
