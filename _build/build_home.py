# -*- coding: utf-8 -*-
"""Build the Business-EFE2 course homepage (../index.html).  Run: python3 build_home.py
Edit STATUS below: 'ready' = open link, 'draft' = open link with a Draft tag, anything else = locked 'Soon'."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'index.html')

STATUS = {1: 'draft'}
FOLDER = {1: 'U01-Introductions'}

# (unit, title, new language, vocabulary, skill)   — from the course contents
U = [
 (1,'Introductions','Present simple and continuous','Etiquette for introductions','Introducing yourself and others'),
 (2,'Getting to know colleagues','Past simple and past continuous','Sharing past experiences','Talking about past experiences'),
 (3,'Departments and roles',None,'Departments and roles',None),
 (4,'Talking about changes','“Used to,” “be / get used to”','Small talk','Talking about changes at work'),
 (5,'Delegating tasks','Modal verbs for obligation','Delegation and politeness','Delegating tasks to colleagues'),
 (6,'Money and finance',None,'Money and finance',None),
 (7,'Writing a report','Past perfect and past simple','Formal business English','Writing reports'),
 (8,'Making apologies','Present perfect continuous','Apologies','Apologizing on the telephone'),
 (9,'Communication technology',None,'Communication technology',None),
 (10,'Making plans by email','Email language','Meetings and workshops','Making plans'),
 (11,'Keeping clients informed','Continuous tenses','Arrangements and schedules','Keeping clients informed'),
 (12,'Informal communication','Phrasal verbs','Arrangements and plans','Keeping co-workers informed'),
 (13,'Production',None,'Production',None),
 (14,'Describing a process','The passive voice','Processes and manufacturing','Discussing how things are done'),
 (15,'Describing a product','Adjective order','Opinion and fact adjectives','Describing a product'),
 (16,'Marketing and advertising',None,'Marketing and advertising',None),
 (17,'Marketing a product','Adjectives and adverbs','Descriptive adjectives','Modifying descriptions of products'),
 (18,'Advertising and branding','Intensifiers','“Enough,” “too,” “so,” and “such”','Adding emphasis to descriptions'),
 (19,'Advice and suggestions','Modal verbs for advice','Workplace pressures','Giving advice'),
 (20,'Management, leadership, and skills',None,'Management, leadership, and skills',None),
 (21,'Talking about abilities','Modal verbs for abilities','Workplace skills','Describing abilities'),
 (22,'Comparing and contrasting','Discourse markers','Teamwork and team building','Expressing your ideas'),
 (23,'Planning events','Verb patterns','Corporate entertainment','Talking about business events'),
 (24,'Meetings',None,'Meetings',None),
 (25,'What people said','Reported speech','Meetings','Reporting what someone said'),
 (26,'What people asked','Reported questions','“Have,” “make,” “get,” “do”','Reporting what someone asked'),
 (27,'Reporting quantities','“Few,” “little,” and “all”','Meetings','Talking about quantity'),
 (28,'Checking information','Subject questions, question tags','Polite checks and echo questions','Checking information'),
 (29,'Industries and professional attributes',None,'Industries and professional attributes',None),
 (30,'Job descriptions','Articles','Job descriptions and applications','Describing a job'),
 (31,'Applying for a job','Dependent prepositions','Cover-letter vocabulary','Writing a cover letter'),
 (32,'Job interviews','Relative clauses','Job interviews','Describing your achievements in detail'),
 (33,'Business idioms',None,'Business idioms',None),
 (34,'Working relationships','Three-word phrasal verbs','Social media','Social networking'),
 (35,'Career outcomes','Modal verbs for possibility','Career development','Talking about the future'),
 (36,'Office and presentation equipment',None,'Office and presentation equipment',None),
 (37,'Structuring a presentation','Signposting language','Presentation equipment','Structuring a presentation'),
 (38,'Developing an argument','Useful presentation language','Presentations','Developing an argument'),
 (39,'Pitching a product','Comparatives and superlatives','Product marketing','Comparing products'),
 (40,'Talking about facts and figures','Collocations','Business trends','Describing facts and figures'),
 (41,'Plans and suggestions','Indirect questions','Business negotiations','Negotiating politely'),
 (42,'Emphasizing your opinion','Discourse markers for emphasis','Workplace disagreement','Emphasizing your opinion'),
 (43,'Discussing conditions','Conditionals','Negotiating and bargaining','Discussing possibilities'),
 (44,'Discussing problems','Third conditional','Workplace mistakes','Talking about past mistakes'),
]
MODULES = [
 ('People & first weeks', '#0F766E'), ('Tasks, money & reports', '#B8892B'), ('Everyday communication', '#1F5F8B'),
 ('Products & processes', '#5B3A7A'), ('Marketing & leadership', '#A4472F'), ('Teams & events', '#4C6B2F'),
 ('Reporting & checking', '#1B3A57'), ('Getting the job', '#0F766E'), ('Careers & networking', '#B8892B'),
 ('Presenting', '#1F5F8B'), ('Negotiating & solving problems', '#A4472F'),
]
assert len(U) == 44 and len(MODULES) * 4 == 44

def card(u):
    n, title, lang, vocab, skill = u
    st = STATUS.get(n)
    focus = lang or 'Vocabulary unit'
    sub = vocab if lang else 'Words and phrases for the workplace'
    tags = ''
    if lang: tags += '<span class="tag t-g">Language</span>'
    tags += '<span class="tag t-v">Vocabulary</span>'
    if skill: tags += '<span class="tag t-s">Skill</span>'
    if st == 'draft': tags += '<span class="tag t-d">Draft</span>'
    inner = ('<div class="c-top"><span class="c-num">%02d</span>%s</div><div class="c-title">%s</div>'
             '<div class="c-focus">%s</div><div class="c-sub">%s</div><div class="c-tags">%s</div>') % (
             n, '' if st else '<span class="c-lock">Soon</span>', title, focus, sub, tags)
    if st:
        return '<a class="card ready" href="%s/index.html">%s</a>' % (FOLDER[n], inner)
    return '<div class="card soon" aria-disabled="true">%s</div>' % inner

mods = ''
for i, (name, col) in enumerate(MODULES):
    units = U[i*4:(i+1)*4]
    ready = sum(1 for u in units if STATUS.get(u[0]))
    mods += ('<section class="mod" style="--mc:%s"><div class="mod-hd"><span class="mod-n">Module %d</span><h2>%s</h2>'
             '<span class="mod-c">Units %d–%d%s</span></div><div class="grid">%s</div></section>\n') % (
             col, i + 1, name, units[0][0], units[-1][0], (' · %d ready' % ready) if ready else '', ''.join(card(u) for u in units))

ready_total = sum(1 for v in STATUS.values() if v)
html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Business English · Level 2</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=DM+Sans:wght@400;500;700&display=swap" rel="stylesheet">
<style>
:root{--ink:#0F2438;--teal:#0F766E;--brass:#B8892B;--paper:#FBF9F4;--line:#D8D2C4;--text:#1B2733;--muted:#586573;}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'DM Sans','Segoe UI',system-ui,sans-serif;background:var(--paper);color:var(--text);font-size:15px;line-height:1.55;zoom:1.2}
.hero{background:radial-gradient(900px 420px at 88% -20%,rgba(15,118,110,.55),transparent 60%),radial-gradient(700px 360px at -10% 120%,rgba(184,137,43,.3),transparent 60%),linear-gradient(160deg,#0B1B2B,#11304B);color:#fff;padding:54px 48px 40px}
.hero-in{max-width:1180px;margin:0 auto}
.eyebrow{letter-spacing:.34em;text-transform:uppercase;color:#E3C477;font-size:12px;margin-bottom:14px}
h1{font-family:'DM Serif Display',Georgia,serif;font-weight:400;font-size:52px;line-height:1.08;margin-bottom:10px}
.hero p{color:rgba(255,255,255,.85);font-size:16px;max-width:640px}
.rule{width:84px;height:3px;background:var(--brass);margin:0 0 20px;border-radius:3px}
.stats{display:flex;gap:34px;margin-top:26px;flex-wrap:wrap}
.stat b{display:block;font-family:'DM Serif Display',Georgia,serif;font-weight:400;font-size:30px;color:#E3C477;line-height:1}
.stat span{font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:rgba(255,255,255,.7)}
.bar{height:6px;background:rgba(255,255,255,.18);border-radius:6px;margin-top:22px;max-width:520px;overflow:hidden}
.bar i{display:block;height:100%;width:__PCT__%;background:linear-gradient(90deg,var(--brass),#E3C477)}
main{max-width:1180px;margin:0 auto;padding:34px 48px 70px}
.mod{margin-bottom:34px}
.mod-hd{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;border-bottom:2px solid var(--mc);padding-bottom:8px;margin-bottom:16px}
.mod-n{font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--mc);font-weight:700}
.mod h2{font-family:'DM Serif Display',Georgia,serif;font-weight:400;font-size:26px;color:var(--ink)}
.mod-c{margin-left:auto;color:var(--muted);font-size:13px}
.grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px}
.card{display:flex;flex-direction:column;gap:6px;background:#fff;border:1px solid var(--line);border-top:5px solid var(--mc);border-radius:14px;padding:16px 18px;text-decoration:none;color:inherit;transition:transform .15s,box-shadow .15s}
.card.ready:hover{transform:translateY(-3px);box-shadow:0 12px 26px rgba(15,36,56,.14)}
.card.soon{opacity:.6}
.c-top{display:flex;align-items:center;justify-content:space-between}
.c-num{font-family:'DM Serif Display',Georgia,serif;font-size:30px;color:var(--mc);line-height:1}
.c-lock{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);border:1px solid var(--line);border-radius:999px;padding:2px 10px}
.c-title{font-weight:700;font-size:16px;color:var(--ink);line-height:1.3}
.c-focus{font-size:13.5px;color:var(--text)}
.c-sub{font-size:12.5px;color:var(--muted)}
.c-tags{display:flex;flex-wrap:wrap;gap:6px;margin-top:auto;padding-top:8px}
.tag{font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;border-radius:999px;padding:2px 9px;font-weight:700}
.t-g{background:#EDE5F4;color:#5B3A7A}.t-v{background:#E2F0EE;color:#0F766E}.t-s{background:#F6EBD0;color:#7A5A12}.t-d{background:#FFF1D6;color:#A8700F;border:1px solid #E4C47C}
footer{max-width:1180px;margin:0 auto;padding:0 48px 40px;color:var(--muted);font-size:13px}
@media(max-width:1000px){.grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(max-width:560px){.grid{grid-template-columns:1fr}.hero{padding:40px 22px 30px}main{padding:26px 22px 60px}h1{font-size:38px}}
</style>
</head>
<body>
<header class="hero"><div class="hero-in">
  <div class="eyebrow">Conversational English with teacher Nanda</div>
  <div class="rule"></div>
  <h1>Business English<br>Level 2</h1>
  <p>Forty-four interactive units for the workplace: meeting people, writing reports, presenting, interviewing and negotiating.</p>
  <div class="stats"><div class="stat"><b>__READY__</b><span>Units ready to open</span></div><div class="stat"><b>44</b><span>Units in the course</span></div><div class="stat"><b>11</b><span>Modules</span></div></div>
  <div class="bar"><i></i></div>
</div></header>
<main>
__MODS__</main>
<footer>Each unit has a lesson and a homework section. Open a unit and use the 📝 Notes button during class.</footer>
</body>
</html>
'''
html = html.replace('__PCT__', '%.1f' % (ready_total / 44.0 * 100)).replace('__READY__', str(ready_total)).replace('__MODS__', mods)
open(OUT, 'w', encoding='utf-8').write(html)
print('home built:', os.path.abspath(OUT), len(html), 'bytes;', ready_total, 'unit(s) open')
