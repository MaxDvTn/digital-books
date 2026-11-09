// Scheda «Il moto equabile» (Discorsi, Giornata Terza): due mobili e Teorema I.
// Dipende da equabile_modello.js (window.Equabile) e dai dati window.DIM_ME_P1 (dimostrazioni/ME-P1.json).
(function () {
  const E = window.Equabile, D = window.DIM_ME_P1;
  const $ = (s, e = document) => e.querySelector(s);
  const NS = "http://www.w3.org/2000/svg";
  if (!E || !D || !$("#equabile")) return;
  function el(tag, attr, par) { const e = document.createElementNS(NS, tag); for (const k in attr) e.setAttribute(k, attr[k]); if (par) par.appendChild(e); return e; }
  function txt(par, x, y, s, attr) { const t = el("text", Object.assign({ x, y }, attr || {}), par); t.textContent = s; return t; }
  const fmt = (x, d = 2) => (Math.round(x * 10 ** d) / 10 ** d).toLocaleString("it-IT");
  const SEGNO = { 1: ">", 0: "=", "-1": "<" };
  const PAROLA = { 1: "maggiore", 0: "eguale", "-1": "minore" };
  const INK = "#22201c", ATT = "var(--attivo)", RUB = "var(--rubrica)", DATO = "#6b6458", OCRA = "#8a5a00";
  const ridotto = matchMedia("(prefers-reduced-motion: reduce)").matches;
  // sul telefono la figura (640 unità) è larga ~330 px: le scritte si ingrandiscono per restare leggibili
  function fattore(svg) { const w = svg.getBoundingClientRect().width || 640; return Math.min(1.9, Math.max(1, 640 / w)); }
  function ingrandisci(svg, f) { if (f <= 1) return; svg.querySelectorAll("text").forEach(t => { const z = +t.getAttribute("font-size"); if (z) t.setAttribute("font-size", (z * f).toFixed(1)); }); }

  /* ---------------------------------------------------------- 1. due mobili */
  const due = { t: 0, play: false, parti: 1, raf: 0, ultimo: 0 };
  const X0 = 70, X1 = 610, BATT = 4, PX = (X1 - X0) / BATT;
  function disegnaDue() {
    const svg = $("#eqDue"); svg.innerHTML = ""; const f = fattore(svg), stretto = f > 1.3;
    const righe = [["equabile", 60, ATT], ["a scatti", 114, OCRA]];
    for (let b = 0; b <= BATT; b++) {
      const x = X0 + b * PX;
      el("line", { x1: x, y1: 26, x2: x, y2: 126, stroke: "#d9d1c3", "stroke-dasharray": "3 3" }, svg);
      txt(svg, x, 17, b === 0 ? "0" : b + (b === 1 && !stretto ? " battuta" : ""), { "text-anchor": "middle", "font-size": 11, fill: DATO, "font-family": "Inter,sans-serif" });
    }
    for (const [nome, y, col] of righe) {
      txt(svg, stretto ? X0 : 6, stretto ? y - 11 : y + 4, nome, { "font-size": 12, fill: col, "font-family": "Inter,sans-serif", "font-weight": 600 });
      el("line", { x1: X0, y1: y, x2: X1, y2: y, stroke: INK, "stroke-width": 1.5 }, svg);
      for (let b = 0; b <= BATT; b++) el("line", { x1: X0 + b * PX, y1: y - 5, x2: X0 + b * PX, y2: y + 5, stroke: INK }, svg);
      const tipo = nome === "equabile" ? "equabile" : "scatti";
      const x = X0 + E.posizione(tipo, due.t) * PX;
      el("circle", { cx: x, cy: y, r: 7, fill: col, stroke: "#fff", "stroke-width": 1.5 }, svg);
    }
    if (!stretto) txt(svg, X1, 140, "un braccio per tacca", { "text-anchor": "end", "font-size": 10, fill: DATO, "font-family": "Inter,sans-serif" });
    // barre: spazio percorso in ogni parte eguale di tempo
    const P = due.parti, w = PX / P, hMax = 34;
    righe.forEach(([nome, , col], r) => {
      const tipo = nome === "equabile" ? "equabile" : "scatti";
      const sp = E.spaziInParti(tipo, BATT, P), base = 190 + r * 50;
      txt(svg, X0, 147, r === 0 ? "spazio percorso in ogni parte eguale di tempo" : "", { "font-size": 10, fill: DATO, "font-family": "Inter,sans-serif" });
      sp.forEach((s, i) => {
        const fine = (i + 1) / P, h = s * P * hMax * 0.62; // altezza ∝ spazio/(durata della parte)·durata: si confrontano spazi in tempi eguali
        const fatta = fine <= due.t + 1e-9;
        el("rect", { x: X0 + i * w + 1.5, y: base - h, width: Math.max(1, w - 3), height: h, fill: fatta ? col : "none", "fill-opacity": .75, stroke: fatta ? "none" : "#c9bfae", "stroke-dasharray": fatta ? "" : "2 2" }, svg);
      });
      el("line", { x1: X0, y1: base, x2: X1, y2: base, stroke: "#bdb3a2" }, svg);
    });
    ingrandisci(svg, f);
    // cifre
    const P1 = E.spaziInParti("equabile", 1, P), P2 = E.spaziInParti("scatti", 1, P);
    const eg2 = E.tuttiEguali(E.spaziInParti("scatti", BATT, P));
    $("#eqDueCifre").innerHTML =
      `<div>In ogni battuta<b>1 braccio tutti e due</b></div>` +
      `<div>Equabile, in ogni ${P === 1 ? "battuta" : "1/" + P + " di battuta"}<b>${P1.map(x => fmt(x)).join(" · ")} braccia</b></div>` +
      `<div>A scatti, in ogni ${P === 1 ? "battuta" : "1/" + P + " di battuta"}<b>${P2.map(x => fmt(x)).join(" · ")} braccia</b></div>` +
      `<div>Spazi eguali in tempi eguali «comunque presi»?<b>equabile: sì · a scatti: ${eg2 ? "sì, per ora" : "no"}</b></div>`;
    $("#eqPartiV").textContent = P === 1 ? "1 parte" : P + " parti";
  }
  function giroDue(ts) {
    if (!due.play) return;
    const dt = due.ultimo ? (ts - due.ultimo) / 1000 : 0; due.ultimo = ts;
    due.t = Math.min(BATT, due.t + dt * 0.5);
    disegnaDue();
    if (due.t >= BATT) { fermaDue(); return; }
    due.raf = requestAnimationFrame(giroDue);
  }
  function fermaDue() { due.play = false; due.ultimo = 0; cancelAnimationFrame(due.raf); $("#eqPlay").setAttribute("aria-pressed", "false"); $("#eqPlay").textContent = "▶ Fai partire"; }
  $("#eqPlay").addEventListener("click", () => {
    if (due.play) { fermaDue(); return; }
    if (due.t >= BATT) due.t = 0;
    if (ridotto) { due.t = BATT; disegnaDue(); return; }
    due.play = true; $("#eqPlay").setAttribute("aria-pressed", "true"); $("#eqPlay").textContent = "❚❚ Ferma"; due.raf = requestAnimationFrame(giroDue);
  });
  $("#eqDaCapo").addEventListener("click", () => { fermaDue(); due.t = 0; disegnaDue(); });
  $("#eqParti").addEventListener("input", e => { due.parti = +e.target.value; disegnaDue(); });

  /* ---------------------------------------------------------- 2. Teorema I */
  const S = { passo: 0, AB: 2, BC: 3, v: 1, m: 3, n: 2, rad2: false, contro: false, latino: false, corsa: null, raf: 0 };
  const K_CONTRO = 0.8;
  const N_GRIGLIA = 12;
  let giaVisti = new Set();

  function valori() {
    const AB = S.rad2 ? Math.SQRT2 * S.BC : S.AB;
    const k = S.contro ? K_CONTRO : 1;
    return { AB, BC: S.BC, v: S.v, m: S.m, n: S.n, k, c: E.costruzione(AB, S.BC, S.v, S.m, S.n, k) };
  }
  function vede(nome) { return D.passi[S.passo].mostra.includes(nome); }

  function disegnaFig() {
    const svg = $("#eqFig"); svg.innerHTML = ""; const f = fattore(svg), stretto = f > 1.3;
    const V = valori(), c = V.c;
    const sx = vede("sx"), dx = vede("dx");
    // posizioni in unità (G e I nell'origine); la scala usa solo gli oggetti già introdotti nel passo
    const u = { G: 0, A: c.GB - V.AB, B: c.GB, C: c.GB + V.BC, H: c.GB + c.BH, I: 0, D: c.IE - c.DE, E: c.IE, F: c.IE + c.EF, K: c.IE + c.EK };
    const uMin = sx ? 0 : Math.min(u.A, u.D), uMax = dx ? Math.max(u.H, u.K) : Math.max(u.C, u.F);
    const M = 58, W = 640 - M - 26, sc = W / (uMax - uMin), X = (q) => M + (q - uMin) * sc;
    const yT = 72, yS = 162;
    const xG = X(u.G), xA = X(u.A), xB = X(u.B), xC = X(u.C), xH = X(u.H), xI = X(u.I), xD = X(u.D), xE = X(u.E), xF = X(u.F), xK = X(u.K);
    const nuovo = (nome) => { const n = !giaVisti.has(nome); giaVisti.add(nome); return n ? " nuovo" : ""; };
    // linee di base
    const lineaS = [sx ? xG : xA, dx ? xH : xC], lineaT = [sx ? xI : xD, dx ? xK : xF];
    el("line", { x1: lineaT[0], y1: yT, x2: lineaT[1], y2: yT, stroke: INK, "stroke-width": 1.6 }, svg);
    el("line", { x1: lineaS[0], y1: yS, x2: lineaS[1], y2: yS, stroke: INK, "stroke-width": 1.6 }, svg);
    txt(svg, 4, yT + 24, "tempi", { "font-size": 10, fill: DATO, "font-family": "Inter,sans-serif" });
    txt(svg, 4, yS - 12, "spazi", { "font-size": 10, fill: DATO, "font-family": "Inter,sans-serif" });
    const tacca = (x, y, h, col, w) => el("line", { x1: x, y1: y - h, x2: x, y2: y + h, stroke: col || INK, "stroke-width": w || 1.3 }, svg);
    const lettera = (x, y, s, col, cls) => { const m = s.length * 4.6 * f + 2; x = Math.max(m, Math.min(640 - m, x));
      return txt(svg, x, y, s, { "text-anchor": "middle", "font-size": 17, fill: col || INK, "font-family": "'EB Garamond',Georgia,serif", class: cls || "" }); };
    // copie a sinistra e a destra (tacche come nell'incisione)
    if (sx) {
      const g = el("g", { class: nuovo("sx").trim() }, svg);
      for (let i = 1; i < V.m; i++) { tacca.call(null, xB - i * V.AB * sc, yS, 5); tacca(xE - i * c.DE * sc, yT, 5); }
      if (V.m > 1) { g.appendChild(lettera(xG - 2, yS + 22, "G")); g.appendChild(lettera(xI - 2, yT - 12, "I")); }
      tacca(xG, yS, 7); tacca(xI, yT, 7);
    }
    if (dx) {
      const g = el("g", { class: nuovo("dx").trim() }, svg);
      for (let i = 1; i < V.n; i++) { tacca(xB + i * V.BC * sc, yS, 5); tacca(xE + i * c.EF * sc, yT, 5); }
      if (V.n > 1) { g.appendChild(lettera(xH + 2, yS + 22, "H")); g.appendChild(lettera(xK + 2, yT - 12, "K")); }
      tacca(xH, yS, 7); tacca(xK, yT, 7);
    }
    // segmenti dati (ipotesi)
    el("line", { x1: xA, y1: yS, x2: xB, y2: yS, stroke: ATT, "stroke-width": 4 }, svg);
    el("line", { x1: xB, y1: yS, x2: xC, y2: yS, stroke: OCRA, "stroke-width": 4 }, svg);
    el("line", { x1: xD, y1: yT, x2: xE, y2: yT, stroke: ATT, "stroke-width": 4 }, svg);
    el("line", { x1: xE, y1: yT, x2: xF, y2: yT, stroke: OCRA, "stroke-width": 4, "stroke-dasharray": V.k < 1 ? "6 3" : "" }, svg);
    for (const [x, y] of [[xA, yS], [xB, yS], [xC, yS], [xD, yT], [xE, yT], [xF, yT]]) tacca(x, y, 9, INK, 1.6);
    const uno = (s, altra, k) => sx && k === 1 && (altra === "G" || altra === "I") || dx && k === 1 && (altra === "H" || altra === "K") ? s + " = " + altra : s;
    lettera(xA, yS + 24, uno("A", "G", V.m)); lettera(xB, yS + 24, "B"); lettera(xC, yS + 24, uno("C", "H", V.n));
    lettera(xD, yT - 14, uno("D", "I", V.m)); lettera(xE, yT - 14, "E"); lettera(xF, yT - 14, uno("F", "K", V.n));
    // coppie BG–EI e BH–EK
    if (vede("coppie")) {
      const g = el("g", { class: nuovo("coppie").trim() }, svg);
      const graffa = (x1, x2, y, su, col, et) => {
        const d = su ? -1 : 1, h = 9;
        g.appendChild(el("path", { d: `M${x1},${y} v${d * h} H${x2} v${-d * h}`, fill: "none", stroke: col, "stroke-width": 1.6 }));
        const meta = et.length * 3.3 * f;   // mezza larghezza stimata dell'etichetta (Inter 11, ingrandita)
        const cx = Math.max(4 + meta, Math.min(636 - meta, (x1 + x2) / 2));
        g.appendChild(txt(g, cx, y + d * (h + (su ? 5 : 13)), et, { "text-anchor": "middle", "font-size": 11, fill: col, "font-family": "Inter,sans-serif" }));
      };
      const v = (k) => stretto ? "·" : (k === 1 ? " volta " : " volte ");
      const da = (k, x, y) => k === 1 ? y : x;
      graffa(xI, xE, yT - 30, true, ATT, `${da(V.m, "EI", "ED")} = ${V.m}${v(V.m)}DE`);
      graffa(xE, xK, yT - 30, true, OCRA, `${da(V.n, "EK", "EF")} = ${V.n}${v(V.n)}EF`);
      graffa(xG, xB, yS + 34, false, ATT, `${da(V.m, "BG", "BA")} = ${V.m}${v(V.m)}AB`);
      graffa(xB, xH, yS + 34, false, OCRA, `${da(V.n, "BH", "BC")} = ${V.n}${v(V.n)}BC`);
    }
    if (vede("tesi") && !vede("sx")) {
      const g = el("g", { class: nuovo("tesi").trim() }, svg);
      g.appendChild(txt(g, 320, 118, "AB : BC  =  DE : EF ?", { "text-anchor": "middle", "font-size": 18, fill: RUB, "font-family": "'EB Garamond',Georgia,serif" }));
    }
    // avviso: un segmento troppo corto rispetto agli altri fa sovrapporre le lettere
    const corto = Math.min(V.AB, V.BC, c.DE, c.EF) * sc < 14 * f;
    if (corto) txt(svg, 320, 246, stretto ? "Segmento molto corto: lettere sovrapposte" : "Attenzione: un segmento è molto corto rispetto agli altri e alcune lettere si sovrappongono.", { "text-anchor": "middle", "font-size": 10, fill: RUB, "font-family": "Inter,sans-serif" });
    // mobile che corre: punto sugli spazi, indice sui tempi
    if (S.corsa) {
      const s = S.corsa.s, tt = S.corsa.t;
      el("circle", { cx: X(s), cy: yS, r: 7, fill: RUB, stroke: "#fff", "stroke-width": 1.5 }, svg);
      el("path", { d: `M${X(tt)},${yT + 4} l-6,12 h12 z`, fill: RUB }, svg);
    }
    ingrandisci(svg, f);
    svg.setAttribute("aria-label", descrizione(V));
  }
  function descrizione(V) {
    const c = V.c, p = D.passi[S.passo];
    let s = `Passo ${S.passo + 1}. Sotto, la linea degli spazi con A, B, C; sopra, la linea dei tempi con D, E, F. AB misura ${fmt(V.AB)} braccia, BC ${fmt(V.BC)}; DE ${fmt(c.DE)} battute, EF ${fmt(c.EF)}.`;
    if (p.mostra.includes("sx")) s += ` A sinistra AB è ripetuto ${V.m} volte fino a G e DE fino a I.`;
    if (p.mostra.includes("dx")) s += ` A destra BC è ripetuto ${V.n} volte fino a H e EF fino a K.`;
    if (p.mostra.includes("confronto")) s += ` GB è ${PAROLA[c.spazi]} di BH e IE è ${PAROLA[c.tempi]} di EK.`;
    return s;
  }
  function disegnaCifre() {
    const V = valori(), c = V.c;
    let h = `<div>AB · BC<b>${S.rad2 ? "√2 · BC" : fmt(V.AB)} · ${fmt(V.BC)} braccia</b></div><div>DE · EF<b>${fmt(c.DE)} · ${fmt(c.EF)} battute</b></div>`;
    if (vede("confronto")) {
      const ok = c.spazi === c.tempi;
      h += `<div>Spazi<b>GB ${SEGNO[c.spazi]} BH</b></div><div>Tempi<b>IE ${SEGNO[c.tempi]} EK</b></div>`;
      h += `<div>Stesso esito?<b style="color:${ok ? "inherit" : "var(--rubrica)"}">${ok ? "sì" : "no ≠"}</b></div>`;
    }
    $("#eqCifre").innerHTML = h;
    for (const [id, val, u] of [["eqAB", S.rad2 ? null : S.AB, " br."], ["eqBC", S.BC, " br."], ["eqV", S.v, " br./batt."], ["eqM", S.m, ""], ["eqN", S.n, ""]])
      $("#" + id + "v").textContent = val === null ? "√2·BC" : fmt(val) + u;
  }
  function disegnaGriglia() {
    const box = $("#eqGrigliaBox"); box.hidden = !vede("griglia"); if (box.hidden) return;
    const V = valori(), G = E.griglia(V.AB, V.BC, V.v, N_GRIGLIA, V.k);
    const svg = $("#eqGrid"); svg.innerHTML = "";
    const M = 34, L = (400 - M - 4) / N_GRIGLIA;
    txt(svg, M + (400 - M) / 2, 12, "n →", { "text-anchor": "middle", "font-size": 11, fill: DATO, "font-family": "Inter,sans-serif" });
    txt(svg, 8, M + (400 - M) / 2, "m ↓", { "font-size": 11, fill: DATO, "font-family": "Inter,sans-serif" });
    const fondo = { 1: "#dbe6f3", 0: "#ffffff", "-1": "#f1e3c8" };
    for (const q of G.celle) {
      const x = M + (q.n - 1) * L, y = M + (q.m - 1) * L;
      el("path", { d: `M${x},${y} h${L} L${x},${y + L} z`, fill: fondo[q.spazi] }, svg);
      el("path", { d: `M${x + L},${y} v${L} h${-L} z`, fill: fondo[q.tempi] }, svg);
      txt(svg, x + L * .3, y + L * .44, SEGNO[q.spazi], { "text-anchor": "middle", "font-size": L * .44, fill: INK, "font-family": "Inter,sans-serif" });
      txt(svg, x + L * .72, y + L * .9, SEGNO[q.tempi], { "text-anchor": "middle", "font-size": L * .44, fill: INK, "font-family": "Inter,sans-serif" });
      el("rect", { x, y, width: L, height: L, fill: "none", stroke: q.ok ? "#d9d1c3" : RUB, "stroke-width": q.ok ? .8 : 3 }, svg);
      if (!q.ok) txt(svg, x + L * .72, y + L * .4, "≠", { "text-anchor": "middle", "font-size": L * .34, fill: RUB, "font-weight": 700, "font-family": "Inter,sans-serif" });
    }
    for (let i = 1; i <= N_GRIGLIA; i++) {
      txt(svg, M + (i - .5) * L, M - 6, i, { "text-anchor": "middle", "font-size": 12, fill: DATO, "font-family": "Inter,sans-serif" });
      txt(svg, M - 6, M + (i - .5) * L + 4, i, { "text-anchor": "end", "font-size": 12, fill: DATO, "font-family": "Inter,sans-serif" });
    }
    el("rect", { x: M + (S.n - 1) * L, y: M + (S.m - 1) * L, width: L, height: L, fill: "none", stroke: INK, "stroke-width": 2.5, "stroke-dasharray": "4 2" }, svg);
    svg.setAttribute("aria-label", `Griglia dei confronti per m e n da 1 a ${N_GRIGLIA}: ${G.discordi === 0 ? "in tutte le caselle i due confronti danno lo stesso esito" : G.discordi + " caselle discordano"}; caselle con moltiplici eguali: ${G.eguali}.`);
    const nota = G.discordi === 0
      ? `Nessuna casella discorda su ${N_GRIGLIA * N_GRIGLIA}${G.eguali ? "" : " (e nessuna ha «=»: la ragione non è tra numeri interi piccoli)"}.`
      : `${G.discordi} caselle discordano: AB : BC e DE : EF non sono la stessa ragione.`;
    $("#eqGrigliaBox .nota-ui").dataset.stato = nota;
    let s = $("#eqGrigliaStato"); if (!s) { s = document.createElement("p"); s.id = "eqGrigliaStato"; s.className = "ui nota-ui"; $("#eqGrigliaBox").appendChild(s); }
    s.textContent = nota;
  }
  function disegnaTesto() {
    const p = D.passi[S.passo];
    $("#eqNum").textContent = `Passo ${S.passo + 1} di ${D.passi.length}`;
    const it = p.frasi.map(i => D.frasi[i].it).join(" ");
    const la = p.frasi.map(i => D.frasi[i].la).join(" ");
    $("#eqTesto").innerHTML = `<span class="cit">«${it}»</span>` + (S.latino ? `<span class="latino">${la}</span>` : "") + `<span class="spieg">${p.nota}</span>`;
    $("#eqPrec").disabled = S.passo === 0; $("#eqSucc").disabled = S.passo === D.passi.length - 1;
    $("#eqCorri").hidden = !vede("coppie");
  }
  function tutto() { disegnaFig(); disegnaCifre(); disegnaGriglia(); disegnaTesto(); }
  function vai(i) { fermaCorsa(); S.passo = Math.max(0, Math.min(D.passi.length - 1, i)); tutto(); }

  // corsa del mobile da G a H, con l'indice del tempo da I a K
  function fermaCorsa() { cancelAnimationFrame(S.raf); S.corsa = null; $("#eqCorri").setAttribute("aria-pressed", "false"); $("#eqCorri").textContent = "▶ Il mobile percorre GH"; }
  $("#eqCorri").addEventListener("click", () => {
    if (S.corsa) { fermaCorsa(); disegnaFig(); return; }
    const V = valori(), c = V.c, Ttot = c.IE + c.EK;
    const sDa = (t) => t <= c.IE ? t * V.v : c.GB + (t - c.IE) * V.v * V.k;
    $("#eqCorri").setAttribute("aria-pressed", "true"); $("#eqCorri").textContent = "❚❚ Ferma";
    if (ridotto) { S.corsa = { s: c.GB, t: c.IE }; disegnaFig(); return; }
    let t0 = 0; const dur = 5000;
    const giro = (ts) => { if (!t0) t0 = ts; const f = Math.min(1, (ts - t0) / dur), t = f * Ttot; S.corsa = { s: sDa(t), t }; disegnaFig(); if (f < 1) S.raf = requestAnimationFrame(giro); else { $("#eqCorri").setAttribute("aria-pressed", "false"); $("#eqCorri").textContent = "▶ Di nuovo"; } };
    S.raf = requestAnimationFrame(giro);
  });

  // controlli
  const cur = [["eqAB", "AB"], ["eqBC", "BC"], ["eqV", "v"], ["eqM", "m"], ["eqN", "n"]];
  for (const [id, k] of cur) $("#" + id).addEventListener("input", e => {
    fermaCorsa(); S[k] = +e.target.value;
    if (k === "AB" && S.rad2) { S.rad2 = false; $("#eqRad2").setAttribute("aria-pressed", "false"); }
    tutto();
  });
  $("#eqRad2").addEventListener("click", e => { fermaCorsa(); S.rad2 = !S.rad2; e.currentTarget.setAttribute("aria-pressed", S.rad2); tutto(); });
  $("#eqContro").addEventListener("click", e => { fermaCorsa(); S.contro = !S.contro; e.currentTarget.setAttribute("aria-pressed", S.contro); tutto(); });
  $("#eqLat").addEventListener("click", e => { S.latino = !S.latino; e.currentTarget.setAttribute("aria-pressed", S.latino); disegnaTesto(); });
  $("#eqPrec").addEventListener("click", () => vai(S.passo - 1));
  $("#eqSucc").addEventListener("click", () => vai(S.passo + 1));
  $("#eqInizio").addEventListener("click", () => { giaVisti = new Set(); vai(0); });
  $("#equabile").addEventListener("keydown", e => {
    if (e.target.matches("input")) return;
    if (e.key === "ArrowRight") { vai(S.passo + 1); e.preventDefault(); }
    if (e.key === "ArrowLeft") { vai(S.passo - 1); e.preventDefault(); }
  });
  // tocco sulla griglia: la casella più vicina
  $("#eqGrid").addEventListener("pointerdown", e => {
    const svg = e.currentTarget, r = svg.getBoundingClientRect(), k = 400 / r.width;
    const x = (e.clientX - r.left) * k, y = (e.clientY - r.top) * k, M = 34, L = (400 - M - 4) / N_GRIGLIA;
    const n = Math.max(1, Math.min(N_GRIGLIA, Math.floor((x - M) / L) + 1)), m = Math.max(1, Math.min(N_GRIGLIA, Math.floor((y - M) / L) + 1));
    S.m = m; S.n = n; $("#eqM").value = m; $("#eqN").value = n; fermaCorsa(); tutto();
  });

  $("#eqGrid").addEventListener("keydown", e => {
    const d = { ArrowRight: [0, 1], ArrowLeft: [0, -1], ArrowDown: [1, 0], ArrowUp: [-1, 0] }[e.key];
    if (!d) return; e.preventDefault(); e.stopPropagation();
    S.m = Math.max(1, Math.min(N_GRIGLIA, S.m + d[0])); S.n = Math.max(1, Math.min(N_GRIGLIA, S.n + d[1]));
    $("#eqM").value = S.m; $("#eqN").value = S.n; fermaCorsa(); tutto();
  });

  // il latino del 1638, completo
  $("#eqLatino").innerHTML = `<p class="ui nota-ui">${D.fonte_latino}</p>` +
    D.latino_preliminari.map(([t, s]) => `<p class="lat1638"><span class="sc">${t}.</span> <i>${s}</i></p>`).join("") +
    `<p class="lat1638">${D.frasi.map(f => f.la).join(" ")}</p>`;

  disegnaDue();
  tutto();
  let tr = 0; window.addEventListener("resize", () => { clearTimeout(tr); tr = setTimeout(() => { disegnaDue(); disegnaFig(); }, 150); });
})();
