"""Confronto tra i conteggi est/ovest di Galileo (trascritti dal testo) e il modello di Meeus."""
import json, subprocess, itertools
O=json.load(open("osservazioni.json")); G=json.load(open("galileo_conteggi.json"))
js="""const A=require('./astro.js');const O=require('./osservazioni.json');
console.log(JSON.stringify(O.map(([f,m,d,h])=>{const r=A.satelliti(A.jdOsservazione(1610,m,d,h));return r.sat.map(s=>s.X*r.raggioArcmin)})))"""
def modello(dh=0):
    js2=js.replace("A.jdOsservazione(1610,m,d,h)","A.jdOsservazione(1610,m,d,h+%f)"%dh)
    return json.loads(subprocess.check_output(["node","-e",js2]))
def conta(x,soglia,fus):
    v=sorted(a for a in x if abs(a)>soglia); out=[]
    for a in v:
        if out and abs(a-out[-1])<fus: continue
        out.append(a)
    return sum(a<0 for a in out), sum(a>0 for a in out)
def punteggio(mod,soglia,fus,verbose=False):
    ok=0;tot_ok=0
    for (f,*_),x in zip(O,mod):
        e,w=conta(x,soglia,fus); g=G[f]
        ok+= (e,w)==tuple(g); tot_ok+= (e+w)==sum(g)
        if verbose and (e,w)!=tuple(g): print(f, "Galileo",g,"modello",[e,w],[round(a,1) for a in sorted(x)])
    return ok,tot_ok
mod=modello()
print("soglia bagliore / fusione -> concordanze esatte E/O")
for s,fu in itertools.product([0.4,0.6,0.8,1.0],[0.3,0.5,0.7]):
    print(f"  {s}' / {fu}'  ->", punteggio(mod,s,fu))
print("\nsensibilità all'ora (soglia 0.8', fusione 0.5'):")
for dh in [-0.5,0,0.5]:
    print(" ", dh, punteggio(modello(dh),0.8,0.5))
print("\ndiscordanze (0.8', 0.5'):"); punteggio(mod,0.8,0.5,True)
