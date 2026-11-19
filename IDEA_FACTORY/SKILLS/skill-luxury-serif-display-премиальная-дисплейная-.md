---
name: SKILL — luxury-serif-display (премиальная дисплейная типографика заголовков)
source: lareper/glm-5.3
round: 91
status: proposed
portable: true
tags: [static-landing, portable, responsive]
---

# SKILL — luxury-serif-display (премиальная дисплейная типографика заголовков)

Полное тело скилла:
**Name:** `luxury-serif-display`
**When to apply:** На любом лендинге, где заголовки h1/h2 набраны одним гротеском и выглядят «плоско». Шаги: (1) в `<head>` добавить второй display-шрифт (Playfair Display / Prata через Google Fonts, только вес 700, `display=swap`); (2) применить его только к h1 и `.grad-text`-частям заголовков — гротеск остаётся для текста; (3) добавить `letter-spacing:-.02em` и `font-feature-settings:"liga"`; (4) проверить на мобильных, что размер не ломает строки.
SAFE CSS:
```
h1, .final h2, .price-card h3{
font-family:'Playfair Display', Georgia, serif;
letter-spacing:-.02em;
font-feature-settings:"liga" 1;
}
@media(max-width:480px){ h1{font-size:clamp(28px,7vw,40px);} }
```

## Когда применять
визуально «дорогой» контраст serif-заголовков на фоне гротескного текста — классический приём премиум-брендов; рост воспринимаемой ценности услуги без изменения контента.

## Проверка
открыть index.improved.html, сравнить hero и секцию цены с оригиналом; в DevTools → Network убедиться, что шрифт грузится один раз; сузить окно до 375px — заголовки не переносятся по буквам.

## SAFE CSS
```css
```
h1, .final h2, .price-card h3{
font-family:'Playfair Display', Georgia, serif;
letter-spacing:-.02em;
font-feature-settings:"liga" 1;
}
@media(max-width:480px){ h1{font-size:clamp(28px,7vw,40px);} }
```
```
