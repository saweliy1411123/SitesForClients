# localhost:8080/ovh/gpt-oss-120b  2026-11-17 05:45:48
duration=35.2 error=- attempts=1

IDEA: Клиентский логотип‑карусель (CSS‑only, бесконечный скролл)  
KNOB: Вставить после секции «Отзывы и работы» (≈ L560) новый блок  
```html
<section class="clients" aria-label="Клиенты">
  <h2 class="reveal">Кому уже доверяют</h2>
  <div class="logo-carousel">
    <div class="logos">
      <img src="data:image/svg+xml,…" alt="Логотип 1" class="logo">
      <img src="data:image/svg+xml,…" alt="Логотип 2" class="logo">
      <img src="data:image/svg+xml,…" alt="Логотип 3" class="logo">
      <!-- повторить набор логотипов 2‑3 раза для плавного бесконечного скролла -->
    </div>
  </div>
</section>
```  
EFFECT: Добавляет визуальный социальный доказательство, повышает доверие и время на странице → рост конверсии.  
RISK: Увеличит объём HTML + CSS (≈ 5 KB); если логотипы тяжёлые – может замедлить загрузку.  
ROLLBACK: `git checkout -- index.html` (или восстановить файл из копии).  
VERIFY: Открыть страницу в браузере, включить DevTools → проверить, что логотипы плавно скользят и нет горизонтального скролла; измерить размер файла.  
PRIORITY: 2 – высокий ROI за небольшие затраты, но не критично для первого экрана.  

---  

SKILL — gradient-border-cta  
KNOB: **Name:** `gradient-border-cta`  
**When to apply:** На всех CTA‑кнопках и ссылках‑кнопках, где нужен премиальный визуальный акцент.  
**Steps:**  
1. Добавить класс `gradient-cta` к элементу `<a>`/`<button>`.  
2. Включить CSS‑правила ниже (SAFE CSS).  
3. При желании добавить небольшую JS‑поддержку для `:focus-visible` (SAFE JS).  

SAFE CSS:  
```css
.gradient-cta {
  position: relative;
  display: inline-block;
  padding: 0.75rem 1.5rem;
  color: #fff;
  background: var(--bg);
  border-radius: 0.5rem;
  overflow: hidden;
  cursor: pointer;
  text-decoration: none;
  transition: color .3s ease;
}
.gradient-cta::before {
  content: "";
  position: absolute;
  inset: -2px;
  background: linear-gradient(135deg,
    #8b5cf6,
    #4ec9f0,
    #8b5cf6);
  background-size: 200% 200%;
  border-radius: 0.6rem;
  z-index: -1;
  animation: gradient-border 4s linear infinite;
}
.gradient-cta:hover,
.gradient-cta:focus-visible {
  color: #fff;
}
@keyframes gradient-border {
  0%   {background-position: 0% 50%}
  50%  {background-position: 100% 50%}
  100% {background-position: 0% 50%}
}
```

SAFE JS (optional, для улучшения фокуса):  
```js
document.querySelectorAll('.gradient-cta').forEach(el=>{
  el.addEventListener('keydown',e=>{
    if(e.key==='Enter' || e.key===' ') el.click()
  })
})
```  

EFFECT: Пульсирующая градиентная рамка привлекает внимание, подчеркивает премиальность, повышает CTR.  
RISK: Небольшой рост CSS‑файла (~1 KB); может конфликтовать с уже существующими `background`‑стилями кнопок.  
ROLLBACK: Удалить класс `gradient-cta` и стили из проекта (`git checkout -- index.improved.html`).  
VERIFY: Открыть страницу, навести курсор/фокус на кнопку, убедиться в анимации рамки и отсутствии сдвигов layout; измерить время до First Contentful Paint (FCP) – должно оставаться < 1 s.  
PRIORITY: 1 – быстрая визуальная выгода, небольшие затраты, повышает восприятие «дорогого» продукта.  
SKILL: gradient-border-cta  

---  

SKILL — subtle-mouse-tilt-card  
KNOB: **Name:** `subtle-mouse-tilt-card`  
**When to apply:** На интерактивных карточках (цены, демо‑концепты) для создания лёгкого 3D‑эффекта при наведении курсора.  
**Steps:**  
1. Добавить к нужным карточкам класс `tilt-card`.  
2. Включить CSS‑правила ниже (SAFE CSS).  
3. Добавить минимальный JS‑скрипт, который обновляет CSS‑переменные `--tilt-x` и `--tilt-y` на движении мыши (SAFE JS).  

SAFE CSS:  
```css
.tilt-card {
  perspective: 800px;
  transform-style: preserve-3d;
  transition: transform .2s ease-out;
}
.tilt-card:hover {
  transform:
    rotateX(var(--tilt-y, 0deg))
    rotateY(var(--tilt-x, 0deg));
}
```

SAFE JS:  
```js
document.querySelectorAll('.tilt-card').forEach(card=>{
  card.addEventListener('mousemove',e=>{
    const rect = card.getBoundingClientRect();
    const x = ((e.clientX - rect.left)/rect.width - 0.5)*10; // ±5deg
    const y = ((e.clientY - rect.top)/rect.height - 0.5)*10;
    card.style.setProperty('--tilt-x', `${x}deg`);
    card.style.setProperty('--tilt-y', `${-y}deg`);
  });
  card.addEventListener('mouseleave',()=> {
    card.style.removeProperty('--tilt-x');
    card.style.removeProperty('--tilt-y');
  });
});
```  

EFFECT: При наведении карточка слегка наклоняется, создавая ощущение глубины и «премиальности», удерживает взгляд пользователя.  
RISK: На мобильных устройствах эффект не нужен – может вызвать лишние вычисления; JS небольшого объёма, но требует `requestAnimationFrame`‑оптимизации при большом числе карточек.  
ROLLBACK: Удалить класс `tilt-card` и подключённый скрипт (`git checkout -- index.improved.html`).  
VERIFY: На десктопе открыть страницу, наведя курсор на любую карточку с классом – наблюдать плавный наклон без рывков; проверить, что на мобильном устройстве эффект отключён (нет `mousemove`).  
PRIORITY: 2 – повышает визуальную ценность, но требует тестирования на всех устройствах.  
SKILL: subtle-mouse-tilt-card
