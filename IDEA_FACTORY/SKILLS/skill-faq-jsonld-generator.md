---
name: SKILL — faq-jsonld-generator
source: localhost:8080/ovh/gpt-oss-120b
round: 132
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — faq-jsonld-generator

**Name:** faq-jsonld-generator
**When to apply:** На любой лендинг с секцией FAQ, где вопросы/ответы размечены в виде `<div class="faq-item">` (или `<details>`/`<summary>`).
**Steps:**
1. Добавить в конец `<body>` скрипт, который собирает все элементы FAQ, извлекает вопрос из `<h3>`/`<summary>` и ответ из последующего `<p>`/`<div>`.
2. Сформировать массив объектов `{question, answer}` и вставить в `<script type="application/ld+json">` согласно схеме `FAQPage`.
3. Поместить скрипт в `<head>` перед закрывающим `</head>` для раннего парсинга поисковыми ботами.
**SAFE CSS:** *(не требуется)*
**SAFE JS:**
```js
(function(){
const faqItems = document.querySelectorAll('.faq-item, .faq > div');
const faqs = [];
faqItems.forEach(item=>{
const q = item.querySelector('h3, summary');
const a = item.querySelector('p, .answer, div:not(:first-child)');
if(q && a){
faqs.push({question:q.textContent.trim(),answer:a.textContent.trim()});
}
});
if(faqs.length){
const script = document.createElement('script');
script.type = 'application/ld+json';
script.text = JSON.stringify({
"@context":"https://schema.org",
"@type":"FAQPage",
"mainEntity":faqs.map(f=>({"@type":"Question","name":f.question,"acceptedAnswer":{"@type":"Answer","text":f.answer}}))
});
document.head.appendChild(script);
}
})();
```

## Когда применять
Автоматическое добавление структурированных данных FAQPage повышает шансы появления в «People also ask» и улучшает SEO‑видимость без ручного редактирования JSON‑LD.

## Проверка
Запустить Google Rich Results Test (https://search.google.com/test/rich-results) по локальному файлу или через сервер; убедиться, что найдено `FAQPage` со всеми вопросами.

## SAFE CSS
```css
** *(не требуется)*
**SAFE JS:**
```js
(function(){
const faqItems = document.querySelectorAll('.faq-item, .faq > div');
const faqs = [];
faqItems.forEach(item=>{
const q = item.querySelector('h3, summary');
const a = item.querySelector('p, .answer, div:not(:first-child)');
if(q && a){
faqs.push({question:q.textContent.trim(),answer:a.textContent.trim()});
}
});
if(faqs.length){
const script = document.createElement('script');
script.type = 'application/ld+json';
script.text = JSON.stringify({
"@context":"https://schema.org",
"@type":"FAQPage",
"mainEntity":faqs.map(f=>({"@type":"Question","name":f.question,"acceptedAnswer":{"@type":"Answer","text":f.answer}}))
});
document.head.appendChild(script);
}
})();
```
```
