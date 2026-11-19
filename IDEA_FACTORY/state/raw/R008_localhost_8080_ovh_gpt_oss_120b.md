# localhost:8080/ovh/gpt-oss-120b  2026-11-17 02:03:40
duration=27.1 error=- attempts=1

IDEA: Добавить короткий список преимуществ сразу под H1 (яркая выгода)  
KNOB: Вставить после `<h1 class="reveal"...>` блок  
```html
<ul class="hero-benefits reveal" style="--d:.2s">
  <li><svg class="check-icon" ...></svg> Сайт готов за 2 дня</li>
  <li><svg class="check-icon" ...></svg> Клиенты находят вас в Яндексе</li>
  <li><svg class="check-icon" ...></svg> Бесплатный демо‑макет</li>
</ul>
```  
и добавить минимальный CSS:  
```css
.hero-benefits{display:flex;gap:1rem;flex-wrap:wrap;justify:center;margin-top:1rem}
.hero-benefits li{display:flex;align-items:center;font-size:1rem;color:#222}
.check-icon{width:1.2rem;height:1.2rem;margin-right:.4rem;stroke:#8b5cf6;stroke-width:2;fill:none}
```  
EFFECT: мгновенно повышает ясность оффера, пользователь видит 3‑х конкретных выгоды без необходимости скроллить.  
RISK: небольшое увеличение HTML‑размера; если список будет слишком длинным — визуальный шум.  
ROLLBACK: `git checkout -- index.html` (или удалить вставленный блок и CSS).  
VERIFY: открыть страницу в браузере, убедиться, что список отображается под заголовком, проверить адаптивность (375 px, 768 px).  
PRIORITY: 1 – самый быстрый способ повысить конверсию на первом экране.  

---  

IDEA: Добавить кликабельный телефонный CTA‑кнопку рядом с основным CTA‑ссылкой  
KNOB: В секции hero (после `.hero-note`) добавить кнопку‑ссылку  
```html
<a href="tel:+7XXXXXXXXXX" class="btn-phone reveal" style="--d:.3s">
  📞 Позвонить сейчас
</a>
```  
и CSS (переиспользовать стили кнопок):  
```css
.btn-phone{display:inline-block;margin-left:.8rem;padding:.6rem 1.2rem;
  background:#8b5cf6;color:#fff;border-radius:4px;font-weight:600;
  text-decoration:none;transition:background .2s}
.btn-phone:hover{background:#7c3aed}
```  
EFFECT: даёт пользователям возможность сразу позвонить, повышая шанс мгновенного контакта, особенно на мобильных.  
RISK: если номер будет недоступен, может вызвать негатив; требуется согласовать реальный номер с владельцем.  
ROLLBACK: удалить добавленную кнопку и CSS‑правило.  
VERIFY: открыть страницу на мобильном устройстве, кликнуть кнопку – должно открыться диалог вызова; проверить, что стили соответствуют остальному дизайну.  
PRIORITY: 2 – конверсия через телефонный канал часто выше, но требует реального номера.  

---  

IDEA: Добавить секцию «Доверяют нам» с логотипами партнёров (Yandex, VK, Google) для повышения доверия  
KNOB: Вставить перед секцией FAQ новый `<section class="trust">`  
```html
<section class="trust reveal" style="--d:.4s">
  <h2 class="trust-title">Клиенты доверяют нам</h2>
  <div class="trust-logos">
    <svg class="logo yandex" ...></svg>
    <svg class="logo vk" ...></svg>
    <svg class="logo google" ...></svg>
  </div>
</section>
```  
и CSS:  
```css
.trust{padding:2rem 0;text-align:center}
.trust-title{font-size:1.5rem;margin-bottom:1rem;color:#222}
.trust-logos{display:flex;gap:2rem;justify:center;align-items:center}
.trust-logos .logo{width:48px;height:auto;filter:grayscale(100%) opacity(.8)}
.trust-logos .logo:hover{filter:none;opacity:1}
```  
EFFECT: визуальные подтверждения (логотипы известных сервисов) усиливают социальное доказательство, снижают скептицизм и повышают доверие к предложению.  
RISK: необходимо убедиться, что использование логотипов разрешено (обычно допускается при указании «работаем с»); иначе может возникнуть нарушение бренда.  
ROLLBACK: удалить секцию и связанные стили.  
VERIFY: открыть страницу, убедиться, что секция отображается корректно, логотипы видимы, проверить на мобильных размерах, убедиться в отсутствии консольных ошибок.  
PRIORITY: 3 – повышает доверие, но требует согласования логотипов; менее критично, чем улучшения первого экрана.
