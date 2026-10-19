import asyncio, os, sys
from playwright.async_api import async_playwright
OUT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','U01-Introductions','index.html'))
SH='/tmp/claude-0/work/shots'; os.makedirs(SH,exist_ok=True)
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1366,'height':820})
        errs=[]; pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None)
        await pg.goto('file://'+OUT); await pg.wait_for_timeout(800)
        n=await pg.evaluate('slides.length')
        for i in range(n):
            await pg.evaluate('goTo(%d)'%i); await pg.wait_for_timeout(500)
            await pg.screenshot(path=SH+'/s%02d.png'%i)
            h=await pg.evaluate("(function(){var s=slides[%d].querySelector('.slide-main');return s?[s.scrollHeight,s.clientHeight]:[0,0]})()"%i)
            print(i,(await pg.evaluate('slideIds[%d]'%i)),h)
        print('errors',errs)
        await b.close()
asyncio.run(main())
