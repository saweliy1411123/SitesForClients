# lareper/glm-5.3  2026-11-17 06:47:42
duration=70.0 error=- attempts=1

SKILL — faq-a11y-details-enhance (семантический FAQ-аккордеон с клавиатурой и запоминанием)
KNOB: SKILL — faq-a11y-details-enhance
Название: `faq-a11y-details-enhance`
Когда применять: на любом статическом лендинге, где FAQ сделан на div/JS-кликах или просто списком — заменить на нативный `<details>/<summary>`: работает без JS, доступен с клавиатуры, индексируется поисковиками, и можно мягко анимировать раскрытие.

Шаги:
1. В секции FAQ (на этом сайте `#faq`, разметка с L663) каждый блок «вопрос+ответ» превратить в:
```html
<details class="faq-item">
  <summary>Текст вопроса</summary>
  <div class="faq-answer"><p>Текст ответа</p></div>
</details>
```
2. Первому (самому частому) вопросу добавить атрибут `open` — чтобы посетитель сразу видел пример ответа.
3. Убрать старый JS-код toggle, если он был — `<details>` работает нативно.
4. (Опционально) один вопрос на странице = один `<details>`; если нужен режим «открыт только один» — добавить SAFE JS ниже.
5. Проверить Tab/Enter: summary фокусируется и открывается клавишей Enter/Space без дополнительного кода.

SAFE CSS:
```css
.faq-item{
  border:1px solid var(--border,#e5e7eb);
  border-radius:14px;
  margin-bottom:12px;
  background:rgba(255,255,255,.03);
  overflow:hidden;
  transition:border-color .25s ease, background .25s ease;
}
.faq-item:hover{border-color:var(--blue,#8b5cf6)}
.faq-item summary{
  cursor:pointer;
  list-style:none;
  padding:18px 22px;
  font-weight:600;
  font-size:16px;
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:16px;
  min-height:48px;
  outline:none;
}
.faq-item summary::-webkit-details-marker{display:none}
.faq-item summary::after{
  content:'';
  width:10px;height:10px;
  border-right:2px solid var(--blue,#8b5cf6);
  border-bottom:2px solid var(--blue,#8b5cf6);
  transform:rotate(45deg);
  transition:transform .3s ease;
  flex-shrink:0;
}
.faq-item[open] summary::after{transform:rotate(225deg)}
.faq-item .faq-answer{
  padding:0 22px 20px;
  color:var(--muted,#9ca3af);
  font-size:15px;
  line-height:1.6;
  animation:faq-open .3s ease;
}
.faq-item summary:focus-visible{
  outline:2px solid var(--blue,#8b5cf6);
  outline-offset:-2px;
  border-radius:14px;
}
@keyframes faq-open{
  from{opacity:0;transform:translateY(-6px)}
  to{opacity:1;transform:translateY(0)}
}
@media (prefers-reduced-motion: reduce){
  .faq-item .faq-answer{animation:none}
  .faq-item summary::after{transition:none}
}
```

SAFE JS:
```js
// режим «открыт только один вопрос» — нативно, без зависимостей
document.querySelectorAll('.faq-item').forEach(function(d){
  d.addEventListener('toggle', function(){
    if(d.open){
      document.querySelectorAll('.faq-item[open]').forEach(function(o){
        if(o!==d){o.removeAttribute('open');}
      });
    }
  });
});
```

EFFECT: FAQ становится доступным (клавиатура, скринридеры), индексируемым (Google читает содержимое details), снижается нагрузка на JS; пользователь быстрее находит ответ на возражение
