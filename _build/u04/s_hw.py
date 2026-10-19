# -*- coding: utf-8 -*-
# Practice Book homework (with PB supporting audio and listening exercises)
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'shared'))
from lib import *
from ex import *
hw_cover('Talking about changes')

H1 = [(["Claude is used to working weekends.", "Claude is used to work weekends."], 0), (["Did Paul use to work in San Francisco?", "Did Paul used to work in San Francisco?"], 0),
      (["I am not use to working in such heat.", "I am not used to working in such heat."], 1), (["The team used to go out for lunch.", "The team used to going out for lunch."], 0),
      (["We didn't used to have so many meetings.", "We didn't use to have so many meetings."], 1), (["I used to living in a house near the office.", "I used to live in a house near the office."], 1),
      (["Did you use to work in Paris?", "Did you used to work in Paris?"], 0), (["I'm used to the new software now.", "I'm use to the new software now."], 0),
      (["I'll never get use to this operating system.", "I'll never get used to this operating system."], 1), (["Kerry is used to commuting a long way.", "Kerry is used to commute a long way."], 0)]
exercise('hw-1', 'HW1 – Mark the Correct Sentences', 'hw', 'HW1 — Which sentence is correct?', 'Mark the sentences that are correct.',
         [pick_row(i + 1, o, o[a], 'hw1-%d' % (i + 1)) for i, (o, a) in enumerate(H1)], 'circ',
         example=pick_example(["Paula is used to talking in front of crowds.", "Paula is use to talking in front of crowds."], "Paula is used to talking in front of crowds."), gid='hw1', aud=AL.pb_clips(4, 1, 10))

# ---- Practice Book 4.2 (listening): number the pictures in the order they are described
_p42 = [('A', 'A woman standing at a train station', '7'), ('C', 'A woman working at a desk in an office', '5'), ('D', 'A woman bowling', '6'),
        ('E', 'A person relaxing on a lounge chair at the beach', '2'), ('F', 'A woman eating lunch at a table', '4'), ('G', 'A person with an umbrella in the rain', '3')]
exercise('hw-L', 'HW2 – Listening: Number the Pictures', 'hw', 'HW2 — Listen and number', 'Listen to the audio, then number the pictures in the order they are described.',
         [pic_num_row(l, t, a) for l, t, a in _p42], 'typed',
         example=pic_num_example('B', 'Cars driving in traffic', '1'), pre=AL.pb_single(4, 2), gid='hwL')


W3 = [("We didn't use to have so much free time.", ['to', 'time.', 'We', 'use', "didn't", 'so', 'have', 'free', 'much']),
      ("I'll never get used to driving on the left.", ['get', 'the', 'used', 'on', 'to', 'never', "I'll", 'left.', 'driving']),
      ("Did Anthony use to work in the Frankfurt branch?", ['to', 'branch?', 'use', 'Anthony', 'work', 'Did', 'in', 'the', 'Frankfurt']),
      ("I am used to having to get up at 6am.", ['get up', 'to', 'I', 'to', 'am', 'having', '6am.', 'used', 'at']),
      ("Derek isn't used to commuting so far to work.", ['used', 'Derek', 'to', "isn't", 'so', 'work.', 'commuting', 'far', 'to']),
      ("The team hasn't got used to the new operating system.", ['got', 'new', 'The', "hasn't", 'to', 'the', 'team', 'system.', 'used', 'operating']),
      ("We used to have lunch in the café near the park.", ['lunch', 'near', 'used', 'the', 'We', 'to', 'in', 'café', 'park.', 'have', 'the']),
      ("Danielle isn't used to giving presentations.", ['giving', 'Danielle', "isn't", 'presentations.', 'to', 'used']),
      ("Pam used to work in the branch in Cologne.", ['to', 'Pam', 'in', 'branch', 'used', 'work', 'the', 'Cologne.', 'in']),
      ("Phil isn't used to wearing a uniform for work.", ['uniform', 'Phil', 'used', 'a', 'to', "isn't", 'work.', 'wearing', 'for'])]
exercise('hw-2', 'HW3 – Word Order', 'hw', 'HW3 — Put the words in order', 'Rewrite the sentences, putting the words in the correct order.',
         [order_row(i + 1, w, a) for i, (a, w) in enumerate(W3)], 'typed',
         example=order_example(['working', 'Peter', 'used', 'from', 'to', 'home.', 'is'], 'Peter is used to working from home.'), gid='hw2', aud=AL.pb_clips(4, 3, 10))

l4 = [mrow('left', 'x', 'I worked in a bank in the past.', example=True), mrow('left', 1, 'She doesn\'t usually work long hours.', 1), mrow('left', 2, 'In the past I was a doctor.', 2),
      mrow('left', 3, 'Dan\'s driven on the left for years.', 3), mrow('left', 4, 'She began getting up early 10 years ago.', 4), mrow('left', 5, 'I tried Indian food once. It\'s spicy!', 5),
      mrow('left', 6, 'I still hate the weather in England after 20 years.', 6), mrow('left', 7, 'I don\'t usually work this late.', 7), mrow('left', 8, 'We\'ve had our new boss for three months.', 8)]
r4 = [mrow('right', 1, 'She\'s not used to working long hours.'), mrow('right', 2, 'I used to work as a doctor.'), mrow('right', 'x', 'I used to work in a bank.', example=True),
      mrow('right', 4, 'She\'s used to getting up early.'), mrow('right', 5, 'I\'m not used to spicy food.'), mrow('right', 3, 'Dan\'s used to driving on the left.'),
      mrow('right', 7, 'I\'m not used to working so late.'), mrow('right', 8, 'We\'re getting used to the new boss.'), mrow('right', 6, 'I\'ll never get used to English weather.')]
match_exercise('hw-3', 'HW4 – Phrases That Mean the Same', 'hw', 'HW4 — Same meaning', 'Match the pairs of phrases that mean the same thing. Click one on the left, then one on the right.', l4, r4, aud=AL.pb_clips(4, 4, 8))

def reply_row(n, q, opts, ans, g):
    b = ''.join('<button class="circ-opt block" data-group="%s" data-correct="%s" onclick="circPick(this)">%s</button>' % (g, esc(ans), o) for o in opts)
    return '<div class="ex-row"><span class="circ-num">%d</span><span class="pick-wrap"><b>%s</b>%s</span></div>' % (n, q, b)
R5 = [("Would you like some coffee?", ["No, thanks. I'm fine.", "I'm used to drinking tea."], "No, thanks. I'm fine."),
      ("You look exhausted, Jenny.", ["I'm not used to this hot weather!", "I will sleep later."], "I'm not used to this hot weather!"),
      ("Would you like to go for lunch?", ["I'm not used to invitations.", "That would be great!"], "That would be great!"),
      ("Have you seen that new movie?", ["I haven't yet. Is it any good?", "Thanks. Tomorrow would be good."], "I haven't yet. Is it any good?"),
      ("How was your commute?", ["I hate public transportation.", "I'm getting used to the traffic."], "I'm getting used to the traffic.")]
exercise('hw-4', 'HW5 – Best Reply', 'hw', 'HW5 — Choose the best reply', 'Mark the best reply to each statement.',
         [reply_row(i + 1, q, o, a, 'hw4-%d' % (i + 1)) for i, (q, o, a) in enumerate(R5)], 'circ',
         example=ex_given('%s<span class="pick-wrap"><b>Are you getting used to your new job?</b><span class="circ-opt block is-example">Yes, but there\'s a lot to remember.</span><span class="circ-opt block struck">Of course I am.</span></span>' % example_badge()), gid='hw4', aud=AL.pb_clips(4, 5, 5))

C6 = [("Are you", ['used to', 'got used to'], 'used to', "living in a tropical country yet?"), ("I", ['was used to', 'used to'], 'used to', "travel to work on foot before they built the metro."),
      ("When I lived in Berlin, we", ['used to', 'get used to'], 'used to', "live in an apartment downtown."), ("", ['Were you used to', 'Did you use to'], 'Did you use to', "work in the Edinburgh branch?"),
      ("I grew up in Japan, so I'm", ['used to', 'got used to'], 'used to', "driving on the left."), ("Arnold's", ['used to', 'use to'], 'used to', "waking up at 5am every morning."),
      ("I", ['used to', 'am used to'], 'am used to', "working for a demanding boss."), ("When I was a child, I didn't", ['get used to', 'use to'], 'use to', "like going to school."),
      ("We", ['are used to', 'used to'], 'used to', "go to Florida each year on vacation."), ("My father", ['used to', 'getting used to'], 'used to', "work in a factory until it closed down.")]
exercise('hw-5', 'HW6 – Choose, Then Say It', 'hw', 'HW6 — Choose, then say it', 'Cross out the incorrect words in each sentence, then say the sentences out loud.',
         [co_row(i + 1, p, c, a, post, 'hw5-%d' % (i + 1), say=True) for i, (p, c, a, post) in enumerate(C6)], 'circ',
         example=co_example('I took a while to', ['get used to', 'am used to'], 'get used to', 'the weather here.'), gid='hw5', aud=AL.pb_clips(4, 6, 10))
