import re,json,sys
h=open('/home/claude/verifica/index.html').read()
f=open('/home/claude/work/Newton_Principia_IT_03_Leggi.md').read()
norm=lambda s:re.sub(r'\s+',' ',s.replace('’',"'").replace('“','"').replace('”','"').replace('*','')).strip()
F=norm(f)
def lawcard(n):
    m=re.search(r'<h3>Legge '+n+r'</h3><p>(.*?)</p>',h); return norm(m.group(1))
for n,tag in [('I','L01'),('II','L03'),('III','L05')]:
    m=re.search(r'\['+tag+r'\] (.*?)\[L',F); ref=m.group(1).strip()
    print(n, lawcard(n)==ref, '\n  pagina:',lawcard(n),'\n  fasc. :',ref)
enun=norm(re.search(r'<p class="enunciato">(Un corpo.*?)</p>',h).group(1))
ref=norm(re.search(r'\[L08\] (.*?) \[L09\]',F).group(1)); print('CorI enunciato', enun==ref)
L09=norm(re.search(r'\[L09\] (.*?) ### Corollario II',F).group(1))
steps=re.findall(r'\{it:"(.*?)",\s*en:',h[h.index('"leggi": ['):h.index('"lemma-1": [')],re.S)
joined=norm(' '.join(steps)); print('CorI passi == L09:', joined==L09)
if joined!=L09:
    import difflib
    for d in difflib.ndiff([joined],[L09]): print(d[:3000])
