---
name: SKILL — premium-hero-gradient-sweep
source: localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct
round: 90
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — premium-hero-gradient-sweep


**Name:** `premium-hero-gradient-sweep`
**When to apply:** На любом статическом лендинге, где герой-секция является основным элементом привлечения внимания.
**SAFE CSS:**
```css
.hero {
background: linear-gradient(120deg, var(--grad) 0%, var(--grad) 100%);
background-clip: text;
-webkit-background-clip: text;
color: transparent;
}
.hero h1 {
font-size: clamp(34px, 5vw, 58px);
font-weight: 700;
line-height: 1.2;
margin: 0 auto 20px;
max-width: 780px;
text-align: center;
}
.hero h1 span {
background: var(--grad);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
}
```

## Когда применять
Улучшение визуальной привлекательности герой-секции за счет применения градиентного эффекта, что делает ее более заметной и привлекательной для пользователей.

## Проверка
Проверить визуальную привлекательность герой-секции после применения градиентного эффекта.
