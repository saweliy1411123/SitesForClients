# lareper/glm-5.2  2026-11-17 06:25:58
duration=2.3 error=- attempts=2

IDEA: SKILL — sticky-cta-reveal (умная плавающая CTA-кнопка, появляется после hero)
SKILL — sticky-cta-reveal
Название: `sticky-cta-reveal`
Когда применять: на любом статическом лендинге, где главный CTA — якорная ссылка на форму/контакт, а после скролла первого экрана кнопка исчезает из виду. Скилл добавляет плавающую кнопку внизу экрана, которая появляется только когда пользователь проскроллил мимо hero и не видит основной CTA, и скрывается, когда виден финальный блок с CTA (чтобы не дублировать).
Шаги:
1. Найти id главного CTA-якоря (например `#contact`) и id финальной секции (например `#final`).
2. Добавить разметку: одна ссылка `<a class="sticky-cta" href="#contact">` перед закрывающим `</body>`.
3. Добавить SAFE CSS (кнопка фиксирована, скрыта по умолчанию, показывается классом `.is-visible`).
4. Добавить SAFE JS: IntersectionObserver на hero и на финальной секции; если hero не виден и финал не виден — показать кнопку, иначе скрыть. Без таймеров и fetch.
5. Проверить: скролл вниз — кнопка появляется; доскроллил до финального CTA — кнопка исчезает; Tab — кнопка в фокус-порядке последней; на мобильном не перекрывает контент (проверить на 375px).
6. Откатить: удалить добавленный блок и стили (git checkout).

SAFE CSS:
.sticky-cta{position:fixed;left:16px;right:16px;bottom:16px;z-index:50;display:none;align-items:center;justify-content:center;gap:8px;padding:15px 20px;min-height:52px;border-radius:14px;background:linear-gradient(135deg,#8b5cf6,#6d5cf6);color:#fff;font-weight:700;font-size:16px;text-decoration:none;box-shadow:0 8px 30px rgba(139,92,246,.35);opacity:0;transform:translateY(12px);transition:opacity .25s,transform .25s}
.sticky-cta.is-visible{display:flex;opacity:1;transform:translateY(0)}
.sticky-cta:focus-visible{outline:3px solid #fff;outline-offset:2px}
@media (prefers-reduced-motion: reduce){.sticky-cta{transition:none;transform:none}}

SAFE JS:
(function(){
  var cta=document.querySelector('.sticky-cta');
  var hero=document.querySelector('.hero');
  var fin=document.querySelector('.final');
  if(!cta||!hero||!('IntersectionObserver' in window))return;
  var heroOut=false, finIn=false;
  new IntersectionObserver(function(e){heroOut=!e[0].isIntersecting;update();}).observe(hero);
  new IntersectionObserver(function(e){finIn=e[0].isIntersecting;update();}).observe(fin);
  function update(){cta.classList.toggle('is-visible',heroOut&&!finIn);}
})();

EFFECT: заявка доступна в один тап с любой точки страницы — растёт доля переходов к #contact, особенно на мобильных, где скролл длинный.
RISK: на очень коротких экранах кнопка может перекрывать контент — нужен тест на 375px и проверка, что sticky-элементы не конфликтуют.
ROLLBACK: `git checkout -- index.improved.html` (правки только в копии) или удалить добавленный блок/стили.
VERIFY: (1) Открыть копию index.improved.html. (2) Скролл до середины — кнопка видна. (3) Доскроллить до финального CTA — кнопка скрылась. (4) Tab с верха — фокус доходит до кнопки, outline виден. (5) DevTools → 375px — не
