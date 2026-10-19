# -*- coding: utf-8 -*-
# Unit 6 homework — Practice Book Unit 6 (6.1 Money and finance)
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'shared'))
from lib import *
from ex import *
hw_cover('Money and finance')

D = [("To lose money by spending more than you earn", 'to make a loss'), ("To charge less than others who sell the same goods or services as you", 'to undercut competitors'),
     ("Extra money the bank allows you to spend", 'an overdraft'), ("The regular costs of running a business, such as wages", 'overheads'),
     ("The amount or value of total sales over a particular period", 'sales figures'), ("To get into a situation where you owe people money", 'to get into debt'),
     ("To earn just enough to cover the costs of producing a product", 'to break even'), ("A major decline in economic activity", 'an economic downturn'),
     ("Money coming into a business", 'income'), ("An amount of money spent", 'expenditure / outlay'), ("A change to more positive business conditions", 'an upturn in the market'),
     ("Records of money paid into and out of a business", 'accounts'), ("To fall, especially in worth or value", 'to drop'),
     ("The rate at which money comes into and goes out of a business", 'cash flow'), ("To reach the highest point", 'to peak'),
     ("The amount of one currency that you get when you change it for another", 'the exchange rate'), ("To no longer be able to exist as a business", 'to go out of business')]
bank = ['to make a loss', 'an upturn in the market', 'sales figures', 'income', 'an economic downturn', 'overheads', 'the exchange rate', 'cash flow', 'an overdraft',
        'to get into debt', 'to go out of business', 'to peak', 'expenditure / outlay', 'a budget', 'to undercut competitors', 'to drop', 'accounts', 'to break even']
def defrow(n, d, a):
    return '<div class="ex-row"><span class="circ-num">%d</span>%s %s</div>' % (n, d, wb_blank(a))
exercise('hw-1', 'HW1 – Money and Finance', 'hw', 'HW1 — Money and finance', 'Write the phrases from the panel under the correct definitions. Click a phrase, then click a gap.',
         [defrow(i + 1, d, a) for i, (d, a) in enumerate(D)], 'wb',
         example=ex_given('%sThe amount of money that is available to spend on something<br><span style="margin-left:34px;display:inline-block;"><span class="wb-blank filled is-example" data-ans="a budget">a budget</span></span>' % example_badge()),
         pre=wb_bank(bank, 'a budget'), gid='hw1', aud=AL.pb_clips(6, 1, 17))
