---
name: SKILL — grad-text-shimmer (живой блик по градиентному тексту h1)
source: lareper/glm-5.2-fast-preview
round: 119
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — grad-text-shimmer (живой блик по градиентному тексту h1)

SKILL — grad-text-shimmer
Name: `grad-text-shimmer`
When to apply: на любом лендинге, где заголовок h1 содержит акцентный градиентный `<span>` (здесь `.grad-text` в h1, L459) и нужен тонкий премиальный акцент.
Steps:
1. К существующему правилу `.grad-text` (L115) добавить анимацию блика поверх градиента.
2. Вставить SAFE CSS.
3. Ничего в разметке менять не нужно — работает на текущем span.
SAFE CSS:
```css

## Когда применять


## Проверка


## SAFE CSS
```css
```css
```
