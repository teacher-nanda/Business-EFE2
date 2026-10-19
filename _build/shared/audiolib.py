# -*- coding: utf-8 -*-
"""Audio helpers: real <audio>/clip players pointing at the 'Course Book Audio' folder (validated against audio_files.txt)."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
FILES = set(l.strip() for l in open(os.path.join(HERE, '..', 'audio_files.txt'), encoding='utf-8') if l.strip())
ROOT = '../EFE.B%20B1%20Level%202%20-%20Course%20Book%20Audio/'
USED = set()

def _src(unit, name):
    rel = '%s/%s.mp3' % (unit, name)
    if rel not in FILES:
        raise SystemExit('MISSING AUDIO FILE: ' + rel)
    USED.add(rel)
    return ROOT + rel

def single(unit, name, top=False):
    """One long track, normal audio player."""
    return '<div class="audio-box%s"><audio controls preload="none" src="%s"></audio></div>' % (' top' if top else '', _src(unit, name))

def clips(unit, base, n, eg=True, top=False, label='🎧 Listen'):
    """Per-item clips: Example, 1 ... n  (files unit/base__eg.mp3, unit/base_1.mp3 ...)."""
    b = []
    if eg:
        b.append('<button class="clip" data-src="%s" onclick="playClip(this)">Example</button>' % _src(unit, base + '__eg'))
    for i in range(1, n + 1):
        b.append('<button class="clip" data-src="%s" onclick="playClip(this)">%d</button>' % (_src(unit, '%s_%d' % (base, i)), i))
    return '<div class="audio-box clips-box%s"><span class="clips-label">%s</span>%s</div>' % (' top' if top else '', label, ''.join(b))

def word(unit, name, label=None):
    """A small speaker button for one word / phrase."""
    return '<button class="clip word" data-src="%s" onclick="playClip(this)" aria-label="listen">🔊%s</button>' % (_src(unit, name), (' ' + label) if label else '')

# ---------------- Practice Book audio (supporting audio: listen and check) ----------------
PBFILES = set(l.strip() for l in open(os.path.join(HERE, '..', 'pb_audio_files.txt'), encoding='utf-8') if l.strip())
PB_ROOT = '../EFE.B%20B1%20Level%202%20-%20Practice%20Book%20Audio/'

def _pbsrc(unit, name):
    rel = '%s/%s.mp3' % (unit, name)
    if rel not in PBFILES:
        raise SystemExit('MISSING PB AUDIO FILE: ' + rel)
    return PB_ROOT + rel

def pb_clips(unit, ex, n, eg=True, label='🎧 Listen and check'):
    """Practice Book supporting audio: Example, 1 ... n  (files unit/unit_ex__eg.mp3, unit/unit_ex_1.mp3 ...)."""
    base = '%s_%s' % (unit, ex)
    b = []
    if eg:
        b.append('<button class="clip" data-src="%s" onclick="playClip(this)">Example</button>' % _pbsrc(unit, base + '__eg'))
    for i in range(1, n + 1):
        b.append('<button class="clip" data-src="%s" onclick="playClip(this)">%d</button>' % (_pbsrc(unit, '%s_%d' % (base, i)), i))
    return '<div class="audio-box clips-box"><span class="clips-label">%s</span>%s</div>' % (label, ''.join(b))

def pb_single(unit, ex, label='🎧 Listen'):
    return '<div class="audio-box"><audio controls preload="none" src="%s"></audio></div>' % _pbsrc(unit, '%s_%s' % (unit, ex))
