# lareper/glm-5.2-fast-preview  2026-11-17 07:08:00
duration=55.6 error=- attempts=1

IDEA: SKILL — reveal-once-scroll-guard (анимации появления без «мигания» и без CLS, с отключением при reduced-motion)
KNOB: SKILL — `reveal-once-scroll-guard`
**Name:** `reveal-once-scroll-guard`
**When to apply:** На любом статическом лендинге, где секции/карточки имеют классы `reveal`/`zoom` и анимируются при скролле через IntersectionObserver. Проблема, которую решает: элементы «мигают» при быстрой прокрутке, повторно проигрывают анимацию, вызывают сдвиг макета (CLS) и не отключаются для пользователей с `prefers-reduced-motion`. Переносим на любой сайт, где есть класс-триггер появления.
**Steps:**
1. Найти в JS класс-триггер (здесь `reveal`), убедиться, что анимация задаётся через `transform`/`opacity` (не через `height`/`top` — иначе CLS).
2. Добавить SAFE CSS: стартовое состояние, класс `.is-visible`, transition только на `opacity` и `transform`, `will-change` только до завершения, полный блок `@media (prefers-reduced-motion: reduce)`.
3. Добавить SAFE JS: один IntersectionObserver, `once: true` (элемент появляется один раз), порог 0.15, guard от двойного добавления класса.
4. Проверить: быстрая прокрутка вверх-вниз — анимация не повторяется; Lighthouse CLS = 0; при включённом reduced-motion контент виден сразу.
5. Откат: удалить добавленный CSS/JS-блок из копии `index.improved.html`.

**SAFE CSS:**
```css
.reveal{opacity:0;transform:translateY(24px);transition:opacity .6s ease,transform .6s cubic-bezier(.2,.7,.3,1);will-change:opacity,transform}
.reveal.zoom{transform:scale(.94)}
.reveal.is-visible{opacity:1;transform:none;will-change:auto}
@media (prefers-reduced-motion: reduce){
  .reveal,.reveal.zoom{opacity:1;transform:none;transition:none;will-change:auto}
}
```

**SAFE JS:**
```js
(function(){
  var els=document.querySelectorAll('.reveal');
  if(!('IntersectionObserver' in window)||window.matchMedia('(prefers-reduced-motion: reduce)').matches){
    els.forEach(function(e){e.classList.add('is-visible')});return;
  }
  var io=new IntersectionObserver(function(entries){
    entries.forEach(function(en){
      if(en.isIntersecting&&!en.target.classList.contains('is-visible')){
        en.target.classList.add('is-visible');io.unobserve(en.target);
      }
    });
  },{threshold:0.15,once:true});
  els.forEach(function(e){io.observe(e)});
})();
```

EFFECT: плавное премиальное появление секций без повторов и сдвигов макета; CLS≈0, ниже воспринимаемая «дешёвость» страницы, стабильный рендер на слабых телефонах.
RISK: если существующий на сайте JS уже управляет `.reveal`, возможен двойной observer — нужно удалить/заменить старый обработчик, а не добавить параллельный.
ROLLBACK: `git checkout -- index.improved.html` (или удалить добавленный блок из копии; оригинал `index.html` не трогается).
VERIFY: (1) открыть index.improved.html, быстро проскроллить вниз и вверх — секции не мигают повторно; (2) DevTools → Rendering → Emulate prefers-reduced-motion: reduce — весь контент виден сразу; (3) Lighthouse → CLS = 0 за ~3 минуты.
PRIORITY: 2 — сайт уже использует reveal-анимации (классы `reveal`/`zoom` по всему файлу), скилл делает существующую механику стабильной и переносимой; эффект заметный, но не первый экран.
SITE_REQUEST: IntersectionObserver
