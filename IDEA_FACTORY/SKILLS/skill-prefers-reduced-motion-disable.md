---
name: SKILL — prefers-reduced-motion-disable
source: localhost:8080/ovh/gpt-oss-120b
round: 104
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — prefers-reduced-motion-disable

**Name:** prefers-reduced-motion-disable
**When to apply:** На любом статическом лендинге, где присутствуют CSS‑анимации (переходы, keyframes, scroll‑reveal).
**Steps:**
1. Добавить в корневой `:root` переменную `--anim-duration` со значением `1s`.
2. Везде, где используется `animation-duration` или `transition-duration`, заменить фиксированные значения на `var(--anim-duration)`.
3. Добавить медиазапрос `@media (prefers-reduced-motion: reduce)` — устанавливающий `--anim-duration: 0s;` и `animation-name: none;`.
4. (Опционально) добавить класс `.no-anim` для элементов, где анимация критична, и переопределять её вручную.
**SAFE CSS:**
```css
:root{--anim-duration:1s}
*{transition-duration:var(--anim-duration)!important;
animation-duration:var(--anim-duration)!important}
@media (prefers-reduced-motion:reduce){
:root{--anim-duration:0s}
*{animation:none!important;
transition:none!important}
}
```
**SAFE JS:** (не требуется)

## Когда применять
Пользователи, включившие «prefers‑reduced‑motion», не увидят анимаций → повышается доступность и соответствие WCAG 2.1 AA/AAA.

## Проверка
В Chrome DevTools включить имитацию «prefers‑reduced‑motion» (Settings → Rendering → Emulate CSS media) и убедиться, что все анимации и переходы прекращаются без ошибок.

## SAFE JS
```js
** (не требуется)
```
