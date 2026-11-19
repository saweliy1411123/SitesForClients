---
name: SKILL — card-hover-lift-and-shadow (премиальное поднятие карточек с мягкой тенью при наведении)
source: localhost:8081/fast
round: 111
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — card-hover-lift-and-shadow (премиальное поднятие карточек с мягкой тенью при наведении)

Полное тело скилла:
**Name:** `card-hover-lift-and-shadow`
**When to apply:** На любом лендинге с карточками (услуги, цены, демо-концепты, шаги), где нужно усилить интерактивность и «дорогой» отклик на hover.
**Steps:**
1. Найти все карточки (`.price-card`, `.demo-card`, `.step-card` и т.п.).
2. Добавить CSS-правила для `:hover` и `:focus-visible`.
3. Для плавности добавить `transition` в базовое состояние.
**SAFE CSS:**
```css
.price-card,.demo-card,.step-card{transition:transform .35s cubic-bezier(.22,.61,.36,1),box-shadow .35s ease;will-change:transform}
.price-card:hover,.demo-card:hover,.step-card:hover{transform:translateY(-8px) scale(1.02);box-shadow:0 24px 60px rgba(0,0,0,.18),0 8px 24px rgba(139,92,246,.12)}
.price-card:focus-visible,.demo-card:focus-visible,.step-card:focus-visible

## Когда применять


## Проверка


## SAFE CSS
```css
**
```css
.price-card,.demo-card,.step-card{transition:transform .35s cubic-bezier(.22,.61,.36,1),box-shadow .35s ease;will-change:transform}
.price-card:hover,.demo-card:hover,.step-card:hover{transform:translateY(-8px) scale(1.02);box-shadow:0 24px 60px rgba(0,0,0,.18),0 8px 24px rgba(139,92,246,.12)}
.price-card:focus-visible,.demo-card:focus-visible,.step-card:focus-visible
```
