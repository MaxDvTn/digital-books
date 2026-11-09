import asyncio, json, sys
from playwright.async_api import async_playwright
JX='/tmp/dl/jx/package/distrib/jsxgraphcore.js'; MJ='/tmp/dl/mj/package/es5/'
URL='file:///home/claude/verifica/index.html'
async def route(r):
    u=r.request.url
    if 'jsxgraph@1.10.1/distrib/jsxgraphcore.js' in u: return await r.fulfill(path=JX, content_type='application/javascript')
    if 'mathjax@3.2.2/es5/' in u:
        rel=u.split('mathjax@3.2.2/es5/')[1].split('?')[0]
        try: return await r.fulfill(path=MJ+rel, content_type='application/javascript')
        except Exception: return await r.abort()
    if u.startswith('file:') or u.startswith('data:'): return await r.continue_()
    return await r.abort()
async def main():
    async with async_playwright() as p:
        br=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        res={}
        for name,vp in [('desktop',{'width':1280,'height':900}),('mobile',{'width':375,'height':740})]:
            ctx=await br.new_context(viewport=vp, device_scale_factor=2 if name=='mobile' else 1, is_mobile=(name=='mobile'), has_touch=(name=='mobile'))
            page=await ctx.new_page(); errs=[]
            page.on('console', lambda m: errs.append(f'{m.type}: {m.text}') if m.type in ('error','warning') else None)
            page.on('pageerror', lambda e: errs.append('PAGEERROR: '+str(e)))
            await page.route('**/*', route)
            await page.goto(URL+'#leggi'); await page.wait_for_timeout(1500)
            R={}
            # porta al passo 3 (indice 2) per vedere il parallelogramma
            await page.evaluate('setStep("leggi",2)'); await page.wait_for_timeout(300)
            js_state='''()=>{const V=VIEWS["leggi"],b=V.board; const t=b.objectsList.find(o=>o.elType==="text"&&String(o.plaintext||o.content||"").includes("degenera"));
              const r=t&&t.rendNode; const bb=r?r.getBoundingClientRect():null; const box=document.getElementById("b-leggi").getBoundingClientRect();
              return {vis:t?!!t.visProp.visible:null, disp:r?getComputedStyle(r).display+"/"+getComputedStyle(r).visibility:null, rect:bb?[bb.left-box.left,bb.top-box.top,bb.width,bb.height].map(x=>Math.round(x)):null, box:[Math.round(box.width),Math.round(box.height)], B:[V.el.B.X(),V.el.B.Y()]};}'''
            R['iniziale']=await page.evaluate(js_state)
            # trascinamento reale col mouse/touch: da B a un punto della retta AC (s=1.4)
            async def scr(x,y):
                return await page.evaluate(f'(()=>{{const b=VIEWS["leggi"].board; const c=new JXG.Coords(JXG.COORDS_BY_USER,[{x},{y}],b); const r=document.getElementById("b-leggi").getBoundingClientRect(); return [r.left+c.scrCoords[1], r.top+c.scrCoords[2]];}})()')
            await page.evaluate('document.getElementById("b-leggi").scrollIntoView()')
            s0=await scr(4.2,3.2); s1=await scr(0.7*0.75, 3-3.2*0.75)
            # B verso il prolungamento di CA oltre A (s=-0.6) -> dentro il riquadro
            await page.mouse.move(*s0); await page.mouse.down()
            for k in range(1,21): await page.mouse.move(s0[0]+(s1[0]-s0[0])*k/20, s0[1]+(s1[1]-s0[1])*k/20)
            await page.mouse.up(); await page.wait_for_timeout(300)
            R['dopo_drag_su_AC']=await page.evaluate(js_state)
            await page.screenshot(path=f'/home/claude/verifica/leggi_{name}_degenere.png')
            # moveTo esatto sulla retta, poi via
            await page.evaluate('(()=>{const e=VIEWS["leggi"].el; e.B.moveTo([0.7*0.5, 3-3.2*0.5]); VIEWS["leggi"].board.update();})()')
            R['moveTo_su_AC']=await page.evaluate(js_state)
            await page.evaluate('(()=>{const e=VIEWS["leggi"].el; e.B.moveTo([4.2,3.2]); VIEWS["leggi"].board.update();})()')
            R['quasi_soglia_sin0.05']=await page.evaluate('(()=>{const e=VIEWS["leggi"].el; const th=Math.atan2(-3.2,0.7)+Math.asin(0.05); e.B.moveTo([2*Math.cos(th),3+2*Math.sin(th)]); VIEWS["leggi"].board.update(); return VIEWS["leggi"].board.objectsList.find(o=>o.elType==="text"&&String(o.plaintext||"").includes("degenera")).visProp.visible;})()')
            R['oltre_soglia_sin0.07']=await page.evaluate('(()=>{const e=VIEWS["leggi"].el; const th=Math.atan2(-3.2,0.7)+Math.asin(0.07); e.B.moveTo([2*Math.cos(th),3+2*Math.sin(th)]); VIEWS["leggi"].board.update(); return VIEWS["leggi"].board.objectsList.find(o=>o.elType==="text"&&String(o.plaintext||"").includes("degenera")).visProp.visible;})()')
            await page.evaluate('(()=>{const e=VIEWS["leggi"].el; e.B.moveTo([4.2,3.2]); VIEWS["leggi"].board.update();})()')
            R['ripristino']=await page.evaluate(js_state)
            # passo 0 (C nascosto) con B allineato
            await page.evaluate('setStep("leggi",0); VIEWS["leggi"].el.B.moveTo([0.35,1.4]); VIEWS["leggi"].board.update();')
            R['passo1_C_nascosto_B_allineato']=await page.evaluate(js_state)
            await page.evaluate('VIEWS["leggi"].el.B.moveTo([4.2,3.2]); VIEWS["leggi"].board.update(); setStep("leggi",0)')
            # conteggio aggiornamenti: un update produce un solo evento?
            R['update_count']=await page.evaluate('(()=>{const b=VIEWS["leggi"].board; let n=0; const h=()=>n++; b.on("update",h); VIEWS["leggi"].el.B.moveTo([0.35,1.4]); b.update(); VIEWS["leggi"].el.B.moveTo([4.2,3.2]); b.update(); b.off("update",h); return n;})()')
            # passi: testi e alt
            R['alt_leggi']=await page.evaluate('STEPS["leggi"].map((s,i)=>{setStep("leggi",i); return document.getElementById("b-leggi").getAttribute("aria-label")===s.alt;})')
            # animazione
            await page.click('#leggi-play'); await page.wait_for_timeout(2600)
            for v in ['lemma-1','prop-1','prop-11']:
                await page.goto(URL+'#'+v); await page.wait_for_timeout(1200)
                n=await page.evaluate(f'STEPS["{v}"].length')
                for i in range(n):
                    await page.evaluate(f'setStep("{v}",{i})'); await page.wait_for_timeout(120)
                await page.screenshot(path=f'/home/claude/verifica/{v}_{name}.png')
                R[v+'_steps']=n
                R[v+'_chips']=await page.evaluate('Array.from(document.querySelectorAll(".view.active .chip")).map(c=>c.className+" | "+c.textContent.replace(/\\s+/g," ").trim()).slice(0,14)')
            R['errors']=errs
            res[name]=R
            await ctx.close()
        await br.close()
        print(json.dumps(res,indent=1,ensure_ascii=False))
asyncio.run(main())
