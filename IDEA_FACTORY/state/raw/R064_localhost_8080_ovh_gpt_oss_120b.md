# localhost:8080/ovh/gpt-oss-120b  2026-11-17 04:46:25
duration=27.4 error=- attempts=1

We need to request snippet.
IDEA: Подзаголовок‑бонус под <h1> — чёткое обещание результата  
KNOB: В hero‑секцию сразу после `<h1 class="reveal">…</h1>` добавить `<p class="hero-sub" style="font-size:clamp(18px,4vw,24px);color:var(--muted);margin-top:12px;">Получите готовый сайт за 2 дня — заявки из Яндекса вырастут минимум 30 %</p>`  
EFFECT: Увеличит восприятие ценности оффера, снизит «потерю»‑внимания в «болях» и повысит конверсию CTA‑кнопки.  
RISK: Требует согласования реального KPI (30 %); если цифра неверна – риск недоверия.  
ROLLBACK: `git checkout -- index.html` (или удалить добавленную строку).  
VERIFY: Открыть страницу, убедиться, что под заголовком появился новый абзац, проверить визуально в мобильной и десктоп‑версии (2 мин).  
PRIORITY: 1 — минимальное вмешательство, высокий потенциал конверсии.  

---  

IDEA: Доверительный «Yandex Business Verified»‑бэйдж в hero‑note  
KNOB: Внутри `<p class="hero-note">` (L465) добавить сразу после существующего текста `<span class="yandex-badge" aria-label="Сайт подтверждён Яндекс.Бизнесом" role="img" style="display:inline-block;vertical-align:middle;margin-left:8px;"><svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2L2 7v7c0 5 4 9 10 9s10-4 10-9V7z"/><path d="M12 12v6"/><path d="M9 9h6"/></svg></span>`  
EFFECT: Явный визуальный сигнал надёжности от известного бренда, повышает доверие и готовность к контакту.  
RISK: Нужно убедиться, что такой бейдж действительно может быть использован без лицензии; при отсутствии подтверждения – потенциальный юридический риск.  
ROLLBACK: Удалить добавленную строку `<span class="yandex-badge">…</span>` (git checkout).  
VERIFY: Перезагрузить страницу, проверить, что бейдж отображается рядом с текстом, убедиться, что он не ломает разметку (2 мин).  
PRIORITY: 2 — добавляет доверие без значительных технических изменений, но требует подтверждения легитимности.  

---  

IDEA: «Sticky CTA bar» внизу экрана после прокрутки > 300 px  
KNOB: В конец `<body>` добавить  

```html
<div class="sticky-cta-bar" role="region" aria-label="Быстрый запрос демо">
  <a class="btn-primary" href="#contact" style="margin-right:12px;">Получить демо бесплатно</a>
  <a class="btn-primary" href="tel:+7XXXXXXXXXX" style="background:#4cc9f0;">Позвонить +7 XXX XXX‑XX‑XX</a>
</div>
```

и в CSS (после существующего стилей) добавить  

```css
.sticky-cta-bar{
  position:fixed;bottom:-100px;left:0;right:0;display:flex;justify-content:center;align-items:center;
  padding:12px;background:rgba(139,92,246,.9);backdrop-filter:blur(6px);z-index:1000;transition:bottom .4s;
}
.sticky-cta-bar.show{bottom:0;}
@media(max-width:720px){
  .sticky-cta-bar{flex-direction:column;gap:8px;}
}
```

и в конец `<script>` добавить небольшую логику (без внешних зависимостей):

```js
(() => {
  const bar = document.querySelector('.sticky-cta-bar');
  const toggle = () => bar.classList.toggle('show', window.scrollY > 300);
  window.addEventListener('scroll', toggle);
  toggle();
})();
```  

EFFECT: Постоянный доступ к главному CTA, повышает вероятность клика у пользователей, которые уже пролистали страницу.  
RISK: Добавление небольшого JS может немного увеличить TTI; если пользователь отключил JavaScript – элемент не появится (не критично).  
ROLLBACK: Удалить добавленный `<div class="sticky-cta-bar">…</div>` и соответствующие CSS/JS‑блоки (git checkout).  
VERIFY: Открыть страницу, прокрутить ниже 300 px – панель должна плавно выскочить; клик по любой кнопке проверяется в 2 мин.  
PRIORITY: 3 — высокий потенциал конверсии, но требует небольших изменений в разметке и скрипте.
