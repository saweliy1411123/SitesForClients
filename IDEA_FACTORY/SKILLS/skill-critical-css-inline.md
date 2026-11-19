---
name: SKILL — critical-css-inline
source: localhost:8080/ovh/gpt-oss-120b
round: 132
status: proposed
portable: true
tags: [static-landing, portable, responsive]
---

# SKILL — critical-css-inline

**Name:** critical-css-inline
**When to apply:** На любой статический лендинг, где важен быстрый первый рендер (например, hero‑секция и верхний блок контента).
**Steps:**
1. Определить набор CSS‑прав, отвечающих только за стили выше‑скролла (`.hero`, `.nav`, `.hero h1`, `.hero p.sub`, `.nav-links`, `.btn-primary` и т.п.).
2. Скопировать эти правила в отдельный блок `<style data-critical>` сразу после `<meta charset="utf-8">`.
3. Оставить оригинальный `<link rel="stylesheet" href="styles.css">` но добавить атрибут `media="print"` и `onload="this.media='all'"` для отложенной загрузки.
4. При необходимости добавить небольшую JS‑прошивку, которая после `load` удалит атрибут `media` у линка, чтобы стили применились без повторного рендера.
**SAFE CSS:**
```css
/* Critical CSS – above‑the‑fold */
.hero{position:relative;min-height:100vh;display:flex;align-items:center;padding:130px 0 100px;overflow:hidden}
.hero .wrap{position:relative;z-index:3}
.hero h1{font-size:clamp(32px,6vw,58px);font-weight:700;line-height:1.2}
.hero p.sub{color:#c3cad9;font-size:clamp(16.5px,2vw,20px);max-width:560px;margin:28px 0 38px}
.nav{display:flex;justify-content:space-between;align-items:center;padding:20px}
.nav-links{display:flex;gap:28px;font-size:14px;color:var(--muted);font-weight:500}
.btn-primary{display:inline-flex;align-items:center;justify-content:center;padding:12px 24px;background:var(--grad);color:#fff;border-radius:6px;text-decoration:none}
```
**SAFE JS:**
```js
document.addEventListener('load',function(){
const ss=document.querySelector('link[rel="stylesheet"][media="print"]');
if(ss) ss.media='all';
});
```

## Когда применять
Сокращение LCP — критический CSS будет применён сразу, без дополнительного сетевого запроса, что ускорит отрисовку первого экрана и повысит конверсию.

## Проверка
Открыть страницу в DevTools → Network, отключить кэш, убедиться, что запрос к `styles.css` происходит только после `load`, а первые стили уже применены (видно в вкладке Elements → <style data-critical>).

## SAFE CSS
```css
**
```css
/* Critical CSS – above‑the‑fold */
.hero{position:relative;min-height:100vh;display:flex;align-items:center;padding:130px 0 100px;overflow:hidden}
.hero .wrap{position:relative;z-index:3}
.hero h1{font-size:clamp(32px,6vw,58px);font-weight:700;line-height:1.2}
.hero p.sub{color:#c3cad9;font-size:clamp(16.5px,2vw,20px);max-width:560px;margin:28px 0 38px}
.nav{display:flex;justify-content:space-between;align-items:center;padding:20px}
.nav-links{display:flex;gap:28px;font-size:14px;color:var(--muted);font-weight:500}
.btn-primary{display:inline-flex;align-items:center;justify-content:center;padding:12px 24px;background:var(--grad);color:#fff;border-radius:6px;text-decoration:none}
```
**SAFE JS:**
```js
document.addEventListener('load',function(){
const ss=document.querySelector('link[rel="stylesheet"][media="print"]');
if(ss) ss.media='all';
});
```
```

## SAFE JS
```js
**
```js
document.addEventListener('load',function(){
const ss=document.querySelector('link[rel="stylesheet"][media="print"]');
if(ss) ss.media='all';
});
```
```
