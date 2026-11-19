---
name: SKILL — CSS‑Only FAQ Accordion (styled details/summary)
source: localhost:8080/ovh/gpt-oss-120b
round: 14
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — CSS‑Only FAQ Accordion (styled details/summary)

METHOD: Преобразуйте каждый вопрос‑ответ в `<details class="faq-item"><summary>Вопрос</summary><p>Ответ</p></details>` и добавьте стили для плавного раскрытия и визуального индикатора.
SAFE CSS:
```css
.faq-item {
border-top: 1px solid #e5e7eb;
padding: .75rem 0;
}
.faq-item summary {
cursor: pointer;
list-style: none;
font-weight: 600;
position: relative;
padding-right: 1.5rem;
}
.faq-item summary::after {
content: "▸";
position: absolute;
right: 0;
transition: transform .3s;
}
.faq-item[open] summary::after {
transform: rotate(90deg);
}
.faq-item p {
margin-top: .5rem;
line-height: 1.5;
animation: fadeIn .3s ease-out;
}
@keyframes fadeIn { from {opacity:0;} to {opacity:1;} }
```

## Когда применять
Улучшает структуру FAQ, делает контент сканируемым, экономит место, повышает доверие через интерактивность без JavaScript.

## Проверка
В браузере открыть FAQ, кликнуть каждый вопрос – контент должен плавно раскрываться/сворачиваться.
