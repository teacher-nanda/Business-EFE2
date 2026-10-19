# -*- coding: utf-8 -*-
# Unit 3 "Departments and roles" — vocabulary lesson.  Theme: the org chart.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'shared'))
from lib import *
from ex import *
import audiolib as AL
U = '3'
W = lambda n: AL.word(U, n)

cover(3, 'Departments and roles', ["Who looks after the salaries?", "I work in event management.", "She works as a fashion designer.", "I'm in charge of administration."])

content('s-lead', 'Warm-Up – Your Place in the Company', 'leadin', 'Your place in the company', '''
    <div class="lead-grid">
      <div class="bd-form">
        <label for="oc-1">Your company</label><input id="oc-1" data-live="co" maxlength="40" autocomplete="off">
        <label for="oc-2">Your department</label><input id="oc-2" data-live="dept" maxlength="40" autocomplete="off">
        <label for="oc-3">Your role</label><input id="oc-3" data-live="role" maxlength="40" autocomplete="off">
        <label for="oc-4">Who you report to</label><input id="oc-4" data-live="boss" maxlength="40" autocomplete="off">
      </div>
      <div class="profile-card">
        <div class="pc-h">Company directory</div>
        <div class="pc-row"><span class="pc-k">Company</span><span class="pc-v" data-bd="co">&nbsp;</span></div>
        <div class="pc-row"><span class="pc-k">Department</span><span class="pc-v" data-bd="dept">&nbsp;</span></div>
        <div class="pc-row"><span class="pc-k">Role</span><span class="pc-v" data-bd="role">&nbsp;</span></div>
        <div class="pc-row"><span class="pc-k">Reports to</span><span class="pc-v" data-bd="boss">&nbsp;</span></div>
      </div>
    </div>''', 'Fill in your entry in the company directory. Then explain it to me in your own words, even if you do not know all the words yet.')

# ---------------- 3.1 DEPARTMENTS (A, B)
D = [('🗂️', 'Administration', 'deals with organization and internal and external communication', 'administration'),
     ('🔬', 'Research and Development (R&amp;D)', 'deals with researching and developing future products for a company', 'researchanddevelopment'),
     ('🤝', 'Human Resources (HR)', 'deals with employee relations and matters such as hiring staff', 'humanresources'),
     ('💰', 'Accounts / Finance', 'deals with money matters, from paying bills to projecting sales', 'accountsfinance'),
     ('📣', 'Marketing', 'deals with promoting products', 'marketing'),
     ('🎤', 'Public Relations (PR)', 'deals with maintaining a positive public image for a company', 'publicrelations'),
     ('🏭', 'Production', 'ensures all manufacturing stages run smoothly', 'production'),
     ('🛒', 'Purchasing', 'deals with buying goods and raw materials', 'purchasing'),
     ('🏷️', 'Sales', 'deals with selling a finished product to outside markets', 'sales'),
     ('🧹', 'Facilities / Office Services', 'ensures the smooth day-to-day running of the practical aspects of a company', 'facilitiesofficeservices'),
     ('⚖️', 'Legal', 'ensures that all contracts and company activities are legal', 'legal'),
     ('💻', 'Information Technology (IT)', 'ensures that all technological systems are working and maintained', 'informationtechnology')]
mk = lambda L: vcards([(ic, n, d, '', W('3_1_' + a)) for ic, n, d, a in L])
content('s-v1', 'Vocabulary – Departments (1)', 'vocab', 'Departments (1 of 2)', mk(D[:6]) + ccqs(
    ('Which department deals with hiring staff?', 'Human Resources (HR).'), ('Which department deals with promoting products?', 'Marketing.')),
    'Click the speaker to hear each department. Which ones exist in your company?')
content('s-v2', 'Vocabulary – Departments (2)', 'vocab', 'Departments (2 of 2)', mk(D[6:]) + ccqs(
    ('Which department deals with buying raw materials?', 'Purchasing.'), ('Which department keeps all the technological systems working?', 'Information Technology (IT).')),
    'Click the speaker to hear each department. Which ones exist in your company?')

# ---------------- PRACTICE: who would you call?
CALL = [("Your laptop will not start.", 'Information Technology (IT)', ['Legal', 'Information Technology (IT)', 'Sales']),
        ("You want to hire a new assistant.", 'Human Resources (HR)', ['Human Resources (HR)', 'Purchasing', 'Production']),
        ("You need to check a supplier's contract.", 'Legal', ['Marketing', 'Legal', 'Public Relations (PR)']),
        ("The office is very dirty.", 'Facilities / Office Services', ['Facilities / Office Services', 'Accounts / Finance', 'Sales']),
        ("You are launching a new ad.", 'Marketing', ['Production', 'Marketing', 'Administration']),
        ("You need to order raw materials.", 'Purchasing', ['Purchasing', 'Research and Development (R&amp;D)', 'Public Relations (PR)'])]
exercise('s-call', 'Practice – Who Would You Call?', 'vocab', 'Who would you call?', 'Read each situation. Which department would you call?',
         [mc_row(i + 1, q, c, a, 'call-%d' % (i + 1)) for i, (q, a, c) in enumerate(CALL)], 'circ', gid='call')


speak('s-sp1', 'Speaking Break – Departments', 'Speaking break: departments', 'Talk to your teacher about the departments you just learned. Click the button when you have said it.', [
    'Which departments does your company have? Name three and say what each one does.',
    'Which department do you work with most? Why?',
    'Which department would you like to visit for a day? Why?',
    'Ask your teacher: &ldquo;Which department do you think is the busiest?&rdquo; Then give your own opinion.'])

# ---------------- 3.2 ROLES
R = [('🧑‍💼', 'employer', 'a person or company that employs people', 'employer'), ('🧑‍💻', 'employee', 'a person who works for an employer', 'employee'),
     ('👔', 'Chief Executive Officer (CEO)', 'the person with the highest position in the company', 'chiefexecutiveofficer'),
     ('📊', 'Chief Financial Officer (CFO)', 'the person in charge of the company\'s finances', 'chieffinancialofficer'),
     ('📋', 'manager', 'a person who is in charge of a team or department', 'manager'), ('🗒️', 'assistant', 'a person who helps someone with their work', 'assistant')]
content('s-v3', 'Vocabulary – Roles', 'vocab', 'Roles', vcards([(ic, n, d, '', W('3_2_' + a)) for ic, n, d, a in R]) + ccqs(
    ('Who pays an employee?', 'The employer.'), ('Who is the most senior person in a company?', 'The CEO.')), 'Click the speaker to hear each role.')


RM = [("Who is the person in charge of the whole company?", ['The CEO', 'The assistant', 'The employee'], 'The CEO'),
      ("Who looks after the company's money at the highest level?", ['The CFO', 'The employer', 'The assistant'], 'The CFO'),
      ("Who helps another person with their work?", ['The manager', 'The assistant', 'The CEO'], 'The assistant'),
      ("Who pays the employees?", ['The employer', 'The employee', 'The assistant'], 'The employer')]
exercise('s-x1', 'Extra – Who Is Who?', 'vocab', 'Who is who?', 'Choose the correct role for each description.',
         [mc_row(i + 1, q, c, a, 'x1-%d' % (i + 1)) for i, (q, c, a) in enumerate(RM)], 'circ', gid='x1')
speak('s-sp2', 'Speaking Break – Roles', 'Speaking break: roles', 'Talk to your teacher. Click the button when you have said it.', [
    'Who is your employer? Who are your managers?',
    'Do you have an assistant, or are you an assistant to someone? What does that person do?',
    'Who is the CEO of your company or of a company you know well? What is the CEO like?'])

# ---------------- 3.3 DESCRIBING ROLES
P = [('🏬', 'to work for', '[to be employed by a company]', 'We all <b>work for</b> a large department store.', 'toworkfor'),
     ('🎈', 'to work in', '[to be employed in a department or area of an industry]', 'I <b>work in</b> event management.', 'toworkin'),
     ('👗', 'to work as', '[to have a particular job or role]', 'She <b>works as</b> a fashion designer.', 'toworkas'),
     ('💵', 'to look after', '[to ensure something runs smoothly]', 'He <b>looks after</b> our salaries and wages.', 'tolookafter'),
     ('🧰', 'to be responsible for', '[to have the duty of ensuring something is done effectively]', 'They are <b>responsible for</b> office maintenance.', 'toberesponsiblefor'),
     ('🗄️', 'to be in charge of', '[to have control and authority over something]', 'I\'m <b>in charge of</b> administration.', 'tobeinchargeof')]
content('s-v4', 'Vocabulary – Describing Roles', 'vocab', 'Describing roles', vcards([(ic, n, d, e, W('3_3_' + a)) for ic, n, d, e, a in P]) + ccqs(
    ('&ldquo;I work in event management.&rdquo; Is event management the company or the area?', 'The area of an industry. For the company we say &ldquo;work for.&rdquo;'),
    ('&ldquo;She works as a fashion designer.&rdquo; What does &ldquo;works as&rdquo; tell us?', 'Her job or role.')), 'Click the speaker to hear each phrase.')

# ---------------- PRACTICE: complete the role sentences (word bank)
WBP = ['to work for', 'to work in', 'to work as', 'to look after', 'to be responsible for', 'to be in charge of']
RS = [("My cousin", 'works as', "an accountant."), ("Pablo", 'works for', "a large department store."), ("Anna", 'is in charge of', "the whole marketing department."),
      ("Sam", 'looks after', "the office equipment."), ("They", 'work in', "event management."), ("Who", 'is responsible for', "the office maintenance?")]
exercise('s-rs', 'Practice – Describe the Roles', 'vocab', 'Describe the roles', 'Fill in the gaps using the phrases in the panel. Click a phrase, then click a gap.',
         [wb_row(i + 1, p, a, post) for i, (p, a, post) in enumerate(RS)], 'wb',
         pre=wb_bank(['works as', 'works for', 'is in charge of', 'looks after', 'work in', 'is responsible for']), gid='rs')


speak('s-sp3', 'Speaking Break – Describe Your Job', 'Speaking break: describe your job', 'Use the phrases from this lesson to talk about your own job. Click the button when you have said it.', [
    'Use &ldquo;work for&rdquo; and &ldquo;work in&rdquo;: where do you work?',
    'Use &ldquo;work as&rdquo;: what is your job?',
    'Use &ldquo;in charge of&rdquo; or &ldquo;responsible for&rdquo;: what do you manage or look after?',
    'Now ask your teacher about their job, using the same phrases.'])

# ---------------- PRONUNCIATION: word stress
sort_slide('s-pron', 'Pronunciation – Word Stress', 'pron', 'Where is the stress?',
           'Click the speaker to hear the word, say it, then click the word and the syllable that is stressed.',
           [("Marketing", "1st"), ("Purchasing", "1st"), ("Legal", "1st"), ("Production", "2nd"), ("Facilities", "2nd"), ("Technology", "2nd"), ("Information", "3rd"), ("Administration", "4th")],
           [("1st", '<b>1st syllable</b><br>MAR-ke-ting'), ("2nd", '<b>2nd syllable</b><br>pro-DUC-tion'), ("3rd", '<b>3rd syllable</b><br>in-for-MA-tion'), ("4th", '<b>4th syllable</b><br>ad-min-is-TRA-tion')],
           aud='<div class="audio-box clips-box"><span class="clips-label">🎧 Listen</span>%s</div>' % ''.join(AL.word(U, '3_1_' + a, l) for a, l in [('marketing', 'marketing'), ('purchasing', 'purchasing'), ('legal', 'legal'), ('production', 'production'), ('administration', 'administration'), ('informationtechnology', 'information technology')]))

freer('s-free', 'Speaking – Org Chart Chat', 'Org chart chat', 'Your teacher is a new employee. Take a card, then explain who does what in the company.', 'Org chart card')
review([('Departments', '🏢'), ('Roles', '🧑‍💼'), ('Describing roles', '🧩')], 'Before you leave the office',
       'Describe your own department and role to me again. Which new phrases can you use?')
