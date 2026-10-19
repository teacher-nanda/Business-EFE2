# -*- coding: utf-8 -*-
# Unit 5 "Delegating tasks" — lesson slides.  Theme: the delegation memo.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'shared'))
from lib import *
from ex import *
import audiolib as AL
U = '5'
SPEAK_EX.update({
 "s-sp1": [
  "I have to answer emails every day. I must never forget a deadline.",
  "I don't have to wear a suit, but some people do.",
  "I must not share passwords. It's against company policy.",
  "What do you have to do this week?"
 ],
 "s-sp2": [
  "Could you look after my project for a week?",
  "Would you send me the report by Friday?",
  "You must not miss the deadline on Monday.",
  "I have to finish the presentation before I leave."
 ]
})

cover(5, 'Delegating tasks', ["I have to leave this with you.", "You must complete this project by Monday.", "Could you look after this for me?", "You don't have to deal with this today."])

content('s-lead', 'Warm-Up – Delegation Memo', 'leadin', 'Delegation memo', '''
    <div class="lead-grid">
      <div class="bd-form">
        <label for="dm-1">A task you would like to delegate</label><input id="dm-1" data-live="task" maxlength="48" autocomplete="off">
        <label for="dm-2">Who would do it</label><input id="dm-2" data-live="who" maxlength="40" autocomplete="off">
        <label for="dm-3">The deadline</label><input id="dm-3" data-live="when" maxlength="40" autocomplete="off">
        <label for="dm-4">A task you would never delegate</label><input id="dm-4" data-live="never" maxlength="48" autocomplete="off">
      </div>
      <div class="profile-card">
        <div class="pc-h">Memo &middot; Delegation</div>
        <div class="pc-row"><span class="pc-k">Task</span><span class="pc-v" data-bd="task">&nbsp;</span></div>
        <div class="pc-row"><span class="pc-k">Assigned to</span><span class="pc-v" data-bd="who">&nbsp;</span></div>
        <div class="pc-row"><span class="pc-k">Deadline</span><span class="pc-v" data-bd="when">&nbsp;</span></div>
        <div class="pc-row"><span class="pc-k">Never delegate</span><span class="pc-v" data-bd="never">&nbsp;</span></div>
      </div>
    </div>''', 'When things get busy, you may want to delegate tasks to colleagues. Fill in your memo, then tell me how you would ask.')

OB, NO, PR = 'obligation', 'no obligation', 'prohibited'
sort_slide('s-m1', 'Meaning – Levels of Obligation', 'grammar', 'How strong is it?',
           'Certain modal verbs can be used to say that someone needs to do something. Click a sentence, then click the box where it belongs.',
           [("I have to leave this with you.", OB), ("I need to leave this with you.", OB), ("You must complete this project by Monday.", OB),
            ("You don't have to deal with this today.", NO), ("You must not go into the testing area.", PR), ("We don't have to work late tomorrow.", NO)],
           [(OB, '<b>Obligation</b><br>someone needs to do something'), (NO, '<b>No obligation</b><br>there is no need to do it'), (PR, '<b>Prohibited</b><br>someone must not do it')],
           post=ccqs(('&ldquo;You don\'t have to deal with this today.&rdquo; Can I deal with it today if I want to?', 'Yes. It is allowed, but it is not necessary.'),
                     ('&ldquo;You must not go into the testing area.&rdquo; Is it allowed?', 'No. &ldquo;Must not&rdquo; means that something is prohibited.'),
                     ('Why can &ldquo;must&rdquo; sound impolite?', 'It is a direct way to say something needs to be done.')),
           aud=AL.single(U, '5_1'))

content('s-g1', 'Grammar – Form', 'grammar', 'How we build them', '''
    <p style="margin:0 0 4px;">&ldquo;Must&rdquo; does not change with the subject, but &ldquo;have to&rdquo; becomes &ldquo;has to&rdquo; in the third person singular. Both are followed by the base form of the main verb. &ldquo;Need&rdquo; acts like a modal verb here, expressing strong obligation.</p>
    ''' + puzzle([('Subject', 'You', ''), ('&ldquo;Must / have to&rdquo;', 'must<br>have (got) to<br>must not<br>don\'t have to', 'a'), ('Main verb', 'leave', ''), ('Rest of sentence', 'early tomorrow.', '')]) + '''
    <div class="two-up">%s%s</div>''' % (
        reveal_card('Which is correct: &ldquo;He must to leave&rdquo; or &ldquo;He must leave&rdquo;?', '&ldquo;He must leave.&rdquo; Must is followed by the base form, without &ldquo;to.&rdquo;'),
        reveal_card('Which is correct: &ldquo;She have to leave&rdquo; or &ldquo;She has to leave&rdquo;?', '&ldquo;She has to leave.&rdquo; Have to becomes has to in the third person singular.')))

M3L = [mrow('left', 'x', 'I need you to', example=True), mrow('left', 1, 'We have got to ask', 1), mrow('left', 2, 'You must put the finished', 2),
       mrow('left', 3, 'We must not forget', 3), mrow('left', 4, 'I have to help Sami produce', 4), mrow('left', 5, 'You don\'t have', 5)]
M3R = [mrow('right', 4, 'a report about recycling.'), mrow('right', 5, 'to complete it today.'), mrow('right', 'x', 'take care of this project while I\'m away.', example=True),
       mrow('right', 2, 'proposal on my desk tomorrow.'), mrow('right', 3, 'to look after this project while he\'s away.'), mrow('right', 1, 'for some support on this project.')]
match_exercise('s-cb53', 'Grammar – Match the Endings', 'grammar', 'Beginnings and endings', 'Match the beginnings of the sentences to the correct endings. Click one on the left, then one on the right.', M3L, M3R, aud=AL.clips(U, '5_3', 5))

O4 = [(["We need to increase sales to Europe.", "We need increase sales to Europe."], 0), (["We can't reveal our new product yet.", "We can't to reveal our new product yet."], 0),
      (["You don't having to work late.", "You don't have to work late."], 1), (["I will need the accounts by tomorrow.", "I need have the accounts tomorrow."], 0),
      (["We have get to find a new IT manager.", "We have got to find a new IT manager."], 1), (["You must to produce a spreadsheet.", "You need to produce a spreadsheet."], 1),
      (["We must reaching our sales target.", "We must reach our sales target."], 1)]
exercise('s-cb54', 'Grammar – Mark the Correct Sentences', 'grammar', 'Which sentence is correct?', 'Mark the sentences that are correct.',
         [pick_row(i + 1, o, o[a], 'cb54-%d' % (i + 1)) for i, (o, a) in enumerate(O4)], 'circ',
         example=pick_example(["You have to do this assignment today.", "You has to do this assignment today."], "You have to do this assignment today."),
         aud=AL.clips(U, '5_4', 7), gid='cb54')

T5 = [("The conference will take place in August.", 'True'), ("The conference will take place at the office.", 'False'), ("The manager wants Shona to ask about prices.", 'False'),
      ("Shona must complete the task by tomorrow.", 'False'), ("Shona's boss often delegates work to her.", 'Not given')]
exercise('s-cb55', 'Listening – Delegating Tasks', 'listening', 'A manager delegates', 'Listen to the audio and answer the questions. A manager is delegating tasks to an employee at a firm.',
         [tf_row(i + 1, t, a, 'cb55-%d' % (i + 1)) for i, (t, a) in enumerate(T5)], 'circ',
         example=tf_example('The conference takes place once a year.', 'Not given'), pre=AL.single(U, '5_5', top=True), gid='cb55')

speak('s-sp1', 'Speaking Break – Delegate and Explain', 'Speaking break: what you have to do', 'Answer the questions about obligations at work.', [
    'What do you have to do every day at work? What must you never forget?',
    'What do you not have to do at work, but some people do?',
    'What must you not do at work? Why?',
    'Ask: &ldquo;What do you have to do this week?&rdquo;'])

content('s-m2', 'Meaning – Politeness', 'grammar', 'Sound polite', '''
    <div class="two-up">
      <div class="scene"><div class="sc-figs">%s</div><div class="say">%s</div>
        <p style="margin:4px 0 0;color:var(--muted);font-size:1rem;">To maintain a friendly, polite atmosphere, use &ldquo;we&rdquo; instead of &ldquo;you&rdquo; to express obligation.</p></div>
      <div class="scene"><div class="sc-figs">%s</div><div class="say b">%s</div>
        <p style="margin:4px 0 0;color:var(--muted);font-size:1rem;">&ldquo;Would&rdquo; is more formal and is rarely used.</p></div>
    </div>
    %s
    %s''' % (figs([TEAL, BRASS]), 'We <b>have to</b> finish this project soon.', figs([BRASS, INK]), '<b>Could / Would</b> you look after this for me?',
             ccqs(('Who has to finish the project when I say &ldquo;We have to finish this project soon&rdquo;?', 'Probably you and I, but the speaker is asking more politely.'),
                  ('&ldquo;Could you look after this for me?&rdquo; Is it an order or a request?', 'A polite request.')),
             AL.single(U, '5_6')), 'Other modal verbs can also be used in business to delegate tasks politely.')

W7 = [("Could you answer my phone?", ['you', 'answer', 'my', 'Could', 'phone?']), ("Would you call the supplier?", ['you', 'Would', 'call', 'the', 'supplier?']),
      ("We have to finish today.", ['We', 'to', 'have', 'today.', 'finish']), ("Would you book a meeting?", ['you', 'Would', 'a', 'book', 'meeting?']),
      ("Could you send this today?", ['send', 'this', 'Could', 'you', 'today?'])]
exercise('s-cb57', 'Grammar – Word Order', 'grammar', 'Put the words in order', 'Rewrite the sentences, putting the words in the correct order.',
         [order_row(i + 1, w, a) for i, (a, w) in enumerate(W7)], 'typed',
         example=order_example(['you', 'print', 'copy?', 'a', 'Could', 'me'], 'Could you print me a copy?'), aud=AL.clips(U, '5_7', 5), gid='cb57')

speak('s-sp2', 'Speaking Break – Polite Requests', 'Speaking break: polite requests', 'Read each situation. What could you say? Use polite modals.', [
    'You are going on vacation for a week. What could you say to ask a colleague to look after your project?',
    'You need a report by Friday. How could you ask a colleague politely?',
    'A colleague might forget an important deadline on Monday. What could you say?',
    'It is the end of the day and you still have work to finish. What could you say?'])

content('s-pron', 'Pronunciation – Linking Modals', 'pron', 'Say it naturally', '''
    <p class="instruction">Listen, then say each sentence. The highlighted words are stronger and clearer.</p>
    %s%s%s%s
    <div class="gram-note">🔊 In fast speech, &ldquo;have to&rdquo; sounds like &ldquo;hafta&rdquo; /hæftə/, &ldquo;got to&rdquo; like &ldquo;gotta&rdquo; /gɑtə/ and &ldquo;could you&rdquo; like &ldquo;could-ya&rdquo; /kʊdʒə/.</div>''' % (
    say_line('I %s to %s this with you.' % (St('have'), St('leave'))), say_line('%s you %s after this for me?' % (St('Could'), St('look'))),
    say_line('You %s %s into the %s area.' % (St('must not'), St('go'), St('testing'))), say_line('You %s %s to %s with this %s.' % (St('don\'t'), St('have'), St('deal'), St('today'))) ))

C8 = [("", ['Could', 'Have'], 'Could', "you deliver this letter for me, please?"), ("", ['Must', 'Would'], 'Would', "you show the new employee around the office?"),
      ("Jess, I", ['have got', 'need to'], 'need to', "leave early today. Could you let Philippe know?")]
exercise('s-cb58', 'Speaking – Choose, Then Say It', 'speaking', 'Choose, then say it', 'Cross out the incorrect words in each sentence, then say the sentences out loud.',
         [co_row(i + 1, p, c, a, post, 'cb58-%d' % (i + 1), say=True) for i, (p, c, a, post) in enumerate(C8)], 'circ',
         example=co_example("Don't worry! You", ["don't have to", 'must not'], "don't have to", 'deal with this right now.'), aud=AL.clips(U, '5_8', 3), gid='cb58')

SHARE = article('Business Weekly', 'Sharing the load', 'Relieve stress by learning to delegate better', [
    "Team leaders must think about goals and how to achieve them. This takes time. You won't have this thinking time if you're busy doing routine tasks and you will feel stressed. You have to let your team members handle the everyday tasks. Show your team members you trust them. Ask them if they could show you a plan of how they can manage their work in their own way. This way you will build a better working relationship."])
content('s-cb59a', 'Reading – Sharing the Load', 'reading', 'Sharing the load', '<div class="ph-small">%s</div>%s' % (ph('🗂️', 'Photo: colorful office folders on a shelf'), SHARE),
        'Look at the title and the picture first. What do you think the article says? Then read it.')
T9 = [("A routine task is answering customer enquiries.", 'Not given'), ("People who don't delegate often feel stressed.", 'True'), ("A team leader has to avoid doing everyday tasks.", 'True'),
      ("Trust in managers is falling in most companies.", 'Not given'), ("Team leaders should trust their staff.", 'True')]
exercise('s-cb59b', 'Reading – True, False, Not Given', 'reading', 'What does the article say?', 'Read the article and answer the questions.',
         [tf_row(i + 1, t, a, 'cb59-%d' % (i + 1)) for i, (t, a) in enumerate(T9)], 'circ',
         example=tf_example('Team leaders should do everyday tasks.', 'False'), pre='<div style="margin-bottom:14px;">%s</div>' % article_toggle('cb59-art', SHARE), gid='cb59')

chat_speak('s-free', 'Speaking – Delegate It', 'Delegate it', 'Read the conversation as it goes. When it is your turn, say what you could say.', 'Alex', [
 ("Hi, you wanted to see me?", 'Politely ask Alex to prepare a report by Friday.', "Yes, Alex. Could you prepare the sales report by Friday?"),
 ("Sure.<br>Do I have to include last year's numbers?", 'Say that it is obligatory.', "Yes, you must include last year's numbers. We need them for the comparison."),
 ("Do I need to send it to the whole team?", 'Say that it is not necessary.', "No, you don't have to send it to the whole team. Just send it to me."),
 ("Is there anything I must not forget?", 'Say what Alex must not forget.', "You must not forget to check the figures. Mistakes are a big problem."),
 ("The deadline is tight.<br>What if I'm late?", 'Say how strict the deadline is.', "You can't be late, I'm afraid. The report has to be ready by 5pm on Friday."),
 ("Understood.<br>Is there anything else?", 'Ask for one more small thing, politely.', "Would you also reserve the meeting room for Monday? Thanks so much!")])
review([('Modal verbs for obligation', '⚙️'), ('Delegation and politeness', '🤝'), ('Delegating tasks to colleagues', '🧩')], 'Before you leave', 'Delegate one real task to me, politely. Then tell me one thing I must not do.')

# ---- CB p.29 REVIEW of Units 1-5 (book table)
rows5 = [('Introducing yourself and others', 'You must be Eric from the UK. / Tony, this is Hayao from our Japanese office.', 'Unit 1'),
         ('The past simple and the past continuous for past experiences', 'I was working 60 hours per week when I came here.', 'Unit 2'),
         ('The past tense for politeness', 'Did you want a tour of the office?', 'Unit 2'),
         ('Talking about the recent past with the present perfect simple', 'I have worked in a few different teams.', 'Unit 2'),
         ('Talking about changes with &ldquo;used to&rdquo; and &ldquo;be / get used to&rdquo;', 'Staff used to eat lunch at their desks. / It took a while to get used to the commute.', 'Unit 4'),
         ('Delegating tasks with modals', 'I have to leave this with you. / Could you look after this for me?', 'Unit 5')]
def ck5(a, b, c):
    return '<button class="check-item" onclick="ckToggle(this)"><span class="ck"></span><span><b>%s</b><br><span style="color:var(--muted);font-size:.95rem;">%s</span></span><span class="ck-ic" style="font-size:.9rem;color:var(--muted);">%s</span></button>' % (a, b, c)
slide('s-review5', 'Review of Units 1–5', '''<div class="slide" id="s-review5">
  %s
  <div class="slide-main"><div class="content">
    <h2>Review: Units 1&ndash;5</h2>
    <p class="instruction">Look back at the English you have learned. Click each one when you can use it, and try the sample sentence out loud.</p>
    <div class="check-list" id="ck-list5">%s</div>
    <div class="win-banner" id="ck-win5">You have completed the review of Units 1&ndash;5.</div>
  </div></div>
</div>''' % (banner('review'), ''.join(ck5(*r) for r in rows5)))
