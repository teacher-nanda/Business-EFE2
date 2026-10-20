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
/* ---- notes box: white, larger text ---- */
#notesPanel { box-shadow:0 8px 28px rgba(0,0,0,.18); border:1px solid #D9D4C5; background:#fff; }
#notesToolbar { background:#EFEBDD; }
#notesToolbar button { background:#fff; color:#1C2B3A; border:1px solid #D9D4C5; }
#notesToolbar button:hover { background:#F6EBD0; }
#notesDragHandle { color:#1C2B3A; }
#notesTA { background:#fff; color:#1C2B3A; font-size:1.2rem; backdrop-filter:none; }
#notesTA:empty::before { color:rgba(28,43,58,.45); }
.ccq-answer.ex-sent.show { display:block; margin:8px 0 0 34px; }
.chat{display:flex;flex-direction:column;gap:12px;margin:6px 0 4px;max-height:calc(100vh - 440px);min-height:240px;overflow-y:auto;padding:2px 6px 2px 0;scroll-behavior:smooth;}
.chat .b{display:none;max-width:76%;padding:12px 16px;border-radius:16px;font-size:1.08rem;line-height:1.5;color:#1C2B3A;}
.chat .b.show{display:block;}
.chat .b.them{align-self:flex-start;background:#fff;border:1.5px solid #D9D4C5;border-bottom-left-radius:4px;}
.chat .b.you{align-self:flex-end;background:#E3F0EC;border:1.5px solid #9CC7BB;border-bottom-right-radius:4px;}
.chat .who{display:block;font-size:.72rem;letter-spacing:.12em;font-weight:700;text-transform:uppercase;color:#6B7280;margin-bottom:2px;}
.chat .you-task{font-weight:600;}
.chat .ccq-answer.ex-sent.show{margin:8px 0 0 0;}
.sum-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;margin:6px 0 16px;align-items:stretch;}
.sum-card{background:#fff;border:1.5px solid #D9D4C5;border-top:5px solid #B8892B;border-radius:14px;padding:14px 18px 8px;}
.sum-card:nth-child(2){border-top-color:#0F766E;}
.sum-card:nth-child(3){border-top-color:#1B3A57;}
.sum-ic{font-size:1.6rem;}
.sum-card h3{margin:2px 0 8px;font-size:1.15rem;color:#1B3A57;}
.sum-p{margin:0 0 8px;font-size:1rem;color:#1C2B3A;}
.sum-p b{color:#0B5D56;}
.sum-p mark,.sum-ex mark{background:#FFF0B3;color:#1C2B3A;padding:0 4px;border-radius:4px;font-weight:700;}
.sum-ex{margin:0 0 8px;padding:6px 10px;border-left:4px solid #B8892B;background:#FAF6EA;border-radius:0 8px 8px 0;font-style:italic;font-size:1rem;color:#1C2B3A;}
.sum-turn{background:#1B3A57;color:#fff;border-radius:12px;padding:12px 18px;font-size:1.05rem;}
.sum-turn-l{display:inline-block;background:#B8892B;color:#fff;font-weight:700;font-size:.75rem;letter-spacing:.12em;text-transform:uppercase;border-radius:6px;padding:2px 8px;margin-right:12px;}
.ai-steps{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:10px;margin:4px 0 10px;}
.ai-step{background:#fff;border:1.5px solid #D9D4C5;border-radius:12px;padding:8px 12px;display:flex;flex-direction:column;gap:2px;font-size:.92rem;line-height:1.4;color:#1C2B3A;position:relative;padding-left:48px;}
.ai-step b{color:#1B3A57;font-size:1.05rem;}
.ai-n{position:absolute;left:12px;top:10px;width:26px;height:26px;border-radius:50%;background:#0F766E;color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center;}
.ai-prompt-wrap{background:#1B3A57;border-radius:14px;padding:12px 16px 14px;}
.ai-prompt-head{display:flex;justify-content:space-between;align-items:center;color:#fff;font-weight:700;letter-spacing:.06em;text-transform:uppercase;font-size:.8rem;margin-bottom:8px;}
.ai-copy{margin:0 !important;padding:8px 18px !important;font-size:.95rem !important;}
.ai-prompt{margin:0;background:#fff;color:#1C2B3A;border-radius:10px;padding:12px 16px;font-family:inherit;font-size:.92rem;white-space:pre-wrap;line-height:1.5;max-height:calc(100vh - 590px);min-height:120px;overflow-y:auto;}
.classify-bank.grid{display:grid;gap:10px;}
.classify-bank.grid .classify-chip{border-radius:12px;padding:12px 16px;text-align:left;line-height:1.5;font-weight:500;font-size:1.05rem;border:1.5px solid #CFC8B4;background:#fff;color:#1C2B3A;}
.classify-bank.grid .classify-chip.selected{background:#1B3A57;color:#fff;border-color:#1B3A57;}
.classify-bank.grid .classify-chip.selected mark.vb{background:#FFE48A;color:#1C2B3A;}
mark.vb{background:#FFE48A;color:#1C2B3A;padding:0 5px;border-radius:5px;font-weight:700;}
.classify-col{padding:0 18px 14px !important;overflow:hidden;min-height:110px;}
.classify-col h4{font-weight:500 !important;margin:0 -18px 10px !important;padding:12px 18px;color:#fff !important;font-size:1.05rem;line-height:1.5;}
.classify-col h4 b{font-size:1.2rem;}
.classify-col.c-a{border-color:#0F766E !important;background:#F0F8F6 !important;}
.classify-col.c-a h4{background:#0F766E;}
.classify-col.c-b{border-color:#C2570C !important;background:#FFF4EA !important;}
.classify-col.c-b h4{background:#C2570C;}
.classify-col.c-c{border-color:#1B3A57 !important;background:#EEF2F7 !important;}
.classify-col.c-c h4{background:#1B3A57;}
.classify-col .placed{display:block !important;margin:6px 0 !important;padding:8px 12px !important;border-radius:10px !important;font-weight:500 !important;background:#fff !important;border:1px solid #CFC8B4 !important;color:#1C2B3A !important;}
.classify-col .placed.correct{background:#E3F5EA !important;border-color:#1A7A4A !important;}
.classify-col .placed.wrong{background:#FBEAE6 !important;border-color:#C4614A !important;}
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
