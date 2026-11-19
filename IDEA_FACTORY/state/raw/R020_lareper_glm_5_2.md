# lareper/glm-5.2  2026-11-17 02:38:50
duration=61.4 error=- attempts=1

IDEA: SKILL — Trust-Strip «Факты без прикрас» (переносимый блок доверия под hero)
KNOB: Название: **trust-strip**. Когда применять: любой статический лендинг, где главный CTA — бесплатное демо/заявка, а доверие нужно подкрепить фактами без фейков. Шаги: (1) сразу после `.hero-note` (L465) вставить полосу из 3–4 фактов, каждый — реальное проверяемое утверждение владельца (город, срок, формат работы, способ связи); (2) стилизовать как тонкую строку с разделителями; (3) на мобильном — перенос строк, без сетки. Для этого сайта факты: «Пермь · работаю лично», «Демо — бесплатно и без обязательств», «Запись не трогаю», «Правки — неделю после запуска» (всё уже заявлено на сайте, ничего не выдумываем).
SAFE CSS:
.trust-strip{display:flex;flex-wrap:wrap;gap:10px 22px;justify-content:center;margin-top:26px;padding:0;list-style:none}
.trust-strip li{position:relative;padding-left:22px;font-size:14px;color:rgba(255,255,255,.72)}
.trust-strip li::before{content:"✓";position:absolute;left:0;top:0;color:#8b5cf6;font-weight:700}
.trust-strip li+li::after{content:"";position:absolute;left:-12px;top:6px;width:1px;height:14px;background:rgba(255,255,255,.15)}
@media (max-width:520px){.trust-strip{flex-direction:column;align-items:center;gap:8px}.trust-strip li+li::after{display:none}}
@media (prefers-reduced-motion: reduce){.trust-strip{animation:none}}
SAFE JS: (не требуется — блок чисто HTML+CSS)
RISK: Низкий — только визуальный блок; факты должны быть подтверждены владельцем, иначе риск недоверия.
ROLLBACK: git checkout -- index.html (или удалить вставленный блок из index.improved.html)
VERIFY: Открыть index.improved.html, DevTools → 375px: полоса не ломает сетку, переносится корректно; 5-секундный тест (I-00062): человек помнит хотя бы 1 факт из полосы.
PRIORITY: 1 — усиливает первый экран и снимает возражения до скролла, нулевой риск.
SITE_REQUEST: hero-note

IDEA: SKILL — «Мягкий подсвет-пульс CTA» (этичное привлечение внимания без dark patterns)
KNOB: Название: **cta-soft-pulse**. Когда применять: любой лендинг с одной якорной CTA-кнопкой (`.btn-primary`), где нужно повысить заметность кнопки без мигания, таймеров и ложных дедлайнов. Шаги: (1) добавить к `.btn-primary` (L462 и финальная CTA) класс-модификатор `.pulse`; (2) лёгкая анимация тени-свечения 3 с цикл, пауза на hover/focus; (3) обязательно отключение при `prefers-reduced-motion`; (4) убедиться, что пульс не меняет размер/положение кнопки (только box-shadow — нет CLS).
SAFE CSS:
.pulse{animation:cta-pulse 3s ease-in-out infinite}
@keyframes cta-pulse{0%,100%{box-shadow:0 0 0 0 rgba(139,92,246,.45)}50%{box-shadow:0 0 0 12px rgba(139,92,246,0)}}
.pulse:hover,.pulse:focus-visible{animation:none;box-shadow:0 8px 30px rgba(139,92,246,.35)}
@media (prefers-reduced-motion: reduce){.pulse{animation:none}}
SAFE JS: (не требуется
