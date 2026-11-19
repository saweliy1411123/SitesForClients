# localhost:8080/zhipu/glm-4.7-flash  2026-11-17 09:24:17
duration=47.7 error=- attempts=2

IDEA: Микро-взаимодействие для ссылок-кнопок (Link-Button Press)
KNOB: Добавить состояния `:hover` и `:active` к селектору `.btn-primary` (это ссылки-кнопки) для имитации нажатия физической кнопки. В CSS добавить `transform: scale` и `box-shadow`.
EFFECT: Создает тактильный отклик при взаимодействии, повышает ощущение "кликабельности" CTA.
RISK: Нет.
ROLLBACK: Удалить добавленные строки CSS.
VERIFY: Навести курсор и кликнуть по кнопке в Hero и финале.
PRIORITY: 2
SITE_REQUEST: hero
SKILL: micro-cta-link-press
SAFE CSS:
```css
.btn-primary:hover {
    transform: scale(1.02);
    box-shadow: 0 4px 12px rgba(139, 92, 246, 0.4);
}
.btn-primary:active {
    transform: scale(0.98);
    box-shadow: 0 2px 8px rgba(139, 92, 246, 0.3);
}
```

IDEA: Skeleton Loader для Hero-секции
KNOB: В HTML секции `.hero` (внутри `<div class="wrap">`) добавить `<div class="hero-skeleton"></div>`. В JS (внутри `<script>`) добавить строку `document.querySelector('.hero-skeleton').remove();` перед рендером частиц/градиентов.
EFFECT: Устраняет эффект "мигания" (FOUC) при загрузке тяжелых градиентов и скриптов, сайт выглядит профессиональнее.
RISK: Нет.
ROLLBACK: Удалить добавленный div и JS строку.
VERIFY: Обновить страницу, проверить отсутствие пустого блока перед появлением контента.
PRIORITY: 3
SITE_REQUEST: hero
SKILL: skeleton-hero-loader
SAFE CSS:
```css
.hero-skeleton {
    width: 100%;
    height: 300px;
    background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
    background-size: 200% 100%;
    animation: shimmer 1.5s infinite;
    border-radius: 8px;
}
@keyframes shimmer {
    0% { background-position: 200% 0; }
    100% { background-position: -200% 0; }
}
```
SAFE JS:
```javascript
const skeleton = document.querySelector('.hero-skeleton');
if (skeleton) skeleton.remove();
```
