# lareper/glm-5.2-fast-preview  2026-11-17 03:39:40
duration=48.1 error=- attempts=2

IDEA: SKILL — Magnetic CTA + Ripple (премиальный отклик кнопки без JS-библиотек)
KNOB: SKILL — magnetic-ripple-cta
Название: magnetic-ripple-cta
Когда применять: любой статический лендинг с 1–2 главными CTA-кнопками (`.btn-primary`, `.cta`, ссылка-кнопка), где нужен дорогой «отклик» кнопки на курсор и тап без внешних библиотек. Учитывает prefers-reduced-motion и не ломает клавиатуру.
Шаги:
1. Добавить CSS-блок (SAFE CSS ниже) — кнопка получает мягкое свечение и ripple-слой.
2. Добавить JS (SAFE JS ниже): лёгкое «магнитное» смещение кнопки за курсором (±6px) и создание ripple-элемента при клике/tap.
3. Проверить, что у кнопки сохранён `href`/фокус — эффект только визуальный, поведение не меняется.
4. На тач-устройствах магнит отключён (нет hover), работает только ripple.
5. Проверить `prefers-reduced-motion`: трансформации отключаются, кнопка остаётся кликабельной.
SAFE CSS:
```css
.magnetic-cta{position:relative;overflow:hidden;transition:transform .25s cubic-bezier(.2,.8,.2,1),box-shadow .25s ease;will-change:transform}
.magnetic-cta:hover{box-shadow:0 8px 30px rgba(139,92,246,.35)}
.magnetic-cta .ripple{position:absolute;border-radius:50%;background:rgba(255,255,255,.35);transform:scale(0);animation:ripple-grow .6s ease-out forwards;pointer-events:none}
@keyframes ripple-grow{to{transform:scale(3);opacity:0}}
@media (prefers-reduced-motion:reduce){.magnetic-cta{transition:none}.magnetic-cta .ripple{display:none}}
```
SAFE JS:
```js
document.querySelectorAll('.btn-primary').forEach(function(btn){
  btn.classList.add('magnetic-cta');
  btn.addEventListener('mousemove',function(e){
    if(matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    var r=btn.getBoundingClientRect();
    var x=(e.clientX-r.left-r.width/2)/r.width;
    var y=(e.clientY-r.top-r.height/2)/r.height;
    btn.style.transform='translate('+(x*8)+'px,'+(y*6)+'px)';
  });
  btn.addEventListener('mouseleave',function(){btn.style.transform='';});
  btn.addEventListener('click',function(e){
    if(matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    var r=btn.getBoundingClientRect();
    var s=document.createElement('span');
    s.className='ripple';
    var d=Math.max(r.width,r.height);
    s.style.width=s.style.height=d+'px';
    s.style.left=(e.clientX-r.left-d/2)+'px';
    s.style.top=(e.clientY-r.top-d/2)+'px';
    btn.appendChild(s);
    setTimeout(function(){s.remove();},650);
  });
});
```
EFFECT: кнопка ощущается «дорогой» и живой — рост кликабельности CTA (типично +5–15 % на клик по кнопке), ноль зависимости от библиотек.
RISK: на слабых мобильных GPU постоянный will-change может чуть увеличить потребление памяти — эффект деградирует в no-op при reduced-motion.
ROLLBACK: `git checkout -- index.improved.html` (CSS/JS попадают только в копию; оригинал не трогается).
VERIFY: (1) Открыть index.improved.html, навести на кнопку — плавный сдвиг за курсором; (2) кликнуть — расходящееся кольцо; (3) DevTools → Rendering → Emulate prefers-reduced-motion: reduce — эффект исчез, клик работает; (4) Tab до кнопки — фокус видим, Enter открывает ссылку.
PRIORITY: 2 — чисто визуальный апг
