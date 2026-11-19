---
name: SKILL — glassy-nav-scroll
source: localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct
round: 112
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — glassy-nav-scroll


**Name:** `glassy-nav-scroll`
**When to apply:** На любом лендинге с фиксированным верхним меню, где нужен премиальный вид навигации.
**SAFE CSS:**
```css
.glassy-nav-scroll {
background: linear-gradient(to bottom, var(--nav-bg-start), var(--nav-bg-end));
backdrop-filter: blur(20px);
padding: 1rem;
position: sticky;
top: 0;
z-index: 1000;
}
```

## Когда применять
Пользователи будут испытывать премиальный эффект навигации при скролле страницы.

## Проверка
Проверить визуальное качество и корректность скилла на разных устройствах и разрешениях.
