#!/usr/bin/env python3
"""Простой статус фабрики сайта."""
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE))
import site_overnight as soi

STATE = BASE / "state"
lock = STATE / "run.lock"
pid = 0
try:
    pid = int(lock.read_text(encoding="utf-8").strip())
except Exception:
    pass
alive = soi.pid_alive(pid)
last = soi.load_json(STATE / "last_round.json", {})
ideas = len(list((BASE / "ideas").glob("I-*.json")))
skills = len(list((BASE / "SKILLS").glob("*.md")))
stop = (BASE / "stop.flag").exists()
imp = soi.load_json(STATE / "improved_build.json", {})
last_ok = "ещё не было"
log = STATE / "log.jsonl"
if log.exists():
    for line in log.read_text(encoding="utf-8").splitlines():
        try:
            e = json.loads(line)
            if e.get("status") == "ok":
                last_ok = e.get("time", "?")
        except Exception:
            pass

print("=== ФАБРИКА САЙТА ===")
print("СТАТУС: %s" % ("РАБОТАЕТ (pid %d)" % pid if alive else "НЕ РАБОТАЕТ — запусти START_SITE_FACTORY.bat"))
print("Раунд:            %s" % last.get("round", "?"))
print("Идей в куче:      %d" % ideas)
print("Скиллов:          %d" % skills)
print("Последний ответ:  %s" % last_ok)
print("CSS/JS-блоков:    %s / %s" % (imp.get("css_blocks", 0), imp.get("js_blocks", 0)))
print("Улучшенная копия: %s" % ("есть" if (BASE.parent / "index.improved.html").exists() else "пока нет"))
print("stop.flag:        %s" % ("ЕСТЬ" if stop else "нет"))
