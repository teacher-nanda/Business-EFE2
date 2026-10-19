import asyncio, os
from playwright.async_api import async_playwright
OUT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','U01-Introductions','index.html'))
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
  const total=s.querySelectorAll('input.ans-input[data-ans], .circ-opt[data-correct]').length;
  return {wrong, ok};
}
'''
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1366,'height':820})
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
        await pg.goto('file://'+OUT); await pg.wait_for_timeout(500)
        ids=await pg.evaluate('slideIds')
        for sid in ids:
            await pg.evaluate("goToId('%s')"%sid)
            r=await pg.evaluate(JS,sid)
            if r['wrong'] or r['ok']: print(sid,'correct marks =',r['ok'],'| problems:',r['wrong'][:3])
        # wrong-answer tests
        await pg.evaluate("goToId('s-cb17')")
        await pg.evaluate("var i=document.querySelector('#cb17 input.ans-input'); i.value='zzz'; checkSlide('cb17')")
        print('wrong typed flagged:', await pg.evaluate("document.querySelector('#cb17 input.ans-input').classList.contains('wrong')"))
        # typed variants accepted
        variants={'s-cb17':[("Hi James. I am Vanisha. I do not think we have met before.",0),("Hi James, I'm Vanisha. I don’t think we’ve met before!",0),("ashley, i'd like to introduce you to my colleague neil",1),("Ashley, I would like to introduce you to my colleague Neil.",1),("I'm enjoying the presentations. Are you?",2),("Nice to meet you, Bethany. How do you do?",3)]}
        for sid,vs in variants.items():
            for val,idx in vs:
                await pg.evaluate("goToId('%s')"%sid)
                res=await pg.evaluate("(function(v,i){var inp=document.querySelectorAll('#cb17 input.ans-input')[i]; inp.value=v; checkSlide('cb17'); return inp.classList.contains('correct');})(%s,%d)"%(repr(val).replace("'",'"') if "'" not in val else '"'+val.replace('"','\\"')+'"', idx))
                print('variant', repr(val), '->', res)
        # games / extras
        await pg.evaluate("goToId('s-lead')")
        await pg.fill('#bd-name','Nanda'); await pg.fill('#bd-role','Teacher'); await pg.fill('#bd-company','Acme'); await pg.fill('#bd-ask','English')
        print('badge:', await pg.evaluate("document.querySelector('#bd-live [data-bd=name]').textContent"))
        await pg.evaluate("goToId('s-review')")
        print('review badge:', await pg.evaluate("document.querySelector('#bd-review [data-bd=name]').textContent"))
        await pg.evaluate("document.querySelectorAll('#ck-list .check-item').forEach(c=>c.click())")
        print('win shown:', await pg.evaluate("document.getElementById('ck-win').classList.contains('show')"))
        await pg.evaluate("goToId('s-free')")
        seen=set()
        for k in range(12):
            await pg.evaluate("dealNext()"); seen.add(await pg.evaluate("document.querySelector('#deal-card .dc-setting').textContent"))
        print('distinct cards in 12 deals:', len(seen))
        await pg.evaluate("goToId('s-m1'); document.getElementById('notesTA').innerHTML='hello'; saveNotes();")
        print('notes saved:', await pg.evaluate("localStorage.getItem(notesStoreKey)"))
        print('errors',errs)
        await b.close()
asyncio.run(main())
