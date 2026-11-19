# localhost:8080/ovh/gpt-oss-120b  2026-11-17 01:53:40
duration=47.8 error=- attempts=1

IDEA: Добавить атрибут `lang="ru"` к корневому элементу `<html>`  
KNOB: в открывающий тег `<html>` добавить `lang="ru"` (и, при необходимости, `dir="ltr"`).  
EFFECT: Улучшит локальное SEO, позволит поисковикам и скрин‑ридерам правильно определять язык страницы.  
RISK: Минимальный — возможен конфликт, если уже используется другой язык в контенте.  
ROLLBACK: `git checkout -- index.html` (или удалить атрибут в файле).  
VERIFY: Открыть страницу в Chrome DevTools → Elements и убедиться, что `<html lang="ru">` присутствует; проверить в Lighthouse → SEO, пункт “Language”.  
PRIORITY: 1 – быстрый, безрисковый апдейт, сразу повышает SEO и доступность.  

IDEA: Обернуть основной контент в семантический `<main id="main">` и добавить `role="navigation"` с `aria-label="Главное меню"` к навигационной секции  
KNOB: добавить `<nav aria-label="Главное меню">` вокруг существующего списка ссылок (или создать `<nav>` если его нет) и обернуть все основные секции в `<main id="main">`.  
EFFECT: Явно указывает структуру страницы для скрин‑ридеров и поисковых роботов, улучшает навигацию клавиатурой и индексацию.  
RISK: Требует небольшого изменения HTML‑структуры; может потребовать корректировки CSS‑селекторов.  
ROLLBACK: `git checkout -- index.html` (или вернуть прежний код из коммита).  
VERIFY: В DevTools проверить, что `<main id="main">` охватывает контент и `<nav aria-label="Главное меню">` присутствует; выполнить тест клавиатурной навигации (Tab) — фокус должен переходить в навигацию, а затем в контент.  
PRIORITY: 2 – небольшое изменение, повышает доступность и SEO, но требует проверки CSS‑совместимости.  

IDEA: Преобразовать CTA‑ссылки в семантические кнопки с ARIA‑метками и стилизовать фокус  
KNOB: заменить `<a class="btn-primary ...">` в hero‑секции и в конце страницы на `<button type="button" class="btn-primary" role="button" aria-label="Заказать демо">…</button>`; добавить CSS `.btn-primary:focus-visible{outline:3px solid #8b5cf6;outline-offset:4px;}`.  
EFFECT: Улучшает доступность (скрин‑ридеры правильно озвучивают кнопку), обеспечивает визуальный индикатор фокуса, повышает конверсию за счёт лучшего UX.  
RISK: Требует небольшого JS‑обработчика, если ссылка была якорем; можно добавить `onclick="location.href='#contact'"` или использовать `<a>` внутри `<button>` (не рекомендуется).  
ROLLBACK: Восстановить оригинальные `<a>`‑теги из коммита (`git checkout -- index.html`).  
VERIFY: Нажать Tab, убедиться, что фокус виден на кнопке; проверить в Chrome Accessibility Tree, что элемент имеет роль button.  
PRIORITY: 1 – критично для доступности и соответствует рекомендациям WCAG 2.1.  

IDEA: Добавить `font-display: swap` и предзагрузку шрифтов Google Fonts  
KNOB: в `<head>` после существующего `<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">` добавить `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>` и изменить запрос шрифтов на `&display=swap` (если отсутствует) + добавить `<link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap" onload="this.rel='stylesheet'">`.  
EFFECT: Уменьшает время до первого отображения текста, устраняет «flash of invisible text», улучшает LCP в Lighthouse.  
RISK: Возможны дублирование запросов, если оба `<link rel="stylesheet">` и `preload` остаются; убедиться, что оригинальный `<link>` имеет `rel="preload"` с `onload` и `rel="stylesheet"` заменяется.  
ROLLBACK: Удалить добавленные строки и вернуть оригинальный `<link>` (`git checkout -- index.html`).  
VERIFY: В Chrome DevTools → Network посмотреть, что шрифт загружается с `font-display: swap`; запустить Lighthouse → Performance, сравнить LCP до/после.  
PRIORITY: 2 – небольшое изменение, заметно ускорит рендеринг текста.  

IDEA: Внедрить JSON‑LD разметку `Offer` с ценой и валютой для секции цены  
KNOB: в конец `<body>` добавить  
```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"Offer",
  "priceCurrency":"RUB",
  "price":"19900",
  "url":"https://example.com/",
  "availability":"https://schema.org/InStock",
  "seller":{"@type":"Person","name":"Савелий"}
}
</script>
```  
(заменить `price` и `url` на реальные данные).  
EFFECT: Позволит поисковикам показывать цену в поисковой выдаче, повышая CTR и локальное SEO.  
RISK: Требует согласования точной цены и условий с владельцем; если цена изменится, разметка должна быть обновлена.  
ROLLBACK: Удалить скрипт (`git checkout -- index.html`).  
VERIFY: Прогнать страницу через Google Rich Results Test; убедиться, что Offer распознан без ошибок.  
PRIORITY: 3 – полезно для SEO, но менее критично, чем доступность.  

IDEA: Добавить медиа‑запрос `prefers-reduced-motion` для отключения анимаций у чувствительных пользователей  
KNOB: в CSS добавить  
```css
@media (prefers-reduced-motion: reduce) {
  .reveal { animation: none !important; transition: none !important; }
}
```  
EFFECT: Уменьшит нагрузку на процессор и улучшит UX для пользователей, избегающих анимаций, соответствуя WCAG 2.1.  
RISK: Анимации могут быть частью брендинга; их отключение может слегка изменить визуальное восприятие.  
ROLLBACK: Удалить добавленный блок CSS (`git checkout -- index.html`).  
VERIFY: В Chrome DevTools → Rendering → Emulate CSS media `prefers-reduced-motion` и убедиться, что элементы с классом `.reveal` больше не анимируются.  
PRIORITY: 2 – небольшое изменение, повышает доступность без риска для конверсии.  

IDEA: Внедрить базовый Content Security Policy (CSP) через `<meta>`‑тег для защиты от XSS  
KNOB: в `<head>` добавить  
```html
<meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://fonts.gstatic.com; font-src https://fonts.gstatic.com; img-src data:; connect-src 'self'">
```  
EFFECT: Ограничит загрузку внешних скриптов и стилей, повышая безопасность сайта без необходимости серверных настроек.  
RISK: Если в дальнейшем будут добавлены внешние скрипты/ресурсы, они могут быть заблокированы; потребуется обновление CSP.  
ROLLBACK: Удалить мета‑тег (`git checkout -- index.html`).  
VERIFY: Открыть страницу, открыть DevTools → Console, убедиться, что нет CSP‑ошибок; проверить, что все стили и шрифты работают.  
PRIORITY: 3 – повышает безопасность, но требует внимательного тестирования, поэтому отложить после базовых улучшений доступности.
