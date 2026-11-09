"""Pagine in più lingue per i libri interattivi.

Una pagina per lingua, generata dallo stesso build:
  index.html (italiano), index.en.html (inglese), index.<xx>.html ...

- estrai(pagina): trova i testi dell'interfaccia (nodi di testo, attributi alt/title/
  aria-label/placeholder, stringhe negli script) con la loro posizione.
- traduci(pagina, dizionario): li sostituisce con la traduzione; restituisce anche
  l'elenco di quelli senza traduzione.
- Il testo del libro non passa di qui: il build lo inserisce come segnaposto ⟦…⟧
  e lo sostituisce dopo con riempi().
- menu_html / MENU_JS: il selettore di lingua nella barra in alto.
"""
import html as _html, json, os, re

LINGUE = {  # codice: (nome nella lingua, etichetta corta)
    "it": ("Italiano", "IT"),
    "en": ("English", "EN"),
}

def nome_file(lingua):
    return "index.html" if lingua == "it" else "index.%s.html" % lingua

SEGNAPOSTO = re.compile(r"⟦[^⟧]*⟧")
_TRADUCIBILE = re.compile(r"[A-Za-zÀ-ÿ]{2,}")
# stringhe che sono codice, non testo: id, classi, selettori, nomi di eventi, formati
_CODICE = re.compile(r"^[#.\w:\[\]=\-\"' >*+~()/%,]*$")

def _parola_sola_codice(s):
    s = s.strip()
    if " " in s:
        return False
    return bool(_CODICE.match(s)) and re.search(r"[-_.#\[\]=(:/]|[a-z][A-Z]|\d", s) is not None

def _segmenti_script(js, base, out):
    """Stringhe '…', "…", `…` in un sorgente JS (salta commenti e regex semplici)."""
    i, n = 0, len(js)
    while i < n:
        c = js[i]
        if c == "/" and i + 1 < n and js[i + 1] in "/*":
            j = js.find("\n", i) if js[i + 1] == "/" else js.find("*/", i + 2) + 2
            i = n if j <= 0 else j
            continue
        if c in "'\"`":
            j, q = i + 1, c
            while j < n and js[j] != q:
                if js[j] == "\\":
                    j += 1
                elif q == "`" and js.startswith("${", j):
                    d, j = 1, j + 2
                    while j < n and d:
                        d += {"{": 1, "}": -1}.get(js[j], 0)
                        j += 1
                    continue
                elif q != "`" and js[j] == "\n":
                    break
                j += 1
            s = js[i + 1:j]
            if _TRADUCIBILE.search(s) and not SEGNAPOSTO.fullmatch(s.strip()) and not _parola_sola_codice(s) \
               and not s.startswith(("data:", "http", "M ", "#", "rgba", "var(")) and "{" not in s.replace("${", ""):
                out.append((base + i + 1, base + j, s, "js"))
            i = j + 1
            continue
        i += 1

def _del_menu(t):
    """testi del menu delle lingue: restano uguali in ogni pagina"""
    nomi = [v[0] for v in LINGUE.values()] + [v[1] for v in LINGUE.values()]
    return t in nomi or t.startswith("Lingua / Language") or all(x in nomi for x in t.split(" · "))

NT_APRI, NT_CHIUDI = "<!--n-->", "<!--/n-->"
def nt(testo):
    """segna un testo che non passa dal dizionario (testo del libro, testi già nella lingua giusta)"""
    return NT_APRI + testo + NT_CHIUDI
NT_ATTR = "\u2063"   # separatore invisibile: in testa al valore di un attributo che non si traduce
def nt_attr(testo):
    return NT_ATTR + testo
def togli_marcatori(pagina):
    return pagina.replace(NT_APRI, "").replace(NT_CHIUDI, "").replace(NT_ATTR, "")

def estrai(pagina, salta_script=()):
    """Restituisce [(inizio, fine, testo, tipo)] in ordine di posizione.
    salta_script: prefissi di <script> da ignorare (dati JSON)."""
    out, salta = [], False
    for m in re.finditer(r"<script\b[^>]*>(.*?)</script>|<style\b[^>]*>.*?</style>|<!--.*?-->|<![^>]*>|</[a-zA-Z][^>]*>|<([a-zA-Z][^>]*)>|([^<]+)", pagina, re.S):
        if m.group(0) in (NT_APRI, NT_CHIUDI):   # testo del libro: non si traduce
            salta = m.group(0) == NT_APRI
            continue
        if salta:
            continue
        if m.group(1) is not None:
            js = m.group(1)
            if not js.strip() or any(js.lstrip().startswith(p) for p in salta_script):
                continue
            _segmenti_script(js, m.start(1), out)
        elif m.group(2) is not None:
            for a in re.finditer(r'\b(alt|title|aria-label|placeholder|data-tip)="([^"]*)"', m.group(2)):
                if _TRADUCIBILE.search(a.group(2)) and not SEGNAPOSTO.fullmatch(a.group(2)) and not a.group(2).startswith(NT_ATTR):
                    s = m.start(2) + a.start(2)
                    out.append((s, s + len(a.group(2)), a.group(2), "attr"))
        elif m.group(3) is not None:
            t = m.group(3)
            core = t.strip()
            if _TRADUCIBILE.search(core) and not SEGNAPOSTO.fullmatch(core):
                s = m.start(3) + t.index(core)
                # un nodo che contiene segnaposto: si traducono solo i pezzi tra i segnaposto
                pos = s
                for parte in SEGNAPOSTO.split(core):
                    q = core.find(parte, pos - s)
                    p = parte.strip()
                    if _TRADUCIBILE.search(p):
                        k = s + q + parte.index(p)
                        out.append((k, k + len(p), p, "html"))
                    pos = s + q + len(parte)
    return sorted(x for x in out if not _del_menu(x[2]))

def traduci(pagina, diz, salta_script=()):
    """diz: {italiano: traduzione}; '=' significa «lascia com'è»; una traduzione che comincia con
    '!' può cambiare anche le espressioni ${…} (es. il formato dei numeri)."""
    segm = estrai(pagina, salta_script)
    mancanti, pezzi, fine = [], [], 0
    for a, b, t, tipo in segm:
        key = t if tipo != "html" else re.sub(r"\s+", " ", _html.unescape(t))
        tr = diz.get(t, diz.get(key))
        if tr is None:
            mancanti.append((tipo, t))
            continue
        if tr == "=":
            continue
        libero = tr.startswith("!")   # «!»: la traduzione cambia di proposito anche il codice (es. formato dei numeri)
        if libero:
            tr = tr[1:]
        if tipo == "js" and not libero:
            esp_it, esp_tr = re.findall(r"\$\{[^}]*\}", t), re.findall(r"\$\{[^}]*\}", tr)
            if sorted(esp_it) != sorted(esp_tr):
                raise ValueError("espressioni ${} diverse nella traduzione di: %r" % t[:80])
        if tipo == "attr":
            tr = tr.replace('"', "&quot;")
        if tipo == "js":   # la traduzione non deve chiudere la stringa che la contiene
            q = pagina[a - 1]
            if q in "'\"`":
                tr = re.sub(r"(?<!\\)" + re.escape(q), lambda m: "\\" + q, tr)
        pezzi.append(pagina[fine:a]); pezzi.append(tr); fine = b
    pezzi.append(pagina[fine:])
    return "".join(pezzi), mancanti

def scheletro(pagina, percorso, salta_script=()):
    """Aggiorna il dizionario (json, lista di coppie) con i testi nuovi, senza toccare quelli già tradotti."""
    vecchio = dict(json.load(open(percorso, encoding="utf-8"))) if os.path.exists(percorso) else {}
    visti, coppie = set(), []
    for a, b, t, tipo in estrai(pagina, salta_script):
        k = t if tipo != "html" else re.sub(r"\s+", " ", _html.unescape(t))
        if k in visti:
            continue
        visti.add(k)
        coppie.append([k, vecchio.get(k, "")])
    json.dump(coppie, open(percorso, "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    return sum(1 for _, v in coppie if not v)

def carica(percorso):
    return {k: v for k, v in json.load(open(percorso, encoding="utf-8")) if v}

def riempi(pagina, contenuti):
    """Sostituisce i segnaposto ⟦chiave⟧ con il contenuto vero."""
    def f(m):
        k = m.group(0)[1:-1]
        if k not in contenuti:
            raise KeyError("segnaposto senza contenuto: " + k)
        return contenuti[k]
    return SEGNAPOSTO.sub(f, pagina)

# ------------------------------------------------------------------ selettore
def menu_html(attuale, disponibili):
    opz = "".join('<option value="%s" lang="%s"%s>%s</option>' % (c, c, " selected" if c == attuale else "", LINGUE[c][1])
                  for c in LINGUE if c in disponibili)
    nomi = " · ".join(LINGUE[c][0] for c in LINGUE if c in disponibili)
    return ('<label class="lingua ui" title="%s">'
            '<select id="selLingua" aria-label="Lingua / Language: %s" data-attuale="%s">%s</select></label>' % (nomi, nomi, attuale, opz))

MENU_CSS = """
.lingua{display:inline-flex;align-items:center;gap:.2rem;font-size:.82rem}
.lingua{flex:none}.lingua select{font:inherit;font-weight:600;letter-spacing:.04em;border:1px solid var(--linea);border-radius:8px;background:#fff;color:var(--inchiostro);min-height:44px;padding:0 .4rem;cursor:pointer}
.suggerimento-lingua{position:fixed;left:50%;bottom:1rem;transform:translateX(-50%);z-index:50;background:#fff;border:1px solid var(--linea);border-radius:10px;box-shadow:0 4px 16px rgba(0,0,0,.12);padding:.6rem .8rem;display:flex;gap:.6rem;align-items:center;font:.85rem Inter,system-ui,sans-serif}
.suggerimento-lingua button{font:inherit;border:1px solid var(--linea);background:#fff;border-radius:8px;min-height:40px;padding:0 .7rem;cursor:pointer}
.suggerimento-lingua button.si{background:var(--attivo);border-color:var(--attivo);color:#fff}
"""

FILES = {c: nome_file(c) for c in LINGUE}

MENU_JS = r"""/*lingue*/
(function(){
  const FILES = %FILES%;
  const sel = document.getElementById("selLingua"); if (!sel) return;
  const attuale = sel.dataset.attuale, disponibili = [...sel.options].map(o => o.value);
  // il punto di lettura: il primo elemento con id visibile in alto
  function ancora(){
    let best = null;
    for (const sel of ["#testo > [id]", "main > [id]"]) {
      for (const e of document.querySelectorAll(sel)) { const r = e.getBoundingClientRect(); if (r.bottom > 80) { best = e; break; } }
      if (best) break;
    }
    return best && window.scrollY > 200 ? "#" + best.id : location.hash;
  }
  function vai(l){ try { localStorage.setItem("lingua", l); } catch (e) {}
    location.href = FILES[l] + ancora(); }
  sel.addEventListener("change", () => vai(sel.value));
  let pref = null; try { pref = localStorage.getItem("lingua"); } catch (e) {}
  // la lingua scelta l'ultima volta (il menu la aggiorna sempre, quindi non ci sono rimbalzi)
  if (pref && pref !== attuale && disponibili.includes(pref)) { location.replace(FILES[pref] + location.hash); return; }
  // primo accesso con il browser in un'altra lingua: un suggerimento, non un reindirizzamento
  const nav = (navigator.language || "").slice(0, 2).toLowerCase();
  if (!pref && nav !== attuale && disponibili.includes(nav === "it" ? "it" : "en") && (nav === "it" || attuale === "it")) {
    const l = nav === "it" ? "it" : "en";
    if (l === attuale) return;
    const box = document.createElement("div"); box.className = "suggerimento-lingua"; box.setAttribute("role", "dialog");
    box.innerHTML = l === "en" ? '<span>This book is also available in English.</span><button class="si">Read in English</button><button class="no">Stay in Italian</button>'
                               : '<span>Questo libro è disponibile anche in italiano.</span><button class="si">Leggi in italiano</button><button class="no">Continue in English</button>';
    box.querySelector(".si").onclick = () => vai(l);
    box.querySelector(".no").onclick = () => { try { localStorage.setItem("lingua", attuale); } catch (e) {} box.remove(); };
    document.body.appendChild(box);
  }
})();
""".replace("%FILES%", json.dumps(FILES))
