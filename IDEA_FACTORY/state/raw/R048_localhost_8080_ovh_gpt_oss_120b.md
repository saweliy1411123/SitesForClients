# localhost:8080/ovh/gpt-oss-120b  2026-11-17 03:57:39
duration=22.7 error=- attempts=1

IDEA: SKILL — Focus‑Visible Outline  
KNOB: **Name:** focus-visible-outline  
**When to apply:** На любой статический лендинг, где интерактивные ссылки/кнопки (a, .btn‑primary) должны быть доступными для клавиатурных пользователей.  
**Steps:**  
1. Добавить в глобальный CSS селектор `:focus-visible` для всех интерактивных элементов.  
2. Сбросить стандартные outline‑ы и задать кастомный контрастный стиль, сохраняющий визуальную согласованность с дизайном.  
3. При необходимости добавить класс `.no‑focus-visible` к элементам, где визуальный фокус нежелателен (например, при клике мышью).  
4. Тестировать в Chrome/Firefox с включённым `Tab`‑навигацией и в режимах высокой контрастности.  

**SAFE CSS:**  
```css
/* focus-visible‑outline – улучшение доступности */
a:focus-visible,
button:focus-visible,
[role="button"]:focus-visible,
.btn-primary:focus-visible {
  outline: 3px solid var(--blue);
  outline-offset: 2px;
  border-radius: 4px;
}

/* Сброс стандартного outline, если нужен только кастомный */
a:focus,
button:focus,
[role="button"]:focus,
.btn-primary:focus {
  outline: none;
}

/* Класс для отключения кастомного фокуса (опционально) */
.no-focus-visible:focus-visible {
  outline: none;
}
```  

**SAFE JS:** *(не требуется)*  

EFFECT: Улучшает восприятие сайта пользователями клавиатуры → повышает показатель Accessibility и потенциально конверсию за счёт снижения барьера выхода.  
RISK: Минимальный – возможен конфликт с уже существующими кастомными `outline`‑правилами; решение – проверка стилей перед внедрением.  
ROLLBACK: `git checkout HEAD -- index.html` (или удалить добавленные правила из CSS).  
VERIFY: Открыть страницу, нажать `Tab` — виден новый синий контур на всех ссылках/кнопках; отключить стили в DevTools – визуальный стиль исчезает.  
PRIORITY: 1 — доступность критична, изменение небольшое, быстрый ROI через улучшение Core Web Vitals (Accessibility).  

---  

IDEA: SKILL — Mobile VH Fix  
KNOB: **Name:** mobile-vh-fix  
**When to apply:** На одностраничных лендингах с полноэкранными секциями (например, `.hero`), где высота `100vh` приводит к обрезке контента на мобильных браузерах с динамической адресной строкой.  
**Steps:**  
1. В `<head>` добавить небольшой скрипт, который вычисляет реальную высоту окна и сохраняет её в CSS‑переменную `--vh`.  
2. Заменить все `height: 100vh` и `min-height: 100vh` на `height: calc(var(--vh, 1vh) * 100)` и аналогично для `min-height`.  
3. При изменении ориентации/размера окна пересчитывать переменную (`resize` и `orientationchange`).  
4. Проверить визуально на Android / iOS‑эмуляторах, убедиться, что первый экран полностью виден без прокрутки.  

**SAFE CSS:**  
```css
/* mobile‑vh‑fix – использование CSS‑переменной для корректной высоты */
.hero {
  min-height: calc(var(--vh, 1vh) * 100);
}
section.fullscreen {
  height: calc(var(--vh, 1vh) * 100);
}
```  

**SAFE JS:**  
```js
/* mobile‑vh‑fix – вычисление реального vh */
(function () {
  const setVH = () => {
    const vh = window.innerHeight * 0.01;
    document.documentElement.style.setProperty('--vh', `${vh}px`);
  };
  setVH();
  window.addEventListener('resize', setVH);
  window.addEventListener('orientationchange', setVH);
})();
```  

EFFECT: Устраняет «потерянный» контент на мобильных устройствах, улучшая пользовательский опыт и показатель CLS → потенциальный рост конверсий.  
RISK: Требует небольшого JS‑фрагмента; если пользователь отключит JS, высота вернётся к обычному `100vh` (не критично).  
ROLLBACK: Удалить `<script>` и CSS‑правила, либо выполнить `git checkout HEAD -- index.html`.  
VERIFY: Открыть страницу на мобильном эмуляторе (Chrome DevTools → Device Toolbar), убедиться, что верхний и нижний край секций полностью видим без скролла; сравнить с версией без скрипта.  
PRIORITY: 2 — значительное улучшение мобильного UX, но требует небольшого кода; стоит реализовать после базовых SEO‑улучшений.
