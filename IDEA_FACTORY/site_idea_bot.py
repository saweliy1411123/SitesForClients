#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Бот «Фабрика идей сайтов»: все модели придумывают концепт, лучший превращается в сайт.

Использует тот же пул моделей и config.json, что и ночная фабрика улучшений.
Оригинальный index.html НЕ трогает. Сайты пишет в generated_sites/.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import threading
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path

import site_overnight as factory

BASE = Path(__file__).resolve().parent
CFG = factory.load_json(BASE / "config.json", {})
RAW = BASE / "state" / "idea_bot_raw"
OUT = BASE / "generated_sites"
STATUS = BASE / "BOT_STATUS.md"
STORE = BASE / "state" / "idea_bot.json"
STOP = BASE / "bot_stop.flag"
RAW.mkdir(parents=True, exist_ok=True)
OUT.mkdir(parents=True, exist_ok=True)

SYSTEM = (
    "Ты продуктовый дизайнер и копирайтер. Возвращай ТОЛЬКО валидный JSON без пояснений. "
    "Не используйmarkdown, не пиши вступлений. Все строки на русском. "
    "Не выдумывай фейковые отзывы, цифры и документы."
)

PROMPT = """Придумай НОВУЮ идею одностраничного сайта для реального малого бизнеса в России.
Концепт должен отличаться от последних: {recent}

Верни JSON строго такого вида:
{{
 "name":"короткое название бренда",
 "niche":"сфера",
 "tagline":"главный заголовок до 8 слов",
 "sub":"подзаголовок до 160 символов",
 "problems":[{{"t":"проблема 1","d":"описание до 140 символов"}},{{"t":"проблема 2","d":"описание"}},{{"t":"проблема 3","d":"описание"}}],
 "steps":["шаг 1","шаг 2","шаг 3"],
 "services":["услуга 1","услуга 2","услуга 3","услуга 4"],
 "price":"цена или 'по запросу'",
 "price_note":"что входит",
 "faq":[["вопрос 1","ответ 1"],["вопрос 2","ответ 2"],["вопрос 3","ответ 3"]],
 "cta":"текст кнопки",
 "accent":"#7c5cff",
 "accent2":"#00e5b0",
 "photo_prompts":["запрос фото 1","запрос фото 2","запрос фото 3"]
}}
Только JSON."""


def now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def log(msg: str) -> None:
    print("[" + now() + "] " + msg, flush=True)


def save_status(text: str) -> None:
    STATUS.write_text(text, encoding="utf-8")


def load_store() -> dict:
    return factory.load_json(STORE, {"rounds": [], "concepts": []})


def save_store(obj: dict) -> None:
    factory.save_json(STORE, obj)


def clean_json(text: str) -> dict | None:
    if not text:
        return None
    t = text.strip()
    t = re.sub(r"^```(?:json)?\s*", "", t, flags=re.I)
    t = re.sub(r"\s*```$", "", t)
    a, b = t.find("{"), t.rfind("}")
    if a < 0 or b <= a:
        return None
    try:
        obj = json.loads(t[a:b + 1])
    except Exception:
        return None
    return obj if isinstance(obj, dict) else None


def txt(v, limit=300) -> str:
    s = re.sub(r"\s+", " ", str(v or "")).strip()
    return html.escape(s[:limit])


def norm_list(v, n=3, limit=140) -> list:
    if not isinstance(v, list):
        return []
    out = []
    for x in v:
        if isinstance(x, dict):
            x = x.get("t") or x.get("title") or x.get("d") or ""
        s = re.sub(r"\s+", " ", str(x or "")).strip()
        if s:
            out.append(html.escape(s[:limit]))
        if len(out) >= n:
            break
    return out


def norm_problems(v) -> list:
    if not isinstance(v, list):
        return []
    out = []
    for x in v[:3]:
        if isinstance(x, dict):
            t = txt(x.get("t") or x.get("title"), 90)
            d = txt(x.get("d") or x.get("desc"), 160)
        else:
            t, d = txt(x, 90), ""
        if t:
            out.append({"t": t, "d": d})
    return out


def norm_faq(v) -> list:
    out = []
    if not isinstance(v, list):
        return out
    for x in v[:3]:
        if isinstance(x, (list, tuple)) and len(x) >= 2:
            q, a = txt(x[0], 120), txt(x[1], 220)
        elif isinstance(x, dict):
            q, a = txt(x.get("q"), 120), txt(x.get("a"), 220)
        else:
            continue
        if q and a:
            out.append((q, a))
    return out


def color(v, default) -> str:
    s = str(v or "").strip()
    return s if re.fullmatch(r"#[0-9a-fA-F]{6}", s) else default


def score(obj: dict, store: dict) -> float:
    s = 0.0
    s += 2 if obj.get("name") else 0
    s += 3 if len(obj.get("tagline", "")) > 8 else 0
    s += 2 if len(obj.get("sub", "")) > 30 else 0
    s += 1.5 * len(obj.get("problems", []))
    s += 1.0 * len(obj.get("steps", []))
    s += 0.5 * len(obj.get("services", []))
    s += 0.8 * len(obj.get("faq", []))
    s += 1 if obj.get("price") else 0
    tokens = set(re.findall(r"[a-zа-яё]{4,}", (obj.get("name", "") + " " + obj.get("tagline", "")).lower()))
    for old in store.get("concepts", [])[-25:]:
        old_tokens = set(re.findall(r"[a-zа-яё]{4,}", str(old).lower()))
        if tokens & old_tokens:
            s -= 2
    return s


def slug(s: str) -> str:
    s = re.sub(r"[^a-zа-яё0-9]+", "-", str(s).lower(), flags=re.I).strip("-")
    return (s or "idea")[:36]


def render(c: dict) -> str:
    acc, acc2 = color(c.get("accent"), "#7c5cff"), color(c.get("accent2"), "#00e5b0")
    probs = "".join(
        '<article class="card rise"><span>0%d</span><h3>%s</h3><p>%s</p></article>' % (i + 1, p["t"], p["d"])
        for i, p in enumerate(c["problems"])
    )
    steps = "".join('<div class="step"><b>%02d</b><span>%s</span></div>' % (i + 1, s) for i, s in enumerate(c["steps"]))
    servs = "".join('<li>%s</li>' % s for s in c["services"])
    faq = "".join(
        '<details><summary>%s</summary><div class="body"><p>%s</p></div></details>' % (q, a)
        for q, a in c["faq"]
    )
    photos = c.get("photo_prompts", [])
    photo_note = ("Фото-запросы для следующего этапа: " + "; ".join(photos[:3])) if photos else ""
    return """<!DOCTYPE html>
<html lang="ru"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="dark"><title>%(name)s — %(niche)s</title>
<style>
:root{--a:%(acc)s;--b:%(acc2)s;--bg:#060810;--s:#101625;--l:#273149;--i:#f3f6ff;--m:#9aa5bd}
*{box-sizing:border-box}body{margin:0;background:radial-gradient(50%% 40%% at 15%% 10%%,color-mix(in oklch,var(--a) 40%%,transparent),transparent 70%%),radial-gradient(50%% 40%% at 85%% 70%%,color-mix(in oklch,var(--b) 30%%,transparent),transparent 70%%),var(--bg);color:var(--i);font:16px/1.6 system-ui,sans-serif;overflow-x:hidden}
.w{width:min(1120px,calc(100%% - 40px));margin:auto}section{padding:90px 0}
h1,h2,h3{margin:0;letter-spacing:-.04em}h1{font-size:clamp(44px,8vw,100px);line-height:.92;max-width:15ch}h2{font-size:clamp(30px,5vw,56px);line-height:1.04}
.tag{color:var(--b);font-size:12px;letter-spacing:.18em;text-transform:uppercase;font-weight:800}.g{background:linear-gradient(100deg,var(--a),var(--b));-webkit-background-clip:text;background-clip:text;color:transparent}
.lede{color:var(--m);max-width:58ch;font-size:18px}.btn{display:inline-block;background:var(--a);color:#fff;padding:13px 22px;border-radius:12px;font-weight:750;margin-top:26px}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px;margin-top:38px}
.card,.price,.step,.faq details{background:var(--s);border:1px solid var(--l);border-radius:20px;padding:24px}
.card span{color:var(--b);font-weight:800;font-size:12px;letter-spacing:.2em}.card h3{font-size:20px;margin:10px 0 8px}.card p{color:var(--m);font-size:14px;margin:0}
.steps{display:grid;gap:12px;margin-top:30px}.step{display:flex;gap:16px;align-items:baseline}.step b{color:var(--b)}.step span{color:var(--m)}
ul{columns:2;max-width:620px;margin:26px 0 0;padding-left:22px;color:var(--m)}li{margin-bottom:10px}
.price{display:flex;justify-content:space-between;gap:20px;align-items:center;flex-wrap:wrap}.price b{font-size:44px;display:block;letter-spacing:-.05em}.price small{color:var(--m)}
.faq{display:grid;gap:12px;max-width:760px;margin-top:30px}summary{cursor:pointer;font-weight:700;list-style:none}summary::-webkit-details-marker{display:none}summary::after{content:"＋";float:right;color:var(--b)}details[open] summary::after{content:"−"}.body{overflow:hidden;transition:height .35s}.body p{color:var(--m);margin:12px 0 0}
footer{border-top:1px solid var(--l);padding:30px 0;color:var(--m);font-size:13px;background:#060810}.rise{opacity:0;translate:0 20px;transition:.7s}.rise.vis{opacity:1;translate:0 0}
@media(max-width:600px){section{padding:60px 0}h1{font-size:42px}ul{columns:1}.price b{font-size:34px}}
@media(prefers-reduced-motion:reduce){*{transition:none!important}.rise{opacity:1;translate:0}}
</style></head><body>
<header class="w" style="padding:24px 0;display:flex;justify-content:space-between"><b>%(name)s</b><a class="btn" href="#cta" style="margin:0;padding:8px 14px">%(cta)s</a></header>
<main>
<section class="w"><span class="tag">%(niche)s</span><h1>%(tagline)s</h1><p class="lede">%(sub)s</p><a class="btn" href="#cta">%(cta)s →</a></section>
<section class="w"><span class="tag">Проблемы</span><h2>Почему сейчас теряются клиенты</h2><div class="grid">%(probs)s</div></section>
<section class="w"><span class="tag">Как работаем</span><h2>От заявки до результата</h2><div class="steps">%(steps)s</div></section>
<section class="w"><span class="tag">Что входит</span><h2>Услуги</h2><ul>%(servs)s</ul></section>
<section class="w"><span class="tag">Цена</span><div class="price"><div><b>%(price)s</b><small>%(price_note)s</small></div><a class="btn" href="#cta">%(cta)s</a></div></section>
<section class="w"><span class="tag">Вопросы</span><h2>Что уточняют</h2><div class="faq">%(faq)s</div></section>
<section class="w" id="cta" style="text-align:center"><span class="tag" style="justify-content:center">Начнём</span><h2>Сделать сайт под ваш бизнес</h2><a class="btn" href="https://t.me/TrainersDontPlays">Написать в Telegram →</a><p class="mini-note" style="color:var(--m);font-size:12px">%(photo_note)s</p></section>
</main><footer><div class="w">Сгенерировано фабрикой идей сайтов · %(time)s</div></footer>
<script>
const io=new IntersectionObserver(e=>e.forEach(x=>{if(x.isIntersecting)x.target.classList.add('vis')}),{threshold:.1});
document.querySelectorAll('.rise').forEach(x=>io.observe(x));
document.querySelectorAll('details').forEach(d=>d.querySelector('summary').addEventListener('click',e=>{e.preventDefault();const b=d.querySelector('.body');if(d.open){b.style.height=b.scrollHeight+'px';requestAnimationFrame(()=>b.style.height='0px');setTimeout(()=>d.open=false,360)}else{d.open=true;b.style.height='0px';requestAnimationFrame(()=>b.style.height=b.scrollHeight+'px');setTimeout(()=>{if(d.open)b.style.height='auto'},360)}}));
</script></body></html>""" % dict(
        name=c.get("name", "Идея"), niche=c.get("niche", "бизнес"), acc=acc, acc2=acc2,
        tagline=c.get("tagline", "Сайт для вашего дела"), sub=c.get("sub", ""), cta=c.get("cta", "Записаться"),
        probs=probs, steps=steps, servs=servs, price=c.get("price", "по запросу"),
        price_note=c.get("price_note", ""), faq=faq, photo_note=txt(photo_note, 300), time=now()
    )


def normalize(obj: dict) -> dict:
    return {
        "name": txt(obj.get("name"), 50) or "Новый проект",
        "niche": txt(obj.get("niche"), 70) or "малый бизнес",
        "tagline": txt(obj.get("tagline"), 110) or "Сайт, который приводит клиентов",
        "sub": txt(obj.get("sub"), 220),
        "problems": norm_problems(obj.get("problems")),
        "steps": norm_list(obj.get("steps"), 3),
        "services": norm_list(obj.get("services"), 4),
        "price": txt(obj.get("price"), 40) or "по запросу",
        "price_note": txt(obj.get("price_note"), 160),
        "faq": norm_faq(obj.get("faq")),
        "cta": txt(obj.get("cta"), 50) or "Записаться",
        "accent": color(obj.get("accent"), "#7c5cff"),
        "accent2": color(obj.get("accent2"), "#00e5b0"),
        "photo_prompts": norm_list(obj.get("photo_prompts"), 3, 140),
    }


def call_model(target: dict, prompt: str, timeout: float) -> tuple[str, float, str]:
    payload = {
        "model": target["model"],
        "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}],
        "max_tokens": int(CFG.get("max_tokens", 900)),
        "temperature": float(CFG.get("temperature", 0.7)),
        "stream": False,
    }
    low = target["model"].lower()
    if low.startswith("glm-") or target["name"].startswith("lareper/"):
        payload["reasoning_effort"] = "none"
    payload["max_tokens"] = max(int(CFG.get("max_tokens", 900)), 1200)
    headers = {"Content-Type": "application/json"}
    if target.get("key"):
        headers["Authorization"] = "Bearer " + target["key"]
    t0 = time.time()
    req = urllib.request.Request(target["url"], data=json.dumps(payload).encode("utf-8"), headers=headers)
    with urllib.request.urlopen(req, timeout=max(2.0, timeout)) as r:
        resp = json.loads(r.read().decode("utf-8", "replace"))
    text = (resp.get("choices") or [{}])[0].get("message", {}).get("content") or ""
    return str(text), round(time.time() - t0, 1), ""


def pick_targets(limit=None, local_only=False):
    targets = factory.build_targets(CFG, factory.lareper_key())
    if local_only:
        targets = [t for t in targets if not t["name"].startswith("lareper/")]
    if limit:
        targets = targets[:limit]
    return targets


def ask_all(round_no: int, recent: str, limit: int | None = None, local_only: bool = False) -> list:
    targets = pick_targets(limit, local_only)
    prompt = PROMPT.format(recent=recent)
    limiters = {}
    for t in targets:
        k = factory.provider_key(t)
        if k not in limiters:
            limiters[k] = threading.Semaphore(max(1, int(CFG.get("provider_limits", {}).get(k, 4))))
    results = []

    def one(t):
        is_lareper = t["name"].startswith("lareper/")
        max_attempts = 1 if is_lareper else 2
        for attempt in range(max_attempts):
            if STOP.exists():
                return t, "", 0, "stopped"
            with limiters[factory.provider_key(t)]:
                try:
                    call_timeout = min(float(t.get("timeout", 75)), 30 if is_lareper else 85)
                    text, dt, err = call_model(t, prompt, call_timeout)
                    if text.strip():
                        return t, text, dt, ""
                    err = "empty"
                except Exception as e:
                    err = str(e)[:140]
            time.sleep(2 + attempt * 3)
        return t, "", 0, err

    with ThreadPoolExecutor(max_workers=max(2, min(8, int(CFG.get("workers", 8))))) as ex:
        futs = [ex.submit(one, t) for t in targets]
        for fut in as_completed(futs):
            results.append(fut.result())
    for t, text, dt, err in results:
        safe = re.sub(r"[^a-z0-9]+", "_", t["name"].lower()).strip("_")[:50]
        (RAW / ("R%03d_%s.txt" % (round_no, safe))).write_text(
            "# %s  dt=%s err=%s\n\n%s" % (t["name"], dt, err or "-", text), encoding="utf-8")
    return results


def run_round(round_no: int, store: dict, limit: int | None = None, local_only: bool = False) -> bool:
    recent = ", ".join(store.get("concepts", [])[-6:]) or "нет"
    targets = pick_targets(limit, local_only)
    log("round %d: asking %d models" % (round_no, len(targets)))
    results = ask_all(round_no, recent, limit, local_only)
    concepts = []
    ok = 0
    for t, text, dt, err in results:
        if not text:
            log("  FAIL %-40s %s" % (t["name"], err))
            continue
        obj = clean_json(text)
        if not obj:
            log("  BAD  %-40s not json" % t["name"])
            continue
        c = normalize(obj)
        c["_model"] = t["name"]
        c["_score"] = score(c, store)
        concepts.append(c)
        ok += 1
        log("  OK   %-40s %5.1fs %s" % (t["name"], dt, c["name"]))
    if not concepts:
        log("no usable concepts this round")
        return False
    concepts.sort(key=lambda x: x["_score"], reverse=True)
    best = concepts[0]
    dest = OUT / (time.strftime("%Y%m%d-%H%M") + "-" + slug(best["name"]) + ".html")
    dest.write_text(render(best), encoding="utf-8")
    (OUT / "latest.html").write_text(dest.read_text(encoding="utf-8"), encoding="utf-8")
    store.setdefault("rounds", []).append({
        "round": round_no, "time": now(), "models_ok": ok, "models_total": len(results),
        "winner": best["name"], "model": best["_model"], "file": str(dest), "score": round(best["_score"], 1)
    })
    store.setdefault("concepts", []).append(best["name"] + " — " + best["tagline"])
    save_store(store)
    save_status("# Фабрика идей сайтов — статус\n\n- Обновлено: %s\n- Раундов: %d\n- Последний сайт: %s\n- Победитель: %s\n- Моделей ответило: %d/%d\n- Всего сайтов: %d\n\nОстановить: создать `bot_stop.flag` в этой папке.\n" % (
        now(), len(store["rounds"]), dest.name, best["name"], ok, len(results), len(list(OUT.glob("*.html")))))
    log("WINNER %s (%s) -> %s" % (best["name"], best["_model"], dest.name))
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rounds", type=int, default=12)
    ap.add_argument("--interval", type=int, default=120)
    ap.add_argument("--once", action="store_true")
    ap.add_argument("--limit", type=int, default=0, help="только первые N моделей (для проверки)")
    ap.add_argument("--local", action="store_true", help="не звать lareper, только локальные пулы")
    args = ap.parse_args()
    if STOP.exists():
        STOP.unlink()
    store = load_store()
    for r in range(1, args.rounds + 1):
        if STOP.exists():
            log("stop flag found")
            break
        try:
            run_round(r, store, args.limit or None, args.local)
        except Exception as e:
            log("ROUND ERROR %s" % e)
        if args.once:
            break
        if r < args.rounds:
            end = time.time() + args.interval
            while time.time() < end and not STOP.exists():
                time.sleep(min(5, max(0.5, end - time.time())))
    log("finished")


if __name__ == "__main__":
    main()
