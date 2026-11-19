# lareper/glm-5.3  2026-11-17 05:02:08
duration=2.4 error=- attempts=1

IDEA: SKILL — scroll-triggered-step-highlight (шаги подсвечиваются по мере прокрутки, «живой» прогресс без бэкенда)
KNOB: SKILL — scroll-triggered-step-highlight
Название: scroll-triggered-step-highlight
Когда применять: на любом статическом лендинге с нумерованными шагами/процессом (3–5 карточек в ряд), чтобы шаги «оживали» по мере прокрутки и вели глаз сверху вниз. Не требует библиотек, работает на чистом IntersectionObserver.
Шаги:
1. Убедиться, что шаги секции обёрнуты в общий контейнер (например `.steps`) и каждый шаг — карточка с классом `.step` (добавить класс, если его нет).
2. Вставить SAFE CSS в конец `<style>`.
3. Вставить SAFE JS перед `</body>` (после основного скрипта).
4. Проверить: при прокрутке шаги по очереди получают класс `.is-active` — рамка/номер подсвечиваются; при `prefers-reduced-motion` анимации отключены.
5. Откатить — удалить вставленные блоки (оригинал index.html не трогается, всё уходит в index.improved.html).

SAFE CSS:
.steps{--step-accent:#8b5cf6}
.step{position:relative;transition:transform .45s ease,box-shadow .45s ease,opacity .45s ease;opacity:.55}
.step.is-active{opacity:1;transform:translateY(-4px);box-shadow:0 24px 60px rgba(139,92,246,.18)}
.step .step-num{transition:color .45s ease,transform .45s ease}
.step.is-active .step-num{color:var(--step-accent);transform:scale(1.12)}
.step.is-active::before{content:'';position:absolute;inset:-1px;border-radius:inherit;border:1px solid rgba(139,92,246,.45);pointer-events:none}
@media (prefers-reduced-motion: reduce){.step,.step .step-num{transition:none}.step.is-active{transform:none}}

SAFE JS:
document.addEventListener('DOMContentLoaded',function(){
var steps=document.querySelectorAll('.steps .step');
if(!steps.length||!('IntersectionObserver' in window))return;
var io=new IntersectionObserver(function(entries){
entries.forEach(function(e){
if(e.isIntersecting){e.target.classList.add('is-active');io.unobserve(e.target);}
});
},{threshold:.4});
steps.forEach(function(s){io.observe(s);});
});

EFFECT: посетитель визуально проходит путь «шаг 1 → шаг 3», лучше понимает процесс и доходит до CTA цены; выглядит дороже, чем статичный список.
RISK: при очень плотной вёрстке подсветка может конфликтовать с существующим hover-эффектом карточек — проверить на копии.
ROLLBACK: git checkout -- index.improved.html (или удалить вставленные CSS/JS блоки).
VERIFY: открыть index.improved.html, прокрутить до «Три шага»: карточки по очереди подсвечиваются; в DevTools → Rendering → Emulate prefers-reduced-motion: reduce — анимации отключены; Tab-порядок не изменился.
PRIORITY: 2 — заметный визуальный/конверсионный выигрыш при нулевом риске для контента.
SITE_REQUEST: steps

IDEA: SKILL — anchor-cta-safe-area (якорные CTA с корректным фокусом, скроллом и safe-area на мобильных — единый фикс для всех кнопок)
KNOB: SKILL — anchor-cta-safe-area
Название: anchor-cta-safe-area
Когда применять: на любом лендинге, где CTA — это `<a href="#...">`-якоря, а на мобильных есть фиксированный sticky-CTA/шапка: якорь уезжает под фикс-элемент, фокус не виден, на iPhone кнопка прилипает к краю экрана. Один блок чинит всё сразу.
Шаги
