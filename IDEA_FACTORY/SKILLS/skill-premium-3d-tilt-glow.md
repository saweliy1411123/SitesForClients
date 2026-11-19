---
name: SKILL — premium-3d-tilt-glow
source: localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct
round: 27
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — premium-3d-tilt-glow


### Название
premium-3d-tilt-glow
### Когда применять
Любой лендинг, где карточки демо-концептов должны привлекать внимание и выглядеть премиально.
### Шаги
1. Обернуть каждый блок демо-концепта в `<div class="glass-card">`.
2. Добавить в CSS:
```css
.glass-card{
background: linear-gradient(to bottom right, #fff, #fff2);
backdrop-filter: blur(16px);
border-radius: 16px;
box-shadow: 0 4px 6px rgba(0,0,0,.1), 0 8px 16px rgba(0,0,0,.1);
transition: transform .3s;
}
.glass-card:hover{
transform: rotateY(5deg) scale(1.05);
}
```
SAFE CSS:
```css
.glass-card{
background: linear-gradient(to bottom right, #fff, #fff2);
backdrop-filter: blur(16px);
border-radius: 16px;
box-shadow: 0 4px 6px rgba(0,0,0,.1), 0 8px 16px rgba(0,0,0,.1);
transition: transform .3s;
}
.glass-card:hover{
transform: rotateY(5deg) scale(1.05);
}
```

## Когда применять
Премиальный вид карточек демо-концептов с эффектом глубины и светимости.

## Проверка
Проверить визуально на разных устройствах и браузерах.
