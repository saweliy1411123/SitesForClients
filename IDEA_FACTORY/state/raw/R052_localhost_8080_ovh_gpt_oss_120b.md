# localhost:8080/ovh/gpt-oss-120b  2026-11-17 04:09:50
duration=19.7 error=- attempts=1

IDEA: Preconnect + font‑display swap for Google Fonts  
KNOB: В <head> добавить `<link rel="preconnect" href="https://fonts.googleapis.com">` и `<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>` перед текущей ссылкой на шрифты; изменить существующий `<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap"` → `...&display=swap&text=АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyz0123456789"` (ограничить набор символов); добавить в любой пользовательский @font-face `font-display: swap;` (если используется локальный @font-face).  
EFFECT: Уменьшает время загрузки шрифтов, устраняет блокировку рендеринга, повышает LCP и CLS → быстрее отображается первый экран, улучшает SEO‑оценку.  
RISK: Необходима проверка, что ограниченный набор символов покрывает весь контент; добавление двух <link> слегка увеличит размер <head>, но без влияния на функциональность.  
ROLLBACK: Удалить новые `<link rel="preconnect">` и вернуть оригинальный URL шрифта (git checkout index.html).  
VERIFY: Открыть страницу в Chrome DevTools → Network, убедиться, что запросы к fonts.googleapis.com/… происходят после preconnect (статус 200, время < 50 мс); измерить LCP в Performance → должно снизиться минимум ≈200 мс.  
PRIORITY: 1 – высокий ROI: небольшие изменения дают заметный рост Core Web Vitals без риска для контента.  

IDEA: Accessible CTA Buttons instead of anchor‑links  
KNOB: Заменить все CTA‑ссылки вида `<a class="btn-primary …" href="#contact">…</a>` на `<button class="btn-primary" type="button" aria-label="Получить бесплатное демо">…</button>`; добавить небольшой inline‑script в конце <body>:

```html
<script>
document.querySelectorAll('.btn-primary').forEach(b=>b.addEventListener('click',e=>{
  const target=document.querySelector('#contact');
  if(target) target.scrollIntoView({behavior:'smooth'});
}));
</script>
```

Обновить CSS, если требуется `cursor:pointer;` для `<button>`.  
EFFECT: Явно сигнализирует о «действии», улучшает поддержку клавиатурной навигации и скрин‑ридеров, повышает доступность (WCAG 2.1 AA).  
RISK: Требуется небольшое JS‑взаимодействие; при отключённом JS кнопка не выполнит скролл (но сохраняет фокус и семантику).  
ROLLBACK: Вернуть оригинальные `<a>`‑элементы и удалить скрипт (git checkout index.html).  
VERIFY: В Chrome DevTools → Elements → Accessibility проверить, что элемент имеет роль button; нажать Tab, активировать клавишей Enter/Space – страница должна плавно прокрутиться к #contact.  
PRIORITY: 2 – важный шаг к соответствию доступности, средний уровень усилий, без влияния на SEO.
