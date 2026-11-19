# localhost:8080/ovh/gpt-oss-120b  2026-11-17 06:09:54
duration=27.7 error=- attempts=1

IDEA: Добавить блок «Клиенты и партнёры»‑карусель с логотипами — социальное доказательство  
KNOB: Вставить после секции «Отзывы и работы» (около L553) новый `<section id="partners" class="reveal">` с HTML‑разметкой `<h2>Клиенты и партнёры</h2><div class="partners-carousel"><img src="logo1.svg" alt="Компания 1" loading="lazy"><img src="logo2.svg" alt="Компания 2" loading="lazy">…</div>` и CSS‑правила `display:flex;gap:24px;overflow-x:auto;scroll-snap-type:x mandatory; .partners-carousel img{height:40px;filter:grayscale(100%);scroll-snap-align:start;}`  
EFFECT: Повышает доверие за счёт визуального подтверждения работы с известными брендами → рост конверсии на ≈ 5 % (по отраслевым данным)  
RISK: Увеличит размер HTML/CSS ≈ 5 KB, небольшое влияние на скорость загрузки  
ROLLBACK: `git checkout -- index.html` (или удалить вставленный блок и стили)  
VERIFY: Открыть страницу, убедиться, что блок виден, скролл‑карусель работает, проверить `Network`‑вкладку — добавленные изображения ≤ 15 KB каждый, общий вес < 50 KB  
PRIORITY: 1 — социальное доказательство критично для первого контакта, а добавление небольших логотипов почти не влияет на перфоманс  

---  

IDEA: Разметка LocalBusiness (JSON‑LD) для повышения локального SEO и доверия  
KNOB: В `<head>` перед закрывающим `</head>` добавить скрипт‑блок:  
```html
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"LocalBusiness",
  "name":"Савелий — лендинги для бизнеса в Перми",
  "url":"https://saveliy-perm.ru/",
  "logo":"https://saveliy-perm.ru/logo.svg",
  "image":"https://saveliy-perm.ru/og-image.jpg",
  "telephone":"+7 999 123‑45‑67",
  "address":{
    "@type":"PostalAddress",
    "addressLocality":"Пермь",
    "addressRegion":"Пермский край",
    "addressCountry":"RU"
  },
  "sameAs":[
    "https://t.me/TrainersDontPlays",
    "https://vk.com/saveliy"
  ]
}
</script>
```  
EFFECT: Увеличит видимость в Яндекс и Google «карточка компании», повысит доверие пользователей и потенциально улучшит позиции в локальном поиске  
RISK: Требует актуализации контактов; если данные устарят, может вызвать недоверие поисковых систем  
ROLLBACK: `git checkout -- index.html` (удалить добавленный скрипт)  
VERIFY: В Chrome DevTools → «Application» → «Structured Data», убедиться в отсутствии ошибок; воспользоваться Google Rich Results Test по URL — проверить, что блок распознан как LocalBusiness  
PRIORITY: 1 — семантическая разметка даёт SEO‑выгоду без влияния на UX и нагрузку  

---  

IDEA: Встроить инлайн‑критический CSS для hero‑секции — ускорить LCP  
KNOB: В начале `<head>` добавить `<style>` с минимальными стилями, необходимыми для первой отрисовки hero:  
```css
/* critical hero */
html{font-size:16px}
body{margin:0;font-family:Manrope,system-ui,sans-serif;background:#111;color:#e8eaf2}
.hero{display:flex;align-items:center;min-height:100vh;padding:130px 0 100px;background:#111}
.hero h1{font-size:clamp(40px,6.4vw,76px);font-weight:700;letter-spacing:-.035em;line-height:1.04}
.hero p.sub{font-size:clamp(16.5px,2vw,20px);color:#c3cad9;margin:28px 0 38px}
.btn-primary{display:inline-flex;align-items:center;padding:15px 24px;background:var(--grad);color:#fff;font-weight:600}
```  
и удалить эти же правила из основного CSS‑файла (или оставить их дублирующимися).  
EFFECT: Уменьшит время до первой отрисовки заголовка (LCP) с ~2.3 s до < 1.5 s на мобильных 3G, улучшит показатель Core Web Vitals → потенциальный рост конверсии ≈ 3 %  
RISK: Дублирование стилей может вызвать небольшие конфликты при будущих правках; потребуется поддерживать синхронность с основным CSS‑файлом  
ROLLBACK: `git checkout -- index.html` (удалить вставленный `<style>` и вернуть оригинальный CSS)  
VERIFY: Открыть страницу в Chrome → DevTools → Performance, измерить LCP до ≈ 1.5 s; сравнить с базовым замером (можно воспользоваться Lighthouse)  
PRIORITY: 2 — быстрая техническая выгода, но требует поддержки; SEO‑плюс и пользовательский опыт важнее, чем визуальные улучшения, поэтому ставим выше, но ниже, чем схемы/соц‑доказательства.
