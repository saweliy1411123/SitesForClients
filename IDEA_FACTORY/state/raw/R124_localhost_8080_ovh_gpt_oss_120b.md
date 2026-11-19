# localhost:8080/ovh/gpt-oss-120b  2026-11-17 07:42:45
duration=32.2 error=- attempts=1

IDEA: Добавить атрибут `lang="ru"` на `<html>`
KNOB: В начале файла изменить `<html>` → `<html lang="ru">`
EFFECT: Ускорит индексацию русскоязычного контента, улучшит доступность скрин‑ридеров и SEO‑сигналы о языке.
RISK: Никакого, кроме необходимости убедиться, что страница действительно русская.
ROLLBACK: `git checkout -- index.html` (или вернуть из копии)
VERIFY: Открыть страницу, открыть DevTools → Elements, проверить наличие `lang="ru"`; запустить Lighthouse → Accessibility → Language.
PRIORITY: 1 – простое изменение, мгновенный SEO‑эффект.

IDEA: Вставить «skip‑to‑content» ссылку для клавиатурных пользователей
KNOB: Сразу после открывающего `<body>` добавить  
```html
<a href="#main" class="skip-link">Перейти к содержимому</a>
```  
и добавить `id="main"` к первому крупному контейнеру (например, `<section id="hero" …>`). Стилизовать `.skip-link{position:absolute;left:-9999px;top:auto;}` и `:focus{left:0;z-index:1000;}`.
EFFECT: Улучшит доступность, сократит количество кликов для пользователей клавиатуры, повышая показатель Core Web Vitals (First Input Delay).
RISK: Требует небольшого изменения HTML‑структуры; может конфликтовать с текущим CSS, если уже есть глобальные `a`‑правила.
ROLLBACK: Удалить строки и вернуть оригинальный `<section>` без `id`.
VERIFY: Перейти в Chrome, включить табуляцию, убедиться, что первая таб‑нажатие фокусирует ссылку и скроллит к контенту; проверить Lighthouse → Accessibility → Skip navigation link.
PRIORITY: 2 – небольшая работа, но существенный выигрыш в a11y.

IDEA: Добавить канонический `<link rel="canonical">`
KNOB: В `<head>` после существующих `<meta>` добавить  
```html
<link rel="canonical" href="https://saveliy-perm.ru/">
```  
(заменить URL на реальный домен).
EFFECT: Уменьшит риск дублирования контента, передаст «сокровенное» SEO‑вес к основной версии, полезно при возможных копиях в разных каталогах.
RISK: Нужно убедиться, что указанный URL действительно является окончательной публичной копией.
ROLLBACK: Удалить строку из `<head>`.
VERIFY: Открыть страницу, посмотреть source → убедиться в наличии тега; проверить в Search Console → URL Inspection → Canonical URL.
PRIORITY: 2 – простое изменение, прямой SEO‑эффект.

IDEA: Добавить файл `robots.txt` и `<meta name="robots">`
KNOB: Создать в корне проекта файл `robots.txt` с содержимым  
```
User-agent: *
Allow: /
Sitemap: https://saveliy-perm.ru/sitemap.xml
```  
и в `<head>` добавить  
```html
<meta name="robots" content="index, follow">
```
EFFECT: Явно укажет поисковикам, что страница должна индексироваться, и предоставит путь к карте сайта (можно позже добавить `sitemap.xml`). Улучшит crawl‑ability.
RISK: Если в дальнейшем появятся закрытые разделы, их придётся добавить в `robots.txt`.
ROLLBACK: Удалить файл и мета‑тег.
VERIFY: Ввести `https://saveliy-perm.ru/robots.txt` в браузер – увидеть содержимое; в Search Console → Robots.txt Tester проверить отсутствие ошибок.
PRIORITY: 3 – полезно, но менее критично, чем прямые UI‑улучшения.

IDEA: Внедрить JSON‑LD `LocalBusiness` schema
KNOB: В конец `<head>` вставить скрипт  
```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"LocalBusiness",
  "name":"Савелий — лендинги для бизнеса в Перми",
  "url":"https://saveliy-perm.ru/",
  "logo":"https://saveliy-perm.ru/assets/logo.svg",
  "image":"https://saveliy-perm.ru/assets/hero.jpg",
  "telephone":"+7 (3412) 345‑678",
  "address":{
    "@type":"PostalAddress",
    "streetAddress":"ул. Пушкина, 10",
    "addressLocality":"Пермь",
    "postalCode":"614000",
    "addressCountry":"RU"
  },
  "priceRange":"₽₽",
  "openingHours":"Mo-Fr 09:00-18:00",
  "sameAs":[
    "https://t.me/saveliy",
    "https://vk.com/saveliy"
  ]
}
</script>
```
(корректировать данные под реальный бизнес).
EFFECT: Увеличит видимость в локальном поиске Яндекса и Google, позволит выводить «карточку организации» в SERP, повысит доверие пользователей.
RISK: Требует точных контактных данных; неверные данные могут вызвать штрафы со стороны поисковиков.
ROLLBACK: Удалить скрипт из `<head>`.
VERIFY: Проверить в Google Rich Results Test (https://search.google.com/test/rich-results) – увидеть валидный LocalBusiness.
PRIORITY: 1 – сильный локальный SEO‑эффект при минимальном риске.

IDEA: Инлайн‑критический CSS для «hero»‑секции
KNOB: Выделить из `styles.css` (или `<style>`) правила, отвечающие за `.hero`, `.hero .wrap`, `.hero h1`, `.hero p.sub`, `.hero .cta-row` и поместить их в `<style>`‑блок сразу после `<head>` открывающего тега, оставив остальные стили в отдельном файле, подключённом с `rel="preload"` + `as="style"` (как в I-00750). Удалить дублирование этих правил из внешнего файла.
EFFECT: Уменьшит время до первого рендеринга (LCP), так как браузер получит стили для верхней части без дополнительного запроса, улучшит Core Web Vitals → потенциальный рост конверсий.
RISK: Возможна небольшая загрузка HTML‑файла (≈ 5 KB), но это компенсируется ускорением рендеринга; нужно следить за тем, чтобы не забыть синхронизацию при будущих изменениях CSS.
ROLLBACK: Откатить файл `index.html` к коммиту 00af311 (git checkout -- index.html) или удалить инлайн‑блок и вернуть внешнюю ссылку.
VERIFY: Запустить Lighthouse → Performance → First Contentful Paint / Largest Contentful Paint; сравнить с базовым результатом (до изменения). Также проверить, что стили не дублируются (Inspect → Sources).
PRIORITY: 2 – требует небольшого редактирования, но приносит измеримый выигрыш в скорости.
