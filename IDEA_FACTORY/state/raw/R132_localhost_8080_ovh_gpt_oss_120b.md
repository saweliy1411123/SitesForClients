# localhost:8080/ovh/gpt-oss-120b  2026-11-17 08:05:21
duration=47.2 error=- attempts=1

IDEA: SKILL — critical-css-inline  
KNOB: **Name:** critical-css-inline  
**When to apply:** На любой статический лендинг, где важен быстрый первый рендер (например, hero‑секция и верхний блок контента).  
**Steps:**  
1. Определить набор CSS‑прав, отвечающих только за стили выше‑скролла (`.hero`, `.nav`, `.hero h1`, `.hero p.sub`, `.nav-links`, `.btn-primary` и т.п.).  
2. Скопировать эти правила в отдельный блок `<style data-critical>` сразу после `<meta charset="utf-8">`.  
3. Оставить оригинальный `<link rel="stylesheet" href="styles.css">` но добавить атрибут `media="print"` и `onload="this.media='all'"` для отложенной загрузки.  
4. При необходимости добавить небольшую JS‑прошивку, которая после `load` удалит атрибут `media` у линка, чтобы стили применились без повторного рендера.  
**SAFE CSS:**  
```css
/* Critical CSS – above‑the‑fold */
.hero{position:relative;min-height:100vh;display:flex;align-items:center;padding:130px 0 100px;overflow:hidden}
.hero .wrap{position:relative;z-index:3}
.hero h1{font-size:clamp(32px,6vw,58px);font-weight:700;line-height:1.2}
.hero p.sub{color:#c3cad9;font-size:clamp(16.5px,2vw,20px);max-width:560px;margin:28px 0 38px}
.nav{display:flex;justify-content:space-between;align-items:center;padding:20px}
.nav-links{display:flex;gap:28px;font-size:14px;color:var(--muted);font-weight:500}
.btn-primary{display:inline-flex;align-items:center;justify-content:center;padding:12px 24px;background:var(--grad);color:#fff;border-radius:6px;text-decoration:none}
```  
**SAFE JS:**  
```js
document.addEventListener('load',function(){ 
  const ss=document.querySelector('link[rel="stylesheet"][media="print"]');
  if(ss) ss.media='all';
});
```  
EFFECT: Сокращение LCP — критический CSS будет применён сразу, без дополнительного сетевого запроса, что ускорит отрисовку первого экрана и повысит конверсию.  
RISK: При ошибочном выборе правил может возникнуть FOUC (мигание без стилей) либо конфликт с остальными стилями при загрузке полной таблицы.  
ROLLBACK: Удалить блок `<style data-critical>` и вернуть оригинальный `<link rel="stylesheet" href="styles.css">` (git checkout index.html).  
VERIFY: Открыть страницу в DevTools → Network, отключить кэш, убедиться, что запрос к `styles.css` происходит только после `load`, а первые стили уже применены (видно в вкладке Elements → <style data-critical>).  
PRIORITY: 1 – быстрый LCP ≈ 1 секунда → значительный рост Core Web Vitals и SEO‑рейтинга.  

---  

IDEA: SKILL — faq-jsonld-generator  
KNOB: **Name:** faq-jsonld-generator  
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
EFFECT: Автоматическое добавление структурированных данных FAQPage повышает шансы появления в «People also ask» и улучшает SEO‑видимость без ручного редактирования JSON‑LD.  
RISK: Если разметка FAQ изменится, скрипт может собрать неправильный контент; требуется проверка на корректность JSON‑LD.  
ROLLBACK: Удалить вставленный `<script type="application/ld+json">` (и сам скрипт‑генератор) из `<head>` (git checkout index.html).  
VERIFY: Запустить Google Rich Results Test (https://search.google.com/test/rich-results) по локальному файлу или через сервер; убедиться, что найдено `FAQPage` со всеми вопросами.  
PRIORITY: 2 – быстрый SEO‑буст без влияния на пользовательский опыт; полезно для локального бизнеса, где вопросы часто ищут.
