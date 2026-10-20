# -*- coding: utf-8 -*-
# Unit 3 homework — Practice Book Unit 3 (3.1, 3.2, 3.3, in book order)
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'shared'))
from lib import *
from ex import *
import aihw

hw_cover('Departments and roles')

dep = ['Public Relations (PR)', 'Administration', 'Research and Development (R&amp;D)', 'Production', 'Facilities / Office Services', 'Accounts / Finance',
       'Information Technology (IT)', 'Human Resources (HR)', 'Sales', 'Purchasing', 'Legal', 'Marketing']
H1 = [("Deals with employee relations and matters such as hiring staff.", 'Human Resources (HR)'),
      ("Ensures that all technological systems are working and maintained.", 'Information Technology (IT)'),
      ("Deals with selling a finished product to outside markets.", 'Sales'),
      ("Deals with maintaining a positive public image for a company.", 'Public Relations (PR)'),
      ("Ensures that all contracts and company activities are legal.", 'Legal'),
      ("Ensures the smooth day-to-day running of the practical aspects of a company.", 'Facilities / Office Services'),
      ("Deals with organization and internal and external communication.", 'Administration'),
      ("Deals with researching and developing future products for a company.", 'Research and Development (R&amp;D)'),
      ("Deals with money matters, from paying bills to projecting sales.", 'Accounts / Finance'),
      ("Deals with promoting products.", 'Marketing'),
      ("Ensures all manufacturing stages run smoothly.", 'Production')]
def defrow(n, d, a):
    return '<div class="ex-row"><span class="circ-num">%d</span>%s %s</div>' % (n, d, wb_blank(a))
exercise('hw-1', 'HW1 – Departments', 'hw', 'HW1 — Departments', 'Write the departments from the panel under the correct definitions. Click a department, then click a gap.',
         [defrow(i + 1, d, a) for i, (d, a) in enumerate(H1)], 'wb',
         example=ex_given('%sDeals with buying goods and raw materials.<br><span style="margin-left:34px;display:inline-block;"><span class="wb-blank filled is-example" data-ans="Purchasing">Purchasing</span></span>' % example_badge()),
         pre=wb_bank(dep, 'Purchasing'), gid='hw1', aud=AL.pb_clips(3, 1, 11))

roles = ['manager', 'Chief Executive Officer (CEO)', 'employer', 'Chief Financial Officer (CFO)', 'employee', 'assistant']
H2 = [("Picture: a man in a suit and a woman holding a folder, standing together", 'assistant'),
      ("Picture: a man in a suit sitting behind a large desk", 'Chief Executive Officer (CEO)'),
      ("Picture: a woman at a desk with an abacus", 'Chief Financial Officer (CFO)'),
      ("Picture: a man and a woman shaking hands at a table", 'employee'),
      ("Picture: a woman at the head of a meeting table, with colleagues around it", 'manager')]
def picrow(n, p, a):
    return '<div class="ex-row"><span class="circ-num">%d</span><span style="display:inline-flex;gap:12px;align-items:center;flex-wrap:wrap;">%s %s</span></div>' % (n, pic(p), wb_blank(a))
exercise('hw-2', 'HW2 – Roles', 'hw', 'HW2 — Roles', 'Write the words from the panel under the correct pictures. Click a word, then click a gap.',
         [picrow(i + 1, p, a) for i, (p, a) in enumerate(H2)], 'wb',
         example=ex_given('%s<span style="display:inline-flex;gap:12px;align-items:center;flex-wrap:wrap;">%s <span class="wb-blank filled is-example" data-ans="employer">employer</span></span>' % (example_badge(), pic('Picture: two people talking at a table'))),
         pre=wb_bank(roles, 'employer'), gid='hw2', aud=AL.pb_clips(3, 2, 5))

ph3 = ['to work as', 'to look after', 'to be in charge of', 'to be responsible for', 'to work in', 'to work for']
H3 = [("To be employed by a company", 'to work for'), ("To have a particular job or role", 'to work as'), ("To have the duty of ensuring something is done effectively", 'to be responsible for'),
      ("To have control and authority over something", 'to be in charge of'), ("To be employed in a department or area of an industry", 'to work in')]
exercise('hw-3', 'HW3 – Describing Roles', 'hw', 'HW3 — Describing roles', 'Write the phrases from the panel under the correct definitions. Click a phrase, then click a gap.',
         [defrow(i + 1, d, a) for i, (d, a) in enumerate(H3)], 'wb',
         example=ex_given('%sTo ensure something runs smoothly<br><span style="margin-left:34px;display:inline-block;"><span class="wb-blank filled is-example" data-ans="to look after">to look after</span></span>' % example_badge()),
         pre=wb_bank(ph3, 'to look after'), gid='hw3', aud=AL.pb_clips(3, 3, 5))


slide('hw-ai', 'HW – Practice with AI', aihw.ai_slide(banner('hw'), 'hw-ai', 'departments and roles in a company, and describing my job', 'department names, and the phrases work for, work in, work as, in charge of and responsible for', 'Which department do you work in, and what is your role there?', 'Save your best corrected sentences. Bring them to the next class.'))
