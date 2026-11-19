# localhost:8080/ovh/gpt-oss-120b  2026-11-17 05:19:46
duration=27.0 error=- attempts=1

IDEA: Добавить канонический URL в <head>  
KNOB: В `<head>` вставить `<link rel="canonical" href="https://saveliy.ru/">` сразу после существующих `<meta>`‑тегов.  
EFFECT: Укрепит SEO‑сигналы, избавит от дублирования URL и поможет поисковикам правильно индексировать страницу.  
RISK: Никакого, если URL совпадает с текущим доменом.  
ROLLBACK: `git checkout index.html` (или удалить строку).  
VERIFY: Открыть страницу, открыть DevTools → Elements, убедиться в наличии тега; в Search Console проверить отсутствие ошибок «duplicate content».  
PRIORITY: 1 – канонический URL критичен для SEO и не требует изменений в дизайне.  

IDEA: «Skip‑to‑content» ссылка для доступности  
KNOB: Сразу после открывающего `<body>` добавить  
```html
<a href="#main" class="skip-link">Перейти к основному содержимому</a>
```  
и в CSS  
```css
.skip-link{position:absolute;top:-40px;left:0;background:#fff;color:#000;padding:8px;z-index:100;transition:top .3s;}
.skip-link:focus{top:0;}
```  
Также добавить `id="main"` к элементу `<main>` (если его нет).  
EFFECT: Улучшит навигацию клавиатурой и скрин‑ридерами, повышая показатель доступности (WCAG 2.1 AA).  
RISK: Небольшой риск визуального смещения, если уже есть элемент с `id="main"` – тогда использовать уникальный ID.  
ROLLBACK: Удалить добавленные строки и вернуть оригинальный `<body>` (git checkout).  
VERIFY: Включить режим имитации клавиатуры (Tab) в DevTools, нажать Shift+Tab до появления ссылки, нажать Enter – фокус должен перейти к основному контенту.  
PRIORITY: 1 – доступность – обязательный критерий, быстрый выигрыш без влияния на дизайн.  

IDEA: Учитывать предпочтения «reduce motion» для анимаций блобов в hero  
KNOB: В CSS добавить медиазапрос  
```css
@media (prefers-reduced-motion: reduce) {
  .hero .blob{animation:none;}
}
```  
(заменить `animation` на текущий ключевой фрейм, если используется).  
EFFECT: Пользователи, запросившие уменьшение анимаций, увидят статичную версию, уменьшая дискомфорт и потенциальный «motion‑sickness».  
RISK: Анимация может стать полностью отключена, но это не ухудшит восприятие сообщения.  
ROLLBACK: Удалить медиазапрос из CSS (git checkout index.html).  
VERIFY: В Chrome DevTools включить «Reduce motion» в Settings → Accessibility, перезагрузить страницу, убедиться, что блобы больше не анимируются.  
PRIORITY: 2 – важно для доступности, но менее критично, чем SEO‑элементы.  

IDEA: Добавить FAQ‑разметку JSON‑LD для улучшения сниппетов в поиске  
KNOB: В конец `<body>` вставить скрипт  
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Сколько времени занимает создание сайта?",
      "acceptedAnswer": {"@type": "Answer","text":"Сайт готов за 2 дня – от идеи до публикации."}
    },
    {
      "@type": "Question",
      "name": "Нужен ли мне технический специалист для поддержки?",
      "acceptedAnswer": {"@type": "Answer","text":"После запуска вы получаете инструкцию и возможность вносить правки самостоятельно."}
    },
    {
      "@type": "Question",
      "name": "Какие гарантии вы даете?",
      "acceptedAnswer": {"@type": "Answer","text":"Если сайт не будет виден в Яндексе после 30 дней, делаем правки бесплатно."}
    }
  ]
}
</script>
```  
EFFECT: Поисковые системы могут вывести расширенный блок FAQ под результатом, повышая CTR и привлекая целевой трафик.  
RISK: Требует точного соответствия реальному содержимому FAQ; если вопросы изменятся – потребуется обновление.  
ROLLBACK: Удалить скрипт (git checkout index.html).  
VERIFY: В Google Search Console → Rich Results Test вставить URL или HTML‑код и убедиться в отсутствии ошибок.  
PRIORITY: 2 – SEO‑выгода заметна, но требует согласования текста вопросов/ответов с владельцем.  

IDEA: Предзагрузка соединений к Google Fonts для ускорения рендеринга текста  
KNOB: В `<head>` добавить две строки перед загрузкой шрифтов:  
```html
<link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```  
EFFECT: Сократит время установления TLS‑соединения, ускорит загрузку шрифтов и уменьшит First Contentful Paint.  
RISK: Никакого; если браузер не поддерживает `preconnect`, он будет проигнорирован.  
ROLLBACK: Удалить добавленные строки (git checkout index.html).  
VERIFY: Открыть DevTools → Network, включить throttling (“Slow 3G”), перезагрузить страницу; сравнить время `fonts.googleapis.com` запроса до и после (должно появиться как “preconnect” со статусом (0 ms)).  
PRIORITY: 2 – быстрое улучшение скорости без визуального воздействия.
