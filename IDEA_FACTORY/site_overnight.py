#!/usr/bin/env python3
"""Ночная фабрика улучшений сайта: идеи + методы, без автоматической правки файлов."""
import argparse
import atexit
import hashlib
import json
import os
import re
import subprocess
import sys
import threading
import time
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent
SITE = BASE.parent / "index.html"
STATE = BASE / "state"
RAW = STATE / "raw"
IDEAS = BASE / "ideas"
SKILLS = BASE / "SKILLS"
LIBRARY = Path.home() / "Desktop" / "SITE_SKILLS_LIBRARY"
LIBRARY_SKILLS = LIBRARY / "skills"
LOCK = STATE / "run.lock"
BRIEF = (BASE / "prompts" / "SITE_BRIEF.md").read_text(encoding="utf-8")
LAREPER_URL = "https://api.lareper.store/v1/chat/completions"
FIELDS = ["IDEA", "KNOB", "EFFECT", "RISK", "ROLLBACK", "VERIFY", "PRIORITY", "SOURCE", "SITE_REQUEST", "SKILL"]
THEMES = [
    "Тема раунда: 3 НОВЫХ улучшения лендинга — ясность оффера, конверсия, доверие.",
    "Тема раунда: 3 НОВЫХ МЕТОДА проверки гипотез за 2–10 минут (без реального деплоя).",
    "Тема раунда: покритикуй идеи из кучи и предложи 2 замены в том же формате.",
    "Тема раунда: улучшения конкретных блоков: hero, боль, шаги, демо, цена, FAQ, финальный CTA.",
    "Тема раунда: SEO / доступность / мобильная версия / скорость — без смены бренда и без фейков.",
    "Тема раунда SKILLS: напиши 1–2 готовых скилла уровня Claude/ дорогих студий. В KNOB дай полное тело: "
    "название, когда применять, шаги, SAFE CSS: (чистый CSS), при нужде SAFE JS: (только безопасный JS). "
    "Скилл должен быть переносим на другой статический лендинг.",
    "Тема раунда SKILLS «дорогой сайт»: премиальная типографика, анимации появления, параллакс, "
    "свет/стекло, 3D-трансформы карточек (perspective/rotateY/translateZ), hover/focus, мобильная адаптивность. "
    "Никаких внешних библиотек и тяжёлых скриптов: максимум CSS + крошечный SAFE JS.",
]
SYSTEM = (
    "Строгий продуктовый дизайнер и frontend-инженер. Отвечай ТОЛЬКО блоками "
    "IDEA/KNOB/EFFECT/RISK/ROLLBACK/VERIFY/PRIORITY. Без таблиц, вступлений и команд на выполнение. "
    "Не выдумывай содержимое сайта — опирайся на снимок."
)


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def load_json(path, default):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    except Exception:
        return default


def save_json(path, obj):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write("\n")


def append_log(event):
    with open(STATE / "log.jsonl", "a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


def pid_alive(pid):
    if not pid:
        return False
    try:
        if os.name == "nt":
            raw = subprocess.run(["tasklist", "/FI", "PID eq %d" % pid],
                                 capture_output=True, timeout=10).stdout or b""
            out = raw.decode("utf-8", "replace").replace("\n", " ")
            return (" %d " % pid) in (" " + out + " ")
        os.kill(pid, 0)
        return True
    except Exception:
        return False


def acquire_lock():
    if LOCK.exists():
        try:
            old = int(LOCK.read_text(encoding="utf-8").strip())
        except Exception:
            old = 0
        if pid_alive(old):
            print("УЖЕ ЗАПУЩЕНА: pid %d жив. Второй запуск выходит." % old, flush=True)
            return False
    LOCK.write_text(str(os.getpid()), encoding="utf-8", newline="\n")
    atexit.register(release_lock)
    return True


def release_lock():
    try:
        if LOCK.exists() and LOCK.read_text(encoding="utf-8").strip() == str(os.getpid()):
            LOCK.unlink()
    except Exception:
        pass


def lareper_key():
    cfg = Path.home() / ".config" / "freellmpool" / "config.toml"
    try:
        for line in cfg.read_text(encoding="utf-8").splitlines():
            m = re.match(r'^LAREPER_API_KEY\s*=\s*"([^"]+)"', line.strip())
            if m:
                return m.group(1)
    except Exception:
        pass
    return ""


def build_targets(cfg, key):
    targets = []
    for m in cfg["models_lareper"]:
        targets.append({
            "name": "lareper/" + m, "model": m, "url": LAREPER_URL, "key": key,
            "timeout": cfg.get("timeouts_lareper", {}).get(m, cfg.get("model_timeout_seconds", 90)),
        })
    for pool in cfg["pools"]:
        host = pool["url"].split("/")[2]
        for m in pool["models"]:
            targets.append({
                "name": host + "/" + m, "model": m, "url": pool["url"],
                "key": None, "timeout": pool.get("timeout", cfg.get("model_timeout_seconds", 90)),
            })
    return targets


def select_targets(targets, failures, workers):
    now_ts = time.time()
    return [t for t in targets
            if float(failures.get(t["name"], {}).get("retry_after", 0)) <= now_ts][:workers * 3]


def cooldown_after_error(failures, name, error, cfg):
    info = failures.setdefault(name, {"count": 0})
    count = int(info.get("count", 0)) + 1
    delay = min(float(cfg.get("retry_max_cooldown_seconds", 120)),
                float(cfg.get("retry_cooldown_seconds", 20)) * (2 ** max(0, count - 1)))
    info.update({"count": count, "ts": time.time(), "retry_after": time.time() + delay,
                 "retry_delay": delay, "reason": str(error)[:160]})
    return delay


# ------------------------------------------------------------- снимок сайта
def git_run(args):
    try:
        p = subprocess.run(["git"] + args, cwd=str(SITE.parent),
                           capture_output=True, timeout=15)
        out = (p.stdout or b"").decode("utf-8", "replace").strip()
        err = (p.stderr or b"").decode("utf-8", "replace").strip()
        return out or err or "(пусто)"
    except Exception as e:
        return "ERROR " + str(e)[:120]


def site_snapshot(force=False):
    p = STATE / "site_snapshot.md"
    if p.exists() and not force and time.time() - p.stat().st_mtime < 300:
        return p.read_text(encoding="utf-8")
    if not SITE.exists():
        return "index.html НЕ НАЙДЕН"
    s = SITE.read_text(encoding="utf-8", errors="replace")
    lines = ["# LIVE SITE SNAPSHOT (%s)" % now()]
    lines.append("- file: %s" % SITE)
    lines.append("- size: %d bytes, lines: %d" % (len(s.encode("utf-8", "replace")), s.count("\n") + 1))
    lines.append("- md5: %s" % hashlib.md5(s.encode("utf-8", "replace")).hexdigest())
    t = re.search(r"<title[^>]*>(.*?)</title>", s, re.S | re.I)
    lines.append("- title: %s" % (t.group(1).strip()[:160] if t else "-"))
    for tag in ("h1", "h2", "h3", "section", "script", "img", "form", "button", "link", "meta"):
        lines.append("- <%s>: %d" % (tag, len(re.findall(r"<%s\b" % tag, s, re.I))))
    heads = []
    for m in re.finditer(r"<(h1|h2|h3)[^>]*>(.*?)</\1>", s, re.S | re.I):
        txt = " ".join(re.sub(r"<[^>]+>", " ", m.group(2)).split())
        heads.append("%s:%s" % (m.group(1), txt[:80]))
    lines.append("- headings: " + " | ".join(heads[:16]))
    assets = sorted(set(m.group(1) for m in re.finditer(
        r"<(?:script|link)[^>]+(?:src|href)=[\"']([^\"']+)", s, re.I)))
    lines.append("- external assets: " + ", ".join(a[:120] for a in assets[:10]))
    lines.append("- git status: " + git_run(["status", "--short"]).replace("\n", " | ")[:400])
    lines.append("- git log: " + git_run(["log", "--oneline", "-3"]).replace("\n", " | ")[:300])
    text = "\n".join(lines)
    p.write_text(text, encoding="utf-8")
    return text


def normalize_request(req):
    req = str(req or "").strip().strip("`\"'")
    if not req or len(req) > 80:
        return None
    if not re.fullmatch(r"[\w\s\-]{1,80}", req, re.UNICODE):
        return None
    return req


def register_site_requests(text):
    pending = load_json(STATE / "site_pending.json", [])
    added = 0
    for m in re.finditer(r"SITE_REQUEST\s*:\s*(.+)", text or "", re.I):
        req = normalize_request(m.group(1))
        if req and req not in pending:
            pending.append(req)
            added += 1
    if added:
        save_json(STATE / "site_pending.json", pending[:40])
    return added


def answer_site_requests():
    pending = load_json(STATE / "site_pending.json", [])
    if not pending:
        return 0
    s = SITE.read_text(encoding="utf-8", errors="replace") if SITE.exists() else ""
    lines = s.splitlines()
    answers = load_json(STATE / "site_answers.json", {})
    done = []
    for req in pending[:12]:
        hits = []
        for i, line in enumerate(lines, 1):
            if req.lower() in line.lower():
                hits.append("L%d: %s" % (i, line.strip()[:180]))
                if len(hits) >= 12:
                    break
        answers[req] = {"time": now(), "result": "\n".join(hits) or "совпадений нет"}
        done.append(req)
    save_json(STATE / "site_answers.json", answers)
    save_json(STATE / "site_pending.json", [x for x in pending if x not in done][:40])
    return len(done)


def site_answers_block():
    answers = load_json(STATE / "site_answers.json", {})
    if not answers:
        return "Запросов фрагментов пока нет."
    items = sorted(answers.items(), key=lambda kv: kv[1].get("time", ""), reverse=True)[:8]
    return "\n".join("- SITE_REQUEST «%s» => %s" % (k, str(v.get("result", ""))[:1200]) for k, v in items)


def build_prompt(round_no, ideas, theme_index, snapshot, answers):
    theme = THEMES[theme_index % len(THEMES)]
    lines = [BRIEF, "\n---\nLIVE SITE SNAPSHOT:\n", snapshot[:5000],
             "\n---\nОТВЕТЫ НА SITE_REQUEST:\n", answers[:5000],
             "\n---\n", theme, "\nУЖЕ В КУЧЕ (не повторяй; вариант той же идеи — с новым значением):"]
    for idea in ideas[-120:]:
        lines.append("- %s [%s] %s" % (idea.get("id", "?"),
                     str(idea.get("title", ""))[:70], str(idea.get("knob", ""))[:100]))
    lines.append("\nЕсли нового нет — одна строка NO_NEW_IDEAS: причина.")
    return "\n".join(lines)


FIELD_RE = re.compile(r"^\s*[\d.)\-*]*\*{0,2}(" + "|".join(FIELDS) + r")\*{0,2}\s*:\s*(.*)$", re.I)


def parse_ideas(text):
    blocks, cur, last_key = [], None, None
    for line in text.splitlines():
        m = FIELD_RE.match(line)
        if m:
            key, val = m.group(1).upper(), m.group(2).strip()
            if key == "IDEA":
                if cur:
                    blocks.append(cur)
                cur = {"title": val}
                last_key = None
            elif cur is not None:
                cur[key] = val
                last_key = key
            continue
        # продолжение предыдущего поля: так сохраняется многострочный SAFE CSS
        if cur is not None and last_key and line.strip() and line.strip() != "---":
            cur[last_key] += "\n" + line.strip()
    if cur:
        blocks.append(cur)
    out = []
    for b in blocks:
        if not b.get("title"):
            continue
        out.append({
            "title": b["title"][:120], "knob": b.get("KNOB", "")[:3000],
            "skill": b.get("SKILL", "")[:200],
            "effect": b.get("EFFECT", "")[:400], "risk": b.get("RISK", "")[:300],
            "rollback": b.get("ROLLBACK", "")[:300], "verify": b.get("VERIFY", "")[:400],
            "priority_claim": b.get("PRIORITY", "")[:120],
            "source_hint": b.get("SOURCE", "")[:80],
            "site_request": normalize_request(b.get("SITE_REQUEST", "")) or "",
        })
    return out


def tokens(s):
    return set(re.findall(r"[a-z0-9]{3,}", str(s).lower()))


def axis_tokens(idea):
    s = (str(idea.get("knob", "")) + " " + str(idea.get("title", ""))).lower()
    s = re.sub(r"\b\d+(?:\.\d+)?\b", " ", s)
    return tokens(s)


def norm_title(s):
    return re.sub(r"[^a-z0-9]+", "", str(s).lower())


def idea_hash(idea):
    raw = "|".join([idea.get("title", ""), idea.get("knob", ""), idea.get("effect", "")])
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


def jaccard(a, b):
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


BANNED_RE = re.compile(
    r"\b(rm\s+-rf|удали\s+весь|убрать\s+весь|заменить\s+весь|сменить\s+бренд|"
    r"клоакинг|cloaking|фейков(?:ый|ые)?\s+отзыв|ложн(?:ые|ая)?\s+цифр|"
    r"dark\s+pattern|тёмн(?:ый|ая)\s+паттерн|собирай\s+данные\s+без\s+согласия)\b",
    re.IGNORECASE,
)


def flags_for(idea):
    flags = []
    knob = idea.get("knob", "")
    if idea.get("category") == "method":
        return flags
    if BANNED_RE.search(knob) or BANNED_RE.search(idea.get("effect", "")):
        flags.append("FORBIDDEN")
    if re.search(r"\b(платный|paid|подписк)", knob, re.I) and "требует решения" not in idea.get("risk", "").lower():
        flags.append("NEEDS_OWNER")
    if re.search(r"\bmeta\s+viewport|viewport.*отключ", knob, re.I):
        flags.append("BREAKS_LAYOUT")
    if not knob.strip():
        flags.append("NO_KNOB")
    return flags


def safe_css_from(text):
    m = re.search(r"SAFE\s+CSS\s*:\s*(.*?)(?=\n[A-Z][A-Z_ ]{2,}:|$)", str(text or ""), re.I | re.S)
    if not m:
        return ""
    css = re.sub(r"</?style[^>]*>", "", m.group(1), flags=re.I).strip()
    if not css or len(css) > 6000 or css.count("{") != css.count("}"):
        return ""
    if re.search(r"@import|url\s*\(|<script|javascript:|expression\s*\(|@charset", css, re.I):
        return ""
    return css


def safe_js_from(text):
    m = re.search(r"SAFE\s+JS\s*:\s*(.*?)(?=\n[A-Z][A-Z_ ]{2,}:|$)", str(text or ""), re.I | re.S)
    if not m:
        return ""
    js = m.group(1).strip()
    if not js or len(js) > 3000 or js.count("{") != js.count("}") or js.count("(") != js.count(")"):
        return ""
    if re.search(r"fetch|XMLHttpRequest|import\s|eval\s*\(|new\s+Function|document\.write|"
                 r"innerHTML|outerHTML|\.remove\s*\(|window\.open|location\.|localStorage|"
                 r"document\.cookie|WebSocket|https?://|<script|setInterval", js, re.I):
        return ""
    return js


def write_skill_file(idea):
    """Сохраняем скилл и локально, и в переносимую библиотеку на Desktop."""
    SKILLS.mkdir(parents=True, exist_ok=True)
    LIBRARY_SKILLS.mkdir(parents=True, exist_ok=True)
    slug = re.sub(r"[^a-z0-9а-яё]+", "-", idea.get("title", "").lower()).strip("-")[:50] or "skill"
    css = safe_css_from(idea.get("knob", ""))
    js = safe_js_from(idea.get("knob", ""))
    tags = ["static-landing", "portable"]
    if "@keyframes" in css or "animation" in css:
        tags.append("animation")
    if "rotate" in css or "perspective" in css or "translateZ" in css:
        tags.append("3d")
    if "media" in css:
        tags.append("responsive")
    body = (
        "---\nname: %s\nsource: %s\nround: %s\nstatus: proposed\nportable: true\n"
        "tags: [%s]\n---\n\n# %s\n\n%s\n\n## Когда применять\n%s\n\n## Проверка\n%s\n"
        % (idea.get("title", ""), idea.get("source", ""), idea.get("round", ""),
           ", ".join(tags), idea.get("title", ""), idea.get("knob", ""),
           idea.get("effect", ""), idea.get("verify", ""))
    )
    if css:
        body += "\n## SAFE CSS\n```css\n" + css + "\n```\n"
    if js:
        body += "\n## SAFE JS\n```js\n" + js + "\n```\n"
    for target in (SKILLS / (slug + ".md"), LIBRARY_SKILLS / (slug + ".md")):
        target.write_text(body, encoding="utf-8", newline="\n")
    return slug + ".md"


def build_improved_site():
    """Собирает безопасные скиллы в ОТДЕЛЬНУЮ копию сайта. Оригинал не трогаем."""
    css_blocks, js_blocks = [], []
    for p in IDEAS.glob("I-*.json"):
        d = load_json(p, {})
        if d.get("category") != "skill":
            continue
        css = safe_css_from(d.get("knob", ""))
        js = safe_js_from(d.get("knob", ""))
        if css and css not in css_blocks:
            css_blocks.append(css)
        if js and js not in js_blocks:
            js_blocks.append(js)
    if not SITE.exists():
        return 0
    s = SITE.read_text(encoding="utf-8", errors="replace")
    out = s
    if css_blocks:
        out = re.sub(r"</head>", '<style id="factory-enhance">\n/* IDEA FACTORY: безопасные улучшения */\n'
                     + "\n\n".join(css_blocks) + '\n</style>\n</head>', out, count=1, flags=re.I)
    if js_blocks:
        js = "\n".join(js_blocks)
        out = re.sub(r"</body>", '<script id="factory-enhance">\n(function(){try{\n'
                     + js + '\n}catch(e){}})();\n</script>\n</body>', out, count=1, flags=re.I)
    target = SITE.parent / "index.improved.html"
    target.write_text(out, encoding="utf-8", newline="\n")
    save_json(STATE / "improved_build.json", {
        "time": now(), "css_blocks": len(css_blocks), "js_blocks": len(js_blocks), "file": str(target)})
    return len(css_blocks) + len(js_blocks)


def store_ideas(parsed, source, round_no, index, threshold):
    added = dups = 0
    ideas = [load_json(IDEAS / (iid + ".json"), {}) for iid in index.get("order", [])]
    for raw in parsed:
        low = (raw.get("title", "") + " " + raw.get("knob", "")).lower()
        if "skill" in low or re.search(r"safe\s+css\s*:", raw.get("knob", ""), re.I):
            raw["category"] = "skill"
        elif raw["knob"].lower().startswith("method"):
            raw["category"] = "method"
        else:
            raw["category"] = "lever"
        h = idea_hash(raw)
        toks = axis_tokens(raw)
        hit = next((iid for iid, meta in index["entries"].items() if meta.get("hash") == h), None)
        nt = norm_title(raw.get("title", ""))
        if not hit and nt:
            for old in ideas:
                if norm_title(old.get("title", "")) == nt:
                    hit = old.get("id")
                    break
        if not hit:
            best, score = None, 0.0
            for iid, meta in index["entries"].items():
                v = jaccard(toks, set(meta.get("toks", [])))
                if v > score:
                    best, score = iid, v
            if score >= threshold:
                hit = best
        if hit:
            p = IDEAS / (hit + ".json")
            idea = load_json(p, {})
            sources = idea.setdefault("sources", [])
            if source not in sources:
                sources.append(source)
            idea["mentions"] = len(sources)
            variants = idea.setdefault("variants", [])
            if raw["knob"] not in variants:
                variants.append(raw["knob"])
            save_json(p, idea)
            index["entries"][hit]["sources"] = sources
            dups += 1
            continue
        index["counter"] = int(index.get("counter", 0)) + 1
        iid = "I-%05d" % index["counter"]
        idea = {"id": iid, "round": round_no, "time": now(), "source": source,
                "sources": [source], "mentions": 1, "status": "NEW", **raw,
                "variants": [raw["knob"]]}
        idea["flags"] = flags_for(idea)
        if any(f in ("FORBIDDEN", "BREAKS_LAYOUT") for f in idea["flags"]):
            idea["status"] = "QUARANTINE"
        save_json(IDEAS / (iid + ".json"), idea)
        if idea["category"] == "skill":
            write_skill_file(idea)
        index["entries"][iid] = {"hash": h, "toks": sorted(toks), "sources": [source]}
        index.setdefault("order", []).append(iid)
        ideas.append(idea)
        added += 1
    save_json(STATE / "index.json", index)
    return added, dups


def provider_key(target):
    for key in ("api.lareper.store", "localhost:8080", "localhost:8081"):
        if key in target.get("url", ""):
            return key
    return "other"


def run_batch(targets, prompt, cfg, no_reasoning, failures, round_no, index, threshold, workers, stop_file):
    """Все модели стартуют сразу; каждая идея/скилл сохраняется сразу по готовности ответа.

    Как и в аудио-фабрике, быстрый ответ не ждёт медленного: запись в склад идёт
    в потоке main по as_completed, а не после завершения всех futures.
    """
    if not targets:
        return []
    limiters = {}
    for t in targets:
        k = provider_key(t)
        if k not in limiters:
            limiters[k] = threading.Semaphore(max(1, int(cfg.get("provider_limits", {}).get(k, 4))))
    budget = float(cfg.get("model_attempt_budget_seconds", 120))
    base_delay = float(cfg.get("retry_delay_seconds", 5))
    max_delay = float(cfg.get("retry_backoff_max_seconds", 15))
    max_attempts = int(cfg.get("max_attempts_per_model", 4))

    def call(target, timeout=None):
        payload = {
            "model": target["model"],
            "messages": [{"role": "system", "content": SYSTEM},
                         {"role": "user", "content": prompt}],
            "max_tokens": cfg.get("max_tokens", 900),
            "temperature": cfg.get("temperature", 0.65), "stream": False,
        }
        low = target["model"].lower()
        if any(low.startswith(p) for p in no_reasoning):
            payload["reasoning_effort"] = "none"
        headers = {"Content-Type": "application/json"}
        if target.get("key"):
            headers["Authorization"] = "Bearer " + target["key"]
        limit = float(timeout or target.get("timeout", 90))
        deadline = time.monotonic() + limit
        t0 = time.time()
        req = urllib.request.Request(target["url"], data=json.dumps(payload).encode("utf-8"), headers=headers)
        with urllib.request.urlopen(req, timeout=max(1.0, deadline - time.monotonic())) as r:
            resp = json.loads(r.read().decode("utf-8", "replace"))
        text = (resp.get("choices") or [{}])[0].get("message", {}).get("content") or ""
        if not str(text).strip():
            left = deadline - time.monotonic()
            if payload.get("reasoning_effort") != "none" and left > 5:
                payload["reasoning_effort"] = "none"
                req = urllib.request.Request(target["url"], data=json.dumps(payload).encode("utf-8"), headers=headers)
                with urllib.request.urlopen(req, timeout=left) as r:
                    resp = json.loads(r.read().decode("utf-8", "replace"))
                text = (resp.get("choices") or [{}])[0].get("message", {}).get("content") or ""
            if not str(text).strip():
                raise RuntimeError("empty content")
        return str(text), round(time.time() - t0, 1)

    def one(t):
        started, attempt, last = time.monotonic(), 0, "unknown"
        while time.monotonic() - started < budget:
            if stop_file.exists():
                return t, None, 0.0, "stopped", attempt
            left_total = budget - (time.monotonic() - started)
            if left_total <= 2 or attempt >= max_attempts:
                break
            attempt += 1
            call_timeout = min(float(t.get("timeout", 90)), left_total)
            with limiters[provider_key(t)]:
                try:
                    text, dt = call(t, timeout=call_timeout)
                    return t, text, dt, None, attempt
                except Exception as e:
                    last = str(e)[:160]
            left_total = budget - (time.monotonic() - started)
            if left_total <= 0 or attempt >= max_attempts:
                break
            delay = min(max_delay, base_delay * (2 ** (attempt - 1)), left_total)
            end = time.time() + delay
            while time.time() < end:
                if stop_file.exists():
                    return t, None, 0.0, "stopped", attempt
                time.sleep(min(2, max(0.2, end - time.time())))
        return t, None, 0.0, last or "budget exhausted", attempt

    failed = []

    def handle(t, text, dt, err, attempt):
        name = t["name"]
        safe = re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")[:50]
        (RAW / ("R%03d_%s.md" % (round_no, safe))).write_text(
            "# %s  %s\nduration=%s error=%s attempts=%s\n\n%s\n" % (name, now(), dt, err or "-", attempt, text or ""),
            encoding="utf-8")
        if err:
            if err != "stopped":
                delay = cooldown_after_error(failures, name, err, cfg)
                print("       -> кулдаун %.0fs, вернёмся автоматически" % delay, flush=True)
            append_log({"round": round_no, "time": now(), "model": name,
                        "status": "fail", "error": err, "attempts": attempt})
            failed.append(t)
            return
        failures.pop(name, None)
        register_site_requests(text)
        parsed = parse_ideas(text)
        if not parsed and re.search(r"NO_NEW_IDEAS", text, re.I):
            append_log({"round": round_no, "time": now(), "model": name, "status": "no_new", "attempts": attempt})
            return
        added, dups = store_ideas(parsed, name, round_no, index, threshold)
        append_log({"round": round_no, "time": now(), "model": name, "status": "ok",
                    "duration": dt, "parsed": len(parsed), "added": added, "dups": dups, "attempts": attempt})
        print("       -> %d новых, %d повторов" % (added, dups), flush=True)

    with ThreadPoolExecutor(max_workers=max(1, workers)) as ex:
        futs = {ex.submit(one, t): t for t in targets}
        for fut in as_completed(futs):
            t, text, dt, err, attempt = fut.result()
            if err:
                print("  FAIL %-42s %s (%d поп.)" % (t["name"], str(err)[:70], attempt), flush=True)
            else:
                print("  OK   %-42s %5.1fs %d chars (%d поп.)" % (t["name"], dt, len(text), attempt), flush=True)
            handle(t, text, dt, err, attempt)
    return failed


def wait_with_stop(seconds, stop_file):
    end = time.time() + seconds
    while time.time() < end:
        if stop_file.exists():
            return False
        time.sleep(min(15, max(0.2, end - time.time())))
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--hours", type=float, default=None)
    ap.add_argument("--interval", type=int, default=None)
    ap.add_argument("--rounds", type=int, default=None)
    ap.add_argument("--workers", type=int, default=None)
    args = ap.parse_args()
    for d in (STATE, RAW, IDEAS, SKILLS):
        d.mkdir(parents=True, exist_ok=True)
    if not acquire_lock():
        return 3
    cfg = load_json(BASE / "config.json", {})
    if not cfg:
        print("CONFIG MISSING", file=sys.stderr)
        return 2
    hours = args.hours if args.hours is not None else cfg.get("hours", 8)
    interval = args.interval if args.interval is not None else cfg.get("interval_seconds", 120)
    max_rounds = args.rounds if args.rounds is not None else cfg.get("max_rounds", 250)
    workers = args.workers if args.workers is not None else cfg.get("workers", 14)
    stop_file = BASE / cfg.get("stop_file", "stop.flag")
    threshold = cfg.get("dedup_jaccard", 0.68)
    no_reasoning = cfg.get("no_reasoning_prefixes", [])
    targets = build_targets(cfg, lareper_key())
    index = load_json(STATE / "index.json", {"counter": 0, "entries": {}, "order": []})
    failures = load_json(STATE / "failures.json", {})
    cooldown_cap = float(cfg.get("retry_max_cooldown_seconds", 120))
    for info in failures.values():
        if float(info.get("retry_after", 0)) > time.time() + cooldown_cap:
            info["retry_delay"] = min(cooldown_cap, float(info.get("retry_delay", cooldown_cap)))
            info["retry_after"] = time.time() + float(info["retry_delay"])
    round_no = load_json(STATE / "last_round.json", {"round": 0}).get("round", 0)
    budget_s = hours * 3600
    active_s = 0.0
    print("SITE FACTORY: %d моделей, %d параллельно, %dс на модель, %d раундов, %s" %
          (len(targets), workers, cfg.get("model_attempt_budget_seconds", 120), max_rounds, SITE), flush=True)
    while round_no < max_rounds and active_s < budget_s:
        if stop_file.exists():
            print("STOP FLAG — выход", flush=True)
            break
        round_no += 1
        t_round = time.monotonic()
        try:
            save_json(STATE / "last_round.json", {"round": round_no, "time": now()})
            loaded = [load_json(IDEAS / (iid + ".json"), {}) for iid in index.get("order", [])]
            prompt = build_prompt(round_no, loaded, round_no - 1,
                                  site_snapshot(force=(round_no == 1)), site_answers_block())
            chosen = select_targets(targets, failures, workers)
            if not chosen:
                eta = min((float(failures.get(t["name"], {}).get("retry_after", 0)) for t in targets), default=0)
                if not wait_with_stop(max(5, min(120, eta - time.time() + 2)), stop_file):
                    break
                continue
            print("\n=== ROUND %d (%s) targets %d ===" % (round_no, now(), len(chosen)), flush=True)
            run_batch(chosen, prompt, cfg, no_reasoning, failures, round_no, index, threshold, workers, stop_file)
            n_css = build_improved_site()
            if n_css:
                print("SITE: собрано %d безопасных блоков (CSS/JS) -> index.improved.html" % n_css, flush=True)
            save_json(STATE / "failures.json", failures)
            n = answer_site_requests()
            if n:
                print("SITE_REQUEST: отвечено %d, ответы в state/site_answers.json" % n, flush=True)
            print("ИТОГО раунд %d: идей %d" % (round_no, len(index.get("order", []))), flush=True)
            if round_no >= max_rounds:
                break
            if not wait_with_stop(interval, stop_file):
                break
        except Exception as e:
            append_log({"round": round_no, "time": now(), "status": "round_error", "error": str(e)[:200]})
            print("ROUND ERROR (продолжаем): %s" % str(e)[:160], flush=True)
            if not wait_with_stop(30, stop_file):
                break
        finally:
            active_s += min(max(0.0, time.monotonic() - t_round), interval + 300)
    print("Фабрика сайта завершилась. Утром: python site_merge.py", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
