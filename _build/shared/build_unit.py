# -*- coding: utf-8 -*-
"""Generic builder: build(...) assembles one unit into ../../<folder>/index.html"""
import os, json
from balance import fix_all
import typeset

def build(S_list, unit_dir, folder, title, lesson_name, extra_js='', extra_css=''):
    here = os.path.dirname(os.path.abspath(__file__))
    BUILD = os.path.join(here, '..')
    OUT = os.path.join(BUILD, '..', folder, 'index.html')
    URL = 'https://teacher-nanda.github.io/Business-EFE2/%s/index.html' % folder
    rd = lambda p: open(p, encoding='utf-8').read()
    S = typeset.apply(fix_all(S_list))
    ids = [s[0] for s in S]; labels = [s[1] for s in S]
    head = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>%s</title>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;500;700;800&display=swap" rel="stylesheet">\n<style>\n') % title
    base_css = rd(os.path.join(here, 'base.css')).replace('AEF4 4B \\2014  A Risky Business', lesson_name)
    js_gen = rd(os.path.join(here, 'js_generic.js'))
    js_gen = js_gen.replace("function saveNotes(){ notesData[current] = document.getElementById('notesTA').innerHTML; }",
        "function saveNotes(){ notesData[current] = document.getElementById('notesTA').innerHTML; try{ localStorage.setItem(notesStoreKey, JSON.stringify(notesData)); }catch(e){} }")
    js_gen = js_gen.replace('Notes – AEF4 4B', 'Notes – ' + lesson_name).replace('AEF4 4B – A Risky Business', lesson_name)
    js_nav = rd(os.path.join(here, 'js_nav.js')).replace("'befeNotes::'", "'befeNotes::%s::'" % folder) if "'befeNotes::'" in rd(os.path.join(here, 'js_nav.js')) else rd(os.path.join(here, 'js_nav.js'))
    js_common = rd(os.path.join(here, 'js_common.js')).replace('__LESSON_NAME__', lesson_name).replace('__URL__', URL)
    out = head + base_css + '\n' + rd(os.path.join(here, 'theme.css')) + '\n' + extra_css + typeset.RULE_CSS + '\n</style>\n</head>\n<body>\n'
    out += rd(os.path.join(here, 'chrome.html')) + '\n<div id="deck">\n\n' + '\n\n'.join(s[2] for s in S) + '\n\n</div><!-- END #deck -->\n\n' + rd(os.path.join(here, 'nav.html')) + '\n'
    out += '<script>\n/* ===================== SLIDE NAV DATA ===================== */\n'
    out += 'var slideIds = ' + json.dumps(ids) + ';\nvar slideLabels = ' + json.dumps(labels, ensure_ascii=False) + ';\n'
    out += js_nav + '\n' + js_gen + '\n' + js_common + '\n' + rd(os.path.join(here, 'clips.js')) + '\n' + rd(os.path.join(here, 'js_unit.js')) + '\n' + extra_js + '\n</script>\n</body>\n</html>\n'
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, 'w', encoding='utf-8').write(out)
    print(len(S), 'slides', len(out), 'bytes ->', os.path.abspath(OUT))
    return S
