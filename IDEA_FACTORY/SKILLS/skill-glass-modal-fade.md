---
name: SKILL — glass-modal-fade
source: localhost:8080/ovh/gpt-oss-120b
round: 91
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — glass-modal-fade

**Name:** `glass-modal-fade`
**When to apply:** Для отображения дополнительной информации (например, «Подробный чек‑лист цены») в модальном окне с эффектом стеклянной морфологии.
**SAFE CSS:**
```css
/* backdrop glass effect */
.glass-modal {
position: fixed;
inset: 0;
display: none;
align-items: center;
justify-content: center;
background: rgba(255,255,255,.1);
backdrop-filter: blur(12px) saturate(180%);
-webkit-backdrop-filter: blur(12px) saturate(180%);
z-index: 1000;
}
.glass-modal.active {display: flex;}
.glass-modal .content {
background: rgba(255,255,255,.15);
border-radius: 12px;
padding: 2rem;
max-width: 90%;
max-height: 80vh;
overflow-y: auto;
box-shadow: 0 8px 32px rgba(0,0,0,.25);
animation: fadeIn .3s ease-out forwards;
}
@keyframes fadeIn {
from {opacity:0; transform:scale(.95);}
to {opacity:1; transform:scale(1);}
}
```
**SAFE JS:**
```js
// открытие/закрытие модального окна
document.addEventListener('click', e => {
if (e.target.matches('[data-modal-open]')) {
const id = e.target.dataset.modalOpen;
document.getElementById(id).classList.add('active');
}
if (e.target.matches('.glass-modal') || e.target.matches('.glass-modal .close')) {
e.target.closest('.glass-modal').classList.remove('active');
}
});
```

## Когда применять
Позволяет показать детальную информацию без перехода на новую страницу, сохраняет стиль «luxury» через стеклянный фон, повышает время нахождения пользователя на сайте.

## Проверка
Добавить кнопку `data-modal-open="priceInfo"` к любой секции, кликнуть – открывается полупрозрачное модальное окно; проверить, что скролл внутри окна работает и закрытие по клику вне контента.
