#!/usr/bin/env python3
"""Allinea la traduzione inglese di E. S. Carlos (1880, Project Gutenberg #46036, pubblico dominio)
ai paragrafi di blocchi.json e scrive blocchi_en.json (stessi id, stessa struttura).

  python3 allinea_en.py   (legge ../../fonti_en/carlos1880_sidereal_messenger.txt)

Carlos tiene ogni osservazione di Giove in un solo paragrafo con il rimando «(Fig. n)»;
l'italiano la spezza intorno al disegno. Il taglio cade sul rimando; i casi che non
tornano sono scritti a mano qui sotto (TAGLI e MANUALI). Le note di Carlos, le
didascalie e le «sidenotes» non entrano nel testo.
"""
import json, os, re, sys

QUI = os.path.dirname(os.path.abspath(__file__))
FONTE = os.path.join(QUI, "..", "..", "fonti_en", "carlos1880_sidereal_messenger.txt")
L = open(FONTE, encoding="utf-8").read().split("\n")

def corsivi(t):
    return re.sub(r"_([^_]+)_", r"<i>\1</i>", t)

# ---------------------------------------------------------------- paragrafi di Carlos
inizio = next(i for i, l in enumerate(L) if l.startswith("TO THE MOST SERENE"))
fine = next(i for i, l in enumerate(L) if "KEPLER’S DIOPTRICS" in l and i > inizio)
blocchi, cur = [], []
for l in L[inizio:fine] + [""]:
    if l.strip() == "":
        if cur: blocchi.append(cur); cur = []
    else:
        cur.append(l)
E = []
for b in blocchi:
    t = " ".join(x.strip() for x in b)
    if b[0].startswith("    ") or t.startswith(("[Sidenote", "[Illustration")):
        continue
    t = re.sub(r"\[Sidenote:[^\]]*\]", "", t)
    t = re.sub(r"\[\d+\]", "", t)
    E.append(corsivi(t.strip()))
assert E[8] == "THE ASTRONOMICAL MESSENGER" and E[49].startswith("On the 7th day of January"), "fonte inattesa"

def taglia(t, marca):
    """divide t prima di 'marca' (che resta nel secondo pezzo)"""
    k = t.find(marca)
    if k < 0:
        sys.exit("marca non trovata: " + marca)
    return t[:k].strip(), t[k:].strip()

def j(*xs):
    return " ".join(x.strip() for x in xs)

# ---------------------------------------------------------------- prosa (p001–p029)
tit = next(i for i, l in enumerate(L) if l.startswith("THE ASTRONOMICAL MESSENGER"))
sott = " ".join(l.strip() for l in L[tit + 1:tit + 12] if l.strip() and not l.strip().startswith("[3]"))
sott = re.sub(r"\[\d+\]", "", sott).replace("_", "")
sott = re.sub(r"named\s+THE COSMIAN STARS\.", "named the Cosmian Stars", sott)
M = {}
M["p001"] = "<i>%s</i>" % sott
M["p002"], M["p003"], M["p004"] = E[9], E[10], E[11]
M["p005"], M["p006"] = taglia(E[12], "But that which will excite")
M["p007"] = E[13]
a, b = taglia(E[18], "Let E be the eye")
M["p008"] = j(E[14], E[15], E[16], E[17], a)
M["p009"] = b
M["p010"] = E[19]
a, b = taglia(E[22], "On the fourth or fifth day")
M["p011"] = j(E[20], a.rstrip("—:") + ":")
b, c = taglia(b, "Again, not only are the boundaries")
a, d = taglia(E[24], "This same spot before")
M["p012"], M["p013"], M["p014"] = b, j(c, E[23], a), d
M["p015"], M["p016"] = E[25], E[26]
M["p017"], a = taglia(E[27], "Of this phenomenon, which affords")
M["p018"] = j(a, E[28], E[29], E[30])
a, b = taglia(E[31], "As I often observed")
M["p019"], M["p020"] = a.rstrip("—:") + ":", b
M["p021"] = E[32]
M["p022"] = j(E[33], E[34], E[35], E[36])
M["p023"] = E[37]
M["p024"] = j(E[38], E[40], E[41])
M["p025"], M["p026"] = E[42], E[43]
a, b = taglia(E[46], "First, you have")
M["p027"], M["p028"] = j(E[45], a), j(b, E[47])
M["p029"] = E[48]

# ---------------------------------------------------------------- osservazioni (p030–p136)
italiano = json.load(open(os.path.join(QUI, "blocchi.json"), encoding="utf-8"))
seq, on = [], False
for b in italiano:
    if b.get("id") == "p030": on = True
    if b.get("id") == "p137": break
    if on: seq.append(b["id"] if b["tipo"] == "par" else "F")
gruppi = [[]]
for s in seq:
    if s == "F": gruppi.append([])
    else: gruppi[-1].append(s)

oss = list(E[49:105])
TAGLI = {  # disegni senza rimando nel testo di Carlos
    "two satellites only presented themselves to view in this position,": "two satellites only presented themselves to view in this position (Fig. X),",
    "The satellites appeared in the following configuration.": "The satellites appeared in the following configuration (Fig. X).",
}
for i, p in enumerate(oss):
    for x, y in TAGLI.items():
        oss[i] = oss[i].replace(x, y)
segm = [[]]
for p in oss:
    parti = re.split(r"\s*\(Fig\. [\dX]+\)", p)
    for k, parte in enumerate(parti):
        if k > 0:
            m = re.match(r"^([^.]{0,45}[.:—]+)\s*(.*)$", parte)
            if m and len(m.group(1)) < 45:   # coda breve («with reference to Jupiter.») resta prima del disegno
                segm[-1][-1] = segm[-1][-1].rstrip() + m.group(1)
                parte = m.group(2)
            if segm[-1]:
                segm[-1][-1] = segm[-1][-1].rstrip().rstrip(".:—") + ":"
            segm.append([])
        parte = parte.strip().lstrip(",;:— ").strip()
        if parte:
            segm[-1].append(parte[0].upper() + parte[1:])

for g, s in zip(gruppi[:56], segm[:56]):
    if g[0] == "p030":
        a, b = taglia(s[0], "The position of them")
        M["p030"], M["p031"] = a, b
    elif g[0] == "p032":
        M["p032"] = j(*s)
    elif g[0] == "p035":
        M["p035"], M["p036"] = j(s[0], s[1]), s[2]
    else:
        if len(g) != len(s):
            sys.exit("gruppo %s: %d paragrafi italiani, %d inglesi" % (g, len(g), len(s)))
        for pid, t in zip(g, s):
            M[pid] = t

MANUALI = {   # dal 21 febbraio (seconda parte) al 2 marzo
 "p124": "The satellite to the east was 2´ from Jupiter; Jupiter was 3´ from the next, which was on the west; and this one was 7´ from the satellite further to the west. They were exactly in the same straight line parallel to the ecliptic.",
 "p125": "Feb. 25: 1 h. 30 m. (for on the three previous nights the sky was overcast).—Three satellites appeared:",
 "p126": "Two on the east, which were at a distance of 4´ apart, the same as the distance of the nearer satellite from Jupiter; on the west there was one satellite at a distance of 2´ from Jupiter. They were exactly in the same straight line in the direction of the ecliptic.",
 "p127": "Feb. 26: 0 h. 30 m.—A pair of satellites only were present:",
 "p128": "One on the east, distant 10´ from Jupiter; the other was on the west, at a distance of 6´. The eastern satellite was slightly smaller than the western. At the fifth hour three satellites were visible:",
 "p129": "For, besides the two already noticed, a third satellite was in view, on the west, near Jupiter, very small, which previously had been hidden behind Jupiter, and it was at a distance of 1´ from the planet. But the satellite on the east was seen to be further off than before, being at a distance of 11´ from Jupiter. On this night, for the first time, I determined to observe the motion of Jupiter and the adjacent planets (his satellites) along the zodiac, by reference to some fixed star; for there was a fixed star in view, eastwards of Jupiter, at a distance of 11´ from the satellite on the east, and a little to the south, in the following manner:",
 "p130": "Feb. 27: 1 h. 4 m.—The satellites appeared in the following configuration:",
 "p131": "The satellite furthest to the east was at a distance of 10´ from Jupiter; the next in order was near Jupiter, being at a distance of 0´ 30´´ from the planet. The next satellite was on the western side, at a distance of 2´ 30´´ from Jupiter; and the satellite further to the west was at a distance of 1´ from this. The two satellites near to Jupiter appeared small, especially the satellite on the east; but the satellites furthest off were very bright, particularly that on the west, and they made a straight line in the direction of the ecliptic exactly. The motion of the planets towards the east was plainly seen by reference to the aforesaid fixed star, for Jupiter and his attendant satellites were nearer to it, as may be seen in the accompanying figure. At the fifth hour the satellite on the east, near to Jupiter, was 1´ from the planet.",
 "p132": "Feb. 28: 1 h.—Only two satellites were visible, one on the east, at a distance of 9´ from Jupiter, and another on the west, at a distance of 2´; they were both rather bright, and in the same straight line with Jupiter, and a straight line drawn from the fixed star perpendicular to this straight line fell upon the satellite on the east, as in the figure:",
 "p133": "At the fifth hour a third satellite was seen at a distance of 2´ from Jupiter, on the east, in the position shown in the figure:",
 "p134": "March 1: 0 h. 40 m.—Four satellites, all on the east of the planet, were seen; the satellite nearest to Jupiter was 2´ from the planet; the next 1´ from this; the third was 0´ 20´´ from the second, and was brighter than the others; and the satellite still further to the east was at a distance of 4´ from it, and was smaller than the others. They made a straight line very nearly, only the satellite third from Jupiter was slightly above the line. The fixed star formed with Jupiter and the most easterly satellite an equilateral triangle, as in the figure:",
 "p135": "March 2: 0 h. 40 m.—Three satellites were in attendance, two on the east and one on the west, in the configuration shown in the diagram:",
 "p136": "The satellite furthest to the east was 7´ from Jupiter; from this satellite the next was distant 0´ 30´´, and the satellite on the west was separated from Jupiter by an interval of 2´. The satellites furthest off were brighter and larger than the remaining satellite, which appeared very small. The satellite furthest to the east seemed to be raised a little towards the north, out of the straight line drawn through the other satellites and Jupiter. The fixed star already noticed was at a distance of 8´ from the western satellite, that is, from the perpendicular drawn from that satellite to the straight line drawn through all the system, as shown in the figure given.",
}
for g in gruppi[56:]:
    for pid in g:
        M[pid] = MANUALI[pid]
M["p137"] = E[105]
M["p138"] = j(E[106], E[107], E[108])

# ---------------------------------------------------------------- uscita
out = []
for b in italiano:
    b = dict(b)
    if b["tipo"] == "titolo":
        b["testo"] = {"Avviso Astronomico": "The Astronomical Messenger"}.get(b["testo"], b["testo"])
    elif b["tipo"] == "par" and b["id"] != "p139":
        if b["id"] not in M:
            sys.exit("manca l'inglese per " + b["id"])
        b["testo"], b["note"] = M[b["id"]], []
    out.append(b)
mancanti = [b["id"] for b in italiano if b["tipo"] == "par" and b["id"] not in M and b["id"] != "p139"]
json.dump(out, open(os.path.join(QUI, "blocchi_en.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("paragrafi inglesi:", len(M), "| mancanti:", mancanti)
