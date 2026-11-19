---
name: Реализовать CSS‑scroll‑snap карусель отзывов в секции «Отзывы и работы»
source: localhost:8080/ovh/gpt-oss-120b
round: 60
status: proposed
portable: true
tags: [static-landing, portable]
---

# Реализовать CSS‑scroll‑snap карусель отзывов в секции «Отзывы и работы»

Обернуть существующие карточки отзывов в `<div class="testimonial-carousel" tabindex="0">`; добавить CSS:
SAFE CSS:
```css
.testimonial-carousel{
display:flex;overflow-x:auto;scroll-snap-type:x mandatory;
-webkit-overflow-scrolling:touch;
}
.testimonial-carousel > *{
flex:0 0 80%;margin-right:1rem;scroll-snap-align:start;
}
.testimonial-carousel::-webkit-scrollbar{display:none;}
```

## Когда применять
Позволит пользователям быстро просматривать отзывы без JavaScript, повышая вовлечённость и доверие

## Проверка
Прокрутить секцию в браузере, убедиться, что карточки «прилипают» к краю; проверить на мобильных устройствах, что свайп работает
