---
name: SKILL — depth-layer-parallax (многослойный 3D-параллакс фона секций с translateZ и scroll-слоями)
source: lareper/glm-5.2
round: 77
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — depth-layer-parallax (многослойный 3D-параллакс фона секций с translateZ и scroll-слоями)



## Когда применять
ощущение дорогого «глубокого» сайта, дольше удержание внимания, премиальность без единой внешней библиотеки; вес <1 КБ JS.

## Проверка
открыть копию index.improved.html, прокрутить — фоновые слои смещаются медленнее контента; в DevTools → Rendering → Paint flashing нет постоянной перекраски всего экрана; на эмуляции touch эффекта нет.
