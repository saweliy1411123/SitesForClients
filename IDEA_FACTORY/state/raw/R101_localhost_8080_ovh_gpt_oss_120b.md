# localhost:8080/ovh/gpt-oss-120b  2026-11-17 06:37:35
duration=21.6 error=- attempts=1

**Критика текущего списка**  
Большинство идей — повторения (напр., «Три шага — явный результат» встречается более 10 раз) — или микроскопические визуальные улучшения, которые дают ограниченный прирост конверсии, но увеличивают технический долг. Некоторые предложения требуют серверных изменений (например, «Telegram deep‑link с предзаполненным текстом заявки»), что выходит за рамки статического лендинга. Приоритет следует отдавать фундаментальным SEO‑ и a11y‑улучшениям, которые дают измеримый рост трафика и снижают барьеры для пользователей, а не лишь «красивые» анимации.

---

### IDEA: I-00701 — JSON‑LD Service schema для описания услуги «лендинг за 2 дня»
**KNOB:** В `<head>` перед закрывающим `</head>` добавить скрипт‑блок  
```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"Service",
  "serviceType":"Создание лендингов за 2 дня",
  "provider":{
    "@type":"LocalBusiness",
    "name":"Савелий",
    "url":"https://example.com",
    "address":{
      "@type":"PostalAddress",
      "addressLocality":"Пермь",
      "addressCountry":"RU"
    },
    "telephone":"+7 999 123‑45‑67"
  },
  "offers":{
    "@type":"Offer",
    "priceCurrency":"RUB",
    "price":"12000",
    "priceSpecification":{
      "@type":"UnitPriceSpecification",
      "priceCurrency":"RUB",
      "price":"12000",
      "unitText":"за проект"
    },
    "availability":"https://schema.org/InStock"
  }
}
</script>
```
**EFFECT:** Улучшает локальное SEO — поисковые системы могут показывать сервис в результатах «Услуги рядом», повышая клики из Яндекса.  

**RISK:** Требует точного указания цены; если в дальнейшем будет менять — нужно будет обновлять структуру.  

**ROLLBACK:** `git checkout HEAD -- index.html` (или удалить только вставленный `<script>`).  

**VERIFY:** В Chrome DevTools → Application → Structured Data → проверка наличия валидного `Service`‑объекта; запустить Google Rich Results Test.  

**PRIORITY:** 1 — низкая техническая сложность, высокий SEO‑эффект, быстро проверяется.

---

### IDEA: I-00702 — DNS‑prefetch и preconnect к yandex.ru для ускорения внешних запросов
**KNOB:** В `<head>` добавить две строки перед первым `<link rel="preload">`  
```html
<link rel="dns-prefetch" href="https://yandex.ru">
<link rel="preconnect" href="https://yandex.ru" crossorigin>
```
**EFFECT:** Сокращает время первого DNS‑lookup и TLS‑рукопожатия при загрузке внешних скриптов/виджетов Яндекса (например, метрика, карты), ускоряя LCP и уменьшая задержку интерактивности.  

**RISK:** Если в дальнейшем Яндекс‑ресурсы будут удалены, предзагрузка станет лишней, но не навредит.  

**ROLLBACK:** Удалить добавленные `<link>`‑теги (или `git checkout HEAD -- index.html`).  

**VERIFY:** Открыть страницу в Chrome → Network, включить “Disable cache”, обновить; измерить `connectStart` → `dnsStart` для yandex.ru до и после.  

**PRIORITY:** 2 — минимальный код, измеримый прирост скорости, особенно важен для мобильных пользователей, где LCP критичен.
