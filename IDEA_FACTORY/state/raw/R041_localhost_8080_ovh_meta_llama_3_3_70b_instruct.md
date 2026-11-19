# localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct  2026-11-17 03:37:40
duration=18.2 error=- attempts=1

IDEA: SKILL — gradient-heading-premium
KNOB: 
### Название
gradient-heading-premium
### Когда применять
Любой тёмный лендинг с декорированным hero-экраном.
### Шаги
1. Определить селектор для hero-заголовка.
2. Добавить в CSS свойства для градиентной анимации текста.
3. Обеспечить доступность и читаемость текста.

SAFE CSS:
```css
.gradient-heading-premium {
  background: linear-gradient(to right, #ff69b4, #ffe68c);
  background-clip: text;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gradient-animation 10s ease infinite;
}

@keyframes gradient-animation {
  0% {
    background-position: 0% 0%;
  }
  100% {
    background-position: 100% 100%;
  }
}
```
SAFE JS: 
```javascript
// нет необходимости в дополнительном JS-коде
```
VERIFY: Проверить видимость и читаемость текста в hero-заголовке после применения градиентной анимации.
PRIORITY: 2
SITE_REQUEST: gradient
SKILL: gradient-heading-premium
