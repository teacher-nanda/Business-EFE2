# -*- coding: utf-8 -*-
# Practice Book homework (with PB supporting audio and listening exercises)
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'shared'))
from lib import *
from ex import *
import aihw

hw_cover('Getting to know colleagues')

H1 = [(["I was preparing for the presentation.", "I was prepare for the presentation."], 0),
      (["Did Greg work in the New York branch?", "Did Greg working in the New York branch?"], 0),
      (["Akira was living in Kyoto in 1998.", "Akira was live in Kyoto in 1998."], 0),
      (["I didn't understanding the presentation.", "I didn't understand the presentation."], 1),
      (["Pete was reading a book at 9pm yesterday.", "Pete read a book at 9pm yesterday."], 0),
      (["I was feeling exhausted at work, so I left.", "I was feel exhausted at work, so I left."], 0),
      (["Did you enjoy the presentation?", "Did you enjoyed the presentation?"], 0),
      (["Were you worked in IT then?", "Were you working in IT then?"], 1),
      (["Kai wasn't feeling well, so he went home.", "Kai didn't feeling well, so he went home."], 0),
      (["I was finding a new job in France.", "I found a new job in France."], 1)]
exercise('hw-1', 'HW1 – Mark the Correct Sentences', 'hw', 'HW1 — Which sentence is correct?', 'Mark the sentences that are correct.',
         [pick_row(i + 1, o, o[a], 'hw1-%d' % (i + 1)) for i, (o, a) in enumerate(H1)], 'circ',
         example=pick_example(["Jan was to look for another job.", "Jan was looking for another job."], "Jan was looking for another job."), gid='hw1', aud=AL.pb_clips(2, 1, 10))

# ---- Practice Book 2.2 (listening): number the pictures in the order they are described
_p22 = [('A', 'Two people having dinner in a restaurant while a waiter serves them', '6'), ('C', 'A speaker presenting a chart to an audience', '5'),
        ('D', 'A man with a suitcase next to a car, an airplane overhead, and two people waving', '7'), ('E', 'Three people walking and greeting each other near a large building', '4'),
        ('F', 'The Arc de Triomphe in Paris', '3'), ('G', 'The Eiffel Tower seen through a window', '2'), ('H', 'A person sitting on a sofa, pointing at the TV', '8')]
exercise('hw-L', 'HW2 – Listening: Number the Pictures', 'hw', 'HW2 — Listen and number', 'Listen to the audio, then number the pictures in the order they are described.',
         [pic_num_row(l, t, a) for l, t, a in _p22], 'typed',
         example=pic_num_example('B', 'A hotel building with a man standing in front of it', '1'), pre=AL.pb_single(2, 2), gid='hwL')


H3 = [("Daniel", 'has worked', 'work', "for more than five different law firms."), ("I", 'have taken', 'take', "the bus to work all my working life."),
      ("The company", 'has employed', 'employ', "five new people since September."), ("Peter is a terrible waiter. He", 'has started', 'start', "looking for a different job."),
      ("Andrea", 'has worked', 'work', "here since she graduated in 1999."), ("The factory", 'has produced', 'produce', "15,000 machines this year."),
      ("Tim's really happy. He", 'has finished', 'finish', "his presentation for tomorrow."), ("We", 'have sold', 'sell', "our products in more than 25 countries."),
      ("I", 'have walked', 'walk', "to work since my car broke down."), ("I", 'have decided', 'decide', "that I'm going to retire next year."),
      ("Dave", 'has taken', 'take', "more time than we expected."), ("I", 'have worked', 'work', "at this office for more than 25 years now."),
      ("Chris", 'has visited', 'visit', "more than 50 countries so far.")]
exercise('hw-2', 'HW3 – Fill in the Gaps', 'hw', 'HW3 — Present perfect simple', 'Fill in the gaps by putting the verbs in the present perfect simple.',
         [gap_row(i + 1, p, a, v, post) for i, (p, a, v, post) in enumerate(H3)], 'typed',
         example=gap_example("Chloe", "has bought", 'buy', "a new apartment in Paris."), gid='hw2', aud=AL.pb_clips(2, 3, 13))

left = [mrow('left', 'x', 'Claire was working at a bank', example=True),
        mrow('left', 1, 'Jim was preparing a presentation', 1), mrow('left', 2, 'I\'ve worked at this company', 2), mrow('left', 3, 'Chris had to wait for a taxi for', 3),
        mrow('left', 4, 'Tim moved to New York', 4), mrow('left', 5, 'I ran my own software company', 5), mrow('left', 6, 'In 2013, our company', 6)]
right = [mrow('right', 2, 'for more than ten years.'), mrow('right', 3, 'more than an hour.'), mrow('right', 'x', 'when she received a new job offer.', example=True),
         mrow('right', 1, 'when his boss entered the room.'), mrow('right', 5, 'before I started working here.'), mrow('right', 6, 'bought a smaller Canadian software firm.'),
         mrow('right', 4, 'when he was transferred to the US office.')]
match_exercise('hw-3', 'HW4 – Match the Endings', 'hw', 'HW4 — Beginnings and endings', 'Match the beginnings of the sentences to the correct endings. Click one on the left, then one on the right.', left, right, aud=AL.pb_clips(2, 4, 6))

BLOG = article('Silvia\'s Blog', 'On the up!', 'Posted Friday, 7:30am', [
    "I've just started my new job at Moda Fashions in Edinburgh. I've worked for three different employers so far, and I'm hoping that this job will be the best I've had.",
    "My first job was in a local supermarket. I hated it. I was bored, I had no responsibilities, and the customers were often rude to me. I left after only three months.",
    "After that, I worked in a bar. It was more interesting and I met some interesting people. I was studying for my business diploma while I worked there, so I had something to dream about.",
    "Then I started to become interested in fashion. I was working as an intern for a small fashion agency when I received my job offer. I'm so excited."])
H4 = [("Silvia has worked for three different employers so far.", 'True'), ("Her first job was boring.", 'True'), ("She worked there for six months.", 'False'),
      ("Silvia worked in a bar while she was studying.", 'True'), ("She only worked in the evenings.", 'Not given'), ("She was working as an intern until recently.", 'True')]
exercise('hw-4', 'HW5 – Read and Answer', 'hw', 'HW5 — Silvia\'s blog', 'Read the article and answer the questions.',
         [tf_row(i + 1, t, a, 'hw4-%d' % (i + 1)) for i, (t, a) in enumerate(H4)], 'circ',
         example=tf_example('Silvia has just started work for a bank.', 'False'), pre=BLOG, gid='hw4')

H5 = [("At 3pm yesterday, I", ['discussed', 'was discussing'], 'was discussing', "the new software with our IT team."),
      ("While Susan", ['has eaten', 'was eating'], 'was eating', "lunch, her team was working hard."),
      ("Karl moved to Berlin when he", ['lost', 'has lost'], 'lost', "his job in Paris."),
      ("Alan", ['traveled', 'was traveling'], 'was traveling', "to work when he received a call from his wife."),
      ("In 2007 I", ['was working', 'have worked'], 'was working', "in the company headquarters in Geneva."),
      ("I", ['have lived', 'was living'], 'have lived', "in San Francisco since 2003."),
      ("Peter", ['is sleeping', 'was sleeping'], 'was sleeping', "at his desk when his phone rang."),
      ("They", ['was', 'have been'], 'have been', "based in Frankfurt since 1994."),
      ("While I", ['was living', 'have living'], 'was living', "in France, I worked as a waiter."),
      ("Derek", ['was buying', 'bought'], 'bought', "his first house in 2009."),
      ("What", ['were you doing', 'have you done'], 'were you doing', "at 4pm this afternoon?"),
      ("I", ['was studying', 'studied'], 'was studying', "in college when I decided to work as a lawyer."),
      ("Who was in the meeting room when you", ['entered', 'have entered'], 'entered', "?"),
      ("We", ['were selling', 'sold'], 'sold', "our first machine in China in 2003.")]
exercise('hw-5', 'HW6 – Choose, Then Say It', 'hw', 'HW6 — Choose, then say it', 'Cross out the incorrect words in each sentence, then say the sentences out loud.',
         [co_row(i + 1, p, c, a, post, 'hw5-%d' % (i + 1), say=True) for i, (p, c, a, post) in enumerate(H5)], 'circ',
         example=co_example('My doctor', ['told', 'was telling'], 'told', 'me that I should take a vacation.'), gid='hw5', aud=AL.pb_clips(2, 6, 14))


slide('hw-ai', 'HW – Practice with AI', aihw.ai_slide(banner('hw'), 'hw-ai', 'talking about my work history with past simple, past continuous and present perfect', 'past simple, past continuous, present perfect, and polite past forms like "I was wondering if..."', 'What did you do in your first job, and what were you doing when you got your current one?', 'Save your best corrected sentences. Bring them to the next class.'))
