# lareper/glm-5.3-prime  2026-11-17 07:26:44
duration=2.4 error=- attempts=1

IDEA: SKILL — contact-copy-chip (клик-копирование контакта с подтверждением, без формы)
KNOB: SKILL — contact-copy-chip
Name: `contact-copy-chip`
When to apply: на любом статическом лендинге, где контакт — только внешняя ссылка (Telegram, email, телефон), и часть пользователей уходит, не совершив переход. Даёт «мягкую» альтернативу: скопировать контакт одним кликом.
Steps:
1. Рядом с основным CTA (например, под L705 в `.final`) добавить чип: `<button class="copy-chip" data-copy="@TrainersDontPlays" type="button">Скопировать: @TrainersDontPlays</button>`.
2. Добавить SAFE CSS ниже.
3. Добавить SAFE JS ниже — он читает `data-copy`, вызывает `navigator.clipboard.writeText` и меняет текст кнопки на «Скопировано ✓» на 2 секунды (без innerHTML — только textContent).
4. Проверить, что кнопка не перехватывает фокус у основного CTA: она вторична по стилю (outline-чип, не btn-primary).
SAFE CSS:
.copy-chip{display:inline-flex;align-items:center;gap:8px;margin-top:14px;padding:10px 16px;border:1px solid rgba(255,255,255,.18);border-radius:999px;background:transparent;color:inherit;font:inherit;font-size:14px;cursor:pointer;transition:border-color .2s,background .2s}
.copy-chip:hover,.copy-chip:focus-visible{border-color:#8b5cf6;background:rgba(139,92,246,.08)}
.copy-chip:active{transform:scale(.97)}
.copy-chip.ok{border-color:#34d399;color:#34d399}
@media (prefers-reduced-motion: reduce){.copy-chip{transition:none}}
SAFE JS:
document.querySelectorAll('.copy-chip').forEach(function(chip){
  chip.addEventListener('click', function(){
    var t = chip.getAttribute('data-copy') || '';
    function done(){
      var old = chip.textContent;
      chip.textContent = 'Скопировано ✓';
      chip.classList.add('ok');
      setTimeout(function(){ chip.textContent = old; chip.classList.remove('ok'); }, 2000);
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(t).then(done, done);
    } else { done(); }
  });
});
EFFECT: пользователь, не готовый переходить в Telegram сразу, уносит контакт в буфер — снижается потеря лидов на последнем экране; работает без бэкенда
