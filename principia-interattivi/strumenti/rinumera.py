#!/usr/bin/env python3
"""Rinumera la parte «b» di un fascicolo diviso perché continui la parte «a».
Uso: rinumera.py PARTE_A.md PARTE_B.md GRUPPO   (es. G5)
Gli identificatori provvisori della parte b (III.Gx.101…) diventano III.Gx.(ultimo_a+1)…
Sposta anche i numeri a tre cifre ≥101 senza prefisso nelle serie («III.G5.104–107», «III.G5.104, 107»)."""
import re, sys
a, b, g = sys.argv[1:4]
ta = open(a, encoding='utf-8').read()
last = max(int(n) for n in re.findall(r'\*\*\[III\.%s\.(\d+)\]\*\*' % g, ta))
off = last + 1 - 101
tb = open(b, encoding='utf-8').read()
def f(n): return '%02d' % (int(n) + off)
pref = r'III\.%s\.' % g
# serie: prefisso + numero, poi separatori e numeri senza prefisso
def serie(m):
    s = m.group(0)
    return re.sub(r'(?<!\d)(1\d\d)(?!\d)', lambda k: f(k.group(1)), s)
tb2 = re.sub(pref + r'1\d\d(?:\s*(?:–|-|,|e|ed|and)\s*(?:' + pref + r')?1\d\d)*', serie, tb)
left = re.findall(pref + r'1\d\d', tb2)
open(b, 'w', encoding='utf-8').write(tb2)
print(f'{b}: ultimo id della parte a = {last}, offset {off}; residui a tre cifre: {len(left)}')
