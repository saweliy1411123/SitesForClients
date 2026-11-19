# localhost:8080/ovh/gpt-oss-120b  2026-11-17 06:44:08
duration=41.2 error=- attempts=1

IDEA: Добавить канонический URL  
KNOB: В `<head>` вставить `<link rel="canonical" href="https://example.com/">` (заменить `example.com` на текущий домен)  
EFFECT: Укрепит ссылочный вес страницы, предотвратит дублирование контента в поисковых системах  
RISK: Если сайт будет доступен по нескольким доменам, необходимо убедиться, что канонический URL соответствует основной версии  
ROLLBACK: Удалить строку‑тег из `<head>` (git checkout HEAD -- index.html)  
VERIFY: Открыть DevTools → Elements, убедиться в наличии тега; выполнить `site:example.com` в поиске Google и проверить отсутствие дублирующихся результатов  
PRIORITY: 1 – низкий риск, высокий SEO‑эффект  

IDEA: Уважать предпочтения пользователей к анимированию  
KNOB: В `<style>` добавить медиазапрос `@media (prefers-reduced-motion: reduce) { .hero-blob, .hero-veil { animation: none !important; } }`  
EFFECT: Пользователи с включённым режимом «меньше движения» не будут испытывать раздражающие анимации, повышая доступность  
RISK: Отключение анимации может слегка изменить визуальный стиль, но это безопасно  
ROLLBACK: Удалить медиазапрос (git checkout HEAD -- index.html)  
VERIFY: Включить «Reduce motion» в настройках ОС/браузера, перезагрузить страницу, убедиться, что анимация исчезла (DevTools → Computed)  
PRIORITY: 2 – важно для a11y, но без влияния на конверсию  

IDEA: Прелоадить критические шрифты Manrope 600 и 700  
KNOB: В `<head>` после `preconnect` добавить:  
```html
<link rel="preload" href="https://fonts.gstatic.com/s/manrope/v13/..." as="font" type="font/woff2" crossorigin>
<link rel="preload" href="https://fonts.gstatic.com/s/manrope/v13/..." as="font" type="font/woff2" crossorigin>
```  
(подставить реальные URL‑ы весов 600 и 700)  
EFFECT: Уменьшит время до первого отображения текста в жирных стилях, улучшит LCP  
RISK: Небольшой рост первоначального трафика из‑за дополнительных запросов – незначительно  
ROLLBACK: Удалить два `<link rel="preload">` (git checkout HEAD -- index.html)  
VERIFY: В DevTools → Network включить «Disable cache», обновить страницу, убедиться, что запросы к шрифтам имеют статус 200 и тип font и что LCP улучшился (Lighthouse)  
PRIORITY: 1 – быстрый выигрыш в Core Web Vitals  

IDEA: Обернуть основной контент в семантический `<main>`  
KNOB: После закрывающего `</header>` (или сразу перед первым `<section>`) добавить `<main>` и закрыть его после последней контент‑секции перед `</footer>`  
EFFECT: Улучшит семантику страницы, облегчает навигацию скрин‑ридерам и повышает SEO‑оценку структуры  
RISK: Неправильное закрытие тега может нарушить разметку; требует внимательной проверки вложенности  
ROLLBACK: Удалить открывающий и закрывающий `<main>` (git checkout HEAD -- index.html)  
VERIFY: В DevTools → Elements увидеть один элемент `<main>` охватывающий все секции; протестировать Tab‑обход – фокус должен попадать внутрь `<main>` без пропусков  
PRIORITY: 1 – низкая стоимость, высокий семантический эффект  

IDEA: Добавить JSON‑LD Service‑schema для локального SEO  
KNOB: В `<head>` перед закрывающим `</head>` вставить:  
```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"Service",
  "serviceType":"Создание лендингов за 2 дня",
  "provider":{
    "@type":"LocalBusiness",
    "name":"Савелий",
    "address":{"@type":"PostalAddress","addressLocality":"Пермь","addressCountry":"RU"},
    "telephone":"+7‑999‑123‑45‑67",
    "url":"https://example.com/"
  },
  "areaServed":"Пермь"
}
</script>
```  
EFFECT: Укрепит локальную релевантность в поиске, появятся rich‑snippets в результатах Google — повышение CTR  
RISK: Требует точных контактных данных; если информация будет неточной, может привести к штрафу за недостоверную разметку  
ROLLBACK: Удалить `<script type="application/ld+json">` (git checkout HEAD -- index.html)  
VERIFY: В консоли Chrome выполнить `JSON.parse(document.querySelector('script[type="application/ld+json"]').innerHTML)` без ошибок; проверить в Google Rich Results Test → валидность  
PRIORITY: 2 – значимый SEO‑эффект, умеренный риск  

IDEA: Добавить мета‑теги Twitter Card для соцсетей  
KNOB: В `<head>` добавить:  
```html
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Савелий — лендинги для бизнеса в Перми | за 2 дня">
<meta name="twitter:description" content="Создаю быстрые лендинги, которые находят в Яндексе. Бесплатный демо‑макет.">
<meta name="twitter:image" content="https://example.com/assets/og-image.jpg">
```  
EFFECT: При публикации ссылки в Twitter будет отображаться крупный превью‑картинка, повышая кликабельность  
RISK: Нужно обеспечить доступность указанного изображения; отсутствие файла приведёт к пустому превью  
ROLLBACK: Удалить четыре `<meta>`‑тега (git checkout HEAD -- index.html)  
VERIFY: Ввести URL в https://cards-dev.twitter.com/validator и убедиться в корректном отображении карточки  
PRIORITY: 2 – мало усилий, улучшает соц‑трафик  

IDEA: Сделать подключаемый скрипт неблокирующим  
KNOB: В `<script src="...">` (единственный скрипт внизу страницы) добавить атрибут `defer` (или переместить в конец `<body>` и добавить `async` если скрипт не зависит от DOM)  
EFFECT: Уменьшит время блокировки рендеринга, ускорит первую отрисовку (LCP)  
RISK: Если скрипт использует элементы, которые ещё не загружены, может возникнуть ошибка – требует проверки совместимости  
ROLLBACK: Удалить атрибут `defer`/`async` (git checkout HEAD -- index.html)  
VERIFY: В DevTools → Network убедиться, что запрос к скрипту помечен как deferred; проверить отсутствие JS‑ошибок в консоли после перезагрузки  
PRIORITY: 1 – быстрый выигрыш в скорости, минимальный риск  

IDEA: Добавить CSS‑свойство `contain: layout` к тяжёлой hero‑секции  
KNOB: В `.hero` добавить `contain: layout;` (можно в уже существующий блок стилей)  
EFFECT: Ограничит влияние изменения размеров hero‑блока на остальную страницу, улучшит производительность при скролле и анимациях  
RISK: При некорректных вложенных позиций может нарушиться позиционирование – потребуется визуальная проверка  
ROLLBACK: Удалить `contain: layout;` из правила `.hero` (git checkout HEAD -- index.html)  
VERIFY: В DevTools → Computed увидеть `contain: layout`; измерить FPS скролла (DevTools → Performance) до и после, ожидая небольшое улучшение  
PRIORITY: 3 – не критично, но полезно для микропроизводительности.
