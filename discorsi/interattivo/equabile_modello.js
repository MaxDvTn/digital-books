// Modello della scheda «Del moto equabile» (Discorsi, Giornata Terza, Teorema I).
// Un solo modello per la pagina e per la verifica (verifica_equabile.py lo confronta con un calcolo indipendente).
// Nessuna algebra nella scheda: i numeri servono solo a disegnare e a controllare i confronti.
(function (radice) {
  const TOLL = 1e-9;

  // confronto di due grandezze omogenee: 1 maggiore, 0 eguale, -1 minore
  function confronta(a, b) {
    const s = Math.max(Math.abs(a), Math.abs(b), 1);
    if (Math.abs(a - b) <= TOLL * s) return 0;
    return a > b ? 1 : -1;
  }

  // Ipotesi del Teorema I: lo stesso mobile, con la stessa velocità v, percorre AB e poi BC.
  // DE = tempo per AB, EF = tempo per BC. Con «controprova» il mobile su BC va più piano (fattore k < 1):
  // l'ipotesi «eadem cum velocitate» non vale più.
  function tempi(AB, BC, v, k) {
    k = k === undefined ? 1 : k;
    return { DE: AB / v, EF: BC / (v * k) };
  }

  // Costruzione di Galileo: GB = m volte AB, EI = m volte DE; BH = n volte BC, EK = n volte EF.
  function costruzione(AB, BC, v, m, n, k) {
    const t = tempi(AB, BC, v, k);
    const GB = m * AB, BH = n * BC, IE = m * t.DE, EK = n * t.EF;
    return { DE: t.DE, EF: t.EF, GB, BH, IE, EK, spazi: confronta(GB, BH), tempi: confronta(IE, EK) };
  }

  // Definizione 5 del libro V di Euclide, provata su tutte le coppie (m, n) fino a N:
  // AB : BC = DE : EF se e solo se i due confronti danno sempre lo stesso esito.
  function griglia(AB, BC, v, N, k) {
    const celle = []; let discordi = 0, eguali = 0;
    for (let m = 1; m <= N; m++) for (let n = 1; n <= N; n++) {
      const c = costruzione(AB, BC, v, m, n, k);
      const ok = c.spazi === c.tempi; if (!ok) discordi++; if (c.spazi === 0) eguali++;
      celle.push({ m, n, spazi: c.spazi, tempi: c.tempi, ok });
    }
    return { celle, discordi, eguali };
  }

  // I due mobili della «Avvertenza»: posizione (in braccia) al tempo t (in battute).
  // Equabile: 1 braccio per battuta. A scatti: 1 braccio per battuta, ma in ogni battuta
  // copre la quota «veloce» del braccio nella prima metà e il resto nella seconda.
  const VELOCE = 0.8;
  function posizione(tipo, t) {
    if (tipo === "equabile") return t;
    const k = Math.floor(t), f = t - k;
    return k + (f < 0.5 ? VELOCE * (f / 0.5) : VELOCE + (1 - VELOCE) * ((f - 0.5) / 0.5));
  }
  // spazi percorsi nelle parti eguali di tempo: battute 0..B, ciascuna divisa in «parti»
  function spaziInParti(tipo, B, parti) {
    const out = [];
    for (let i = 0; i < B * parti; i++) out.push(posizione(tipo, (i + 1) / parti) - posizione(tipo, i / parti));
    return out;
  }
  function tuttiEguali(xs) { return xs.every(x => confronta(x, xs[0]) === 0); }

  const API = { TOLL, VELOCE, confronta, tempi, costruzione, griglia, posizione, spaziInParti, tuttiEguali };
  if (typeof module !== "undefined" && module.exports) module.exports = API; else radice.Equabile = API;
})(typeof window !== "undefined" ? window : globalThis);
