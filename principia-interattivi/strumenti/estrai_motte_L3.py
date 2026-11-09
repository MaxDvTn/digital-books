import re,html,sys
from html.parser import HTMLParser
D='/home/claude/src_epub/OEBPS/1508224473918383187_76404-h-%d.htm.xhtml'
class T(HTMLParser):
    BLOCK={'p','div','br','h1','h2','h3','h4','h5','h6','li','tr','table','blockquote'}
    def __init__(s): super().__init__(convert_charrefs=True); s.out=[]; s.skip=0; s.intr=0
    def handle_starttag(s,tag,a):
        if tag in('script','style','head'): s.skip+=1
        if tag=='tr': s.intr=1; s.out.append('\n'); return
        if tag in s.BLOCK and not s.intr: s.out.append('\n')
        if tag in('td','th'): s.out.append(' | ')
        if tag=='img':
            d=dict(a); src=d.get('src','')
            m=re.search(r'_(\d+)\.svg$',src)
            if m: s.out.append(' [SVG %s] '%m.group(1))
            else: s.out.append('\n[FIG: %s]\n'%(d.get('alt') or src.split('/')[-1]))
    def handle_endtag(s,tag):
        if tag in('script','style','head'): s.skip-=1
        if tag=='tr': s.intr=0; s.out.append(' |\n'); return
        if tag in s.BLOCK and not s.intr: s.out.append('\n')
    def handle_data(s,d):
        if not s.skip: s.out.append(d.replace('\n',' ') if s.intr else d)
txt=''
for i in range(19,26):
    t=T(); t.feed(open(D%i,encoding='utf-8').read()); txt+=''.join(t.out)+'\n'
txt=re.sub(r'[ \t\r\f\v]+',' ',txt); txt=re.sub(r' *\n *','\n',txt); txt=re.sub(r'\n{3,}','\n\n',txt)
open('/home/claude/libro3work/motte_L3_tutto.txt','w').write(txt)
