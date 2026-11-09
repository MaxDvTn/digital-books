#!/usr/bin/env python3
"""Importatore LaTeX -> JSON per i libri di Galileo (modello comune a Sidereus,
Saggiatore, Dialogo, Discorsi).

Uso:
  python3 importa_latex.py LIBRO.tex --da RIGA --a RIGA --out blocchi.json
         [--sigle "DEL MOTO EQUABILE=ME,DEL MOTO NATURALMENTE ACCELERATO=MA"]

Produce una lista di blocchi in ordine di lettura:
  {"tipo": "titolo"|"par"|"figura"|"battuta"|"enunciato"|"rimando",
   "id": "...", "testo": "...", "file": "images/figuraNN.png", "riga": N,
   "voce": "Salv."}

Regole:
- ogni paragrafo (separato da riga vuota) e' un blocco "par" con id p001...;
- ogni \\includegraphics e' un blocco "figura" con id = nome del file;
- \\speaker{X} (Dialogo, Discorsi) produce un blocco "battuta" con la voce;
- (v2, Discorsi) un paragrafo che comincia con \\textbf{TEOREMA n. PROPOSIZIONE m},
  \\textbf{COROLLARIO n}, DEFINIZIONE, ASSIOMA n, AVVERTENZA, SCOLIO, LEMMA,
  PROBLEMA n. PROPOSIZIONE m produce un blocco "enunciato" con genere, numeri e
  un id stabile (es. MA-P2, MA-P2-C1) costruito con la sigla della sezione;
  se l'intestazione e' sola, il testo e' il paragrafo che segue;
- (v2) \\begin{enunciato}...\\end{enunciato} dentro il dialogo produce un blocco
  "enunciato" con genere "citato";
- (v2) \\propbox{X} produce un blocco "rimando" (marginale «[Prop I]» della
  Giornata Seconda); \\theoremheader{X} un titolo di livello "teorema";
- (v2) \\textcolor{rubric}{X} diventa <span class="rubrica">X</span>;
  le glosse del curatore tra quadre diventano <span class="glossa">[...]</span>;
  \\addcontentsline e \\markboth sono rimossi; \\\\ nei titoli separa il
  sottotitolo, nel testo diventa <br>;
- i comandi di stile sono convertiti in HTML minimo (<i>, <b>, <sup>, small-caps);
- le note \\footnote{...} sono estratte nel campo "note" del blocco;
- ogni comando sconosciuto viene segnalato su stderr, non cancellato in silenzio.
  Le tabelle (tabular) non sono ancora gestite e vengono segnalate.
"""
import argparse, json, re, sys

NOTI = {"vspace", "begin", "end", "textwidth", "textheight", "includegraphics",
        "textsc", "textsuperscript", "textit", "emph", "textbf", "footnote",
        "par", "itshape", "chapter", "section", "bigskip", "medskip", "smallskip",
        "speaker", "noindent", "centering", "small", "large", "Large", "normalsize",
        "footnotesize", "scshape", "addcontentsline", "markboth", "textcolor",
        "propbox", "theoremheader", "textquotesingle", "mainmatter", "frontmatter",
        "backmatter", "appendix", "tableofcontents", "vfill", "item", "frac"}

GENERI = {"TEOREMA": "teorema", "PROBLEMA": "problema", "COROLLARIO": "corollario",
          "DEFINIZIONE": "definizione", "AVVERTENZA": "avvertenza", "ASSIOMA": "assioma",
          "SCOLIO": "scolio", "LEMMA": "lemma", "POSTULATO": "postulato"}
GENERI["ALTRA DIMOSTRAZIONE DELLO STESSO"] = "altra_dimostrazione"
RE_INT1 = re.compile(r"^(" + "|".join(GENERI) + r")(?:\s+(\d+))?(?:\.\s*PROPOSIZIONE\s+(\d+))?$")
RE_INT2 = re.compile(r"^PROPOSIZIONE\s+(\d+)(?:\.\s*(PROBLEMA|TEOREMA))?$")


def intestazione(testo):
    """Se testo comincia con \\textbf{INTESTAZIONE}, restituisce
    (genere, n_genere, n_prop, integrata, resto); altrimenti None."""
    t = testo.strip()
    if not t.startswith("\\textbf{"):
        return None
    c, j = leggi_graffa(t, len("\\textbf"))
    h = re.sub(r"\\\\", "", c).strip()
    integrata = h.startswith("[") and h.endswith("]")
    h = h.strip("[]").strip()
    m = RE_INT1.match(h)
    if m:
        g, ng, npr = m.group(1), m.group(2), m.group(3)
    else:
        m = RE_INT2.match(h)
        if not m:
            return None
        g, ng, npr = (m.group(2) or "TEOREMA"), None, m.group(1)
    resto = re.sub(r"^\s*(\\\\)?\s*", "", t[j:])
    return GENERI[g], ng, npr, integrata, resto


def leggi_graffa(s, i):
    """s[i] == '{' ; restituisce (contenuto, indice dopo la graffa chiusa)."""
    assert s[i] == "{"
    d, j = 0, i
    while j < len(s):
        if s[j] == "{":
            d += 1
        elif s[j] == "}":
            d -= 1
            if d == 0:
                return s[i + 1:j], j + 1
        j += 1
    raise ValueError("graffa non chiusa")


def estrai_comando(s, nome, nargs=1):
    """Rimuove \\nome{...}{...} (nargs argomenti) da s: (s_senza, [contenuti])."""
    out, trovati, i = [], [], 0
    tag = "\\" + nome + "{"
    while True:
        k = s.find(tag, i)
        if k < 0:
            out.append(s[i:])
            break
        out.append(s[i:k])
        j = k + len(tag) - 1
        args = []
        for _ in range(nargs):
            while j < len(s) and s[j] == " ":
                j += 1
            c, j = leggi_graffa(s, j)
            args.append(c)
        trovati.append(args[0] if nargs == 1 else args)
        i = j
    return "".join(out), trovati


def stile(s):
    def sost(nome, a, b, nargs=1):
        nonlocal s
        while "\\" + nome + "{" in s:
            k = s.find("\\" + nome + "{")
            j = k + len(nome) + 1
            c, j = leggi_graffa(s, j)
            if nargs == 2:          # \textcolor{colore}{testo}
                c, j = leggi_graffa(s, j)
            s = s[:k] + a + c + b + s[j:]
    s = estrai_comando(s, "addcontentsline", 3)[0]
    s = estrai_comando(s, "markboth", 2)[0]
    sost("textcolor", '<span class="rubrica">', "</span>", nargs=2)
    sost("textit", "<i>", "</i>")
    sost("emph", "<i>", "</i>")
    sost("textbf", "<b>", "</b>")
    sost("textsuperscript", "<sup>", "</sup>")
    sost("textsc", '<span class="sc">', "</span>")
    s = s.replace("\\textquotesingle", "'")
    s = re.sub(r"\\(mainmatter|frontmatter|backmatter|appendix|tableofcontents|vfill)\b", "", s)
    s = re.sub(r"\\item\[([^\]]*)\]\s*", r"<b>\1</b> ", s)
    s = re.sub(r"\\item\b\s*", "", s)
    s = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"\1/\2", s)
    s = s.replace("~", "\u00a0").replace("---", "—").replace("--", "–")
    s = s.replace("``", "“").replace("''", "”")
    s = re.sub(r"\\(par|bigskip|medskip|smallskip|noindent|centering)\b", "", s)
    s = re.sub(r"\\(normalsize|large|Large|small|footnotesize)\b\s*", "", s)
    s = re.sub(r"\{\\itshape\s*(.*?)\}", r"<i>\1</i>", s, flags=re.S)
    s = re.sub(r"\\itshape\s*(.*)$", r"<i>\1</i>", s, flags=re.S)
    s = s.replace("\\\\", "<br>")
    return re.sub(r"\s+", " ", s).strip()


def glosse(s):
    """[...] del curatore -> <span class="glossa">[...]</span>."""
    return re.sub(r"\[([^\[\]]{1,200})\]", r'<span class="glossa">[\1]</span>', s)


def importa(tex, da, a, sigle=None):
    sigle = sigle or {}
    righe = tex.split("\n")[da - 1:a]
    blocchi, buf, riga_buf = [], [], None
    sconosciuti = {}
    np = 0
    st = {"sigla": "E", "ultima_prop": None, "conta": {}, "attende": None}

    def nuovo_id_enunciato(genere, n_gen, n_prop):
        sg = st["sigla"]
        if n_prop:
            st["ultima_prop"] = "%s-P%s" % (sg, n_prop)
            st["conta"] = {}
            return st["ultima_prop"]
        base = st["ultima_prop"] or sg
        sig = {"corollario": "C", "scolio": "S", "lemma": "L", "avvertenza": "AVV",
               "definizione": "DEF", "assioma": "A", "postulato": "POST",
               "altra_dimostrazione": "AD", "teorema": "T", "problema": "PB"}[genere]
        if genere in ("definizione", "assioma", "avvertenza", "postulato"):
            base = sg
        if n_gen:
            return "%s-%s%s" % (base, sig, n_gen)
        k = st["conta"].get(sig, 0) + 1
        st["conta"][sig] = k
        return "%s-%s" % (base, sig) if k == 1 else "%s-%s%d" % (base, sig, k)

    def titolo(testo, livello, r):
        parti = re.split(r"\\\\", testo, maxsplit=1)
        b = {"tipo": "titolo", "livello": livello, "testo": stile(parti[0]), "riga": r}
        if len(parti) > 1:
            b["sottotitolo"] = re.sub(r"</?i>", "", stile(parti[1]))
        blocchi.append(b)
        t = re.sub(r"<[^>]+>", "", b["testo"]).strip().upper()
        if t in sigle or livello == "section":
            st["sigla"] = sigle.get(t, st["sigla"])
            st["ultima_prop"] = None

    def chiudi():
        nonlocal buf, riga_buf, np
        testo = " ".join(buf).strip()
        buf, r = [], riga_buf
        riga_buf = None
        if not testo:
            return
        for c in re.findall(r"\\([a-zA-Z]+)", testo):
            if c not in NOTI:
                sconosciuti[c] = sconosciuti.get(c, 0) + 1
        testo, note = estrai_comando(testo, "footnote")
        note = [glosse(stile(n)) for n in note]
        testo = estrai_comando(testo, "addcontentsline", 3)[0]
        testo = estrai_comando(testo, "markboth", 2)[0].strip()
        # rimandi marginali e intestazioni
        testo, pb = estrai_comando(testo, "propbox")
        for x in pb:
            blocchi.append({"tipo": "rimando", "testo": stile(x), "riga": r})
        testo, th = estrai_comando(testo, "theoremheader")
        for x in th:
            blocchi.append({"tipo": "titolo", "livello": "teorema", "testo": stile(x), "riga": r})
        if not testo.strip():
            return
        m = re.match(r"\\speaker\{([^}]*)\}\s*(.*)", testo, re.S)
        if m:
            np += 1
            blocchi.append({"tipo": "battuta", "id": "p%03d" % np, "voce": m.group(1),
                            "testo": stile(m.group(2)), "note": note, "riga": r})
            return
        m = re.match(r"\\(chapter|section)\*?\{(.*)\}", testo, re.S)
        if m:
            titolo(m.group(2), m.group(1), r)
            return
        m = re.match(r"\\begin\{enunciato\}(.*)\\end\{enunciato\}", testo.strip(), re.S)
        if m:
            np += 1
            blocchi.append({"tipo": "enunciato", "genere": "citato", "id": "p%03d" % np,
                            "testo": stile(m.group(1)), "note": note, "riga": r})
            return
        m = intestazione(testo)
        if m:
            genere, ng, npr, integrata, resto = m
            nome = {"altra_dimostrazione": "Altra dimostrazione dello stesso"}.get(genere, genere.capitalize())
            b = {"tipo": "enunciato", "genere": genere,
                 "id": nuovo_id_enunciato(genere, ng, npr),
                 "intestazione": nome + (" " + ng if ng else "")
                                 + (". Proposizione " + npr if npr else ""),
                 "numero": int(ng) if ng else None,
                 "proposizione": int(npr) if npr else None,
                 "testo": glosse(stile(resto)), "note": note, "riga": r}
            if integrata:
                b["intestazione_integrata"] = True   # [LEMMA]: aggiunta del curatore
            blocchi.append(b)
            if not b["testo"]:
                st["attende"] = b
            return
        if testo.startswith("\\begin{center}") and "includegraphics" not in testo:
            testo = testo.replace("\\begin{center}", "").replace("\\end{center}", "")
        if "\\begin{tabular}" in testo:
            sconosciuti["tabular (tabella non convertita)"] = sconosciuti.get("tabular (tabella non convertita)", 0) + 1
        testo = re.sub(r"\\(begin|end)\{[a-z]+\}", "", testo)
        testo = re.sub(r"\\vspace\{[^}]*\}", "", testo)
        if not testo.strip() or not stile(testo):
            return
        if st["attende"] is not None and not st["attende"]["testo"]:
            # intestazione sola: il testo dell'enunciato e' questo paragrafo
            st["attende"]["testo"] = glosse(stile(testo))
            st["attende"]["riga_testo"] = r
            st["attende"]["note"] += note
            st["attende"] = None
            return
        st["attende"] = None
        np += 1
        blocchi.append({"tipo": "par", "id": "p%03d" % np, "testo": glosse(stile(testo)),
                        "note": note, "riga": r})

    for n, ln in enumerate(righe, start=da):
        if "\\includegraphics" in ln:
            chiudi()
            f = re.search(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", ln).group(1)
            blocchi.append({"tipo": "figura", "id": f.split("/")[-1].rsplit(".", 1)[0],
                            "file": f, "riga": n})
            resto = re.sub(r".*\\end\{center\}", "", ln).strip()
            if resto:
                buf, riga_buf = [resto], n
            continue
        if ln.strip().startswith("%"):
            continue
        m = re.match(r"\\(chapter|section)\*?\{(.*)\}\s*$", ln.strip())
        if m:
            chiudi()
            titolo(m.group(2), m.group(1), n)
            continue
        if not ln.strip():
            chiudi()
            continue
        if riga_buf is None:
            riga_buf = n
        buf.append(ln)
    chiudi()
    for c, k in sorted(sconosciuti.items()):
        print("ATTENZIONE: comando non gestito \\%s (%d volte)" % (c, k), file=sys.stderr)
    return blocchi


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("tex")
    ap.add_argument("--da", type=int, default=1)
    ap.add_argument("--a", type=int, default=10 ** 9)
    ap.add_argument("--out", required=True)
    ap.add_argument("--sigle", default="", help='"TITOLO SEZIONE=SIGLA,..."')
    x = ap.parse_args()
    sigle = dict(p.split("=", 1) for p in x.sigle.split(",") if "=" in p)
    sigle = {k.strip().upper(): v.strip() for k, v in sigle.items()}
    b = importa(open(x.tex, encoding="utf-8").read(), x.da, x.a, sigle)
    json.dump(b, open(x.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    from collections import Counter
    print(Counter(k["tipo"] for k in b), "->", x.out)
