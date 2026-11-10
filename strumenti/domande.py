"""Domande per la classe, comuni a tutti i libri interattivi.

Una sola fonte, <libro>/interattivo/domande.json, alimenta:
  - i riquadri «Domande» dentro il libro (riquadri(), runtime() e CSS), anche nel libro sfogliabile;
  - la pagina «Per i docenti» (pagina_docenti()), con filtri, note, errori tipici e scheda di lavoro stampabile.

Tipi di domanda:
  testo   la risposta è un passo del libro: «Mostrami dove» lo apre ed evidenzia le parole (passo.termini);
  scelta  scelta multipla (opzioni, giusta); con «scheda» diventa «Prevedi, poi verifica»;
  numero  risposta numerica (valore, tolleranza, unita);
  scheda  si risponde muovendo una scheda interattiva: SCHEDE[id].leggi() è confrontato con scheda.verifica
          (lista di alternative; ogni chiave è un intervallo [min, max] oppure un valore esatto).
Ogni domanda può avere «passo» (Mostrami dove) e «scheda.apri» (Apri la scheda in quello stato).

Le schede del libro devono esporre window.SCHEDE[id] = {imposta(stato), leggi()}.
Il build controlla: id unici, ancore e schede esistenti, chiavi di verifica note, parole del passo presenti nel testo.
"""
import html, json, re, unicodedata

UI = {
 "it": {"box": "Domande per la classe", "apri_box": "Apri le domande ↗", "domande": "Domande",
        "intro": "Prova a rispondere: sotto ogni domanda ci sono un indizio e la soluzione.",
        "tipi": {"testo": "Trova nel testo", "scheda": "Prova con la scheda", "prevedi": "Prevedi, poi verifica",
                 "scelta": "Scegli la risposta", "numero": "Calcola"},
        "liv": ["", "base", "medio", "impegnativo"], "livello": "livello",
        "controlla": "Controlla", "dove": "Mostrami dove", "scheda": "Apri la scheda ↗", "indizio": "Indizio",
        "risposta": "Soluzione", "tua": "La tua risposta", "scegli_leg": "Scegli una risposta",
        "docenti": "Tutte le domande, con le note per i docenti →",
        "js": {"giusto": "Giusto!", "riprova": "Non ancora: riprova, o guarda l'indizio.", "scegli": "Scegli una risposta.",
               "numero": "Scrivi un numero.", "verifica": "Ora controlla nella scheda.", "torna": "Torna alla domanda",
               "nondisp": "La scheda non è disponibile in questa pagina."}},
 "en": {"box": "Questions for the class", "apri_box": "Open the questions ↗", "domande": "Questions",
        "intro": "Try to answer: under each question there are a hint and the solution.",
        "tipi": {"testo": "Find it in the text", "scheda": "Try it in the panel", "prevedi": "Predict, then check",
                 "scelta": "Choose the answer", "numero": "Work it out"},
        "liv": ["", "basic", "intermediate", "challenging"], "livello": "level",
        "controlla": "Check", "dove": "Show me where", "scheda": "Open the panel ↗", "indizio": "Hint",
        "risposta": "Solution", "tua": "Your answer", "scegli_leg": "Choose an answer",
        "docenti": "All the questions, with notes for teachers →",
        "js": {"giusto": "Right!", "riprova": "Not yet: try again, or look at the hint.", "scegli": "Choose an answer.",
               "numero": "Write a number.", "verifica": "Now check it in the panel.", "torna": "Back to the question",
               "nondisp": "The panel is not available on this page."}},
}
# chiavi che ogni scheda restituisce con leggi() (per controllare le verifiche al build)
CHIAVI = {
 "fasi": {"giorno", "vista", "cinerea"},
 "cannocchiale": {"m", "foro"},
 "luna": {"cd", "passo", "ad"},
 "giove": {"disegno", "libero", "ore", "nomi", "visibili", "stessoLato"},
}
TIPI = ("testo", "scelta", "numero", "scheda")


def norm(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()


def carica(percorso):
    return json.load(open(percorso, encoding="utf-8"))


def gruppi(dati):
    """Domande raggruppate per ancora («dopo»), nell'ordine del file; numerazione progressiva."""
    out, idx = [], {}
    for n, d in enumerate(dati["domande"], 1):
        d["_n"] = n
        if d["dopo"] not in idx:
            idx[d["dopo"]] = len(out); out.append((d["dopo"], []))
        out[idx[d["dopo"]]][1].append(d)
    return out


def tipo_label(d, L):
    t = d["tipo"]
    if t == "scelta" and d.get("scheda"):
        t = "prevedi"
    return UI[L]["tipi"][t]


def controlla(dati, testi, ancore, schede, lingue_):
    """testi: {lingua: {id_paragrafo: html}}; ancore: id a cui si può agganciare un riquadro;
    schede: id delle schede presenti. Restituisce la lista degli errori (vuota se tutto va bene)."""
    err, visti = [], set()
    for d in dati["domande"]:
        i = d.get("id", "?")
        if i in visti: err.append("%s: id ripetuto" % i)
        visti.add(i)
        if d.get("tipo") not in TIPI: err.append("%s: tipo sconosciuto %r" % (i, d.get("tipo")))
        if d.get("tema") not in dati["temi"]: err.append("%s: tema sconosciuto" % i)
        if d.get("dopo") not in ancore: err.append("%s: ancora «dopo» inesistente: %s" % (i, d.get("dopo")))
        for L in lingue_:
            for campo in ("testo", "risposta"):
                if not d.get(campo, {}).get(L): err.append("%s: manca %s in %s" % (i, campo, L))
        if d["tipo"] == "scelta":
            ops = d.get("opzioni") or []
            if len(ops) < 2 or not (0 <= d.get("giusta", -1) < len(ops)): err.append("%s: opzioni o «giusta» non valide" % i)
        if d["tipo"] == "numero" and not isinstance(d.get("valore"), (int, float)): err.append("%s: manca il valore" % i)
        if d["tipo"] == "testo" and not d.get("passo"): err.append("%s: una domanda «testo» richiede il passo" % i)
        if d["tipo"] == "scheda" and not (d.get("scheda") or {}).get("verifica"): err.append("%s: una domanda «scheda» richiede la verifica" % i)
        s = d.get("scheda")
        if s:
            if s["id"] not in schede: err.append("%s: scheda inesistente %s" % (i, s["id"]))
            note = CHIAVI.get(s["id"])
            for alt in s.get("verifica", []) + [s.get("apri") or {}]:
                for k in alt:
                    if note is not None and k not in note: err.append("%s: chiave %r sconosciuta per la scheda %s" % (i, k, s["id"]))
        p = d.get("passo")
        if p:
            for L in lingue_:
                t = testi.get(L, {}).get(p["id"])
                if t is None:
                    err.append("%s: passo %s inesistente (%s)" % (i, p["id"], L)); continue
                pezzi = [norm(html.unescape(x)) for x in re.split(r"<[^>]+>", t)]   # come l'evidenziatore: dentro un solo nodo di testo
                for w in p["termini"].get(L, []):
                    if not any(norm(w) in x for x in pezzi):
                        err.append("%s: «%s» non compare nel passo %s (%s)" % (i, w, p["id"], L))
    return err


def _e(s):
    return html.escape(s, quote=True)


def domanda_html(d, L, href_docenti):
    U = UI[L]
    a = {"class": "dq", "id": d["id"], "data-tipo": d["tipo"]}
    if d["tipo"] == "scelta": a["data-giusta"] = str(d["giusta"])
    if d["tipo"] == "numero": a.update({"data-valore": repr(d["valore"]), "data-tol": repr(d.get("tolleranza", 0))})
    s = d.get("scheda")
    if s:
        a["data-scheda"] = s["id"]
        if s.get("apri"): a["data-apri"] = json.dumps(s["apri"])
        if s.get("verifica"): a["data-verifica"] = json.dumps(s["verifica"])
        if s.get("ok"): a["data-ok"] = s["ok"][L]
        if s.get("no"): a["data-no"] = s["no"][L]
    if d.get("passo"):
        a["data-passo"] = d["passo"]["id"]
        a["data-termini"] = json.dumps([norm(w) for w in d["passo"]["termini"][L]], ensure_ascii=False)
    attr = " ".join('%s="%s"' % (k, _e(v)) for k, v in a.items())
    liv = d.get("livello", 1)
    h = ['<li %s value="%d">' % (attr, d["_n"])]
    h.append('<div class="dq-testa ui"><span class="dq-tipo">%s</span><span class="dq-liv" title="%s: %s" aria-label="%s: %s">%s</span></div>'
             % (tipo_label(d, L), U["livello"], U["liv"][liv], U["livello"], U["liv"][liv], "●" * liv + "○" * (3 - liv)))
    h.append('<p class="dq-testo">%s</p>' % _e(d["testo"][L]))
    if d["tipo"] == "scelta":
        h.append('<fieldset class="dq-opzioni"><legend class="vh">%s</legend>' % U["scegli_leg"])
        for k, o in enumerate(d["opzioni"]):
            h.append('<label><input type="radio" name="r-%s" value="%d"><span>%s</span></label>' % (d["id"], k, _e(o[L])))
        h.append("</fieldset>")
    if d["tipo"] == "numero":
        h.append('<label class="dq-num ui">%s <input type="text" inputmode="decimal" autocomplete="off" aria-label="%s"> <span>%s</span></label>'
                 % (U["tua"], U["tua"], _e(d.get("unita", {}).get(L, ""))))
    b = []
    if d["tipo"] != "testo": b.append('<button class="b" data-azione="controlla">%s</button>' % U["controlla"])
    if s: b.append('<button class="b" data-azione="scheda">%s</button>' % U["scheda"])
    if d.get("passo"): b.append('<button class="b" data-azione="dove">%s</button>' % U["dove"])
    h.append('<div class="dq-azioni ui">%s</div>' % "".join(b))
    h.append('<p class="dq-esito ui" aria-live="polite"></p>')
    if d.get("indizio"):
        h.append('<details class="dq-ind"><summary>%s</summary><div>%s</div></details>' % (U["indizio"], _e(d["indizio"][L])))
    h.append('<details class="dq-sol"><summary>%s</summary><div>%s</div></details>' % (U["risposta"], _e(d["risposta"][L])))
    h.append("</li>")
    return "".join(h)


def riquadri(dati, L, href_docenti):
    """{ancora: html della sezione con le domande}."""
    U, out = UI[L], {}
    for dopo, ds in gruppi(dati):
        tema = dati["temi"][ds[0]["tema"]][L]
        sid = "domande-" + re.sub(r"[^\w-]", "", dopo)
        h = ['<section class="scheda domande" id="%s" aria-labelledby="h-%s" data-titolo="%s" data-etichetta="%s" data-apri="%s">'
             % (sid, sid, _e(tema), _e(U["box"]), _e(U["apri_box"]))]
        h.append('<h3 id="h-%s">%s · %s</h3>' % (sid, U["domande"], _e(tema)))
        h.append('<p class="intro">%s</p>' % U["intro"])
        h.append('<ol class="dq-lista">%s</ol>' % "".join(domanda_html(d, L, href_docenti) for d in ds))
        h.append('<p class="dq-docenti ui"><a href="%s#%s">%s</a></p>' % (href_docenti, ds[0]["id"], U["docenti"]))
        h.append("</section>")
        out[dopo] = "\n".join(h)
    return out


CSS = """
section.scheda.domande{background:#f8f3e7;border:1px solid #e3d9c6;border-left:4px solid var(--rubrica)}
.dq-lista{padding-left:1.5rem;margin:.5rem 0 .2rem}
.dq{margin:.2rem 0 1.3rem;padding-left:.15rem;border-radius:6px}
.dq::marker{font:600 .95rem Inter,system-ui,sans-serif;color:var(--rubrica)}
.dq-testa{display:flex;gap:.5rem;align-items:center;flex-wrap:wrap;font-size:.68rem;text-transform:uppercase;letter-spacing:.06em;color:var(--dato)}
.dq-tipo{background:#fff;border:1px solid var(--linea);border-radius:99px;padding:.08rem .55rem}
.dq-liv{letter-spacing:.12em;color:var(--rubrica);font-size:.75rem}
.dq-testo{margin:.3rem 0 .45rem;line-height:1.5}
fieldset.dq-opzioni{border:0;padding:0;margin:.3rem 0;display:grid;gap:.35rem;min-width:0}
.dq-opzioni label{display:flex;gap:.6rem;align-items:flex-start;background:#fff;border:1px solid var(--linea);border-radius:8px;padding:.55rem .7rem;font-size:.95rem;line-height:1.4;cursor:pointer;min-height:44px}
.dq-opzioni input{margin:.2rem 0 0;accent-color:var(--attivo);flex:none;width:18px;height:18px}
.dq-opzioni label:has(input:checked){border-color:var(--attivo);background:#eef4fb}
.dq-num{display:flex;align-items:center;flex-wrap:wrap;gap:.5rem;font-size:.85rem;margin:.35rem 0}
.dq-num input{width:7em;font:1rem Inter,system-ui,sans-serif;min-height:44px;padding:.3rem .55rem;border:1px solid var(--linea);border-radius:8px;background:#fff}
.dq-azioni{display:flex;flex-wrap:wrap;gap:.4rem;margin:.45rem 0 .2rem}
.dq-esito{font-size:.85rem;margin:.25rem 0;min-height:1.3em;line-height:1.4}
.dq-esito.ok{color:var(--s2)}.dq-esito.no{color:var(--rubrica)}
.dq details{margin:.35rem 0}
.dq-docenti{font-size:.8rem;margin:.2rem 0 0;text-align:right}
.vh{position:absolute!important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.dq-torna{position:fixed;left:50%;top:70px;transform:translateX(-50%);z-index:300;background:var(--inchiostro);color:#fff;border:0;border-radius:99px;padding:.6rem 1.15rem;font:.9rem Inter,system-ui,sans-serif;min-height:44px;box-shadow:0 4px 16px rgba(0,0,0,.25);cursor:pointer;max-width:calc(100vw - 24px)}
@keyframes dqLampo{0%{background:#f6dc8a}100%{background:transparent}}
.dq-lampo{animation:dqLampo 1.8s ease}
.lb-tavola.lb-domande{border-style:dashed;background:#f8f3e7}
@media print{.dq-torna,.dq-azioni{display:none}}
"""

JS = r"""/*lingue*/
(function(){
  const T = %T%;
  const libroAperto = () => !!(window.Libro && Libro.aperto && Libro.aperto());
  const scheda = id => (window.SCHEDE || {})[id];
  let chip = null, chipT = null;
  function vai(q){
    q.scrollIntoView({block: "center"});
    q.classList.remove("dq-lampo"); void q.offsetWidth; q.classList.add("dq-lampo");
    const f = q.querySelector("input, button"); if (f) try { f.focus({preventScroll: true}); } catch (e) {}
  }
  function contesto(q){
    const m = location.hash.match(/^#pagina-(\d+)$/);
    return {box: q.closest("section").id, libro: libroAperto(), pagina: m ? +m[1] : null};
  }
  function torna(q, ctx){   // pulsante «Torna alla domanda» dopo un salto
    if (!chip) { chip = document.createElement("button"); chip.className = "dq-torna"; chip.type = "button"; document.body.appendChild(chip); }
    chip.textContent = "↩ " + T.torna; chip.hidden = false;
    clearTimeout(chipT); chipT = setTimeout(() => { chip.hidden = true; }, 180000);
    chip.onclick = () => {
      chip.hidden = true;
      if (ctx.libro && window.Libro) {
        const apri = () => { Libro.chiudiScheda(); Libro.apriScheda(ctx.box, () => setTimeout(() => vai(q), 30)); };
        if (libroAperto()) apri(); else Promise.resolve(Libro.apri(ctx.pagina)).then(apri);
      } else vai(q);
    };
  }
  function segna(q){ try { history.replaceState(history.state, "", "#" + q.id); } catch (e) {} }
  function apriScheda(q){
    const id = q.dataset.scheda, st = q.dataset.apri ? JSON.parse(q.dataset.apri) : null, sez = document.getElementById(id);
    if (!sez) return;
    const ctx = contesto(q), S = scheda(id);
    if (ctx.libro) { Libro.chiudiScheda(); Libro.apriScheda(id, () => { if (S && st) S.imposta(st); }); }
    else { segna(q); if (S && st) S.imposta(st); if (window.NAV) NAV.vaiA(sez); else sez.scrollIntoView(); }
    torna(q, ctx);
  }
  function mostraDove(q){
    const p = document.getElementById(q.dataset.passo); if (!p) return;
    const ctx = contesto(q), termini = JSON.parse(q.dataset.termini || "[]");
    if (ctx.libro) Libro.chiudi();
    segna(q);
    if (window.NAV) NAV.vaiA(p, termini); else p.scrollIntoView({block: "center"});
    torna(q, ctx);
  }
  function esito(q, ok, msg){
    const e = q.querySelector(".dq-esito");
    e.textContent = (ok ? "✓ " : "✗ ") + msg; e.className = "dq-esito ui " + (ok ? "ok" : "no");
  }
  function controlla(q){
    const t = q.dataset.tipo;
    if (t === "scelta") {
      const r = q.querySelector("input[type=radio]:checked");
      if (!r) return esito(q, false, T.scegli);
      const ok = +r.value === +q.dataset.giusta;
      return esito(q, ok, ok ? T.giusto + (q.dataset.scheda ? " " + T.verifica : "") : T.riprova);
    }
    if (t === "numero") {
      const v = parseFloat(q.querySelector(".dq-num input").value.replace(/\s/g, "").replace(",", "."));
      if (isNaN(v)) return esito(q, false, T.numero);
      const ok = Math.abs(v - +q.dataset.valore) <= +q.dataset.tol + 1e-9;
      return esito(q, ok, ok ? T.giusto : T.riprova);
    }
    if (t === "scheda") {
      const S = scheda(q.dataset.scheda);
      if (!S || !S.leggi) return esito(q, false, T.nondisp);
      const st = S.leggi(), alt = JSON.parse(q.dataset.verifica || "[]");
      const ok = alt.some(a => Object.keys(a).every(k => { const v = a[k], x = st[k];
        return Array.isArray(v) ? (x >= v[0] - 1e-9 && x <= v[1] + 1e-9) : x === v; }));
      return esito(q, ok, ok ? (q.dataset.ok || T.giusto) : (q.dataset.no || T.riprova));
    }
  }
  document.addEventListener("click", e => {
    const b = e.target.closest(".dq [data-azione]"); if (!b) return;
    const q = b.closest(".dq"), a = b.dataset.azione;
    if (a === "controlla") controlla(q); else if (a === "scheda") apriScheda(q); else if (a === "dove") mostraDove(q);
  });
  document.addEventListener("keydown", e => {
    if (e.key === "Enter" && e.target.matches(".dq-num input")) { e.preventDefault(); controlla(e.target.closest(".dq")); }
  });
  /* link diretti: #SN-03 apre la domanda; #scheda=luna&cd=200 apre la scheda in quello stato */
  function daHash(){
    let h = location.hash.slice(1); try { h = decodeURIComponent(h); } catch (e) {}
    const m = h.match(/^scheda=([\w-]+)(?:&(.*))?$/);
    if (m) {
      const S = scheda(m[1]), sez = document.getElementById(m[1]), st = {};
      (m[2] || "").split("&").filter(Boolean).forEach(kv => { const [k, v] = kv.split("=");
        st[k] = v === "true" ? true : v === "false" ? false : (v !== "" && !isNaN(+v)) ? +v : v; });
      if (S && Object.keys(st).length) S.imposta(st);
      if (sez) setTimeout(() => sez.scrollIntoView({block: "start"}), 60);
      return;
    }
    const q = document.getElementById(h);
    if (q && q.classList.contains("dq")) setTimeout(() => vai(q), 60);
  }
  window.addEventListener("hashchange", daHash);
  if (document.readyState === "complete") daHash(); else window.addEventListener("load", daHash);
})();
"""


def applica(pagina, L):
    """Stile e script delle domande nella pagina del libro."""
    js = JS.replace("%T%", json.dumps(UI[L]["js"], ensure_ascii=False))
    pagina = pagina.replace("</head>", "<style>%s</style>\n</head>" % CSS, 1)
    return pagina.replace("</body>", "<script>%s</script>\n</body>" % js, 1)


# ------------------------------------------------------------------ pagina per i docenti
UI_DOC = {
 "it": {"titolo": "Per i docenti", "sotto": "Domande per la classe", "home": "⌂ Home", "libro": "Apri il libro",
        "altra": "English", "intro": "Tutte le domande del libro, con le soluzioni, gli errori tipici degli studenti e gli obiettivi. Le stesse domande compaiono nel testo, alla fine delle sezioni. Scegli quelle che ti servono e componi una scheda di lavoro da stampare o da proiettare.",
        "tipi_tit": "Quattro modi di interrogare il libro",
        "tipi_desc": {"testo": "la risposta è un passo del testo; «Mostrami dove» lo apre ed evidenzia le parole.",
                      "scheda": "si risponde muovendo una scheda; il pulsante «Controlla» legge lo stato della scheda.",
                      "prevedi": "si sceglie una risposta prima di aprire la scheda, poi si verifica.",
                      "numero": "si calcola un numero, a mano o leggendolo nella scheda."},
        "tutti": "Tutti", "tema": "Tema", "tipo": "Tipo", "livello": "Livello", "n": "{n} domande", "n1": "1 domanda",
        "selvis": "Seleziona le visibili", "desel": "Deseleziona tutte", "componi": "Componi la scheda di lavoro ({n})",
        "sel": "Nella scheda di lavoro", "attesa": "Risposta attesa", "toll": "tolleranza", "giusta": "risposta giusta",
        "risposta": "Soluzione", "indizio": "Indizio", "doc": "Per il docente", "errori": "Errori tipici", "obiettivi": "Obiettivi",
        "nel_libro": "Apri nel libro", "scheda_cosi": "Apri la scheda in questo stato ↗", "passo": "Il passo nel testo",
        "foglio_tit": "Scheda di lavoro", "risp": "Risposta", "piede": "Testi e schede: CC BY-NC-SA 4.0 · codice: MIT", "nome": "Nome", "classe": "Classe", "data": "Data",
        "con_sol": "Aggiungi le soluzioni in fondo", "stampa": "Stampa", "chiudi": "Chiudi", "vuoto": "Seleziona almeno una domanda.",
        "usa_scheda": "Usa la tavola interattiva «{t}» del libro.", "cerca": "Cerca il passo nel libro.", "sol_tit": "Soluzioni",
        "link_libro": "Il libro interattivo:", "nota": "Le soluzioni sono leggibili anche dagli studenti, sotto ogni domanda del libro: questa pagina aggiunge le note didattiche.",
        "schede": {"fasi": "Le fasi della Luna", "cannocchiale": "Come funziona il cannocchiale", "luna": "Quanto sono alti i monti della Luna?", "giove": "L'osservatorio di Galileo"}},
 "en": {"titolo": "For teachers", "sotto": "Questions for the class", "home": "⌂ Home", "libro": "Open the book",
        "altra": "Italiano", "intro": "All the book's questions, with solutions, typical student mistakes and goals. The same questions appear in the text, at the end of the sections. Pick the ones you need and compose a worksheet to print or project.",
        "tipi_tit": "Four ways to question the book",
        "tipi_desc": {"testo": "the answer is a passage of the text; «Show me where» opens it and highlights the words.",
                      "scheda": "the answer comes from moving a panel; «Check» reads the panel's state.",
                      "prevedi": "students choose an answer before opening the panel, then check.",
                      "numero": "students work out a number, by hand or reading it from the panel."},
        "tutti": "All", "tema": "Topic", "tipo": "Type", "livello": "Level", "n": "{n} questions", "n1": "1 question",
        "selvis": "Select visible", "desel": "Clear selection", "componi": "Compose the worksheet ({n})",
        "sel": "In the worksheet", "attesa": "Expected answer", "toll": "tolerance", "giusta": "correct answer",
        "risposta": "Solution", "indizio": "Hint", "doc": "For the teacher", "errori": "Typical mistakes", "obiettivi": "Goals",
        "nel_libro": "Open in the book", "scheda_cosi": "Open the panel in this state ↗", "passo": "The passage in the text",
        "foglio_tit": "Worksheet", "risp": "Answer", "piede": "Texts and panels: CC BY-NC-SA 4.0 · code: MIT", "nome": "Name", "classe": "Class", "data": "Date",
        "con_sol": "Add the solutions at the end", "stampa": "Print", "chiudi": "Close", "vuoto": "Select at least one question.",
        "usa_scheda": "Use the interactive plate «{t}» in the book.", "cerca": "Find the passage in the book.", "sol_tit": "Solutions",
        "link_libro": "The interactive book:", "nota": "Students can also read the solutions, under each question in the book: this page adds the teaching notes.",
        "schede": {"fasi": "The phases of the Moon", "cannocchiale": "How the telescope works", "luna": "How high are the mountains of the Moon?", "giove": "Galileo's observatory"}},
}

CSS_DOC = """
:root{--carta:#fbf8f2;--carta2:#f3eee4;--inchiostro:#22201c;--rubrica:#871919;--attivo:#1f5fa8;--dato:#6b6458;--linea:#d9d1c3;--ok:#1f7a4d}
*{box-sizing:border-box}
body{margin:0;background:var(--carta);color:var(--inchiostro);font:18px/1.55 "EB Garamond",Georgia,serif}
.ui,button,select,input,label,summary,.barra,.filtri,.c-testa,.c-link,.badge{font-family:Inter,system-ui,-apple-system,"Segoe UI",sans-serif}
a{color:var(--attivo)}
:focus-visible{outline:3px solid #f0b400;outline-offset:2px}
.barra{position:sticky;top:0;z-index:5;background:rgba(251,248,242,.96);border-bottom:1px solid var(--linea);backdrop-filter:blur(4px)}
.barra .dentro{max-width:980px;margin:0 auto;display:flex;align-items:center;gap:.4rem;padding:.4rem .8rem;flex-wrap:wrap}
.barra .marchio{font:600 1rem "EB Garamond",serif;color:var(--rubrica);font-variant:small-caps;letter-spacing:.03em;margin-right:auto}
.barra a{font-size:.85rem;text-decoration:none;color:var(--inchiostro);border:1px solid var(--linea);border-radius:8px;padding:.5rem .75rem;min-height:44px;display:inline-flex;align-items:center;background:#fff}
main{max-width:980px;margin:0 auto;padding:1rem 1rem 4rem}
h1{font-weight:400;font-variant:small-caps;color:var(--rubrica);font-size:2.1rem;margin:1.2rem 0 0;letter-spacing:.04em}
.sotto{font-style:italic;color:var(--dato);margin:0 0 1rem;font-size:1.15rem}
.intro{max-width:46em}
.nota{font:.82rem/1.5 Inter,system-ui,sans-serif;color:var(--dato);max-width:52em}
.tipi{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:.6rem;margin:1rem 0 1.4rem;padding:0;list-style:none}
.tipi li{background:var(--carta2);border-radius:10px;padding:.7rem .85rem;font-size:.95rem;line-height:1.4}
.tipi b{display:block;font:600 .8rem Inter,system-ui,sans-serif;text-transform:uppercase;letter-spacing:.05em;color:var(--rubrica);margin-bottom:.2rem}
.filtri{padding:.5rem 0;border-bottom:1px solid var(--linea);display:flex;flex-wrap:wrap;gap:.5rem .8rem;align-items:center;font-size:.85rem}
.filtri label{display:flex;align-items:center;gap:.35rem}
.filtri select{font-size:.85rem;min-height:44px;border:1px solid var(--linea);border-radius:8px;background:#fff;padding:.2rem .4rem;max-width:58vw}
.filtri .conta{color:var(--dato);margin-right:auto}
button.b{font-size:.85rem;border:1px solid var(--linea);background:#fff;border-radius:8px;padding:.45rem .8rem;cursor:pointer;min-height:44px;color:var(--inchiostro)}
button.b:hover{border-color:var(--attivo)}
button.b.pieno{background:var(--rubrica);border-color:var(--rubrica);color:#fff}
button.b:disabled{opacity:.5;cursor:default}
.tema-tit{font-weight:400;font-variant:small-caps;color:var(--rubrica);font-size:1.4rem;margin:1.8rem 0 .4rem;letter-spacing:.03em}
.carta{background:#fff;border:1px solid var(--linea);border-radius:12px;padding:.9rem 1rem 1rem;margin:.8rem 0;scroll-margin-top:72px}
#bComponi{position:fixed;right:16px;bottom:16px;z-index:6;box-shadow:0 4px 16px rgba(0,0,0,.22);font-size:.9rem;padding:.6rem 1rem}
#bComponi[hidden]{display:none}
.carta.scelta-on{border-color:var(--attivo);box-shadow:0 0 0 2px rgba(31,95,168,.15)}
.c-testa{display:flex;flex-wrap:wrap;gap:.35rem .6rem;align-items:center;font-size:.75rem;color:var(--dato)}
.c-sel{display:inline-flex;align-items:center;gap:.4rem;font-weight:600;color:var(--inchiostro);min-height:44px;cursor:pointer}
.c-sel input{width:20px;height:20px;accent-color:var(--attivo)}
.badge{background:var(--carta2);border-radius:99px;padding:.12rem .6rem;text-transform:uppercase;letter-spacing:.05em;font-size:.68rem}
.liv{color:var(--rubrica);letter-spacing:.1em}
.c-testo{font-size:1.08rem;margin:.35rem 0 .5rem}
.c-opz{margin:.2rem 0 .6rem;padding-left:1.6rem}
.c-opz li{margin:.15rem 0}
.c-opz li.giusta{font-weight:600}
.c-opz li.giusta::after{content:" ✓";color:var(--ok)}
.c-val{font:.88rem Inter,system-ui,sans-serif;margin:.2rem 0 .6rem}
.c-griglia{display:grid;grid-template-columns:1fr;gap:.6rem}
@media(min-width:760px){.c-griglia{grid-template-columns:1fr 1fr}}
.c-blocco{background:var(--carta);border-radius:8px;padding:.55rem .75rem;font-size:.97rem;line-height:1.45}
.c-blocco.doc{background:#f4f0e6}
.c-blocco h4{margin:0 0 .2rem;font:600 .72rem Inter,system-ui,sans-serif;text-transform:uppercase;letter-spacing:.06em;color:var(--dato)}
.c-blocco p{margin:.2rem 0}
.c-blocco ul{margin:.2rem 0;padding-left:1.1rem}
.c-link{display:flex;flex-wrap:wrap;gap:.4rem;margin:.7rem 0 0;font-size:.82rem}
.c-link a{border:1px solid var(--linea);border-radius:8px;padding:.45rem .7rem;text-decoration:none;min-height:44px;display:inline-flex;align-items:center}
.c-link a:hover{border-color:var(--attivo)}
#foglio{background:#fff;border:1px solid var(--linea);border-radius:12px;margin:1.2rem 0;padding:1rem 1.2rem}
#foglio .comandi{display:flex;flex-wrap:wrap;gap:.5rem .8rem;align-items:center;font-size:.85rem;border-bottom:1px solid var(--linea);padding-bottom:.6rem;margin-bottom:.8rem}
#foglio .comandi label{display:flex;align-items:center;gap:.4rem;min-height:44px}
#foglio .comandi input[type=checkbox]{width:20px;height:20px}
#fTitolo{font:600 1.5rem "EB Garamond",serif;color:var(--rubrica);border:0;border-bottom:1px dashed var(--linea);width:100%;background:transparent;font-variant:small-caps;padding:.1rem 0}
.f-dati{display:flex;flex-wrap:wrap;gap:.4rem 1.6rem;font:.85rem Inter,system-ui,sans-serif;margin:.6rem 0 1rem}
.f-dati span{flex:1 1 160px;border-bottom:1px solid #999;padding-bottom:.15rem}
.f-dom{margin:0 0 1.1rem;padding-left:1.5rem}
.f-dom>li{margin:0 0 1.1rem;break-inside:avoid}
.f-dom .f-op{list-style:none;padding:0;margin:.3rem 0}
.f-dom .f-op li::before{content:"☐  "}
.f-riga{border-bottom:1px solid #aaa;height:1.7em}
.f-dove{font:italic .8rem Inter,system-ui,sans-serif;color:var(--dato)}
.f-sol{break-before:page;border-top:2px solid var(--rubrica);padding-top:.6rem;margin-top:1.4rem}
.f-sol h2{font:600 1.1rem "EB Garamond",serif;color:var(--rubrica);font-variant:small-caps;margin:0 0 .4rem}
.f-sol li{margin:.3rem 0;font-size:.95rem}
.f-piede{font:.72rem Inter,system-ui,sans-serif;color:var(--dato);margin-top:1rem}
footer{max-width:980px;margin:0 auto;padding:1rem 1rem 3rem;font:.8rem Inter,system-ui,sans-serif;color:var(--dato)}
@media(max-width:600px){h1{font-size:1.6rem}.barra .marchio{display:none}.carta{padding:.8rem .75rem}}
@media print{
  body{background:#fff;font-size:12pt}
  body.stampa>*:not(main),body.stampa main>*:not(#foglio){display:none!important}
  #foglio{border:0;padding:0;margin:0}
  #foglio .comandi{display:none}
  #fTitolo{border:0}
}
"""

JS_DOC = r"""/*lingue*/
(function(){
  const T = %T%, D = %D%;
  const $ = s => document.querySelector(s), $$ = s => [...document.querySelectorAll(s)];
  const carte = $$(".carta"), fT = $("#fTema"), fP = $("#fTipo"), fL = $("#fLiv");
  function filtra(){
    let n = 0;
    carte.forEach(c => { const ok = (!fT.value || c.dataset.tema === fT.value) && (!fP.value || c.dataset.tipo === fP.value) && (!fL.value || c.dataset.liv === fL.value);
      c.hidden = !ok; if (ok) n++; });
    $$(".tema-tit").forEach(h => { h.hidden = !carte.some(c => !c.hidden && c.dataset.tema === h.dataset.tema); });
    $("#conta").textContent = n === 1 ? T.n1 : T.n.replace("{n}", n);
    conta();
  }
  function scelte(){ return carte.filter(c => c.querySelector(".c-sel input").checked).map(c => c.id); }
  function conta(){
    const s = scelte();
    $("#bComponi").textContent = T.componi.replace("{n}", s.length); $("#bComponi").hidden = !s.length;
    carte.forEach(c => c.classList.toggle("scelta-on", c.querySelector(".c-sel input").checked));
  }
  [fT, fP, fL].forEach(s => s.addEventListener("change", filtra));
  document.addEventListener("change", e => { if (e.target.closest(".c-sel")) conta(); });
  $("#bVis").addEventListener("click", () => { carte.forEach(c => { if (!c.hidden) c.querySelector(".c-sel input").checked = true; }); conta(); });
  $("#bDesel").addEventListener("click", () => { carte.forEach(c => c.querySelector(".c-sel input").checked = false); conta(); });
  const esc = s => String(s).replace(/[&<>"]/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}[c]));
  function componi(){
    const s = scelte(); if (!s.length) return;
    const qs = s.map(id => D[id]);
    let h = "";
    qs.forEach(q => {
      h += "<li><p>" + esc(q.testo) + "</p>";
      if (q.opzioni) h += '<ul class="f-op">' + q.opzioni.map(o => "<li>" + esc(o) + "</li>").join("") + "</ul>";
      else if (q.tipo === "numero") h += "<p>" + esc(T.risp) + ': ____________ ' + esc(q.unita || "") + "</p>";
      else h += '<div class="f-riga"></div><div class="f-riga"></div><div class="f-riga"></div>';
      if (q.dove) h += '<p class="f-dove">' + esc(q.dove) + "</p>";
      h += "</li>";
    });
    $("#fDom").innerHTML = h;
    $("#fSol").innerHTML = '<h2>' + esc(T.sol_tit) + '</h2><ol>' + qs.map(q => "<li>" + esc(q.risposta) + "</li>").join("") + "</ol>";
    $("#fSol").hidden = !$("#fConSol").checked;
    $("#fLink").textContent = new URL(D._libro, location.href).href;
    $("#foglio").hidden = false; $("#foglio").scrollIntoView({behavior: "smooth", block: "start"});
  }
  $("#bComponi").addEventListener("click", componi);
  $("#fConSol").addEventListener("change", e => { $("#fSol").hidden = !e.target.checked; });
  $("#fStampa").addEventListener("click", () => { document.body.classList.add("stampa"); window.print(); });
  window.addEventListener("afterprint", () => document.body.classList.remove("stampa"));
  $("#fChiudi").addEventListener("click", () => { $("#foglio").hidden = true; });
  try { localStorage.setItem("lingua", document.documentElement.lang); } catch (e) {}
  filtra();
  if (location.hash) { const c = document.getElementById(location.hash.slice(1)); if (c) setTimeout(() => c.scrollIntoView({block: "start"}), 50); }
})();
"""


def _link_scheda(libro_href, s):
    q = "&".join("%s=%s" % (k, str(v).lower() if isinstance(v, bool) else v) for k, v in (s.get("apri") or {}).items())
    return "%s#scheda=%s%s" % (libro_href, s["id"], ("&" + q) if q else "")


def pagina_docenti(dati, L, libro_href, home_href, altra_href, testa_extra=""):
    U, Ub = UI_DOC[L], UI[L]
    libro = dati["libro"][L]
    temi = dati["temi"]
    gr = gruppi(dati)
    perjs = {"_libro": libro_href}
    card = []
    tema_corrente = None
    for d in dati["domande"]:
        if d["tema"] != tema_corrente:
            tema_corrente = d["tema"]
            card.append('<h2 class="tema-tit" data-tema="%s">%s</h2>' % (d["tema"], _e(temi[d["tema"]][L])))
        tipo_k = "prevedi" if d["tipo"] == "scelta" and d.get("scheda") else d["tipo"]
        liv = d.get("livello", 1)
        h = ['<article class="carta" id="%s" data-tema="%s" data-tipo="%s" data-liv="%d">' % (d["id"], d["tema"], tipo_k, liv)]
        h.append('<div class="c-testa"><label class="c-sel"><input type="checkbox" aria-label="%s: %s"> %d · %s</label>'
                 '<span class="badge">%s</span><span class="liv" title="%s">%s %s</span><span>%d min</span></div>'
                 % (U["sel"], d["id"], d["_n"], d["id"], tipo_label(d, L), Ub["livello"], "●" * liv + "○" * (3 - liv), Ub["liv"][liv], d.get("minuti", 5)))
        h.append('<p class="c-testo">%s</p>' % _e(d["testo"][L]))
        if d["tipo"] == "scelta":
            h.append('<ol class="c-opz" type="A">%s</ol>' % "".join('<li%s>%s</li>' % (' class="giusta"' if k == d["giusta"] else "", _e(o[L])) for k, o in enumerate(d["opzioni"])))
        if d["tipo"] == "numero":
            tol = d.get("tolleranza", 0)
            val = ("%g" % d["valore"]).replace(".", "," if L == "it" else ".")
            h.append('<p class="c-val">%s: <b>%s %s</b>%s</p>' % (U["attesa"], val, _e(d.get("unita", {}).get(L, "")),
                     (" (%s ± %s)" % (U["toll"], ("%g" % tol).replace(".", "," if L == "it" else "."))) if tol else ""))
        h.append('<div class="c-griglia"><div class="c-blocco"><h4>%s</h4><p>%s</p>%s</div>' % (U["risposta"], _e(d["risposta"][L]),
                 ('<h4 style="margin-top:.5rem">%s</h4><p>%s</p>' % (U["indizio"], _e(d["indizio"][L]))) if d.get("indizio") else ""))
        doc = d.get("docenti", {})
        dh = ['<div class="c-blocco doc"><h4>%s</h4>' % U["doc"]]
        if doc.get("commento"): dh.append("<p>%s</p>" % _e(doc["commento"][L]))
        if doc.get("errori"): dh.append('<h4 style="margin-top:.5rem">%s</h4><ul>%s</ul>' % (U["errori"], "".join("<li>%s</li>" % _e(x[L]) for x in doc["errori"])))
        if doc.get("obiettivi"): dh.append('<p><b>%s:</b> %s</p>' % (U["obiettivi"], _e(doc["obiettivi"][L])))
        dh.append("</div></div>")
        h.append("".join(dh))
        links = ['<a href="%s#%s">%s</a>' % (libro_href, d["id"], U["nel_libro"])]
        if d.get("scheda"): links.append('<a href="%s">%s</a>' % (_e(_link_scheda(libro_href, d["scheda"])), U["scheda_cosi"]))
        if d.get("passo"): links.append('<a href="%s#%s">%s</a>' % (libro_href, d["passo"]["id"], U["passo"]))
        h.append('<p class="c-link">%s</p></article>' % "".join(links))
        card.append("".join(h))
        dove = U["usa_scheda"].replace("{t}", U["schede"].get(d["scheda"]["id"], d["scheda"]["id"])) if d.get("scheda") else (U["cerca"] if d.get("passo") else "")
        perjs[d["id"]] = {"testo": d["testo"][L], "tipo": d["tipo"], "risposta": d["risposta"][L], "dove": dove,
                          "opzioni": [o[L] for o in d["opzioni"]] if d["tipo"] == "scelta" else None,
                          "unita": d.get("unita", {}).get(L, "")}
    opt = lambda pairs: "".join('<option value="%s">%s</option>' % (k, _e(v)) for k, v in pairs)
    temi_usati = []
    for d in dati["domande"]:
        if d["tema"] not in temi_usati: temi_usati.append(d["tema"])
    tipi_usati = []
    for d in dati["domande"]:
        k = "prevedi" if d["tipo"] == "scelta" and d.get("scheda") else d["tipo"]
        if k not in tipi_usati: tipi_usati.append(k)
    filtri = ('<div class="filtri ui">'
              '<label>%s <select id="fTema"><option value="">%s</option>%s</select></label>'
              '<label>%s <select id="fTipo"><option value="">%s</option>%s</select></label>'
              '<label>%s <select id="fLiv"><option value="">%s</option>%s</select></label>'
              '<span class="conta" id="conta"></span>'
              '<button class="b" id="bVis">%s</button><button class="b" id="bDesel">%s</button>'
              '</div><button class="b pieno" id="bComponi" hidden></button>'
              % (U["tema"], U["tutti"], opt((k, temi[k][L]) for k in temi_usati),
                 U["tipo"], U["tutti"], opt((k, Ub["tipi"][k]) for k in tipi_usati),
                 U["livello"], U["tutti"], opt((str(i), Ub["liv"][i]) for i in (1, 2, 3)),
                 U["selvis"], U["desel"]))
    tipi = '<h2 class="tema-tit" style="margin-top:1.2rem">%s</h2><ul class="tipi">%s</ul>' % (
        U["tipi_tit"], "".join("<li><b>%s</b>%s</li>" % (Ub["tipi"][k], U["tipi_desc"][k]) for k in ("testo", "scheda", "prevedi", "numero")))
    foglio = ('<section id="foglio" hidden aria-label="%s"><div class="comandi ui">'
              '<label><input type="checkbox" id="fConSol"> %s</label>'
              '<button class="b pieno" id="fStampa">%s</button><button class="b" id="fChiudi">%s</button></div>'
              '<input id="fTitolo" value="%s — %s" aria-label="%s">'
              '<div class="f-dati"><span>%s:</span><span>%s:</span><span>%s:</span></div>'
              '<ol class="f-dom" id="fDom"></ol><p class="f-piede">%s <span id="fLink"></span></p>'
              '<div class="f-sol" id="fSol" hidden></div></section>'
              % (U["foglio_tit"], U["con_sol"], U["stampa"], U["chiudi"], U["foglio_tit"], _e(libro), U["foglio_tit"],
                 U["nome"], U["classe"], U["data"], U["link_libro"]))
    T = {k: U[k] for k in ("n", "n1", "componi", "risp", "sol_tit")}
    js = JS_DOC.replace("%T%", json.dumps(T, ensure_ascii=False)).replace("%D%", json.dumps(perjs, ensure_ascii=False))
    return """<!DOCTYPE html>
<html lang="%(L)s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(libro)s — %(tit)s</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,600;1,400&family=Inter:wght@400;600&display=swap" rel="stylesheet">
<style>%(css)s</style>
%(extra)s</head>
<body>
<header class="barra"><div class="dentro"><span class="marchio">%(libro)s · %(tit)s</span>
<a href="%(home)s">%(uhome)s</a><a href="%(lh)s">%(ulibro)s</a><a href="%(alt)s" hreflang="%(altl)s">%(ualt)s</a></div></header>
<main>
<h1>%(tit)s</h1>
<p class="sotto">%(sotto)s · <i>%(libro)s</i></p>
<p class="intro">%(intro)s</p>
<p class="nota">%(nota)s</p>
%(tipi)s
%(filtri)s
%(foglio)s
%(carte)s
</main>
<footer>%(piede)s · <a href="https://github.com/MaxDvTn/digital-books">GitHub</a></footer>
<script>%(js)s</script>
</body>
</html>
""" % {"L": L, "libro": _e(libro), "tit": U["titolo"], "css": CSS_DOC, "extra": testa_extra, "home": home_href, "uhome": U["home"],
       "lh": libro_href, "ulibro": U["libro"], "alt": altra_href, "altl": "en" if L == "it" else "it", "ualt": U["altra"],
       "sotto": U["sotto"], "intro": U["intro"], "nota": U["nota"], "tipi": tipi, "filtri": filtri, "foglio": foglio,
       "carte": "\n".join(card), "js": js, "piede": U["piede"]}
