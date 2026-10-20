# -*- coding: utf-8 -*-
# Unit 1 "Introductions" — homework slides (Practice Book Unit 1, exercises 1.1-1.5, in book order)
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'shared'))
import aihw
from lib import slide, audio, banner, ex_given, example_badge, tf_row, tf_example, PB_ARTICLE, ph
from s_lesson import (wb_row, wb_bank, wb_blank, mrow, mc_row, rw_row, co_row, alts)

slide('hw-cover', 'Homework Cover', '''<div class="slide" id="hw-cover">
  <div class="title-inner">
    <div class="hw-badge">📝 Homework</div>
    <div class="title-main" style="margin-top:22px;">Introductions</div>
  </div>
</div>''')

# ---- HW1 (Practice Book 1.1): fill in the gaps using the words in the panel
slide('hw-1', 'HW1 – Fill in the Gaps', '''<div class="slide" id="hw-1">
  %s
  <div class="slide-main"><div class="content">
    <h2>HW1 — Fill in the gaps</h2>
    <p class="instruction">Fill in the gaps using the words in the panel. Click a word, then click a gap.</p>
    %s
    %s
    <div class="fixed-two-col" id="hw1"><div>%s%s%s%s</div><div>%s%s%s%s%s</div></div>
    <div class="btn-row">
      <button class="btn-check" onclick="checkWbSlide('hw1')">Check Answers</button>
      <button class="btn-reset" onclick="resetWbSlide('hw1')">Reset</button>
    </div>
    %s
  </div></div>
</div>''' % (banner('hw'),
             wb_bank(['pleasure', 'see', 'do', 'told', 'met', 'must', 'think', 'meet', 'introduce', 'Nice'], 'do'),
             ex_given('%s How do you <span class="wb-blank filled is-example" data-ans="do">do</span> ? I\'m Christophe from BlueTech.' % example_badge()),
             wb_row(1, 'I\'d like to', 'introduce', 'you to Marco from IT.'), wb_row(2, 'You', 'must', 'be Paola from Madrid.'),
             wb_row(3, 'Gloria,', 'meet', 'Julia, our new secretary.'), wb_row(4, 'Have you two', 'met', 'each other before?'),
             wb_row(5, 'Great to', 'see', 'you again!'), wb_row(6, '', 'Nice', 'to meet you, Antonio.'),
             wb_row(7, 'Sanjay has', 'told', 'me all about you.'), wb_row(8, 'I don\'t', 'think', 'we\'ve met before, have we?'),
             wb_row(9, 'It\'s a', 'pleasure', 'to meet you.'),
             audio('pb1.1')))

# ---- HW2 (Practice Book 1.2): match the beginnings to the correct endings
from s_lesson import match_slide
hw2_left = [mrow('left', 'x', 'Peter, Philippe, I\'m not sure', example=True),
            mrow('left', 1, 'Simone, I\'d like to introduce you to', 1), mrow('left', 2, 'Hello. I don\'t think we\'ve', 2),
            mrow('left', 3, 'You must be Selma from the', 3), mrow('left', 4, 'Hi, Omar. I think we', 4),
            mrow('left', 5, 'My boss has told me', 5), mrow('left', 6, 'This is Colin from IT.', 6)]
hw2_right = [mrow('right', 1, 'Gerald, our new sales manager.'), mrow('right', 2, 'met. My name\'s Jana.'),
             mrow('right', 'x', 'if you have met each other.', example=True), mrow('right', 5, 'so much about your work.'),
             mrow('right', 6, 'Colin, meet Liam. He\'s joining our team soon.'), mrow('right', 3, 'Chicago branch. Great to meet you.'),
             mrow('right', 4, 'met at the conference in Dubai last year.')]
slide('hw-2', 'HW2 – Match the Introductions', match_slide(
    'hw-2', '', 'hw', 'HW2 — Beginnings and endings',
    'Match the beginnings of the introductions to the correct endings. Click one on the left, then one on the right.',
    hw2_left, hw2_right, 'pb1.2'))

# ---- HW3 (Practice Book 1.3): read the article and answer the questions
pb13 = [
 ('Meeting people will always make you successful.', 'False'),
 ('You should talk about your recent experiences.', 'True'),
 ('The author thinks food is a good topic of conversation.', 'Not given'),
 ('You shouldn\'t ask how much someone earns.', 'True'),
 ('The author suggests talking about your education.', 'False'),   # TEACHER NOTE: the official key says False (the article does not mention education, so "Not given" would be expected) - see summary
 ('The author says that you shouldn\'t talk about clients.', 'False'),
]
r3 = [tf_row(i + 1, t, a, 'hw3-%d' % (i + 1)) for i, (t, a) in enumerate(pb13)]
slide('hw-3', 'HW3 – Read and Answer', '''<div class="slide" id="hw-3">
  %s
  <div class="slide-main"><div class="content">
    <h2>HW3 — Meeting and greeting</h2>
    <p class="instruction">Read the article and answer the questions.</p>
    <!-- TEACHER NOTE: answer 5 follows the official key (False). Strictly, the article never mentions education, so "Not given" would also be defensible. -->
    %s
    %s
    <div class="fixed-two-col" id="hw3"><div>%s%s%s</div><div>%s%s%s</div></div>
    <div class="btn-row">
      <button class="btn-check" onclick="checkCircSlide('hw3')">Check Answers</button>
      <button class="btn-reset" onclick="resetCircSlide('hw3')">Reset</button>
    </div>
  </div></div>
</div>''' % (banner('hw'), PB_ARTICLE,
             tf_example('The author says that meeting people is easy.', 'False'),
             r3[0], r3[1], r3[2], r3[3], r3[4], r3[5]))

# ---- HW4 (Practice Book 1.4): rewrite the sentences, correcting the errors
CONTR2 = [("I'm", 'I am'), ("don't", 'do not'), ("doesn't", 'does not'), ("it's", 'it is'), ("I'd", 'I would')]
def rw2(n, cue, prompt, ans):
    al = alts(ans, CONTR2)
    if 'José' in ans: al = (al + '|' if al else '') + ans.replace('José', 'Jose') + '|' + ans.replace('José', 'Jose').replace("I'd", 'I would')
    return ('<div class="ex-row"><span class="circ-num">%d</span><span class="cue">%s</span>%s<input class="ans-input wide" data-ans="%s" data-alt="%s" aria-label="rewrite %d"></div>'
            % (n, cue, prompt, ans.replace('"', '&quot;'), al.replace('"', '&quot;'), n))
hw4 = [
 ('🚆', 'I am catching the train to work at 8:15am each morning.', 'I catch the train to work at 8:15am each morning.'),
 ('🖨️', 'We are having a new printer that is difficult to use.', 'We have a new printer that is difficult to use.'),
 ('🏙️', 'I working at the Guangdong branch all this August.', 'I am working at the Guangdong branch all this August.'),
 ('🤝', 'Sanchez is knowing Katie because they worked together.', 'Sanchez knows Katie because they worked together.'),
 ('📊', 'Do you enjoying this presentation? I think it\'s great.', 'Are you enjoying this presentation? I think it\'s great.'),
 ('👥', 'Tim isn\'t knowing Anna from the Montevideo branch.', 'Tim doesn\'t know Anna from the Montevideo branch.'),
 ('🪑', 'Marek is liking the new furniture we bought for the office.', 'Marek likes the new furniture we bought for the office.'),
 ('🔤', 'How are you spelling your name?', 'How do you spell your name?'),
 ('🗓️', 'The meeting usually is take only half an hour.', 'The meeting usually takes only half an hour.'),
 ('🎤', 'Doug is really enjoy the conference this year.', 'Doug is really enjoying the conference this year.'),
 ('🤝', 'I\'d like introduce you to my manager, José Rodriguez.', 'I\'d like to introduce you to my manager, José Rodriguez.'),
 ('⏰', 'Clara working from 8:30 to 4:30 on Thursdays and Fridays.', 'Clara works from 8:30 to 4:30 on Thursdays and Fridays.'),
]
r4 = [rw2(i + 1, c, p, a) for i, (c, p, a) in enumerate(hw4)]
slide('hw-4', 'HW4 – Correct the Errors', '''<div class="slide" id="hw-4">
  %s
  <div class="slide-main"><div class="content">
    <h2>HW4 — Spot the mistake</h2>
    <p class="instruction">Rewrite the sentences, correcting the errors.</p>
    %s
    <div class="fixed-two-col" id="hw4"><div>%s</div><div>%s</div></div>
    <div class="btn-row">
      <button class="btn-check" onclick="checkSlide('hw4')">Check Answers</button>
      <button class="btn-reset" onclick="resetSlide('hw4')">Reset</button>
    </div>
    %s
  </div></div>
</div>''' % (banner('hw'),
             ex_given('%s<span class="cue">🏨</span><span>I staying at the hotel on Park Lane all this week.</span><span class="ans-line">I\'m staying at the hotel on Park Lane all this week.</span>' % example_badge()),
             ''.join(r4[:6]), ''.join(r4[6:]), audio('pb1.4')))

# ---- HW5 (Practice Book 1.5): cross out the incorrect words, then say the sentences out loud
def co2(n, pre, a, b, correct, post):
    return co_row(n, pre, a, b, correct, post, 'hw5-%d' % n)
hw5_ex = ex_given('%sRaul <span class="circ-opt struck">presents</span> <span class="circ-sep">/</span> <span class="circ-opt is-example">is presenting</span> at the moment.' % example_badge())
r5 = [
 co2(1, 'Our company', 'is having', 'have', 'is having', 'some difficulties at the moment.'),
 co2(2, 'Pablo, I\'d like you to', 'meet', 'meeting', 'meet', 'my wife, Elvira.'),
 co2(3, 'I usually hate conferences, but I', 'enjoy', 'am enjoying', 'am enjoying', 'this one a lot.'),
 co2(4, 'I', 'have', 'am having', 'have', 'two children, a son and a daughter.'),
 co2(5, 'Michael,', 'I like', 'I\'d like', 'I\'d like', 'to introduce you to Michelle.'),
 co2(6, 'I', 'don\'t think', 'am not thinking', 'don\'t think', 'we\'ve met before, have we?'),
 co2(7, 'It\'s so great', 'to see', 'see', 'to see', 'you again after such a long time.'),
 co2(8, 'How', 'do you pronounce', 'are you pronouncing', 'do you pronounce', 'your last name?'),
 co2(9, 'You must', 'be', 'being', 'be', 'Harold from Copenhagen. Nice to meet you.'),
 co2(10, 'Hi, I think we met in Oslo,', 'aren\'t we', 'didn\'t we', 'didn\'t we', '?'),
]
slide('hw-5', 'HW5 – Choose, Then Say It', '''<div class="slide" id="hw-5">
  %s
  <div class="slide-main"><div class="content">
    <h2>HW5 — Choose, then say it</h2>
    <p class="instruction">Cross out the incorrect words in each sentence, then say the sentences out loud.</p>
    %s
    <div class="fixed-two-col" id="hw5"><div>%s</div><div>%s</div></div>
    <div class="btn-row">
      <button class="btn-check" onclick="checkCircSlide('hw5')">Check Answers</button>
      <button class="btn-reset" onclick="resetCircSlide('hw5')">Reset</button>
    </div>
    %s
  </div></div>
</div>''' % (banner('hw'), hw5_ex, ''.join(r5[:5]), ''.join(r5[5:]), audio('pb1.5')))


slide('hw-ai', 'HW – Practice with AI', aihw.ai_slide(banner('hw'), 'hw-ai', 'present simple and present continuous, and introducing myself and other people at a business event', 'present simple for habits, present continuous for what is happening now, and phrases for introductions', 'What do you usually do at work, and what are you working on at the moment?', 'Save your best corrected sentences. Bring them to the next class.'))
