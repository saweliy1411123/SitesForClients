# localhost:8080/ovh/gpt-oss-120b  2026-11-17 06:22:12
duration=42.0 error=- attempts=1

IDEA: Добавить атрибут языка `lang="ru"` к корневому элементу  
KNOB: В файле `index.html` заменить открывающий тег `<html>` на `<html lang="ru">`  
EFFECT: Явно указывает язык страницы — повышает локальное SEO и помогает скрин‑ридерам правильно озвучивать контент  
RISK: Минимальный; может сломать скрипты, которые ищут точный строку `<html>` (маловероятно)  
ROLLBACK: `git checkout -- index.html` (или удалить добавленный атрибут)  
VERIFY: Открыть исходный код в браузере, убедиться в наличии `lang="ru"`; запустить Lighthouse → SEO, проверить, что в "Language" указано `ru`  
PRIORITY: 1 — высокий эффект при почти нулевых затратах  

IDEA: Вставить «skip‑link» для быстрой навигации клавиатурой  
KNOB: Сразу после `<body>` добавить  
```html
<a href="#main" class="skip-link">Перейти к содержимому</a>
```  
и в CSS добавить (скрыто по‑умолчанию, видно при focus)  
```css
/* SAFE CSS */
.skip-link{
  position:absolute;
  top:-40px;
  left:0;
  background:#fff;
  color:#000;
  padding:8px 12px;
  z-index:1000;
}
.skip-link:focus{
  top:0;
}
```  
EFFECT: Пользователи, перемещающиеся по Tab, могут сразу перейти к основному контенту, улучшая WCAG 2.1 AA и UX  
RISK: Возможен визуальный рывок, если стили не скрывают ссылку корректно  
ROLLBACK: Удалить строку‑ссылку и соответствующий CSS‑блок  
VERIFY: Открыть страницу, нажать Tab — первая фокусировка должна попасть на «skip‑link», после её активации фокус переходит к элементу с `id="main"` (добавьте `<main id="main">` если ещё нет)  
PRIORITY: 2 — небольшие изменения, значительный прирост доступности  

IDEA: Отключать анимации при запросе `prefers-reduced-motion`  
KNOB: В конец CSS‑файла добавить  
```css
/* SAFE CSS */
@media (prefers-reduced-motion: reduce) {
  .hero .blob,
  .btn-primary .arr,
  .price-card:hover,
  .price-card:focus {
    animation: none !important;
    transition: none !important;
  }
}
```  
EFFECT: Пользователи, включившие «Reduced motion», не увидят потенциально вызывающие дискомфорт анимаций, повышая доступность  
RISK: Потеря визуального «блеска» для части аудитории, но функциональность сохраняется  
ROLLBACK: Удалить добавленный медиазапрос  
VERIFY: В Chrome DevTools включить «Emulate CSS prefers‑reduced‑motion» и убедиться, что анимации (blobs, hover‑стрелки) перестали работать  
PRIORITY: 2 — важный accessibility‑шаг, реализуется одной строкой CSS  

IDEA: Предварительно установить соединения `preconnect` к CDN‑шрифтам  
KNOB: В `<head>` перед загрузкой Google‑Fonts добавить  
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```  
EFFECT: Уменьшает время DNS‑lookup и TLS‑handshake, ускоряя загрузку шрифтов и улучшая LCP‑метрику  
RISK: Нет — браузер просто игнорирует, если не поддерживает `preconnect`  
ROLLBACK: Удалить две строки `<link rel="preconnect"...>`  
VERIFY: Запустить Lighthouse → Performance, убедиться, что в разделе “Preconnect to required origins” указаны оба домена; в сети DevTools увидеть раннее открытие соединения  
PRIORITY: 2 — быстрый выигрыш в скорости без риска  

IDEA: Добавить JSON‑LD‑разметку FAQPage для секции вопросов‑ответов  
KNOB: Перед закрывающим `</head>` вставить  
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Как быстро будет готов сайт?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Сайт будет готов в течение 2‑ух рабочих дней после уточнения требований."
      }
    },
    {
      "@type": "Question",
      "name": "Сколько стоит разработка?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Стоимость фиксирована – 12 000 ₽, без скрытых доплат."
      }
    }
    /* добавить остальные вопросы из секции FAQ -->
  ]
}
</script>
```  
(скопировать реальные вопросы/ответы из текущей разметки FAQ)  
EFFECT: Позволяет поисковикам выводить расширенные сниппеты «Вопрос‑Ответ», повышая CTR и видимость в поиске  
RISK: Нужно поддерживать актуальность данных; несоответствие может привести к ошибкам в Rich Results Test  
ROLLBACK: Удалить весь `<script type="application/ld+json">` блок  
VERIFY: В Google Rich Results Test ввести URL или скопировать HTML‑фрагмент; убедиться, что схема проходит без ошибок  
PRIORITY: 2 — умеренный объём работы, но потенциально повышает органический трафик
