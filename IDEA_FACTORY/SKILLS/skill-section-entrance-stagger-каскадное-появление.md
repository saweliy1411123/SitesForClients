---
name: SKILL — section-entrance-stagger (каскадное появление блоков секции при скролле с резервом для no-JS)
source: lareper/glm-5.2
round: 90
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — section-entrance-stagger (каскадное появление блоков секции при скролле с резервом для no-JS)

SKILL — section-entrance-stagger
Название: `section-entrance-stagger`
Когда применять: на любом одностраничном лендинге, где секции/карточки появляются резко или без анимации; даёт «дорогую» каскадную анимацию появления (IntersectionObserver + CSS-переходы) с гарантией видимости контента при выключенном JS.
Шаги:
1. Вставить SAFE CSS.
2. Вставить SAFE JS перед `</body>`.
3. Разметить нужные элементы классом `.stagger-item` (карточки

## Когда применять


## Проверка

