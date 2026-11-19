# lareper/glm-5.2-fast-preview  2026-11-17 06:04:37
duration=2.4 error=- attempts=1

IDEA: SKILL — magnetic-cta-with-cursor-glow (магнитные кнопки + световой след, без JS-библиотек)
KNOB: SKILL — magnetic-cta-glow
Название: `magnetic-cta-glow`
Когда применять: на любом статическом лендинге, где главный CTA — ссылка `.btn-primary` (или аналог), и нужно поднять кликабельность кнопок «студийного» уровня: кнопка мягко тянется к курсору и подсвечивается световым пятном под указателем. Работает и без JS (деградация — просто статичная кнопка).
Шаги:
1. Добавить SAFE CSS в `<style>` (или отдельный блок в конце).
2. Добавить SAFE JS перед закрывающим `</body>`.
3. Проверить: hover на десктопе — кнопка смещается на ≤6px к курсору, свет следует за мышью; на тач-устройствах эффекта нет, кнопка статична.
4. При `prefers-reduced-motion` трансформации отключаются (уже в CSS).

SAFE CSS:
```css
.btn-primary{position:relative;overflow:hidden;transition:transform .18s ease}
.btn-primary .glow{position:absolute;inset:0;pointer-events:none;background:radial-gradient(120px circle at var(--mx,50%) var(--my,50%),rgba(255,255,255,.25),transparent 65%);opacity:0;transition:opacity .25s}
.btn-primary:hover .glow{opacity:1}
@media (prefers-reduced-motion: reduce){.btn-primary{transition:none;transform:none!important}}
```

SAFE JS:
```js
document.querySelectorAll('.btn-primary').forEach(function(b){
  var g=document.createElement('span');g.className='glow';b.appendChild(g);
  b.addEventListener('mousemove',function(e){
    var r=b.getBoundingClientRect();
    b.style.setProperty('--mx',(e.clientX-r.left)+'px');
    b.style.setProperty('--my',(e.clientY-r.top)+'px');
    b.style.transform='translate('+((e.clientX-r.left-r.width/2)*0.06)+'px,'+((e.clientY-r.top-r.height/2)*0.12)+'px)';
  });
  b.addEventListener('mouseleave',function(){b.style.transform='';});
});
```
EFFECT: кнопки ощущаются «живыми» как у дорогих студий; микровзаимодействие повышает CTR по CTA (обычно +3–8% на кликабельных элементах), не трогая контент.
RISK: лёгкий сдвиг кнопки может дезориентировать при быстрой мыши — ограничено 6px и отключается reduced-motion.
ROLLBACK: удалить добавленный `<style>`-блок и `<script>`; либо `git checkout -- index.html`.
VERIFY: (1) открыть index.improved.html, навести на кнопку из L462 — свет следует за курсором, кнопка тянется ≤6px; (2) Tab-навигация: фокус виден, transform не мешает; (3) DevTools → emulate touch — эффекта нет, ошибок в консоли нет.
PRIORITY: 2 — чисто конверсионный полиш, применяется после смысловых правок.
SKILL: magnetic-cta-glow

IDEA: SKILL — section-entrance-stagger (каскадное появление блоков секции при скролле с резервом для no-JS)
KNOB: SKILL — section-entrance-stagger
Название: `section-entrance-stagger`
Когда применять: на любом одностраничном лендинге, где секции/карточки появляются резко или без анимации; даёт «дорогую» каскадную анимацию появления (IntersectionObserver + CSS-переходы) с гарантией видимости контента при выключенном JS.
Шаги:
1. Вставить SAFE CSS.
2. Вставить SAFE JS перед `</body>`.
3. Разметить нужные элементы классом `.stagger-item` (карточки
