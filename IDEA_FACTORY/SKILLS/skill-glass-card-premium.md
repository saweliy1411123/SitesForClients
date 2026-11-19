---
name: SKILL — glass-card-premium
source: localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct
round: 48
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — glass-card-premium


### Название
glass-card-premium
### Когда применять
тёмный лендинг с цветными фоновыми изображениями
### Шаги
1. Добавить к каждому элементу `.demo-item` класс `.glass-card`.
2. Добавить в `<style>` блок:
```css
.glass-card {
background: linear-gradient(135deg, rgba(139,92,246,.5), transparent 65%);
backdrop-filter: blur(10px);
border-radius: 10px;
padding: 20px;
box-shadow: 0 0 10px rgba(139,92,246,.2);
}
```

## Когда применять
повысить визуальную привлекательность демо-концептов

## Проверка
проверить визуальную привлекательность и читаемость текста на фоне
