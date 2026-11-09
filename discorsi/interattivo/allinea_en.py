#!/usr/bin/env python3
"""Allinea la traduzione inglese di H. Crew e A. de Salvio (Dialogues Concerning Two New Sciences,
Macmillan 1914, pubblico dominio; trascrizione della Online Library of Liberty, EPUB in
../../fonti_en/crew1914_two_new_sciences_oll.epub) ai blocchi di blocchi.json e scrive blocchi_en.json.

Àncore, nell'ordine: titoli, battute (389 in entrambe le lingue, stesso parlante), enunciati del
trattato (abbinati per tipo e numero: Definition, Axiom n, Theorem/Problem…, Proposition n,
Corollary, Scholium, Lemma) e rimandi alle proposizioni della Giornata Seconda. Tra due àncore
i paragrafi inglesi si distribuiscono sui blocchi italiani in proporzione alla lunghezza; quando
l'inglese ha più testo (le dimostrazioni, che l'ed. UTET omette) il blocco riceve più paragrafi
separati da una riga vuota. Note a piè di pagina, figure e numeri di pagina dell'EPUB sono tolti.
"""
import json, os, re, sys, zipfile
from bs4 import BeautifulSoup, NavigableString, Tag

QUI = os.path.dirname(os.path.abspath(__file__))
EPUB = os.path.join(QUI, "..", "..", "fonti_en", "crew1914_two_new_sciences_oll.epub")

# ---------------------------------------------------------------- inglese: sequenza di elementi
soup = BeautifulSoup(zipfile.ZipFile(EPUB).read("Galileo_0416.html").decode("utf-8"), "lxml")
for x in soup.select("span.pb, div.figure, div.type-figure, div.type-footnote, a.footnote-link"):
    x.decompose()

def inline(el):
    out = []
    for c in el.children:
        if isinstance(c, NavigableString):
            out.append(str(c).replace("<", "&lt;").replace(">", "&gt;"))
        elif isinstance(c, Tag):
            cls, dentro = " ".join(c.get("class", [])), inline(c)
            out.append("<i>%s</i>" % dentro if "ital" in cls else "<sub>%s</sub>" % dentro if cls == "sub"
                       else "<sup>%s</sup>" % dentro if cls == "sup" else " " if c.name == "br" else dentro)
    return "".join(out)

pul = lambda t: re.sub(r"\s+", " ", t).strip()
EN = []
def visita(el):
    for c in el.children:
        if not isinstance(c, Tag):
            continue
        if c.name in ("h1", "h2", "h3", "h4"):
            EN.append(["H", pul(c.get_text(" "))])
        elif "sp" in c.get("class", []):
            sp = c.find("div", class_="speaker")
            EN.append(["SP", pul(sp.get_text()) if sp else "?", [pul(inline(p)) for p in c.find_all("p") if pul(inline(p))]])
        elif c.name == "p":
            t = pul(inline(c))
            if t:
                EN.append(["P", t])
        elif c.name in ("div", "section", "blockquote"):
            if "table-wrap" in " ".join(c.get("class", [])):
                EN.append(["P", "[%s]" % "Table"])
                continue
            visita(c)
visita(soup.body)
inizio = next(i for i, x in enumerate(EN) if x[0] == "H" and x[1].startswith("TO THE MOST ILLUSTRIOUS"))
EN = [x for x in EN[inizio:] if not (x[0] == "H" and x[1] in ("TABLE OF CONTENTS", "TWO NEW SCIENCES BY GALILEO"))]
# il sommario (tra «TABLE OF CONTENTS» e «FIRST DAY») non serve
a = next(i for i, x in enumerate(EN) if x[0] == "H" and x[1].startswith("THE PUBLISHER"))
b = next(i for i, x in enumerate(EN) if x[0] == "H" and x[1].startswith("FIRST DAY"))
pub = [x for x in EN[a:b] if x[0] == "P"][:5]
EN = EN[:a + 1] + pub + EN[b:]

CORREZIONI_TITOLI = {"Propositionhi VI": "Proposition VI", "Theoremposition. Pro VII": "Theorem. Proposition VII",
                     "Theorem II, Proposition II,": "Theorem II, Proposition II"}
ROMANI = {r: i for i, r in enumerate("I II III IV V VI VII VIII IX X XI XII XIII XIV XV XVI XVII XVIII XIX XX XXI XXII XXIII XXIV XXV XXVI XXVII XXVIII XXIX XXX XXXI XXXII XXXIII XXXIV XXXV XXXVI XXXVII XXXVIII".split(), 1)}

def chiave_en(h):
    h = CORREZIONI_TITOLI.get(h, h)
    u = h.upper()
    for k, t in [("FIRST DAY", "Giornata Prima"), ("SECOND DAY", "Giornata Seconda"), ("THIRD DAY", "Giornata Terza"),
                 ("FOURTH DAY", "Giornata Quarta"), ("UNIFORM MOTION", "DEL MOTO EQUABILE"),
                 ("NATURALLY ACCELERATED", "DEL MOTO NATURALMENTE ACCELERATO"), ("THE MOTION OF PROJECTILES", "DEL MOTO DEI PROIETTI"),
                 ("APPENDIX", "Appendice"), ("TO THE MOST ILLUSTRIOUS", "Allo Illustrissimo Signore"), ("THE PUBLISHER", "Lo Stampatore a i Lettori")]:
        if u.startswith(k):
            return ("T", t), h
    m = re.search(r"Proposition\s+([IVXL]+)", h)
    if m:
        return ("E", "prop", ROMANI[m.group(1)]), h
    for k, g in [("DEFINITION", "definizione"), ("CAUTION", "avvertenza"), ("COROLLARY", "corollario"), ("SCHOLIUM", "scolio"), ("LEMMA", "lemma")]:
        if u.startswith(k):
            return ("E", g, None), h
    m = re.match(r"AXIOM\s+([IVX]+)", u)
    if m:
        return ("E", "assioma", ROMANI[m.group(1)]), h
    return None, h

# ---------------------------------------------------------------- italiano: àncore
IT = json.load(open(os.path.join(QUI, "blocchi.json"), encoding="utf-8"))
def chiave_it(b):
    if b["tipo"] == "titolo":
        return ("T", b["testo"])
    if b["tipo"] == "battuta":
        return ("B", b["voce"])
    if b["tipo"] == "rimando":
        if b["testo"].startswith("Corol"):
            return ("E", "corollario", None)
        return ("E", "prop", ROMANI[re.search(r"([IVXL]+)$", b["testo"]).group(1)])
    if b["tipo"] == "enunciato" and b["genere"] != "citato":
        g = b["genere"]
        if g in ("teorema", "problema"):
            return ("E", "prop", int(re.search(r"Proposizione (\d+)", b["intestazione"]).group(1)))
        if g == "assioma":
            return ("E", "assioma", int(re.search(r"(\d+)", b["intestazione"]).group(1)))
        return ("E", g, None)
    return None

# sequenza inglese con chiavi; le battute hanno chiave per parlante
NORM = {"SALV.": "Salv.", "SAGR.": "Sagr.", "SALVIATI.": "Salv."}
seq_en = []
for x in EN:
    if x[0] == "SP":
        seq_en.append([("B", NORM.get(x[1], x[1])), x[2], None])
    elif x[0] == "H":
        k, h = chiave_en(x[1])
        seq_en.append([k, [], h])        # k None: titolo senza corrispondente, diventa testo
    else:
        seq_en.append([None, [x[1]], None])

# abbinamento delle àncore: per ogni àncora italiana, la prima inglese con la stessa chiave
abb, j = {}, 0
for i, b in enumerate(IT):
    k = chiave_it(b)
    if not k:
        continue
    if k[0] == "T" and k[1] in ("Dedica e Avviso ai Lettori",):
        continue
    jj = j
    while jj < len(seq_en) and seq_en[jj][0] != k:
        if seq_en[jj][0] and seq_en[jj][0][0] == "B":   # non si salta mai una battuta
            jj = len(seq_en); break
        jj += 1
    if jj < len(seq_en):
        abb[i] = jj; j = jj + 1
    elif k[0] == "B":
        sys.exit("battuta non abbinata: blocco %d" % i)
print("àncore italiane abbinate:", len(abb), "di", sum(1 for b in IT if chiave_it(b)))
print("  non abbinate:", [(i, IT[i].get("id"), chiave_it(IT[i])) for i, b in enumerate(IT) if chiave_it(b) and i not in abb])

# ---------------------------------------------------------------- distribuzione
def frasi(t):
    # non si taglia dopo «Fig.», «Prop.», «q. e.», «i. e.» e simili
    t = re.sub(r"\b(Fig|Figs|Prop|Props|Cor|Lib|vol|i\. e|e\. g|q\. e|ch|p|pp)\.\s", lambda m: m.group(0).replace(" ", "\u00a0"), t)
    return [x.replace("\u00a0", " ") for x in re.split(r"(?<=[.;:?!])\s+(?=[A-Z“(\[<])", t) if x]

def gettoni(t):
    """segni indipendenti dalla lingua: lettere dei punti geometrici e numeri"""
    t = re.sub(r"<i>([a-z]{1,4})</i>", lambda m: " " + m.group(1).upper() + " ", t)
    lett = re.findall(r"\b[A-Z]{2,5}\b", re.sub(r"<[^>]+>", " ", t))
    num = re.findall(r"\b\d{2,}\b", t)
    return set(x for x in lett if x not in ("SALV", "SAGR", "SIMP", "II", "III", "IV", "VI", "VII", "VIII", "IX", "XI", "XII")) | set(num)

def distribuisci(lung_it, paragrafi, testi_it=None):
    """assegna le frasi inglesi (in ordine) ai blocchi italiani: programmazione dinamica che
    premia i segni in comune (lettere dei punti, numeri) e la posizione relativa nel segmento"""
    k = len(lung_it)
    if k == 0:
        return []
    pezzi = [(f, n) for n, p in enumerate(paragrafi) for f in frasi(p)]
    m = len(pezzi)
    if m == 0:
        return [""] * k
    testi_it = testi_it or [""] * k
    G_it = [gettoni(t) for t in testi_it]
    tot_it = sum(lung_it) or 1
    ini, s = [], 0
    for L in lung_it:
        ini.append((s / tot_it, (s + L) / tot_it)); s += L
    tot_en = sum(len(p) for p, _ in pezzi) or 1
    mid, s = [], 0
    for p, _ in pezzi:
        mid.append((s + len(p) / 2) / tot_en); s += len(p)
    def punti(j, i):
        g = gettoni(pezzi[j][0])
        bonus = sum(1.0 for x in g if x in G_it[i]) - sum(0.6 for x in g if x not in G_it[i] and any(x in G for G in G_it))
        a, b = ini[i]
        dist = 0 if a <= mid[j] <= b else min(abs(mid[j] - a), abs(mid[j] - b))
        return bonus - 6.0 * dist
    NEG = -1e18
    dp = [[NEG] * k for _ in range(m)]
    da = [[0] * k for _ in range(m)]
    dp[0][0] = punti(0, 0)
    for j in range(1, m):
        for i in range(k):
            best, arg = dp[j - 1][i], i                       # stesso blocco
            if i > 0 and dp[j - 1][i - 1] > best:             # blocco successivo
                best, arg = dp[j - 1][i - 1], i - 1
            if m < k:                                          # poche frasi: si possono saltare blocchi
                for ii in range(i - 1):
                    if dp[j - 1][ii] - 2.0 * (i - ii - 1) > best:
                        best, arg = dp[j - 1][ii] - 2.0 * (i - ii - 1), ii
            if best > NEG:
                dp[j][i], da[j][i] = best + punti(j, i), arg
    fine = k - 1 if dp[m - 1][k - 1] > NEG else max(range(k), key=lambda i: dp[m - 1][i])
    ass, i = [0] * m, fine
    for j in range(m - 1, -1, -1):
        ass[j] = i; i = da[j][i]
    res = []
    for b in range(k):   # frasi dello stesso paragrafo unite da spazio, paragrafi diversi da riga vuota
        testo, prec = "", None
        for (p, n), a in zip(pezzi, ass):
            if a == b:
                testo += ((" " if n == prec else "\n\n") if testo else "") + p; prec = n
        res.append(testo)
    return res

# ---------------------------------------------------------------- composizione
TITOLI = {
 "Dedica e Avviso ai Lettori": ("Dedication and Notice to the Reader", None),
 "Allo Illustrissimo Signore": ("To the Most Illustrious Lord", "Count of Noailles"),
 "Lo Stampatore a i Lettori": ("The Publisher to the Reader", None),
 "Giornata Prima": ("First Day", None), "Giornata Seconda": ("Second Day", None),
 "Giornata Terza": ("Third Day", "Change of Position [De Motu Locali]"),
 "DEL MOTO EQUABILE": ("UNIFORM MOTION", None), "DEL MOTO NATURALMENTE ACCELERATO": ("NATURALLY ACCELERATED MOTION", None),
 "Giornata Quarta": ("Fourth Day", "The Motion of Projectiles"), "DEL MOTO DEI PROIETTI": ("THE MOTION OF PROJECTILES", None),
 "Appendice": ("Appendix", "Theorems and demonstrations concerning the centres of gravity of solids"),
}
ancore = sorted(abb.items())
out = [dict(b) for b in IT]
for b in out:
    if b["tipo"] == "titolo":
        b["testo_lingua"], st = TITOLI[b["testo"]]
        if "sottotitolo" in b or st:
            b["sottotitolo"] = st or ""
INIZIO_APPENDICE = next(i for i, b in enumerate(IT) if b["tipo"] == "titolo" and b["testo"] == "Appendice")
TESTUALI = ("par", "battuta", "enunciato", "rimando")
SEGUACI = ("par", "battuta", "enunciato")   # i rimandi non ricevono testo: hanno solo il titolo
diagnosi = []
for n, (i, j) in enumerate(ancore):
    i2, j2 = ancore[n + 1] if n + 1 < len(ancore) else (INIZIO_APPENDICE, None)
    if i >= INIZIO_APPENDICE:
        break
    j2 = j2 if j2 is not None else next(jj for jj in range(j, len(seq_en)) if seq_en[jj][0] == ("T", "Appendice"))
    k, testi, intest = seq_en[j]
    # testo inglese del segmento, dopo l'àncora
    seg = list(testi)
    for jj in range(j + 1, j2):
        kk, tt, hh = seq_en[jj]
        if hh and kk is None:
            seg.append("<b>%s</b>" % hh)    # titolo inglese senza corrispondente italiano
        elif hh and kk:
            seg.append("<b>%s</b>" % hh)    # (non abbinato: resta come sottotitolo nel testo)
        seg.extend(tt)
    a = IT[i]
    if a["tipo"] == "enunciato" and intest:
        out[i]["intestazione_lingua"] = CORREZIONI_TITOLI.get(intest, intest)
    if a["tipo"] == "rimando" and intest:
        seg = seg  # il rimando prende il titolo inglese
        out[i]["testo"] = CORREZIONI_TITOLI.get(intest, intest)
    seguaci = [x for x in range(i + 1, i2) if IT[x]["tipo"] in SEGUACI]
    if a["tipo"] in ("battuta", "enunciato"):
        blocchi = [i] + seguaci
    else:   # titolo o rimando: il testo va ai blocchi seguenti
        blocchi = seguaci
    if not blocchi:
        if seg:
            if a["tipo"] == "titolo":
                out[i]["paragrafi_dopo"] = seg
            else:
                out[i]["testo"] = (out[i]["testo"] + "\n\n" if out[i]["testo"] else "") + "\n\n".join(seg)
        continue
    lung = [1 if "\\toprule" in IT[x]["testo"] else len(re.sub(r"<[^>]+>", "", IT[x]["testo"])) for x in blocchi]
    ris = distribuisci(lung, seg, [IT[x]["testo"] for x in blocchi])   # in ordine: l'àncora riceve sempre il primo pezzo
    for x, t in zip(blocchi, ris):
        out[x]["testo"] = t
        diagnosi.append((IT[x]["id"] if "id" in IT[x] else "-", len(re.sub(r"<[^>]+>", "", IT[x]["testo"])), len(re.sub(r"<[^>]+>", "", t))))

# ---------------------------------------------------------------- casi particolari
def blocco(pid):
    return next(b for b in out if b.get("id") == pid)
for b in out:   # rimandi non abbinati: solo il titolo inglese
    if b["tipo"] == "rimando" and b["testo"] == IT[out.index(b)]["testo"]:
        m = re.search(r"([IVXL]+)$", b["testo"])
        b["testo"] = ("Proposition " + m.group(1)) if m else "Corollary"
t = blocco("p277")["testo"]   # «Proposition II» c'è già come rimando
blocco("p277")["testo"] = "\n\n".join(x for x in t.split("\n\n") if x != "<b>Proposition II</b>")
MANUALI = {"p007": "<i>Interlocutors: Salviati, Sagredo and Simplicio</i>", "p256": "End of the First Day",
           "p467": "End of the Third Day", "p550": "End of the Fourth Day"}
for pid, t in MANUALI.items():
    blocco(pid)["testo"] = t
# Tavole e Problema XIII della Giornata Quarta (p522–p532): l'ed. UTET pone tavole e Problema XIII
# in un ordine diverso da Crew (che mette il Problema prima delle battute di Sagredo e Salviati).
sp_salv = next(x for x in EN if x[0] == "SP" and x[2][0].startswith("This result can, I think, be obtained as follows"))
k = EN.index(sp_salv)
assert EN[k + 1] == ["H", "Problem. Proposition XIII"]
blocco("p522")["testo"] = sp_salv[2][0]
blocco("p523")["testo"] = "Amplitudes of semi-parabolas described with the same initial speed."
blocco("p525")["testo"] = sp_salv[2][1]
blocco("p526")["testo"] = "Altitudes of semi-parabolas described with the same initial speed."
for pid in ("p524", "p527", "p532"):   # tavole: il build mette l'avviso
    blocco(pid)["testo"] = IT[out.index(blocco(pid))]["testo"]
blocco("PR-P13")["intestazione_lingua"] = "Problem. Proposition XIII"
blocco("PR-P13")["testo"] = "\n\n".join(EN[x][1] for x in (k + 2, k + 3, k + 4))
blocco("p530")["testo"] = EN[k + 5][1]
blocco("p531")["testo"] = "Table giving the altitudes and sublimities of semi-parabolas of constant amplitude, namely 10000 parts, computed for each degree of elevation."
blocco("p528")["testo"] = "\n\n".join(EN[k + 6][2])
blocco("p529")["testo"] = "\n\n".join(EN[k + 7][2])

# note dell'edizione Manuzio: riguardano il testo italiano
for b in out:
    if b["tipo"] == "par" and (re.match(r"^\(\d\) ", IT[out.index(b)]["testo"]) or IT[out.index(b)]["testo"] == "<b>Note:</b>"):
        b["omesso"] = True
# appendice: non c'è in Crew–de Salvio; resta l'italiano con un avviso
AVVISO = "<i>[The Appendix is not included in the English translation by Crew and de Salvio (1914): the Italian text is given here.]</i>"
primo_app = True
for x in range(INIZIO_APPENDICE + 1, len(out)):
    if out[x]["tipo"] in TESTUALI:
        out[x]["lingua_testo"] = "it"
        if primo_app:
            out[x]["prima"] = AVVISO; primo_app = False

for b in out:   # le note dell'ed. Manuzio riguardano il testo italiano
    if b.get("lingua_testo") != "it" and "note" in b:
        b["note"] = []
vuoti = [b.get("id") for b in out if b["tipo"] in TESTUALI and not b.get("omesso") and b.get("lingua_testo") != "it" and not b["testo"].strip()]
json.dump(out, open(os.path.join(QUI, "blocchi_en.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(diagnosi, open("/tmp/diagnosi_discorsi.json", "w"))
print("blocchi senza inglese:", vuoti)
