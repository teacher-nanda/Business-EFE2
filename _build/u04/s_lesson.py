# -*- coding: utf-8 -*-
# Unit 4 "Talking about changes" — lesson slides.  Theme: then and now.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'shared'))
from lib import *
from ex import *
import audiolib as AL
U = '4'

cover(4, 'Talking about changes', ["Staff used to eat lunch at their desks.", "It took a while to get used to the commute.", "Nowadays I am used to waking up early.", "Did you use to work in London?"])

content('s-lead', 'Warm-Up – Then and Now', 'leadin', 'Then and now', '''
    <div class="lead-grid">
      <div class="bd-form">
        <label for="tn-1">Five years ago, you&hellip;</label><input id="tn-1" data-live="then" maxlength="48" autocomplete="off">
        <label for="tn-2">Today, you&hellip;</label><input id="tn-2" data-live="now" maxlength="48" autocomplete="off">
        <label for="tn-3">A change you still find difficult</label><input id="tn-3" data-live="hard" maxlength="48" autocomplete="off">
        <label for="tn-4">A change you have enjoyed</label><input id="tn-4" data-live="good" maxlength="48" autocomplete="off">
      </div>
      <div class="profile-card">
        <div class="pc-h">Then and now</div>
        <div class="pc-row"><span class="pc-k">Then</span><span class="pc-v" data-bd="then">&nbsp;</span></div>
        <div class="pc-row"><span class="pc-k">Now</span><span class="pc-v" data-bd="now">&nbsp;</span></div>
        <div class="pc-row"><span class="pc-k">Difficult</span><span class="pc-v" data-bd="hard">&nbsp;</span></div>
        <div class="pc-row"><span class="pc-k">Enjoyed</span><span class="pc-v" data-bd="good">&nbsp;</span></div>
      </div>
    </div>''', 'There are many ways to talk about changes at work. Fill in your own changes, then tell me about them.')

# ---- 4.1 / 4.2 MEANING: used to / get used to / be used to
UT, GU, BU = 'used to', 'get used to', 'be used to'
sort_slide('s-m1', 'Meaning – Used To, Get Used To, Be Used To', 'grammar', 'Three meanings of &ldquo;used to&rdquo;',
           'Click a sentence, then click the box where it belongs.',
           [("Staff used to eat lunch at their desks.", UT), ("It took a while to get used to the commute.", GU), ("Nowadays I am used to waking up early.", BU),
            ("Did you use to do everything by hand in the factory?", UT), ("I don't know that I will ever get used to these uniforms!", GU),
            ("After working here for a decade, we are used to the noise.", BU), ("We didn't use to have so much construction in the area.", UT)],
           [(UT, '<b>used to + infinitive</b><br>a regular habit or state in the past'), (GU, '<b>get used to</b><br>the process of becoming familiar with something'),
            (BU, '<b>be used to</b><br>being familiar with something')],
           post=ccqs(('&ldquo;Staff used to eat lunch at their desks.&rdquo; Do they still do it?', 'No. It was a habit in the past, but it is not true now.'),
                     ('&ldquo;It took a while to get used to the commute.&rdquo; Is the commute strange now?', 'No. At first it was strange, but the speaker became familiar with it.')),
           aud='<div class="audio-box clips-box"><span class="clips-label">🎧 Listen</span>%s%s</div>' % (AL.word(U, '4_1', 'key language'), AL.word(U, '4_2', 'further examples')))

content('s-g1', 'Grammar – Form', 'grammar', 'How we build them', '''
    <div class="form-grid">
      <div class="form-card"><h4>used to + infinitive</h4>
        <div class="form-row"><span class="fr-k">Positive</span><span class="fr-v">Staff <b>used to eat</b> lunch at their desks.</span></div>
        <div class="form-row"><span class="fr-k">Negative</span><span class="fr-v">We <b>didn't use to have</b> so much construction.</span></div>
        <div class="form-row"><span class="fr-k">Question</span><span class="fr-v"><b>Did</b> you <b>use to do</b> everything by hand?</span></div>
        <p style="margin:6px 0 0;color:var(--muted);">In questions and negatives, there is no &ldquo;d&rdquo; after &ldquo;use.&rdquo;</p></div>
      <div class="form-card cont"><h4>get used to / be used to</h4>
        <div class="form-row"><span class="fr-k">get used to</span><span class="fr-v">I will <b>get used to</b> <i>the commute</i> / <i>commuting</i>.</span></div>
        <div class="form-row"><span class="fr-k">be used to</span><span class="fr-v">I <b>am used to</b> <i>early mornings</i> / <i>waking up early</i>.</span></div>
        <p style="margin:6px 0 0;color:var(--muted);">After &ldquo;get used to&rdquo; and &ldquo;be used to,&rdquo; use a noun or a gerund (&ldquo;-ing&rdquo;).</p></div>
    </div>
    <div class="two-up" style="margin-top:12px;">%s%s</div>''' % (
        reveal_card('Which is correct: &ldquo;I used to commuting&rdquo; or &ldquo;I used to commute&rdquo;?', '&ldquo;I used to commute.&rdquo; After &ldquo;used to&rdquo; (the habit) we use the infinitive.'),
        reveal_card('Which is correct: &ldquo;I am used to commute&rdquo; or &ldquo;I am used to commuting&rdquo;?', '&ldquo;I am used to commuting.&rdquo; After &ldquo;be used to&rdquo; we use a noun or a gerund.')))

# ---- CB 4.3
O3 = [(["I use to travel to work by car.", "I used to travel to work by car."], "I used to travel to work by car."),
      (["She's used to giving big presentations.", "She's used to give big presentations."], "She's used to giving big presentations."),
      (["I'll get used to my new job eventually.", "I get used to my new job eventually."], "I'll get used to my new job eventually."),
      (["We didn't used to get paid a bonus.", "We didn't use to get paid a bonus."], "We didn't use to get paid a bonus."),
      (["Did he use to work in marketing?", "Did he used to work in marketing?"], "Did he use to work in marketing?")]
exercise('s-cb43', 'Grammar – Mark the Correct Sentences', 'grammar', 'Which sentence is correct?', 'Mark the sentences that are correct.',
         [pick_row(i + 1, o, a, 'cb43-%d' % (i + 1)) for i, (o, a) in enumerate(O3)], 'circ',
         example=pick_example(["He is used to working from home.", "He is use to working from home."], "He is used to working from home."),
         aud=AL.clips(U, '4_3', 5), gid='cb43')

# ---- CB 4.4 listening: number the pictures
PICS = [('A', 'A man in a suit points at a no-smoking sign while a woman at her desk looks at him.', '2'),
        ('C', 'A man in an orange shirt shows a woman where a door is.', '4'),
        ('D', 'A woman carrying a bag looks at a clock.', '3')]
def num_row(letter, desc, ans, g):
    b = ''.join('<button class="circ-opt" data-group="%s" data-correct="%s" onclick="circPick(this)">%s</button>' % (g, ans, n) for n in '1234')
    return '<div class="ex-row"><span class="circ-num">%s</span>%s<br><span style="margin-left:34px;display:inline-block;margin-top:6px;">%s</span></div>' % (letter, pic('Picture %s: %s' % (letter, desc)), b)
exercise('s-cb44', 'Listening – Number the Pictures', 'listening', 'Number the pictures', 'Listen to the audio, then number the pictures in the order they are described.',
         [num_row(l, d, a, 'cb44-%s' % l) for l, d, a in PICS], 'circ',
         example=ex_given('<span class="example-badge">✓</span>%s<br><span style="margin-left:34px;display:inline-block;margin-top:6px;"><span class="circ-opt is-example">1</span> <span class="circ-opt struck">2</span> <span class="circ-opt struck">3</span> <span class="circ-opt struck">4</span></span>' % pic('Picture B: A woman on the phone at a counter, with three clocks on the wall.')),
         pre=AL.single(U, '4_4', top=True), gid='cb44')

# ---- CB 4.5
W5 = [("We used to finish at noon on Fridays.", ['on', 'used', 'finish', 'Fridays.', 'at', 'We', 'to', 'noon']),
      ("She didn't use to be so serious.", ['serious.', "didn't", 'to', 'She', 'be', 'use', 'so']),
      ("I am used to working for a strict boss.", ['strict', 'am', 'boss.', 'used', 'working', 'I', 'for', 'to', 'a']),
      ("Did you use to work in London?", ['to', 'London?', 'work', 'you', 'Did', 'use', 'in'])]
exercise('s-cb45', 'Grammar – Word Order', 'grammar', 'Put the words in order', 'Rewrite the sentences, putting the words in the correct order.',
         [order_row(i + 1, w, a) for i, (a, w) in enumerate(W5)], 'typed',
         example=order_example(['to', 'here?', 'get', 'Will', 'used', 'we', 'living', 'ever'], 'Will we ever get used to living here?'),
         aud=AL.clips(U, '4_5', 4), gid='cb45')

speak('s-sp1', 'Speaking Break – Then and Now', 'Speaking break: then and now', 'Talk to your teacher about change at work. Use &ldquo;used to&rdquo; and &ldquo;get used to&rdquo;. Click the button when you have said it.', [
    'What did you use to do in your first job that you do not do now?',
    'What was difficult to get used to when you started your current job?',
    'What is something at work that you are used to now, but that was new to you before?',
    'Ask your teacher: &ldquo;What did you use to do at work that you do not do now?&rdquo;'])

# ---- PRONUNCIATION
content('s-pron', 'Pronunciation – Used To', 'pron', 'Say it smoothly', '''
    <p class="instruction">Listen to your teacher. Then say each sentence. The highlighted words are stronger and clearer.</p>
    %s%s%s%s
    <div class="gram-note">🔊 The &ldquo;d&rdquo; in &ldquo;used to&rdquo; is not heard: it sounds like &ldquo;use-ta&rdquo; /juːstə/. After &ldquo;did&rdquo; and &ldquo;didn't,&rdquo; we say &ldquo;use to&rdquo; /juːs tə/.</div>''' % (
    say_line('Staff %s to %s lunch at their %s.' % (St('used'), St('eat'), St('desks')), ),
    say_line('I\'m %s to %s %s.' % (St('used'), St('waking'), St('up early')) ),
    say_line('%s you %s to work in %s?' % (St('Did'), St('use'), St('London')) ),
    say_line('We %s %s to have so much %s.' % (St('didn\'t'), St('use'), St('construction'))) ))

# ---- CB 4.6 MATCH
l6 = [mrow('left', 'x', 'I was a bank employee in the past.', example=True),
      mrow('left', 1, 'I began working long days early in my career.', 1), mrow('left', 2, 'He is a qualified lawyer now.', 2), mrow('left', 3, 'I don\'t usually work short days.', 3),
      mrow('left', 4, 'Your working day was shorter in the past.', 4), mrow('left', 5, 'Has he worked in a bank before?', 5)]
r6 = [mrow('right', 5, 'Did he use to work in a bank?'), mrow('right', 'x', 'I used to work in a bank.', example=True), mrow('right', 4, 'You didn\'t use to work such long hours.'),
      mrow('right', 3, 'I am used to working long hours.'), mrow('right', 2, 'He didn\'t use to have a law degree.'), mrow('right', 1, 'I got used to long hours in my first job.')]
match_exercise('s-cb46', 'Grammar – Phrases That Mean the Same', 'grammar', 'Same meaning', 'Match the pairs of phrases that mean the same thing. Click one on the left, then one on the right.', l6, r6, aud=AL.clips(U, '4_6', 5))

# ---- CB 4.7 READING
TALK = article('Workplace advice', "It's good to talk", 'Small talk&mdash;chatting about trivial topics such as the weather', [
    "&ldquo;Morning, Sammy. Did you see the game last night?&rdquo; This kind of small talk happens in every office around the world, every day. People who make an effort to talk to others are more well-liked by their colleagues. When you make small talk, you make the other person feel more relaxed, and form a connection with that person. People who are good at small talk tend to be quick thinkers, and businesses like employees who can think on their feet.",
    "So what are the key skills you need to master to be good at small talk? Make eye contact with the other person, and listen. Be interested in what they have to say. Stick to topics such as hobbies, books, films, and the weather. And avoid uncomfortable topics such as politics, religion, and money."])
content('s-cb47a', 'Reading – It\'s Good to Talk', 'reading', "It's good to talk",
        '<div class="ph-small">%s</div>%s' % (ph('📖', 'Photo: an open book'), TALK), 'Look at the title and the picture first. What do you think the article says? Then read it.')
T7 = [("Being good at small talk can give you an advantage in your job.", 'True'), ("Sports are the most common topic for small talk.", 'Not given'),
      ("People who are good at small talk are generally disliked.", 'False'), ("When talking to a colleague, don't look at their face.", 'False'),
      ("Not every topic is suitable for small talk.", 'True')]
exercise('s-cb47b', 'Reading – True, False, Not Given', 'reading', 'What does the article say?', 'Read the article and answer the questions.',
         [tf_row(i + 1, t, a, 'cb47-%d' % (i + 1)) for i, (t, a) in enumerate(T7)], 'circ',
         example=tf_example('Weather is a common topic for small talk.', 'True'), pre='<div style="margin-bottom:14px;">%s</div>' % article_toggle('cb47-art', TALK), gid='cb47')

# ---- CB 4.8 BEST REPLY
R8 = [("You look tired.", ["I feel really hungry.", "I'm not used to starting at 6am!"], "I'm not used to starting at 6am!"),
      ("Did you see the game last night?", ["I enjoy watching films.", "Yes, what a disappointment!"], "Yes, what a disappointment!"),
      ("Would you like some of this pizza?", ["I didn't use to like it.", "Yes, please. It looks delicious."], "Yes, please. It looks delicious."),
      ("It takes me 20 minutes to get to work.", ["That's a very short commute!", "It's more expensive by train."], "That's a very short commute!"),
      ("The sky looks black outside.", ["Yes, I think it's going to rain.", "I'm going away this weekend."], "Yes, I think it's going to rain.")]
def reply_row(n, q, opts, ans, g):
    b = ''.join('<button class="circ-opt block" data-group="%s" data-correct="%s" onclick="circPick(this)">%s</button>' % (g, esc(ans), o) for o in opts)
    return '<div class="ex-row"><span class="circ-num">%d</span><span class="pick-wrap"><b>%s</b>%s</span></div>' % (n, q, b)
exercise('s-cb48', 'Speaking – Best Reply', 'speaking', 'Choose the best reply', 'Mark the best reply to each statement.',
         [reply_row(i + 1, q, o, a, 'cb48-%d' % (i + 1)) for i, (q, o, a) in enumerate(R8)], 'circ',
         example=ex_given('%s<span class="pick-wrap"><b>I\'m not used to this heat!</b><span class="circ-opt block is-example">Would you like something to drink?</span><span class="circ-opt block struck">Good afternoon, Mrs. Sullivan.</span></span>' % example_badge()),
         aud=AL.clips(U, '4_8', 5), gid='cb48')

# ---- CB 4.9
C9 = [("When I was young, I", ["didn't use to", "wasn't use to"], "didn't use to", "like mushrooms."),
      ("My grandfather", ['used to', 'got used to'], 'used to', "walk four miles to school every morning."),
      ("Are you", ['used to', 'got used to'], 'used to', "your new job yet?"),
      ("I grew up in Florida, so I", ['used to', 'am used to'], 'am used to', "the heat."),
      ("We", ['used to', 'were used to'], 'used to', "go to the south of France every year.")]
exercise('s-cb49', 'Speaking – Choose, Then Say It', 'speaking', 'Choose, then say it', 'Cross out the incorrect words in each sentence, then say the sentences out loud.',
         [co_row(i + 1, p, c, a, post, 'cb49-%d' % (i + 1), say=True) for i, (p, c, a, post) in enumerate(C9)], 'circ',
         example=co_example('When I lived there, I', ['used to', 'was used to'], 'used to', 'have breakfast in a café every morning.'),
         aud=AL.clips(U, '4_9', 5), gid='cb49')

freer('s-free', 'Speaking – Small Talk', 'Small talk card', 'Your teacher is a colleague. Take a card, then make small talk. Stick to safe topics: hobbies, books, films and the weather.', 'Small talk card')
review([('&ldquo;Used to,&rdquo; &ldquo;be / get used to&rdquo;', '⚙️'), ('Small talk', '☕'), ('Talking about changes at work', '🧩')], 'Before you leave',
       'Tell me about two changes in your working life, one from the past and one you are still getting used to.')
