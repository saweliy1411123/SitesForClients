# localhost:8080/ovh/gpt-oss-120b  2026-11-17 06:04:18
duration=26.3 error=- attempts=1

IDEA: SKILL — content‑visibility‑auto (lazy‑render секций ниже фолда)  
KNOB: **Name:** `content-visibility-auto`  
**When to apply:** На любой одностраничный лендинг, где ниже‑фолд контент тяжёлый (текст, карточки, изображения) и нужен быстрый First Contentful Paint.  
**Steps:**  
1. Открыть `index.html` и добавить в конец `<style>` блок ниже существующего CSS.  
2. Вставить CSS‑правило, которое включает `content-visibility: auto` для всех секций, кроме первой (hero) и навигации.  
3. При желании задать `contain-intrinsic-size` – пример ≈ 600 px, чтобы браузер оставил место до загрузки.  
**SAFE CSS:**  
```css
/* ---------- content‑visibility‑auto ---------- */
section:not(.hero):not(.nav) {
  content-visibility: auto;
  contain-intrinsic-size: 600px;
}
```
**SAFE JS:** *(не требуется)*  
EFFECT: Уменьшает количество DOM‑элементов, отрисовываемых до скролла, тем самым сокращая LCP и CLS → быстрее загрузка, лучше Core Web Vitals, повышается конверсия на мобильных.  
RISK: Если секция сильно меньше 600 px, может появиться «прыжок» при загрузке; но он минимален и легко корректируется.  
ROLLBACK: `git checkout HEAD -- index.html` или удалить только только что добавленный CSS‑блок.  
VERIFY: Открыть страницу в Chrome, открыть DevTools → Performance, выполнить скролл до нижних секций и убедиться, что их `content‑visibility` = `auto` (вкладка Elements → Computed). Затем измерить LCP до и после (можно через `PerformanceObserver` в консоли).  
PRIORITY: 2 – быстрая победа без риска, улучшает Core Web Vitals, но не меняет бизнес‑логики.  

---  

IDEA: SKILL — link‑underline‑reveal (анимированное подчёркивание ссылок‑CTA)  
KNOB: **Name:** `link-underline-reveal`  
**When to apply:** На статических лендингах, где CTA‑ссылки оформлены как `<a class="btn-primary …">` и нужны визуальные подсказки при наведении/фокусе без JavaScript.  
**Steps:**  
1. В конец `<style>` добавить CSS‑правило, которое использует псевдо‑элемент `::after` для создания 2‑px линии, появляющейся слева‑направо.  
2. Применить класс `underline-reveal` к любой ссылке‑CTA (например, добавить к существующим `btn-primary`).  
**SAFE CSS:**  
```css
/* ---------- link‑underline‑reveal ---------- */
.underline-reveal {
  position: relative;
  overflow: hidden;
}
.underline-reveal::after {
  content: "";
  position: absolute;
  left: 0;
  bottom: 0;
  height: 2px;
  width: 0;
  background: var(--grad, #8b5cf6);
  transition: width .25s ease;
}
.underline-reveal:hover::after,
.underline-reveal:focus-visible::after {
  width: 100%;
}
```
**SAFE JS:** *(не требуется)*  
EFFECT: Делает интерактивные ссылки более заметными, усиливает ощущение «кликабельности», повышает коэффициент кликов (CTR) на CTA без добавления лишних элементов.  
RISK: Требует, чтобы у ссылки был `position: relative` (добавлено в правиле) – конфликтов с уже установленными позициями маловероятен.  
ROLLBACK: Удалить только CSS‑блок и убрать класс `underline-reveal` из HTML‑разметки (можно откатить файл через `git checkout`).  
VERIFY: Открыть страницу, навести курсор и/или перейти клавишей Tab к ссылке‑CTA; убедиться, что подчеркивание анимировано от нуля до полной ширины. Проверить отсутствие смещения текста (должно оставаться на месте).  
PRIORITY: 3 – не критично для скорости, но улучшает UX и визуальную иерархию; легко внедряется и откатывается.
