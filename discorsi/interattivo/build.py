#!/usr/bin/env python3
"""Genera index.html dei Discorsi interattivi.

  python3 build.py              # usa blocchi.json già importato
  python3 build.py --importa    # prima rigenera blocchi.json da ../discorsi.tex con strumenti/importa_latex.py

Ingressi: blocchi.json, trattato.json, template.html, libro.js, libro.css,
equabile_modello.js, scheda_equabile.html, scheda_equabile.js, dimostrazioni/*.json,
fac/*.png e le figure in ../images/.
"""
import base64, json, os, re, subprocess, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "strumenti"))
import copertina, lingue, navigazione
from collections import Counter

QUI = os.path.dirname(os.path.abspath(__file__))
LIBRO = os.path.normpath(os.path.join(QUI, ".."))
P = lambda *a: os.path.join(QUI, *a)
leggi = lambda *a: open(P(*a), encoding="utf-8").read()

SIGLE = "DEL MOTO EQUABILE=ME,DEL MOTO NATURALMENTE ACCELERATO=MA,DEL MOTO DEI PROIETTI=PR,APPENDICE=AP"
DA, A = 119, 2204   # dalla Dedica alla fine (la Nota filologica del .tex è riscritta nelle note della pagina)

if "--importa" in sys.argv:
    subprocess.run([sys.executable, os.path.join(LIBRO, "..", "strumenti", "importa_latex.py"),
                    os.path.join(LIBRO, "discorsi.tex"), "--da", str(DA), "--a", str(A),
                    "--sigle", SIGLE, "--out", P("blocchi.json")], check=True)

DISPONIBILI = ["it"] + [l for l in lingue.LINGUE if l != "it" and os.path.exists(P("blocchi_%s.json" % l))]
LINGUA = next((a for a in sys.argv[1:] if a in lingue.LINGUE), None)
if LINGUA is None:   # senza lingua: tutte quelle disponibili
    for l in DISPONIBILI:
        subprocess.run([sys.executable, os.path.abspath(__file__), l] + [a for a in sys.argv[1:] if a.startswith("--") and a != "--importa"], check=True)
    sys.exit(0)
T = json.load(open(P("i18n", "testi_build.json"), encoding="utf-8"))[LINGUA]   # testi generati qui, per lingua
nt = lingue.nt
blocchi = json.load(open(P("blocchi.json"), encoding="utf-8"))
tratt = json.load(open(P("trattato.json"), encoding="utf-8"))["intervalli"]
nel_trattato = lambda r: any(a <= r <= b for a, b in tratt)

# ---------------------------------------------------------------- controlli sulla fonte
cnt = Counter(b["tipo"] for b in blocchi)
voci = Counter(b["voce"] for b in blocchi if b["tipo"] == "battuta")
attesi = {"Salv.": 180, "Sagr.": 117, "Simp.": 92}
if LINGUA != "it":   # i controlli valgono sull'italiano; poi si usano i blocchi della lingua
    pass
if dict(voci) != attesi:
    sys.exit("battute: %s, attese %s" % (dict(voci), attesi))
if cnt["figura"] != 96:
    sys.exit("figure nel testo: %d, attese 96 (97 con il frontespizio)" % cnt["figura"])
ids = [b["id"] for b in blocchi if "id" in b]
doppi = [i for i, c in Counter(ids).items() if c > 1]
if doppi:
    sys.exit("id doppi: %s" % doppi)

if LINGUA != "it":
    blocchi = json.load(open(P("blocchi_%s.json" % LINGUA), encoding="utf-8"))

LINGUA_ATT = [None]   # lingua del blocco corrente, se diversa da quella della pagina
def paragrafi(classe, ident, testo, coda="", prefisso=""):
    """un blocco; nelle altre lingue il testo può avere più paragrafi separati da una riga vuota"""
    parti = [x for x in testo.split("\n\n") if x.strip()] or [""]
    lang = ' lang="%s"' % LINGUA_ATT[0] if LINGUA_ATT[0] else ""
    h = '<p class="%s" id="%s"%s>%s%s%s</p>' % (classe, ident, lang, prefisso, nt(parti[0]), coda)
    for x in parti[1:]:
        seguito = "t trattato" if classe.startswith("enunciato") and "citato" not in classe else (classe.replace("battuta", "").strip() or "t")
        h += '\n<p class="%s cont">%s</p>' % (seguito, nt(x))
    return h

# ---------------------------------------------------------------- figure
def uri(percorso):
    ext = percorso.rsplit(".", 1)[1].lower()
    return "data:image/%s;base64,%s" % ("jpeg" if ext in ("jpg", "jpeg") else "png",
                                         base64.b64encode(open(percorso, "rb").read()).decode())

def dimensioni_png(percorso):
    with open(percorso, "rb") as f:
        t = f.read(24)
    return int.from_bytes(t[16:20], "big"), int.from_bytes(t[20:24], "big")

# ---------------------------------------------------------------- titoli
ID_CAP = {"Dedica e Avviso ai Lettori": "dedica", "Giornata Prima": "g1", "Giornata Seconda": "g2",
          "Giornata Terza": "g3", "Giornata Quarta": "g4", "Appendice": "appendice"}
def id_sezione(t):
    return re.sub(r"[^a-z]+", "-", t.lower().replace("del ", "").replace("dei ", "")).strip("-")
def titolo_sezione(t):   # «DEL MOTO EQUABILE» -> «Del moto equabile» (il maiuscoletto lo fa il CSS)
    return t[:1].upper() + t[1:].lower() if t.isupper() else t

def pulisci_latex_residuo(t):
    t = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"\1/\2", t)
    return t

# ---------------------------------------------------------------- testo
SCHEDE_DOPO = {"ME-P1": "equabile"}
schede_html = {"equabile": leggi("scheda_equabile.html").replace("%%FAC_EQ%%", uri(P("fac", "fac1638_p152.png")))}

out, residui, in_tratt_prec = [], [], False
for b in blocchi:
    if b.get("omesso"):
        continue
    LINGUA_ATT[0] = b.get("lingua_testo") if LINGUA != "it" else None
    if b.get("prima"):
        out.append('<p class="avviso ui">%s</p>' % nt(b["prima"]))
    t = b.get("testo", "")
    if b["tipo"] == "titolo":
        in_tratt_prec = False
        if b["livello"] == "chapter":
            i = ID_CAP.get(b["testo"], id_sezione(b["testo"]))
            sotto = '<span class="sotto">%s</span>' % nt(b["sottotitolo"]) if b.get("sottotitolo") else ""
            out.append('<h2 id="%s">%s%s</h2>' % (i, nt(b.get("testo_lingua", b["testo"])), sotto))
        else:
            out.append('<h3 class="sez" id="%s">%s</h3>' % (id_sezione(b["testo"]), nt(titolo_sezione(b.get("testo_lingua", b["testo"])))))
        for x in b.get("paragrafi_dopo", []):
            out.append('<p class="t">%s</p>' % nt(x))
        continue
    if b["tipo"] == "figura":
        f = os.path.join(LIBRO, b["file"])
        w, h = dimensioni_png(f)
        n = re.sub(r"\D", "", b["id"]) or b["id"]
        out.append('<figure class="fac" data-fig="%s"><img width="%d" height="%d" alt="%s" src="%s"><figcaption>%s</figcaption></figure>'
                   % (b["id"], w, h, lingue.nt_attr(T["alt_fig"] % n), uri(f), nt(T["fig"] % n)))
        continue
    note = "".join(' <span class="nota">(%s)</span>' % x for x in b.get("note", []))
    t = pulisci_latex_residuo(t)
    if "\\" in t:
        if "toprule" in t or "tabular" in t or "&" in t and "midrule" in t:
            t = '<span class="ui nota">%s</span>' % T["tavola"]
        else:
            residui.append((b.get("riga"), t[:80]))
    if b["tipo"] == "battuta":
        out.append(paragrafi("t battuta", b["id"], t, note, '<span class="voce">%s</span> ' % b["voce"]))
        in_tratt_prec = False
        continue
    if b["tipo"] == "rimando":
        out.append('<p class="rimando">[%s]</p>' % nt(t))
        continue
    trattato = b["tipo"] == "enunciato" and b["genere"] != "citato" or b["tipo"] == "par" and nel_trattato(b["riga"])
    if trattato and not in_tratt_prec and b["riga"] < 2058:
        out.append('<p class="etichetta-trattato">%s</p>' % nt(T["etichetta_trattato"]))
    in_tratt_prec = trattato
    if b["tipo"] == "enunciato":
        if b["genere"] == "citato":
            out.append(paragrafi("enunciato citato", b["id"], t, note))
        else:
            out.append(paragrafi("enunciato " + b["genere"], b["id"], t, note, '<span class="int">%s</span>' % nt(b.get("intestazione_lingua", b["intestazione"]))))
            if b["id"] in SCHEDE_DOPO:
                out.append(schede_html.pop(SCHEDE_DOPO[b["id"]]))
                in_tratt_prec = False
        continue
    if re.match(r"^\(\d\) ", t) or t == "<b>Note:</b>":
        out.append('<p class="notafine">%s</p>' % nt(t))
        continue
    cls = "t trattato" if trattato else ("t breve" if len(t) < 140 else "t")
    out.append(paragrafi(cls, b["id"], t, note))

if schede_html:
    sys.exit("schede non inserite: %s" % list(schede_html))
if residui:
    print("ATTENZIONE: comandi LaTeX rimasti nel testo:", len(residui))
    for r in residui[:12]:
        print("  riga", r[0], r[1])



NOTE_IT = """
<p><b>Testo.</b> Galileo Galilei, <i>Discorsi e dimostrazioni matematiche intorno a due nuove scienze</i> (Leida, 1638), nell'edizione elettronica del Progetto Manuzio di Liber Liber (1998; a cura di Catia Righi, revisione di Giovanni Mazzarello), che indica come opera di riferimento <i>Opere di Galileo Galilei</i>, a cura di Franz Brunetti, UTET, Classici della Scienza, 1980 (ISBN 88-02-03457-5). Licenza: <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.it">CC BY-NC-SA 4.0</a>, come indicato dalla pagina di <a href="https://www.liberliber.it/online/autori/autori-g/galileo-galilei/discorsi-e-dimostrazioni-matematiche-intorno-a-due-nuove-scienze/">Liber Liber</a> (controllata l'8 novembre 2026). Il testo è stato ricomposto in LaTeX dal curatore e importato in questa pagina con uno script che non modifica le parole.</p>
<p><b>Le parti latine.</b> Nel 1638 il trattato <i>De motu locali</i>, letto da Salviati nelle Giornate Terza e Quarta, è stampato in latino. Il testo qui riprodotto ne dà una traduzione italiana moderna ridotta agli enunciati (definizioni, assiomi, teoremi, problemi, corollari), con brevi integrazioni tra parentesi quadre, qui in grigio; le dimostrazioni sono omesse, come segnala anche una nota dell'edizione Manuzio («avendo l'edizione U.T.E.T. omesso una dimostrazione»). Né Liber Liber né la fonte LaTeX indicano l'autore della traduzione: è verosimilmente quella del volume UTET, da verificare sulla stampa.</p>
<p><b>Le dimostrazioni nelle schede.</b> Il latino è trascritto dai curatori dalla stampa del 1638 (esemplare digitalizzato da Google Books, file «Galilei - Discorsi e dimostrazioni matematiche intorno a due nuove scienze - 1638.djvu» su Wikimedia Commons, pubblico dominio). La traduzione italiana delle dimostrazioni è dei curatori di questa edizione e segue la stessa licenza del volume. Il facsimile nella scheda del moto equabile è ritagliato dalla stessa stampa (p. 152).</p>
<p><b>Le figure del testo.</b> Le 96 figure provengono dalla fonte LaTeX; se siano riproduzioni delle incisioni del 1638 o ridisegni è ancora da verificare.</p>
<p><b>Una correzione alla nota storica della fonte.</b> La traduzione latina pubblicata a Strasburgo nel 1635 da Matthias Bernegger (<i>Systema cosmicum</i>) è quella del <i>Dialogo sopra i due massimi sistemi</i>, non dei <i>Discorsi</i>.</p>
<p><b>Licenza di questa pagina.</b> Testi e schede: CC BY-NC-SA 4.0 (per la licenza del testo). Codice: MIT.</p>
"""
NOTE = nt(T["note"]) if LINGUA != "it" else NOTE_IT
STRUMENTI = os.path.join(LIBRO, "..", "strumenti")
COP = json.load(open(P("copertina.json"), encoding="utf-8"))
CONF = dict({"autore": "Galileo Galilei", "frontespizioDa": "#copertina .cop-fac img"}, **T["conf"])

pagina = (leggi("template.html")
          .replace("%%TESTO%%", "\n".join(out))
          .replace("%%NOTE%%", NOTE)
          .replace("%%COPERTINA%%", copertina.html(COP, QUI))
          .replace("%%COPERTINA_CSS%%", copertina.CSS)
          .replace("%%LIBRO_CSS%%", open(os.path.join(STRUMENTI, "libro", "libro.css"), encoding="utf-8").read())
          .replace("%%LIBRO_JS%%", open(os.path.join(STRUMENTI, "libro", "libro.js"), encoding="utf-8").read())
          .replace("%%LIBRO_CONF%%", json.dumps(CONF, ensure_ascii=False))
          .replace("%%DIM_ME_P1%%", json.dumps(json.load(open(P("dimostrazioni", "ME-P1.json"), encoding="utf-8")), ensure_ascii=False))
          .replace("%%MODELLO_EQ%%", leggi("equabile_modello.js"))
          .replace("%%SCHEDA_EQ_JS%%", leggi("scheda_equabile.js")))
if "%%" in pagina:
    sys.exit("segnaposto non sostituiti: %s" % sorted(set(re.findall(r"%%[A-Z_]+%%", pagina))))
# ---------------------------------------------------------------- navigazione (indice dai titoli del testo)
pagina = navigazione.applica(pagina, casa="../../index.html")
# ---------------------------------------------------------------- lingua
pagina = (pagina.replace('<html lang="it">', '<html lang="%s">' % LINGUA)
          .replace("</div></header>", lingue.menu_html(LINGUA, DISPONIBILI) + "</div></header>", 1)
          .replace("</head>", "<style>%s</style>\n</head>" % lingue.MENU_CSS, 1)
          .replace("</body>", "<script>%s</script>\n</body>" % lingue.MENU_JS, 1))
SALTA = ("window.LIBRO_LATINO", "/*lingue*/")
DIZ, SORGENTE = P("i18n", "%s.json" % LINGUA), P("i18n", ".sorgente_it.html")
if LINGUA == "it":
    open(SORGENTE, "w", encoding="utf-8").write(pagina)
else:
    if "--scheletro" in sys.argv or not os.path.exists(DIZ):
        print("testi da tradurre:", lingue.scheletro(open(SORGENTE, encoding="utf-8").read(), DIZ, SALTA))
    pagina, mancanti = lingue.traduci(pagina, lingue.carica(DIZ), SALTA)
    if mancanti:
        print("ATTENZIONE: %d testi senza traduzione (restano in italiano):" % len(mancanti))
        for tipo, x in mancanti[:15]:
            print("  ", tipo, repr(x[:90]))
pagina = lingue.togli_marcatori(pagina)
copertina.controlla_ancore(COP, pagina)
open(P(lingue.nome_file(LINGUA)), "w", encoding="utf-8").write(pagina)
print("blocchi:", dict(cnt), "| battute:", dict(voci))
print(lingue.nome_file(LINGUA), len(pagina) // 1024, "KB")
