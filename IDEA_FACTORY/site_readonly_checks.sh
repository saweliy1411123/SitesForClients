#!/bin/sh
# Только чтение. В Git-Bash: sh site_readonly_checks.sh
cd ".."
git status --short
git diff --stat
md5sum index.html index.improved.html 2>/dev/null
wc -l index.html index.improved.html 2>/dev/null
grep -i -m1 '<title' index.html
grep -c '<h2' index.html
