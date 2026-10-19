# -*- coding: utf-8 -*-
"""Shared helpers for the Business-EFE2 lesson builds (slides are (id, label, html) tuples)."""
S = []

def slide(sid, label, html):
    S.append((sid, label, html))

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'shared'))
import audiolib as AL
_TRACKS = {'cb1.1': ('single', '1', '1_1'), 'cb1.2': ('clips', '1', '1_2', 5), 'cb1.3': ('clips', '1', '1_3', 5),
           'cb1.4': ('single', '1', '1_4'), 'cb1.5': ('single', '1', '1_5'), 'cb1.7': ('clips', '1', '1_7', 4), 'cb1.8': ('clips', '1', '1_8', 4),
           'pb1.1': ('pb', '1', '1', 9), 'pb1.2': ('pb', '1', '2', 6), 'pb1.4': ('pb', '1', '4', 12), 'pb1.5': ('pb', '1', '5', 10)}
def audio(track, top=False):
    t = _TRACKS.get(track)
    if t and t[0] == 'pb':
        return AL.pb_clips(t[1], t[2], t[3])
    if t:
        return AL.single(t[1], t[2], top) if t[0] == 'single' else AL.clips(t[1], t[2], t[3], True, top)
    return ''   # no audio file available -> no player at all

def green(txt):
    return '<span class="hl-ok">%s</span>' % txt

def ccq(q, a):
    return ('<li>%s <button class="ccq-reveal-btn" onclick="this.nextElementSibling.classList.toggle(\'show\')">Show answer</button>'
            '<span class="ccq-answer">%s</span></li>') % (q, a)

def reveal_card(q, a):
    return ('<button class="reveal-card" onclick="this.classList.toggle(\'open\')"><span class="rc-q">%s</span>'
            '<span class="rc-hint">Think first, then click</span><span class="rc-a">%s</span></button>') % (q, a)

def ph(icon, text):
    return '<div class="img-placeholder"><span class="ip-icon">%s</span>%s</div>' % (icon, text)

def banner(kind):
    labels = {'bridge': '🌉 Bridge', 'leadin': '🎯 Warm-Up', 'vocab': '📚 Vocabulary', 'reading': '📖 Reading',
              'listening': '🎧 Listening', 'speaking': '💬 Speaking', 'grammar': '📐 Grammar',
              'pron': '🔊 Pronunciation', 'review': '⭐ Lesson Review', 'hw': '📝 Homework'}
    return '<div class="banner banner-%s">%s</div>' % (kind, labels[kind])

def ex_given(inner):
    return '<div class="ex-row ex-given">%s</div>' % inner

def example_badge():
    return '<span class="example-badge">✓</span>'

def tf_row(n, text, ans, group):
    b = ''.join('<button class="circ-opt" data-group="%s" data-correct="%s" onclick="circPick(this)">%s</button>' % (group, ans, o) for o in ('True', 'False', 'Not given'))
    return '<div class="ex-row"><span class="circ-num">%d</span>%s<br><span style="margin-left:34px;display:inline-block;">%s</span></div>' % (n, text, b)

def tf_example(text, ans):
    b = ''.join('<span class="circ-opt %s">%s</span>' % ('is-example' if o == ans else 'struck', o) for o in ('True', 'False', 'Not given'))
    return ex_given('%s%s<br><span style="margin-left:34px;display:inline-block;">%s</span>' % (example_badge(), text, b))

def figs(cols, shake=False):
    """Simple two-tone delegate pictograms."""
    n = len(cols)
    W = 60 * n + 30
    parts = []
    for i, c in enumerate(cols):
        cx = 45 + i * 60
        parts.append('<circle cx="%d" cy="22" r="11" fill="%s"/>' % (cx, c))
        parts.append('<path d="M%d 70 Q%d 38 %d 38 Q%d 38 %d 70 Z" fill="%s"/>' % (cx - 16, cx - 16, cx, cx + 16, cx + 16, c))
        parts.append('<rect x="%d" y="68" width="9" height="26" rx="3" fill="%s"/><rect x="%d" y="68" width="9" height="26" rx="3" fill="%s"/>' % (cx - 12, c, cx + 3, c))
    if shake and n == 2:
        parts.append('<line x1="58" y1="56" x2="92" y2="56" stroke="#B8892B" stroke-width="5" stroke-linecap="round"/>')
    return '<svg viewBox="0 0 %d 100" role="img" aria-hidden="true">%s</svg>' % (W, ''.join(parts))

TEAL, BRASS, INK, PLUM = '#0F766E', '#B8892B', '#1B3A57', '#5B3A7A'

# ---- article texts (word for word from the book pages) ----
CB_ARTICLE = ('<div class="article-box">'
  '<span class="kicker">Career Ladder</span>'
  '<h3>Making connections</h3>'
  '<p class="deck">How to network better if you\'re shy</p>'
  '<p>Networking doesn\'t necessarily mean talking to hundreds of people at a conference. A few good connections are much better than meeting lots of people who you will never hear from again. Start by chatting to ex-colleagues or old friends. Ask what they are doing now and share your experiences.</p>'
  '<p>One common habit of shy people is to constantly apologize for everything. Apologizing all of the time looks unprofessional and shows a lack of confidence in yourself. Instead of saying sorry, remember to smile, maintain eye contact, ask questions, and, of course, exchange business cards.</p>'
  '</div>')

PB_ARTICLE = ('<div class="article-box">'
  '<span class="kicker">Essential Skills</span>'
  '<h3>Meeting and greeting</h3>'
  '<p class="deck">Meeting new people isn\'t always easy, but it\'s an essential skill for a young business professional.</p>'
  '<p>Whether you\'re looking for a new job, hope to grow your business, or just want to find new clients, you need to talk to the right people. It doesn\'t always lead to success, but it can provide a great first step. So, what\'s the best way to start talking?</p>'
  '<p>Talk about your recent experience: &ldquo;I\'m working with some great software engineers at the moment&rdquo; is a great way to start. You can tell them about your personal life and interests: &ldquo;I play golf with my friend on the weekend&rdquo; might be a good starter. But you shouldn\'t talk about things that are too personal. If you ask someone how much money they earn, they might be offended! Another good idea is to talk about one of your clients: &ldquo;I often work with ElectroSan, an exciting new Japanese start-up.&rdquo; You will soon find that the person you\'re talking to wants to know more&hellip;</p>'
  '</div>')

def article_toggle(tid, article):
    return ('<div class="btn-row" style="justify-content:flex-start;margin-top:0;"><button class="btn-akey" onclick="toggleSuggested(\'%s\')">📖 Show / hide the article</button></div>'
            '<div class="akey-box" id="%s" style="background:#fff;padding:0;border:0;">%s</div>') % (tid, tid, article)
