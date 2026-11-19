from pathlib import Path

note = """

## Разбор скиллов сайта и чистка сгенерированного файла (11:57)
- Проверено: 198 скиллов в Desktop/SITE_SKILLS_LIBRARY/skills, SITE_REPORT: 995 идей (594 улучшения / 203 метода / 198 скиллов), 52 CSS + 88 JS блоков.
- 🔴 Найден баг генератора: в index.improved.html (111 955 байт) второй блок script factory-enhance (31 КБ) содержал markdown-мусор из скиллов (```js, **, пояснения моделей, SAFE CSS/JS внутри кода) — JS был синтаксически битым. В style также висел мусор и JS-фрагменты.
- Создан IDEA_FACTORY/clean_improved.py: удаляет заражённый script целиком (оригинальный script сайта оставлен и валиден), вырезает markdown-строки и JS-вставки из style, оставляет только CSS.
- Результат: index.improved.clean.html, 72 456 байт. Проверки: node --check script OK; CSS скобки 496/496 сбалансированы; markdown-мусор 0; структура </html>/</body> на месте. Оригинал index.html не тронут.
- Важно: библиотека скиллов как ИСТОЧНИК ИДЕЙ полезна (3D-tilt, glass, premium-baseline и т.д.), но автоматическая склейка их в HTML фабрикой была некачественной — применять скиллы надо точечно, не целиком.
- Открыт превью очищенной версии.
"""

p = Path(r"C:\Users\Савелий\Desktop\u4000Ultra\.workbuddy-ai\memory\2026-11-17.md")
p.write_text(p.read_text(encoding="utf-8") + note, encoding="utf-8")
print("logged")
