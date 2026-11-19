---
name: SKILL — proof-counter-aria-live
source: localhost:8081/big_only
round: 34
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — proof-counter-aria-live


name: proof-counter-aria-live
when: при наличии анимированных числовых счётчиков в hero‑или секциях «доверие» (элементы `<em data-count="…">`)
steps:
- Обернуть каждый `<em data-count="…">` в `<span class="proof-number" role="status" aria-live="polite" aria-label="Количество довольных клиентов">`.
- Переместить числовое значение в атрибут `data-count` (оставить `0` в тексте).
- Добавить CSS‑класс для стилизации счётчика.
- Включить небольшую безопасную анимацию счётчика (см. SAFE JS).
SAFE CSS:
.proof-number{font-weight:600;color:var(--accent);transition:color .3s ease}
SAFE JS:
(()=>{const items=document.querySelectorAll('.proof-number[data-count]');items.forEach(el=>{const target=+el.dataset.count;let cur=0;const step=Math.ceil(target/60);const upd=()=>{cur=Math.min(cur+step,target);el.textContent=cur;if(cur<target)requestAnimationFrame(upd)};requestAnimationFrame(upd)});})();

## Когда применять
скрин‑ридеры озвучивают текущие значения, повышая доступность; анимация сохраняет визуальный эффект без потери семантики.

## Проверка
открыть страницу, включить режим «Screen Reader» в DevTools → Accessibility, убедиться, что счётчик объявляется; проверить, что цифры плавно растут до целевого значения.

## SAFE CSS
```css
.proof-number{font-weight:600;color:var(--accent);transition:color .3s ease}
```

## SAFE JS
```js
(()=>{const items=document.querySelectorAll('.proof-number[data-count]');items.forEach(el=>{const target=+el.dataset.count;let cur=0;const step=Math.ceil(target/60);const upd=()=>{cur=Math.min(cur+step,target);el.textContent=cur;if(cur<target)requestAnimationFrame(upd)};requestAnimationFrame(upd)});})();
```
