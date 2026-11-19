# localhost:8080/ovh/gpt-oss-120b  2026-11-17 08:19:40
duration=24.1 error=- attempts=1

IDEA: Preconnect & DNS‑prefetch для Google Fonts  
KNOB: В `<head>` добавить строки  
```html
<link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
<link rel="dns-prefetch" href="https://fonts.gstatic.com">
```  
EFFECT: Уменьшит время первого рендера текста, улучшит LCP и восприятие скорости.  
RISK: Никакого (только небольшое увеличение HEAD).  
ROLLBACK: `git checkout -- index.html` (или удалить добавленные строки).  
VERIFY: Открыть DevTools → Network, убедиться, что запросы к fonts.googleapis.com идут без предварительного DNS‑lookup.  
PRIORITY: 1 – быстрая выгода для Core Web Vitals без кода‑изменений.  

IDEA: Явные ARIA‑метки и role для CTA‑ссылок  
KNOB: Для всех ссылок‑кнопок (класс `.btn-primary` и `.cta-row a`) добавить атрибуты `role="button"` и `aria-label="Получить бесплатное демо"` (или соответствующий текст).  
EFFECT: Повысит доступность для скрин‑ридеров, улучшит SEO‑оценку accessibility.  
RISK: Нужна точная формулировка aria‑label, иначе может вводить в заблуждение.  
ROLLBACK: `git checkout -- index.html` (удалить добавленные атрибуты).  
VERIFY: В консоли `document.querySelectorAll('a.btn-primary').forEach(a=>console.log(a.getAttribute('aria-label')))` → все ссылки имеют не‑пустой aria‑label.  
PRIORITY: 1 – критично для a11y, небольшие изменения.  

IDEA: Блок доверительных знаков под ценой  
KNOB: Внутри `.price-card` после списка `<ul>` вставить:  
```html
<div class="trust-badges">
  <span class="badge">30‑дневная гарантия</span>
  <span class="badge">Оплата через Яндекс.Деньги</span>
  <span class="badge">Без скрытых комиссий</span>
</div>
```  
и в CSS добавить простую стилизацию `.trust-badges {display:flex;gap:12px;justify:center;margin-top:12px;} .badge{background:#f3f4f6;padding:4px 8px;border-radius:4px;font-size:13px;}`  
EFFECT: Снимает возражения о риске покупки, повышает конверсию цены.  
RISK: Нужно убедиться, что заявления правдивы (владельцу).  
ROLLBACK: `git checkout -- index.html` (удалить вставку).  
VERIFY: В браузере увидеть новые бейджи, проверить, что они не ломают верстку на мобильных (DevTools → responsive).  
PRIORITY: 2 – повышает доверие, но требует согласования текста.  

IDEA: Интерактивный карусель‑демо с клавиатурной навигацией  
KNOB: Обернуть каждый демо‑элемент в `<div class="demo-item" tabindex="0">…</div>` и добавить простой JS‑скрипт (≈30 строк) для горизонтального скролла по стрелкам ←/→ и кнопкам «prev/next».  
EFFECT: Пользователи могут просматривать больше концептов без прокрутки, повышает вовлечённость.  
RISK: Требует небольшого JS, может конфликтовать с существующим скриптом (проверить).  
ROLLBACK: Удалить добавленные `<div>` и скрипт, `git checkout -- index.html`.  
VERIFY: На странице нажать стрелки, убедиться, что фокус переходит между элементами, проверить в мобильном – свайп работает.  
PRIORITY: 2 – улучшает UX, но добавляет небольшой код.  

IDEA: Анимированные цифры‑шаги в секции «Три шага»  
KNOB: Внутри каждого блока шага добавить `<span class="step-number">01</span>` и в CSS:  
```css
.step-number{font-weight:700;font-size:2rem;opacity:0;transform:translateY(10px);
  animation: stepFade 0.6s forwards; animation-delay:calc(var(--i)*0.2s);}
@keyframes stepFade{to{opacity:1;transform:none;}}
```  
где `--i` задаётся в HTML (`style="--i:0"` и т.д.).  
EFFECT: Визуально подчёркивает порядок, делает секцию более динамичной, повышает запоминание.  
RISK: Нужно корректно задать индексы, иначе анимация будет одинаковой.  
ROLLBACK: Удалить добавленные `<span>` и CSS‑правила, `git checkout -- index.html`.  
VERIFY: Перезагрузить страницу, убедиться, что цифры появляются с задержкой.  
PRIORITY: 3 – эстетическое улучшение, низкий бизнес‑эффект.  

IDEA: Фоновое видео‑заставка в hero (muted, loop, fallback)  
KNOB: Внутри `<header class="hero">` добавить:  
```html
<video class="hero-bg-video" autoplay muted loop playsinline poster="hero-poster.jpg">
  <source src="hero.mp4" type="video/mp4">
</video>
```  
и в CSS:  
```css
.hero-bg-video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-1;}
```  
EFFECT: Делает первый экран более живым, повышает время на странице и восприятие качества.  
RISK: Увеличит размер загрузки (нужен компрессированный mp4 ≈ 200 KB), может замедлить LCP на медленных соединениях.  
ROLLBACK: Удалить `<video>`‑элемент и CSS‑правило, `git checkout -- index.html`.  
VERIFY: Открыть страницу, убедиться, что видео воспроизводится без звука, проверить в DevTools → Network размер загрузки.  
PRIORITY: 3 – визуальная «блеск»‑фича, но потенциально ухудшит скорость; ставим ниже.  

IDEA: Канонический URL в head для SEO  
KNOB: В `<head>` добавить  
```html
<link rel="canonical" href="https://example.com/">
```  
(заменить на реальный домен).  
EFFECT: Уменьшит риск дублирования контента, поможет поисковикам правильно индексировать страницу.  
RISK: Нужно убедиться, что URL действительно каноничен; иначе может навредить.  
ROLLBACK: Удалить строку, `git checkout -- index.html`.  
VERIFY: В Chrome DevTools → Elements искать `<link rel="canonical">`, убедиться, что href корректен.  
PRIORITY: 1 – важный SEO‑элемент, простая правка.
