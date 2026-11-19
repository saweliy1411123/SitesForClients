# localhost:8080/ovh/gpt-oss-120b  2026-11-17 08:25:16
duration=26.8 error=- attempts=1

IDEA: SKILL — fluid-typography-clamp  
KNOB: **Name:** fluid-typography-clamp  
**When to apply:** На любом статическом лендинге, где используется фиксированное `font-size` в px/rem и требуется адаптивная типографика без множества медиазапросов.  
**Steps:**  
1. Добавить в глобальный CSS блок `SAFE CSS` (см. ниже).  
2. При необходимости задать кастомные переменные `--fs-min` и `--fs-max` в `:root` для разных уровней заголовков.  
3. На нужных элементах добавить класс `.fluid-text` (или `.fluid-h1`, `.fluid-h2` и т.д., если нужны отдельные диапазоны).  
4. При тестировании проверить читаемость на ширине 320 px – 1440 px.  

**SAFE CSS:**  
```css
:root{
  --fs-min: 0.875rem;   /* 14 px */
  --fs-max: 1.25rem;    /* 20 px */
}
.fluid-text{
  font-size: clamp(var(--fs-min), 1.2vw, var(--fs-max));
  line-height: 1.4;
}
.fluid-h1{
  --fs-min: 1.5rem;
  --fs-max: 2.5rem;
  font-size: clamp(var(--fs-min), 2vw, var(--fs-max));
  line-height: 1.2;
}
.fluid-h2{
  --fs-min: 1.25rem;
  --fs-max: 2rem;
  font-size: clamp(var(--fs-min), 1.8vw, var(--fs-max));
  line-height: 1.3;
}
```

EFFECT: Читабельный текст, автоматически подстраивающийся под любые экраны, повышает UX и SEO‑доступность без добавления новых медиазапросов.  
RISK: При экстремальных размерах окна шрифт может стать слишком маленьким/большим — требуется быстрый визуальный чек.  
ROLLBACK: Удалить класс(ы) `.fluid‑*` из HTML и удалить блок CSS из проекта (`git checkout index.html` или `git revert` соответствующего коммита).  
VERIFY: Открыть страницу в Chrome, открыть DevTools → Device Toolbar, переключить между 320 px и 1440 px, убедиться, что размер текста плавно меняется в пределах заданных границ.  
PRIORITY: 2 – значительное улучшение читаемости, но не критично для конверсии.  
SKILL: fluid-typography-clamp  

---  

IDEA: SKILL — section-scroll-snap  
KNOB: **Name:** section-scroll-snap  
**When to apply:** На одностраничных лендингах с несколькими вертикальными секциями, где желателен «прокрутка‑привязка» (scroll‑snap) для создания плавного, контролируемого скроллинга на мобильных и десктоп‑устройствах.  
**Steps:**  
1. Обернуть все основные `<section>` в контейнер `<div class="snap-container">`.  
2. Добавить каждому `<section>` класс `.snap-section`.  
3. Включить глобальный `scroll-behavior: smooth;`.  
4. Добавить CSS‑правила `SAFE CSS` (см. ниже).  
5. Проверить, что ссылки‑якоря (например, в навигации) корректно скроллят к нужным секциям.  

**SAFE CSS:**  
```css
html{
  scroll-behavior: smooth;
}
.snap-container{
  overflow-y: auto;
  height: 100vh;
  scroll-snap-type: y mandatory;
}
.snap-section{
  scroll-snap-align: start;
  min-height: 100vh;
  /* optional: keep existing padding/margin */
}
```

EFFECT: Пользователи ощущают более «погружающий» опыт, легче воспринимают структуру страницы, снижается количество «потерянных» скроллов и повышается время, проведённое на странице.  
RISK: Привязка может конфликтовать с естественным скроллом, особенно если пользователь пытается быстро пролистывать; может нарушать работу кастомных скролл‑скриптов (если появятся в будущем).  
ROLLBACK: Удалить обёртку `.snap-container` и класс `.snap-section` из HTML, а также удалить соответствующие правила из CSS (`git checkout index.html` или `git revert`).  
VERIFY: В Chrome открыть страницу, включить мобильный режим, прокручивать мышью/трекпадом – каждая секция должна «прилипать» к верхней части окна; клик по навигационным ссылкам‑якорям должен плавно вести к секции без «прыжков».  
PRIORITY: 1 – значительное улучшение UX и восприятия контента, особенно на мобильных устройствах, где большинство трафика.  
SKILL: section-scroll-snap
