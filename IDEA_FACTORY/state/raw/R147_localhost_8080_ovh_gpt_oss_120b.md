# localhost:8080/ovh/gpt-oss-120b  2026-11-17 08:47:40
duration=27.1 error=- attempts=1

IDEA: SKILL — glassmorphic‑card‑hover  
KNOB: SKILL: **Name:** `glassmorphic-card-hover`  
**When to apply:** На любых «карточных» блоках (price‑card, step‑card, отзыв) для придания премиального «стеклянного» эффекта при наведении.  
**Steps:** 1️⃣ Добавить класс `card-glass` к нужным элементам. 2️⃣ Включить ниже‑приведённый CSS в общий файл стилей.  
SAFE CSS:  
```css
.card-glass{
  background:rgba(255,255,255,0.12);
  border:1px solid rgba(255,255,255,0.2);
  backdrop-filter:blur(8px);
  transition:transform .3s ease,box-shadow .3s ease;
}
.card-glass:hover,
.card-glass:focus-visible{
  transform:translateY(-6px) scale(1.02);
  box-shadow:0 12px 30px rgba(0,0,0,0.2);
}
```  
EFFECT: Увеличивает восприятие «роскоши» и выделяет ключевые предложения, повышая конверсию CTA.  
RISK: `backdrop-filter` не поддерживается в старых версиях IE/Edge; в этих браузерах эффект будет отсутствовать.  
ROLLBACK: Удалить класс `card-glass` или закомментировать блок CSS.  
VERIFY: Открыть страницу, навести курсор на цену/шаг‑карточку – должен появиться лёгкий подъём и размытие фона; протестировать в Chrome/Firefox.  
PRIORITY: 2 – высокий визуальный эффект, минимальный код, риски ограничены старыми браузерами.  

---  

IDEA: SKILL — gradient‑border‑cta  
KNOB: SKILL: **Name:** `gradient-border-cta`  
**When to apply:** К любой ссылке‑кнопке с классом `.btn-primary` (главный CTA) для создания анимированной градиентной рамки.  
**Steps:** 1️⃣ Заменить класс `.btn-primary` на `btn-gradient-border` (или добавить оба). 2️⃣ Добавить CSS ниже.  
SAFE CSS:  
```css
.btn-gradient-border{
  position:relative;
  overflow:hidden;
  border:2px solid transparent;
  background:var(--bg);
  color:var(--blue);
  transition:color .3s;
}
.btn-gradient-border::before{
  content:"";
  position:absolute;
  inset:-2px;
  background:linear-gradient(45deg,var(--grad-start),var(--grad-end));
  z-index:-1;
  transition:transform .4s;
  transform:scaleX(0);
  transform-origin:left;
}
.btn-gradient-border:hover::before,
.btn-gradient-border:focus-visible::before{
  transform:scaleX(1);
}
.btn-gradient-border:hover,
.btn-gradient-border:focus-visible{
  color:#fff;
}
```  
EFFECT: Динамичная градиентная рамка привлекает внимание к CTA, усиливает ощущение «дорогого» дизайна и повышает кликабельность.  
RISK: При слишком малой контрастности текста может снижаться читаемость; требуется проверить контраст.  
ROLLBACK: Убрать класс `btn-gradient-border` или закомментировать CSS‑блок.  
VERIFY: Навести курсор на кнопку – градиентная рамка должна «заполняться» слева направо; проверить, что текст остаётся читаемым.  
PRIORITY: 2 – мощный визуальный триггер, простая реализация, низкий риск.  

---  

IDEA: SKILL — scroll‑parallax‑layer  
KNOB: SKILL: **Name:** `scroll-parallax-layer`  
**When to apply:** К декоративным элементам в секции hero (blobs, фоновые SVG) и к любым фоновым блокам, где нужен лёгкий параллакс при прокрутке.  
**Steps:** 1️⃣ Добавить атрибут `data-speed="0.3"` (значение 0–1) к каждому элементу. 2️⃣ Добавить класс `parallax-layer`. 3️⃣ Включить CSS и небольшой JS‑скрипт ниже.  
SAFE CSS:  
```css
.parallax-layer{
  will-change:transform;
}
```  
SAFE JS:  
```js
document.addEventListener('scroll',()=>{
  const y = window.scrollY;
  document.querySelectorAll('.parallax-layer').forEach(el=>{
    const s = parseFloat(el.dataset.speed)||0.5;
    el.style.transform=`translateY(${y*s}px)`;
  });
});
```  
EFFECT: Создаёт ощущение глубины и динамики без тяжёлых библиотек, усиливая премиальный «живой» образ сайта.  
RISK: JS‑скрипт добавляет небольшую нагрузку; на очень медленных устройствах может возникнуть лёгкое дрожание.  
ROLLBACK: Удалить атрибут `data-speed`/класс `parallax-layer` и скрипт из проекта.  
VERIFY: Прокрутить страницу; декоративные элементы должны медленно смещаться относительно скролла; проверить плавность в Chrome DevTools → Performance.  
PRIORITY: 3 – увеличивает восприятие «современности», но требует небольшого JS‑влияния; стоит после реализации более критичных улучшений.
