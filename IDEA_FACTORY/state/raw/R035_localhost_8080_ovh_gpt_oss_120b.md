# localhost:8080/ovh/gpt-oss-120b  2026-11-17 03:21:37
duration=53.3 error=- attempts=1

IDEA: SKILL — parallax-scroll-layers  
KNOB: METHOD: SKILL  
**Name:** `parallax-scroll-layers`  
**When to apply:** На лендингах, где есть несколько визуальных слоёв (фон, иллюстрации, карточки) и требуется лёгкий глубинный эффект при прокрутке, не используя тяжёлые JS‑библиотеки.  
**Steps:**  
1. Добавить в HTML контейнер‑обёртку `data-parallax` вокруг слоёв, которым нужен эффект (например, `.bg-layer`, `.mid-layer`, `.fg-layer`).  
2. В CSS задать каждому слою начальное `transform: translateZ(0)` и `will-change: transform`.  
3. Внизу файла добавить безопасный JS, который на событии `scroll` (с `requestAnimationFrame`) считает процент прокрутки и обновляет `transform: translateY(var(--offset))` для каждого слоя, используя коэффициенты глубины (например, 0.3, 0.6, 0.9).  
4. Добавить `@media (prefers-reduced-motion: reduce)`‑правило, которое отключает скрипт (ставит `transform: none`).  

**SAFE CSS:**  
```css
[data-parallax] {
  perspective: 1000px;
  overflow: hidden;
}
[data-parallax] > .layer {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  will-change: transform;
}
.layer-bg   { --depth: 0.2; }
.layer-mid  { --depth: 0.5; }
.layer-fg   { --depth: 0.8; }
```

**SAFE JS:**  
```js
(() => {
  const layers = document.querySelectorAll('[data-parallax] .layer');
  if (!layers.length) return;
  const onScroll = () => {
    const scrollY = window.scrollY;
    layers.forEach(l => {
      const depth = parseFloat(getComputedStyle(l).getPropertyValue('--depth'));
      l.style.transform = `translateY(${scrollY * depth}px)`;
    });
  };
  const raf = () => { onScroll(); requestAnimationFrame(raf); };
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  requestAnimationFrame(raf);
})();
```  
EFFECT: Создаёт ощущение глубины и динамичности без тяжёлых библиотек, усиливая премиальный визуальный стиль и удерживая внимание посетителя.  
RISK: Малый риск «jank» на старых мобильных устройствах при высоких коэффициентах глубины; можно скорректировать коэффициенты.  
ROLLBACK: `git checkout -- index.html` (если изменения внесены в копию `index.improved.html`).  
VERIFY: Открыть страницу в браузере, включить DevTools → Performance, прокрутить и убедиться, что FPS ≥ 55 и нет «long tasks». Проверить, что при `prefers-reduced-motion` слой не движется.  
PRIORITY: 1 — Высокий визуальный и конверсионный потенциал при минимальном весе кода.  

---  

IDEA: SKILL — frosted-hero-bg  
KNOB: METHOD: SKILL  
**Name:** `frosted-hero-bg`  
**When to apply:** Для секции hero, где нужен премиальный «стеклянный» фон, подчёркивающий главный оффер и CTA, без использования PNG‑изображений.  
**Steps:**  
1. Внутри `<header class="hero">` добавить элемент `<div class="hero-frost"></div>` сразу после контент‑обёртки.  
2. Применить к нему `backdrop-filter: blur(12px) saturate(150%)` и полупрозрачный фон‑цвет.  
3. Ограничить высоту/ширину элементом `inset: 0; position: absolute; z-index: -1;` чтобы покрывать весь hero.  
4. Добавить fallback для браузеров без `backdrop-filter`: `background: rgba(10,10,15,0.85);`.  

**SAFE CSS:**  
```css
.hero {
  position: relative;
  overflow: hidden;
}
.hero-frost {
  position: absolute;
  inset: 0;
  background: rgba(10,10,15,0.6);
  backdrop-filter: blur(12px) saturate(150%);
  -webkit-backdrop-filter: blur(12px) saturate(150%);
  z-index: -1;
}
@supports not ((-webkit-backdrop-filter: blur(0)) or (backdrop-filter: blur(0))) {
  .hero-frost { background: rgba(10,10,15,0.85); }
}
```  

**SAFE JS:** *не требуется*  

EFFECT: Делает первый экран более «привлекательным» и современным, усиливает восприятие бренда как премиального, повышает читаемость текста на фоне динамичных слоёв.  
RISK: На некоторых Android‑браузерах `backdrop-filter` может замедлять отрисовку; fallback‑цвет сохраняет читаемость.  
ROLLBACK: Удалить строки `<div class="hero-frost"></div>` и соответствующий CSS‑блок.  
VERIFY: Включить/выключить `backdrop-filter` в DevTools → CSS → toggle; убедиться, что текст остаётся контрастным, а FPS ≥ 55. Проверить в Chrome, Safari и Firefox.  
PRIORITY: 2 — Улучшает визуальную премиальность без влияния на SEO/структуру, но менее критично для конверсии, чем CTA‑эффекты.  

---  

IDEA: SKILL — neon-glow-interactive  
KNOB: METHOD: SKILL  
**Name:** `neon-glow-interactive`  
**When to apply:** Для интерактивных элементов (кнопки, ссылки, карточки) на темных премиальных лендингах, где нужен мягкий световой акцент при наведении/фокусе, но без мерцания и без JavaScript.  
**Steps:**  
1. Добавить всем интерактивным элементам класс `.neon`.  
2. В CSS задать переменную `--neon-color` (по умолчанию `#4cc9f0`).  
3. Применить `box-shadow` и `filter: drop-shadow` для создания «неонового» свечения, а также `transition` для плавного появления.  
4. Добавить `:focus-visible` стиль, идентичный `:hover`, чтобы обеспечить доступность.  

**SAFE CSS:**  
```css
.neon {
  --neon-color: #4cc9f0;
  position: relative;
  color: var(--neon-color);
  text-decoration: none;
  transition: box-shadow .3s ease, filter .3s ease;
}
.neon::after {
  content: "";
  position: absolute;
  inset: -4px;
  border-radius: inherit;
  background: var(--neon-color);
  opacity: 0;
  transition: opacity .3s ease;
}
.neon:hover,
.neon:focus-visible {
  box-shadow: 0 0 12px var(--neon-color), 0 0 24px var(--neon-color);
  filter: drop-shadow(0 0 8px var(--neon-color));
}
.neon:hover::after,
.neon:focus-visible::after {
  opacity: 0.15;
}
```  

**SAFE JS:** *не требуется*  

EFFECT: Делает ссылки и кнопки более заметными на тёмном фоне, повышает восприятие «премиального» дизайна и улучшает кликабельность без навязывания.  
RISK: При слишком ярком цвете возможен визуальный дискомфорт; рекомендуется протестировать на разных дисплеях.  
ROLLBACK: Удалить класс `.neon` из HTML и CSS‑блок выше.  
VERIFY: Открыть страницу, навести курсор и переключить фокус (Tab) – проверять, что световой эффект появляется и исчезает плавно, а в `prefers-reduced-motion` он отключается (можно добавить `@media (prefers-reduced-motion: reduce) { .neon { transition: none; } }`).  
PRIORITY: 3 — Низкий порог внедрения, улучшает детали UI, но не критичен для основной конверсии.
