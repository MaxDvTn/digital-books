// Modalità «libro sfogliabile» del Sidereus interattivo.
// Riusa il testo e le figure già presenti nella pagina continua (#testo), impagina in base
// allo schermo, sfoglia con una pagina che gira in 3D, apre le schede interattive a tutto schermo.
(function () {
  const $ = (s, e = document) => e.querySelector(s);
  const LAT = window.LIBRO_LATINO || [];
  const stato = { aperto: false, latino: false, doppia: true, spread: 0, spreads: [], anim: false, ancora: null };
  let radice, palco, sotto, barra, modale;

  // ------------------------------------------------------------ contenuti
  function elementiItaliani() {
    const out = [{ t: "h", html: "Avviso Astronomico" }];
    for (const el of $("#testo").children) {
      if (el.matches("p.sottotitolo")) out.push({ t: "p", html: el.innerHTML, cls: "sottotitolo" });
      else if (el.matches("p")) out.push({ t: "p", html: el.innerHTML, cls: el.className, id: el.id });
      else if (el.matches("figure")) { out.push({ t: "fig", fid: el.dataset.fig, nodo: el }); if (el.dataset.fig === "figura01") out.push({ t: "loop" }); }
      else if (el.matches("section.scheda")) out.push({ t: "tavola", id: el.id, titolo: $("h3", el).textContent.replace(/^Scheda · /, ""), intro: ($(".intro", el) || {}).textContent || "" });
    }
    return out;
  }
  function elementiLatini() {
    const out = [];
    for (const b of LAT) {
      if (b.tipo === "titolo") out.push({ t: "h", html: b.testo });
      else if (b.tipo === "figura") out.push({ t: "fig", fid: b.id, solaImmagine: true });
      else if (b.tipo === "par") out.push({ t: "p", html: b.testo + (b.note || []).map(n => ` <span class="nota">(${n.replace(/<\/?sup>/g, "")})</span>`).join(""), cls: b.testo.startsWith("<i>") && b.testo.length < 400 ? "sottotitolo" : (b.testo.length < 140 ? "t breve" : "t"), id: "la-" + b.id });
    }
    return out;
  }
  function blocchi(items) { // divide in blocchi che iniziano con una figura: le stesse 71 nei due testi
    const ch = [[]];
    for (const it of items) { if (it.t === "fig") ch.push([]); ch[ch.length - 1].push(it); }
    return ch;
  }

  // ------------------------------------------------------------ rendering degli elementi
  function nodoFigura(it) {
    const orig = document.querySelector(`#testo figure[data-fig="${it.fid}"]`);
    const f = document.createElement("figure"); f.className = "lb-fig"; f.dataset.fig = it.fid;
    const o = $("img", orig), img = o.cloneNode();
    // dimensioni esplicite: la misura dell'impaginazione non deve dipendere dalla decodifica dell'immagine
    if (o.naturalWidth) { img.width = o.naturalWidth; img.height = o.naturalHeight; }
    f.appendChild(img);
    if (!it.solaImmagine) {
      const r = $(".ricostruito", orig); if (r) f.appendChild(r.cloneNode(true));
      const cap = $("figcaption", orig); if (cap) f.appendChild(cap.cloneNode(true));
    }
    if (orig.classList.contains("piccola")) f.classList.add("piccola");
    return f;
  }
  function nodo(it, html) {
    if (it.t === "h") { const h = document.createElement("h2"); h.className = "lb-titolo"; h.innerHTML = it.html; return h; }
    if (it.t === "fig") return nodoFigura(it);
    if (it.t === "loop") {
      const f = document.createElement("figure"); f.className = "lb-loop";
      f.innerHTML = '<canvas width="420" height="420" role="img" aria-label="Animazione: le fasi della Luna in un mese, nello stile delle incisioni di Galileo"></canvas><figcaption>Un mese lunare in otto secondi, come al cannocchiale (simulazione). Tocca per fermare.</figcaption>';
      return f;
    }
    if (it.t === "tavola") {
      const d = document.createElement("div"); d.className = "lb-tavola";
      d.innerHTML = `<div class="lb-tav-et">Tavola interattiva</div><div class="lb-tav-tit">${it.titolo}</div><button class="b lb-apri" data-scheda="${it.id}">Apri la scheda ↗</button>`;
      return d;
    }
    const p = document.createElement("p"); p.className = it.cls || "t"; p.innerHTML = html !== undefined ? html : it.html;
    if (it.cont) p.classList.add("cont");
    return p;
  }

  // ------------------------------------------------------------ divisione dei paragrafi tra due pagine
  function tokenizza(html) { // parole e tag, con la pila dei tag aperti
    const tok = []; const re = /(<[^>]+>)|([^<\s]+)|(\s+)/g; let m;
    while ((m = re.exec(html))) tok.push(m[1] ? { tag: m[1] } : m[2] ? { w: m[2] } : { s: m[3] });
    return tok;
  }
  function taglia(tok, n) { // primi n "pezzi di parola"; ritorna [testa, coda] in HTML ben formato
    const pila = []; let a = "", k = 0, i = 0;
    for (; i < tok.length; i++) {
      const t = tok[i];
      if (t.tag) { if (/^<\//.test(t.tag)) pila.pop(); else if (!/\/>$/.test(t.tag)) pila.push(t.tag); a += t.tag; }
      else if (t.w) { if (k === n) break; a += t.w; k++; }
      else a += t.s;
    }
    const chiudi = pila.slice().reverse().map(t => "</" + t.match(/^<([a-zA-Z0-9]+)/)[1] + ">").join("");
    let b = pila.join("");
    for (; i < tok.length; i++) { const t = tok[i]; b += t.tag || t.w || t.s; }
    return [a.replace(/\s+$/, "") + chiudi, b.replace(/^\s+/, "")];
  }

  // ------------------------------------------------------------ impaginazione
  let misura; // pagina nascosta per le misure
  function nuovaPagina(lato) {
    const p = document.createElement("div"); p.className = "lb-pagina" + (lato === "la" ? " latina" : "");
    p.innerHTML = '<div class="lb-testata"><span></span><span></span></div><div class="lb-corpo"></div><div class="lb-piede"></div>';
    return p;
  }
  function entra(corpo) { return corpo.scrollHeight <= corpo.clientHeight + 1; }
  // Versa gli elementi nella pagina "pag" finché ci stanno; ritorna gli elementi rimasti (o null se tutto è entrato)
  function versa(items, pag, divisibile) {
    const corpo = $(".lb-corpo", pag);
    for (let i = 0; i < items.length; i++) {
      const it = items[i]; const n = nodo(it); corpo.appendChild(n);
      if (entra(corpo)) continue;
      corpo.removeChild(n);
      if (it.t === "p" && divisibile) {
        const tok = tokenizza(it.html), tot = tok.filter(t => t.w).length;
        let lo = 0, hi = tot - 1, best = 0;
        while (lo <= hi) { const mid = (lo + hi) >> 1; const [a] = taglia(tok, mid); const q = nodo(it, a); corpo.appendChild(q); const ok = entra(corpo); corpo.removeChild(q); if (ok) { best = mid; lo = mid + 1; } else hi = mid - 1; }
        if (best >= 4 && tot - best < 3) best = tot - 3;   // non lasciare una riga orfana di una o due parole
        if (best >= 4 && tot - best >= 3) {
          const [a, b] = taglia(tok, best); const q = nodo(it, a); q.classList.add("spezzato"); corpo.appendChild(q);
          return [Object.assign({}, it, { html: b, cont: true })].concat(items.slice(i + 1));
        }
      }
      if (corpo.children.length === 0) { // elemento più grande della pagina: lo forziamo
        corpo.appendChild(n); return items.slice(i + 1).length ? items.slice(i + 1) : null;
      }
      return items.slice(i);
    }
    return null;
  }
  function impagina(items) { // flusso continuo -> elenco di pagine
    const pagine = []; let resto = items;
    while (resto && resto.length) { const p = nuovaPagina(); misura.appendChild(p); resto = versa(resto, p, true); pagine.push(p); misura.removeChild(p); }
    return pagine;
  }
  function provaIntero(items, pag) { // prova a mettere tutti gli elementi senza dividere; se non entrano, ripristina
    const corpo = $(".lb-corpo", pag), prima = corpo.children.length;
    for (const it of items) { corpo.appendChild(nodo(it)); }
    if (entra(corpo)) return true;
    while (corpo.children.length > prima) corpo.removeChild(corpo.lastChild);
    return false;
  }
  function impaginaAFronte() {
    const ci = blocchi(elementiItaliani()), cl = blocchi(elementiLatini());
    const spreads = []; let L = null, I = null;
    const apri = () => { L = nuovaPagina("la"); I = nuovaPagina(); misura.appendChild(L); misura.appendChild(I); };
    const chiudi = () => { if (L) { misura.removeChild(L); misura.removeChild(I); spreads.push([L, I]); L = I = null; } };
    apri();
    for (let k = 0; k < Math.max(ci.length, cl.length); k++) {
      const a = cl[k] || [], b = ci[k] || [];
      const vuota = $(".lb-corpo", L).children.length === 0 && $(".lb-corpo", I).children.length === 0;
      if (provaIntero(a, L)) { if (provaIntero(b, I)) continue; const c = $(".lb-corpo", L); for (let j = 0; j < a.length; j++) c.removeChild(c.lastChild); }
      if (!vuota) { chiudi(); apri(); if (provaIntero(a, L)) { if (provaIntero(b, I)) continue; const c = $(".lb-corpo", L); for (let j = 0; j < a.length; j++) c.removeChild(c.lastChild); } }
      // blocco più lungo di una doppia pagina: i due testi scorrono ciascuno per conto suo
      let ra = a, rb = b;
      while ((ra && ra.length) || (rb && rb.length)) {
        if (ra && ra.length) ra = versa(ra, L, true);
        if (rb && rb.length) rb = versa(rb, I, true);
        if ((ra && ra.length) || (rb && rb.length)) { chiudi(); apri(); }
      }
    }
    chiudi();
    return spreads;
  }

  function dimensioni() {
    const W = radice.clientWidth, H = radice.clientHeight - barra.offsetHeight - 16;
    stato.doppia = W >= 860 && W / H > 1.15;
    let h = H, w = Math.round(h * 17 / 24);
    const maxW = stato.doppia ? (W - 130) / 2 : (W > 600 ? W - 120 : W - 12);
    if (w > maxW) { w = Math.floor(maxW); h = stato.doppia ? Math.round(w * 24 / 17) : Math.min(H, Math.round(w * 1.75)); }
    const fs = Math.max(13, Math.min(19, w / 26));
    radice.style.setProperty("--lb-w", w + "px"); radice.style.setProperty("--lb-h", h + "px"); radice.style.setProperty("--lb-fs", fs + "px");
  }

  function costruisci() {
    dimensioni();
    misura.innerHTML = "";
    let spreads;
    if (stato.latino) {
      spreads = impaginaAFronte();
      if (!stato.doppia) spreads = spreads.flatMap(s => [[s[0]], [s[1]]]);
    } else {
      const pagine = impagina(elementiItaliani());
      if (stato.doppia) { spreads = [[null, pagine[0]]]; for (let i = 1; i < pagine.length; i += 2) spreads.push([pagine[i], pagine[i + 1] || null]); }
      else spreads = pagine.map(p => [p]);
    }
    // numeri di pagina e testatine
    let n = 0;
    spreads.forEach(s => s.forEach((p, j) => {
      if (!p) return; n++;
      const sx = stato.doppia ? j === 0 : n % 2 === 0;
      const t = p.querySelectorAll(".lb-testata span");
      if (p.classList.contains("latina")) { t[0].textContent = "Sidereus Nuncius"; t[1].textContent = "Venetiis, MDCX"; }
      else if (stato.latino) { t[0].textContent = "Avviso Astronomico"; t[1].textContent = "trad. L. Lanzillotta"; }
      else { t[0].textContent = sx ? "Galileo Galilei" : ""; t[1].textContent = sx ? "" : "Avviso Astronomico"; }
      $(".lb-piede", p).textContent = n; p.dataset.n = n;
      if (stato.doppia) p.classList.add(j === 0 ? "sx" : "dx");
    }));
    stato.spreads = spreads; stato.pagine = n;
    $(".lb-salto", barra).max = spreads.length - 1;
  }

  // ------------------------------------------------------------ visualizzazione e sfoglio
  function pagOVuota(p, lato) {
    if (p) { const c = p.cloneNode(true); return c; }
    const v = nuovaPagina(); v.classList.add("vuota", lato); $(".lb-testata", v).innerHTML = "";
    if (lato === "sx" && stato.spread === 0) v.innerHTML = '<div class="lb-frontespizio"><div>GALILEO GALILEI</div><div class="g">SIDEREUS<br>NUNCIUS</div><div>Avviso Astronomico</div><div class="p">Venezia, 1610<br>traduzione di Luisa Lanzillotta</div></div>';
    return v;
  }
  function mostra(i, dir) {
    i = Math.max(0, Math.min(stato.spreads.length - 1, i));
    const vecchio = stato.spread; stato.spread = i;
    const s = stato.spreads[i];
    const vista = document.createElement("div"); vista.className = "lb-vista" + (stato.doppia ? " doppia" : "");
    if (stato.doppia) { vista.appendChild(pagOVuota(s[0], "sx")); vista.appendChild(pagOVuota(s[1], "dx")); }
    else vista.appendChild(pagOVuota(s[0], "dx"));
    const prima = $(".lb-vista", palco);
    if (dir && prima && !matchMedia("(prefers-reduced-motion: reduce)").matches) gira(prima, vista, dir);
    else { palco.innerHTML = ""; palco.appendChild(vista); }
    const ps = s.filter(Boolean).map(p => p.dataset.n);
    $(".lb-num", barra).textContent = ps.length ? `pag. ${ps.join("–")} di ${stato.pagine}` : "";
    $(".lb-salto", barra).value = i;
    stato.ancora = s.filter(Boolean).map(p => $(".lb-corpo > p[id]:not(.cont), .lb-corpo > figure", p)).find(Boolean);
    try { history.replaceState(null, "", "#pagina-" + (ps[0] || 1)); } catch (e) { }
  }
  function gira(prima, dopo, dir) {
    stato.anim = true;
    const doppia = stato.doppia;
    const sotto = dopo.cloneNode(true);
    const vecchieP = prima.children, nuoveP = dopo.children;
    // sotto: la parte che non gira resta quella vecchia finché la pagina passa
    if (doppia) { if (dir > 0) sotto.replaceChild(vecchieP[0].cloneNode(true), sotto.children[0]); else sotto.replaceChild(vecchieP[1].cloneNode(true), sotto.children[1]); }
    const foglio = document.createElement("div"); foglio.className = "lb-foglio " + (dir > 0 ? "avanti" : "indietro") + (doppia ? " doppia" : "");
    const fronte = document.createElement("div"); fronte.className = "lb-faccia fronte";
    const retro = document.createElement("div"); retro.className = "lb-faccia retro";
    if (doppia) {
      fronte.appendChild((dir > 0 ? vecchieP[1] : vecchieP[0]).cloneNode(true));
      retro.appendChild((dir > 0 ? nuoveP[0] : nuoveP[1]).cloneNode(true));
    } else {
      fronte.appendChild((dir > 0 ? vecchieP[0] : nuoveP[0]).cloneNode(true));
      retro.appendChild(nuoveP[0].cloneNode(true)); retro.style.visibility = "hidden";
      if (dir < 0) sotto.replaceChild(vecchieP[0].cloneNode(true), sotto.children[0]);
    }
    foglio.appendChild(fronte); foglio.appendChild(retro);
    palco.innerHTML = ""; palco.appendChild(sotto); sotto.appendChild(foglio);
    requestAnimationFrame(() => requestAnimationFrame(() => foglio.classList.add("via")));
    setTimeout(() => { palco.innerHTML = ""; palco.appendChild(dopo); stato.anim = false; }, 720);
  }
  function avanti() { if (!stato.anim && stato.spread < stato.spreads.length - 1) mostra(stato.spread + 1, 1); }
  function indietro() { if (!stato.anim && stato.spread > 0) mostra(stato.spread - 1, -1); }
  function vaiAPagina(n) { const i = stato.spreads.findIndex(s => s.some(p => p && +p.dataset.n === n)); mostra(i < 0 ? 0 : i); }
  function vaiAElemento(sel) { const i = stato.spreads.findIndex(s => s.some(p => p && p.querySelector(sel))); if (i >= 0) mostra(i); }

  function ricostruisci() {
    const anc = stato.ancora;
    const sel = anc ? (anc.id ? "#" + CSS.escape(anc.id) : anc.dataset && anc.dataset.fig ? `figure[data-fig="${anc.dataset.fig}"]` : null) : null;
    costruisci();
    if (sel) vaiAElemento(sel); else mostra(0);
  }

  // ------------------------------------------------------------ animazione in loop delle fasi
  let FOT = null, t0 = 0, fermo = false, rafLoop = 0;
  function preparaFotogrammi() {
    if (FOT || !window.FasiFotogrammi) return;
    try { FOT = window.FasiFotogrammi(72, 420); } catch (e) { console.error(e); FOT = null; }
  }
  function ciclo(ora) {
    rafLoop = 0;
    if (!stato.aperto) return;
    const tele = radice.querySelectorAll(".lb-palco .lb-loop canvas");
    if (tele.length) {
      if (!FOT) preparaFotogrammi();
      if (FOT && FOT.pronti < FOT.n && !stato.anim) FOT.avanza(10); // pochi millisecondi per fotogramma video
      if (!t0) t0 = ora;
      const ridotto = matchMedia("(prefers-reduced-motion: reduce)").matches;
      const disp = FOT ? FOT.pronti : 0;
      let k = -1;
      if (disp > 0) {
        if (ridotto) k = Math.min(disp - 1, Math.round(FOT.n * 4.5 / 29.53));
        else k = Math.floor(((fermo ? tFermo : ora) - t0) / 1000 * 9) % (disp >= FOT.n ? FOT.n : disp);
      }
      tele.forEach(c => {
        const g = c.getContext("2d");
        if (k < 0) { g.fillStyle = "#fbf8f2"; g.fillRect(0, 0, c.width, c.height); g.font = "italic 22px 'EB Garamond', Georgia, serif"; g.fillStyle = "#6b6458"; g.textAlign = "center"; g.fillText("preparo l'animazione…", c.width / 2, c.height / 2); return; }
        const sx = (k % FOT.cols) * FOT.size, sy = Math.floor(k / FOT.cols) * FOT.size;
        g.drawImage(FOT.sprite, sx, sy, FOT.size, FOT.size, 0, 0, c.width, c.height);
        const giorno = Math.floor(k / FOT.n * 29.53);
        g.font = "italic 22px 'EB Garamond', Georgia, serif"; g.fillStyle = "#1e1c1a"; g.textAlign = "right";
        g.fillText(giorno === 0 ? "luna nuova" : "giorno " + giorno, c.width - 14, c.height - 14);
      });
    }
    rafLoop = requestAnimationFrame(ciclo);
  }
  let tFermo = 0;
  function avviaCiclo() { if (!rafLoop) rafLoop = requestAnimationFrame(ciclo); }

  // ------------------------------------------------------------ schede a tutto schermo
  let segnaposto = null, schedaAperta = null;
  function apriScheda(id, dopo) {
    const sez = document.getElementById(id); if (!sez) return;
    segnaposto = document.createComment("scheda"); sez.parentNode.insertBefore(segnaposto, sez);
    $(".lb-modale-corpo", modale).appendChild(sez); schedaAperta = sez;
    modale.hidden = false; $(".lb-chiudi", modale).focus();
    window.dispatchEvent(new Event("resize"));
    if (dopo) dopo();
  }
  function chiudiScheda() {
    if (!schedaAperta) return;
    segnaposto.parentNode.insertBefore(schedaAperta, segnaposto); segnaposto.remove();
    schedaAperta = null; modale.hidden = true; window.dispatchEvent(new Event("resize"));
  }

  // ------------------------------------------------------------ apertura e controlli
  function pronte() { return Promise.all([...document.querySelectorAll("#testo figure img")].map(i => i.decode ? i.decode().catch(() => { }) : Promise.resolve())); }
  async function apri(pagina) {
    await pronte();
    stato.aperto = true; radice.hidden = false; document.body.classList.add("lb-on");
    $("#btnLibro").setAttribute("aria-pressed", "true");
    costruisci();
    if (pagina) vaiAPagina(pagina); else mostra(0);
    palco.focus(); avviaCiclo();
  }
  function chiudi() {
    stato.aperto = false; radice.hidden = true; document.body.classList.remove("lb-on");
    $("#btnLibro").setAttribute("aria-pressed", "false");
    try { history.replaceState(null, "", "#testo"); } catch (e) { }
  }

  function init() {
    radice = document.createElement("div"); radice.id = "libro"; radice.hidden = true; radice.setAttribute("role", "region"); radice.setAttribute("aria-label", "Il libro sfogliabile");
    radice.innerHTML = `
      <div class="lb-barra ui">
        <button class="b lb-esci">← Pagina continua</button>
        <button class="b lb-latino" aria-pressed="false">Latino a fronte</button>
        <span class="lb-num" aria-live="polite"></span>
        <input type="range" class="lb-salto" min="0" max="1" value="0" aria-label="Vai a pagina">
      </div>
      <div class="lb-tavolo">
        <button class="lb-freccia sx" aria-label="Pagina precedente">‹</button>
        <div class="lb-palco" tabindex="0"></div>
        <button class="lb-freccia dx" aria-label="Pagina successiva">›</button>
      </div>
      <div class="lb-misura" aria-hidden="true"></div>`;
    document.body.appendChild(radice);
    modale = document.createElement("div"); modale.className = "lb-modale"; modale.hidden = true; modale.setAttribute("role", "dialog"); modale.setAttribute("aria-label", "Scheda interattiva");
    modale.innerHTML = '<div class="lb-modale-barra ui"><button class="b lb-chiudi">✕ Torna al libro</button></div><div class="lb-modale-corpo"></div>';
    document.body.appendChild(modale);
    barra = $(".lb-barra", radice); palco = $(".lb-palco", radice); misura = $(".lb-misura", radice);

    $(".lb-esci", radice).addEventListener("click", chiudi);
    $(".lb-latino", radice).addEventListener("click", (e) => { stato.latino = !stato.latino; e.currentTarget.setAttribute("aria-pressed", stato.latino); ricostruisci(); });
    $(".lb-salto", radice).addEventListener("input", (e) => mostra(+e.target.value));
    $(".lb-freccia.sx", radice).addEventListener("click", indietro);
    $(".lb-freccia.dx", radice).addEventListener("click", avanti);
    $(".lb-chiudi", modale).addEventListener("click", chiudiScheda);
    document.addEventListener("keydown", (e) => {
      if (!stato.aperto) return;
      if (schedaAperta) { if (e.key === "Escape") chiudiScheda(); return; }
      if (e.target.tagName === "INPUT") return;
      if (e.key === "ArrowRight" || e.key === "PageDown") { avanti(); e.preventDefault(); }
      if (e.key === "ArrowLeft" || e.key === "PageUp") { indietro(); e.preventDefault(); }
      if (e.key === "Escape") chiudi();
    });
    // tocchi: clic sui margini o trascinamento orizzontale
    let x0 = null, y0 = null;
    palco.addEventListener("pointerdown", (e) => { x0 = e.clientX; y0 = e.clientY; });
    palco.addEventListener("pointerup", (e) => {
      if (x0 === null) return; const dx = e.clientX - x0, dy = e.clientY - y0; x0 = null;
      if (e.target.closest("button, a, input")) return;
      if (Math.abs(dx) > 45 && Math.abs(dx) > Math.abs(dy)) { dx < 0 ? avanti() : indietro(); return; }
      if (Math.abs(dx) < 8 && Math.abs(dy) < 8) { const r = palco.getBoundingClientRect(); const fx = (e.clientX - r.left) / r.width; if (fx > 0.8) avanti(); else if (fx < 0.2) indietro(); }
    });
    palco.addEventListener("click", (e) => {
      const b = e.target.closest(".lb-apri"); if (b) { apriScheda(b.dataset.scheda); return; }
      if (e.target.closest(".lb-loop")) { e.stopPropagation(); if (!fermo) { fermo = true; tFermo = performance.now(); } else { t0 += performance.now() - tFermo; fermo = false; } return; }
      const g = e.target.closest(".vaiOss"); if (g) { e.stopPropagation(); apriScheda("giove", () => { if (window.osserva) window.osserva(+g.dataset.i); }); }
    }, true);
    let t = null;
    window.addEventListener("resize", () => { if (!stato.aperto || schedaAperta) return; clearTimeout(t); t = setTimeout(ricostruisci, 200); });
    $("#btnCielo").addEventListener("click", () => { if (stato.aperto) setTimeout(ricostruisci, 50); });
    $("#btnLibro").addEventListener("click", () => stato.aperto ? chiudi() : apri());
    const m = location.hash.match(/^#pagina-(\d+)$/); if (m) apri(+m[1]); else if (location.hash === "#libro") apri();
  }
  window.Libro = { init, apri, chiudi };
})();
