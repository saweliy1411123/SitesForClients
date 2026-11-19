# localhost:8080/ovh/gpt-oss-120b  2026-11-17 07:06:11
duration=22.4 error=- attempts=1

IDEA: SKILL — scroll-progress-bar  
KNOB: **Name:** `scroll-progress-bar`  
**When to apply:** На любом одностраничном лендинге, где важна визуальная индикация прогресса чтения и удержания внимания пользователя.  
**Steps:**  
1. В конец `<body>` добавить элемент `<div class="scroll-progress"><div class="scroll-progress__fill"></div></div>`.  
2. В `index.improved.html` подключить файл `scroll-progress.css` (inline‑вставка в `<style>`).  
3. Добавить безопасный скрипт `scroll-progress.js`, который слушает событие `scroll` и задаёт ширину `.scroll-progress__fill` в % от прокрутки.  
4. При необходимости задать `z-index` выше шапки, чтобы индикатор всегда был виден.  

**SAFE CSS:**  
```css
/* scroll-progress-bar */
.scroll-progress{
  position:fixed;
  top:0;
  left:0;
  width:100%;
  height:4px;
  background:rgba(0,0,0,0.1);
  z-index:9999;
}
.scroll-progress__fill{
  width:0%;
  height:100%;
  background:var(--blue);
  transition:width .2s ease-out;
}
```

**SAFE JS:**  
```js
/* scroll-progress-bar */
document.addEventListener('scroll',function(){
  const docHeight = document.documentElement.scrollHeight - window.innerHeight;
  const scrolled = (window.scrollY / docHeight) * 100;
  document.querySelector('.scroll-progress__fill').style.width = `${scrolled}%`;
});
```  

EFFECT: Пользователь сразу видит, сколько контента уже просмотрел, повышая вовлечённость и вероятность прокрутки до CTA‑блоков.  
RISK: Минимальный — небольшое увеличение DOM‑узла и небольшая нагрузка от `scroll`‑listener (можно оптимизировать через `requestAnimationFrame`).  
ROLLBACK: `git rm index.improved.html && git checkout index.html` (или удалить блоки `<div class="scroll-progress">` и скрипт).  
VERIFY: Открыть страницу в браузере, прокручивать вниз — индикатор должен плавно заполняться от 0 % до 100 % без задержек.  
PRIORITY: 1 – быстрый, заметный эффект на UX и метрику времени на странице, без необходимости бэкенда.  

---  

IDEA: SKILL — faq-accordion-details  
KNOB: **Name:** `faq-accordion-details`  
**When to apply:** На любой лендинг‑странице с секцией FAQ, где требуется улучшить семантику, доступность и анимацию раскрытия ответов.  
**Steps:**  
1. В секции `#faq` заменить каждый блок `<div class="faq-item">` на `<details class="faq-item"><summary class="faq-question">…</summary><div class="faq-answer">…</div></details>`.  
2. Добавить стили для плавного раскрытия/сворачивания и визуального маркера.  
3. При желании добавить небольшой скрипт, который закрывает все остальные `<details>` при открытии нового (необязательно, сохраняет чистый HTML).  

**SAFE CSS:**  
```css
/* faq-accordion-details */
details.faq-item{
  border-bottom:1px dashed var(--border);
  padding:12px 0;
}
details.faq-item summary{
  cursor:pointer;
  list-style:none;
  font-weight:600;
  display:flex;
  align-items:center;
  gap:8px;
}
details.faq-item summary::-webkit-details-marker{
  display:none;
}
details.faq-item summary::after{
  content:"▸";
  transition:transform .2s;
}
details[open].faq-item summary::after{
  transform:rotate(90deg);
}
details.faq-item .faq-answer{
  margin-top:8px;
  animation:fadeIn .3s ease-out;
}
@keyframes fadeIn{
  from{opacity:0;transform:translateY(-4px);}
  to{opacity:1;transform:none;}
}
```  

**SAFE JS (optional):**  
```js
/* faq-accordion-details – закрывать остальные при открытии */
document.querySelectorAll('details.faq-item').forEach(d=>{
  d.addEventListener('toggle',()=>{ if(d.open){
    document.querySelectorAll('details.faq-item').forEach(o=>{ if(o!==d) o.open=false; });
  }});
});
```  

EFFECT: Улучшает доступность (поддержка клавиатуры, ARIA‑поведение), повышает доверие поисковиков (semantic HTML) и делает раскрытие ответов визуально приятным, что может увеличить время на странице и CTR к CTA‑блокам.  
RISK: Требует небольших правок в разметке; если в тексте есть вложенные ссылки, они сохранят свою работу без изменений.  
ROLLBACK: Восстановить оригинальный файл из Git (`git checkout -- index.html`) или заменить блоки `<details>` обратно на `<div class="faq-item">`.  
VERIFY: Открыть страницу, кликнуть по каждому вопросу – ответы должны плавно открываться/закрываться, а клавиша Tab должна фокусировать заголовки вопросов.  
PRIORITY: 2 – повышает SEO и a11y без влияния на бизнес‑логика, но требует небольших правок в HTML, поэтому чуть ниже по срочности, чем scroll‑progress‑bar.
