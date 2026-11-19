# lareper/glm-5.3  2026-11-17 06:50:47
duration=31.7 error=- attempts=1

IDEA: SKILL — aurora-glass-hero (свет/стекло на hero: стеклянная панель под h1 + мягкое «аврора»-свечение, отличное от уже предложенных gradient-sweep и neon-border)
KNOB: SKILL — aurora-glass-hero
Name: `aurora-glass-hero`
When to apply: на любом статическом лендинге, где hero — тёмный фон с градиентом/blob-ами (как здесь, `.hero`, L449), и нужно премиальное «дорогое» ощущение без картинок и библиотек.

Steps:
1. В разметке hero обернуть содержимое `.hero .wrap` в `<div class="glass-panel">` (или применить класс к самому `.wrap`).
2. Добавить SAFE CSS (ниже) в конец `<style>`.
3. Опционально добавить SAFE JS для лёгкого смещения свечения за курсором (только на desktop, pointer:fine).
4. Проверить на мобильном: панель не должна вылезать за viewport (overflow-x: hidden уже есть на body — убедиться).

SAFE CSS:
```css
.glass-panel{
  position:relative;
  padding:clamp(28px,5vw,56px);
  border-radius:24px;
  background:linear-gradient(145deg,rgba(255,255,255,.06),rgba(255,255,255,.02));
  backdrop-filter:blur(18px) saturate(140%);
  -webkit-backdrop-filter:blur(18px) saturate(140%);
  border:1px solid rgba(255,255,255,.10);
  box-shadow:0 30px 80px rgba(0,0,0,.45), inset 0 1px 0 rgba(255,255,255,.08);
  overflow:hidden;
}
.glass-panel::before{
  content:'';
  position:absolute;
  inset:-40%;
  background:conic-gradient(from 120deg at 50% 50%,
    rgba(139,92,246,.18), rgba(56,189,248,.12), rgba(139,92,246,.05), rgba(139,92,246,.18));
  filter:blur(60px);
  animation:aurora-drift 14s linear infinite;
  pointer-events:none;
  z-index:0;
}
.glass-panel > *{position:relative;z-index:1}
@keyframes aurora-drift{
  0%{transform:rotate(0deg)}
  100%{transform:rotate(360deg)}
}
@media (prefers-reduced-motion: reduce){
  .glass-panel::before{animation:none}
}
@media (max-width:720px){
  .glass-panel{padding:22px 18px;border-radius:18px}
}
```

SAFE JS:
```js
(function(){
  var panel=document.querySelector('.glass-panel');
  if(!panel||!window.matchMedia('(pointer:fine)').matches)return;
  if(window.matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  panel.addEventListener('mousemove',function(e){
    var r=panel.getBoundingClientRect();
    var x=(e.clientX-r.left)/r.width-.5, y=(e.clientY-r.top)/r.height-.5;
    panel.style.setProperty('--gx',(x*30)+'px');
    panel.style.setProperty('--gy',(y*30)+'px');
  });
})();
```
(Для эффекта смещения добавить в CSS к `.glass-panel::before`: `transform:translate(var(--gx,0),var(--gy,0));` — тогда вращение заменить на drift через translate, либо оставить только rotate.)

EFFECT: hero выглядит «дорого» — стекло, глубина, живой свет; повышает воспринимаемую ценность услуги премиум-сегмента и удержание на первом экране.
RISK: backdrop-filter может подтормаживать на слабых Android — нужен fallback через @supports и проверка на реальном телефоне.
ROLLBACK: git checkout -- index.html (или удалить добавленный блок CSS/JS и класс glass-panel).
VERIFY: открыть index.html локально, сравнить hero до/после в
