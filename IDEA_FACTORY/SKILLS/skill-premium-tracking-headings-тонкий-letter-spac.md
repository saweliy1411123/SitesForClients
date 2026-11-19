---
name: SKILL — premium-tracking-headings (тонкий letter-spacing/word-spacing ритм для «дорогой» типографики)
source: lareper/glm-5.3-prime
round: 105
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — premium-tracking-headings (тонкий letter-spacing/word-spacing ритм для «дорогой» типографики)

SKILL — premium-tracking-headings
Name: `premium-tracking-headings`
When to apply: на любом лендинге, где крупные заголовки (h1/h2) выглядят «плотно» и дёшево из-за дефолтного трекинга; особенно при отрицательном letter-spacing, доведённом до экстремума.
Steps:
1. Найти текущие значения letter-spacing у h1/h2 (у `.price-card .price` уже −.04em — экстремум).
2. Задать иерархию трекинга: чем крупнее текст — тем плотнее, но в пределах −.01…−.03em; крупным цифрам цены вернуть −.02em вместо −.04em.
3. Добавить `font-feature-settings:"k

## Когда применять


## Проверка

