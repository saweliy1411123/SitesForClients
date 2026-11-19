# localhost:8080/ovh/gpt-oss-120b  2026-11-17 08:11:55
duration=60.2 error=- attempts=1

IDEA: Визуальный доверительный бейдж «Яндекс‑партнёр» рядом с заголовком в hero  
KNOB: Внутри `<header class="hero">` сразу после `<h1 class="reveal">` добавить  
```html
<div class="trust-badge" aria-label="Савелий — проверенный партнёр Яндекса">
  <img src="data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzAiIGhla..."/>
  <span>Яндекс‑партнёр</span>
</div>
```  
и в CSS добавить стили (пример):  
```css
.trust-badge{display:flex;align-items:center;margin-top:12px;color:#fff;font-size:14px}
.trust-badge img{height:20px;margin-right:6px}
```  
EFFECT: Усилит восприятие экспертизы и надёжности сразу на первом экране, повышая доверие и конверсию CTA.  
RISK: Требует наличия прав на логотип Яндекса; при отсутствии лицензии может нарушать бренд‑правила.  
ROLLBACK: `git checkout -- index.html` (или удалить вставленный блок и стили).  
VERIFY: Открыть страницу, убедиться, что бейдж виден рядом с заголовком, корректно масштабируется на мобильных, и проверка alt‑текста в DevTools.  
PRIORITY: 1 – высокий ROI, небольшие изменения, сразу повышают доверие.  

IDEA: Кликабельный телефонный CTA с `tel:` и микроданными `schema.org/ContactPoint`  
KNOB: В секцию `.final` (финальный CTA) добавить после существующего текста кнопку‑ссылку:  
```html
<a href="tel:+7(999)123-45-67" class="btn-primary phone-cta" aria-label="Позвонить Савелию: +7 999 123‑45‑67">
  📞 Позвонить сейчас
</a>
```  
и в `<head>` добавить JSON‑LD:  
```json
{
  "@context":"https://schema.org",
  "@type":"LocalBusiness",
  "telephone":"+7-999-123-4567",
  "contactPoint":{
    "@type":"ContactPoint",
    "telephone":"+7-999-123-4567",
    "contactType":"sales"
  }
}
```  
EFFECT: Уменьшит трение для мобильных пользователей, позволяя сразу позвонить, повышая конверсию из мобильного трафика.  
RISK: Неправильный формат номера или отсутствие поддержки `tel:` на десктопе (не критично).  
ROLLBACK: Удалить добавленный `<a>` и `<script type="application/ld+json">` блок.  
VERIFY: На мобильном эмуляторе кликнуть кнопку → должно открыться dialer; в консоли проверить наличие `ContactPoint` в `application/ld+json`.  
PRIORITY: 2 – быстрый выигрыш в мобильной конверсии, низкий риск.  

IDEA: Карусель логотипов клиентов (социальное доказательство) под секцией цены  
KNOB: После закрывающего `</section>` цены (`#price`) вставить:  
```html
<section class="clients-carousel" aria-label="Клиенты">
  <h3 class="visually-hidden">Наши клиенты</h3>
  <div class="carousel-track">
    <img src="client1.svg" alt="Логотип клиента 1" loading="lazy">
    <img src="client2.svg" alt="Логотип клиента 2" loading="lazy">
    <img src="client3.svg" alt="Логотип клиента 3" loading="lazy">
    <img src="client4.svg" alt="Логотип клиента 4" loading="lazy">
  </div>
</section>
```  
и CSS:  
```css
.clients-carousel{overflow:hidden;padding:40px 0;background:#f9fafb}
.carousel-track{display:flex;gap:32px;animation:scroll 20s linear infinite}
.carousel-track img{height:40px;filter:grayscale(100%) contrast(0.9)}
@keyframes scroll{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
```  
EFFECT: Демонстрирует реальное сотрудничество, повышая социальное доказательство и доверие, что положительно сказывается на конверсии.  
RISK: Нужно иметь реальные логотипы; использование вымышленных может нарушать правила честности.  
ROLLBACK: Удалить вставленный блок и CSS‑правила.  
VERIFY: Открыть страницу, убедиться, что карусель отображается, анимация работает, и логотипы загружаются без ошибок (Network).  
PRIORITY: 3 – дополнительный социальный сигнал, требует подготовки логотипов, но полезен для долгосрочного доверия.
