# localhost:8080/ovh/gpt-oss-120b  2026-11-17 03:12:43
duration=41.7 error=- attempts=1

IDEA: Hero — Блок‑плюс‑плюс: три быстрых выгоды с иконками  
KNOB: В секцию `<header class="hero">` добавить под `.sub` список `<ul class="hero-benefits"><li>⚡ Быстрая загрузка (< 1 с)</li><li>📈 Топ‑3 в Яндексе за 2 дня</li><li>📱 Полностью адаптивный</li></ul>` и в CSS задать стили `ul.hero‑benefits{display:flex;gap:1rem;justify-content:center;margin-top:1rem}ul.hero‑benefits li{display:flex;align-items:center;font-size:clamp(14px,1.2vw,16px);color:#c3cad9}`  
EFFECT: Мгновенно усиливает восприятие ценности, повышает конверсию за счёт визуального подкрепления оффера.  
RISK: Небольшой рост HTML‑размера (≈200 Б).  
ROLLBACK: `git checkout -- index.html` (или удалить добавленные строки).  
VERIFY: Открыть страницу в браузере, убедиться, что список отображается под подзаголовком и выглядит одинаково на мобильных/десктопных ширинах.  
PRIORITY: 1 — прямое усиление первого экрана, низкая стоимость.

IDEA: Боль — SVG‑иллюстрация «Нет результатов в поиске»  
KNOB: В секцию боли (после заголовка «Запись есть — клиентов из поиска нет») вставить `<svg class="no-results-ill" aria-hidden="true" width="120" height="120" viewBox="0 0 24 24"><path fill="none" stroke="#c3cad9" d="M2 2l20 20M2 22l20-20"/></svg>` и в CSS добавить `.no-results-ill{margin:1rem auto;display:block;opacity:.4}`  
EFFECT: Делает проблему более осязаемой, улучшает визуальное восприятие боли, повышает время на странице.  
RISK: Возможный конфликт с темой, если SVG‑цвет не контрастирует; решаемо правкой цвета.  
ROLLBACK: Удалить вставленный `<svg>` и CSS‑правило.  
VERIFY: Включить DevTools → Elements, убедиться, что SVG виден и не влияет на читаемость текста.  
PRIORITY: 2 — улучшает эмоциональное воздействие без технических сложностей.

IDEA: Шаги — Scroll‑triggered progress bar над секцией «Три шага»  
KNOB: Над `<section class="steps">` добавить `<div class="steps-progress" aria-hidden="true"><div class="progress-bar"></div></div>`; в CSS:  

```css
.steps-progress{position:relative;height:4px;background:#2d2d3a;margin-bottom:1rem}
.progress-bar{width:0;height:100%;background:#8b5cf6;transition:width .3s ease}
```

и в JS (в конце `<body>`):  

```js
const bar=document.querySelector('.progress-bar')
const steps=document.querySelector('.steps')
window.addEventListener('scroll',()=>{ 
  const rect=steps.getBoundingClientRect()
  const total=window.innerHeight+rect.height
  const scrolled=Math.min(Math.max(window.innerHeight-rect.top,0),total)
  bar.style.width=`${(scrolled/total)*100}%`
})
```  

EFFECT: Пользователь визуально видит, как продвигается к «Трём шагам», усиливая вовлечённость и удержание.  
RISK: Требует небольшого JS; может конфликтовать с другими скролл‑слушателями (проверить).  
ROLLBACK: Удалить добавленные HTML‑ и CSS‑блоки и скрипт.  
VERIFY: Прокрутить страницу, наблюдать плавный рост полосы от 0 % до 100 % при достижении конца секции.  
PRIORITY: 2 — модернизирует UI, но требует теста совместимости.

IDEA: Демо — PDF‑кейс‑стади «Смотрите результат»  
KNOB: В секцию «Демо‑концепты» после каждого блока добавить кнопку‑ссылку `<a href="case-study.pdf" class="demo-pdf" download>Скачать PDF‑кейс</a>` и в CSS `.demo-pdf{display:inline-block;margin-top:.5rem;color:#8b5cf6;text-decoration:underline;}`  
EFFECT: Позволяет потенциальным клиентам подробно изучить результаты офлайн, повышая доверие и вероятность заявки.  
RISK: Нужно предоставить PDF‑файл; отсутствие файла приведёт к 404‑ошибке.  
ROLLBACK: Удалить ссылки и стили.  
VERIFY: Кликнуть по ссылке, убедиться, что файл скачивается (или открывается).  
PRIORITY: 3 — добавляет ценность, но зависит от наличия готового PDF.

IDEA: Цена — Schema.org Offer JSON‑LD для цены  
KNOB: В конец `<body>` вставить  

```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"Offer",
  "url":"https://example.com/#contact",
  "priceCurrency":"RUB",
  "price":"19900",
  "availability":"https://schema.org/InStock",
  "itemOffered":{"@type":"Service","name":"Лендинг за 2 дня"}
}
</script>
```  

EFFECT: Улучшает поисковую выдачу (rich snippets), повышает CTR в поиске.  
RISK: Требует корректного URL и цены; неверные данные могут привести к штрафу поисковика.  
ROLLBACK: Удалить `<script>`‑блок.  
VERIFY: В Chrome DevTools → Structured Data Testing Tool, убедиться в валидности JSON‑LD.  
PRIORITY: 2 — SEO‑выгода без влияния на UX.

IDEA: FAQ — Клиентский поиск по вопросам  
KNOB: В начало секции FAQ добавить `<input type="search" class="faq-search" placeholder="Поиск по вопросам…" aria-label="Поиск по вопросам FAQ">` и небольшой скрипт в конце `<body>`:  

```js
document.querySelector('.faq-search').addEventListener('input',e=>{
  const term=e.target.value.toLowerCase()
  document.querySelectorAll('.faq-item').forEach(item=>{
    const q=item.querySelector('summary').textContent.toLowerCase()
    item.style.display = q.includes(term)||!term ? '' : 'none'
  })
})
```  

EFFECT: Позволяет пользователю быстро находить нужный ответ, повышает удовлетворённость и снижает отток.  
RISK: Требует небольшого JS; возможен конфликт со стилями `details`.  
ROLLBACK: Удалить `<input>` и скрипт.  
VERIFY: Ввести запрос в поле, убедиться, что вопросы фильтруются в реальном времени.  
PRIORITY: 3 — полезно, но мало влияет на конверсию без больших трафиков.

IDEA: Финальный CTA — Desktop‑sticky bottom bar (появляется после 60 % прокрутки)  
KNOB: В конец `<body>` добавить  

```html
<div class="sticky-cta-desktop" role="region" aria-label="Бесплатное демо">
  <a href="#contact" class="btn-primary">Получить демо бесплатно</a>
</div>
```  

CSS:  

```css
.sticky-cta-desktop{
  position:fixed;bottom:-80px;left:0;right:0;background:#111;padding:1rem;display:flex;justify-content:center;transition:bottom .4s ease;z-index:1000;
}
.sticky-cta-desktop.show{bottom:0}
```

JS (в конце `<body>`):  

```js
const bar=document.querySelector('.sticky-cta-desktop')
window.addEventListener('scroll',()=>{ 
  const scrollPerc = window.scrollY / (document.body.scrollHeight - window.innerHeight)
  bar.classList.toggle('show', scrollPerc > 0.6)
})
```  

EFFECT: Повторный, но контекстный CTA для десктоп‑посетителей, увеличивает шанс клика после ознакомления с контентом.  
RISK: Может восприниматься как навязчивая реклама, если анимация слишком резкая; можно настроить плавность.  
ROLLBACK: Удалить HTML‑блок, CSS‑правила и скрипт.  
VERIFY: Прокрутить страницу до 70 % высоты, убедиться, что бар плавно выезжает и ссылка работает.  
PRIORITY: 2 — добавляет дополнительный путь к конверсии без изменения существующего CTA.
