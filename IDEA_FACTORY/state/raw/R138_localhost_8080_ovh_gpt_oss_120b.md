# localhost:8080/ovh/gpt-oss-120b  2026-11-17 08:22:45
duration=43.7 error=- attempts=1

IDEA: Добавить атрибут языка в HTML  
KNOB: В открывающий тег `<html>` добавить `lang="ru"` (при необходимости также `dir="ltr"`).  
EFFECT: Указывает поисковикам и скрин‑ридерам язык страницы → лучшее SEO и доступность.  
RISK: Никакого, если язык указан верно.  
ROLLBACK: `git checkout index.html` или удалить атрибут из файла.  
VERIFY: Открыть страницу, посмотреть в инспекторе — должен быть `lang="ru"`; запустить Lighthouse → проверка «Language attribute».  
PRIORITY: 1 – минимальный труд, высокий SEO‑эффект.  

IDEA: Добавить канонический URL  
KNOB: В `<head>` вставить `<link rel="canonical" href="https://example.com/">` (заменить example.com на реальный домен).  
EFFECT: Убирает риск дублирования контента, передаёт «вес» страниц поисковикам → рост ранжирования.  
RISK: Ошибочный URL может привести к неверному канонизации.  
ROLLBACK: Удалить строку или откатить коммит (`git checkout index.html`).  
VERIFY: Проверить в исходном коде наличие тега; в Google Search Console → Coverage проверить отсутствие ошибок канони
