# -*- coding: utf-8 -*-
"""Exercise builders shared by Units 2+ (every item comes from the Course Book / Practice Book)."""
import itertools, math
from lib import (slide, green, ccq, reveal_card, ph, banner, ex_given, example_badge, tf_row, tf_example, figs,
                 TEAL, BRASS, INK, PLUM, article, article_toggle)

def alts(sentence, pairs):
    out = set()
    present = [p for p in pairs if p[0] in sentence or p[1] in sentence]
    for combo in itertools.product([0, 1], repeat=len(present)):
        s = sentence
        for use, (c, e) in zip(combo, present):
            s = s.replace(e, c) if use == 0 else s.replace(c, e)
        out.add(s)
    out.discard(sentence)
    return '|'.join(sorted(out))

CONTR = [("I'm", 'I am'), ("don't", 'do not'), ("doesn't", 'does not'), ("didn't", 'did not'), ("wasn't", 'was not'), ("weren't", 'were not'),
         ("haven't", 'have not'), ("hasn't", 'has not'), ("it's", 'it is'), ("I'd", 'I would'), ("we've", 'we have'), ("I've", 'I have'),
         ("he's", 'he is'), ("she's", 'she is'), ("they're", 'they are'), ("we're", 'we are'), ("you're", 'you are'), ("isn't", 'is not'),
         ("aren't", 'are not'), ("can't", 'cannot'), ("won't", 'will not'), ("I'll", 'I will'), ("couldn't", 'could not'), ("shouldn't", 'should not'),
         ("wouldn't", 'would not'), ("mustn't", 'must not'), ("that's", 'that is'), ("there's", 'there is'), ("what's", 'what is')]

def esc(s): return s.replace('"', '&quot;')

# ---------- row builders ----------
def pick_row(n, opts, correct, group, num=True):
    """Choose one of several options, each on its own line (mark the correct sentence / best reply)."""
    b = ''.join('<button class="circ-opt block" data-group="%s" data-correct="%s" onclick="circPick(this)">%s</button>' % (group, esc(correct), o) for o in opts)
    return '<div class="ex-row"><span class="circ-num">%d</span><span class="pick-wrap">%s</span></div>' % (n, b)

def pick_example(opts, correct):
    b = ''.join('<span class="circ-opt block %s">%s</span>' % ('is-example' if o == correct else 'struck', o) for o in opts)
    return ex_given('%s<span class="pick-wrap">%s</span>' % (example_badge(), b))

def mc_row(n, q, choices, ans, group):
    b = ''.join('<button class="circ-opt" data-group="%s" data-correct="%s" onclick="circPick(this)">%s</button>' % (group, esc(ans), c) for c in choices)
    return '<div class="ex-row"><span class="circ-num">%d</span>%s<br><span style="margin-left:34px;display:inline-block;">%s</span></div>' % (n, q, b)

def co_row(n, pre, choices, correct, post, group, say=False):
    """Cross out the incorrect words: sentence with 2-3 inline options."""
    bs = ' <span class="circ-sep">/</span> '.join('<button class="circ-opt" data-group="%s" data-correct="%s" onclick="circPick(this)">%s</button>' % (group, esc(correct), c) for c in choices)
    sp = '' if (not post or post[:1] in '?.,!') else ' '
    pre = (pre + ' ') if pre else ''
    sb = '<br><button class="say-btn" style="margin-left:34px;margin-top:6px;" onclick="this.classList.toggle(\'done\')">🗣 I said it</button>' if say else ''
    return '<div class="ex-row"><span class="circ-num">%d</span>%s%s%s%s%s</div>' % (n, pre, bs, sp, post, sb)

def co_example(pre, choices, correct, post):
    bs = ' <span class="circ-sep">/</span> '.join('<span class="circ-opt %s">%s</span>' % ('is-example' if c == correct else 'struck', c) for c in choices)
    sp = '' if (not post or post[:1] in '?.,!') else ' '
    return ex_given('%s%s%s%s%s' % (example_badge(), (pre + ' ') if pre else '', bs, sp, post))

def typed_row(n, prompt, ans, cue='', pairs=CONTR, extra_alt='', before=False, wide=True):
    """Typed answer. prompt = text before the input; cue shown in brackets after it."""
    al = alts(ans, pairs)
    if extra_alt: al = (al + '|' + extra_alt) if al else extra_alt
    inp = '<input class="ans-input%s" data-ans="%s" data-alt="%s" aria-label="answer %d">' % (' wide' if wide else '', esc(ans), esc(al), n)
    cue = (' <span class="cue-verb">(%s)</span>' % cue) if cue else ''
    return '<div class="ex-row"><span class="circ-num">%d</span>%s%s%s</div>' % (n, (prompt + ' ') if prompt else '', inp, cue)

def gap_row(n, pre, ans, verb, post, pairs=CONTR, extra_alt=''):
    """A sentence with a typed gap in the middle: pre [____] (verb) post."""
    al = alts(ans, pairs)
    if extra_alt: al = (al + '|' + extra_alt) if al else extra_alt
    inp = '<input class="ans-input" style="width:9.5em;" data-ans="%s" data-alt="%s" aria-label="answer %d">' % (esc(ans), esc(al), n)
    v = (' <span class="cue-verb">(%s)</span>' % verb) if verb else ''
    return '<div class="ex-row"><span class="circ-num">%d</span>%s %s%s %s</div>' % (n, pre, inp, v, post)

def gap_example(pre, ans, verb, post):
    return ex_given('%s%s <span class="ans-line" style="display:inline">%s</span>%s %s' % (example_badge(), pre, ans, (' <span class="cue-verb">(%s)</span>' % verb) if verb else '', post))

def rewrite_example(wrong, right, icon=''):
    ic = ('<span class="cue">%s</span>' % icon) if icon else ''
    return ex_given('%s%s<span>%s</span><span class="ans-line">%s</span>' % (example_badge(), ic, wrong, right))

def wb_blank(ans):
    return '<span class="wb-blank" data-ans="%s" onclick="wbPlace(this)">______</span>' % esc(ans)
def wb_row(n, pre, ans, post):
    return '<div class="ex-row"><span class="circ-num">%d</span>%s %s %s</div>' % (n, pre, wb_blank(ans), post)
def wb_bank(words, example_word=None):
    tiles = ''
    for w in words:
        if w == example_word:
            tiles += '<button class="wb-tile example-used" data-val="%s" disabled>%s</button>' % (esc(w), w)
        else:
            tiles += '<button class="wb-tile" data-val="%s" onclick="wbPick(this)">%s</button>' % (esc(w), w)
    return '<div class="wb-bank book-style">%s</div>' % tiles

def mrow(side, pair, text, num=None, example=False):
    if example:
        return '<div class="match-item example-pair">%s%s</div>' % ((example_badge() if side == 'left' else ''), text)
    if side == 'left':
        return '<div class="match-item" data-side="left" data-pair="%s" onclick="matchPick(this)"><span class="circ-num">%d</span>%s</div>' % (pair, num, text)
    return '<div class="match-item" data-side="right" data-pair="%s" onclick="matchPick(this)">%s</div>' % (pair, text)

# ---------- slide builders ----------
def _two_col(rows, gid):
    k = math.ceil(len(rows) / 2.0)
    return '<div class="fixed-two-col" id="%s"><div>%s</div><div>%s</div></div>' % (gid, ''.join(rows[:k]), ''.join(rows[k:]))

def exercise(sid, label, kind, h2, instr, rows, mode='circ', example='', pre='', aud='', gid=None, inst_class='instruction'):
    gid = gid or sid
    chk, rst = {'circ': ('checkCircSlide', 'resetCircSlide'), 'typed': ('checkSlide', 'resetSlide'), 'wb': ('checkWbSlide', 'resetWbSlide')}[mode]
    html = '''<div class="slide" id="%s">
  %s
  <div class="slide-main"><div class="content">
    <h2>%s</h2>
    <p class="%s">%s</p>
    %s
    %s
    %s
    <div class="btn-row">
      <button class="btn-check" onclick="%s('%s')">Check Answers</button>
      <button class="btn-reset" onclick="%s('%s')">Reset</button>
    </div>
    %s
  </div></div>
</div>''' % (sid, banner(kind), h2, inst_class, instr, pre, example, _two_col(rows, gid), chk, gid, rst, gid, aud)
    slide(sid, label, html)

def match_exercise(sid, label, kind, h2, instr, left, right, aud=''):
    html = '''<div class="slide" id="%s">
  %s
  <div class="slide-main"><div class="content">
    <h2>%s</h2>
    <p class="instruction">%s</p>
    <div class="match-wrap compact" id="%s-match">
      <div>%s</div>
      <div>%s</div>
    </div>
    <div class="btn-row">
      <button class="btn-check" onclick="checkMatchSlide('%s-match')">Check Answers</button>
      <button class="btn-reset" onclick="resetMatchSlide('%s-match')">Reset</button>
    </div>
    %s
  </div></div>
</div>''' % (sid, banner(kind), h2, instr, sid, ''.join(left), ''.join(right), sid, sid, aud)
    slide(sid, label, html)

def cover(unit_no, title, cards):
    c = ''.join('<div class="cv-card %s" aria-hidden="true">%s</div>' % (k, t) for k, t in zip('abcd', cards))
    slide('s1', 'Cover', '''<div class="slide active" id="s1">
  %s
  <div class="title-inner">
    <div class="title-label">Conversational English</div>
    <div class="title-sub">with teacher Nanda</div>
    <div class="title-main">%s</div>
    <a href="../index.html" title="All units" style="position:absolute;bottom:70px;left:32px;font-size:1.7rem;line-height:1;text-decoration:none;z-index:5;">🏠</a>
    <div style="position:absolute;bottom:70px;right:32px;z-index:5;">
      <button onclick="goToId('hw-cover')" style="cursor:pointer;font-family:inherit;font-size:.95rem;">📝 Homework</button>
    </div>
  </div>
</div>''' % (c, title))

def hw_cover(title):
    slide('hw-cover', 'Homework Cover', '''<div class="slide" id="hw-cover">
  <div class="title-inner">
    <div class="hw-badge">📝 Homework</div>
    <div class="title-main" style="margin-top:22px;">%s</div>
  </div>
</div>''' % title)

def ck(label, icon):
    return '<button class="check-item" onclick="ckToggle(this)"><span class="ck"></span><span>%s</span><span class="ck-ic">%s</span></button>' % (label, icon)

def review(items, h2, closing, extra_right=''):
    slide('s-review', 'Lesson Review', '''<div class="slide" id="s-review">
  %s
  <div class="slide-main"><div class="content">
    <h2>%s</h2>
    <p class="instruction">Click each one when you feel ready to use it.</p>
    <div class="check-list" id="ck-list">%s</div>
    <div class="win-banner" id="ck-win">You are ready for the next unit.</div>
    %s
    <p class="instruction" style="margin-top:22px;">%s</p>
  </div></div>
</div>''' % (banner('review'), h2, ''.join(ck(l, i) for l, i in items), extra_right, closing))

def freer(sid, label, h2, instr, deck_name='Scenario card'):
    slide(sid, label, '''<div class="slide" id="%s">
  %s
  <div class="slide-main"><div class="content">
    <h2>%s</h2>
    <p class="instruction">%s</p>
    <div class="deal-wrap">
      <div class="deal-card" id="deal-card"><div class="dc-head">%s</div>
        <div class="dc-body"><p class="dc-setting">Ready?</p><p class="dc-line">Press <b>Deal a card</b> to see the situation and what you need to do.</p></div></div>
      <div class="btn-row" style="margin-top:0;align-items:center;">
        <button class="btn-deal" onclick="dealNext()">Deal a card</button>
        <button class="btn-reset" onclick="dealReset()">Shuffle</button>
        <span class="deal-count" id="deal-count">Cards played: 0</span>
      </div>
    </div>
  </div></div>
</div>''' % (sid, banner('speaking'), h2, instr, deck_name))

def content(sid, label, kind, h2, body, instr=''):
    slide(sid, label, '''<div class="slide" id="%s">
  %s
  <div class="slide-main"><div class="content">
    <h2>%s</h2>
    %s
    %s
  </div></div>
</div>''' % (sid, banner(kind), h2, ('<p class="instruction">%s</p>' % instr) if instr else '', body))

def ccqs(*pairs):
    return '<div class="ccq-box"><p class="ccq-label">💭 Check your understanding</p><ul class="ccq-list">%s</ul></div>' % ''.join(ccq(q, a) for q, a in pairs)

def sort_slide(sid, label, kind, h2, instr, items, cols, pre='', post='', aud='', ncols=None):
    """Sort chips into categories. items=[(text, target)], cols=[(target, heading)]."""
    chips = ''.join('<button class="classify-chip" data-ans="%s" onclick="classifyPick(this)">%s</button>' % (esc(t), x) for x, t in items)
    cs = ''.join('<div class="classify-col" data-target="%s" onclick="classifyTarget(this)"><h4>%s</h4></div>' % (esc(t), h) for t, h in cols)
    n = ncols or len(cols)
    slide(sid, label, '''<div class="slide" id="%s">
  %s
  <div class="slide-main"><div class="content">
    <h2>%s</h2>
    %s
    <p class="instruction" style="margin-bottom:12px;">%s</p>
    <div id="%s-bank" class="classify-bank" style="margin-bottom:16px;">%s</div>
    <div id="%s-cols" style="display:grid;grid-template-columns:repeat(%d,minmax(0,1fr));gap:16px;">%s</div>
    <div class="btn-row">
      <button class="btn-check" onclick="checkClassifySlide('%s')">Check Answers</button>
      <button class="btn-reset" onclick="resetClassifySlide('%s')">Reset</button>
    </div>
    %s
    %s
  </div></div>
</div>''' % (sid, banner(kind), h2, pre, instr, sid, chips, sid, n, cs, sid, sid, post, aud))

def bubble(text, who='a'):
    return '<div class="say%s">%s</div>' % (' b' if who == 'b' else '', text)

def card3(title, rule, lines):
    ls = ''.join('<div class="say">%s</div>' % l for l in lines)
    return '<div class="scene"><div class="rc-q" style="font-family:\'DM Serif Display\',Georgia,serif;font-size:1.35rem;color:var(--ink);">%s</div>%s<p style="margin:2px 0 0;color:var(--muted);font-size:1rem;">%s</p></div>' % (title, ls, rule)

def puzzle(parts):
    """Sentence-form puzzle: parts=[(label, text, cls)]  cls in '', 'a','b','c'"""
    h = ''.join('<div class="pz %s"><span class="pz-k">%s</span><span class="pz-v">%s</span></div>' % (c, k, v) for k, v, c in parts)
    return '<div class="pz-row">%s</div>' % h

def vcards(items, cols=3):
    """items=[(icon, name_html, definition_html, example_html, clip_html)]"""
    h = ''
    for ic, name, d, ex, cl in items:
        h += ('<div class="vcard"><div class="vc-top"><span class="vc-ic">%s</span>%s</div><div class="vc-name">%s</div>%s%s</div>'
              % (ic, cl, name, ('<div class="vc-def">%s</div>' % d) if d else '', ('<div class="vc-ex">%s</div>' % ex) if ex else ''))
    return '<div class="vgrid%s">%s</div>' % (' two' if cols == 2 else '', h)

def pic(text):
    return '<div class="pic-ph"><span>🖼️</span><span>%s</span></div>' % text

def order_row(n, words, ans, extra_alt=''):
    """Rewrite the sentence putting the words in the correct order (typed)."""
    ch = ''.join('<span class="scr-w">%s</span>' % w for w in words)
    al = alts(ans, CONTR)
    if extra_alt: al = (al + '|' + extra_alt) if al else extra_alt
    return ('<div class="ex-row"><span class="circ-num">%d</span><span class="scr">%s</span><br><input class="ans-input ord" data-ans="%s" data-alt="%s" aria-label="answer %d"></div>'
            % (n, ch, esc(ans), esc(al), n))

def order_example(words, ans):
    ch = ''.join('<span class="scr-w">%s</span>' % w for w in words)
    return ex_given('%s<span class="scr">%s</span><span class="ans-line">%s</span>' % (example_badge(), ch, ans))

def say_line(html):
    return '<div class="stress-line"><span>%s</span><button class="say-btn" onclick="this.classList.toggle(\'done\')">I said it</button></div>' % html
St = lambda t: '<span class="st">%s</span>' % t
Sy = lambda t: '<span class="st sy">%s</span>' % t


def speak(sid, label, h2, instr, items, closing=''):
    """Speaking break slide: numbered prompts, each with an 'I said it' button."""
    rows = ''.join('<div class="ex-row"><span class="circ-num">%d</span>%s<br><button class="say-btn" style="margin-left:34px;margin-top:6px;" onclick="this.classList.toggle(\'done\')">🗣 I said it</button></div>' % (i + 1, t) for i, t in enumerate(items))
    content(sid, label, 'speaking', h2, rows + closing, instr)
