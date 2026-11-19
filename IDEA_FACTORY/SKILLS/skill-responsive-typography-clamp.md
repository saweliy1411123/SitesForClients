---
name: SKILL — responsive-typography-clamp
source: localhost:8080/ovh/gpt-oss-120b
round: 112
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — responsive-typography-clamp

Заменить фиксированные размеры шрифтов в стилях заголовков (`h1, h2, h3`) на fluid‑типы с `clamp()`. Пример:
```css
/* SAFE CSS */
h1 { font-size: clamp(2rem, 5vw + 1rem, 3.5rem); }
h2 { font-size: clamp(1.75rem, 4vw + 0.8rem, 2.8rem); }
h3 { font-size: clamp(1.5rem, 3.5vw + 0.6rem, 2.2rem); }
```

## Когда применять
Текст автоматически подстраивается под ширину экрана, улучшая читаемость и эстетический вид на всех устройствах без медиа‑запросов.

## Проверка
Открыть страницу в Chrome DevTools, переключать ширину окна и убедиться, что размеры заголовков плавно меняются в пределах заданных границ.
