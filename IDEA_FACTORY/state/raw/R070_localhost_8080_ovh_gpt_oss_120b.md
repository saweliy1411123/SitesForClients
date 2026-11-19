# localhost:8080/ovh/gpt-oss-120b  2026-11-17 05:04:59
duration=40.0 error=- attempts=1

IDEA: SKILL — Variable Font‑Weight Hover  
KNOB: METHOD: SKILL  
**Name:** variable-font-weight-hover  
**When to apply:** На всех заголовках h1‑h3 на премиальных лендингах, где нужен интерактивный типографический акцент без JavaScript.  
**Steps:**  
1. В `:root` объявить CSS‑переменную `--h-weight` со значением `500`.  
2. Добавить к заголовкам правило `font-weight: var(--h-weight); transition: font-weight 0.25s ease;`.  
3. В `:hover, :focus-visible` установить `--h-weight: 700;`.  
4. При отсутствии поддержки `transition` для `font-weight` (IE) будет обычный переход без анимации – приемлемо.  
SAFE CSS:  
```css
:root{--h-weight:500}
h1,h2,h3{font-weight:var(--h-weight);transition:font-weight .25s ease}
h1:hover,h1:focus-visible,
h2:hover,h2:focus-visible,
h3:hover,h3:focus-visible{--h-weight:700}
```  
SAFE JS: *(не требуется)*  
EFFECT: Делает заголовки более «живыми», усиливает восприятие премиального бренда и повышает CTR на CTA, расположенные рядом.  
RISK: На старых браузерах (IE 11) переход `font-weight` не анимируется – будет мгновенное изменение, но визуально не ухудшит.  
ROLLBACK: `git checkout -- index.improved.html` или удалить файл `skills/variable-font-weight-hover.md` и соответствующий импорт из `index.improved.html`.  
VERIFY: Открыть страницу в Chrome/Firefox, навести курсор на любой h1‑h3 – вес шрифта должен плавно перейти 500 → 700 за ≈ 0.25 с; проверить отсутствие JS‑ошибок в консоли.  
PRIORITY: 1 – быстрый, лёгкий апдейт, заметный визуальный эффект, без риска для SEO.  
SKILL: variable-font-weight-hover  

---  

IDEA: SKILL — Parallax Scroll‑Zoom Background  
KNOB: METHOD: SKILL  
**Name:** parallax-scroll-zoom  
**When to apply:** На секциях с крупным фон‑изображением (например, `.hero`) где нужен лёгкий глубинный эффект без внешних библиотек.  
**Steps:**  
1. Добавить к секции атрибут `data-bg="url(...)"` (заменить текущий `background-image`).  
2. В `<style>` задать начальное состояние `background-size: 100%; background-position: center;`.  
3. Подключить небольшой безопасный JS‑скрипт, использующий `IntersectionObserver` и `requestAnimationFrame` для изменения `background-size` от `100%` до `115%` по мере прокрутки.  
SAFE CSS:  
```css
.parallax-zoom{background-image:var(--bg);background-size:100%;background-position:center;transition:background-size .3s ease-out}
```  
SAFE JS:  
```js
document.querySelectorAll('.parallax-zoom').forEach(el=>{
  const img=el.dataset.bg;el.style.setProperty('--bg',`url(${img})`);
  const onScroll=()=>{const rect=el.getBoundingClientRect();const perc=1-Math.min(Math.max(rect.top/window.innerHeight,0),1);
    el.style.backgroundSize=100+15*perc+'%'}
  window.addEventListener('scroll',()=>requestAnimationFrame(onScroll));
});
```  
EFFECT: Создаёт ощущение глубины и «живости» при скролле, усиливает премиальный визуальный стиль и удерживает внимание пользователя.  
RISK: При очень медленных устройствах небольшая нагрузка от `requestAnimationFrame`; ограничено только несколькими секциями, риск минимален.  
ROLLBACK: Удалить файл `skills/parallax-scroll-zoom.md` и убрать импорт из `index.improved.html`.  
VERIFY: Открыть страницу, пролистать вниз – фон секции `.hero` должен плавно увеличиваться от 100% до 115% по мере прокрутки; проверить отсутствие «jank» в DevTools Performance.  
PRIORITY: 2 – повышает визуальную «дороговизну», но требует небольшого JS‑кода; стоит после базовых типографических улучшений.  
SKILL: parallax-scroll-zoom  

---  

IDEA: SKILL — Gradient Underline Hover for Section Headings  
KNOB: METHOD: SKILL  
**Name:** gradient-underline-hover  
**When to apply:** На заголовках h2 внутри секций, где требуется акцентировать название (например, «Три шага», «Цена», «FAQ»).  
**Steps:**  
1. Добавить к h2 класс `.underline-anim`.  
2. В CSS создать псевдо‑элемент `::after` с градиентным `background-image`.  
3. При `:hover`/`:focus-visible` анимировать `transform:scaleX(1)` от `scaleX(0)`.  
SAFE CSS:  
```css
h2.underline-anim{position:relative;overflow:hidden}
h2.underline-anim::after{
  content:"";position:absolute;bottom:0;left:0;height:3px;width:100%;
  background:linear-gradient(90deg,var(--blue),var(--purple));
  transform:scaleX(0);transform-origin:left;transition:transform .35s ease
}
h2.underline-anim:hover::after,
h2.underline-anim:focus-visible::after{transform:scaleX(1)}
```  
SAFE JS: *(не требуется)*  
EFFECT: При наведении/фокусе под заголовком появляется яркая градиентная линия, подчёркивающая важность секции и усиливающая восприятие «премиального» дизайна.  
RISK: Нет; только визуальное изменение, не влияет на SEO или доступность.  
ROLLBACK: Удалить класс `.underline-anim` из HTML и CSS‑правила из `index.improved.html` или откатить `git checkout -- index.improved.html`.  
VERIFY: Открыть страницу, навести курсор на любой h2 с классом `.underline-anim` – должна появиться плавно анимированная градиентная линия; проверить доступность через клавиатуру (Tab → focus).  
PRIORITY: 2 – быстрый визуальный апгрейд, улучшает восприятие структуры без нагрузки.  
SKILL: gradient-underline-hover
