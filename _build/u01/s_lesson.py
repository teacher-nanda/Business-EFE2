# -*- coding: utf-8 -*-
# Unit 1 "Introductions" — lesson slides (cover -> review). Theme: the conference lobby.
import itertools
from lib import (slide, audio, green, ccq, reveal_card, ph, banner, ex_given, example_badge, tf_row, tf_example,
                 figs, TEAL, BRASS, INK, PLUM, CB_ARTICLE, article_toggle)

def alts(sentence, pairs):
    """All combinations of contracted / expanded forms, for typed answers. pairs = [(contracted, expanded), ...]."""
    out = set()
    present = [p for p in pairs if p[0] in sentence or p[1] in sentence]
    for combo in itertools.product([0, 1], repeat=len(present)):
        s = sentence
        for use, (c, e) in zip(combo, present):
            s = s.replace(e, c) if use == 0 else s.replace(c, e)
        out.add(s)
    out.discard(sentence)
    return '|'.join(sorted(out))

# ------------------------------------------------------------------ 1 COVER
slide('s1', 'Cover', '''<div class="slide active" id="s1">
  <div class="cv-card a" aria-hidden="true">You must be Eric from the UK.</div>
  <div class="cv-card b" aria-hidden="true">I'd like to introduce you to Faisal.</div>
  <div class="cv-card c" aria-hidden="true">Great to see you again!</div>
  <div class="cv-card d" aria-hidden="true">Pleased to meet you.</div>
  <div class="title-inner">
    <div class="title-label">Conversational English</div>
    <div class="title-sub">with teacher Nanda</div>
    <div class="title-main">Introductions</div>
    <a href="../index.html" title="All units" style="position:absolute;bottom:70px;left:32px;font-size:1.7rem;line-height:1;text-decoration:none;z-index:5;">🏠</a>
    <div style="position:absolute;bottom:70px;right:32px;z-index:5;">
      <button onclick="goToId('hw-cover')" style="cursor:pointer;font-family:inherit;font-size:.95rem;">📝 Homework</button>
    </div>
  </div>
</div>''')

# ------------------------------------------------------------------ 2 WARM-UP: DELEGATE BADGE
slide('s-lead', 'Warm-Up – Registration Desk', '''<div class="slide" id="s-lead">
  %s
  <div class="slide-main"><div class="content">
    <h2>Registration desk</h2>
    <p class="instruction">You've arrived at a business conference. Fill in your delegate badge, then introduce yourself to me.</p>
    <div class="lead-grid">
      <div class="bd-form">
        <label for="bd-name">First name</label><input id="bd-name" maxlength="16" autocomplete="off" oninput="bdUpdate()">
        <label for="bd-role">Job title</label><input id="bd-role" maxlength="34" autocomplete="off" oninput="bdUpdate()">
        <label for="bd-company">Company</label><input id="bd-company" maxlength="34" autocomplete="off" oninput="bdUpdate()">
        <label for="bd-ask">Ask me about&hellip;</label><input id="bd-ask" maxlength="44" autocomplete="off" oninput="bdUpdate()">
        <p class="bd-tip"><b>Ask me about&hellip;</b> is a topic you would be happy to talk about with a new contact: your work, a project, your city, a hobby or a goal.<br>For example: <i>my team's new project</i> &middot; <i>working in logistics</i> &middot; <i>learning English for meetings</i> &middot; <i>cycling in Brasília</i></p>
      </div>
      <div class="badge" id="bd-live">
        <div class="bd-event">MERIDIAN BUSINESS SUMMIT</div>
        <div class="bd-hello">Hello, I'm</div>
        <div class="bd-name" data-bd="name">&nbsp;</div>
        <div class="bd-role" data-bd="role">&nbsp;</div>
        <div class="bd-company" data-bd="company">&nbsp;</div>
        <div class="bd-ask"><b>Ask me about</b><span data-bd="ask">&nbsp;</span></div>
        <div class="bd-foot">DELEGATE</div>
      </div>
    </div>
  </div></div>
</div>''' % banner('leadin'))

# ------------------------------------------------------------------ 3 WARM-UP: WOULD YOU RATHER
def wyr(n, a, b):
    g = 'wyr%d' % n
    return ('<div class="ex-row" style="margin-bottom:18px;"><span class="circ-num">%d</span>'
            '<button class="circ-opt" style="font-size:1.1rem;padding:8px 20px;white-space:normal;text-align:left;" data-group="%s" onclick="circPick(this)">%s</button> '
            '<b style="margin:0 6px;">or</b> '
            '<button class="circ-opt" style="font-size:1.1rem;padding:8px 20px;white-space:normal;text-align:left;" data-group="%s" onclick="circPick(this)">%s</button></div>') % (n, g, a, g, b)
slide('s-lead2', 'Warm-Up – Would You Rather?', '''<div class="slide" id="s-lead2">
  %s
  <div class="slide-main"><div class="content">
    <h2>Would you rather&hellip;?</h2>
    <p class="instruction">At a conference, which would you rather do? Choose one. Then tell me why.</p>
    %s%s%s
  </div></div>
</div>''' % (banner('leadin'),
             wyr(1, 'introduce yourself to a stranger', 'wait for someone to introduce you'),
             wyr(2, 'go to a huge conference with 500 delegates', 'go to a small workshop with 15 people'),
             wyr(3, 'remember everyone\'s name but forget their job', 'remember everyone\'s job but forget their name')))

slide('s-l1', 'Listening – Key Language', '''<div class="slide" id="s-l1">
  %s
  <div class="slide-main"><div class="content">
    <h2>Listen: people meet and introduce each other</h2>
    <p class="instruction">Listen to the audio. Then try to summarize it in your own words.</p>
    %s
    <div class="two-up" style="margin-top:6px;">
      <div class="scene"><p style="margin:0 0 6px;"><b>1. Tell me what you understood</b></p>
        <p style="margin:0;">Who is talking? Who knows whom? Where do people say they met? It is OK if you do not understand everything.</p></div>
      <div class="scene"><p style="margin:0 0 6px;"><b>2. Check your understanding</b></p>
        <ul class="ccq-list" style="margin:0;">%s</ul></div>
    </div>
    <div class="btn-row" style="justify-content:flex-start;margin-top:14px;">
      <button class="btn-akey" onclick="toggleSuggested('l1-script')">📄 Show / hide the transcript</button>
    </div>
    <div class="akey-box" id="l1-script" style="background:#fff;">
      <p style="margin:0 0 8px;"><b>Transcript</b> &mdash; listen again and read at the same time.</p>
      <p style="margin:0 0 8px;"><b>1.</b> You must be Eric from the UK. Carl has told me a lot about you.</p>
      <p style="margin:0 0 8px;"><b>2.</b> I think we met in Mumbai, didn&rsquo;t we? I&rsquo;m Max from HTB Engineering. &ndash; Great to see you again!</p>
      <p style="margin:0 0 8px;"><b>3.</b> Hello, I don&rsquo;t think we&rsquo;ve met. I&rsquo;m Osric. &ndash; Hi Osric. Laura.</p>
      <p style="margin:0 0 8px;"><b>4.</b> Tony, this is Hayao from our Japanese office.<br>Hayao, meet Tony, our new director of marketing.</p>
      <p style="margin:0;"><b>5.</b> Victoria, I&rsquo;d like to introduce you to Faisal. I&rsquo;m not sure you two have met each other.<br>Nice to meet you. &ndash; How do you do?</p>
    </div>
  </div></div>
</div>''' % (banner('listening'), audio('cb1.1', top=True),
             ccq('How many short conversations do you hear?', 'Five.') +
             ccq('Has the speaker in the first conversation met Eric before?', 'No. Carl has told the speaker about him.') +
             ccq('In the second conversation, where do they think they met?', 'In Mumbai.') +
             ccq('Who is introduced to Faisal?', 'Victoria.')))

# ------------------------------------------------------------------ 4 MEANING: THREE FIRST MOMENTS (book 1.1, top)
def scene(target, cols, say_a, say_b=None, shake=False):
    b = '<div class="say b">%s</div>' % say_b if say_b else ''
    return ('<div class="scene"><div class="sc-figs">%s</div><div class="say">%s</div>%s'
            '<div class="sc-drop classify-col" data-target="%s" onclick="classifyTarget(this)">Use when you meet someone&hellip;</div></div>') % (figs(cols, shake), say_a, b, target)
S1, S2, S3 = ('you have heard about', 'you think you may have met before', 'for the first time')
chips = ''.join('<button class="classify-chip" data-ans="%s" onclick="classifyPick(this)">%s</button>' % (t, t) for t in (S2, S3, S1))
slide('s-m1', 'Vocabulary – Three First Moments', '''<div class="slide" id="s-m1">
  %s
  <div class="slide-main"><div class="content">
    <h2>Meeting a new colleague</h2>
    <p class="inst-light" style="margin:0 0 6px;">It is common to shake hands with new colleagues and introduce yourself.</p>
    <p class="instruction" style="margin-bottom:12px;">Read what each delegate says. Click a situation, then click the delegate it matches.</p>
    <div id="sit-bank" class="classify-bank" style="margin-bottom:16px;">%s</div>
    <div id="sit-cols" class="three-up">%s%s%s</div>
    <div class="btn-row">
      <button class="btn-check" onclick="checkClassifySlide('sit')">Check Answers</button>
      <button class="btn-reset" onclick="resetClassifySlide('sit')">Reset</button>
    </div>
    <div class="ccq-box"><p class="ccq-label">💭 Check your understanding</p>
      <ul class="ccq-list">%s%s%s</ul></div>
  </div></div>
</div>''' % (banner('vocab'), chips,
             scene(S1, [TEAL, BRASS], 'You must be Eric from the UK. Carl has told me a lot about you.'),
             scene(S2, [TEAL, BRASS], 'I think we met in Mumbai, didn\'t we? I\'m Max from HTB Engineering.', 'Great to see you again!'),
             scene(S3, [TEAL, BRASS], 'Hello, I don\'t think we\'ve met. I\'m Osric.', 'Hi Osric. Laura.', True),
             ccq('In the first conversation, has the speaker met Eric before?', 'No. A colleague, Carl, has told the speaker about him.'),
             ccq('In the second, is Max completely sure they have met?', 'No. He says "I think" and checks with "didn\'t we?"'),
             ccq('In the third, does Osric think they have met before?', 'No, probably not. "I don\'t think we\'ve met" is a polite way to say it.')))

# ------------------------------------------------------------------ 5 MEANING: INTRODUCING OTHER PEOPLE (book 1.1, bottom)
slide('s-m2', 'Vocabulary – Introducing Other People', '''<div class="slide" id="s-m2">
  %s
  <div class="slide-main"><div class="content">
    <h2>Introducing people you know</h2>
    <p class="instruction">It is polite to introduce people you know but who do not know each other.</p>
    <div class="two-up">
      <div class="scene"><div class="sc-figs">%s</div>
        <div class="say" style="border-left-color:#0F766E;">Tony, this is Hayao from our Japanese office.<br>Hayao, meet Tony, our new director of marketing.</div>
        <p style="margin:4px 0 0;color:var(--muted);font-size:1rem;">When you know both parties, introduce each one separately, saying both their names.</p></div>
      <div class="scene"><div class="sc-figs">%s</div>
        <div class="say" style="border-left-color:#1B3A57;">Victoria, I'd like to introduce you to Faisal.<br>I'm not sure you two have met each other.</div>
        <div class="say" style="border-left-color:#B8892B;">Nice to meet you.</div>
        <div class="say" style="border-left-color:#0F766E;">Pleased to meet you.</div>
        <p style="margin:4px 0 0;color:var(--muted);font-size:1rem;">Say a polite response when you are introduced.</p></div>
    </div>
    <div class="two-up" style="margin-top:18px;">
      %s%s
    </div>
    %s
  </div></div>
</div>''' % (banner('vocab'), figs([TEAL, INK, BRASS]), figs([INK, BRASS, TEAL]),
             reveal_card('Tony and Hayao do not know each other. Who knows both of them?', 'The speaker. That is why the speaker says both names, one sentence for each person.'),
             reveal_card('Which replies can you use when you are introduced?', '&ldquo;Nice to meet you.&rdquo; or &ldquo;Pleased to meet you.&rdquo;'),
             ''))

# ------------------------------------------------------------------ 6 CB 1.2 MATCH
def mrow(side, pair, text, num=None, example=False):
    badge = ''
    if example:
        return '<div class="match-item example-pair">%s%s</div>' % ((example_badge() if side == 'left' else ''), text)
    if side == 'left':
        return '<div class="match-item" data-side="left" data-pair="%s" onclick="matchPick(this)"><span class="circ-num">%d</span>%s</div>' % (pair, num, text)
    return '<div class="match-item" data-side="right" data-pair="%s" onclick="matchPick(this)">%s</div>' % (pair, text)

def match_slide(sid, label, banner_kind, h2, instruction, left, right, audio_track=None, extra=''):
    L = ''.join(left); R = ''.join(right)
    return '''<div class="slide" id="%s">
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
</div>''' % (sid, banner(banner_kind), h2, instruction, sid, L, R, sid, sid, audio(audio_track) if audio_track else '')

# Course Book 1.2: example = "My manager has told me" -> "so much about your business!"
cb12_left = [mrow('left', 'x', 'My manager has told me', example=True),
             mrow('left', 1, 'Hi, Katherine. I think I', 1), mrow('left', 2, 'I\'m not sure whether you', 2),
             mrow('left', 3, 'Yes, we met in Barcelona.', 3), mrow('left', 4, 'You must be Gloria from the design team.', 4),
             mrow('left', 5, 'This is Brian from customer services.', 5)]
cb12_right = [mrow('right', 2, 'have met each other before.'), mrow('right', 3, 'It\'s great to see you again.'),
              mrow('right', 'x', 'so much about your business!', example=True), mrow('right', 5, 'Brian, meet Tonya. She\'s joining our team.'),
              mrow('right', 1, 'met you at the Market Max conference.'), mrow('right', 4, 'Guvan told me about your great work.')]
slide('s-cb12', 'Vocabulary – Match the Introductions', match_slide(
    's-cb12', '', 'vocab', 'Beginnings and endings',
    'Match the beginnings of the introductions to the correct endings. Click one on the left, then one on the right.',
    cb12_left, cb12_right, 'cb1.2'))

# ------------------------------------------------------------------ 7 CB 1.3 FILL THE GAPS (word panel)
def wb_blank(ans):
    return '<span class="wb-blank" data-ans="%s" onclick="wbPlace(this)">______</span>' % ans
def wb_row(n, pre, ans, post):
    return '<div class="ex-row"><span class="circ-num">%d</span>%s %s %s</div>' % (n, pre, wb_blank(ans), post)
def wb_bank(words, example_word):
    tiles = ''
    for w in words:
        if w == example_word:
            tiles += '<button class="wb-tile example-used" data-val="%s" disabled>%s</button>' % (w, w)
        else:
            tiles += '<button class="wb-tile" data-val="%s" onclick="wbPick(this)">%s</button>' % (w, w)
    return '<div class="wb-bank book-style">%s</div>' % tiles

slide('s-cb13', 'Vocabulary – Fill in the Gaps', '''<div class="slide" id="s-cb13">
  %s
  <div class="slide-main"><div class="content">
    <h2>Complete the introductions</h2>
    <p class="instruction">Fill in the gaps using the words in the panel. Click a word, then click a gap.</p>
    %s
    %s
    <div class="fixed-two-col" id="cb13"><div>%s%s%s</div><div>%s%s</div></div>
    <div class="btn-row">
      <button class="btn-check" onclick="checkWbSlide('cb13')">Check Answers</button>
      <button class="btn-reset" onclick="resetWbSlide('cb13')">Reset</button>
    </div>
    %s
  </div></div>
</div>''' % (banner('vocab'),
             wb_bank(['must', 'introduce', 'meet', 'our', 'met', 'see'], 'must'),
             ex_given('%s You <span class="wb-blank filled is-example" data-ans="must">must</span> be Joe Smith.' % example_badge()),
             wb_row(1, 'Did we', 'meet', 'at a conference?'), wb_row(2, 'Really good to', 'see', 'you again.'),
             wb_row(3, 'Roula, meet Maria,', 'our', 'new assistant.'),
             wb_row(4, 'I\'d like to', 'introduce', 'you to Karl.'), wb_row(5, 'Have you two', 'met', 'each other before?'),
             audio('cb1.3')))

# ------------------------------------------------------------------ 8 CB 1.4 LISTENING (True / False / Not given)
slide('s-cb14', 'Listening – At the Conference', '''<div class="slide" id="s-cb14">
  %s
  <div class="slide-main"><div class="content">
    <h2>Delegates introduce themselves</h2>
    <p class="instruction">Listen to the audio and answer the questions. Delegates at a conference are introducing themselves.</p>
    %s
    %s
    <div class="fixed-two-col" id="cb14"><div>%s%s%s</div><div>%s%s</div></div>
    <div class="btn-row">
      <button class="btn-check" onclick="checkCircSlide('cb14')">Check Answers</button>
      <button class="btn-reset" onclick="resetCircSlide('cb14')">Reset</button>
    </div>
  </div></div>
</div>''' % (banner('listening'), audio('cb1.4', top=True),
             tf_example('Jared has met Sasha before.', 'True'),
             tf_row(1, 'Jared works in the Lima office.', 'False', 'cb14-1'),
             tf_row(2, 'Daniel and Sasha have not met before.', 'True', 'cb14-2'),
             tf_row(3, 'Daniel shares an office with Jared.', 'Not given', 'cb14-3'),
             tf_row(4, 'Their new product is expensive.', 'Not given', 'cb14-4'),
             tf_row(5, 'Sasha works in Lima.', 'True', 'cb14-5')))

# ------------------------------------------------------------------ 9 GRAMMAR MEANING (book 1.5)
def tl_simple():
    dots = ''.join('<circle cx="%d" cy="52" r="6" fill="#5B3A7A"/>' % x for x in (45, 105, 165, 225, 285, 345))
    return ('<svg viewBox="0 0 400 100" role="img" aria-label="repeated routine"><line x1="10" y1="52" x2="385" y2="52" stroke="#9AA5B1" stroke-width="3"/>'
            '<polygon points="392,52 380,45 380,59" fill="#9AA5B1"/>%s<text x="10" y="22" font-size="13" fill="#586573">past</text><text x="352" y="22" font-size="13" fill="#586573">future</text>'
            '<text x="170" y="82" font-size="13" fill="#586573">again and again</text></svg>') % dots
def tl_cont():
    return ('<svg viewBox="0 0 400 100" role="img" aria-label="happening now for a limited time"><line x1="10" y1="52" x2="385" y2="52" stroke="#9AA5B1" stroke-width="3"/>'
            '<polygon points="392,52 380,45 380,59" fill="#9AA5B1"/><rect x="135" y="26" width="130" height="52" rx="12" fill="rgba(15,118,110,.12)" stroke="#0F766E" stroke-width="2.5" stroke-dasharray="6 5"/>'
            '<circle cx="200" cy="52" r="8" fill="#0F766E"/><text x="10" y="22" font-size="13" fill="#586573">past</text><text x="352" y="22" font-size="13" fill="#586573">future</text>'
            '<text x="173" y="94" font-size="13" fill="#586573">now · limited time</text></svg>')
slide('s-g1', 'Grammar – Meaning: Present Simple and Continuous', '''<div class="slide" id="s-g1">
  %s
  <div class="slide-main"><div class="content">
    <h2>Always, or right now?</h2>
    <div class="gram-box"><h3>Present simple and present continuous</h3>
      <p style="margin:0;">The <span class="hl">present simple</span> is used to describe something that happens in general, or is part of a routine. The <span class="hl">present continuous</span> describes something that is happening right now, and will be continuing for a limited time.</p></div>
    <div class="big-sent">I don't usually <span class="ps">enjoy</span> networking, but I'm <span class="pc">enjoying</span> this conference.</div>
    <div class="anno-row">
      <div class="anno ps"><b>Present simple</b> is the same as the base form of the verb without &ldquo;to.&rdquo;</div>
      <div class="anno pc"><b>Present continuous</b> is formed by adding &ldquo;be&rdquo; before the verb and &ldquo;-ing&rdquo; to the verb.</div>
    </div>
    <div class="tl-wrap">
      <div class="tl"><h4>Present simple</h4><div class="tl-sub">in general · part of a routine</div>%s<div class="tl-ex">I don't usually <span class="hl">enjoy</span> networking.</div></div>
      <div class="tl"><h4>Present continuous</h4><div class="tl-sub">right now · for a limited time</div>%s<div class="tl-ex">I'm <span class="hl">enjoying</span> this conference.</div></div>
    </div>
    <div class="ccq-box"><p class="ccq-label">💭 Check your understanding</p>
      <ul class="ccq-list">%s%s%s</ul></div>
    %s
  </div></div>
</div>''' % (banner('grammar'), tl_simple(), tl_cont(),
             ccq('Do I enjoy networking in general?', 'No. &ldquo;I don\'t usually enjoy networking&rdquo; is about my general habit.'),
             ccq('Is the conference happening now?', 'Yes. &ldquo;I\'m enjoying this conference&rdquo; is about now.'),
             ccq('Will I enjoy this conference for ever?', 'No. It is only for a limited time, because the conference will end.'),
             audio('cb1.5')))

# ------------------------------------------------------------------ 10 GRAMMAR FORM
slide('s-g2', 'Grammar – Form', '''<div class="slide" id="s-g2">
  %s
  <div class="slide-main"><div class="content">
    <h2>How we build them</h2>
    <div class="form-grid">
      <div class="form-card"><h4>Present simple</h4>
        <div class="form-row"><span class="fr-k">Positive</span><span class="fr-v">I / you / we / they <b>work</b><br>he / she / it <b>works</b></span></div>
        <div class="form-row"><span class="fr-k">Negative</span><span class="fr-v">We <b>don't work</b> on Fridays.<br>She <b>doesn't work</b> in Finance.</span></div>
        <div class="form-row"><span class="fr-k">Question</span><span class="fr-v"><b>Do</b> you <b>travel</b> a lot?<br><b>Does</b> he <b>work</b> here?</span></div></div>
      <div class="form-card cont"><h4>Present continuous</h4>
        <div class="form-row"><span class="fr-k">Positive</span><span class="fr-v">I<b>'m</b> work<b>ing</b><br>you / we / they<b>'re</b> work<b>ing</b><br>he / she<b>'s</b> work<b>ing</b></span></div>
        <div class="form-row"><span class="fr-k">Negative</span><span class="fr-v">I<b>'m not</b> work<b>ing</b>.<br>He <b>isn't</b> work<b>ing</b>. They <b>aren't</b> work<b>ing</b>.</span></div>
        <div class="form-row"><span class="fr-k">Question</span><span class="fr-v"><b>Is</b> she present<b>ing</b> today?<br><b>Are</b> you stay<b>ing</b> here?</span></div></div>
    </div>
    <div class="state-box"><h4>Verbs we don't usually use in the continuous</h4>
      <p style="margin:0 0 6px;">Some verbs describe a state, not an action. We usually use the present simple, even for now.</p>
      <div class="chip-row"><span class="chip">know</span><span class="chip">like</span><span class="chip">love</span><span class="chip">hate</span><span class="chip">want</span><span class="chip">need</span><span class="chip">understand</span><span class="chip">believe</span></div>
      <p style="margin:10px 0 4px;"><span class="hl-ok">I know your manager.</span> &nbsp; <span class="hl-no">I'm knowing your manager.</span></p>
      <p style="margin:10px 0 4px;"><b>think</b> and <b>have</b> change meaning:</p>
      <p style="margin:2px 0;"><span class="hl-ok">I think it's a great venue.</span> (opinion) &nbsp;&nbsp; <span class="hl-ok">I'm thinking about the next talk.</span> (an action in my head)</p>
      <p style="margin:2px 0;"><span class="hl-ok">She has a small office.</span> (possession) &nbsp;&nbsp; <span class="hl-ok">We're having lunch.</span> (an activity)</p>
    </div>
  </div></div>
</div>''' % banner('grammar'))


# ------------------------------------------------------------------ EXTRA PRACTICE + SPEAKING BREAKS (between teaching slides)
def _xrow(n, pre, a, b, correct, post, group):
    bs = ' <span class="circ-sep">/</span> '.join('<button class="circ-opt" data-group="%s" data-correct="%s" onclick="circPick(this)">%s</button>' % (group, correct, c) for c in (a, b))
    return '<div class="ex-row"><span class="circ-num">%d</span>%s %s %s</div>' % (n, pre, bs, post)
def _xspeak(sid, label, h2, instr, items):
    rows = ''.join('<div class="ex-row"><span class="circ-num">%d</span>%s<br><button class="say-btn" style="margin-left:34px;margin-top:6px;" onclick="this.classList.toggle(\'done\')">🗣 I said it</button></div>' % (i + 1, t) for i, t in enumerate(items))
    slide(sid, label, '''<div class="slide" id="%s">
  %s
  <div class="slide-main"><div class="content">
    <h2>%s</h2>
    <p class="instruction">%s</p>
    %s
  </div></div>
</div>''' % (sid, banner('speaking'), h2, instr, rows))
XR = [("Our sales team", 'travels', 'is traveling', 'travels', "to Madrid every month."), ("Please be quiet. The director", 'gives', 'is giving', 'is giving', "a presentation."),
      ("I", 'know', 'am knowing', 'know', "your manager."), ("Right now we", 'test', 'are testing', 'are testing', "the new software."),
      ("He usually", 'starts', 'is starting', 'starts', "work at 8:00."), ("She", 'thinks', 'is thinking', 'is thinking', "about moving to another department at the moment.")]
slide('s-x1', 'Extra – Simple or Continuous?', '''<div class="slide" id="s-x1">
  %s
  <div class="slide-main"><div class="content">
    <h2>Simple or continuous?</h2>
    <p class="instruction">Cross out the incorrect word or words in each sentence. Think: is it a habit, a state, or happening now?</p>
    <div id="x1">%s</div>
    <div class="btn-row">
      <button class="btn-check" onclick="checkCircSlide('x1')">Check Answers</button>
      <button class="btn-reset" onclick="resetCircSlide('x1')">Reset</button>
    </div>
  </div></div>
</div>''' % (banner('grammar'), ''.join(_xrow(i + 1, p, a, b, c, post, 'x1-%d' % (i + 1)) for i, (p, a, b, c, post) in enumerate(XR))))
_xspeak('s-x2', 'Speaking Break – Habits and Right Now', 'Speaking break: habits and right now', 'Talk to your teacher. Use the present simple for habits and the present continuous for what is happening now. Click the button when you have said it.',
        ['What do you usually do on Monday mornings at work?', 'What are you working on at the moment? Tell me about one project.', 'Do you know many people at your company? Who do you know best?', 'What do you think about networking events? Are you enjoying this course?'])

# ------------------------------------------------------------------ 11 SMALL WORDS THAT MATTER
def chunk(title, rule, lines):
    ls = ''.join('<div class="say">%s</div>' % l for l in lines)
    return '<div class="scene"><div class="rc-q" style="font-family:\'DM Serif Display\',Georgia,serif;font-size:1.35rem;color:var(--ink);">%s</div>%s<p style="margin:2px 0 0;color:var(--muted);font-size:1rem;">%s</p></div>' % (title, ls, rule)
H = lambda t: '<span class="hl-ok">%s</span>' % t
slide('s-g3', 'Grammar – Small Words That Matter', '''<div class="slide" id="s-g3">
  %s
  <div class="slide-main"><div class="content">
    <h2>Small words that matter</h2>
    <div class="two-up">%s%s%s%s</div>
    <div style="margin-top:16px;">%s</div>
  </div></div>
</div>''' % (banner('grammar'),
             chunk('I\'d like to + verb', 'I\'d like = I would like. It is a polite way to say &ldquo;I want to.&rdquo; Compare: I like = something I enjoy.', ['I\'d like %s introduce you to the new director.' % H('to'), 'I like this venue.']),
             chunk('Nice / great / a pleasure + to + verb', 'After &ldquo;to,&rdquo; use the base verb. The verb has no ending.', ['Nice %s meet you.' % H('to'), 'Great %s see you again!' % H('to'), 'It\'s a pleasure %s meet you.' % H('to')]),
             chunk('You must be&hellip;', 'You say &ldquo;must be&rdquo; when you are almost sure who someone is.', ['You %s be the new director.' % H('must')]),
             chunk('meet, met, have met', 'did + base verb; the past form is &ldquo;met&rdquo;; have + met.', ['Did you %s Ana yesterday?' % H('meet'), 'We %s last year.' % H('met'), 'Have they %s your manager?' % H('met')]),
             chunk('Checking with a question tag', 'The tag repeats the auxiliary: did&rarr;didn\'t we? &nbsp; are&rarr;aren\'t you?', ['I think we met in Mumbai, %s' % H('didn\'t we?'), 'You\'re from Lima, %s' % H('aren\'t you?')])
             ))

_xspeak('s-x3', 'Speaking Break – Make the Introductions', 'Speaking break: make the introductions', 'Imagine you are at a conference. Say these to your teacher. Click the button when you have said it.',
        ['Say you are happy to meet your teacher. (&ldquo;It&rsquo;s a pleasure to&hellip;&rdquo;)', 'Introduce yourself politely. (&ldquo;I&rsquo;d like to introduce myself&hellip;&rdquo;)', 'You think you know who your teacher is. Check. (&ldquo;You must be&hellip;&rdquo;)', 'You think you met before. Check with a question tag. (&ldquo;We met in&hellip;, didn&rsquo;t we?&rdquo;)'])

# ------------------------------------------------------------------ 12 PRONUNCIATION
def stress_line(html):
    return '<div class="stress-line"><span>%s</span><button class="say-btn" onclick="this.classList.toggle(\'done\')">I said it</button></div>' % html
St = lambda t: '<span class="st">%s</span>' % t
Sy = lambda t: '<span class="st sy">%s</span>' % t
slide('s-pron', 'Pronunciation – Sound Like a Professional', '''<div class="slide" id="s-pron">
  %s
  <div class="slide-main"><div class="content">
    <h2>Stress the important words</h2>
    <p class="instruction">Listen to your teacher. Then say each sentence. The highlighted words are stronger and clearer.</p>
    %s%s%s%s%s
    <div class="gram-note">🔊 The small words are quick and weak. In fast speech, &ldquo;to&rdquo; sounds like /tə/ and &ldquo;you&rdquo; sounds like /jə/.</div>
  </div></div>
</div>''' % (banner('pron'),
             stress_line('%s to %s you.' % (St('Nice'), St('meet'))),
             stress_line('How do you %s?' % St('do')),
             stress_line('I\'d %s to intro%s you to %s.' % (St('like'), Sy('duce'), St('Karl'))),
             stress_line('%s to %s you a%s!' % (St('Great'), St('see'), Sy('gain'))),
             stress_line('I don\'t %s we\'ve %s.' % (St('think'), St('met')))))

# ------------------------------------------------------------------ 13 CB 1.6 READING
slide('s-cb16a', 'Reading – Making Connections', '''<div class="slide" id="s-cb16a">
  %s
  <div class="slide-main"><div class="content">
    <h2>Making connections</h2>
    <p class="instruction">Look at the title and the picture first. What do you think the article says? Then read it.</p>
    <div class="ph-small">%s</div>
    %s
  </div></div>
</div>''' % (banner('reading'), ph('🤝', 'Photo: two hands exchanging a business card'), CB_ARTICLE))

def mc_row(n, q, choices, ans, group):
    b = ''.join('<button class="circ-opt" data-group="%s" data-correct="%s" onclick="circPick(this)">%s</button>' % (group, ans, c) for c in choices)
    return '<div class="ex-row"><span class="circ-num">%d</span>%s<br><span style="margin-left:34px;display:inline-block;">%s</span></div>' % (n, q, b)
def mc_example(q, choices, ans):
    b = ''.join('<span class="circ-opt %s">%s</span>' % ('is-example' if c == ans else 'struck', c) for c in choices)
    return ex_given('%s%s<br><span style="margin-left:34px;display:inline-block;">%s</span>' % (example_badge(), q, b))
cb16 = [
 ('What kind of people is the article aimed at?', ['Shy', 'Confident', 'Intelligent'], 'Shy'),
 ('What types of connections are useful?', ['New ones', 'Good ones', 'Lots of them'], 'Good ones'),
 ('Who might be useful people to talk to?', ['Ex-colleagues', 'Recruiters', 'Family'], 'Ex-colleagues'),
 ('What do shy people do a lot?', ['Lie', 'Say sorry', 'Say thank you'], 'Say sorry'),
 ('What does apologizing a lot make you seem?', ['Confident', 'Worried', 'Unprofessional'], 'Unprofessional'),
 ('Where should you look when talking to people?', ['Their eyes', 'Their feet', 'Their mouths'], 'Their eyes'),
 ('What should you give contacts?', ['Money', 'Gifts', 'Your business card'], 'Your business card'),
]
rows = [mc_row(i + 1, q, c, a, 'cb16-%d' % (i + 1)) for i, (q, c, a) in enumerate(cb16)]
slide('s-cb16b', 'Reading – Answer the Questions', '''<div class="slide" id="s-cb16b">
  %s
  <div class="slide-main"><div class="content">
    <h2>What does the article say?</h2>
    <p class="instruction">Read the article and answer the questions.</p>
    <div style="margin-bottom:14px;">%s</div>
    %s
    <div class="fixed-two-col" id="cb16"><div>%s</div><div>%s</div></div>
    <div class="btn-row">
      <button class="btn-check" onclick="checkCircSlide('cb16')">Check Answers</button>
      <button class="btn-reset" onclick="resetCircSlide('cb16')">Reset</button>
    </div>
  </div></div>
</div>''' % (banner('reading'), article_toggle('cb16-art', CB_ARTICLE),
             mc_example('What word is used for making connections?', ['Networking', 'Sharing', 'Dividing'], 'Networking'),
             ''.join(rows[:3]), ''.join(rows[3:])))

# ------------------------------------------------------------------ 14 CB 1.7 REWRITE
CONTR = [("I'm", 'I am'), ("don't", 'do not'), ("we've", 'we have'), ("I'd", 'I would')]
def rw_row(n, prompt, ans, extra_alt=''):
    al = alts(ans, CONTR)
    if extra_alt: al = (al + '|' + extra_alt) if al else extra_alt
    return ('<div class="ex-row"><span class="circ-num">%d</span>%s<input class="ans-input wide" data-ans="%s" data-alt="%s" aria-label="rewrite %d"></div>'
            % (n, prompt, ans.replace('"', '&quot;'), al.replace('"', '&quot;'), n))
rw_ex = ex_given('%s<span>I am being happy to finally meet you, Zoe.</span><span class="ans-line">I\'m happy to finally meet you, Zoe.</span>' % example_badge())
slide('s-cb17', 'Grammar – Correct the Errors', '''<div class="slide" id="s-cb17">
  %s
  <div class="slide-main"><div class="content">
    <h2>Spot the mistake</h2>
    <p class="instruction">Rewrite the sentences, correcting the errors.</p>
    %s
    <div class="fixed-two-col" id="cb17"><div>%s%s</div><div>%s%s</div></div>
    <div class="btn-row">
      <button class="btn-check" onclick="checkSlide('cb17')">Check Answers</button>
      <button class="btn-reset" onclick="resetSlide('cb17')">Reset</button>
    </div>
    %s
  </div></div>
</div>''' % (banner('grammar'), rw_ex,
             rw_row(1, 'Hi James. I\'m Vanisha. I don\'t think we are meeting before.', 'Hi James. I\'m Vanisha. I don\'t think we\'ve met before.'),
             rw_row(2, 'Ashley, I\'d like introduce you to my colleague Neil.', 'Ashley, I\'d like to introduce you to my colleague Neil.'),
             rw_row(3, 'I enjoying the presentations. Are you?', 'I am enjoying the presentations. Are you?'),
             rw_row(4, 'Nice to meet you Bethany. How do you doing?', 'Nice to meet you Bethany. How do you do?'),
             audio('cb1.7')))

# ------------------------------------------------------------------ 15 CB 1.8 CROSS OUT + SAY ALOUD
def co_row(n, pre, a, b, correct, post, group):
    ba = '<button class="circ-opt" data-group="%s" data-correct="%s" onclick="circPick(this)">%s</button>' % (group, correct, a)
    bb = '<button class="circ-opt" data-group="%s" data-correct="%s" onclick="circPick(this)">%s</button>' % (group, correct, b)
    sp = '' if post[:1] in '?.,!' else ' '
    return ('<div class="ex-row"><span class="circ-num">%d</span>%s %s <span class="circ-sep">/</span> %s%s%s<br>'
            '<button class="say-btn" style="margin-left:34px;margin-top:6px;" onclick="this.classList.toggle(\'done\')">🗣 I said it</button></div>') % (n, pre, ba, bb, sp, post)
co_ex = ex_given('%sI\'m sorry, how <span class="circ-opt is-example">do you say</span> <span class="circ-sep">/</span> <span class="circ-opt struck">are you saying</span> your name again?' % example_badge())
slide('s-cb18', 'Speaking – Choose, Then Say It', '''<div class="slide" id="s-cb18">
  %s
  <div class="slide-main"><div class="content">
    <h2>Choose, then say it</h2>
    <p class="instruction">Cross out the incorrect words in each sentence, then say the sentences out loud.</p>
    %s
    <div class="fixed-two-col" id="cb18"><div>%s%s</div><div>%s%s</div></div>
    <div class="btn-row">
      <button class="btn-check" onclick="checkCircSlide('cb18')">Check Answers</button>
      <button class="btn-reset" onclick="resetCircSlide('cb18')">Reset</button>
    </div>
    %s
  </div></div>
</div>''' % (banner('speaking'), co_ex,
             co_row(1, 'Hello Frank.', 'Are you enjoying', 'do you enjoy', 'Are you enjoying', 'the conference?', 'cb18-1'),
             co_row(2, 'Wilfred, I\'d like you to', 'meet', 'be meeting', 'meet', 'Roger, our new press officer.', 'cb18-2'),
             co_row(3, 'Serena, it\'s really great to', 'see', 'seeing', 'see', 'you again after so long.', 'cb18-3'),
             co_row(4, 'I usually enjoy workshops, but I am not', 'find', 'finding', 'finding', 'this one interesting.', 'cb18-4'),
             audio('cb1.8')))

# ------------------------------------------------------------------ 16 FREER PRACTICE: WORK THE ROOM
slide('s-free', 'Speaking – Work the Room', '''<div class="slide" id="s-free">
  %s
  <div class="slide-main"><div class="content">
    <h2>Work the room</h2>
    <p class="instruction">Your teacher is another delegate. Take a card, then start the conversation.</p>
    <div class="deal-wrap">
      <div class="deal-card" id="deal-card"><div class="dc-head">Delegate card</div>
        <div class="dc-body"><p class="dc-setting">Ready?</p><p class="dc-line">Press <b>Deal a card</b> to see who you are, who you meet, and what you need to do.</p></div></div>
      <div class="btn-row" style="margin-top:0;align-items:center;">
        <button class="btn-deal" onclick="dealNext()">Deal a card</button>
        <button class="btn-reset" onclick="dealReset()">Shuffle</button>
        <span class="deal-count" id="deal-count">Cards played: 0</span>
      </div>
    </div>
  </div></div>
</div>''' % banner('speaking'))

# ------------------------------------------------------------------ 17 LESSON REVIEW
def ck(label, icon):
    return '<button class="check-item" onclick="ckToggle(this)"><span class="ck"></span><span>%s</span><span class="ck-ic">%s</span></button>' % (label, icon)
slide('s-review', 'Lesson Review – Before You Leave the Lobby', '''<div class="slide" id="s-review">
  %s
  <div class="slide-main"><div class="content">
    <h2>Before you leave the lobby</h2>
    <p class="instruction">Click each one when you feel ready to use it.</p>
    <div class="lead-grid">
      <div>
        <div class="check-list" id="ck-list">%s%s%s</div>
        <div class="win-banner" id="ck-win">You are ready for the next unit.</div>
      </div>
      <div>
        <div class="badge" id="bd-review">
          <div class="bd-event">MERIDIAN BUSINESS SUMMIT</div>
          <div class="bd-hello">Hello, I'm</div>
          <div class="bd-name" data-bd="name">&nbsp;</div>
          <div class="bd-role" data-bd="role">&nbsp;</div>
          <div class="bd-company" data-bd="company">&nbsp;</div>
          <div class="bd-ask"><b>Ask me about</b><span data-bd="ask">&nbsp;</span></div>
          <div class="bd-foot">DELEGATE</div>
        </div>
      </div>
    </div>
    <p class="instruction" style="margin-top:22px;">Introduce yourself to me one more time. What is different from the first time?</p>
  </div></div>
</div>''' % (banner('review'),
             ck('Present simple and continuous', '⚙️'), ck('Etiquette for introductions', '🤝'), ck('Introducing yourself and others', '🧩')))
