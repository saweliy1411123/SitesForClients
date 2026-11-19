@echo off
cd /d "%~dp0"
if exist stop.flag (
  echo Removing old stop.flag
  del stop.flag
)
set PY=python
where python >nul 2>nul || set PY=py -3
echo SITE FACTORY starting: fast retry, 45s interval, 120s per model
echo Etalon: "Kafe Vechernee" standard, constructor uses lareper GLM-first
echo To stop: create stop.flag in this folder
%PY% site_overnight.py --hours 8 --interval 45
echo.
echo Factory stopped. In the morning run: python site_merge.py
pause
