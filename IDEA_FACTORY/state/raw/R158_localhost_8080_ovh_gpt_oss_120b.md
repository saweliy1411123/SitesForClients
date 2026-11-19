# localhost:8080/ovh/gpt-oss-120b  2026-11-17 09:18:34
duration=46.3 error=- attempts=1

IDEA: Click‑to‑call CTA‑button в hero‑секции  
KNOB: Внутри `<header class="hero">` добавить сразу после подзаголовка `<p class="sub">` кнопку‑ссылку  
```html
<a href="tel:+73412345678" class="btn-primary cta-call" role="button" aria-label="Позвонить сейчас">
  📞 Позвонить бесплатно
</a>
```  
и в CSS добавить минимум `margin-top:1rem;` для отступа.  
EFFECT: Увеличивает конверсию мобильных пользователей, позволяя сразу связаться без копирования номера.  
RISK: Требует подтверждения владельца о наличии рабочего телефонного номера.  
ROLLBACK: `git checkout -- index.html` (или удалить только добавленные строки).  
VERIFY: Открыть страницу на мобильном эмуляторе, кликнуть кнопку – должно открыться приложение звонка/диалог “Позвонить”.  
PRIORITY: 1 – быстрый прирост конверсии на мобильных, минимальные изменения кода.  

IDEA: Иконки‑визуализация пунктов боли  
KNOB: В секции `#problem` (см. SITE_REQUEST «problem») заменить каждый `<h3>`‑пункт на блок с SVG‑иконкой слева:  
```html
<div class="pain-item">
  <svg class="icon" aria-hidden="true">…</svg>
  <h3>Вас не находят в поиске</h3>
</div>
```  
и добавить в CSS `.pain-item{display:flex;align-items:center;gap:0.75rem;margin-bottom:1rem;}`.  
EFFECT: Улучшает сканируемость текста, повышает восприятие проблемы и удерживает внимание.  
RISK: Увеличит размер HTML (~1 KB) за счёт встроенных SVG‑иконок.  
ROLLBACK: Удалить блоки `.pain-item` и вернуть оригинальные `<h3>` (git checkout).  
VERIFY: В браузере убедиться, что каждый пункт отображается с иконкой и выравнивается корректно.  
PRIORITY: 2 – повышает UX без влияния на SEO, небольшие затраты.  

IDEA: Автоматическая нумерация шагов с анимацией появления  
KNOB: В секции «Три шага» (см. SITE_REQUEST «steps») добавить класс‑контейнеру шагов `class="step"` и в CSS использовать счётчик:  
```css
.step::before{
  counter-increment: step;
  content: counter(step);
  display:inline-block;
  width:2rem;height:2rem;
  line-height:2rem;
  text-align:center;
  background:var(--blue);
  color:#fff;
  border-radius:50%;
  margin-right:0.5rem;
  opacity:0;
  transform:translateY(10px);
  transition:opacity .4s ease,transform .4s ease;
}
.step.visible::before{opacity:1;transform:none;}
```  
JS‑скрипт (≈10 строк) добавит класс `.visible` к каждому `.step` при появлении в viewport (IntersectionObserver).  
EFFECT: Делает процесс более наглядным, усиливает восприятие последовательности, повышает вовлечённость.  
RISK: Требует небольшого JS; может конфликтовать с уже существующим скриптом, если он использует глобальные переменные.  
ROLLBACK: Удалить добавленные стили и скрипт (git checkout).  
VERIFY: Прокрутить страницу, убедиться, что перед каждым шагом появляется цифра с плавной анимацией.  
PRIORITY: 2 – визуальный апгрейд, легко реализуемый, улучшает UX.  

IDEA: Ссылка‑скачивание PDF‑кейса под каждым демо‑концептом  
KNOB: В секции демо (см. SITE_REQUEST «works») после описания каждого концепта добавить кнопку‑ссылку:  
```html
<a href="case-study-01.pdf" class="btn-secondary download-pdf" download>Скачать кейс‑стади (PDF)</a>
```  
и в CSS `.download-pdf{margin-top:0.5rem;}`.  
EFFECT: Предлагает более глубокий материал для «скептиков», повышает доверие и шанс конверсии.  
RISK: Требует наличия PDF‑файлов на сервере; если их нет – ссылка будет битой.  
ROLLBACK: Удалить добавленные ссылки (git checkout).  
VERIFY: Кликнуть ссылку – должен начаться download PDF без ошибок 404.  
PRIORITY: 2 – добавляет ценный контент, небольшие затраты.  

IDEA: Тултип‑подсказка «Что входит в цену» в карточке цены  
KNOB: Внутри `.price-card` (см. SITE_REQUEST «price») добавить атрибут `aria-describedby="price-incl"` к элементу цены и блок‑тултип:  
```html
<span id="price-incl" class="tooltip" role="tooltip">
  Включает: дизайн, адаптивность, базовый SEO, 1‑мес. поддержки
</span>
```  
CSS:  
```css
.tooltip{
  visibility:hidden;
  opacity:0;
  position:absolute;
  background:#fff;
  border:1px solid var(--border);
  padding:0.5rem;
  border-radius:4px;
  top:100%; left:0;
  transition:opacity .2s;
}
.price-card:hover .tooltip{visibility:visible;opacity:1;}
```  
EFFECT: Снимает сомнения о составе цены, повышает доверие и готовность к покупке.  
RISK: Тултип может перекрывать другие элементы на маленьких экранах; требуется проверка на мобильных.  
ROLLBACK: Удалить блок `.tooltip` и атрибут `aria-describedby` (git checkout).  
VERIFY: Навести курсор (или тап) на цену – появится подсказка с перечислением включений.  
PRIORITY: 2 – повышает прозрачность предложения, небольшие изменения.  

IDEA: Поисковый фильтр по вопросам в FAQ  
KNOB: В секции `#faq` добавить над списком поле ввода и JS‑скрипт, который скрывает/показывает вопросы по совпадению текста:  
```html
<input type="search" id="faq-search" placeholder="Найти вопрос…" class="faq-search">
```
JS (≈15 строк) слушает `input` и сравнивает `innerText` вопросов, скрывая не совпадающие (`.faq-item {display:none;}`).  
EFFECT: Пользователи быстрее находят нужный ответ, снижая фрустрацию и повышая удовлетворённость.  
RISK: Добавит небольшую нагрузку JS; требуется тестировать на старых браузерах (можно добавить полифил).  
ROLLBACK: Удалить `<input>` и скрипт (git checkout).  
VERIFY: Ввести часть текста вопроса – соответствующие пункты остаются видимыми, остальные скрыты.  
PRIORITY: 2 – улучшает UX без влияния на SEO, легко измеряется (время поиска).  

IDEA: ARIA‑live‑region для подтверждения отправки финального CTA‑запроса  
KNOB: В секции `.final` (см. SITE_REQUEST «final») обернуть текст CTA‑кнопки в `<div class="final-cta" aria-live="polite">…</div>` и добавить небольшую JS‑функцию, которая после клика меняет текст на «Спасибо! Мы свяжемся с вами в течение 15 минут».  
EFFECT: Улучшает доступность для скрин‑ридеров, фиксирует действие пользователя, повышает доверие.  
RISK: Требует небольшого JS; если пользователь отключил JS, сообщение не появится (не критично).  
ROLLBACK: Удалить `aria-live` и скрипт (git checkout).  
VERIFY: Кликнуть CTA, убедиться, что текст меняется и скрин‑ридер объявляет новое сообщение.  
PRIORITY: 2 – небольшие изменения, но сильный эффект для доступности.
