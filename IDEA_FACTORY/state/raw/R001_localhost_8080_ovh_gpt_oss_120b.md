# localhost:8080/ovh/gpt-oss-120b  2026-11-17 17:15:51
duration=24.5 error=- attempts=1

IDEA: Rotating benefit badge — кратко о главном оффере в hero  
KNOB: Внутри `<header class="hero">` сразу после `<h1 class="reveal">` добавить `<div class="hero-offer" aria-label="Ключевые выгоды"></div>` и в CSS задать переменную `--offers` со списком преимуществ, анимацию `@keyframes rotateOffer` меняющую `content` через `attr(data-index)` / `counter`.  
EFFECT: Пользователь мгновенно видит 2‑3 чётких выгоды, повышая восприятие оффера и уменьшая «потерю» в первом экране.  
RISK: Требует небольшого JS‑скрипта для переключения индекса; возможен конфликт с другими скриптами `lareper`.  
ROLLBACK: Удалить вставленный `<div class="hero-offer">` и связанные CSS‑правила (git checkout index.html).  
VERIFY: Открыть страницу, убедиться, что в hero появляется меняющийся текст каждые 4 сек., без ошибок в консоли.  
PRIORITY: 1 – ключевой элемент first‑fold, напрямую влияет на ясность оффера.  

IDEA: Мини‑форма захвата лидов — email + согласие GDPR  
KNOB: После закрывающего `</header>` вставить блок `<section id="lead-capture" class="lead-capture"><h2>Получите бесплатный демо‑прототип</h2><form class="lead-form" action="mailto:saveliy@example.com" method="POST" novalidate><input type="email" name="email" placeholder="Ваш e‑mail" required aria-required="true"><label class="gdpr"><input type="checkbox" name="gdpr" required>Я согласен с обработкой данных</label><button type="submit" class="btn-primary">Отправить</button></form></section>` и добавить CSS‑стили для `.lead-capture` / `.lead-form`.  
EFFECT: Прямой путь к заявке без переходов повышает конверсию, а согласие удовлетворяет требования конфиденциальности.  
RISK: Требует корректного `mailto:` или внешнего обработчика; если пользователь отключил почтовый клиент, запрос не дойдет.  
ROLLBACK: Удалить секцию `#lead-capture` и связанные стили (git checkout index.html).  
VERIFY: Заполнить форму в браузере, убедиться, что открывается клиент почты с предзаполненными полями и не появляется JS‑ошибок.  
PRIORITY: 2 – высокий потенциал конверсии, но зависит от готовности владельца принимать письма.  

IDEA: Блок клиентских логотипов + Schema Organization для доверия  
KNOB: После секции цены (`</section>` с id="price") вставить `<section class="clients" aria-labelledby="clients-heading"><h2 id="clients-heading">Клиенты доверяют нам</h2><div class="client-logos"><img src="logo1.svg" alt="Компания 1"><img src="logo2.svg" alt="Компания 2"><img src="logo3.svg" alt="Компания 3"></div></section>` и добавить в `<head>` JSON‑LD `<script type="application/ld+json">{ "@context":"https://schema.org","@type":"Organization","name":"Савелий — лендинги для бизнеса в Перми","url":"https://example.com","logo":"https://example.com/logo.svg","sameAs":["https://vk.com/...","https://instagram.com/..."] }</script>`.  
EFFECT: Визуальные подтверждения (логотипы) и структурированные данные повышают доверие и улучшают SEO‑видимость.  
RISK: Нужно иметь права на использование логотипов; отсутствие изображений приведёт к пустому блоку.  
ROLLBACK: Удалить секцию `.clients` и `<script type="application/ld+json">` (git checkout index.html).  
VERIFY: В браузере увидеть ряд логотипов, проверить в поисковой консоли наличие `Organization`‑разметки через Rich Results Test.  
PRIORITY: 3 – добавляет социальное доказательство, но менее критично, чем оффер и форма захвата.
