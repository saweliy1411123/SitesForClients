from pathlib import Path

note = """

## Улучшение скиллов и новый апплайер (12:05)
- Аудит библиотеки: 198 скиллов, 167 с исполняемым кодом (167 CSS + 118 JS блоков), 31 пустой, 82 с мусором **, все 198 уникальных имён.
- 🔴 Первопричина «дрисни»: старый apply_skills.py брал ВСё из markdown-блоков, включая **SAFE JS:** и пояснения моделей, и склеивал это в <script>.Отсюда битый JS в index.improved.html.
- Переписан SITE_SKILLS_LIBRARY/apply_skills.py: strip_markdown (убирает **/```/нумерованные списки/проза), строгая проверка CSS (баланс скобок, запрет @import/url/javascript), проверка JS через node --check, дедупликация по содержимому, лимиты MAX_CSS_BLOCKS=14 / MAX_JS_BLOCKS=10, флаги --only и --skip.
- Проверка: python apply_skills.py index.html --out index.premium.html → CSS 14, JS 10, отклонено 4 битых скилла, JS-ошибок 0, скобки 289/289, размер 62 382. Оригинал index.html не тронут.
- Открыт превью index.premium.html. Это РЕКОМЕНДУЕМЫЙ путь применения скиллов вместо сгенерированной фабрикой кучи.
- Звук: step193 — TAIL_ENABLE=0 и Dym2 gain −10→−7 (фронт/громкость). md5 c4bdc797.
"""

p = Path(r"C:\Users\Савелий\Desktop\u4000Ultra\.workbuddy-ai\memory\2026-11-17.md")
p.write_text(p.read_text(encoding="utf-8") + note, encoding="utf-8")
print("logged")
