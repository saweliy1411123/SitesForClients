from pathlib import Path
import re
from collections import Counter

BASE = Path(r"C:\Users\Савелий\Desktop\SITE_SKILLS_LIBRARY\skills")
files = sorted(BASE.glob("*.md"))
print("total files:", len(files))

empty = with_code = with_junk = 0
names = []
css_total = js_total = 0

for f in files:
    s = f.read_text(encoding="utf-8", errors="replace")
    css = re.findall(r"```css(.*?)```", s, re.S)
    js = re.findall(r"```(?:js|javascript)(.*?)```", s, re.S)
    good_css = [c for c in css if c.strip() and not c.strip().startswith("**")]
    good_js = [j for j in js if j.strip() and j.strip() != "// нет" and not j.strip().startswith("**")]
    if good_css or good_js:
        with_code += 1
        css_total += len(good_css)
        js_total += len(good_js)
    else:
        empty += 1
    if s.count("**") > 6:
        with_junk += 1
    m = re.search(r"^\*\*NAME:\*\*\s*(.+)$", s, re.M)
    if not m:
        m = re.search(r"^name:\s*(.+)$", s, re.M)
    if m:
        names.append(m.group(1).strip().lower())

print("с исполняемым кодом:", with_code)
print("без кода:", empty)
print("с мусором **:", with_junk)
print("css блоков:", css_total, "js блоков:", js_total)
print("именованных:", len(names), "уникальных:", len(set(names)))
for n, c in Counter(names).most_common(10):
    print("  ", c, n[:70])
