from pathlib import Path
import re
import subprocess

BASE = Path(r"C:\Users\Савелий\Desktop\Мой сайт")
s = (BASE / "index.improved.html").read_text(encoding="utf-8")

# 1) Вырезать заражённый блок <script id="factory-enhance"> целиком
start = s.find('<script id="factory-enhance">')
end = s.rfind("</script>") + len("</script>")
if start < 0 or end < start:
    raise SystemExit("factory-enhance block not found")
s = s[:start] + s[end:]

# 2) Внутри <style> оставить только CSS-строки
BAD_PREFIXES = ("```", "**", "*", "(", ")", "</", "<")


def is_css_like(line):
    t = line.strip()
    if not t:
        return True
    if t.startswith(BAD_PREFIXES):
        return False
    if t in ("})();", "})()", "})();", "};", "}"):
        return True if t == "}" else False
    if re.match(r"^\d+[\.\)]\s", t):
        return False
    first = t[0]
    if first.isalpha() or first in "@[].:#}$-+/":
        return True
    return False


def clean_style(block):
    return "\n".join(line for line in block.split("\n") if is_css_like(line))


s = re.sub(
    r"(<style[^>]*>)(.*?)(</style>)",
    lambda m: m.group(1) + clean_style(m.group(2)) + m.group(3),
    s,
    flags=re.S,
)

(BASE / "index.improved.clean.html").write_text(s, encoding="utf-8")

css = "".join(re.findall(r"<style[^>]*>(.*?)</style>", s, re.S))
print("size:", len(s))
print("fences:", s.count("```"), "stars:", s.count("**"))
print("css braces:", css.count("{"), css.count("}"))
scripts = re.findall(r"<script[^>]*>(.*?)</script>", s, re.S)
for i, sc in enumerate(scripts):
    p = BASE / ("tmp_verify_%d.js" % i)
    p.write_text(sc, encoding="utf-8")
    r = subprocess.run(["node", "--check", str(p)], capture_output=True, text=True)
    print("script", i, "OK" if r.returncode == 0 else "FAIL", r.stderr[:200])
