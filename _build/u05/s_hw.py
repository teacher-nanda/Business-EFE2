# -*- coding: utf-8 -*-
# Practice Book homework (with PB supporting audio and listening exercises)
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'shared'))
from lib import *
from ex import *
hw_cover('Delegating tasks')

H1 = [(["Staff must not smoking in the building.", "Staff must not smoke in the building."], 1), (["We don't have to go to work tomorrow.", "We not have to go to work tomorrow."], 0),
      (["I have to go home early on Thursday.", "I have going home early on Thursday."], 0), (["You have to do this assignment today.", "You has to do this assignment today."], 0),
      (["We need to increase sales this year.", "We need increase sales this year."], 0), (["Jim doesn't have to attend the meeting.", "Jim don't have to attend the meeting."], 0),
      (["The team must not forget their timesheets.", "The team must forget not their timesheets."], 0), (["Paolo has got to signing up for the course.", "Paolo has got to sign up for the course."], 1),
      (["We will need to hire new staff this fall.", "We will need hiring new staff this fall."], 0), (["We must improve our productivity.", "We must to improve our productivity."], 0)]
exercise('hw-1', 'HW1 – Mark the Correct Sentences', 'hw', 'HW1 — Which sentence is correct?', 'Mark the sentences that are correct.',
         [pick_row(i + 1, o, o[a], 'hw1-%d' % (i + 1)) for i, (o, a) in enumerate(H1)], 'circ',
         example=pick_example(["Peter has to stop working during lunch.", "Peter has stop working during lunch."], "Peter has to stop working during lunch."), gid='hw1', aud=AL.pb_clips(5, 1, 10))

# ---- Practice Book 5.2 (listening): True / False / Not given
_p52 = [('Janice&rsquo;s presentation is about marketing.', 'False'), ('She hasn&rsquo;t reserved a meeting room yet.', 'True'), ('Janice wants James to reserve a small room.', 'False'),
        ('She doesn&rsquo;t need a projector or sound system.', 'False'), ('Janice needs the room from 2:30 to 5pm.', 'False'), ('Janice wants James to email the team.', 'Not given'),
        ('James should order refreshments for the break.', 'True'), ('Janice wants James to check the visuals.', 'True'), ('Janice invites James for lunch to say thank you.', 'Not given')]
exercise('hw-L', 'HW2 – Listening: True or False', 'hw', 'HW2 — Listen and answer', 'Listen to the audio and answer the questions.',
         [tf_row(i + 1, t, a, 'hwL-%d' % (i + 1)) for i, (t, a) in enumerate(_p52)], 'circ',
         example=tf_example('Janice is giving a presentation on Wednesday.', 'False'), pre=AL.pb_single(5, 2) + '<p class="instruction">A manager, Janice, is giving tasks to her assistant, James.</p>', gid='hwL')


W3 = [("Would you give Peter a copy of the minutes, please?", ['copy', 'you', 'minutes,', 'of', 'please?', 'give', 'the', 'Would', 'Peter', 'a']),
      ("All visitors must leave their passes at reception.", ['at', 'leave', 'reception.', 'passes', 'All', 'their', 'must', 'visitors']),
      ("Could you take this letter to the post office, please?", ['the', 'post', 'to', 'office,', 'please?', 'this', 'take', 'Could', 'letter', 'you']),
      ("Ramon needs to work harder if he wants a promotion.", ['harder', 'Ramon', 'to', 'if', 'work', 'he', 'a promotion.', 'needs', 'wants']),
      ("Sharon needs to sign up for the training course.", ['needs', 'the', 'Sharon', 'sign up', 'training', 'for', 'course.', 'to']),
      ("Could you leave a copy of the agenda on my desk, please?", ['copy', 'you', 'of', 'Could', 'on', 'leave a', 'agenda', 'the', 'please?', 'my desk,']),
      ("You must complete the enrolment form before 5pm on Friday.", ['enrolment', 'before', 'You', 'complete', 'must', 'the', 'on', 'Friday.', 'form', '5pm']),
      ("Staff must not smoke inside the building.", ['inside', 'smoke', 'Staff', 'the', 'must', 'building.', 'not']),
      ("Would you send an email to everyone about the meeting?", ['everyone', 'Would', 'you', 'an email', 'to', 'the', 'send', 'meeting?', 'about']),
      ("You must finish the project by Wednesday evening.", ['the', 'by', 'finish', 'You', 'project', 'must', 'evening.', 'Wednesday'])]
exercise('hw-2', 'HW3 – Word Order', 'hw', 'HW3 — Put the words in order', 'Rewrite the sentences, putting the words in the correct order.',
         [order_row(i + 1, w, a) for i, (a, w) in enumerate(W3)], 'typed',
         example=order_example(['have', 'before', 'to', 'the', 'We', 'presentation', '5pm.', 'finish'], 'We have to finish the presentation before 5pm.'), gid='hw2', aud=AL.pb_clips(5, 3, 10))

l4 = [mrow('left', 'x', 'Staff must wear', example=True), mrow('left', 1, 'The company must change', 1), mrow('left', 2, 'I need you to finish', 2), mrow('left', 3, 'Could you keep a', 3),
      mrow('left', 4, 'Would you inform', 4), mrow('left', 5, 'The company has got to', 5), mrow('left', 6, 'You don\'t have', 6), mrow('left', 7, 'We need to think', 7)]
r4 = [mrow('right', 1, 'if it wants to survive.'), mrow('right', 3, 'record of everything you spend this week?'), mrow('right', 'x', 'identity cards at all times in the building.', example=True),
      mrow('right', 4, 'the team about the recent changes, please?'), mrow('right', 2, 'the presentation by Friday.'), mrow('right', 7, 'about closing some of our branches.'),
      mrow('right', 5, 'invest more in training.'), mrow('right', 6, 'to finish the assignment today.')]
match_exercise('hw-3', 'HW4 – Match the Endings', 'hw', 'HW4 — Beginnings and endings', 'Match the beginnings of the sentences to the correct endings. Click one on the left, then one on the right.', l4, r4, aud=AL.pb_clips(5, 4, 7))

TIPS = article('Daily Office Tips', 'A problem shared&hellip; can be a problem halved', None, [
    "Getting your fellow team members involved in your daily tasks makes life easier for everyone, surely? But only when you know how to delegate effectively. In my experience, I've found it helps if you think about these four simple steps:",
    "<b>1</b> You need to think about who you're delegating to. Are they the best person for the job? What will they give, and what will they learn?",
    "<b>2</b> You don't have to follow your team's every step or decision. But you should be communicative and offer advice. A supported team is an effective team.",
    "<b>3</b> You must set a clear deadline. Everyone needs to know when the project should end. Otherwise your project will lose its momentum.",
    "<b>4</b> You have to offer your team feedback. Everyone appreciates credit for success, but they also want to know what went wrong."])
H5 = [("You should think about who to delegate to.", 'True'), ("You should follow your team's every step.", 'False'), ("You should organize team-building activities.", 'Not given'),
      ("Deadlines should always be flexible.", 'False'), ("Your team won't appreciate negative feedback.", 'False')]
exercise('hw-4', 'HW5 – Read and Answer', 'hw', 'HW5 — A problem shared', 'Read the article and answer the questions.',
         [tf_row(i + 1, t, a, 'hw4-%d' % (i + 1)) for i, (t, a) in enumerate(H5)], 'circ',
         example=tf_example('The author says delegating is always effective.', 'False'), pre=TIPS, gid='hw4')

def resp_row(n, prompt, pre, ans, post):
    return '<div class="ex-row"><span class="circ-num">%d</span><span style="color:var(--muted);">%s</span><br><span style="margin-left:34px;display:inline-block;margin-top:4px;">%s %s %s</span></div>' % (n, prompt, pre, wb_blank(ans), post)
R6 = [("Is this presentation high priority?", "No, I", "don't need", "you to finish it today."), ("Is it OK if I hand in the report next week?", "I'm sorry, Mike. We really", "must", "have it by Friday."),
      ("Can we look around the factory?", "I'm sorry, but members of the public", "must not", "enter the building."), ("The new uniforms still haven't arrived.", "We need them tomorrow.", "Could", "you call the supplier, please?"),
      ("Do you want me to stay late tonight?", "No, you", "don't have", "to. The deadline is next week."), ("I'm afraid I still haven't finished the report.", "Well, I", "need", "it by 1pm today.")]
exercise('hw-5', 'HW6 – Respond', 'hw', 'HW6 — Respond', 'Read each statement, then respond out loud, filling in the gaps using the words in the panel. Click a word, then click a gap.',
         [resp_row(i + 1, a, b, c, d) for i, (a, b, c, d) in enumerate(R6)], 'wb',
         example=ex_given('%s<span style="color:var(--muted);">I just received Eric\'s memo about the conference.</span><br><span style="margin-left:34px;display:inline-block;margin-top:4px;">Great. <span class="wb-blank filled is-example" data-ans="Would">Would</span> you print me a copy, please?</span>' % example_badge()),
         pre=wb_bank(["don't have", 'need', 'Would', 'must', "don't need", 'Could', 'must not'], 'Would'), gid='hw5', aud=AL.pb_clips(5, 6, 6))
