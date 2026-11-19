# localhost:8080/ovh/gpt-oss-120b  2026-11-17 05:28:06
duration=28.6 error=- attempts=1

IDEA: Кратко измеримый результат в hero  
KNOB: В блоке `.hero` сразу после `<h1>` добавить `<p class="hero-metric" id="hero-metric">От 10 новых заявок в месяц уже после первой недели</p>`; в CSS‑файле задать `.hero-metric{font-size:clamp(16px,2vw,20px);font-weight:600;color:var(--accent);margin-top:0.5rem}`  
EFFECT: Делает оффер осязаемым, повышая ясность предложения и повышая конверсию за счёт конкретного обещания результата.  
RISK: Обещание должно быть реалистичным — нужно согласовать цифры с владельцем, иначе возникнет недоверие.  
ROLLBACK: `git checkout index.html` (или удалить только добавленные строки).  
VERIFY: Открыть страницу в браузере, убедиться, что новый абзац виден в hero‑секции и корректно адаптируется под мобильный экран (проверить в DevTools → responsive).  
PRIORITY: 1 — самый высокий, потому что напрямую влияет на восприятие оффера и первое впечатление.  

IDEA: Schema.org Review‑разметка для отзывов  
KNOB: В секции отзывов (около L589) обернуть каждый отзыв в `<blockquote itemscope itemtype="https://schema.org/Review"><p itemprop="reviewBody">…текст отзыва…</p><footer>— <span itemprop="author">Имя Фамилия</span></footer></blockquote>`; добавить в `<head>` JSON‑LD‑скрипт:  
```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"ItemList",
  "itemListElement":[
    {"@type":"ListItem","position":1,"item":{"@type":"Review","reviewBody":"…","author":{"@type":"Person","name":"Имя"}}},
    {"@type":"ListItem","position":2,"item":{"@type":"Review","reviewBody":"…","author":{"@type":"Person","name":"Имя"}}}
  ]
}
</script>
```  
EFFECT: Увеличивает доверие через отображение rich‑snippets в поиске, улучшает SEO‑показатели и конверсию.  
RISK: Требует реальных отзывов с реальными именами; фальшивые данные могут нарушить правила поисковых систем.  
ROLLBACK: `git checkout index.html` (удалить добавленные блоки и скрипт).  
VERIFY: Запустить Google Rich Results Test по URL и убедиться, что отзывы обнаружены как Review.  
PRIORITY: 2 — средний, потому что повышает доверие, но требует точных данных.  

IDEA: Google Site Verification meta‑тег для SEO‑доверия  
KNOB: В `<head>` добавить `<meta name="google-site-verification" content="YOUR_VERIFICATION_CODE">` (заменить YOUR_VERIFICATION_CODE на реальный код из Google Search Console).  
EFFECT: Позволяет подтвердить владение сайтом в Google, улучшая индексирование и повышая доверие поисковых систем.  
RISK: Требует наличия действующего кода подтверждения; без него тег бесполезен.  
ROLLBACK: Удалить строку из `<head>` (`git checkout index.html` или вручную).  
VERIFY: После публикации открыть Google Search Console → Проверка статуса подтверждения сайта; метка должна стать «Подтверждено».  
PRIORITY: 3 — низкий, но полезный для SEO‑здоровья и доверия поисковика.
