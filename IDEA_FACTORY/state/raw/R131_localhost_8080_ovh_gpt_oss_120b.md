# localhost:8080/ovh/gpt-oss-120b  2026-11-17 08:02:24
duration=37.6 error=- attempts=1

IDEA: Добавить атрибут языка ru к корневому элементу
KNOB: В `<html>` добавить `lang="ru"` (и, при необходимости, `dir="ltr"`)
EFFECT: Улучшает SEO‑ориентирование по языку и позволяет скрин‑ридерам правильно озвучивать контент
RISK: Неправильный атрибут может сбить парсеры, если в проекте есть скрипты, читающие `document.documentElement.lang`
ROLLBACK: `git checkout index.html` (или удалить строку `lang="ru"`)
VERIFY: Открыть страницу, нажать Ctrl+U, убедиться в наличии `lang="ru"`; запустить Lighthouse → SEO → “Language attribute”
PRIORITY: 1 – небольшие изменения, высокий SEO‑эффект

IDEA: Добавить канонический URL‑тег
KNOB: В `<head>` вставить `<link rel="canonical" href="https://example.com/">` (заменить example.com на реальный домен)
EFFECT: Уменьшает риск дублирования контента в поисковых системах, усиливает авторитет страницы
RISK: Ошибочный URL может привести к неправильному индексированию
ROLLBACK: Удалить добавленную строку или выполнить `git checkout index.html`
VERIFY: Просмотреть исходный код, убедиться в наличии тега; проверить в Google Search Console → Coverage
PRIORITY: 2 – важный SEO‑элемент, но
