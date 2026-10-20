# -*- coding: utf-8 -*-
# Unit 6 "Money and finance" — vocabulary lesson.  Theme: the finance dashboard.
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'shared'))
from lib import *
from ex import *
import audiolib as AL
U = '6'
SPEAK_EX.update({
 "s-sp1": [
  "The biggest expenditure is salaries.",
  "Yes, we have a training budget. It's about two thousand dollars per person.",
  "Getting into debt is dangerous because you have to pay interest.",
  "A restaurant has high overheads. It can break even by selling more lunches."
 ],
 "s-sp2": [
  "A large retailer went out of business last year. Its sales figures dropped fast.",
  "They undercut competitors to win customers. It can hurt their profit margin.",
  "There was an upturn in the market in 2021, and a downturn in 2008.",
  "When the exchange rate drops, imports become more expensive."
 ]
})
W = lambda n: AL.word(U, '6_1_' + n)

cover(6, 'Money and finance', ["We've made a loss.", "Our sales figures have improved.", "We need to undercut our competitors.", "Thankfully, there was an upturn in the market."])

content('s-lead', 'Warm-Up – Finance Snapshot', 'leadin', 'Finance snapshot', '''
    <div class="lead-grid">
      <div class="bd-form">
        <label for="fs-1">A budget you manage</label><input id="fs-1" data-live="budget" maxlength="44" autocomplete="off">
        <label for="fs-2">A big cost in your company</label><input id="fs-2" data-live="cost" maxlength="44" autocomplete="off">
        <label for="fs-3">Something that made a good profit</label><input id="fs-3" data-live="profit" maxlength="44" autocomplete="off">
        <label for="fs-4">Something that lost money</label><input id="fs-4" data-live="loss" maxlength="44" autocomplete="off">
      </div>
      <div class="profile-card">
        <div class="pc-h">Finance snapshot</div>
        <div class="pc-row"><span class="pc-k">Budget</span><span class="pc-v" data-bd="budget">&nbsp;</span></div>
        <div class="pc-row"><span class="pc-k">Big cost</span><span class="pc-v" data-bd="cost">&nbsp;</span></div>
        <div class="pc-row"><span class="pc-k">Profit</span><span class="pc-v" data-bd="profit">&nbsp;</span></div>
        <div class="pc-row"><span class="pc-k">Loss</span><span class="pc-v" data-bd="loss">&nbsp;</span></div>
      </div>
    </div>''', 'Fill in your finance snapshot, then explain it to me in your own words, even if you do not know all the words yet.')

A = [('📈', 'income', 'money coming into a business', 'The company\'s <b>income</b> fell last year.', 'income'),
     ('🧾', 'expenditure / outlay', 'an amount of money spent', 'The initial <b>expenditure</b> on technology was huge, but now we can work faster.', 'expenditureoutlay'),
     ('💵', 'a budget', 'the amount of money that is available to spend on something', 'We have a large <b>budget</b> for this movie, so the effects will be amazing.', 'abudget'),
     ('📉', 'to get into debt', 'to get into a situation where you owe people money', 'We must do all we can to avoid <b>getting into debt</b>.', 'togetintodebt'),
     ('🏦', 'an overdraft', 'extra money the bank allows you to spend', 'The bank charges for <b>overdrafts</b> now.', 'anoverdraft'),
     ('🏷️', 'a profit margin', 'the difference between the cost of making or buying something and what it\'s sold for', 'The <b>profit margin</b> on these T-shirts is huge!', 'aprofitmargin'),
     ('⚖️', 'to break even', 'to earn just enough to cover the costs of producing a product', 'We need to sell two cars to <b>break even</b>.', 'tobreakeven'),
     ('🔻', 'to make a loss', 'to lose money by spending more than you earn', 'We haven\'t sold enough pineapples. We\'ve <b>made a loss</b>.', 'tomakealoss'),
     ('📒', 'accounts', 'records of money paid into and out of a business', 'We need to make sure the <b>accounts</b> are always up to date.', 'accounts'),
     ('👥', 'overheads', 'the regular costs of running a business, such as wages', 'High <b>overheads</b> make this business difficult to run.', 'overheads')]
B = [('💲', 'cost (US) / cost price (UK)', 'a sales price that covers the costs of producing an item without making a profit', 'I\'m selling these earrings at <b>cost</b> to attract customers.', 'cost'),
     ('🔄', 'cash flow', 'the rate at which money comes into and goes out of a business', 'Our clients need to pay now or we will have a <b>cash flow</b> problem.', 'cashflow'),
     ('⛰️', 'to peak', 'to reach the highest point', 'The prices <b>peaked</b> in June, but they\'re down now.', 'topeak'),
     ('🚪', 'to go out of business', 'to no longer be able to exist as a business', 'It\'s always hard to see a company <b>go out of business</b>.', 'togooutofbusiness'),
     ('⬇️', 'to drop', 'to fall, especially in worth or value', 'When the CEO left, the company\'s value <b>dropped</b>.', 'todrop'),
     ('🛒', 'to undercut competitors', 'to charge less than others who sell the same goods or services as you', 'We need to <b>undercut our competitors</b> or we will lose customers.', 'toundercutcompetitors'),
     ('💱', 'the exchange rate', 'the amount of one currency that you get when you change it for another', 'Changes in the <b>exchange rate</b> make the market uncertain.', 'theexchangerate'),
     ('📊', 'sales figures', 'the amount or value of total sales over a particular period', 'Our <b>sales figures</b> have improved consistently each year.', 'salesfigures'),
     ('🌦️', 'an upturn in the market', 'a change to more positive business conditions', 'Thankfully, there was an <b>upturn in the market</b>.', 'anupturninthemarket'),
     ('🌧️', 'an economic downturn', 'a major decline in economic activity', 'Everyone suffered because of the <b>economic downturn</b> last year.', 'aneconomicdownturn')]
def vc(items):
    h = vcards([(ic, n, d, ex, W(a)) for ic, n, d, ex, a in items], 2)
    return h.replace('class="vgrid two"', 'class="vgrid two tight"')
content('s-v1', 'Vocabulary – Money and Finance (1)', 'vocab', 'Money and finance (1 of 2)', vc(A), 'Click the speaker to hear each phrase. Read the example sentence.')
gapsA = [("The company's", 'income', "fell last year."), ("The initial", 'expenditure', "on technology was huge, but now we can work faster."), ("We have a large", 'budget', "for this movie."),
         ("We must do all we can to avoid", 'getting into debt', "."), ("The bank charges for", 'overdrafts', "now."), ("The", 'profit margin', "on these T-shirts is huge!"),
         ("We need to sell two cars to", 'break even', "."), ("We haven't sold enough pineapples. We've", 'made a loss', "."), ("We need to make sure the", 'accounts', "are always up to date."),
         ("High", 'overheads', "make this business difficult to run.")]
exercise('s-cl1', 'Practice – Complete the Sentences (1)', 'vocab', 'Complete the sentences (1 of 2)', 'Fill in the gaps using the words in the panel. Click a word, then click a gap.',
         [wb_row(i + 1, p, a, post) for i, (p, a, post) in enumerate(gapsA)], 'wb', pre=wb_bank([a for _, a, _ in gapsA]), gid='cl1')
speak('s-sp1', 'Speaking Break – Income and Costs', 'Speaking break: income and costs', 'Answer the questions. Use the phrases from the first list.', [
    'What is the biggest expenditure in your company or your household? Why?',
    'Does your company have a budget for training? What do you know about it?',
    'Why is it important to avoid getting into debt? Give your opinion.',
    'Describe a business that has high overheads. How can it break even?'])

content('s-v2', 'Vocabulary – Money and Finance (2)', 'vocab', 'Money and finance (2 of 2)', vc(B), 'Click the speaker to hear each phrase. Read the example sentence.')

gapsB = [("I'm selling these earrings at", 'cost', "to attract customers."), ("Our clients need to pay now or we will have a", 'cash flow', "problem."), ("The prices", 'peaked', "in June, but they're down now."),
         ("It's always hard to see a company", 'go out of business', "."), ("When the CEO left, the company's value", 'dropped', "."), ("We need to", 'undercut our competitors', "or we will lose customers."),
         ("Changes in the", 'exchange rate', "make the market uncertain."), ("Our", 'sales figures', "have improved consistently each year."), ("Thankfully, there was an", 'upturn in the market', "."),
         ("Everyone suffered because of the", 'economic downturn', "last year.")]
exercise('s-cl2', 'Practice – Complete the Sentences (2)', 'vocab', 'Complete the sentences (2 of 2)', 'Fill in the gaps using the words in the panel. Click a word, then click a gap.',
         [wb_row(i + 1, p, a, post) for i, (p, a, post) in enumerate(gapsB)], 'wb', pre=wb_bank([a for _, a, _ in gapsB]), gid='cl2')

speak('s-sp2', 'Speaking Break – The Market', 'Speaking break: good and bad times', 'Answer the questions. Use the phrases from the second list.', [
    'Think of a company that dropped in value or went out of business. What happened?',
    'Why do some companies undercut their competitors? Is it a good idea?',
    'When did your industry have an upturn in the market, or an economic downturn?',
    'How do changes in the exchange rate affect companies that sell abroad?'])

GOOD, BAD = 'good', 'bad'
sort_slide('s-m1', 'Meaning – Good News or Bad News?', 'vocab', 'Good news or bad news?', 'Click a sentence, then click the box where it belongs.',
           [("Thankfully, there was an upturn in the market.", GOOD), ("Everyone suffered because of the economic downturn.", BAD), ("We haven't sold enough pineapples. We've made a loss.", BAD),
            ("The profit margin on these T-shirts is huge!", GOOD), ("High overheads make this business difficult to run.", BAD), ("Our sales figures have improved consistently each year.", GOOD),
            ("The company's income fell last year.", BAD), ("We have a large budget for this movie.", GOOD)],
           [(GOOD, '<b>Good news</b><br>for a business'), (BAD, '<b>Bad news</b><br>for a business')],
           post=ccqs(('If you break even, do you make a profit?', 'No. You earn just enough to cover your costs.'), ('If a company goes out of business, can it still sell products?', 'No. It is no longer able to exist as a business.')))

S1, S2 = 'first', 'later'
sort_slide('s-pron', 'Pronunciation – Word Stress', 'pron', 'Where is the stress?', 'Click the speaker to hear the word, say it, then click the word and the box with its stress pattern.',
           [("income", S1), ("budget", S1), ("overheads", S1), ("overdraft", S1), ("accounts", S2), ("expenditure", S2), ("exchange", S2), ("economic", S2)],
           [(S1, '<b>Stress on the 1st syllable</b><br>IN-come'), (S2, '<b>Stress later in the word</b><br>ac-COUNTS')],
           aud='<div class="audio-box clips-box"><span class="clips-label">🎧 Listen</span>%s</div>' % ''.join(AL.word(U, '6_1_' + a, l) for a, l in [('income', 'income'), ('abudget', 'budget'), ('overheads', 'overheads'), ('anoverdraft', 'overdraft'), ('accounts', 'accounts'), ('expenditureoutlay', 'expenditure'), ('theexchangerate', 'exchange rate'), ('aneconomicdownturn', 'economic downturn')]))

chat_speak('s-free', 'Speaking – Financial Update', 'Financial update', 'Read the conversation as it goes. When it is your turn, say what you could say.', 'Jordan', [
 ("Can you give me a quick financial update on the company?", 'Give a short overview of the company&rsquo;s income.', "Of course. Overall, our income is up this quarter."),
 ("That's good.<br>What about our costs?", 'Talk about costs.', "Our biggest expenditure is salaries, but our overheads are low."),
 ("Are we going to break even this year?", 'Answer, and say when.', "Yes. We expect to break even by December."),
 ("What about our competitors? Are they undercutting us?", 'Talk about the competition.', "Yes, one competitor has dropped its prices to undercut us."),
 ("How is the market doing?", 'Describe the market.', "There was an upturn this spring, but there could be a downturn next year."),
 ("Do we have enough money in the budget for new equipment?", 'Answer, and give advice about debt.', "Not at the moment. We should avoid getting into debt, so let's wait until next quarter.")])
summary_review('Lesson summary', [('💰', 'Money and finance', ['<mark>income</mark> = money coming in.', '<mark>expenditure</mark> = money going out.', '<mark>overheads</mark> = regular costs, like rent.', '<mark>a budget</mark> = a plan for income and spending.', 'To <mark>break even</mark> = to make no profit and no loss.']), ('📊', 'Good news or bad news?', ['<b>Good:</b> <mark>an upturn in the market</mark>, to <mark>break even</mark>, rising <mark>income</mark>.', '<b>Bad:</b> <mark>an economic downturn</mark>, to <mark>make a loss</mark>, to <mark>get into debt</mark>, to <mark>go out of business</mark>.']), ('🧩', 'Talking about a business situation', ['ex:Our biggest <mark>expenditure</mark> is salaries.', 'ex:We expect to <mark>break even</mark> by December.', 'ex:A competitor wants to <mark>undercut</mark> us.', 'ex:We should avoid <mark>getting into debt</mark>.'])],
       'Give me a short financial update about a real or imaginary company, using at least five new phrases.')
