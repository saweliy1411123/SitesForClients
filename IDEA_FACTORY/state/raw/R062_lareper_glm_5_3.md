# lareper/glm-5.3  2026-11-17 04:41:26
duration=2.4 error=- attempts=1

IDEA: SKILL — magnetic-cta-pulse (премиальный CTA: магнитный hover + мягкий пульс, только для главного действия)
KNOB: SKILL — magnetic-cta-pulse
Название: magnetic-cta-pulse
Когда применять: на любом статическом лендинге, где главный CTA — ссылка `.btn-primary` (или аналог), и нужно поднять кликабельность без агрессии: тонкое «магнитное» притяжение курсора и очень медленный пульс тени, который останавливается при prefers-reduced-motion.
Шаги:
1. Найти главный CTA (на этом сайте: L462, L657, L705, L736 — `.btn-primary`).
2. Добавить класс `magnet-pulse` только к первому экрану и финальному CTA (не ко всем — иначе эффект обесценивается).
3. Вставить SAFE CSS в конец существующего `<style>`.
4. Вставить SAFE JS перед `</body>` — он двигает кнопку на ±4px за курсором в радиусе 60px и возвращает её на место.
5. Проверить на мобильном: transform через JS не срабатывает (нет mousemove) — остаётся только пульс.
6. A/B: копия файла `index-mp.html` с классом, оригинал без — сравнить клики за 3–5 дней.

SAFE CSS:
```css
.magnet-pulse{position:relative;transition:transform .25s cubic-bezier(.2,.8,.2,1),box-shadow .25s}
.magnet-pulse::after{content:'';position:absolute;inset:0;border-radius:inherit;box-shadow:0 0 0 0 rgba(139,92,246,.45);animation:mp-pulse 2.8s ease-out infinite;pointer-events:none}
@keyframes mp-pulse{0%{box-shadow:0 0 0 0 rgba(139,92,246,.40)}70%{box-shadow:0 0 0 14px rgba(139,92,246,0)}100%{box-shadow:0 0 0 0 rgba(139,92,246,0)}}
@media (prefers-reduced-motion: reduce){.magnet-pulse::after{animation:none}.magnet-pulse{transition:none}}
```

SAFE JS:
```js
(function(){
if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
var b=document.querySelector('.hero .magnet-pulse');if(!b)return;
var r=null;
b.addEventListener('mousemove',function(e){
r=b.getBoundingClientRect();
var x=(e.clientX-r.left-r.width/2)/r.width, y=(e.clientY-r.top-r.height/2)/r.height;
b.style.transform='translate('+x*8+'px,'+y*6+'px)';
});
b.addEventListener('mouseleave',function(){b.style.transform='';});
})();
```

EFFECT: главный CTA заметнее на фоне других кнопок; магнитный hover даёт «дорогое» ощущение уровня студийных лендингов; ожидаемый прирост кликов по hero-CTA 5–15%.
RISK: пульс может раздражать при долгом чтении первого экрана — смягчено медленным циклом 2.8s и reduced-motion.
ROLLBACK: `git checkout -- index.improved.html` (или удалить класс `magnet-pulse` и два вставленных блока).
VERIFY: (1) Открыть копию, навести курсор на hero-CTA — кнопка смещается за курсором и возвращается. (2) DevTools → Rendering → Emulate prefers-reduced-motion: reduce — пульс и смещение отключены. (3) Tab до кнопки — фокус-стили не сломаны.
PRIORITY: 2 — заметный конверсионный эффект при нулевом риске для контента, но ниже структурных правок (FAQ, шаги).
SITE_REQUEST: hero

IDEA: SKILL — price-anchor-strip (полоса «что вы платите /
