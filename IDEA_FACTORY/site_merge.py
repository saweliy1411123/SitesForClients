#!/usr/bin/env python3
"""Утро: склад идей сайта -> SITE_REPORT.md + шортлист + безопасные проверки."""
import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))
import site_overnight as soi

IDEAS = BASE / "ideas"
STATE = BASE / "state"


def load_ideas():
    return [d for p in sorted(IDEAS.glob("I-*.json"))
            if (d := soi.load_json(p, None))]


def parse_inbox():
    text = (BASE / "INBOX.md").read_text(encoding="utf-8")
    out, cur = [], None
    for line in text.splitlines():
        m = re.match(r"^###\s+IDEA\s*:\s*(.*)$", line, re.I)
        if m:
            if cur:
                out.append(cur)
            cur = {"title": m.group(1).strip()}
            continue
        if line.strip().startswith("###") or line.strip() == "---":
            if cur:
                out.append(cur)
                cur = None
            continue
        if cur:
            f = re.match(r"^(IDEA|KNOB|EFFECT|RISK|ROLLBACK|VERIFY|PRIORITY|SOURCE)\s*:\s*(.*)$", line.strip(), re.I)
            if f:
                cur[f.group(1).upper()] = f.group(2).strip()
    if cur:
        out.append(cur)
    return [{"title": b["title"], "knob": b.get("KNOB", ""), "effect": b.get("EFFECT", ""),
             "risk": b.get("RISK", ""), "rollback": b.get("ROLLBACK", ""),
             "verify": b.get("VERIFY", ""), "category": "lever",
             "sources": ["INBOX"], "mentions": 1, "id": "INBOX", "flags": []}
            for b in out if b.get("title")]


def score(idea):
    s = 10 + min(9, 3 * (int(idea.get("mentions", 1)) - 1))
    k = idea.get("knob", "")
    if re.search(r"#[a-zA-Z]|<\w+|\.class|SAFE CSS|meta|h1|h2|schema", k, re.I):
        s += 3
    for field in ("verify", "rollback", "risk", "effect"):
        if idea.get(field):
            s += 2 if field in ("verify", "rollback") else 1
    if idea.get("category") == "method":
        s += 1
    f = idea.get("flags", [])
    s -= 4 * ("BREAKS_LAYOUT" in f)
    s -= 5 * ("NEEDS_OWNER" in f)
    s -= 20 * ("FORBIDDEN" in f)
    return s


def bad(idea):
    return idea.get("status") == "QUARANTINE" or any(
        x in idea.get("flags", []) for x in ("FORBIDDEN", "BREAKS_LAYOUT"))


def block(idea, s, i):
    lines = ["**%d. [%d] %s** %s" % (i, s, idea.get("title", "?"), "`%s`" % idea.get("id", "")),
             "- Голоса: %d — %s" % (idea.get("mentions", 1), ", ".join(idea.get("sources", [])[:5])),
             "- KNOB: " + str(idea.get("knob", "—"))[:1200],
             "- EFFECT: " + str(idea.get("effect", "—")),
             "- RISK: " + str(idea.get("risk", "—")),
             "- ROLLBACK: " + str(idea.get("rollback", "—")),
             "- VERIFY: " + str(idea.get("verify", "—"))]
    if idea.get("site_request"):
        lines.append("- SITE_REQUEST: " + str(idea["site_request"])[:100])
    variants = [v for v in idea.get("variants", []) if v != idea.get("knob")]
    if variants:
        lines.append("- Варианты: " + " | ".join(variants[:4])[:600])
    if idea.get("flags"):
        lines.append("- Флаги: " + ", ".join(idea["flags"]))
    return "\n".join(lines)


def main():
    items = load_ideas() + parse_inbox()
    scored = [(score(x), x) for x in items]
    good = [(s, x) for s, x in scored if not bad(x)]
    groups = {
        "lever": sorted([p for p in good if p[1].get("category") == "lever"], key=lambda p: -p[0]),
        "method": sorted([p for p in good if p[1].get("category") == "method"], key=lambda p: -p[0]),
        "skill": sorted([p for p in good if p[1].get("category") == "skill"], key=lambda p: -p[0]),
        "bad": sorted([p for p in scored if bad(p[1])], key=lambda p: -p[0]),
    }
    out = ["# Утренний отчёт — фабрика сайта", "",
           "Собрано: %s. Идей: %d (улучшения %d, методы %d, скиллы %d, карантин %d)." % (
               datetime.now().strftime("%Y-%m-%d %H:%M:%S"), len(items),
               len(groups["lever"]), len(groups["method"]), len(groups["skill"]), len(groups["bad"])), ""]

    imp = soi.load_json(STATE / "improved_build.json", {})
    improved = BASE.parent / "index.improved.html"
    out.append("## Готовый файл")
    out.append("- `%s` — создан %s, CSS-блоков: %d, JS-блоков: %d. Оригинал `index.html` НЕ тронут." % (
        improved.name, imp.get("time", "—"), imp.get("css_blocks", 0), imp.get("js_blocks", 0)))
    out.append("- Переносимая библиотека скиллов: `Desktop\\SITE_SKILLS_LIBRARY\\skills` — "
               "применима к любому будущему сайту через `apply_skills.py <index.html>`.")
    out.append("- Сравнить: `git diff --no-index index.html index.improved.html` (в папке сайта).")
    out.append("- Подменить только после просмотра: `cp index.improved.html index.html`.")
    out.append("")

    for key, title, limit in (("lever", "ТОП улучшений", 15), ("method", "Методы проверки", 10),
                              ("skill", "Скиллы, написанные моделями", 10),
                              ("bad", "Карантин", 12)):
        out.extend(["## " + title, ""])
        if not groups[key]:
            out.append("_(пусто)_")
        for i, (s, idea) in enumerate(groups[key][:limit], 1):
            out.extend([block(idea, s, i), ""])

    answers = soi.load_json(STATE / "site_answers.json", {})
    if answers:
        out.extend(["## Ответы на SITE_REQUEST", ""])
        for k, v in sorted(answers.items(), key=lambda kv: kv[1].get("time", ""), reverse=True)[:10]:
            out.append("- «%s» → %s" % (k, str(v.get("result", "")).replace("\n", " | ")[:300]))
        out.append("")

    log_path = STATE / "log.jsonl"
    statuses = Counter()
    if log_path.exists():
        for line in log_path.read_text(encoding="utf-8").splitlines():
            try:
                statuses[json.loads(line).get("status", "?")] += 1
            except Exception:
                pass
    out.extend(["## Статистика", "",
                "- Ответы моделей: " + ", ".join("%s=%d" % kv for kv in statuses.most_common()) or "нет",
                "- Скиллы локально: %d" % len(list((BASE / "SKILLS").glob("*.md"))),
                "- Скиллы в переносимой библиотеке: %d" % len(list((Path.home() / "Desktop" / "SITE_SKILLS_LIBRARY" / "skills").glob("*.md"))), ""])

    report = BASE / "SITE_REPORT.md"
    report.write_text("\n".join(out) + "\n", encoding="utf-8")
    soi.save_json(BASE / "site_shortlist.json", [
        {"id": d.get("id"), "score": s, "category": d.get("category"), "title": d.get("title"),
         "knob": d.get("knob", "")[:1000], "mentions": d.get("mentions", 1),
         "flags": d.get("flags", [])}
        for s, d in groups["lever"][:15] + groups["method"][:10] + groups["skill"][:10]])
    checks = """#!/bin/sh
# Только чтение. В Git-Bash: sh site_readonly_checks.sh
cd ".."
git status --short
git diff --stat
md5sum index.html index.improved.html 2>/dev/null
wc -l index.html index.improved.html 2>/dev/null
grep -i -m1 '<title' index.html
grep -c '<h2' index.html
"""
    (BASE / "site_readonly_checks.sh").write_text(checks, encoding="utf-8", newline="\n")
    print("Готово: SITE_REPORT.md | улучшения %d, методы %d, скиллы %d, карантин %d" % (
        len(groups["lever"]), len(groups["method"]), len(groups["skill"]), len(groups["bad"])))
    print("Топ-3:", [(d.get("id"), d.get("title", "")[:45], s) for s, d in groups["lever"][:3]])
    return 0


if __name__ == "__main__":
    sys.exit(main())
