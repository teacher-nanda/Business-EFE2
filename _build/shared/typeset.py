# -*- coding: utf-8 -*-
"""Typesetting rules for every lesson (teacher's standing rules):
   1. line spacing 1.5 everywhere
   2. when two sentences follow each other in a text block, each sentence goes on its own line
"""
import re

RULE_CSS = '''
/* ---- typesetting rule: line-height 1.5 everywhere ---- */
body, p, li, .instruction, .ex-row, .ccq-list li, .scene p, .scene .say, .gram-note, .gram-mistake, .gram-box p, .glossary-box p,
.akey-box, .akey-box p, .article-box p, .form-row, .dc-line, .dc-goal, .vc-def, .rc-a, .rc-q, .bd-tip, .ccq-answer, .big-sent .say-btn,
.classify-chip, .circ-opt, .match-item, .inst-light, .discuss-list, .check-item, .pc-v { line-height:1.5 !important; }
.sent-br { display:block; }
'''

_ABBR = r'(?<!\d)(?<!e\.g)(?<!i\.e)(?<!Mr)(?<!Mrs)(?<!Ms)(?<!Dr)(?<!vs)(?<!etc)(?<!U\.S)(?<!St)'
SPLIT = re.compile(_ABBR + r'([.?!](?:&rdquo;|&rsquo;|”|’|\)|")?)\s+(?=(?:&ldquo;|&lsquo;|“|\(|<b>|<i>)?[A-Z])')

def split_sentences(inner):
    return SPLIT.sub(r'\1<br>', inner)

_ART = re.compile(r'<div class="article-box">.*?</div>', re.S)
_P = re.compile(r'<p((?:\s[^>]*)?)>(.*?)</p>', re.S)
_OTH = re.compile(r'<(div|span)((?:\s[^>]*)?)>(.*?)</\1>', re.S)
_CLS = re.compile(r'class="([^"]*)"')
_ON = ('instruction', 'gram-note', 'gram-mistake', 'bd-tip', 'ccq-answer', 'rc-a', 'dc-goal', 'dc-line', 'say', 'sc-note')

def _p(m):
    attrs, inner = m.group(1), m.group(2)
    if '<input' in inner or '<button' in inner:
        return m.group(0)
    return '<p%s>%s</p>' % (attrs, split_sentences(inner))

def _oth(m):
    tag, attrs, inner = m.group(1), m.group(2), m.group(3)
    if '<div' in inner or '<input' in inner or '<button' in inner:
        return m.group(0)
    cm = _CLS.search(attrs)
    cls = cm.group(1).split() if cm else []
    if any(c in cls for c in _ON):
        return '<%s%s>%s</%s>' % (tag, attrs, split_sentences(inner), tag)
    return m.group(0)

def fix_html(html):
    masks = []
    def keep(m):
        masks.append(m.group(0)); return '@@ART%d@@' % (len(masks) - 1)
    h = _ART.sub(keep, html)
    h = _P.sub(_p, h)
    h = _OTH.sub(_oth, h)
    for i, a in enumerate(masks):
        h = h.replace('@@ART%d@@' % i, a)
    return h

def apply(S):
    return [(sid, label, fix_html(html)) for sid, label, html in S]
