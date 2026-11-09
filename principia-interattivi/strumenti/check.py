#!/usr/bin/env python3
"""Valida la Parte B di un fascicolo.
Uso: check.py FASCICOLO.md LATINO1.md [LATINO2.md ...] --en MOTTE1.md [MOTTE2.md ...]
Controlla: JSON valido; stringhe 'la' ed 'en' (enunciati e passi) sottostringhe esatte
delle fonti (spazi normalizzati, marcatori di pagina <n> e [FIG n] ignorati);
id unici; identificatori [Sx.yy] presenti nel testo per ogni 'copertura'."""
import sys, re, json

def norm(s):
    s = re.sub(r'\[FIG[^\]]*\]', ' ', s)
    s = re.sub(r'\[SVG \d+\]', ' ', s)
    s = re.sub(r'\s*<[A-Za-z0-9]+>\s*', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()

args = sys.argv[1:]
if '--en' not in args or len(args) < 4:
    print(__doc__); sys.exit(2)
k = args.index('--en')
fasc, la_files, en_files = args[0], args[1:k], args[k+1:]
txt = open(fasc, encoding='utf-8').read()
LA = norm(' '.join(open(f, encoding='utf-8').read() for f in la_files))
EN = norm(' '.join(open(f, encoding='utf-8').read() for f in en_files))

blocks = re.findall(r'```json\s*(.*?)```', txt, re.S)
if not blocks:
    print('ERRORE: nessun blocco ```json``` trovato'); sys.exit(1)
try:
    data = json.loads(blocks[-1])
except Exception as e:
    print('ERRORE JSON:', e); sys.exit(1)

errs, warns, n_steps, ids = [], [], 0, set()
units = data.get('unita') or data.get('corollari') or []
ids_in_text = set(re.findall(r'\*\*\[((?:[IV]+\.)?[SG]\d+\.\d+)\]\*\*', txt))
for u in units:
    uid = u.get('id', '?')
    if uid in ids: errs.append(f'id unita duplicato: {uid}')
    ids.add(uid)
    for c in u.get('copertura', []):
        if c not in ids_in_text: warns.append(f'{uid}: copertura {c} non trovata nel testo')
    en_ = u.get('enunciato', {})
    for fld, SRC in (('la', LA), ('en', EN)):
        v = en_.get(fld)
        if v and norm(v) not in SRC: errs.append(f'{uid} enunciato.{fld} non è sottostringa esatta: {v[:70]!r}')
    for p in u.get('passi', []):
        n_steps += 1
        pid = p.get('id', '?')
        if pid in ids: errs.append(f'id passo duplicato: {pid}')
        ids.add(pid)
        for fld in ('la', 'it', 'en', 'dipende_da', 'figura'):
            if fld not in p: errs.append(f'{pid}: manca il campo {fld}')
        if p.get('la') and norm(p['la']) not in LA: errs.append(f'{pid} la non è sottostringa esatta: {p["la"][:70]!r}')
        if p.get('en') and norm(p['en']) not in EN: warns.append(f'{pid} en non è sottostringa esatta (ammesso solo se spiegato in nota): {p["en"][:60]!r}')
print(f'unità: {len(units)}  passi: {n_steps}  identificatori nel testo: {len(ids_in_text)}')
for w in warns: print('AVVISO', w)
for e in errs: print('ERRORE', e)
print('OK' if not errs else f'{len(errs)} errori')
sys.exit(1 if errs else 0)
