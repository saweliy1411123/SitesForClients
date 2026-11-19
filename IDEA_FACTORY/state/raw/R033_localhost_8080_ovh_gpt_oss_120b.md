# localhost:8080/ovh/gpt-oss-120b  2026-11-17 03:15:19
duration=32.1 error=- attempts=1

IDEA: Добавить атрибут `lang="ru"` к `<html>`
KNOB: В файл `index.html` изменить открывающий тег `<html>` → `<html lang="ru">`
EFFECT: Улучшит SEO (поисковые системы учитывают язык) и доступность (скрин‑ридеры сразу знают язык контента)
RISK: Минимальный; может потребовать согласования, если сайт планируется многократно локализовать
ROLLBACK: `git checkout -- index.html` (или откатить конкретную строку)
VERIFY: Открыть страницу в Chrome DevTools → Elements, убедиться, что атрибут присутствует; проверить в Lighthouse → Internationalization → Language attribute = ru
PRIORITY: 1 – быстрый и безрисковый апдейт, сразу даёт SEO‑плюс

IDEA: Предзагрузка шрифтов Google Fonts через `preconnect` и `dns-prefetch`
KNOB: В `<head>` добавить две ссылки:  
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
```  
(при желании добавить `dns-prefetch` аналогично)
EFFECT: Сократит время установления соединения с CDN, ускорит отрисовку текста → лучше Core Web Vitals
RISK: Никакого, только небольшое увеличение HEAD‑размера
ROLLBACK: Удалить добавленные строки или выполнить `git checkout -- index.html`
VERIFY: В Chrome DevTools → Network, включить “Disable cache” и обновить страницу; время до первого запроса к `fonts.googleapis.com` должно уменьшиться (< 30 мс)
PRIORITY: 2 – небольшие изменения, заметный прирост скорости

IDEA: Перенести скрипт анимации частиц в `defer` и добавить поддержку `prefers-reduced-motion`
KNOB: 1) В `<script src="...">` добавить атрибут `defer` (или если скрипт inline – обернуть в `<script defer>…</script>`).  
2) В CSS добавить медиа‑правило:  
```css
@media (prefers-reduced-motion: reduce) {
  #particles { display:none; }
}
```  
EFFECT: Скрипт не блокирует парсинг HTML, а пользователи с отключённой анимацией не увидят лишние визуальные эффекты → лучше доступность и время первой отрисовки
RISK: Если скрипт зависит от элементов, которые ещё не созданы к моменту выполнения, может потребоваться небольшая корректировка (обычно `defer` решает)
ROLLBACK: Удалить `defer` и медиа‑правило; `git checkout -- index.html`
VERIFY: Открыть страницу в Chrome → Performance, убедиться, что `script` загружается после `DOMContentLoaded`; включить “Reduced motion” в системных настройках и проверить отсутствие canvas‑анимации
PRIORITY: 2 – повышает перфоманс и удовлетворяет требованиям доступности

IDEA: Добавить `role="alert"` к элементам счётчиков доверия (proof‑item)
KNOB: В HTML обернуть каждый `<em data-count="…">` в `<span class="proof-number" role="alert" aria-live="polite">…</span>`
EFFECT: Скрин‑ридеры объявят изменение цифр как важное уведомление, повышая восприятие динамических доказательств
RISK: Возможна небольшая нагрузка на скрин‑ридер при каждом обновлении счётчика; однако счётчики обновляются один раз при загрузке, так что риск ничтожен
ROLLBACK: Удалить обёртку и атрибуты; `git checkout -- index.html`
VERIFY: Включить VoiceOver/NVDA, перезагрузить страницу, убедиться, что при появлении цифр озвучивается их значение
PRIORITY: 3 – небольшое улучшение доступности, не критично, но полезно

IDEA: Внедрить базовый CSP через `<meta http‑equiv="Content‑Security‑Policy">`
KNOB: В `<head>` добавить строку:  
```html
<meta http-equiv="Content-Security-Policy"
      content="default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://fonts.gstatic.com; font-src https://fonts.gstatic.com; img-src data:;">
```  
EFFECT: Защищает от XSS‑атак, повышает доверие поисковиков к сайту, ограничивает загрузку внешних ресурсов
RISK: Если в будущем появятся внешние скрипты/стили, они будут заблокированы, потребуется обновление CSP
ROLLBACK: Удалить мета‑тег; `git checkout -- index.html`
VERIFY: Открыть DevTools → Console, убедиться, что нет CSP‑violations; проверить, что все стили и шрифты загружаются корректно
PRIORITY: 3 – небольшое изменение, повышает безопасность без влияния на текущий функционал.
