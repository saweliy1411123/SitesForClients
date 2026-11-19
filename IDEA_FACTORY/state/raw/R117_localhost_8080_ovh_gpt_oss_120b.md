# localhost:8080/ovh/gpt-oss-120b  2026-11-17 07:23:13
duration=24.5 error=- attempts=1

IDEA: Добавить структурированные данные FAQ‑schema.org (FAQPage) в <head>
KNOB: Вставить <script type="application/ld+json"> с массивом вопросов‑ответов, взятых из секции FAQ (h2/h3). Убедиться, что каждый вопрос‑ответ уникален и соответствует visible тексту.
EFFECT: Повышает видимость в поиске (расширенные сниппеты), улучшает SEO и доверие пользователей.
RISK: Требует точного соответствия контенту; если FAQ изменится, данные могут стать неактуальными.
ROLLBACK: Удалить вставленный <script> (git checkout -- index.html) или закомментировать его.
VERIFY: Открыть Chrome DevTools → Console → `JSON.parse(document.querySelector('script[type="application/ld+json"]').innerHTML)` и убедиться, что структура валидна; затем выполнить https://search.google.com/structured-data/testing-tool/ на локальном файле.
PRIORITY: 1 – быстрый, без кода бэкенда, сразу улучшает CTR в SERP.

IDEA: Улучшить контраст текста для WCAG AA (особенно var(--muted) и фоновые градиенты)
KNOB: В CSS добавить правило `:root { --muted: #6b7280; }` (повысить яркость) и в секциях с низким контрастом (например, .hero-note, .sub) установить `color: var(--text)` или `color: #e5e7eb`. Добавить `@media (prefers-contrast: more)` альтернативные цвета.
EFFECT: Повышает доступность, снижает показатель CLS (меньше пере‑рисовки) и улучшает восприятие на мобильных.
RISK: Изменение визуального стиля может слегка изменить фирменный вид.
ROLLBACK: Откатить изменения в CSS (git checkout -- index.html) или вернуть прежние значения переменных.
VERIFY: В Chrome DevTools → Lighthouse → Accessibility, проверить пункт “Contrast ratio”. Также визуально сравнить скриншоты до/после.
PRIORITY: 2 – важный для соответствия рекомендациям, но менее критичен для SEO, чем структурированные данные.

IDEA: Добавить предзагрузку DNS и шрифтов Manrope (preconnect + preload) для ускорения LCP
KNOB: В <head> перед существующими `<link rel="preconnect">` добавить:
```html
<link rel="dns-prefetch" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap" onload="this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap"></noscript>
```
EFFECT: Сократит время загрузки шрифтов, улучшит LCP и First Contentful Paint.
RISK: Небольшой рост объёма HTML (≈200 байт) и возможные блокировки в строгих CSP, если они появятся.
ROLLBACK: Удалить добавленные строки (git checkout -- index.html) или закомментировать.
VERIFY: В Chrome DevTools → Network, включить “Disable cache”, перезагрузить и посмотреть время загрузки `fonts.googleapis.com` и `fonts.gstatic.com`; сравнить LCP в Performance.
PRIORITY: 1 – прямое влияние на Core Web Vitals, быстрый фикс.

IDEA: Сделать ссылки‑CTA семантически кнопками с ролью button и aria‑label
KNOB: Для всех `<a class="btn-primary"...>` изменить на `<button class="btn-primary" type="button" aria-label="Получить демо бесплатно" onclick="location.href='#contact'">…</button>` или добавить `role="button"` и `aria-label` к текущим `<a>`.
EFFECT: Улучшает доступность (клавиатурная навигация, скрин‑ридеры), повышает показатель Accessibility в Lighthouse.
RISK: Требует небольшого JS для перехода по якорю (можно использовать `href="#contact"` в `<a>` и оставить `role="button"`; изменение в `<button>` без `href` может ломать fallback в случае отключённого JS).
ROLLBACK: Вернуть оригинальные `<a>` (git checkout -- index.html).
VERIFY: В Chrome DevTools → Accessibility, проверить, что элементы объявлены как button; протестировать Tab‑navigation, убедиться, что фокус переходит к кнопке и срабатывает переход.
PRIORITY: 2 – важный для a11y, но не критичен для SEO напрямую.

IDEA: Внедрить «scroll‑margin‑top» для всех якорных секций, чтобы фиксированный хедер не перекрывал контент
KNOB: В CSS добавить:
```css
section[id] { scroll-margin-top: 100px; } /* высота хедера + небольшой отступ */
```
EFFECT: При клике на навигационные ссылки пользователь видит начало секции, повышает UX и снижает bounce rate.
RISK: При изменении высоты хедера может потребоваться корректировка значения.
ROLLBACK: Удалить правило (git checkout -- index.html) или задать `scroll-margin-top: 0;`.
VERIFY: Кликнуть по каждой навигационной ссылке, убедиться, что контент не скрыт под хедером.
PRIORITY: 1 – быстрый UI‑улучшение, не требует кода бэкенда.

IDEA: Добавить «Back‑to‑Top» кнопку, фиксированную в правом нижнем углу, с плавным скроллом
KNOB: В <body> добавить `<button class="scroll-top" aria-label="Наверх">↑</button>`; в CSS:
```css
.scroll-top{
  position:fixed;right:1rem;bottom:1rem;
  width:2.5rem;height:2.5rem;
  background:var(--grad);
  color:#fff;border:none;border-radius:50%;
  display:none;align-items:center;justify-content:center;
  cursor:pointer;z-index:1000;
}
.scroll-top.show{display:flex;}
```
и JS (inline, defer‑compatible):
```js
const btn=document.querySelector('.scroll-top');
window.addEventListener('scroll',()=>{ btn.classList.toggle('show',window.scrollY>300); });
btn.addEventListener('click',()=>window.scrollTo({top:0,behavior:'smooth'}));
```
EFFECT: Уменьшает фрустрацию пользователей, особенно на мобильных, повышает время на сайте.
RISK: Добавит небольшой JS‑файл (≈1 KB); возможен конфликт с уже существующим скриптом, если используют одинаковые переменные.
ROLLBACK: Удалить элемент и связанные блоки CSS/JS (git checkout -- index.html).
VERIFY: Прокрутить страницу, убедиться в появлении кнопки, клик → плавный скролл к верху.
PRIORITY: 2 – улучшает UX, но менее критично для SEO.

IDEA: Добавить атрибут `title` ко всем внешним ссылкам (Telegram) для лучшего контекстного подсказа
KNOB: Для `<a href="https://t.me/...">` добавить `title="Открыть в Telegram – бесплатное демо"` (можно через поиск‑замену).
EFFECT: Повышает доступность (tooltip для скрин‑ридеров) и CTR, особенно в мобильных браузерах.
RISK: Небольшой рост HTML‑размера.
ROLLBACK: Удалить атрибут `title` (git checkout -- index.html).
VERIFY: Навести курсор на ссылки, увидеть подсказку; в Lighthouse Accessibility проверить отсутствие «link missing descriptive text».
PRIORITY: 3 – мелкое улучшение, но быстро реализуемое.

IDEA: Включить meta‑теги Twitter Card (summary_large_image) для соцсетей
KNOB: В <head> добавить:
```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Сайт для вашего бизнеса за 2 дня — клиенты находят вас в Яндексе">
<meta name="twitter:description" content="Быстрый лендинг за 2 дня, привлекающий клиентов из поиска.">
<meta name="twitter:image" content="https://example.com/assets/og-image.jpg">
```
EFFECT: При шаринге в Twitter будет отображаться красивый превью‑блок, повышая кликабельность.
RISK: Нужно обеспечить доступность изображения по указанному URL; если URL недоступен, превью будет пустым.
ROLLBACK: Удалить метатеги (git checkout -- index.html).
VERIFY: В https://cards-dev.twitter.com/validator вставить URL локального файла (можно через ngrok) и проверить отображение.
PRIORITY: 2 – улучшает соцсетевой охват, не влияет на Core Web Vitals.
