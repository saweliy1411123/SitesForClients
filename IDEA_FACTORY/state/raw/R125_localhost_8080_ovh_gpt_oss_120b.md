# localhost:8080/ovh/gpt-oss-120b  2026-11-17 07:45:25
duration=24.6 error=- attempts=1

IDEA: SKILL — scroll-progress-indicator  
KNOB: **Name:** `scroll-progress-indicator`  
**When to apply:** На любой одностраничной статической посадочной странице, где важно визуально подсказать пользователю, сколько контента осталось, повысить вовлечённость и удержание.  
**Steps:**  
1. В начало `<body>` добавить элемент `<div class="scroll-progress"></div>`.  
2. В CSS‑файл (или в `<style>`) вставить правила из `SAFE CSS` ниже.  
3. В конец `<body>` добавить скрипт из `SAFE JS` ниже (можно разместить в отдельном файле `scroll-progress.js`).  
4. Проверить, что переменная `--grad` уже объявлена (используется в проекте). При её отсутствии добавить `--grad: #8b5cf6;`.  

**SAFE CSS:**  
```css
.scroll-progress{
  position:fixed;
  top:0;
  left:0;
  height:4px;
  width:0;
  background:var(--grad);
  z-index:9999;
  transition:width .1s linear;
}
```  

**SAFE JS:**  
```js
(() => {
  const bar = document.querySelector('.scroll-progress');
  if (!bar) return;
  const doc = document.documentElement;
  const set = () => {
    const scroll = doc.scrollTop || document.body.scrollTop;
    const height = doc.scrollHeight - doc.clientHeight;
    const perc = (scroll / height) * 100;
    bar.style.width = perc + '%';
  };
  let ticking = false;
  window.addEventListener('scroll', () => {
    if (!ticking) {
      window.requestAnimationFrame(() => {
        set();
        ticking = false;
      });
      ticking = true;
    }
  });
  set(); // init on load
})();
```  

EFFECT: Пользователь сразу видит прогресс чтения, что повышает восприятие «продуманного» сайта и может увеличить время на странице → рост конверсии на CTA.  
RISK: Минимальный; небольшое увеличение количества запросов к JavaScript (меньше 1 KB).  
ROLLBACK: `git checkout -- index.html` (или удалить добавленный `<div>` и строки CSS/JS).  
VERIFY: Открыть страницу в браузере, прокрутить вниз – индикатор должен плавно заполняться от 0 % до 100 %; проверить отсутствие ошибок в консоли.  
PRIORITY: 1 – быстрый, безопасный апдейт, сразу даёт визуальный сигнал пользователю и улучшает метрики вовлечённости.  

---  

IDEA: SKILL — focus-visible-gradient-ring  
KNOB: **Name:** `focus-visible-gradient-ring`  
**When to apply:** На любой лендинге, где есть интерактивные ссылки, кнопки и элементы‑сводки (`<summary>`), чтобы улучшить доступность и добавить премиальный визуальный акцент при клавиатурной навигации.  
**Steps:**  
1. Убедиться, что в корневом `:root` объявлена переменная `--grad` (используется в проекте).  
2. В CSS‑файл (или в `<style>`) добавить правила из `SAFE CSS` ниже.  
3. При желании, в конец `<body>` можно добавить небольшой скрипт из `SAFE JS` (необязательно) для поддержки старых браузеров, не поддерживающих `:focus-visible`.  

**SAFE CSS:**  
```css
a:focus-visible,
button:focus-visible,
summary:focus-visible{
  outline:none;
  box-shadow:0 0 0 3px var(--grad);
  border-radius:4px;
  transition:box-shadow .2s ease-in-out;
}
```  

**SAFE JS (optional):**  
```js
(() => {
  const style = document.createElement('style');
  style.textContent = 'a:focus,button:focus,summary:focus{outline:none;box-shadow:0 0 0 3px var(--grad);border-radius:4px;}';
  document.head.appendChild(style);
})();
```  

EFFECT: Ясный визуальный индикатор фокуса повышает доступность (WCAG 2.1 AA) и усиливает восприятие бренда как «премиального». Это может увеличить конверсию за счёт снижения количества «потерянных» пользователей, навигирующих клавиатурой.  
RISK: Возможен конфликт с уже существующими кастомными `:focus`‑стилями; в этом случае потребуется уточнить селекторы.  
ROLLBACK: `git checkout -- index.html` (удалить добавленные CSS‑правила/JS‑блок).  
VERIFY: Открыть страницу, перейти к любой ссылке/кнопке с помощью клавиши Tab – вокруг элемента должен появиться градиентный светящийся контур; убедиться, что контур исчезает при потере фокуса и нет ошибок в консоли.  
PRIORITY: 2 – улучшение доступности и визуального восприятия, требует лишь небольших изменений в CSS, но даёт ощутимый прирост доверия и соответствия требованиям WCAG.
