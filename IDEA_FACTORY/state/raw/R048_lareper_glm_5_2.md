# lareper/glm-5.2  2026-11-17 03:59:14
duration=2.3 error=- attempts=2

IDEA: SKILL — focus-visible-kit (единая премиальная клавиатурная видимость фокуса)
KNOB: Название: focus-visible-kit. Когда применять: любой статический лендинг с ссылками-CTA, якорями, details/summary — везде, где фокус по умолчанию выглядит по-разному или скрыт обнулением outline. Шаги: (1) Проверить Tab-проход по странице: есть ли видимый фокус на .btn-primary, nav-ссылках, внешних ссылках. (2) Добавить в `<style>` блок SAFE CSS ниже. (3) Добавить skip-link сразу после `<body>`: `<a class="skip-link" href="#top">К содержимому</a>`. (4) Проверить: Tab с первого элемента — skip-link появляется, дальше фокус-кольца на всех интерактивных элементах, ни один не «теряется» на тёмном фоне. SAFE CSS:
```css
:root{--focus-ring:0 0 0 3px rgba(139,92,246,.55),0 0 0 6px rgba(76,201,240,.35)}
a:focus-visible,button:focus-visible,summary:focus-visible,[tabindex]:focus-visible{
outline:none;box-shadow:var(--focus-ring);border-radius:8px}
.btn-primary:focus-visible{box-shadow:var(--focus-ring),0 12px 40px rgba(139,92,246,.45)}
.skip-link{position:fixed;top:-60px;left:16px;z-index:9999;background:#fff;color:#0a0a0f;
padding:10px 18px;border-radius:10px;font-weight:700;transition:top .2s}
.skip-link:focus{top:12px}
@media (prefers-reduced-motion:reduce){.skip-link{transition:none}}
```
EFFECT: клавиатурные пользователи и скринридеры не теряют CTA; растёт a11y-оценка Lighthouse; премиальный единый вид фокуса вместо браузерного.
RISK: на светлом фоне фиолетовое кольцо может слиться — подобрать цвет через VERIFY.
ROLLBACK: git checkout -- index.html (правки только в index.improved.html).
VERIFY: открыть страницу, нажать Tab 10 раз: каждый интерактивный элемент даёт видимое кольцо; skip-link появляется первым; Lighthouse Accessibility ≥ 95.
PRIORITY: 2 — дешёвый универсальный a11y-буст, не виден большинству, но критичен для доступности и аудитов.
SKILL: focus-visible-kit

IDEA: SKILL — anchor-offset-fix (якоря не прячутся под фиксированной шапкой)
KNOB: Название: anchor-offset-fix. Когда применять: любой одностраничник с фиксированным/sticky-хедером и якорной навигацией (#faq, #price, #steps) — при клике заголовок секции уезжает под шапку. Шаги: (1) Кликнуть по каждой якор
