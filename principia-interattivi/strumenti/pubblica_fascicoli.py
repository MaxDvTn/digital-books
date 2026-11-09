#!/usr/bin/env python3
"""Crea traduzione-pubblica/ dai fascicoli di traduzione/, svuotando i campi
"la" della Parte B (frasi della trascrizione latina del Newton Project, che non
si pubblica finché non se ne chiariscono le condizioni d'uso).

Uso:  python3 strumenti/pubblica_fascicoli.py   (dalla cartella principia-interattivi)
"""
import pathlib, re

QUI = pathlib.Path(__file__).resolve().parent.parent
SRC, DST = QUI / "traduzione", QUI / "traduzione-pubblica"
CAMPO_LA = re.compile(r'("la"\s*:\s*)"(?:[^"\\]|\\.)*"')
AVVISO = ("> **Copia pubblica.** In questa versione i campi `\"la\"` della Parte B sono "
          "vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non "
          "si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.\n\n")

DST.mkdir(exist_ok=True)
totale = 0
for f in sorted(SRC.glob("*.md")):
    testo = f.read_text(encoding="utf-8")
    nuovo, n = CAMPO_LA.subn(r'\1""', testo)
    totale += n
    (DST / f.name).write_text((AVVISO if n else "") + nuovo, encoding="utf-8")
    print(f"{f.name}: {n} campi latini svuotati")
print(f"Totale: {totale}")
