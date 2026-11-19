# localhost:8081/big_only  2026-11-17 09:21:32
duration=56.7 error=- attempts=1

IDEA: Preconnect к Google Fonts для ускорения загрузки шрифтов  
KNOB: В `<head>` добавить перед существующей ссылкой на шрифты две строки: `<link rel="preconnect" href="https://fonts.googleapis.com">` и `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>`  
EFFECT: Сокращает время DNS‑lookup и TLS‑handshake, ускоряя загрузку шрифтов → лучше LCP и FCP  
RISK: Минимальный — при невозможности preconnect браузер выполнит обычный запрос без ухудшения функционала  
ROLLBACK: `git checkout index.html` или удалить только только что добавленные две строки `<link rel="preconnect">`  
VERIFY: В DevTools → Network → filter fonts, сравнить время первого запроса до и после изменения (ожидаем снижение ≈30‑50 мс)  
PRIORITY: 2 — быстрый выигрыш в скорости при почти нулевом риске  

IDEA: Добавить OG‑изображение для соцсетей  
KNOB: В `<head>` после остальных OG‑тегов вставить `<meta property="og:image" content="https://example.com/assets/og-image.jpg">` (заменить URL на реальное изображение)  
EFFECT: При публикации ссылки в соцсетях появляется превью‑картинка, повышая CTR и бренд‑узнаваемость  
RISK: Требуется наличие доступного изображения; если ссылка битая, превью не отобразится  
ROLLBACK: Удалить только добавленную строку `<meta property="og:image">`  
VERIFY: Запустить Facebook Sharing Debugger или Twitter Card validator; в результатах должна появиться картинка  
PRIORITY: 2 — небольшие усилия, заметный SEO/соц‑эффект  

IDEA: JSON‑LD разметка FAQPage для схемы вопросов‑ответов  
KNOB: После секции FAQ (см. SITE_REQUEST «faq») добавить скрипт `<script type="application/ld+json">` с массивом объектов `{ "@type":"Question","name":"...", "acceptedAnswer":{ "@type":"Answer","text":"..." } }`, основываясь на текущих `<h3>`/параграфах FAQ  
EFFECT: Позволяет поисковикам выводить rich‑snippet «Вопросы и ответы», повышая видимость и CTR в SERP  
RISK: Требует синхронизации JSON‑LD с реальным контентом; устаревшие данные могут вводить в заблуждение  
ROLLBACK: Удалить весь `<script type="application/ld+json">` блок  
VERIFY: Запустить Google Rich Results Test на странице; должна отобразиться разметка FAQPage без ошибок  
PRIORITY: 1 — высокий SEO‑выигрыш, небольшие изменения  

IDEA: Добавить ARIA‑роль «contentinfo» к подвалу для лучшей навигации скрин‑ридеров  
KNOB: Найти элемент `<footer>` (или обернуть финальный CTA в `<footer>`) и добавить атрибут `role="contentinfo"`  
EFFECT: Явно обозначает область подвала, упрощая ориентирование пользователей вспомогательных технологий  
RISK: Отсутствует; изменение только атрибута  
ROLLBACK: Удалить атрибут `role="contentinfo"`  
VERIFY: Включить Chrome Accessibility pane или axe‑core; подвал должен быть помечен как «content info»  
PRIORITY: 1 — важный шаг в доступности, риск‑ноль  

IDEA: Указать роль кнопки и ARIA‑метку для финального CTA‑ссылка  
KNOB: В секции `.final` (см. SITE_REQUEST «final») найти CTA‑ссылку `<a …>` и добавить `role="button"` и `aria-label="Заказать бесплатное демо"` (или текст CTA)  
EFFECT: Делает интерактивный элемент более понятным для скрин‑ридеров и клавиатурных пользователей, повышая доступность и конверсию  
RISK: Нет функциональных конфликтов; единственное – необходимо корректно сформулировать метку  
ROLLBACK: Удалить добавленные атрибуты `role` и `aria-label`  
VERIFY: Включить Chrome Accessibility tree или протестировать в NVDA/VoiceOver; элемент объявится как «button» с указанной меткой  
PRIORITY: 1 — критически важный для a11y, простая правка.
