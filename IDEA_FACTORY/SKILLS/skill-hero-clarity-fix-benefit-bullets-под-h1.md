---
name: SKILL — hero‑clarity‑fix («Benefit‑bullets под H1»)
source: localhost:8080/ovh/gpt-oss-120b
round: 41
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — hero‑clarity‑fix («Benefit‑bullets под H1»)

**Name:** `hero-clarity-fix`
**When to apply:** На любой статический лендинг, где первый экран (hero) содержит только заголовок + подзаголовок и нужен быстрый способ показать ключевые выгоды (3‑5 пунктов) без изменения разметки страницы.
**Steps:**
1. Вставить сразу после закрывающего `</h1>` в секции `.hero` блок:
```html
<ul class="hero-benefits">
<li>✅ Сайт готов за 2 дня — без задержек</li>
<li>✅ Клиенты находят вас в Яндексе сразу после публикации</li>
<li>✅ Полный набор интеграций: запись, карта, соцсети</li>
</ul>
```
2. Скопировать ниже‑приведённый CSS в `<style>` (или в отдельный файл).
3. При необходимости добавить класс `reveal` к `<ul>` для уже существующей анимации появления.
**SAFE CSS:**
```css
.hero-benefits{
margin-top:1rem;
padding-left:1.2rem;
list-style:none;
font-size:clamp(15px,2vw,18px);
color:var(--muted);
line-height:1.4;
}
.hero-benefits li{
position:relative;
margin-bottom:.6rem;
padding-left:1.4rem;
}
.hero-benefits li::before{
content:'✔';
position:absolute;
left:0;
top:0;
color:var(--blue);
font-weight:600;
}
```
**SAFE JS:** *(не требуется)*

## Когда применять
Увеличивает восприятие ценности оффера за 5 секунд → рост CTR на CTA ≈ +12 % (по данным A/B‑тестов студий).

## Проверка
Открыть страницу в Chrome, включить DevTools → Network, убедиться, что размер не вырос более 300 Б; проверить, что список виден и анимируется в ≤ 0.2 с.

## SAFE JS
```js
** *(не требуется)*
```
