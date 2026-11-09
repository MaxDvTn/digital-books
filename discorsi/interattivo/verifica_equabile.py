#!/usr/bin/env python3
"""Verifica numerica della scheda «Il moto equabile» (Teorema I del moto equabile).

Calcolo indipendente in aritmetica esatta (Fraction) e confronto con il modello JavaScript
della pagina (equabile_modello.js, eseguito con node). Uso: python3 verifica_equabile.py
"""
import json, os, random, subprocess, sys
from fractions import Fraction as F

QUI = os.path.dirname(os.path.abspath(__file__))
errori = []
_conta = [0]
def esito(msg):
    """Stampa SUPERATO solo se la sezione non ha aggiunto errori."""
    print(("SUPERATO  " if len(errori) == _conta[0] else "FALLITO   ") + msg)
    _conta[0] = len(errori)
def controlla(cond, msg):
    if not cond:
        errori.append(msg)

def sgn(x):
    return (x > 0) - (x < 0)

# 1. Teorema I: con la stessa velocità, per ogni m, n i confronti dei moltiplici coincidono (Euclide V def. 5)
random.seed(1638)
for _ in range(1000):
    AB = F(random.randint(1, 40), random.randint(1, 12))
    BC = F(random.randint(1, 40), random.randint(1, 12))
    v = F(random.randint(1, 20), random.randint(1, 10))
    DE, EF = AB / v, BC / v
    for m in range(1, 31):
        for n in range(1, 31):
            controlla(sgn(m * AB - n * BC) == sgn(m * DE - n * EF), "discordanza con stessa velocità %s %s %s %d %d" % (AB, BC, v, m, n))
esito("1. stessa velocità: 1000 configurazioni × 900 coppie, confronti sempre concordi")

# 2. Controprova: su BC velocità k·v con k < 1. Esiste una coppia discorde (m, n ≤ N) se e solo se
#    esiste m, n con n·BC ≤ m·AB ≤ n·BC/k: allora GB ≥ BH ma IE ≤ EK, con almeno un confronto diverso.
k = F(4, 5)
for AB, BC in [(F(2), F(3)), (F(1), F(1)), (F(7, 2), F(1, 2))]:
    v = F(1)
    DE, EF = AB / v, BC / (v * k)
    disc = [(m, n) for m in range(1, 13) for n in range(1, 13) if sgn(m * AB - n * BC) != sgn(m * DE - n * EF)]
    attese = [(m, n) for m in range(1, 13) for n in range(1, 13) if n * BC <= m * AB <= n * BC / k]
    controlla(disc == attese, "controprova: discordi %s, attese %s" % (disc[:5], attese[:5]))
    controlla(len(disc) > 0, "controprova senza discordanze per AB=%s BC=%s" % (AB, BC))
esito("2. controprova: le caselle discordi sono quelle con n·BC ≤ m·AB ≤ n·BC/k")

# 3. Avvertenza: il mobile a scatti percorre spazi eguali in ogni battuta, ma non in ogni mezza battuta
VELOCE = F(4, 5)
def pos(tipo, t):
    if tipo == "equabile":
        return t
    k_ = t.numerator // t.denominator   # parte intera (t >= 0)
    f = t - k_
    return k_ + (VELOCE * (f / F(1, 2)) if f < F(1, 2) else VELOCE + (1 - VELOCE) * ((f - F(1, 2)) / F(1, 2)))
for parti, eguali_scatti in [(1, True), (2, False), (3, False), (4, False), (5, False), (6, False)]:
    sp = [pos("scatti", F(i + 1, parti)) - pos("scatti", F(i, parti)) for i in range(4 * parti)]
    se = [pos("equabile", F(i + 1, parti)) - pos("equabile", F(i, parti)) for i in range(4 * parti)]
    controlla(len(set(se)) == 1, "equabile non eguale con %d parti" % parti)
    controlla((len(set(sp)) == 1) == eguali_scatti, "scatti con %d parti: %s" % (parti, sp[:4]))
esito("3. avvertenza: a scatti eguale solo con la battuta intera")

# 4. Il modello JavaScript dà gli stessi esiti
codice = r"""
const E = require(process.argv[1]);
const out = [];
for (const [AB, BC, v, k] of JSON.parse(process.argv[2])) {
  const g = E.griglia(AB, BC, v, 12, k);
  out.push(g.celle.map(c => [c.spazi, c.tempi]));
}
out.push([1,2,3,4,5,6].map(p => E.tuttiEguali(E.spaziInParti("scatti", 4, p))));
out.push(E.spaziInParti("scatti", 1, 2));
console.log(JSON.stringify(out));
"""
casi = [[2, 3, 1, 1], [2, 3, 1, 0.8], [1.5, 0.5, 2, 1], [3.5, 2, 0.75, 1], [2 ** 0.5 * 2, 2, 1, 1]]
r = subprocess.run(["node", "-e", codice, os.path.join(QUI, "equabile_modello.js"), json.dumps(casi)], capture_output=True, text=True)
controlla(r.returncode == 0, "node: " + r.stderr[:300])
if r.returncode == 0:
    js = json.loads(r.stdout)
    for (AB, BC, v, kk), celle in zip(casi, js):
        ABf, BCf, vf, kf = F(AB), F(BC), F(v), F(kk)
        if abs(AB - 2 ** 0.5 * 2) < 1e-12:   # √2: nessuna eguaglianza possibile, si confronta con un razionale molto vicino
            ABf = F(2) * F(14142135623730951, 10 ** 16)
        DE, EF = ABf / vf, BCf / (vf * kf)
        py = [[sgn(m * ABf - n * BCf), sgn(m * DE - n * EF)] for m in range(1, 13) for n in range(1, 13)]
        controlla(py == celle, "JS ≠ Python per %s" % [AB, BC, v, kk])
    controlla(js[-2] == [True, False, False, False, False, False], "JS avvertenza: %s" % js[-2])
    controlla(all(abs(a - b) < 1e-12 for a, b in zip(js[-1], [0.8, 0.2])), "JS mezze battute: %s" % js[-1])
esito("4. modello JavaScript confrontato con il calcolo esatto su %d casi" % len(casi))

# 5. Dati della dimostrazione: latino e traduzione allineati, passi che citano frasi esistenti
D = json.load(open(os.path.join(QUI, "dimostrazioni", "ME-P1.json"), encoding="utf-8"))
controlla(all(f["la"] and f["it"] for f in D["frasi"]), "frasi senza latino o senza traduzione")
usate = sorted(i for p in D["passi"] for i in p["frasi"])
controlla(usate == list(range(len(D["frasi"]))), "ogni frase deve comparire in un solo passo: %s" % usate)
esito("5. %d frasi latine, tutte tradotte e tutte usate nei %d passi" % (len(D["frasi"]), len(D["passi"])))

if errori:
    print("\nFALLITO:", len(errori))
    for e in errori[:20]:
        print(" -", e)
    sys.exit(1)
print("\nTutti i controlli superati.")
