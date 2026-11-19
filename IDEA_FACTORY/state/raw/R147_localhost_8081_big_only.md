# localhost:8081/big_only  2026-11-17 08:47:54
duration=41.2 error=- attempts=1

IDEA: Preconnect к доменам шрифтов Google Fonts  
KNOB: В `<head>` добавить две ссылки‑предзагрузки: `<link rel="preconnect" href="https://fonts.googleapis.com">` и `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>`  
EFFECT: Сокращение TTFB для загрузки шрифтов → быстрее First Contentful Paint, лучше Core Web Vitals  
RISK: Никакого, только небольшое увеличение HTML‑размера ≈ 140 байт  
ROLLBACK: `git checkout -- index.html` (или удалить добавленные строки)  
VERIFY: Открыть DevTools → Network, включить Disable cache, обновить страницу, сравнить `fonts.googleapis.com` и `fonts.gstatic.com` запросы — должны быть preconnected (статус 200 без DNS‑lookup)  
PRIORITY: 1 – влияние на скорость критично для SEO и конверсии  

IDEA: Улучшить доступность CTA‑ссылок (роль button, aria‑label)  
KNOB: Для всех ссылок‑CTA (например, в `.hero .cta-row a`, `.final a`) добавить атрибуты `role="button"` и `aria-label="Получить бесплатное демо"` (текст можно брать из visible текста)  
EFFECT: Увеличение доступности для скрин‑ридеров, улучшение навигации клавиатурой → рост конверсии среди пользователей‑с ограниченными возможностями  
RISK: Требует согласования текста aria‑label, иначе дублирование; минимальный риск несоответствия UX, но легко поправить  
ROLLBACK: `git checkout -- index.html` (удалить добавленные атрибуты)  
VERIFY: Включить VoiceOver/Screen Reader, перейти к CTA‑ссылке клавишей Tab — должно озвучиваться «Получить бесплатное демо, button»; также в DevTools → Elements проверить наличие атрибутов  
PRIORITY: 2 – доступность ≈ 30 % всех пользователей, плюс SEO‑плюс  

IDEA: SKILL — premium-typography-hover  
KNOB: **Name:** `premium-typography-hover`  
**When to apply:** На любые крупные заголовки (h1, h2) и ссылки‑CTA, где нужен премиальный визуальный отклик  
**SAFE CSS:**  
```css
/* premium-typography-hover */
h1, h2, .btn-primary {
  font-variation-settings: "wght" 500;
  transition: font-variation-settings 250ms ease, transform 250ms ease;
}
h1:hover, h2:hover, .btn-primary:hover,
h1:focus-visible, h2:focus-visible, .btn-primary:focus-visible {
  font-variation-settings: "wght" 700;
  transform: translateY(-2px);
}
```
EFFECT: При наведении/фокусе заголовки плавно «утолщаются», создавая ощущение премиального качества и усиливая визуальный клик‑трэкинг → потенциальный рост CTR на CTA‑элементы  
RISK: Требует, чтобы шрифт Manrope поддерживал вариативный вес 500‑700 (он так и есть); на старых браузерах может игнорировать `font-variation-settings` → безопасно, просто без эффекта  
ROLLBACK: Удалить файл `SKILLS/premium-typography-hover.md` и строку `@import "./SKILLS/premium-typography-hover.css"` из `index.improved.html` (или `git checkout -- index.improved.html`)  
VERIFY: Открыть страницу, навести курсор на h1/h2/CTA — должно наблюдаться плавное утолщение текста и небольшое поднятие; в DevTools → Computed проверить `font-variation-settings` меняется с 500 на 700  
PRIORITY: 3 – мягкое UX‑улучшение, низкий риск, но потенциальный рост конверсии при премиальном восприятии.
