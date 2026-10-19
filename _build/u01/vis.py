import asyncio, os
from playwright.async_api import async_playwright
OUT=os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','U01-Introductions','index.html'))
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={'width':1366,'height':820})
        await pg.goto('file://'+OUT); await pg.wait_for_timeout(500)
        n=await pg.evaluate('slides.length')
        for i in range(n):
            await pg.evaluate('goTo(%d)'%i); await pg.wait_for_timeout(200)
            r=await pg.evaluate("(function(){var s=slides[%d];var b=s.querySelector('.btn-check');if(!b)return null;var r=b.getBoundingClientRect();return Math.round(r.bottom)})()"%i)
            if r is not None: print(i, await pg.evaluate('slideIds[%d]'%i), 'check bottom', r, 'OK' if r<=768 else 'BELOW FOLD')
        await b.close()
asyncio.run(main())
