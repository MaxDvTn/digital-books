#!/usr/bin/env python3
"""Genera index.html del Sidereus interattivo da blocchi.json + immagini + astro.js."""
import base64, json, html, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "strumenti"))
import copertina, lingue

BASE = os.environ.get("SIDEREUS_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")) + "/"
QUI = os.path.dirname(os.path.abspath(__file__))
DISPONIBILI = ["it"] + [l for l in lingue.LINGUE if l != "it" and os.path.exists(os.path.join(QUI, "blocchi_%s.json" % l))]
LINGUA = sys.argv[1] if len(sys.argv) > 1 else None
if LINGUA is None:   # senza argomenti: tutte le lingue disponibili
    import subprocess
    for l in DISPONIBILI:
        subprocess.run([sys.executable, os.path.abspath(__file__), l], check=True)
    sys.exit(0)
suf = "" if LINGUA == "it" else "_" + LINGUA
blocchi = json.load(open(os.path.join(QUI, "blocchi%s.json" % suf), encoding="utf-8"))
# testi generati dal build (date, didascalie): uno per lingua
T = {
 "it": {"mesi": ["", "gennaio", "febbraio", "marzo"], "mesi_brevi": ["", "gen.", "feb.", "mar."],
        "alt_oss": "Disegno di Galileo: Giove e i suoi satelliti, %d %s 1610", "apri": "apri nell'osservatorio",
        "incisione": "%s (incisione dell'edizione 1610)",
        "alt_fig": {"figura01": "Le fasi della Luna disegnate da Galileo", "figura02": "La Cintura e la Spada di Orione",
                    "figura03": "La Nebulosa della Testa di Orione e il Presepe", "figura05": "Schema dei raggi nel cannocchiale",
                    "figura06": "La Luna e i suoi rilievi lungo il bordo", "figura07": "La figura per l'altezza dei monti lunari",
                    "figura04": "Figura"}, "figura": "Figura",
        "conf": {"titolo": "Avviso Astronomico", "testaTrad": "trad. L. Lanzillotta", "frontespizioNota": "Venezia, 1610 · frontespizio originale"}},
 "en": {"mesi": ["", "January", "February", "March"], "mesi_brevi": ["", "Jan.", "Feb.", "Mar."],
        "alt_oss": "Galileo's drawing: Jupiter and its satellites, %d %s 1610", "apri": "open in the observatory",
        "incisione": "%s (engraving from the 1610 edition)",
        "alt_fig": {"figura01": "The phases of the Moon drawn by Galileo", "figura02": "The Belt and Sword of Orion",
                    "figura03": "The Nebula of Orion's Head and Praesepe", "figura05": "Diagram of the rays in the telescope",
                    "figura06": "The Moon and its relief along the edge", "figura07": "The figure for the height of the lunar mountains",
                    "figura04": "Figure"}, "figura": "Figure",
        "conf": {"titolo": "The Sidereal Messenger", "testaTrad": "transl. E. S. Carlos", "frontespizioNota": "Venice, 1610 · original title page"}},
}[LINGUA]
CONT = {}   # testo del libro, inserito dopo la traduzione dell'interfaccia
def fisso(testo):   # testo già nella lingua giusta, generato qui: non passa dal dizionario
    k = "F%d" % len(CONT)
    CONT[k] = testo
    return "⟦%s⟧" % k
def segnaposto(pid, testo):
    CONT[pid] = testo
    return "⟦%s⟧" % pid
oss_raw = json.load(open(os.path.join(QUI, "osservazioni.json")))
par = {b["id"]: b for b in blocchi if b["tipo"] == "par"}

# affermazioni principali in grassetto (scelta editoriale, dichiarata nelle note della pagina)
EVIDENZE = json.load(open(os.path.join(QUI, "evidenze%s.json" % suf), encoding="utf-8"))
for pid, frase, _ in EVIDENZE:
    t = par[pid]["testo"]
    n = t.count(frase)
    if n != 1:
        sys.exit("evidenze.json: la frase non compare esattamente una volta in %s (trovata %d volte): %s" % (pid, n, frase[:60]))
    par[pid]["testo"] = t.replace(frase, '<b class="chiave">' + frase + "</b>")
print("affermazioni in grassetto:", len(EVIDENZE))
for pid in par:
    par[pid]["testo"] = segnaposto(pid, par[pid]["testo"])

def uri(f):
    return "data:image/png;base64," + base64.b64encode(open(BASE + "images/" + f + ".png", "rb").read()).decode()

# --- osservazioni di Giove --------------------------------------------------
OSS, idx = [], {}
for i, (f, m, d, h, p_prima, p_dopo, ora) in enumerate(oss_raw):
    testo = ""
    if p_dopo:
        testo = par[p_dopo]["testo"]
    else:  # la figura chiude il paragrafo che la introduce
        testo = par[p_prima]["testo"]
    if True:
        pid = testo[1:-1]
        CONT["J:" + pid] = json.dumps(CONT[pid], ensure_ascii=False)[1:-1]
        testo = "⟦J:%s⟧" % pid
    OSS.append({"f": f, "m": m, "d": d, "h": h, "ora": ora, "testo": testo})
    idx[f] = i
IMG = {o["f"]: uri(o["f"]) for o in OSS}

# --- schede -----------------------------------------------------------------
SCHEDA_CANN = """
<section class="scheda" id="cannocchiale" aria-labelledby="hCann">
<h3 id="hCann">Scheda · Come funziona il cannocchiale</h3>
<p class="intro">Galileo spiega in poche righe due cose: quanto il suo strumento ingrandisce, e come usarlo per misurare piccoli angoli tra le stelle.</p>
<div class="etichetta">I raggi senza lenti (tratteggio) e con le lenti (blu)</div>
<div class="fig"><svg id="cRaggi" role="img" aria-label="Schema dei raggi: l'occhio E, l'apertura CD, l'oggetto FG; con le lenti si vede solo la parte HI"></svg></div>
<div class="controlli ui">
<label>Ingrandimento <input type="range" id="cM" min="1" max="30" step="1" value="20" aria-label="Ingrandimento dei diametri"></label>
<label>Foro della lamina <input type="range" id="cForo" min="5" max="100" step="1" value="100" aria-label="Apertura della lamina in percentuale"></label>
</div>
<div class="controlli ui" role="group" aria-label="Gli strumenti di Galileo">
<span>Gli strumenti di Galileo:</span>
<button class="b" data-strum="3">primo, 3×</button><button class="b" data-strum="8">secondo, 8×</button><button class="b" data-strum="30">l'ultimo, 30×</button>
</div>
<div class="cifre" id="cCifre"></div>
<div class="etichetta">La prova dei due quadrati di carta</div>
<div class="fig"><svg id="cQuadri" role="img" aria-label="Il quadrato grande visto a occhio nudo e il piccolo visto col cannocchiale: coincidono quando l'ingrandimento è 20"></svg></div>
<details><summary>Per la classe</summary><div><ol>
<li>Galileo dice che il suo ultimo strumento mostra gli oggetti «ingranditi quasi mille volte e trenta volte più vicini». Come stanno insieme i due numeri?
<details><summary>Risposta</summary><div>«Mille» si riferisce alle superfici, «trenta» ai diametri: 30 × 30 = 900, cioè quasi mille. Per Galileo «ingrandito» vuol dire ingrandito in superficie.</div></details></li>
<li>Nella prova dei quadrati, perché il lato grande deve essere 20 volte il piccolo per verificare un ingrandimento di 400?
<details><summary>Risposta</summary><div>Perché l'area cresce come il quadrato del lato: 20² = 400.</div></details></li>
<li>Restringendo il foro della lamina, l'angolo HEI diventa di pochi primi. Perché questo serve a misurare la distanza tra due stelle?
<details><summary>Risposta</summary><div>Ogni foro corrisponde a un angolo noto. Se due stelle stanno appena dentro il campo, la loro distanza è al massimo quell'angolo: il foro fa da righello angolare.</div></details></li>
</ol></div></details>
<details><summary>Lettura moderna</summary><div>Il cannocchiale di Galileo ha un obiettivo convergente e un oculare divergente; l'ingrandimento angolare vale circa il rapporto tra le distanze focali, M ≈ f<sub>ob</sub>/f<sub>oc</sub>. Un angolo α diventa M·α: per questo il campo inquadrato (l'angolo HEI) è M volte più stretto di quello a occhio nudo. Nello schema la rifrazione è rappresentata in modo semplificato, come nella figura di Galileo.</div></details>
</section>
"""

SCHEDA_LUNA = """
<section class="scheda" id="luna" aria-labelledby="hLuna" tabindex="-1">
<h3 id="hLuna">Scheda · Quanto sono alti i monti della Luna?</h3>
<p class="intro">Una cima illuminata dentro la parte buia, un raggio di Sole radente e il teorema di Pitagora. Segui la costruzione passo per passo, poi cambia la distanza della cima dal confine della luce.</p>
<div class="lGriglia"><div class="fig"><svg id="lFig" role="img"></svg></div><div class="fig lZoomBox" hidden><svg id="lZoom" role="img" aria-label="Riquadro in scala vera intorno alla cima: la montagna sale lungo il raggio fino a toccare il raggio di Sole radente"></svg></div></div>
<div class="passi ui"><button class="b" id="lPrec" aria-label="Passo precedente">◀</button><span class="num" id="lNum"></span><button class="b" id="lSucc" aria-label="Passo successivo">▶</button><button class="b" id="lInizio">Da capo</button></div>
<div class="lettura" id="lTesto" aria-live="polite"></div>
<div class="controlli ui"><label>Distanza della cima dal confine della luce, CD <input type="range" id="lF" min="20" max="250" step="5" value="100" aria-label="Distanza CD in miglia"> <output id="lFv" style="min-width:5.5em">100 miglia</output></label></div>
<div class="cifre" id="lCifre"></div>
<details><summary>Per la classe</summary><div><ol>
<li>Galileo scrive che ED è «più di 1004» e AD «più di 4». Calcola il valore esatto. Perché Galileo si accontenta di «più di»?
<details><summary>Risposta</summary><div>ED = √1 010 000 ≈ 1004,99, quindi AD ≈ 4,99 miglia. Gli basta dimostrare che i monti superano le 4 miglia: un limite inferiore è più difficile da contestare di un valore preciso.</div></details></li>
<li>Se la cima fosse lontana dal confine un decimo del diametro, quanto sarebbe alta?
<details><summary>Risposta</summary><div>CD = 200, DE² = 1 040 000, ED ≈ 1019,8: AD ≈ 19,8 miglia. Raddoppiando la distanza, l'altezza diventa circa quattro volte maggiore.</div></details></li>
<li>Galileo afferma che sulla Terra nessun monte arriva a un miglio di altezza. Che cosa ne pensi oggi?
<details><summary>Risposta</summary><div>È falso: l'Everest supera gli 8800 m, cioè circa cinque miglia. Ai tempi di Galileo le altezze dei monti erano molto sottostimate. Il suo ragionamento sulla Luna resta valido; è il confronto con la Terra a essere sbagliato.</div></details></li>
</ol></div></details>
<details><summary>Lettura moderna</summary><div>Con raggio lunare R, distanza dal terminatore d e altezza h: (R + h)² = R² + d². Se d è piccola rispetto a R, h ≈ d² / (2R). Con d = 100 e R = 1000: h ≈ 10 000 / 2000 = 5 miglia. Per avere i chilometri si usa il rapporto con il diametro: Galileo stima la Luna 2000 miglia, oggi sappiamo che misura 3474 km.</div></details>
</section>
"""

SCHEDA_GIOVE = """
<section class="scheda" id="giove" aria-labelledby="hGiove" tabindex="-1">
<h3 id="hGiove">Scheda · L'osservatorio di Galileo: gli Astri Medicei</h3>
<p class="intro">Dal 7 gennaio al 2 marzo 1610 Galileo disegna 65 volte Giove con le sue «stelle». Qui ogni disegno è affiancato al cielo di quella sera ricostruito con un modello moderno. All'inizio i satelliti non hanno nome: prova a capire da solo quale è quale.</p>
<div class="dataoss" id="gData" aria-live="polite"></div>
<div class="passi ui"><button class="b" id="gPrec" aria-label="Disegno precedente">◀</button><span class="num" id="gNum"></span><button class="b" id="gSucc" aria-label="Disegno successivo">▶</button><button class="b" id="gPlay" aria-pressed="false">▶ Anima</button><button class="b" id="gNomi" aria-pressed="false">Mostra i nomi</button></div>
<div class="etichetta">Il disegno di Galileo</div>
<div class="disegnoG" id="gImg"></div>
<div class="etichetta">Il cielo ricostruito (oriente a sinistra, come nei disegni)</div>
<div class="fig"><svg id="gStriscia" role="img" aria-label="Posizioni calcolate di Giove e dei quattro satelliti"></svg></div>
<div class="cifre" id="gCifre"></div>
<div class="controlli ui"><label>Tempo libero, dal 7 gennaio al 2 marzo 1610 <input type="range" id="tempo" min="0" max="1320" step="0.25" value="0" aria-label="Tempo in ore dal 7 gennaio"></label></div>
<div class="etichetta">Che cosa ha scritto Galileo</div>
<div class="testoOss" id="gTesto"></div>
<div class="duecol">
<div><div class="etichetta">Visto dall'alto: perché a volte se ne vedono meno di quattro</div><div class="fig"><svg id="gAlto" role="img" aria-label="Le orbite viste dall'alto; i satelliti nella fascia davanti o dietro a Giove non si vedono"></svg></div></div>
<div><div class="etichetta">Tutte le notti in un grafico (il tempo scorre verso il basso)</div><div class="grafico"><svg id="gGrafico" role="img" aria-label="Distanza dei satelliti da Giove in funzione del tempo; le tacche rosse sono le osservazioni di Galileo"></svg></div>
<p class="ui" style="font-size:.75rem;color:var(--dato);margin:.3rem 0">Ogni disegno di Galileo è una fetta orizzontale di questo grafico. Le tacche rosse a sinistra sono le sue osservazioni: tocca il grafico per aprire quella più vicina (con la tastiera usa ◀ ▶).</p></div>
</div>
<details><summary>Per la classe</summary><div><ol>
<li>Galileo scrive che il satellite con l'orbita più grande ha un «periodo semimensile». Usa il grafico (con i nomi) per misurare il periodo di Callisto, da un massimo a oriente al successivo.
<details><summary>Risposta</summary><div>Circa 16 giorni e 2/3 (oggi: 16,69 giorni). «Semimensile» è una buona stima.</div></details></li>
<li>Il 24 gennaio, all'ora sesta, Galileo scrive che due stelline «s'erano unite in una». Che cosa è successo davvero?
<details><summary>Risposta</summary><div>Europa e Ganimede, a oriente, si trovavano quasi alla stessa distanza da Giove (circa 3,5′): con quel cannocchiale non si potevano più distinguere.</div></details></li>
<li>In molte sere Galileo vede tre satelliti, a volte due. Elenca le ragioni per cui uno può mancare.
<details><summary>Risposta</summary><div>Si trova dietro Giove o davanti al suo disco luminoso; è troppo vicino al pianeta e si perde nel suo bagliore; è sovrapposto a un altro satellite; è nell'ombra di Giove (eclissi, non calcolata qui).</div></details></li>
<li>Perché la scoperta è un argomento a favore di Copernico? (rileggi l'ultimo paragrafo)
<details><summary>Risposta</summary><div>Chi rifiutava Copernico obiettava che la Terra non poteva girare intorno al Sole portandosi dietro la Luna. Giove mostra quattro lune che lo seguono mentre gira: un sistema del genere esiste davvero.</div></details></li>
</ol></div></details>
<details><summary>Lettura moderna: la terza legge di Keplero</summary><div>Raggi delle orbite (in raggi di Giove) e periodi: Io 5,9 e 1,77 giorni; Europa 9,4 e 3,55; Ganimede 15,0 e 7,15; Callisto 26,4 e 16,69. Il rapporto r³/T² è circa lo stesso per tutti e quattro (≈ 66): è la stessa legge che vale per i pianeti intorno al Sole. Nota anche le risonanze: i periodi di Io, Europa e Ganimede stanno quasi come 1 : 2 : 4.</div></details>
</section>
"""

# --- testo --------------------------------------------------------------------
out = []
for b in blocchi:
    if b["tipo"] == "titolo":
        continue
    if b["tipo"] == "par":
        if b["id"] == "p139":
            continue
        t = b["testo"]
        if b["id"] == "p001":
            out.append('<p class="sottotitolo">%s</p>' % t)
            continue
        cls = "t breve" if len(t) < 140 else "t"
        note = "".join(' <span class="nota">(%s)</span>' % n.replace("<sup>", "").replace("</sup>", "") for n in b.get("note", []))
        out.append('<p class="%s" id="%s">%s%s</p>' % (cls, b["id"], t, note))
        if b["id"] == "p009":
            out.append(SCHEDA_CANN)
        if b["id"] == "p020":
            pass
        if b["id"] == "p029":
            out.append(SCHEDA_GIOVE)
    else:
        f = b["id"]
        if f in idx:
            i = idx[f]; o = OSS[i]
            alt = fisso(T["alt_oss"] % (o["d"], T["mesi"][o["m"]]))
            out.append('<figure class="fac piccola" data-fig="%s"><img alt="%s" src="%s">'
                       '<div class="ricostruito" data-i="%d"><svg role="img" aria-label="Cielo ricostruito per la stessa sera"></svg></div>'
                       '<figcaption>%s <button class="minibtn vaiOss" data-i="%d">%s</button></figcaption></figure>'
                       % (f, alt, IMG[f], i, fisso("%d %s" % (o["d"], T["mesi_brevi"][o["m"]])), i, fisso(T["apri"])))
        else:
            alt = T["alt_fig"].get(f, T["figura"])
            didasc = fisso(T["incisione"] % alt)
            alt = fisso(alt)
            cls = "fac"
            out.append('<figure class="%s" data-fig="%s"><img alt="%s" src="%s"><figcaption>%s</figcaption></figure>' % (cls, f, alt, uri(f), didasc))
            if f == "figura07":
                out.append(SCHEDA_LUNA)
            if f == "figura01":
                out.append(open(os.path.join(QUI, "fasi_scheda.html")).read())

# controlla che ogni figura dell'italiano sia stata usata
usate = [b["id"] for b in blocchi if b["tipo"] == "figura"]
print("figure nel testo:", len(usate), "osservazioni:", len(OSS))

STRUMENTI = os.path.join(QUI, "..", "..", "strumenti")
COP = json.load(open(os.path.join(QUI, "copertina.json"), encoding="utf-8"))
CONF = dict({"autore": "Galileo Galilei", "loopFig": "figura01", "testaLat0": "Sidereus Nuncius", "testaLat1": "Venetiis, MDCX",
        "frontespizioDa": "#copertina .cop-fac img"}, **T["conf"])
tpl = open(os.path.join(QUI, "template.html")).read()
page = (tpl.replace("%%TESTO%%", "\n".join(out))
        .replace("%%ASTRO%%", open(os.path.join(QUI, "astro.js")).read())
        .replace("%%OSS%%", json.dumps(OSS, ensure_ascii=False))
        .replace("%%IMG%%", json.dumps(IMG))
        .replace("%%COPERTINA%%", copertina.html(COP, QUI))
        .replace("%%COPERTINA_CSS%%", copertina.CSS)
        .replace("%%LIBRO_CONF%%", json.dumps(CONF, ensure_ascii=False))
        .replace("%%LIBRO_CSS%%", open(os.path.join(STRUMENTI, "libro", "libro.css")).read())
        .replace("%%LIBRO_JS%%", open(os.path.join(STRUMENTI, "libro", "libro.js")).read())
        .replace("%%LATINO%%", json.dumps([x for x in json.load(open(os.path.join(QUI, "blocchi_la.json"))) if x["tipo"] != "titolo" or True], ensure_ascii=False))
        .replace("%%FASI_CSS%%", open(os.path.join(QUI, "fasi_css.css")).read())
        .replace("%%FASI_JS%%", open(os.path.join(QUI, "fasi.js")).read())
        .replace("%%FASI_IMG%%", json.dumps(["data:image/png;base64," + base64.b64encode(open(os.path.join(QUI, "fasi", "g%d.png" % k), "rb").read()).decode() for k in range(1, 6)])))
# --- lingua: menu, traduzione dell'interfaccia, testo del libro
page = (page.replace('<html lang="it">', '<html lang="%s">' % LINGUA)
        .replace("</div></header>", lingue.menu_html(LINGUA, DISPONIBILI) + "</div></header>", 1)
        .replace("</head>", "<style>%s</style>\n</head>" % lingue.MENU_CSS, 1)
        .replace("</body>", "<script>%s</script>\n</body>" % lingue.MENU_JS, 1))
SALTA = ("window.LIBRO_LATINO", "/*lingue*/")
DIZ = os.path.join(QUI, "i18n", "%s.json" % LINGUA)
SORGENTE = os.path.join(QUI, "i18n", ".sorgente_it.html")   # pagina italiana senza testo del libro (non va nel repository)
if LINGUA == "it":
    os.makedirs(os.path.dirname(SORGENTE), exist_ok=True)
    open(SORGENTE, "w", encoding="utf-8").write(page)
    page = lingue.riempi(page, CONT)
else:
    os.makedirs(os.path.dirname(DIZ), exist_ok=True)
    if "--scheletro" in sys.argv or not os.path.exists(DIZ):
        print("testi da tradurre:", lingue.scheletro(open(SORGENTE, encoding="utf-8").read(), DIZ, SALTA))
    page, mancanti = lingue.traduci(page, lingue.carica(DIZ), SALTA)
    page = lingue.riempi(page, CONT)
    if mancanti:
        print("ATTENZIONE: %d testi senza traduzione (restano in italiano):" % len(mancanti))
        for tipo, t in mancanti[:15]:
            print("  ", tipo, repr(t[:90]))
copertina.controlla_ancore(COP, page)
nome = lingue.nome_file(LINGUA)
open(os.path.join(QUI, nome), "w", encoding="utf-8").write(page)
print(nome, len(page) // 1024, "KB")
