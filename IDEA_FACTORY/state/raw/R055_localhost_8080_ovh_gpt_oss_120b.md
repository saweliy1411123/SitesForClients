# localhost:8080/ovh/gpt-oss-120b  2026-11-17 04:20:23
duration=34.5 error=- attempts=1

IDEA: SKILL — trust-logos-carousel  
KNOB: **Name:** `trust-logos-carousel`  
**When to apply:** На любой лендинг, где требуется показать логотипы партнёров/клиентов для повышения доверия.  
**Steps:**  
1. Вставить после секции цены (`.price-card`) блок‑контейнер:  
   ```html
   <section id="trust" class="trust" role="region" aria-label="Нам доверяют">
     <h2 class="reveal">Нам доверяют</h2>
     <div class="trust-carousel" aria-roledescription="carousel">
       <!-- повторить для каждого логотипа -->
       <div class="trust-item"><img src="logo1.svg" alt="Логотип партнёра 1" loading="lazy"></div>
       <div class="trust-item"><img src="logo2.svg" alt="Логотип партнёра 2" loading="lazy"></div>
       <div class="trust-item"><img src="logo3.svg" alt="Логотип партнёра 3" loading="lazy"></div>
       <!-- … -->
     </div>
   </section>
   ```  
2. Добавить в `<head>` (или в конец `<style>`) следующий CSS (SAFE CSS):  

   SAFE CSS:  
   ```css
   .trust {padding:80px 0;background:#111;color:#fff;text-align:center}
   .trust h2 {margin-bottom:40px;font-size:clamp(28px,5vw,36px)}
   .trust-carousel {
     display:flex;gap:40px;overflow-x:auto;scroll-snap-type:x mandatory;
     -webkit-overflow-scrolling:touch;scroll-behavior:smooth;
   }
   .trust-item {
     flex:0 0 auto;scroll-snap-align:center;opacity:.6;transition:opacity .3s;
   }
   .trust-item:hover,
   .trust-item:focus-within {opacity:1}
   .trust-item img {max-height:48px;max-width:120px;display:block;margin:auto}
   /* hide scrollbar in WebKit */
   .trust-carousel::-webkit-scrollbar {display:none}
   ```
3. (Опционально) Добавить небольшую JS‑анимацию автопрокрутки, но это не требуется – пользователь может скроллить вручную.  

EFFECT: Показ логотипов партнёров усиливает социальное доказательство, повышает доверие и, как правило, улучшает конверсию CTA‑кнопок.  

RISK: Требуется собрать/разместить логотипы партнёров; если их нет, блок будет пустым и может выглядеть небрежно.  

ROLLBACK: `git checkout index.html` или `git restore index.html` (если изменения внесены в отдельный файл `index.improved.html`).  

VERIFY: Открыть страницу в браузере, убедиться, что блок «Нам доверяют» появился, логотипы отображаются, можно прокручивать горизонтально, и при наведении/фокусе они становятся ярче. Проверить, что на мобильных ширина 360 px логотипы не вылезают за экран.  

PRIORITY: 2 – умеренный объём работы (HTML + CSS), но потенциальный рост доверия и конверсии значителен.  

---  

IDEA: SKILL — hero-cta-clipboard-copy  
KNOB: **Name:** `hero-cta-clipboard-copy`  
**When to apply:** На лендингах, где CTA‑кнопка ведёт в мессенджер (Telegram) и пользователь может захотеть скопировать ссылку/username.  

**Steps:**  
1. В hero‑секцию рядом с основной CTA‑кнопкой добавить вторую кнопку‑ссылка:  
   ```html
   <a class="btn-primary clipboard" href="javascript:void(0)" aria-label="Скопировать ссылку на Telegram">
     Скопировать ссылку <span class="arr">→</span>
   </a>
   ```  
2. Добавить в конец `<body>` безопасный скрипт, который копирует в буфер обмена фиксированную строку (Telegram‑username):  

   SAFE JS:  
   ```js
   (() => {
     const btn = document.querySelector('.clipboard');
     if (!btn) return;
     const text = 'https://t.me/TrainersDontPlays';
     btn.addEventListener('click', async e => {
       e.preventDefault();
       try {
         await navigator.clipboard.writeText(text);
         btn.textContent = 'Скопировано!';
         setTimeout(() => btn.innerHTML = 'Скопировать ссылку <span class="arr">→</span>', 2000);
       } catch (err) {
         console.error('Clipboard write failed', err);
       }
     });
   })();
   ```  
3. Добавить небольшое CSS‑оформление, чтобы кнопка выглядела как остальные CTA (SAFE CSS):  

   SAFE CSS:  
   ```css
   .clipboard {
     display:inline-flex;align-items:center;justify-content:center;
     margin-left:12px;padding:15px 20px;font-weight:600;
     background:var(--grad);color:#fff;border-radius:8px;
     cursor:pointer;transition:background .3s;
   }
   .clipboard:hover {background:var(--grad-dark);}
   .clipboard .arr {margin-left:6px;transition:transform .2s;}
   .clipboard:hover .arr {transform:translateX(4px);}
   ```  

EFFECT: Позволяет пользователю быстро скопировать ссылку на Telegram без переключения окна, снижая трение и повышая вероятность контакта.  

RISK: Требует поддержки Clipboard API (не работает в устаревших браузерах); в старых браузерах действие просто не выполнится, но пользователь не пострадает.  

ROLLBACK: Удалить добавленные строки HTML, CSS и JS; если изменения сделаны в `index.improved.html`, выполнить `git checkout index.improved.html`.  

VERIFY: Открыть страницу, нажать кнопку «Скопировать ссылку», затем вставить (Ctrl+V) в любой текстовый редактор – должна появиться полная ссылка. Убедиться, что после 2 секунд текст кнопки возвращается к исходному.  

PRIORITY: 1 – небольшие изменения (один HTML‑блок, небольшие CSS и безопасный JS) дают мгновенный UX‑прокач, особенно для аудитории, привыкшей копировать ссылки.
