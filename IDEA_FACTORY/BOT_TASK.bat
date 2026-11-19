@echo off
cd /d "%~dp0"
set PY=python
where python >nul 2>nul || set PY=py -3
%PY% -u site_idea_bot.py --rounds 20 --interval 120 > idea_bot.log 2> idea_bot.err.log
