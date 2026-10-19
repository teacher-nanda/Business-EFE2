# -*- coding: utf-8 -*-
"""Build Business-EFE2 / Unit 1 -> ../../U01-Introductions/index.html   (run: python3 build.py)"""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '..'))
os.chdir(HERE)
import lib, s_lesson, s_hw          # noqa: F401  (importing registers the slides in order)
from balance import fix_all

TITLE_FULL = "Unit 1 — Introductions"
LESSON_NAME = "Business English · Unit 1 · Introductions"
URL = "https://teacher-nanda.github.io/Business-EFE2/U01-Introductions/index.html"
OUT = os.path.join(HERE, '..', '..', 'U01-Introductions', 'index.html')

S = fix_all(lib.S)
ids = [s[0] for s in S]
labels = [s[1] for s in S]
slides_html = "\n\n".join(s[2] for s in S)

SH = os.path.join(HERE, '..', 'shared')
def rd(p): return open(p, encoding='utf-8').read()

head = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;500;700;800&display=swap" rel="stylesheet">
<style>
''' % TITLE_FULL

base_css = rd(os.path.join(SH, 'base.css')).replace('AEF4 4B \\2014  A Risky Business', LESSON_NAME)
theme = rd('theme.css')
chrome = rd(os.path.join(SH, 'chrome.html'))
nav = rd(os.path.join(SH, 'nav.html'))
js_nav = rd(os.path.join(SH, 'js_nav.js'))
js_gen = rd(os.path.join(SH, 'js_generic.js'))
js_common = rd(os.path.join(SH, 'js_common.js'))
js_new = rd('js_new.js')

# generic notes: persist to localStorage on every keystroke; neutralize the old per-lesson strings
js_gen = js_gen.replace("function saveNotes(){ notesData[current] = document.getElementById('notesTA').innerHTML; }",
                        "function saveNotes(){ notesData[current] = document.getElementById('notesTA').innerHTML; try{ localStorage.setItem(notesStoreKey, JSON.stringify(notesData)); }catch(e){} }")
js_gen = js_gen.replace('Notes – AEF4 4B', 'Notes – ' + LESSON_NAME).replace('AEF4 4B – A Risky Business', LESSON_NAME)
js_common = js_common.replace('__LESSON_NAME__', LESSON_NAME).replace('__URL__', URL)

out = head + base_css + "\n" + theme + "\n</style>\n</head>\n<body>\n"
out += chrome + "\n<div id=\"deck\">\n\n" + slides_html + "\n\n</div><!-- END #deck -->\n\n" + nav + "\n"
out += "<script>\n/* ===================== SLIDE NAV DATA ===================== */\n"
out += "var slideIds = " + json.dumps(ids) + ";\n"
out += "var slideLabels = " + json.dumps(labels, ensure_ascii=False) + ";\n"
out += js_nav + "\n" + js_gen + "\n" + js_common + "\n" + js_new + "\n</script>\n</body>\n</html>\n"

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w', encoding='utf-8').write(out)
print(len(S), 'slides', len(out), 'bytes ->', os.path.abspath(OUT))
