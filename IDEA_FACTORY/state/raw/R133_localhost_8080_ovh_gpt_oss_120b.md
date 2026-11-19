# localhost:8080/ovh/gpt-oss-120b  2026-11-17 08:08:54
duration=44.2 error=- attempts=1

IDEA: Glassmorphic CTA button  
KNOB: SKILL — glassmorphic-cta-button  
Name: glassmorphic-cta-button  
When to apply: На всех ссылках‑CTA с классом `.btn-primary` в любом лендинге, где нужен премиальный визуальный акцент без тяжёлых скриптов.  
SAFE CSS:  
```css
.btn-primary {
  position: relative;
  overflow: hidden;
  background: rgba(255,255,255,0.12);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255,255,255,0.2);
  color: var(--text);
  transition: background .3s ease, box-shadow .3s ease;
}
.btn-primary::before {
  content: "";
  position: absolute;
  inset: -50%;
  background: linear-gradient(135deg, rgba(139,92,246,.2), rgba(76,201,240,.2));
  transform: rotate(45deg);
  transition: transform .5s ease;
}
.btn-primary:hover::before {
  transform: rotate(45deg) translateX(200%);
}
.btn-primary:hover {
  background: rgba(255,255,255,0.18);
  box-shadow: 0 4px 12px rgba(0,0,0,.15);
}
```  
SAFE JS: *(не требуется)*  
EFFECT: Повышает восприятие ценности CTA, делает кнопку более «премиальной», увеличивает CTR за счёт визуального контраста.  
RISK: Некоторая часть старых браузеров (IE) не поддерживает `backdrop-filter`; в них кнопка будет без эффекта размытия.  
ROLLBACK: `git rm SKILLS/glassmorphic-cta-button.md && git checkout -- index.improved.html`  
VERIFY: Открыть страницу в Chrome, навести курсор на любую кнопку CTA – должна появиться анимация градиентного сдвига и размытие фона; сравнить CTR в аналитике до/после.  
PRIORITY: 1 – быстрый визуальный апгрейд с высокой вероятностью роста конверсии, без изменений кода страницы.  

IDEA: Parallax blob background  
KNOB: SKILL — parallax-blob-layer  
Name: parallax-blob-layer  
When to apply: В секции `.hero` (или любой full‑width секции) для создания глубины с лёгким движением при наведении/скролле.  
SAFE CSS:  
```css
.hero {
  perspective: 800px;
  overflow: hidden;
}
.hero .blob-layer {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-repeat: no-repeat;
  background-size: cover;
  will-change: transform;
}
.blob-layer--far  { background-image: url('data:image/svg+xml,…'); transform: translateZ(-30px) scale(1.2); }
.blob-layer--mid  { background-image: url('data:image/svg+xml,…'); transform: translateZ(-15px) scale(1.1); }
.blob-layer--near { background-image: url('data:image/svg+xml,…'); transform: translateZ(0); }
```  
SAFE JS:  
```js
document.addEventListener('mousemove',e=>{
  const {innerWidth:w,innerHeight:h}=window;
  const x=(e.clientX/w-0.5)*2;
  const y=(e.clientY/h-0.5)*2;
  document.querySelectorAll('.blob-layer').forEach(el=>{
    const depth=el.dataset.depth||0;
    el.style.transform=`translate3d(${x*depth*10}px,${y*depth*10}px,0)`;
  });
});
```  
EFFECT: Создаёт ощущение трёхмерного пространства, усиливает эмоциональное вовлечение и удержание внимания на первом экране.  
RISK: При сильных движениях может возникнуть небольшая «дрожь» на слабом GPU; пользователи с отключённым JS не увидят анимацию.  
ROLLBACK: `git rm SKILLS/parallax-blob-layer.md && git checkout -- index.improved.html`  
VERIFY: Открыть страницу, переместить курсор – фон‑слои должны плавно смещаться в разных направлениях; проверить отсутствие лагов в DevTools → Performance.  
PRIORITY: 2 – повышает визуальную привлекательность, но требует небольшого JS; стоит после базовых улучшений.  

IDEA: Depth‑hover 3D card  
KNOB: SKILL — depth-hover-card  
Name: depth-hover-card  
When to apply: На любые карточки (`.price-card`, `.step`, `.demo-card`) где нужен интерактивный 3D‑эффект при наведении.  
SAFE CSS:  
```css
.card-3d {
  perspective: 600px;
  transform-style: preserve-3d;
  transition: transform .3s ease;
}
```  
SAFE JS:  
```js
document.querySelectorAll('.card-3d').forEach(c=>{
  c.addEventListener('mousemove',e=>{
    const r=c.getBoundingClientRect();
    const x=((e.clientX-r.left)/r.width-0.5)*20;
    const y=((e.clientY-r.top)/r.height-0.5)*20;
    c.style.transform=`rotateY(${x}deg) rotateX(${ -y }deg)`;
  });
  c.addEventListener('mouseleave',()=>c.style.transform='rotateY(0) rotateX(0)');
});
```  
EFFECT: Делает карточки «живыми», повышает вовлечённость и запоминаемость предложения, что может увеличить конверсии в цене/демо.  
RISK: На мобильных устройствах без указателя курсор не будет работать; потребуется fallback (без трансформаций).  
ROLLBACK: `git rm SKILLS/depth-hover-card.md && git checkout -- index.improved.html`  
VERIFY: На ПК переместить курсор по карточке – она должна наклоняться; на мобильном проверить отсутствие ошибок в консоли.  
PRIORITY: 2 – хороший визуальный апгрейд, но требует JS, поэтому ставим после более критичных улучшений.  

IDEA: Mobile navigation chips scroll  
KNOB: SKILL — mobile-nav-chips  
Name: mobile-nav-chips  
When to apply: В медиазапросе `@media(max-width:720px)` заменить скрытие `.nav-links` на горизонтально прокручиваемый набор «чипов»‑якорей, чтобы пользователь мог быстро перейти к секциям.  
SAFE CSS:  
```css
@media(max-width:720px){
  .nav-links{
    display:flex;
    overflow-x:auto;
    -webkit-overflow-scrolling:touch;
    gap:12px;
    padding:8px;
    scrollbar-width:none;
  }
  .nav-links::-webkit-scrollbar{display:none;}
  .nav-links a{
    flex:0 0 auto;
    padding:6px 12px;
    background:rgba(255,255,255,.08);
    border-radius:9999px;
    font-size:14px;
    white-space:nowrap;
  }
  .nav-links a:focus-visible{
    outline:2px solid var(--blue);
  }
}
```  
SAFE JS: *(не требуется)*  
EFFECT: Улучшает доступность навигации на мобильных, повышает вероятность быстрого перехода к нужному разделу, снижает показатель отказов.  
RISK: При слишком большом количестве пунктов навигации может потребоваться дополнительный отступ, но это редкость для 7‑секций.  
ROLLBACK: `git rm SKILLS/mobile-nav-chips.md && git checkout -- index.improved.html`  
VERIFY: В мобильном режиме (Chrome DevTools) открыть страницу, убедиться, что меню отображается как горизонтальная прокрутка, ссылки работают, а скролл плавный.  
PRIORITY: 1 – критически важный для мобильных пользователей, где большинство трафика, без необходимости писать JS.
