# lareper/glm-5.3  2026-11-17 05:00:24
duration=35.8 error=- attempts=1

IDEA: rel="noopener noreferrer" на всех внешних ссылках target="_blank"
KNOB: Ссылки на `https://t.me/TrainersDontPlays` (L705) и `https://vk.ru/trainersdontplays` (L707) — добавить `rel="noopener noreferrer"` к каждому `<a target="_blank">`.
EFFECT: Устраняет утечку window.opener (безопасность) и убирает передачу реферера; плюс к аудиту Lighthouse Best Practices — выше доверие и балл.
RISK: Практически нулевой; потеря реферера в статистике мессенджеров.
ROLLBACK: `git checkout -- index.html` (или удалить добавленный атрибут в копии).
VERIFY: Консоль: `[...document.querySelectorAll('a[target="_blank"]')].filter(a=>!a.rel.includes('noopener'))` — до правки вывести список, после — пусто.
PRIORITY: 1 — тривиальная правка, прямой пункт Lighthouse.

IDEA: Fallback-шрифт с metric-override — убрать CLS от Google Fonts
KNOB: В `<style>` до загрузки Manrope добавить `@font-face { font-family:'Manrope-fallback'; src:local('Arial'); size-adjust:104%; ascent-override:96%; line-gap-override:0%; }` и в `font-family` элементов указать `'Manrope','Manrope-fallback',sans-serif`.
EFFECT: Пока шрифт грузится (или заблокирован), текст рендерится в fallback с совпадающими метриками — нулевой layout shift (CLS), заголовки не «прыгают».
RISK: Метрики fallback не идеальны — нужен визуальный прогон на h1/price.
ROLLBACK: `git checkout -- index.html`.
VERIFY: DevTools → Performance → перезагрузка, смотреть CLS до/после; либо Layout Shift regions (Rendering → Layout Shift Regions).
PRIORITY: 2 — заметно на мобильных/медленной сети, но эффект тонкий.

IDEA: scroll-margin-top для якорей + плавный скролл (CTA → #contact под sticky-шапкой)
KNOB: В CSS добавить `html{scroll-behavior:smooth}` и `[id]{scroll-margin-top:90px}` (значение = высота sticky-хедера). Кнопки ведут на `#contact
