# -*- coding: utf-8 -*-
# Unit 2 "Getting to know colleagues" — lesson slides.  Theme: the coffee-machine catch-up.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'shared'))
from lib import *
from ex import *
import audiolib as AL

U = '2'
SPEAK_EX.update({
 "s-sp1": [
  "I worked in a bank for three years. I helped customers open accounts.",
  "A year ago I was working for a small company and studying at night.",
  "I was driving to work when I heard the news. I was so happy!",
  "Did you work abroad? Were you studying when you got your first job?"
 ],
 "s-sp2": [
  "Did you want some more coffee?",
  "I was wondering if you could help me with this report.",
  "Did you want a tour of the office?",
  "I wanted to ask about the history of the company."
 ],
 "s-sp3": [
  "Have you ever worked in a team? How big was it?",
  "How long have you worked here?",
  "Have you finished the budget yet?",
  "I have organized two events this year. I haven't finished my training yet."
 ],
 "s-rd5": [
  "Yes. I had a short chat with a manager, and she offered me a new project.",
  "I was waiting for a meeting when I met a new colleague.",
  "I think they would work well. People would talk more.",
  "My company has created a shared lunch area. It has helped us meet people from other teams."
 ]
})



cover(2, 'Getting to know colleagues', ["What did you do before you came here?", "I was working 60 hours a week.", "Have you worked in a team before?", "Did you want a tour of the office?"])

# ------------------------------------------------------------------ WARM-UP: CAREER SNAPSHOT
content('s-lead', 'Warm-Up – Career Snapshot', 'leadin', 'Your career snapshot', '''
    <div class="lead-grid">
      <div class="bd-form">
        <label for="cs-1">Your first job</label><input id="cs-1" data-live="first" maxlength="44" autocomplete="off">
        <label for="cs-2">The job before this one</label><input id="cs-2" data-live="last" maxlength="44" autocomplete="off">
        <label for="cs-3">What you do now</label><input id="cs-3" data-live="now" maxlength="44" autocomplete="off">
        <label for="cs-4">Something you are proud of</label><input id="cs-4" data-live="proud" maxlength="52" autocomplete="off">
      </div>
      <div class="profile-card">
        <div class="pc-h">Career snapshot</div>
        <div class="pc-row"><span class="pc-k">First job</span><span class="pc-v" data-bd="first">&nbsp;</span></div>
        <div class="pc-row"><span class="pc-k">Before this</span><span class="pc-v" data-bd="last">&nbsp;</span></div>
        <div class="pc-row"><span class="pc-k">Now</span><span class="pc-v" data-bd="now">&nbsp;</span></div>
        <div class="pc-row"><span class="pc-k">Proud of</span><span class="pc-v" data-bd="proud">&nbsp;</span></div>
      </div>
    </div>''', 'A new colleague asks about your work history. Fill in your career snapshot, then tell me the story.')

# ------------------------------------------------------------------ WARM-UP 2: WHAT'S THE BEST QUESTION
def wyr(n, a, b):
    g = 'wyr%d' % n
    s = 'font-size:1.1rem;padding:8px 20px;white-space:normal;text-align:left;'
    return ('<div class="ex-row" style="margin-bottom:18px;"><span class="circ-num">%d</span>'
            '<button class="circ-opt" style="%s" data-group="%s" onclick="circPick(this)">%s</button> <b style="margin:0 6px;">or</b> '
            '<button class="circ-opt" style="%s" data-group="%s" onclick="circPick(this)">%s</button></div>') % (n, s, g, a, s, g, b)
content('s-lead2', 'Warm-Up – Would You Rather?', 'leadin', 'Would you rather&hellip;?',
        wyr(1, 'work for a huge company', 'work for a small team') + wyr(2, 'have one job for 20 years', 'change jobs every three years') +
        wyr(3, 'tell a new colleague about your past jobs', 'hear about their past jobs'),
        'Choose one. Then tell me why.')

# ------------------------------------------------------------------ 2.1 MEANING: past simple vs continuous (sort)
S_SIMPLE, S_CONT = 'simple', 'continuous'
sort_slide('s-m1', 'Meaning – Past Simple or Past Continuous?', 'grammar', 'Finished, or in progress?',
           'Talking about your past work experience is a good way to get to know your colleagues. Click a sentence, then click the box where it belongs.',
           [("I fixed computers.", S_SIMPLE), ("I was working 60 hours a week before I came here.", S_CONT), ("I ran my own construction company.", S_SIMPLE),
            ("At 9am yesterday I was writing a report.", S_CONT), ("I was a legal assistant.", S_SIMPLE), ("While I was waiting, the manager arrived.", S_CONT)],
            [(S_SIMPLE, '<b>Past simple</b><br>a single, completed action, a past habit, or a state that was true for a time'),
             (S_CONT, '<b>Past continuous</b><br>an ongoing action that was in progress at a certain time in the past')],
           post=ccqs(('&ldquo;I ran my own construction company.&rdquo; Is the company still mine now?', 'No. It is finished. We use the past simple for completed actions and states.'),
                     ('&ldquo;I was working 60 hours a week before I came here.&rdquo; What happened next?', 'The speaker came here. The long action (working) was in progress when the short action (came) happened.')),
           aud=AL.single(U, '2_1'))

# ------------------------------------------------------------------ 2.2 FORM
content('s-g1', 'Grammar – Form', 'grammar', 'How we build them', '''
    <p style="margin:0 0 4px;">The past simple is usually formed by adding &ldquo;-ed&rdquo; to the base form of the verb. The past continuous is formed by adding &ldquo;was&rdquo; or &ldquo;were&rdquo; in front of the verb, and &ldquo;-ing&rdquo; to the end of the verb.</p>
    ''' + puzzle([('Subject', 'I', ''), ('Past continuous', 'was working', 'a'), ('Rest of clause', '60 hours a week', ''), ('Past simple', 'before I came here.', 'b')]) + '''
    <div class="form-grid">
      <div class="form-card"><h4>Past simple</h4>
        <div class="form-row"><span class="fr-k">Positive</span><span class="fr-v">I <b>worked</b> for TCE.<br>I <b>ran</b> my own company. <i>(irregular)</i></span></div>
        <div class="form-row"><span class="fr-k">Negative</span><span class="fr-v">I <b>didn't work</b> there.</span></div>
        <div class="form-row"><span class="fr-k">Question</span><span class="fr-v"><b>Did</b> you <b>work</b> in a hotel?</span></div></div>
      <div class="form-card cont"><h4>Past continuous</h4>
        <div class="form-row"><span class="fr-k">Positive</span><span class="fr-v">I <b>was working</b>.<br>They <b>were working</b>.</span></div>
        <div class="form-row"><span class="fr-k">Negative</span><span class="fr-v">I <b>wasn't working</b>.<br>They <b>weren't working</b>.</span></div>
        <div class="form-row"><span class="fr-k">Question</span><span class="fr-v"><b>Were</b> you <b>working</b> as a waiter?</span></div></div>
    </div>''')

# ------------------------------------------------------------------ CB 2.3
S3 = [("They", ['began', 'were beginning'], 'were beginning', "to sell more when the shop suddenly closed last year."),
      ("I", ['lost', 'was losing'], 'lost', "my job when the factory closed last December."),
      ("I was delighted when I", ['got', 'was getting'], 'got', "promoted to senior manager in 2015."),
      ("We moved here when my wife", ['was finding', 'found'], 'found', "a new job two years ago."),
      ("", ['I was training', 'trained'], 'I was training', "to be a chef when I was given this award."),
      ("When I worked 90 hours a week, I", ['felt', 'was feeling'], 'felt', "exhausted all the time."),
      ("When I was a photographer, I", ['was meeting', 'met'], 'met', "a lot of famous people through my work.")]
exercise('s-cb23', 'Grammar – Cross Out the Incorrect Words', 'grammar', 'Which tense?', 'Cross out the incorrect words in each sentence.',
         [co_row(i + 1, p, c, a, post, 'cb23-%d' % (i + 1)) for i, (p, c, a, post) in enumerate(S3)], 'circ',
         example=co_example('', ['I started', 'was starting'], 'I started', 'my own printing company more than 10 years ago.'),
         aud=AL.clips(U, '2_3', 7), gid='cb23')

speak('s-sp1', 'Speaking Break 1 – Your Work Story', 'Speaking break: your work story', 'Answer the questions about you. Use the past simple for finished jobs and the past continuous for actions in progress.', [
    'Tell me about a job you had in the past. What did you do there?',
    'What were you doing a year ago? Where were you working or studying?',
    'Think about the day you got your current job. What were you doing when you heard the news?',
    'Now ask three questions about someone&rsquo;s past. Use &ldquo;Did you&hellip;?&rdquo; and &ldquo;Were you&hellip;ing&hellip;?&rdquo;'])

# ------------------------------------------------------------------ 2.4 MEANING: past tense for politeness
content('s-m2', 'Meaning – The Past Tense for Politeness', 'grammar', 'A polite way to ask', '''
    <p class="instruction" style="margin-bottom:10px;">You may hear people ask questions about a present situation in the past tense. This makes the question more polite. The past tense is also sometimes used to make a polite request.</p>
    <div class="two-up">
      <div class="scene"><div class="sc-figs">%s</div><div class="say">%s</div>
        <p style="margin:4px 0 0;color:var(--muted);font-size:1rem;">&ldquo;Do&rdquo; becomes &ldquo;Did&rdquo; to make the question in past tense.</p></div>
      <div class="scene"><div class="sc-figs">%s</div><div class="say b">%s</div>
        <p style="margin:4px 0 0;color:var(--muted);font-size:1rem;">A polite request about something you want now.</p></div>
    </div>
    %s
    %s''' % (figs([TEAL, BRASS]), 'Did you want a tour of the office?', figs([BRASS, INK]), 'I wanted to ask about the company\'s history.',
             ccqs(('Is the person asking about a tour in the past?', 'No. The tour is for now. The past tense is just more polite.'),
                  ('Which sounds more polite: &ldquo;Do you want a tour?&rdquo; or &ldquo;Did you want a tour?&rdquo;', '&ldquo;Did you want a tour?&rdquo;')),
             AL.single(U, '2_4')))

# ------------------------------------------------------------------ CB 2.5
S5 = [(["I was to look for another job.", "I was looking for another job."], "I was looking for another job."),
      (["I was wondering if you could help.", "I was wondered if you could help."], "I was wondering if you could help."),
      (["Were you working as a waiter?", "Were you work as a waiter?"], "Were you working as a waiter?"),
      (["They weren't employing young people.", "They not employing young people."], "They weren't employing young people."),
      (["I didn't enjoy my last job.", "I didn't enjoying my last job."], "I didn't enjoy my last job."),
      (["Did you work in a hotel?", "Did you working in a hotel?"], "Did you work in a hotel?")]
exercise('s-cb25', 'Grammar – Mark the Correct Sentences', 'grammar', 'Which sentence is correct?', 'Mark the sentences that are correct.',
         [pick_row(i + 1, o, a, 'cb25-%d' % (i + 1)) for i, (o, a) in enumerate(S5)], 'circ',
         example=pick_example(["Did you want some more coffee?", "Do you wanting some more coffee?"], "Did you want some more coffee?"),
         aud=AL.clips(U, '2_5', 6), gid='cb25')

speak('s-sp2', 'Speaking Break 2 – Be Polite', 'Speaking break: sound polite', 'Read each situation. What could you say? Use the past tense to sound polite.', [
    'A new colleague has an empty cup. What could you say to offer more coffee?',
    'You need help with a report. How could you ask a colleague politely?',
    'A visitor arrived this morning. How could you ask if they wanted a tour of the office?',
    'You are curious about how the company started. What could you say?'])

# ------------------------------------------------------------------ 2.6 MEANING: present perfect simple vs past simple (sort)
P_PS, P_PP = 'past simple', 'present perfect'
sort_slide('s-m3', 'Meaning – Present Perfect or Past Simple?', 'grammar', 'Is there a date?',
           'The present perfect simple is used to talk about events in the recent past that still have an effect on the present moment. Click a sentence, then click the box where it belongs.',
           [("I have worked in a few different teams.", P_PP), ("I worked in a small team in 2005.", P_PS), ("I haven't worked in a team before.", P_PP),
            ("We moved offices last March.", P_PS), ("He has just finished the report.", P_PP), ("She left the company in 2019.", P_PS)],
           [(P_PP, '<b>Present perfect</b><br>no date is specified'), (P_PS, '<b>Past simple</b><br>a specific date is given')],
           post=ccqs(('&ldquo;I have worked in a few different teams.&rdquo; Do we know when?', 'No. No date is specified, so the present perfect is used.'),
                     ('&ldquo;I worked in a small team in 2005.&rdquo; Why the past simple?', 'A specific date is given, so the past simple is used.')),
           aud=AL.single(U, '2_6'))

# ------------------------------------------------------------------ 2.7 FORM
content('s-g2', 'Grammar – Form: Present Perfect Simple', 'grammar', 'Have or has, plus a past participle', '''
    <p style="margin:0 0 4px;">The present perfect simple is formed with &ldquo;have&rdquo; and a past participle.</p>
    ''' + puzzle([('Subject', 'I', ''), ('&ldquo;Have / has&rdquo; + past participle', 'have worked', 'a'), ('Rest of sentence', 'in a few teams.', '')]) + '''
    <div class="form-grid">
      <div class="form-card"><h4>Positive</h4>
        <div class="form-row"><span class="fr-k">I / you / we / they</span><span class="fr-v"><b>have</b> worked</span></div>
        <div class="form-row"><span class="fr-k">he / she / it</span><span class="fr-v"><b>has</b> worked</span></div></div>
      <div class="form-card cont"><h4>Negative and question</h4>
        <div class="form-row"><span class="fr-k">Negative</span><span class="fr-v">I <b>haven't worked</b> in a team before.</span></div>
        <div class="form-row"><span class="fr-k">Question</span><span class="fr-v"><b>Have</b> you <b>worked</b> in a team before?</span></div></div>
    </div>''')

# ------------------------------------------------------------------ CB 2.8
S8 = [("He", 'has taken', 'take', "15 days off sick this year and it is only May!"),
      ("Julia has a lot of experience. She", 'has managed', 'manage', "this department for years."),
      ("They", 'have employed', 'employ', "more than 300 people over the years."),
      ("John", 'has trained', 'train', "lots of young employees across a few different teams."),
      ("I'm so happy! I", 'have finished', 'finish', "my apprenticeship at last."),
      ("My manager", 'has approved', 'approve', "my vacation days. I'm going to Italy in July.")]
exercise('s-cb28', 'Grammar – Fill in the Gaps', 'grammar', 'Present perfect simple', 'Fill in the gaps by putting the verbs in the present perfect simple.',
         [gap_row(i + 1, p, a, v, post) for i, (p, a, v, post) in enumerate(S8)], 'typed',
         example=gap_example("Susan", "has worked", 'work', "here since she graduated from college five years ago."),
         aud=AL.clips(U, '2_8', 6), gid='cb28')

speak('s-sp3', 'Speaking Break 3 – Interview a Colleague', 'Speaking break: interview your colleague', 'Read each situation. What could you ask or say? Use the present perfect.', [
    'You want to know if a new colleague has any team experience. What could you ask? Then add a follow-up question.',
    'You want to know how long a colleague has been at the company. What could you ask?',
    'A colleague looks relieved. You think they have just finished something. What could you ask?',
    'Now your turn. Tell me one thing you have done at work this year, and one thing you have not done yet.'])

# ------------------------------------------------------------------ PRONUNCIATION: -ed endings
sort_slide('s-pron', 'Pronunciation – -ed Endings', 'pron', 'Three sounds for -ed',
           'Say each verb out loud, then click the verb and the sound you hear at the end.',
           [("worked", "/t/"), ("fixed", "/t/"), ("finished", "/t/"), ("employed", "/d/"), ("trained", "/d/"), ("approved", "/d/"),
            ("managed", "/d/"), ("invested", "/ɪd/"), ("started", "/ɪd/")],
           [("/t/", '<b>/t/</b><br>after voiceless sounds'), ("/d/", '<b>/d/</b><br>after voiced sounds'), ("/ɪd/", '<b>/ɪd/</b><br>after /t/ or /d/ (an extra syllable)')],
           post='<div class="gram-note">🔊 Only the /ɪd/ verbs get an extra syllable: <b>start-ed</b>, <b>invest-ed</b>.</div>')

# ------------------------------------------------------------------ CB 2.9 LISTENING
exercise('s-cb29', 'Listening – Two Colleagues', 'listening', 'Two colleagues talk about their past',
         'Listen to the audio and answer the questions. Two colleagues are discussing their past experience.',
         [tf_row(1, "Suzi's previous company was smaller.", 'True', 'cb29-1'), tf_row(2, 'Suzi has always worked in HR.', 'False', 'cb29-2'),
          tf_row(3, 'Jack has worked for CIE for six years.', 'Not given', 'cb29-3'), tf_row(4, 'Jack has never worked for another company.', 'True', 'cb29-4'),
          tf_row(5, 'Jack and Suzi always work the same days.', 'Not given', 'cb29-5')], 'circ',
         example=tf_example("This is Suzi's first day at the company.", 'False'),
         pre=AL.single(U, '2_9', top=True) + ph('🎧', 'Photo: two colleagues talking in an office').replace('img-placeholder', 'img-placeholder ph-small'), gid='cb29')

# ------------------------------------------------------------------ EXTRA READING: the coffee-machine article
content('s-rd0', 'Reading – Before You Read', 'reading', 'Before you read', '''
    <div class="two-up">
      <div class="scene"><p style="margin:0 0 6px;"><b>Talk about it</b></p>
        <p style="margin:0;">1. Where do people talk at your workplace: the coffee machine, the elevator, the kitchen?<br>2. Have you ever learned something important from a short chat with a colleague?<br>3. Is it easy or difficult for you to start a conversation with a new colleague?</p></div>
      <div class="scene"><p style="margin:0 0 6px;"><b>Predict</b></p>
        <p style="margin:0;">The article is called &ldquo;The best meeting happens at the coffee machine&rdquo;. What do you think it says? Write down two ideas, then read to check.</p></div>
    </div>''', 'Discuss the questions and the prediction. Then go to the next slide to read.')

COFFEE = article('Workplace culture', 'The best meeting happens at the coffee machine', 'How a five-minute chat helped a new employee&mdash;and her whole team',
  ["When Elena Novak joined a logistics company in Rotterdam last spring, she did not know a single person on her floor. &ldquo;I was eating lunch alone at my desk and I felt invisible,&rdquo; she remembers. Three weeks later everything had changed, and it started at the coffee machine.",
   "One morning, while Elena was waiting for her coffee, a colleague from the finance department asked a simple question: &ldquo;What were you doing before you came here?&rdquo; She had worked in three countries and had managed a small warehouse team in Poland. Her colleague had never met anyone with that experience, and soon half the floor was asking her questions.",
   "Managers have started to notice the effect of these short chats. Many companies have created &ldquo;conversation corners&rdquo; instead of formal ice-breaker events, and some have changed the layout of their offices so that people from different departments meet by accident. Employees say they have learned more about each other&rsquo;s skills in ten minutes of small talk than in a month of emails.",
   "Elena has now worked at the company for a year. She has led two cross-department projects, and both started with a conversation over a cup of coffee. &ldquo;I wasn&rsquo;t looking for a project,&rdquo; she says. &ldquo;I was just asking a colleague about his weekend.&rdquo;"])
content('s-rd1', 'Reading – The Coffee Machine', 'reading', 'The best meeting happens at the coffee machine', COFFEE,
        'Read the article. Is it close to your ideas? (This article was written for this course.)')
T2 = [("Elena knew many people on her floor when she started.", 'False'), ("A colleague from the finance department asked Elena about her past.", 'True'),
      ("Elena has worked in three countries.", 'True'), ("The company is in Hamburg.", 'False'),
      ("Some companies have changed their office layout to help people meet.", 'True'), ("Elena was promoted because of her projects.", 'Not given')]
exercise('s-rd2', 'Reading – True, False, Not Given', 'reading', 'What does the article say?', 'Read the article again and answer the questions.',
         [tf_row(i + 1, t, a, 'rd-%d' % (i + 1)) for i, (t, a) in enumerate(T2)], 'circ',
         example=tf_example('Elena felt invisible at the beginning.', 'True'), pre='<div style="margin-bottom:14px;">%s</div>' % article_toggle('rd-art', COFFEE), gid='rd')
M2 = [("What is the main idea of the article?", ['Formal meetings are the best way to make friends.', 'Short, informal chats can help colleagues connect.', 'New employees should eat lunch alone.'], 'Short, informal chats can help colleagues connect.'),
      ("Why was Elena&rsquo;s colleague interested in her?", ['She worked in the finance department.', 'She was the new manager.', 'She had a lot of international experience.'], 'She had a lot of international experience.'),
      ("What does &ldquo;I wasn&rsquo;t looking for a project&rdquo; mean?", ['She did not plan to find a project.', 'She could not find her project.', 'She did not like projects.'], 'She did not plan to find a project.')]
exercise('s-rd3', 'Reading – Understanding the Article', 'reading', 'Choose the best answer', 'Choose the correct answer for each question.',
         [mc_row(i + 1, q, c, a, 'rdm-%d' % (i + 1)) for i, (q, c, a) in enumerate(M2)], 'circ', pre='<div style="margin-bottom:14px;">%s</div>' % article_toggle('rd-art2', COFFEE), gid='rdm')
V2 = [("If nobody notices you, you feel", 'invisible', ''), ("The way furniture and rooms are arranged in an office is its", 'layout', ''),
      ("A project with people from several departments is a", 'cross-department', ''), ("An activity to help people who do not know each other start talking is an", 'ice-breaker', '')]
exercise('s-rd4', 'Reading – Words in Context', 'reading', 'Words from the article', 'Find the word in the article and type it in the gap. (Hint: look at paragraphs 1, 3 and 4.)',
         [typed_row(i + 1, p + ' ______:', a, c) for i, (p, a, c) in enumerate(V2)], 'typed', pre='<div style="margin-bottom:14px;">%s</div>' % article_toggle('rd-art3', COFFEE), gid='rdv')
speak('s-rd5', 'Speaking – About the Article', 'Speaking break: what do you think?', 'Answer the questions about you. Use the past and the present perfect from this unit.', [
    'Have you ever had a conversation at work that changed something for you? What happened?',
    'What were you doing the last time you met a new colleague?',
    'Would conversation corners work in your company? Why, or why not?',
    'Elena has led two projects since she joined. What has your company done recently to help people meet?'])

# ------------------------------------------------------------------ CB 2.10
S10 = [("", ['drove', 'was driving', 'have driven'], 'was driving', "taxis when I saw this job advertised."),
       ("", ['managed', 'was managing', 'have managed'], 'have managed', "accounts for this company for seven years."),
       ("", ['bought', 'was buying', 'have bought'], 'bought', "my first business in 2009."),
       ("I was studying in college when I", ['saw', 'was seeing', 'have seen'], 'saw', "this job."),
       ("They", ['invested', 'were investing', 'have invested'], 'have invested', "in this company since 2010."),
       ("In 2014, I", ['sold', 'was selling', 'has sold'], 'sold', "the company to an investor.")]
exercise('s-cb210', 'Speaking – Choose, Then Say It', 'speaking', 'Choose, then say it', 'Cross out the incorrect words in each sentence, then say the sentences out loud.',
         [co_row(i + 1, p, c, a, post, 'cb210-%d' % (i + 1), say=True) for i, (p, c, a, post) in enumerate(S10)], 'circ',
         example=co_example('', ['I worked', 'was working', 'have worked'], 'have worked', 'in marketing since 1995.'),
         aud=AL.clips(U, '2_10', 6), gid='cb210')

# ------------------------------------------------------------------ FREER PRACTICE
chat_speak('s-free', 'Speaking – Coffee Machine Catch-up', 'Coffee-machine catch-up', 'Read the conversation as it goes. When it is your turn, say what you could say.', 'Priya', [
 ("Hi! I'm Priya. I just joined the finance team.<br>Have you worked here long?", 'Say how long you have worked at the company.', "Hi, Priya. I've worked here for about six years."),
 ("Wow, that's a long time.<br>What did you do before you came here?", 'Say what job you had before.', "I worked for a small marketing agency in Madrid."),
 ("Nice!<br>What were you doing when you got this job offer?", 'Say what you were doing when you got the offer.', "I was working on a big project when the recruiter called me."),
 ("I was studying for my MBA when I got mine.<br>Did you enjoy your first year here?", 'Answer, and add a detail.', "Yes, I did. Everyone was friendly, and I learned a lot."),
 ("Have you ever worked in another country?", 'Answer, and add one detail.', "Yes, I have. I lived in Dubai for two years, and I loved it."),
 ("I was wondering if you could show me where the meeting rooms are.", 'Offer to show Priya around, politely.', "Of course! Did you want a quick tour of the whole office?")])

# ------------------------------------------------------------------ REVIEW
review([('Past simple and past continuous', '⚙️'), ('Sharing past experiences', '🗂️'), ('Talking about past experiences', '🧩')],
       'Before you leave the coffee machine', 'Tell me about your career one more time. What can you say now that you could not say before?')
