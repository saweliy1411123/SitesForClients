---
name: SKILL — hero-cta-clipboard-copy
source: localhost:8080/ovh/gpt-oss-120b
round: 55
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — hero-cta-clipboard-copy

**Name:** `hero-cta-clipboard-copy`
**When to apply:** На лендингах, где CTA‑кнопка ведёт в мессенджер (Telegram) и пользователь может захотеть скопировать ссылку/username.
**Steps:**
1. В hero‑секцию рядом с основной CTA‑кнопкой добавить вторую кнопку‑ссылка:
```html
<a class="btn-primary clipboard" href="javascript:void(0)" aria-label="Скопировать ссылку на Telegram">
Скопировать ссылку <span class="arr">→</span>
</a>
```
2. Добавить в конец `<body>` безопасный скрипт, который копирует в буфер обмена фиксированную строку (Telegram‑username):
SAFE JS:
```js
(() => {
const btn = document.querySelector('.clipboard');
if (!btn) return;
const text = 'https://t.me/TrainersDontPlays';
btn.addEventListener('click', async e => {
e.preventDefault();
try {
await navigator.clipboard.writeText(text);
btn.textContent = 'Скопировано!';
setTimeout(() => btn.innerHTML = 'Скопировать ссылку <span class="arr">→</span>', 2000);
} catch (err) {
console.error('Clipboard write failed', err);
}
});
})();
```
3. Добавить небольшое CSS‑оформление, чтобы кнопка выглядела как остальные CTA (SAFE CSS):
SAFE CSS:
```css
.clipboard {
display:inline-flex;align-items:center;justify-content:center;
margin-left:12px;padding:15px 20px;font-weight:600;
background:var(--grad);color:#fff;border-radius:8px;
cursor:pointer;transition:background .3s;
}
.clipboard:hover {background:var(--grad-dark);}
.clipboard .arr {margin-left:6px;transition:transform .2s;}
.clipboard:hover .arr {transform:translateX(4px);}
```

## Когда применять
Позволяет пользователю быстро скопировать ссылку на Telegram без переключения окна, снижая трение и повышая вероятность контакта.

## Проверка
Открыть страницу, нажать кнопку «Скопировать ссылку», затем вставить (Ctrl+V) в любой текстовый редактор – должна появиться полная ссылка. Убедиться, что после 2 секунд текст кнопки возвращается к исходному.
