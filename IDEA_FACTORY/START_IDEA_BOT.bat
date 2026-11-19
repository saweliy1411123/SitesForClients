@echo off
cd /d "%~dp0"
if exist bot_stop.flag del bot_stop.flag
set PY=python
where python >nul 2>nul || set PY=py -3
echo SITE IDEA BOT starting: 20 rounds, 120s interval, all models
echo To stop: create bot_stop.flag or run STOP_BOT.bat
%PY% -u site_idea_bot.py --rounds 20 --interval 120
pause
