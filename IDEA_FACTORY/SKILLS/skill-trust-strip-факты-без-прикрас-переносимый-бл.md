---
name: SKILL — Trust-Strip «Факты без прикрас» (переносимый блок доверия под hero)
source: lareper/glm-5.2
round: 20
status: proposed
portable: true
tags: [static-landing, portable, animation, responsive]
---

# SKILL — Trust-Strip «Факты без прикрас» (переносимый блок доверия под hero)

Название: **trust-strip**. Когда применять: любой статический лендинг, где главный CTA — бесплатное демо/заявка, а доверие нужно подкрепить фактами без фейков. Шаги: (1) сразу после `.hero-note` (L465) вставить полосу из 3–4 фактов, каждый — реальное проверяемое утверждение владельца (город, срок, формат работы, способ связи); (2) стилизовать как тонкую строку с разделителями; (3) на мобильном — перенос строк, без сетки. Для этого сайта факты: «Пермь · работаю лично», «Демо — бесплатно и без обязательств», «Запись не трогаю», «Правки — неделю после запуска» (всё уже заявлено на сайте, ничего не выдумываем).
SAFE CSS:
.trust-strip{display:flex;flex-wrap:wrap;gap:10px 22px;justify-content:center;margin-top:26px;padding:0;list-style:none}
.trust-strip li{position:relative;padding-left:22px;font-size:14px;color:rgba(255,255,255,.72)}
.trust-strip li::before{content:"✓";position:absolute;left:0;top:0;color:#8b5cf6;font-weight:700}
.trust-strip li+li::after{content:"";position:absolute;left:-12px;top:6px;width:1px;height:14px;background:rgba(255,255,255,.15)}
@media (max-width:520px){.trust-strip{flex-direction:column;align-items:center;gap:8px}.trust-strip li+li::after{display:none}}
@media (prefers-reduced-motion: reduce){.trust-strip{animation:none}}
SAFE JS: (не требуется — блок чисто HTML+CSS)

## Когда применять


## Проверка
Открыть index.improved.html, DevTools → 375px: полоса не ломает сетку, переносится корректно; 5-секундный тест (I-00062): человек помнит хотя бы 1 факт из полосы.

## SAFE CSS
```css
.trust-strip{display:flex;flex-wrap:wrap;gap:10px 22px;justify-content:center;margin-top:26px;padding:0;list-style:none}
.trust-strip li{position:relative;padding-left:22px;font-size:14px;color:rgba(255,255,255,.72)}
.trust-strip li::before{content:"✓";position:absolute;left:0;top:0;color:#8b5cf6;font-weight:700}
.trust-strip li+li::after{content:"";position:absolute;left:-12px;top:6px;width:1px;height:14px;background:rgba(255,255,255,.15)}
@media (max-width:520px){.trust-strip{flex-direction:column;align-items:center;gap:8px}.trust-strip li+li::after{display:none}}
@media (prefers-reduced-motion: reduce){.trust-strip{animation:none}}
```

## SAFE JS
```js
(не требуется — блок чисто HTML+CSS)
```
