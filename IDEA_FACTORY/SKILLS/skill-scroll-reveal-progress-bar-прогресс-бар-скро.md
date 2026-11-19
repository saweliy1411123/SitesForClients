---
name: SKILL — scroll-reveal-progress-bar (прогресс-бар скролла с градиентом и glow-эффектом)
source: localhost:8081/fast
round: 111
status: proposed
portable: true
tags: [static-landing, portable]
---

# SKILL — scroll-reveal-progress-bar (прогресс-бар скролла с градиентом и glow-эффектом)

Полное тело скилла:
**Name:** `scroll-reveal-progress-bar`
**When to apply:** На любом статическом лендинге с вертикальным скроллом, где нужно визуально показать прогресс чтения и повысить вовлечённость.
**Steps:**
1. В `<body>` сразу после `<header>` добавить `<div class="scroll-progress" aria-hidden="true"><span></span></div>`.
2. В `<style>` добавить CSS (см. SAFE CSS).
3. Если нужен JS — добавить SAFE JS для обновления ширины.
**SAFE CSS:**
```css
.scroll-progress{position:fixed;top:0;left:0;width:100%;height:4px;z-index:9999;background:transparent;pointer-events:none}
.scroll-progress span{display:block;height:100%;width:0;background:linear-gradient(90deg,#8b5cf6,#ec4899,#f59e0b);border-radius:0 2px 2px 0;box-shadow:0 0 12px rgba(139,92,246,.6);transition:width .1s linear;will-change:width}
```
**SAFE JS:**
```js
(function(){var bar=document.querySelector('.scroll-progress span');if(!bar)return;function update(){var h=document.documentElement;var max=h.scrollHeight-h.clientHeight;var p=max>0?(h.scrollTop||document.body.scrollTop)/max*100:0;bar.style.width=p+'%';}window.addEventListener('scroll',update,{passive:true});window.addEventListener('resize',update);update();})();
```

## Когда применять
Визуальный индикатор прогресса чтения — пользователь видит, сколько осталось, что повышает удержание и снижает bounce-rate; добавляет премиальный «дорогой» вид.

## Проверка
Открыть index.html, проскроллить — полоска плавно заполняется от 0 до 100%.

## SAFE CSS
```css
**
```css
.scroll-progress{position:fixed;top:0;left:0;width:100%;height:4px;z-index:9999;background:transparent;pointer-events:none}
.scroll-progress span{display:block;height:100%;width:0;background:linear-gradient(90deg,#8b5cf6,#ec4899,#f59e0b);border-radius:0 2px 2px 0;box-shadow:0 0 12px rgba(139,92,246,.6);transition:width .1s linear;will-change:width}
```
**SAFE JS:**
```js
(function(){var bar=document.querySelector('.scroll-progress span');if(!bar)return;function update(){var h=document.documentElement;var max=h.scrollHeight-h.clientHeight;var p=max>0?(h.scrollTop||document.body.scrollTop)/max*100:0;bar.style.width=p+'%';}window.addEventListener('scroll',update,{passive:true});window.addEventListener('resize',update);update();})();
```
```

## SAFE JS
```js
**
```js
(function(){var bar=document.querySelector('.scroll-progress span');if(!bar)return;function update(){var h=document.documentElement;var max=h.scrollHeight-h.clientHeight;var p=max>0?(h.scrollTop||document.body.scrollTop)/max*100:0;bar.style.width=p+'%';}window.addEventListener('scroll',update,{passive:true});window.addEventListener('resize',update);update();})();
```
```
