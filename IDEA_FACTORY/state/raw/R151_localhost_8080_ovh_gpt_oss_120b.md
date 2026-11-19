# localhost:8080/ovh/gpt-oss-120b  2026-11-17 08:58:59
duration=39.7 error=- attempts=1

IDEA: Preconnect & dns‑prefetch for Google Fonts  
KNOB: В `<head>` добавить сразу перед текущим `<link href="https://fonts.googleapis.com/...">` две строки:  
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```  
EFFECT: Сокращает время DNS‑lookup и TLS‑handshake, ускоряя загрузку шрифтов → улучшает First Contentful Paint и общую скорость.  
RISK: Никакого, браузеры, не поддерживающие `preconnect`, просто игнорируют тег.  
ROLLBACK: Удалить добавленные строки; `git checkout index.html`.  
VERIFY: В DevTools включить throttling 3G, измерить TTFB/FCP до и после; ожидается ≈ 50‑100 мс прирост.  
PRIORITY: 2 – быстрый, низкозатратный выигрыш в производительности.  

IDEA: Gradient‑text shimmer на заголовке hero  
KNOB: В CSS добавить анимацию и стили для `.hero h1`:  
```css
.hero h1 {
  background: linear-gradient(90deg,var(--grad) 0%,#fff 50%,var(--grad) 100%);
  background-size:200%;
  -webkit-background-clip:text;
  color:transparent;
  animation:shimmer 3s infinite;
}
@keyframes shimmer{to{background-position:-200% 0;}}
```  
EFFECT: Привлекает внимание к основному офферу, повышая CTR на CTA.  
RISK: Увеличивает объём CSS ≈ 200 Б, на старых браузерах эффект просто не отобразится.  
ROLLBACK: Удалить добавленные правила; `git checkout index.html`.  
VERIFY: Открыть страницу, убед
