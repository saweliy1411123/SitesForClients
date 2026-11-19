# localhost:8080/ovh/Meta-Llama-3_3-70B-Instruct  2026-11-17 06:24:47
duration=44.1 error=- attempts=1

IDEA: SKILL — glassmorphic-cta-button
KNOB: 
**Name:** `glassmorphic-cta-button`
**When to apply:** На любом статическом лендинге, где есть CTA-кнопки.
**SAFE CSS:**
```css
.glassmorphic-cta-button {
  background: linear-gradient(145deg, #fff 0%, #fff 100%);
  box-shadow: 6px 9px 20px -5px rgba(0, 0, 0, 0.1), 
              -10px -5px 30px 10px rgba(0, 0, 0, 0.2);
  border-radius: 20px;
  padding: 10px 20px;
  font-size: 16px;
  font-weight: 600;
  color: #333;
  cursor: pointer;
  transition: box-shadow 0.3s ease-in-out;
}

.glassmorphic-cta-button:hover {
  box-shadow: 10px 10px 30px 10px rgba(0, 0, 0, 0.3), 
              -10px -10px 40px 20px rgba(0, 0, 0, 0.2);
}
```
EFFECT: Добавление стиля "glassmorphic" к CTA-кнопкам для улучшения визуальной привлекательности.
RISK: Нет
ROLLBACK: Удаление класса `glassmorphic-cta-button` из CSS.
VERIFY: Проверка визуальной привлекательности кнопок после добавления класса.
PRIORITY: 2
SITE_REQUEST: btn-primary
