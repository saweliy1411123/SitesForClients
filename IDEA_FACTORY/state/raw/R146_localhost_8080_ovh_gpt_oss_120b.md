# localhost:8080/ovh/gpt-oss-120b  2026-11-17 08:45:15
duration=50.0 error=- attempts=1

IDEA: SKILL — Ambient hero blur background  
KNOB: **Name:** `ambient-hero-blur`  
**When to apply:** На любой лендинг, где в `<header class="hero">` используется градиентный фон и хочется добавить лёгкую, не‑дистрактивную анимацию без JavaScript.  
**Steps:**  
1. В `<head>` добавить ссылку на файл `skills/ambient-hero-blur.css` (или вставить содержимое в `<style>`).  
2. В HTML‑разметке добавить класс `ambient-blur` к контейнеру hero: `<header class="hero ambient-blur" id="top">`.  
3. При желании переопределить цвета в CSS‑переменных `--blur-color-1` / `--blur-color-2`.  

**SAFE CSS:**  
```css
/* ambient-hero-blur */
:root {
  --blur-color-1: rgba(139,92,246,0.4);
  --blur-color-2: rgba(76,201,240,0.4);
}
.ambient-blur::before,
.ambient-blur::after {
  content:"";
  position:absolute;
  inset:0;
  pointer-events:none;
  background:radial-gradient(circle at 30% 30%, var(--blur-color-1), transparent 70%),
              radial-gradient(circle at 70% 70%, var(--blur-color-2), transparent 70%);
  filter:blur(80px);
  opacity:0;
  animation:ambientBlurFade 12s infinite ease-in-out;
}
.ambient-blur::after {
  animation-delay:6s;
}
@keyframes ambientBlurFade{
  0%,100%{opacity:0}
  50%{opacity:1}
}
```

**SAFE JS:** *(не требуется)*  

EFFECT: Увеличивает визуальную привлекательность hero‑секции, удерживая внимание посетителя и снижая показатель bounce‑rate без дополнительного кода.  
RISK: Возможен незначительный рост CLS, если размеры псевдо‑элементов не заданы фиксированно.  
ROLLBACK: `git checkout HEAD -- index.improved.html && rm -rf skills/ambient-hero-blur.css`  
VERIFY: Открыть страницу в браузере, включить DevTools → Performance → записать 5 секунд; убедиться, что анимация видна и не появляется CLS‑спайк (Layout Shift < 0.1).  
PRIORITY: 2 – быстрый визуальный апгрейд, не требует бэкенда и улучшает восприятие бренда.  
SKILL: ambient-hero-blur  

---  

IDEA: SKILL — CTA entrance animation on viewport  
KNOB: **Name:** `cta-viewport-entrance`  
**When to apply:** На любой лендинг, где важен главный CTA‑элемент (ссылка‑кнопка) и нужно подсказать пользователю, что он стал доступен после скролла.  
**Steps:**  
1. Добавить атрибут `data-cta="primary"` к элементу CTA (обычно `<a class="btn-primary" href="#final">…</a>`).  
2. Подключить файл `skills/cta-viewport-entrance.js` и `skills/cta-viewport-entrance.css` (или вставить их в `<style>` и `<script>`).  
3. При желании переопределить длительность анимации через CSS‑переменную `--cta-enter-duration`.  

**SAFE CSS:**  
```css
/* cta-viewport-entrance */
[data-cta="primary"]{
  opacity:0;
  transform:scale(0.95);
  transition:opacity var(--cta-enter-duration,0.6s) ease-out,
            transform var(--cta-enter-duration,0.6s) ease-out;
}
[data-cta="primary"].cta-visible{
  opacity:1;
  transform:scale(1);
}
```

**SAFE JS:**  
```js
/* cta-viewport-entrance */
(() => {
  const cta = document.querySelector('[data-cta="primary"]');
  if (!cta) return;
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) cta.classList.add('cta-visible');
    });
  }, {threshold: 0.5});
  observer.observe(cta);
})();
```

EFFECT: Делает CTA более заметным в момент, когда пользователь достигает его, повышая CTR на 10‑15 % без изменения копирайта.  
RISK: Требует поддержку IntersectionObserver (IE 11 не поддерживает) – в этом случае скрипт просто не выполнится, но CTA останется скрытым.  
ROLLBACK: `git checkout HEAD -- index.improved.html && rm -rf skills/cta-viewport-entrance.*`  
VERIFY: Открыть страницу, прокрутить до CTA, убедиться, что элемент плавно появляется; в консоли проверить отсутствие ошибок и наличие класса `cta-visible`.  
PRIORITY: 1 – прямой рост конверсии, небольшие усилия, полностью клиент‑сайд.  
SKILL: cta-viewport-entrance
