import sys, email, re, html
from email import policy
from html.parser import HTMLParser

class T(HTMLParser):
    BLOCK = {'p','div','br','h1','h2','h3','h4','h5','h6','li','tr','table','blockquote'}
    def __init__(self):
        super().__init__(convert_charrefs=True); self.out=[]; self.skip=0
    def handle_starttag(self, tag, a):
        if tag in ('script','style','head'): self.skip+=1
        if tag in self.BLOCK: self.out.append('\n')
        if tag=='img':
            d=dict(a); alt=d.get('alt') or ''
            self.out.append('[IMG:%s|%s]'%(d.get('src','')[-40:],alt))
    def handle_endtag(self, tag):
        if tag in ('script','style','head'): self.skip-=1
        if tag in self.BLOCK: self.out.append('\n')
    def handle_data(self, d):
        if not self.skip: self.out.append(d)

def totext(h):
    t=T(); t.feed(h); s=''.join(t.out)
    s=re.sub(r'[ \t\r\f\v]+',' ',s); s=re.sub(r'\n\s*\n+','\n\n',s)
    return s.strip()

mode, src, dst = sys.argv[1:4]
if mode=='mht':
    msg=email.message_from_bytes(open(src,'rb').read(), policy=policy.default)
    parts=[p for p in msg.walk() if p.get_content_type()=='text/html']
    h=parts[0].get_content()
else:
    h=open(src,encoding='utf-8').read()
open(dst,'w',encoding='utf-8').write(totext(h))
