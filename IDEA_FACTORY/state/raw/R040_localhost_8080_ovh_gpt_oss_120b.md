# localhost:8080/ovh/gpt-oss-120b  2026-11-17 03:35:35
duration=58.4 error=- attempts=1

IDEA: Добавить атрибут `lang="ru"` к `<html>`
KNOB: В открывающий тег `<html>` добавить `lang="ru"` (пример: `<html lang="ru">`)
EFFECT: Улучшит SEO (поиск по языку) и доступность (скрин‑ридеры правильно объявят язык)
RISK: Никакого, единственное требование — убедиться, что весь контент действительно на русском
ROLLBACK: `git checkout -- index.html` (или удалить атрибут вручную)
VERIFY: Открыть страницу в Chrome DevTools → Elements, убедиться, что `<html lang="ru">` присутствует; проверить в Lighthouse → SEO → “Document has a valid language attribute”
PRIORITY: 1 – быстрый, безопасный апдейт, сразу повышает SEO и a11y

IDEA: Добавить ARIA‑роль `banner` к шапке и `contentinfo` к футеру
KNOB: В элемент `<header class="hero" …>` добавить `role="banner"`; в блок футера (если есть) добавить `role="contentinfo"`
EFFECT: Явно обозначит структурные области для вспомогательных технологий, повышая доступность
RISK: Никакого, роли совместимы с HTML5‑семантикой
ROLLBACK: Удалить добавленные атрибуты
VERIFY: В DevTools → Accessibility, проверить, что “Banner” и “Content info” отображаются в дереве
PRIORITY: 1 – небольшое изменение, сразу улучшает навигацию скрин‑ридеров

IDEA: Предзагрузка (preload) основного CSS‑файла
KNOB: В `<head>` добавить `<link rel="preload" href="styles.css" as="style" onload="this.rel='stylesheet'">` (заменить `styles.css` на реальное имя) и оставить оригинальный `<link rel="stylesheet">` как fallback
EFFECT: Уменьшит время первого рендера, снизит блокирующий CSS
RISK: Если указать неверный путь – стили не загрузятся; требуется проверка пути
ROLLBACK: Удалить добавленную строку `<link rel="preload">`
VERIFY: В Chrome → Network убедиться, что файл загружается с типом “style” и без задержки; в Lighthouse → Performance проверить снижение “Render‑blocking resources”
PRIORITY: 1 – значительный выигрыш в скорости за минимум усилий

IDEA: Добавить `font-display: swap` в @font-face для Manrope
KNOB: Внутри `<style>` или отдельного CSS‑файла объявить:
```css
@font-face{
  font-family:'Manrope';
  src:url('https://fonts.gstatic.com/s/manrope/v13/... .woff2') format('woff2');
  font-weight:400 500 600 700;
  font-display:swap;
}
```
(заменить URL на тот, который уже используется)
EFFECT: Уменьшит FOIT (flash of invisible text), ускорит визуальное отображение текста
RISK: Нужно точно скопировать URL‑адреса шрифтов; ошибочный URL → шрифт не загрузится
ROLLBACK: Удалить объявление @font-face или вернуть оригинальный `<link>` к Google Fonts
VERIFY: Открыть страницу, включить “Disable cache” и посмотреть, что текст появляется сразу (нет пустого пространства); проверить в Lighthouse → Performance → “Avoid invisible text”
PRIORITY: 2 – улучшает восприятие без риска, но требует точного копирования URL

IDEA: Отключать анимацию при `prefers-reduced-motion`
KNOB: В конец `<style>` добавить:
```css
@media (prefers-reduced-motion: reduce){
  .particles, .reveal, .magnetic{animation:none!important;transition:none!important}
}
```
EFFECT: Уважает предпочтения пользователей с ограниченными возможностями, улучшает доступность и снижает нагрузку на CPU
RISK: Пользователи без предпочтения могут не заметить изменения; проверка нужна
ROLLBACK: Удалить блок `@media` из CSS
VERIFY: В Chrome DevTools → Rendering включить “Emulate CSS prefers-reduced-motion” и убедиться, что анимации исчезают
PRIORITY: 2 – отвечает требованиям WCAG 2.1, небольшая правка

IDEA: Добавить JSON‑LD схему `Service` для описания услуги «лендинг за 2 дня»
KNOB: В конец `<body>` вставить `<script type="application/ld+json">` с:
```json
{
  "@context":"https://schema.org",
  "@type":"Service",
  "serviceType":"Создание лендингов за 2 дня",
  "provider":{"@type":"LocalBusiness","name":"Савелий","address":{"@type":"PostalAddress","addressLocality":"Пермь"}},
  "areaServed":"Пермь",
  "offers":{"@type":"Offer","priceCurrency":"RUB","price":"0","url":"#contact","availability":"https://schema.org/InStock"}
}
```
EFFECT: Расширит семантику для поисковиков, может появиться в Rich Results (Service)
RISK: Требует точного соответствия реальному предложению; если цена меняется – нужно обновлять
ROLLBACK: Удалить скрипт из HTML
VERIFY: В Google Rich Results Test ввести URL, убедиться, что схема распознаётся без ошибок
PRIORITY: 2 – повышает SEO‑видимость, но требует поддержания актуальности

IDEA: Добавить `rel="noopener noreferrer"` к внешним ссылкам (Telegram)
KNOB: В `<a class="btn-primary magnetic" href="#contact">` и в любой другой внешней ссылке (например, `href="https://t.me/..."`) добавить `rel="noopener noreferrer"`
EFFECT: Повышает безопасность (защита от reverse tabnabbing) и небольшое улучшение SEO за счёт чистых атрибутов
RISK: Никакого
ROLLBACK: Удалить атрибут `rel`
VERIFY: В DevTools → Elements проверить наличие атрибута; в консоли `document.querySelectorAll('a[rel="noopener noreferrer"]').length` > 0
PRIORITY: 3 – небольшая правка, но хорошая практика

IDEA: Добавить `aria-label` к главной CTA‑кнопке в hero
KNOB: В элемент `<a class="btn-primary magnetic" href="#contact">…</a>` добавить `aria-label="Получить бесплатное демо‑макет в Telegram"`
EFFECT: Явно описывает действие для скрин‑ридеров, повышает конверсию у пользователей с ограниченными возможностями
RISK: Нужно обеспечить, чтобы текст метки точно соответствовал действию
ROLLBACK: Удалить атрибут `aria-label`
VERIFY: В DevTools → Accessibility, убедиться, что у ссылки есть “Accessible name: Получить бесплатное демо‑макет в Telegram”
PRIORITY: 2 – улучшает доступность без визуального изменения

IDEA: Добавить мета‑тег `robots` с `index, follow`
KNOB: В `<head>` после остальных `<meta>` вставить `<meta name="robots" content="index, follow">`
EFFECT: Явно указывает поисковикам индексировать страницу и следовать по ссылкам, устраняя возможные дефолтные ограничения
RISK: Если владелец хочет ограничить индексацию – потребуется изменить
ROLLBACK: Удалить тег
VERIFY: В View Source убедиться в наличии; в Google Search Console → URL Inspection увидеть статус “Indexed”
PRIORITY: 3 – небольшая SEO‑оптимизация, но полезна

IDEA: Увеличить минимальный размер тап‑цели для мобильного CTA до 48 px
KNOB: В CSS для `.btn-primary` (и `.sticky-cta .btn-primary`) добавить `min-height:48px; min-width:48px; line-height:1.2;`
EFFECT: Соответствует рекомендациям WCAG 2.1 (минимальный размер интерактивного элемента), улучшает конверсию на мобильных
RISK: Может слегка изменить визуальный дизайн; потребуется проверить, что кнопка не выглядит «растянутой»
ROLLBACK: Удалить добавленные `min-height/min-width` свойства
VERIFY: В Chrome DevTools → Device Toolbar, включить “Emulate touch screen”, навести курсор – должно быть минимум 48 px по обеим осям
PRIORITY: 2 – важный аспект мобильной доступности, простая правка.
