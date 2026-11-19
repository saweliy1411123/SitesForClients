# localhost:8080/ovh/gpt-oss-120b  2026-11-17 06:24:24
duration=21.7 error=- attempts=1

IDEA: SKILL — gradient‑text‑hero  
KNOB: **Name:** `gradient-text-hero`  
**When to apply:** На любой статический лендинг с крупным заголовком в hero‑секции, где нужен визуальный акцент без добавления изображений.  
**Steps:**  
1. Добавить класс `gradient-text` к элементу `<h1>` (или другому блоку, требующему акцента).  
2. Включить CSS‑правило из `SAFE CSS` ниже в глобальный `<style>` либо в отдельный файл стилей.  
3. При желании задать индивидуальный градиент через CSS‑переменную `--gradient`.  
4. (Опционально) Добавить небольшую анимацию плавного смещения градиента через `SAFE CSS`.  

**SAFE CSS:**  
```css
/* gradient‑text‑hero */
.gradient-text {
  --gradient: linear-gradient(90deg, #8b5cf6, #3b82f6, #10b981, #f59e0b);
  background: var(--gradient);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  display: inline-block;
  animation: gradient-slide 8s linear infinite;
}

/* плавный сдвиг градиента */
@keyframes gradient-slide {
  0%   { background-position: 0% 50%; }
  50%  { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* адаптивность – отключаем анимацию на слабых устройствах */
@media (prefers-reduced-motion: reduce) {
  .gradient-text { animation: none; }
}
```  

**SAFE JS:** *(необязательно – только если нужен контроль над включением/выключением анимации)*  
```js
// отключить анимацию, если пользователь предпочитает reduced‑motion
if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  document.querySelectorAll('.gradient-text').forEach(el => {
    el.style.animation = 'none';
  });
}
```  

---  

IDEA: SKILL — scroll‑triggered‑counter  
KNOB: **Name:** `scroll-triggered-counter`  
**When to apply:** На лендингах, где в секциях (например, «Боль», «Доказательства», «Отзывов») присутствуют статистические цифры, которые должны «оживить» пользователя при прокрутке.  
**Steps:**  
1. Обернуть каждое число в элемент с классом `counter` и атрибутом `data-target` — целевое значение (например, `<span class="counter" data-target="124">0</span>`).  
2. Вставить ниже CSS‑правило из `SAFE CSS` в глобальный стиль.  
3. Добавить JavaScript‑блок из `SAFE JS` в конец `<body>` (или в отдельный файл). Скрипт использует `IntersectionObserver` и анимирует счётчик от 0 до `data-target` за 1.5 сек.  

**SAFE CSS:**  
```css
/* scroll‑triggered‑counter */
.counter {
  font-weight: 700;
  font-size: clamp(30px,4vw,46px);
  line-height: 1.05;
  display: inline-block;
}
```  

**SAFE JS:**  
```js
// scroll‑triggered‑counter
(() => {
  const formatNumber = n => Math.floor(n).toLocaleString('ru-RU');

  const animate = (el, target) => {
    const duration = 1500;
    const start = performance.now();
    const step = now => {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      el.textContent = formatNumber(progress * target);
      if (progress < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = +el.dataset.target;
        animate(el, target);
        obs.unobserve(el);
      }
    });
  }, {threshold: 0.6});

  document.querySelectorAll('.counter[data-target]').forEach(el => observer.observe(el));
})();
```  

---  

PRIORITY: 1 – оба скилла дают мгновенный визуальный рост восприятия (градиентный текст усиливает бренд‑идентичность, а анимированные цифры повышают доверие и удержание). Их внедрение требует только добавления CSS/JS без изменения структуры сайта и без серверных зависимостей.  

ROLLBACK: `git checkout -- index.html` (или удалить добавленные файлы/строки).  

VERIFY:  
1. Открыть страницу в браузере, убедиться, что заголовок с классом `gradient-text` отображает плавный градиент и анимацию (можно временно отключить через DevTools → `animation: none`).  
2. Прокрутить до элемента с классом `counter`; убедиться, что цифра плавно считает от 0 до целевого значения и останавливается.  

SKILL: gradient‑text‑hero  
SKILL: scroll‑triggered‑counter
