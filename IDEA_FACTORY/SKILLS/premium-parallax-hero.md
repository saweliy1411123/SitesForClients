---
name: premium-parallax-hero
source: localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct
round: 84
status: proposed
portable: true
tags: [static-landing, portable]
---

# premium-parallax-hero


**Name:** `premium-parallax-hero`
**When to apply:** На любом статическом лендинге, где герой-секция имеет большой фон.
**SAFE CSS:**
```css
.hero {
background-size: 150% auto;
background-position: 50% 50%;
}
.hero::before {
content: '';
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background: linear-gradient(to bottom, var(--bg), var(--bg));
background-size: 150% auto;
background-position: 50% 50%;
transform: translateZ(-10px);
transition: transform 0.5s ease;
}
.hero:hover::before {
transform: translateZ(0);
}
```

## Когда применять
Создаст премиальный параллакс-эффект в герой-секции.

## Проверка
Проверить работу параллакс-эффекта в разных браузерах и на разных устройствах.
