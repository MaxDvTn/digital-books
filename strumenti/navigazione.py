"""Navigazione comune ai libri interattivi: home, indietro, indice e ricerca nel testo.

Il build la aggiunge alla barra in alto con:

    import navigazione
    pagina = navigazione.applica(pagina, casa="../../index.html", sommario=None)

- casa: percorso della home del sito, relativo alla pagina del libro.
- sommario: facoltativo, {lingua: [[id, titolo, livello], ...]}. Se manca, l'indice si costruisce
  da solo con i titoli del testo (h2[id], h3.sez[id]). Le tavole interattive (section.scheda[id])
  e le note (#note) si aggiungono sempre in fondo.

I testi dell'interfaccia (it/en) stanno nello script, che comincia con /*lingue*/ e quindi
non passa dal dizionario delle traduzioni. L'HTML inserito non contiene testo.
"""
import json

# Contatore delle visite (GoatCounter). Vuoto = nessun contatore.
# Dopo aver creato il sito su goatcounter.com, scrivere qui il codice (es. "classici-scienza").
GOATCOUNTER = ""


def contatore_html():
    if not GOATCOUNTER:
        return ""
    return ('<script data-goatcounter="https://%s.goatcounter.com/count" '
            'async src="https://gc.zgo.at/count.js"></script>' % GOATCOUNTER)


HTML = ('<div class="nv-sx">'
        '<a class="b ui nv-btn" id="nvCasa" href="%CASA%"></a>'
        '<button class="b ui nv-btn" id="nvIndietro" type="button"></button>'
        '</div>')
HTML_DX = ('<button class="b ui nv-btn" id="nvCerca" type="button"></button>'
           '<button class="b ui nv-btn nv-indice" id="nvIndice" type="button" aria-expanded="false" aria-controls="nvPannello"></button>')
PANNELLO = ('<div class="nv-velo" id="nvVelo" hidden></div>'
            '<aside class="nv-pannello ui" id="nvPannello" hidden role="dialog" aria-modal="true" aria-labelledby="nvTitolo">'
            '<div class="nv-testa"><h2 id="nvTitolo"></h2><a class="nv-casa" id="nvCasa2" href="%CASA%"></a><button class="b nv-chiudi" id="nvChiudi" type="button"></button></div>'
            '<div class="nv-campo"><input type="search" id="nvQ" autocomplete="off" spellcheck="false"></div>'
            '<p class="nv-conta" id="nvConta" aria-live="polite"></p>'
            '<ol class="nv-risultati" id="nvRisultati" hidden></ol>'
            '<nav class="nv-sommario" id="nvSommario"></nav>'
            '</aside>')

CSS = """
.nv-sx{display:flex;gap:.3rem;flex:none}
.nv-btn{display:inline-flex;align-items:center;justify-content:center;gap:.35rem;text-decoration:none;font-size:.82rem;padding:.35rem .6rem}
a.nv-btn{color:var(--inchiostro);border:1px solid var(--linea);border-radius:8px;background:#fff;min-height:44px;min-width:44px}
a.nv-btn:hover{border-color:var(--attivo)}
.nv-btn .ic{font-size:1.05rem;line-height:1}
.nv-velo{position:fixed;inset:0;background:rgba(34,32,28,.28);z-index:40}
.nv-pannello{position:fixed;top:0;right:0;bottom:0;width:min(400px,92vw);z-index:41;background:var(--carta);border-left:1px solid var(--linea);box-shadow:-8px 0 24px rgba(0,0,0,.12);display:flex;flex-direction:column}
.nv-testa{display:flex;align-items:center;justify-content:space-between;padding:.6rem .8rem .3rem 1rem}
.nv-testa h2{margin:0;font:600 1.25rem "EB Garamond",Georgia,serif;font-variant:small-caps;letter-spacing:.04em;color:var(--rubrica);text-align:left}
.nv-campo{padding:.3rem 1rem .4rem}
.nv-campo input{width:100%;font:1rem Inter,system-ui,sans-serif;min-height:44px;padding:0 .8rem;border:1px solid var(--linea);border-radius:8px;background:#fff;color:var(--inchiostro)}
.nv-campo input:focus{outline:3px solid #f0b400;outline-offset:1px;border-color:var(--attivo)}
.nv-conta{margin:0;padding:0 1rem .4rem;font-size:.78rem;color:var(--dato);min-height:1.2em}
.nv-sommario,.nv-risultati{flex:1;overflow-y:auto;overscroll-behavior:contain;padding:0 .5rem 2rem;margin:0}
.nv-sommario ol{list-style:none;margin:0;padding:0}
.nv-sommario .gruppo{font-size:.68rem;text-transform:uppercase;letter-spacing:.08em;color:var(--rubrica);margin:1rem .5rem .3rem;font-weight:600}
.nv-sommario a{display:block;padding:.55rem .6rem;border-radius:6px;color:var(--inchiostro);text-decoration:none;font:1.02rem/1.3 "EB Garamond",Georgia,serif;min-height:44px}
.nv-sommario a .sotto{display:block;font-size:.85rem;font-style:italic;color:var(--dato)}
.nv-sommario a.l2{padding-left:1.6rem;font-size:.95rem}
.nv-sommario a.tav::before{content:"◆ ";color:var(--rubrica);font-size:.75em}
.nv-sommario a:hover,.nv-sommario a:focus{background:var(--pannello)}
.nv-sommario a[aria-current=true]{background:var(--pannello);box-shadow:inset 3px 0 0 var(--rubrica)}
.nv-risultati{list-style:none}
.nv-risultati li a{display:block;padding:.6rem .6rem;border-radius:6px;color:var(--inchiostro);text-decoration:none;border-bottom:1px solid var(--linea)}
.nv-risultati li a:hover,.nv-risultati li a:focus{background:var(--pannello)}
.nv-risultati .dove{display:block;font-size:.68rem;text-transform:uppercase;letter-spacing:.06em;color:var(--rubrica);margin-bottom:.15rem}
.nv-risultati .brano{display:block;font:.98rem/1.4 "EB Garamond",Georgia,serif}
.nv-risultati mark,mark.nv-trovato{background:#f6dc8a;color:inherit;border-radius:2px;padding:0 .05em}
.nv-lampo{animation:nvLampo 2.4s ease}
@keyframes nvLampo{0%,40%{background:#fbefc4}100%{background:transparent}}
@media (prefers-reduced-motion: reduce){.nv-lampo{animation:none;background:#fbefc4}}
header.barra .dentro{flex-wrap:nowrap}header.barra .dentro>nav{flex:1;min-width:0}
#nvCasa .tx,#nvIndietro .tx,#nvCerca .tx{display:none}
@media(max-width:1279px){header.barra .marchio{display:none}}
@media(max-width:1023px){.nv-btn .tx{display:none}}
@media(max-width:600px){header.barra .dentro>nav{display:none}header.barra .dentro{justify-content:space-between}#nvCerca,#nvCasa{display:none}.nv-btn{padding:.3rem .45rem}}
.nv-testa .nv-casa{margin-right:auto;margin-left:.6rem;font-size:.8rem;color:var(--attivo);text-decoration:none;display:inline-flex;align-items:center;min-height:44px;padding:0 .4rem}
"""

JS = r"""/*lingue*/ /*navigazione*/
(function(){
  const L = (document.documentElement.lang || "it").slice(0, 2);
  const T = {
    it: {casa: "Home", casaT: "Torna alla home del sito", indietro: "Indietro", indietroT: "Torna al punto precedente",
         indice: "Indice", indiceT: "Indice e ricerca nel libro", cerca: "Cerca", cercaT: "Cerca nel libro (tasto /)",
         chiudi: "Chiudi", segnaposto: "Cerca nel libro…", tavole: "Tavole interattive", copertina: "Copertina",
         note: "Note all'edizione", nessuno: "Nessun risultato", uno: "1 risultato", molti: n => n + " risultati",
         primi: (m, n) => "primi " + m + " di " + n + " risultati", breve: "Scrivi almeno due lettere", testo: "Testo"},
    en: {casa: "Home", casaT: "Back to the home page", indietro: "Back", indietroT: "Back to where you were",
         indice: "Contents", indiceT: "Contents and search", cerca: "Search", cercaT: "Search the book (/ key)",
         chiudi: "Close", segnaposto: "Search the book…", tavole: "Interactive plates", copertina: "Cover",
         note: "Notes on this edition", nessuno: "No results", uno: "1 result", molti: n => n + " results",
         primi: (m, n) => "first " + m + " of " + n + " results", breve: "Type at least two letters", testo: "Text"}
  }[L] || null;
  if (!T) return;
  const $ = id => document.getElementById(id);
  const SOMMARIO = (window.NAV_SOMMARIO || {})[L];
  const btn = (el, ic, tx, tit) => { if (!el) return; el.innerHTML = '<span class="ic" aria-hidden="true">' + ic + '</span><span class="tx">' + tx + '</span>';
    el.title = tit; el.setAttribute("aria-label", tx); };
  btn($("nvCasa"), "⌂", T.casa, T.casaT);
  btn($("nvIndietro"), "←", T.indietro, T.indietroT);
  btn($("nvCerca"), '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21"/></svg>', T.cerca, T.cercaT);
  btn($("nvIndice"), "☰", T.indice, T.indiceT);
  $("nvTitolo").textContent = T.indice; $("nvCasa2").textContent = "⌂ " + T.casa; $("nvCasa2").title = T.casaT;
  $("nvChiudi").textContent = "✕"; $("nvChiudi").setAttribute("aria-label", T.chiudi); $("nvChiudi").title = T.chiudi;
  $("nvQ").placeholder = T.segnaposto; $("nvQ").setAttribute("aria-label", T.segnaposto);

  /* ---------- indietro: i salti dentro il libro (indice, ricerca, link #) si contano nella cronologia */
  const prof = () => (history.state && history.state.nvP) || 0;
  window.addEventListener("hashchange", () => { if (!history.state || history.state.nvP == null) {
    try { history.replaceState(Object.assign({}, history.state, {nvP: navP + 1}), ""); } catch (e) {} } navP = prof(); });
  let navP = prof();
  window.addEventListener("popstate", () => { navP = prof(); });
  function salta(id){ // nuova voce nella cronologia, così «Indietro» riporta qui
    try { history.pushState({nvP: prof() + 1}, "", "#" + id); } catch (e) { location.hash = id; }
    navP = prof();
  }
  $("nvIndietro").addEventListener("click", () => {
    const daSito = document.referrer && document.referrer.indexOf(location.origin) === 0;
    if (prof() > 0 || daSito) history.back(); else location.href = $("nvCasa").href;
  });

  /* ---------- pannello */
  const pan = $("nvPannello"), velo = $("nvVelo"), q = $("nvQ");
  let ritorno = null;
  function apri(cerca){
    if (document.body.classList.contains("lb-on") && window.Libro) Libro.chiudi();
    ritorno = document.activeElement;
    costruisciSommario(); evidenziaCorrente();
    pan.hidden = false; velo.hidden = false; $("nvIndice").setAttribute("aria-expanded", "true");
    if (cerca || q.value) { q.focus(); q.select(); } else { const c = pan.querySelector("a[aria-current=true]") || pan.querySelector("a"); if (c) c.focus(); }
  }
  function chiudi(){ pan.hidden = true; velo.hidden = true; $("nvIndice").setAttribute("aria-expanded", "false");
    if (ritorno && ritorno.focus) ritorno.focus(); }
  $("nvIndice").addEventListener("click", () => pan.hidden ? apri(false) : chiudi());
  $("nvCerca").addEventListener("click", () => apri(true));
  $("nvChiudi").addEventListener("click", chiudi);
  velo.addEventListener("click", chiudi);
  document.addEventListener("keydown", e => {
    if (e.key === "Escape" && !pan.hidden) { chiudi(); return; }
    const inCampo = /^(INPUT|TEXTAREA|SELECT)$/.test((e.target || {}).tagName || "");
    if ((e.key === "/" && !inCampo && !e.ctrlKey && !e.metaKey) || ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k")) {
      if (document.body.classList.contains("lb-on")) return;
      e.preventDefault(); apri(true);
    }
    if (e.key === "Tab" && !pan.hidden) { // il fuoco resta nel pannello
      const f = [...pan.querySelectorAll("a,button,input")].filter(x => x.offsetParent);
      if (!f.length) return;
      if (e.shiftKey && document.activeElement === f[0]) { e.preventDefault(); f[f.length - 1].focus(); }
      else if (!e.shiftKey && document.activeElement === f[f.length - 1]) { e.preventDefault(); f[0].focus(); }
    }
  });

  /* ---------- sommario */
  let voci = null;
  const pulito = el => { const c = el.cloneNode(true); c.querySelectorAll(".sotto,.ic,sup,.nota").forEach(x => x.remove()); return c.textContent.replace(/\s+/g, " ").trim(); };
  function costruisciSommario(){
    if (voci) return;
    voci = [];
    const cop = $("copertina"); if (cop) voci.push({el: cop, t: T.copertina, l: 1});
    if (SOMMARIO) for (const [id, t, l] of SOMMARIO) { const el = $(id); if (el) voci.push({el, t, l: l || 1}); }
    else document.querySelectorAll("#testo h2[id], #testo h3.sez[id]").forEach(el => {
      const s = el.querySelector(".sotto");
      voci.push({el, t: pulito(el), s: s ? s.textContent.trim() : "", l: el.tagName === "H2" ? 1 : 2}); });
    const tav = [...document.querySelectorAll("section.scheda[id]")].map(el => { const h = el.querySelector("h3"); return {el, t: h ? pulito(h).replace(/^(Scheda|Tavola|Panel|Plate)\s*·\s*/, "") : el.id, tav: true}; });
    const note = $("note");
    const esc = s => s.replace(/[&<>"]/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}[c]));
    let h = "<ol>" + voci.map((v, i) => '<li><a href="#' + v.el.id + '" data-i="' + i + '" class="l' + v.l + '">' + esc(v.t) + (v.s ? '<span class="sotto">' + esc(v.s) + '</span>' : "") + "</a></li>").join("") + "</ol>";
    if (tav.length) { h += '<p class="gruppo">' + T.tavole + "</p><ol>" + tav.map((v, i) => '<li><a class="tav" href="#' + v.el.id + '" data-t="' + i + '">' + esc(v.t) + "</a></li>").join("") + "</ol>"; }
    if (note) h += '<ol style="margin-top:1rem"><li><a href="#note">' + T.note + "</a></li></ol>";
    $("nvSommario").innerHTML = h;
    $("nvSommario").addEventListener("click", e => { const a = e.target.closest("a"); if (!a) return; e.preventDefault();
      vaiA(document.getElementById(a.getAttribute("href").slice(1))); });
    // per le sezioni dei risultati: voci in ordine di documento
    voci.sort((a, b) => a.el.compareDocumentPosition(b.el) & Node.DOCUMENT_POSITION_FOLLOWING ? -1 : 1);
  }
  function evidenziaCorrente(){
    let cur = -1;
    voci.forEach((v, i) => { if (v.el.getBoundingClientRect().top < 120) cur = i; });
    $("nvSommario").querySelectorAll("a").forEach(a => a.removeAttribute("aria-current"));
    const a = $("nvSommario").querySelector('a[data-i="' + cur + '"]');
    if (a) { a.setAttribute("aria-current", "true"); setTimeout(() => a.scrollIntoView({block: "center"}), 0); }
  }
  function vaiA(el, termini){
    if (!el) return;
    chiudi();
    let conId = el.id ? el : el.closest("[id]");
    if (conId) salta(conId.id);
    if (el.tagName === "SECTION" && el.classList.contains("scheda")) el.scrollIntoView({block: "start"});
    else el.scrollIntoView({block: termini ? "center" : "start"});
    if (termini) { evidenzia(el, termini); el.classList.remove("nv-lampo"); void el.offsetWidth; el.classList.add("nv-lampo"); }
  }

  /* ---------- ricerca: senza accenti e senza maiuscole, tutte le parole */
  const norm1 = c => c.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase();
  function normMappa(s){ let n = "", m = []; for (let i = 0; i < s.length; i++) { const x = norm1(s[i]); for (const _ of x) m.push(i); n += x; } m.push(s.length); return [n, m]; }
  let indice = null;
  function costruisciIndice(){
    if (indice) return;
    costruisciSommario();
    const sel = "#testo p, #testo li, #testo h2, #testo h3, #testo figcaption, #testo td, #note p";
    const els = [...document.querySelectorAll(sel)].filter(el => {
      const sc = el.closest("section.scheda");
      if (sc && !el.matches("section.scheda > h3, section.scheda .intro")) return false;
      return !el.closest(".lb-tav, #libro, .nv-pannello, details") && el.textContent.trim().length > 1;
    });
    let k = 0;
    indice = els.map(el => {
      while (k < voci.length - 1 && (voci[k + 1].el === el || voci[k + 1].el.compareDocumentPosition(el) & Node.DOCUMENT_POSITION_FOLLOWING)) k++;
      const dove = voci.length && (voci[k].el === el || voci[k].el.compareDocumentPosition(el) & Node.DOCUMENT_POSITION_FOLLOWING) ? voci[k].t : "";
      const sc = el.closest("section.scheda"), tit = sc && sc.querySelector("h3");
      const testo = el.textContent.replace(/\s+/g, " ").trim();
      return {el, testo, n: normMappa(testo)[0], dove: tit ? "◆ " + pulito(tit) : (el.closest("#note") ? T.note : dove)};
    });
  }
  const esc = s => s.replace(/[&<>"]/g, c => ({"&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;"}[c]));
  function brano(r, termini){
    const [n, m] = normMappa(r.testo);
    let pos = [];
    for (const t of termini) { let i = n.indexOf(t); while (i >= 0) { pos.push([m[i], m[i + t.length]]); i = n.indexOf(t, i + t.length); } }
    pos.sort((a, b) => a[0] - b[0]);
    const unite = []; for (const p of pos) { const u = unite[unite.length - 1]; if (u && p[0] <= u[1]) u[1] = Math.max(u[1], p[1]); else unite.push(p.slice()); }
    const primo = unite.length ? unite[0][0] : 0;
    let a = Math.max(0, primo - 70), b = Math.min(r.testo.length, primo + 150);
    if (a > 0) { const s = r.testo.indexOf(" ", a); if (s > 0 && s < primo) a = s + 1; }
    if (b < r.testo.length) { const s = r.testo.lastIndexOf(" ", b); if (s > primo) b = s; }
    let out = "", c = a;
    for (const [x, y] of unite) { if (y <= a || x >= b) continue; out += esc(r.testo.slice(c, Math.max(c, x))) + "<mark>" + esc(r.testo.slice(Math.max(c, x), Math.min(y, b))) + "</mark>"; c = Math.min(y, b); }
    out += esc(r.testo.slice(c, b));
    return (a > 0 ? "… " : "") + out + (b < r.testo.length ? " …" : "");
  }
  const MAX = 80;
  let trovati = [], termini = [], attesa = null;
  function cerca(){
    const v = q.value.trim();
    const ris = $("nvRisultati"), som = $("nvSommario"), conta = $("nvConta");
    if (!v) { ris.hidden = true; som.hidden = false; conta.textContent = ""; $("nvTitolo").textContent = T.indice; return; }
    $("nvTitolo").textContent = T.cerca;
    termini = [...new Set(normMappa(v)[0].split(/[\s,.;:!?«»"“”'’()\[\]]+/).filter(t => t.length > 1))];
    som.hidden = true; ris.hidden = false;
    if (!termini.length) { ris.innerHTML = ""; conta.textContent = T.breve; return; }
    costruisciIndice();
    trovati = indice.filter(r => termini.every(t => r.n.includes(t)));
    const n = trovati.length;
    conta.textContent = n === 0 ? T.nessuno : n === 1 ? T.uno : n > MAX ? T.primi(MAX, n) : T.molti(n);
    ris.innerHTML = trovati.slice(0, MAX).map((r, i) => '<li><a href="#" data-r="' + i + '">' + (r.dove ? '<span class="dove">' + esc(r.dove) + "</span>" : "") +
      '<span class="brano">' + brano(r, termini) + "</span></a></li>").join("");
  }
  q.addEventListener("input", () => { clearTimeout(attesa); attesa = setTimeout(cerca, 160); });
  q.addEventListener("keydown", e => { if (e.key === "Enter") { e.preventDefault(); clearTimeout(attesa); cerca(); if (trovati.length) vaiA(trovati[0].el, termini); }
    if (e.key === "ArrowDown") { const a = $("nvRisultati").querySelector("a"); if (a) { e.preventDefault(); a.focus(); } } });
  $("nvRisultati").addEventListener("click", e => { const a = e.target.closest("a[data-r]"); if (!a) return; e.preventDefault(); vaiA(trovati[+a.dataset.r].el, termini); });
  $("nvRisultati").addEventListener("keydown", e => { const a = e.target.closest("a"); if (!a) return; const li = a.parentElement;
    if (e.key === "ArrowDown" && li.nextElementSibling) { e.preventDefault(); li.nextElementSibling.querySelector("a").focus(); }
    if (e.key === "ArrowUp") { e.preventDefault(); (li.previousElementSibling ? li.previousElementSibling.querySelector("a") : q).focus(); } });

  /* evidenzia le parole cercate nel paragrafo (si tolgono dopo un po' o alla ricerca successiva) */
  let segnati = [], timer = null;
  function togli(){ for (const m of segnati) { const p = m.parentNode; if (!p) continue; p.replaceChild(document.createTextNode(m.textContent), m); p.normalize(); } segnati = []; }
  function evidenzia(el, termini){
    togli(); clearTimeout(timer);
    const w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT), nodi = [];
    while (w.nextNode()) nodi.push(w.currentNode);
    for (const nodo of nodi) {
      const s = nodo.nodeValue, [n, m] = normMappa(s), pos = [];
      for (const t of termini) { let i = n.indexOf(t); while (i >= 0) { pos.push([m[i], m[i + t.length]]); i = n.indexOf(t, i + t.length); } }
      if (!pos.length) continue;
      pos.sort((a, b) => a[0] - b[0]);
      const fr = document.createDocumentFragment(); let c = 0;
      for (const [x, y] of pos) { if (x < c) continue; fr.appendChild(document.createTextNode(s.slice(c, x)));
        const mk = document.createElement("mark"); mk.className = "nv-trovato"; mk.textContent = s.slice(x, y); fr.appendChild(mk); segnati.push(mk); c = y; }
      fr.appendChild(document.createTextNode(s.slice(c)));
      nodo.parentNode.replaceChild(fr, nodo);
    }
    timer = setTimeout(togli, 12000);
  }
})();
"""


def applica(pagina, casa, sommario=None):
    """Inserisce barra, pannello, stile e script nella pagina di un libro (template con header.barra)."""
    testa = '<header class="barra"><div class="dentro">'
    if testa not in pagina:
        raise ValueError("navigazione: barra in alto non trovata")
    pagina = pagina.replace(testa, testa + HTML.replace("%CASA%", casa), 1)
    # indice e ricerca a destra, prima del selettore di lingua (o in fondo alla barra)
    pagina = pagina.replace("</div></header>", HTML_DX + "</div></header>", 1)
    pagina = pagina.replace("</head>", "<style>%s</style>\n%s</head>" % (CSS, contatore_html()), 1)
    dati = "window.NAV_SOMMARIO=%s;\n" % json.dumps(sommario or {}, ensure_ascii=False)
    pagina = pagina.replace("</body>", PANNELLO.replace("%CASA%", casa) + "<script>%s</script>\n</body>" % (JS.replace("(function(){", dati + "(function(){", 1)), 1)
    return pagina
