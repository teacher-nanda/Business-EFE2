"""Generic QA for a unit: python3 qa.py U02-Getting-to-know-colleagues [shots]"""
import asyncio, os, sys
from playwright.async_api import async_playwright
folder = sys.argv[1]; shots = len(sys.argv) > 2
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', folder, 'index.html'))
SH = '/tmp/claude-0/work/shots/' + folder; os.makedirs(SH, exist_ok=True)
JS = r'''
(sid)=>{
  const s=document.getElementById(sid);
  s.querySelectorAll('input.ans-input[data-ans]').forEach(i=>{ i.value=i.dataset.ans; });
  s.querySelectorAll('.circ-opt[data-correct]').forEach(b=>{ if(b.textContent.trim()===b.dataset.correct) b.click(); });
  s.querySelectorAll('.match-item[data-side="left"]').forEach(l=>{ const r=s.querySelector('.match-item[data-side="right"][data-pair="'+l.dataset.pair+'"]'); l.click(); if(r) r.click(); });
  s.querySelectorAll('.wb-blank:not(.is-example)').forEach(b=>{ const t=[...s.querySelectorAll('.wb-tile')].find(x=>!x.classList.contains('used') && !x.classList.contains('example-used') && x.dataset.val===b.dataset.ans); if(t){ t.click(); b.click(); } });
  s.querySelectorAll('.classify-chip[data-ans]').forEach(c=>{ c.click(); const col=[...s.querySelectorAll('.classify-col')].find(x=>x.dataset.target===c.dataset.ans); if(col) col.click(); });
  s.querySelectorAll('.btn-check').forEach(b=>b.click());
  const wrong=[...s.querySelectorAll('.wrong,.wrongpair,.empty-warn')].map(e=>e.outerHTML.slice(0,90));
  const ok=s.querySelectorAll('.correct,.correctpair,.placed.correct').length;
  const exp=s.querySelectorAll('input.ans-input[data-ans], .circ-opt[data-correct]:not(.x)').length;
  const groups=new Set([...s.querySelectorAll('.circ-opt[data-correct]')].map(b=>b.dataset.group)).size;
  const inputs=s.querySelectorAll('input.ans-input[data-ans]').length;
  const chips=s.querySelectorAll('.classify-chip').length, pairs=s.querySelectorAll('.match-item[data-side=left]').length, blanks=s.querySelectorAll('.wb-blank:not(.is-example)').length;
  return {wrong, ok, expected: groups+inputs+chips+pairs+blanks};
}
'''
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1366, 'height': 820})
        errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
        await pg.goto('file://' + OUT); await pg.wait_for_timeout(600)
        ids = await pg.evaluate('slideIds'); bad = 0
        for i, sid in enumerate(ids):
            await pg.evaluate("goToId('%s')" % sid); await pg.wait_for_timeout(120 if shots else 0)
            r = await pg.evaluate(JS, sid)
            vis = await pg.evaluate("(function(){var s=slides[%d];var b=s.querySelector('.btn-check');if(!b)return null;return Math.round(b.getBoundingClientRect().bottom)})()" % i)
            h = await pg.evaluate("(function(){var s=slides[%d].querySelector('.slide-main');return s?[s.scrollHeight,s.clientHeight]:[0,0]})()" % i)
            flag = ''
            if r['wrong']: flag += ' PROBLEMS ' + str(r['wrong'][:2]); bad += 1
            if r['expected'] != 0 and r['ok'] < r['expected']: flag += ' LOW-OK'; bad += 1
            if vis is not None and vis > 768: flag += ' [check below fold %d]' % vis
            if r['ok'] or flag or vis: print('%2d %-12s ok=%-3d exp=%-3d scroll=%s%s' % (i, sid, r['ok'], r['expected'], h, flag))
            if shots:
                await pg.evaluate("goToId('%s')" % sid); await pg.reload(); await pg.wait_for_timeout(300)
                await pg.evaluate("goToId('%s')" % sid); await pg.wait_for_timeout(250)
                await pg.screenshot(path=SH + '/s%02d.png' % i)
        # alt acceptance: first alternative of every typed answer is accepted
        n = await pg.evaluate("""(function(){var bad=[];document.querySelectorAll('input.ans-input[data-alt]').forEach(function(i){var a=(i.dataset.alt||'').split('|')[0]; if(!a) return; i.value=a; var sid=i.closest('.slide').id; i.className='ans-input'; var g=i.closest('.fixed-two-col'); if(!g) return; checkSlide(g.id); if(!i.classList.contains('correct')) bad.push(a);}); return bad;})()""")
        print('alt not accepted:', n[:5])
        await pg.evaluate("goToId('s-review')")
        await pg.evaluate("document.querySelectorAll('#ck-list .check-item').forEach(c=>c.click())")
        print('win shown:', await pg.evaluate("document.getElementById('ck-win').classList.contains('show')"))
        if 's-free' in ids:
            await pg.evaluate("goToId('s-free')")
            tot = await pg.evaluate("document.querySelectorAll('#s-free-chat .b').length")
            for k in range(tot + 2):
                await pg.evaluate("chatNext('s-free')")
            print('chat bubbles shown:', await pg.evaluate("document.querySelectorAll('#s-free-chat .b.show').length"), 'of', tot)
        print('clip buttons:', await pg.evaluate("document.querySelectorAll('.clip').length"), 'audio tags:', await pg.evaluate("document.querySelectorAll('audio[src]').length"))
        print('errors', errs, 'problems', bad)
        await b.close()
asyncio.run(main())
