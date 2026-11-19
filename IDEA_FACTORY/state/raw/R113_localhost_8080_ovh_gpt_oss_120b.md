# localhost:8080/ovh/gpt-oss-120b  2026-11-17 07:11:57
duration=26.3 error=- attempts=1

IDEA: Accessible CTA links — роль button и aria‑label  
KNOB: Во всех ссылках‑CTA с классом `.btn-primary` добавить атрибуты `role="button"` и `aria-label="Получить бесплатный демо‑лендинг"`; дополнительно в глобальном CSS добавить `:focus-visible {outline:3px solid var(--blue);}` (если ещё нет).  
EFFECT: Увеличит конверсию у пользователей скрин‑ридеров и клавиатурной навигации, повысит WCAG‑AA‑соответствие и доверие к сайту.  
RISK: Небольшой риск — некоторые старые браузеры могут игнорировать `role="button"` (но это безопасно).  
ROLLBACK: `git checkout -- index.html` (или восстановить из копии).  
VERIFY: Открыть страницу в Chrome, включить DevTools → Accessibility, убедиться, что у CTA‑ссылок есть `role="button"` и `aria-label`; проверить, что при Tab‑фокусе появляется outline.  
PRIORITY: 1 — доступность напрямую влияет на конверсию и SEO.  
SITE_REQUEST: «btn-primary»

---

IDEA: Яндекс‑Бизнес‑верификация — визуальный trust‑badge и schema.org LocalBusiness verificationProperty  
KNOB: После секции `#price` вставить блок `<div class="trust-badge"><img src="yandex-badge.svg" alt="Подтверждено в Яндекс.Бизнес" width="120"><span>Проверено в Яндекс.Бизнес</span></div>`; добавить в `<head>` JSON‑LD `<script type="application/ld+json">{"@context":"https://schema.org","@type":"LocalBusiness","name":"Савелий","address":{"@type":"PostalAddress","addressLocality":"Пермь"},"verificationProperty":"Yandex Business"}"</script>`.  
EFFECT: Усиливает доверие потенциальных клиентов (социальное доказательство) и улучшает локальное SEO за счёт структурированных данных.  
RISK: Требует наличия реального подтверждения в Яндекс.Бизнес; без него может выглядеть вводящим в заблуждение.  
ROLLBACK: Удалить вставленный `<div class="trust-badge">` и скрипт‑блок; `git checkout -- index.html`.  
VERIFY: В браузере увидеть бейдж под ценой; в DevTools → Structured Data проверить наличие `LocalBusiness` с `verificationProperty`.  
PRIORITY: 2 — доверие критично для B2B‑лендинга, а реализация лёгка.  
SITE_REQUEST: «price»

---

IDEA: Сжимающийся фиксированный хедер + плавающая CTA‑кнопка после скролла  
KNOB: В `<header class="hero">` добавить класс `shrinkable`; в CSS `.shrinkable {transition:height .3s; height:100vh;} .shrinkable.scrolled {height:70vh;}`; в JS‑блок (в конце `<body>`) добавить `const hdr=document.querySelector('header');window.addEventListener('scroll',()=>{hdr.classList.toggle('scrolled',window.scrollY>100);});` и после хедера вставить `<a href="#price" class="btn-primary sticky-cta" role="button">Получить демо бесплатно</a>` с `position:fixed;bottom:20px;right:20px;display:none;` + `.shrinkable.scrolled ~ .sticky-cta{display:block;}`.  
EFFECT: Хедер уменьшится, освобождая экранное пространство, а CTA‑кнопка будет всегда доступна после прокрутки, повышая количество кликов.  
RISK: Добавление JS может слегка увеличить TTI; требует тестирования на старых устройствах.  
ROLLBACK: Удалить добавленные CSS‑правила, JS‑скрипт и элемент `.sticky-cta`; `git checkout -- index.html`.  
VERIFY: Прокрутить страницу, убедиться, что хедер стал короче и появилось фиксированное CTA‑окно; кликнуть CTA — должна перейти к секции цены.  
PRIORITY: 3 — улучшает UX и конверсию, но менее критично, чем доверие и доступность.  
SITE_REQUEST: «header»
