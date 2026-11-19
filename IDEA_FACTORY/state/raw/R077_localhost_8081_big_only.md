# localhost:8081/big_only  2026-11-17 05:25:12
duration=19.6 error=- attempts=1

IDEA: Premium gradient sweep on hero heading  
KNOB: **SKILL — premium-hero-gradient-sweep**  
**Name:** `premium-hero-gradient-sweep`  
**When to apply:** На главном hero‑заголовке, где нужен премиальный визуальный акцент.  
**SAFE CSS:**  
```css
.hero h1 {
  position: relative;
  overflow: hidden;
  color: transparent;
  -webkit-background-clip: text;
  background-clip: text;
  background-image: linear-gradient(120deg, var(--blue) 30%, var(--purple) 70%);
  background-size: 200% 100%;
  animation: gradient-sweep 4s ease-in-out infinite;
}
@keyframes gradient-sweep {
  0%   { background-position: 200% 0; }
  50%  { background-position: 0 0; }
  100% { background-position: 200% 0; }
}
```
**SAFE JS:** *(не требуется)*  
EFFECT: Привлекает внимание к главному офферу, усиливает ощущение премиальности и повышает время‑взгляда (dwell time).  
RISK: Может конфликтовать с пользовательскими темными/светлыми темами, если переменные `--blue`/`--purple` переопределены.  
ROLLBACK: `git checkout HEAD -- index.html` (или откатить изменения в файле стилей).  
VERIFY: Открыть страницу, убедиться, что заголовок анимирован плавным градиентом, измерить время до полной отрисовки в Chrome DevTools → Performance (не должно превышать 100 ms).  
PRIORITY: 1 – высокий визуальный ROI при минимальном коде.  
SKILL: premium-hero-gradient-sweep  

---  

IDEA: 3D‑tilt glass‑morphism для карточек цены  
KNOB: **SKILL — tilt-glass-price-card**  
**Name:** `tilt-glass-price-card`  
**When to apply:** На блоках `.price-card` в секции цены, где нужен премиальный 3‑D‑эффект и стеклянный вид.  
**SAFE CSS:**  
```css
.price-card {
  perspective: 800px;
  background: rgba(255,255,255,0.07);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255,255,255,0.2);
  transform-style: preserve-3d;
  transition: transform 0.35s ease, box-shadow 0.35s ease;
}
.price-card:hover,
.price-card:focus-visible {
  transform: rotateY(8deg) rotateX(4deg) translateZ(20px);
  box-shadow: 0 12px 30px rgba(0,0,0,0.25);
}
.price-card::before {
  content:"";
  position:absolute;
  inset:0;
  border-radius:inherit;
  background: linear-gradient(135deg, rgba(255,255,255,0.15), transparent);
  pointer-events:none;
}
```
**SAFE JS:** *(не требуется)*  
EFFECT: Делает цену более «осязаемой», повышает доверие и запоминаемость предложения, усиливает восприятие премиального бренда.  
RISK: На слабых устройствах (мобильные старые) может возникнуть небольшое падение FPS; требуется тестировать на low‑end.  
ROLLBACK: `git checkout HEAD -- index.html` (откатить изменения в `.price-card` стили).  
VERIFY: Открыть страницу на десктопе и мобильном, проверить плавность анимации (Chrome DevTools → Rendering → FPS > 55).  
PRIORITY: 2 – хороший визуальный эффект, но требует проверки производительности.  
SKILL: tilt-glass-price-card  

---  

IDEA: Typed‑out подзаголовок в hero‑секции  
KNOB: **SKILL — hero-typed-subtitle**  
**Name:** `hero-typed-subtitle`  
**When to apply:** В hero‑блоке после `<p class="sub">`, где хочется добавить динамичность без тяжёлых библиотек.  
**SAFE CSS:**  
```css
.hero .typed-subtitle {
  display:inline-block;
  border-right:2px solid currentColor;
  white-space:nowrap;
  overflow:hidden;
  font-family:inherit;
  font-size:inherit;
  animation: caret-blink 0.7s steps(1) infinite;
}
@keyframes caret-blink {
  0%,100% { border-color:transparent; }
  50% { border-color:currentColor; }
}
```
**SAFE JS:**  
```js
(() => {
  const txt = "Получите первых клиентов из Яндекса за 2 дня";
  const el = document.querySelector('.hero .typed-subtitle');
  if (!el) return;
  let i = 0;
  const interval = setInterval(() => {
    el.textContent = txt.slice(0, ++i);
    if (i === txt.length) clearInterval(interval);
  }, 60);
})();
```
EFFECT: Добавляет живой элемент, удерживает внимание, повышает воспринимаемую динамичность предложения.  
RISK: Если JavaScript отключён, текст останется пустым – необходимо предусмотреть fallback‑текст.  
ROLLBACK: Удалить вставку `<p class="typed-subtitle">` и скрипт; `git checkout HEAD -- index.html`.  
VERIFY: Отключить JS в браузере → убедиться, что отображается статический fallback‑текст; включить → проверить корректность печати без задержек > 200 ms.  
PRIORITY: 3 – умеренный конверсионный эффект, легко реализуется, но требует небольшого JS.  
SKILL: hero-typed-subtitle
