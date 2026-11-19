---
name: SKILL — «Мягкое свечение CTA при появлении в вьюпорте» (cta-glow-pulse)
source: lareper/glm-5.3
round: 20
status: proposed
portable: true
tags: [static-landing, portable, animation, responsive]
---

# SKILL — «Мягкое свечение CTA при появлении в вьюпорте» (cta-glow-pulse)

Название: **cta-glow-pulse**. Когда применять: любой лендинг, где главный CTA — ссылка `.btn-primary` (или аналог), находится ниже первого экрана (final-секция), и нужно привлечь внимание без агрессивных миганий. Шаги:
1. Добавить SAFE CSS в `<style>`.
2. Добавить SAFE JS в конец `<body>`: IntersectionObserver вешает класс `.is-visible` на CTA, когда он входит во вьюпорт; анимация пульса проигрывается 2 раза и останавливается (не бесконечная — уважает внимание и reduced-motion).
3. Не менять разметку кнопки — только классы.
4. Проверить: при `prefers-reduced-motion: reduce` анимация полностью отключена.
SAFE CSS:
.btn-primary{position:relative}
@keyframes cta-glow{0%,100%{box-shadow:0 0 0 0 rgba(139,92,246,0)}50%{box-shadow:0 0 0 10px rgba(139,92,246,.25)}}
.btn-primary.is-visible{animation:cta-glow 1.2s ease-in-out 2}
@media (prefers-reduced-motion: reduce){.btn-primary.is-visible{animation:none}}
SAFE JS:
document.querySelectorAll('.btn-primary').forEach(function(b){
if(!('IntersectionObserver

## Когда применять


## Проверка


## SAFE CSS
```css
.btn-primary{position:relative}
@keyframes cta-glow{0%,100%{box-shadow:0 0 0 0 rgba(139,92,246,0)}50%{box-shadow:0 0 0 10px rgba(139,92,246,.25)}}
.btn-primary.is-visible{animation:cta-glow 1.2s ease-in-out 2}
@media (prefers-reduced-motion: reduce){.btn-primary.is-visible{animation:none}}
```
