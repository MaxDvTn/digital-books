import asyncio, json, sys
sys.path.insert(0,'/home/claude/verifica/script')
src=open('/home/claude/verifica/script/browser.py').read()
route_code=src[src.index('JX='):src.index('async def main')]
from playwright.async_api import async_playwright
exec(route_code)
async def main():
  async with async_playwright() as p:
    br=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox']); page=await br.new_page(viewport={'width':375,'height':812})
    errs=[]; page.on('pageerror',lambda e: errs.append(str(e))); page.on('console',lambda m: errs.append(m.type+': '+m.text))
    await page.route('**/*', route)
    await page.goto('file:///home/claude/verifica/index_v041.html#leggi'); await page.wait_for_timeout(1500)
    js=lambda s: page.evaluate(s)
    print('ERR', errs, await js('()=>typeof JXG+" "+document.title'))
    r={}
    # passo 0, allinea B
    await js("()=>{const e=VIEWS['leggi'].el; e.B.moveTo([1.4,-3.4]); VIEWS['leggi'].board.update();}")
    r['step0_aligned_visible']=await js("()=>VIEWS['leggi'].board.objectsList.filter(o=>o.elType==='text'&&/allineati/.test(o.plaintext||'')).map(o=>o.visProp.visible)")
    await js("()=>setStep('leggi',2)")
    r['step2_aligned_visible']=await js("()=>VIEWS['leggi'].board.objectsList.filter(o=>o.elType==='text'&&/allineati/.test(o.plaintext||'')).map(o=>o.visProp.visible)")
    r['live']=await js("()=>document.querySelector('#live').textContent")
    await js("()=>{const e=VIEWS['leggi'].el; e.B.moveTo([4.2,3.2]); VIEWS['leggi'].board.update();}")
    r['step2_normal_visible']=await js("()=>VIEWS['leggi'].board.objectsList.filter(o=>o.elType==='text'&&/allineati/.test(o.plaintext||'')).map(o=>o.visProp.visible)")
    await js("()=>{const e=VIEWS['leggi'].el; e.B.moveTo([1.4,-3.4]); VIEWS['leggi'].board.update();}")
    await page.screenshot(path='/home/claude/verifica/leggi_v041_375.png')
    r['errors']=errs
    print(json.dumps(r,ensure_ascii=False,indent=1)); await br.close()
asyncio.run(main())
