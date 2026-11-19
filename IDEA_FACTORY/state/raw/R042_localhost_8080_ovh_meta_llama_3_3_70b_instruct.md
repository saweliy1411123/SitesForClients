# localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct  2026-11-17 03:40:40
duration=14.6 error=- attempts=1

IDEA: hero-clarity-boost
KNOB: 
### Название
hero-clarity-boost
### Когда применять
На лендингах с первым экраном (hero), где оффер и CTA не сразу понятны.
### Шаги
1. Добавить под h1 список益 «что вы получите» (ul/li).
2. Улучшить контраст и читаемость текста hero.
3. Добавить атрибут aria-label к кнопке CTA.

SAFE CSS:
```css
.hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 40px 0;
}

.hero h1 {
  font-size: 36px;
  font-weight: 600;
  margin-bottom: 20px;
}

.hero ul {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.hero li {
  margin: 10px;
  font-size: 18px;
}

.hero li::before {
  content: "\2713";
  margin-right: 10px;
  font-weight: bold;
  color: #8b5cf6;
}

.btn-primary {
  transition: filter 0.3s ease;
}

.btn-primary:hover {
  filter: drop-shadow(0 2px 4px rgba(0, 0, 0, 0.2));
}
```
SAFE JS:
```javascript
// нет
```
VERIFY: открыть index.html в браузере и проверить видимость и читаемость hero.
PRIORITY: 2
SITE_REQUEST: hero
