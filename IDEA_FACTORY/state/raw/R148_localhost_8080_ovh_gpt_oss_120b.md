# localhost:8080/ovh/gpt-oss-120b  2026-11-17 08:50:27
duration=28.5 error=- attempts=1

IDEA: Hero benefit badge – чёткая визуальная формулировка оффера  
KNOB: Внутри `<header class="hero">` сразу после `<h1>` добавить  
```html
<div class="hero-badge" aria-label="Ключевое предложение">
  <svg class="icon" aria-hidden="true">…</svg>
  <span>2 дня → готовый сайт, клиенты из Яндекса</span>
</div>
```  
и в CSS (в `<style>` или отдельный файл)   
```css
.hero-badge{
  display:inline-flex;
  align-items:center;
  gap:.5rem;
  padding:.4rem .8rem;
  margin-top:.8rem;
  background:var(--bg);
  border:1px solid var(--border);
  border-radius:6px;
  font-size:clamp(14px,2vw,16px);
  color:var(--text);
}
.hero-badge .icon{
  width:1em;height:1em;fill:var(--blue);
}
```  
EFFECT: мгновенно сообщает клиенту «что», «за сколько», «где», повышая понятность оффера и CTR CTA.  
RISK: небольшое увеличение высоты hero‑секции; на мобильных может потребовать небольшую корректировку паддингов.  
ROLLBACK: `git checkout -- index.html` (удалить вставленный блок и CSS).  
VERIFY: открыть страницу, убедиться, что блок виден под заголовком, высота hero ≤ 120 vh, отсутствие горизонтального скролла.  
PRIORITY: 1 – высокий ROI за ≈ 5 минут работы.  
SITE_REQUEST: hero  

---  

IDEA: FAQ‑аккордеон – сворачиваемые ответы для лучшей мобильной читаемости  
KNOB: В секции `#faq .faq` заменить каждый `<h3>` + текст на структуру `<details><summary>Вопрос</summary>Ответ</details>`. Добавить CSS:  
```css
.faq details{
  margin-bottom:1rem;
  border-bottom:1px solid var(--border);
}
.faq summary{
  cursor:pointer;
  font-weight:600;
  padding:.5rem 0;
}
.faq summary::marker{color:var(--blue);}
.faq details[open] summary{color:var(--blue);}
```  
EFFECT: уменьшает длину страницы, ускоряет восприятие, повышает удобство навигации на мобильных, тем самым повышает конверсию.  
RISK: в старых браузерах (< Edge 79) `<details>` может не работать; однако в современных браузерах поддержка‑полная.  
ROLLBACK: `git checkout -- index.html` (удалить `<details>`‑структуру и CSS).  
VERIFY: в Chrome/Firefox открыть страницу, переключить в режим мобильного устройства, кликнуть по вопросам – ответы должны раскрываться/сворачиваться без перезагрузки.  
PRIORITY: 2 – средний эффект, но небольшие усилия и улучшение UX.  
SITE_REQUEST: faq  

---  

IDEA: Trust‑badge‑row в hero‑секции – социальные подтверждения доверия сразу вверху  
KNOB: После `<div class="hero-badge">` (или после `<h1>` если badge не используется) вставить  
```html
<div class="hero-trust" aria-label="Доверие клиентов">
  <svg class="trust-icon" aria-label="Yandex Partner">…</svg>
  <svg class="trust-icon" aria-label="Google Partner">…</svg>
  <span class="trust-text">100+ довольных клиентов</span>
</div>
```  
и добавить CSS:  
```css
.hero-trust{
  display:flex;
  align-items:center;
  gap:1rem;
  margin-top:.8rem;
  flex-wrap:wrap;
}
.hero-trust .trust-icon{
  width:24px;height:24px;fill:var(--blue);
}
.hero-trust .trust-text{
  font-size:clamp(13px,2vw,15px);
  color:var(--muted);
}
```  
EFFECT: повышает уровень доверия сразу на первом экране, улучшает конверсию за счёт социальных доказательств.  
RISK: добавление небольших SVG‑иконок (≈ 2 KB) слегка увеличит размер первой загрузки; можно использовать inline‑SVG, чтобы избежать дополнительных запросов.  
ROLLBACK: `git checkout -- index.html` (удалить блок и CSS).  
VERIFY: открыть страницу, убедиться, что иконки и текст отображаются корректно, проверить размер `index.html` (не более + 5 KB).  
PRIORITY: 2 – значительное влияние на доверие, лёгкая реализация.  
SITE_REQUEST: hero
