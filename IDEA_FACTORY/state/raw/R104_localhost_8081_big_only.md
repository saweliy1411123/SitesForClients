# localhost:8081/big_only  2026-11-17 06:48:05
duration=27.7 error=- attempts=2

IDEA: Ripple‑effect на CTA‑кнопках  
KNOB: **SKILL — ripple-effect-cta-button**  
**Name:** ripple-effect-cta-button  
**When to apply:** На любом статическом лендинге, где CTA реализованы ссылками `<a class="btn-primary">`.  
**Steps:**  
1. Добавить класс `.btn-ripple` к каждому CTA‑ссылке (например, `<a href="#price" class="btn-primary btn-ripple">`).  
2. Вставить в `<head>` блок `<style>` с SAFE CSS (см. ниже).  
3. При желании добавить лёгкий SAFE JS, который удаляет анимацию после её завершения (см. ниже).  

**SAFE CSS:**  
```css
/* ripple effect */
.btn-ripple {
  position: relative;
  overflow: hidden;
}
.btn-ripple::after {
  content: "";
  position: absolute;
  left: 50%;
  top: 50%;
  width: 0;
  height: 0;
  background: rgba(255,255,255,0.3);
  border-radius: 50%;
  transform: translate(-50%, -50%);
  transition: width .4s ease-out, height .4s ease-out, opacity .6s;
  pointer-events: none;
}
.btn-ripple:active::after {
  width: 200px;
  height: 200px;
  opacity: 0;
}
```

**SAFE JS (optional):**  
```js
// Убираем оставшийся псевдо‑элемент после анимации (чисто для старых браузеров)
document.querySelectorAll('.btn-ripple').forEach(btn=>{
  btn.addEventListener('transitionend',e=>{
    if(e.propertyName==='opacity') btn.classList.remove('ripple-running');
  });
});
```  

EFFECT: Увеличивает ощущение интерактивности CTA, повышает конверсию за счёт микровзаимодействия.  
RISK: Возможен конфликт с существующими стилями `.btn-primary` (перекрытие `overflow`).  
ROLLBACK: `git checkout -- index.html` (или вернуть предыдущий коммит).  
VERIFY: Открыть страницу, навести курсор и кликнуть по любой `.btn-primary`. Должен появиться плавный радиальный всплеск. Проверить, что остальные стили кнопки не изменились.  
PRIORITY: 2 – небольшие изменения, быстрый эффект UX без риска для SEO.  

---  

IDEA: Плавающий фиксированный хедер после скролла (sticky‑header‑reveal)  
KNOB: **SKILL — sticky-header-reveal**  
**Name:** sticky-header-reveal  
**When to apply:** На лендингах с крупным `<header class="hero">` и навигационными ссылками, где полезно сохранять доступ к меню при прокрутке.  
**Steps:**  
1. Добавить в `<body>` элемент `<header class="sticky-header">` с теми же навигационными ссылками, что в `.hero .nav-links`.  
2. Вставить в `<head>` блок `<style>` с SAFE CSS (см. ниже).  
3. Добавить лёгкий SAFE JS, который добавляет класс `.scrolled` к `body` при прокрутке > 80 px.  

**SAFE CSS:**  
```css
/* базовый скрытый хедер */
.sticky-header {
  position: sticky;
  top: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 12px 0;
  background: var(--bg);
  box-shadow: 0 2px 8px rgba(0,0,0,.1);
  opacity: 0;
  transform: translateY(-100%);
  transition: opacity .3s ease, transform .3s ease;
  z-index: 1000;
}

/* видимый после скролла */
body.scrolled .sticky-header {
  opacity: 1;
  transform: translateY(0);
}
```

**SAFE JS:**  
```js
// Добавляем/удаляем класс .scrolled на body при прокрутке
window.addEventListener('scroll',()=>{
  if(window.scrollY>80) document.body.classList.add('scrolled');
  else document.body.classList.remove('scrolled');
});
```  

EFFECT: Улучшает навигацию и удерживает пользовательский фокус на CTA‑ссылках, повышая вероятность перехода к важным секциям.  
RISK: Добавление нового `<header>` может слегка увеличить размер HTML; если уже есть фиксированный хедер, может возникнуть дублирование.  
ROLLBACK: Удалить вставленные блоки `.sticky-header`, CSS и JS; `git checkout -- index.html`.  
VERIFY: Прокрутить страницу вниз более чем на 80 px – верхний хедер должен плавно появиться. Проверить, что ссылки работают и не перекрываются другими элементами.  
PRIORITY: 2 – небольшие изменения, положительно влияют на UX и удержание пользователя без риска для SEO.  

SKILL: ripple-effect-cta-button  
SKILL: sticky-header-reveal
