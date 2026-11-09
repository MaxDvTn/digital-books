// Modello astronomico per il Sidereus interattivo.
// Unica fonte delle formule: usato dalla pagina e dagli script di verifica (node).
// Satelliti: J. Meeus, Astronomical Algorithms, 2a ed., cap. 44 (metodo a bassa precisione).
// Sole: formule a bassa precisione di Meeus, cap. 25; tramonto con h0 = -0.833°.
(function (root) {
  const D2R = Math.PI / 180, R2D = 180 / Math.PI;
  const sin = (d) => Math.sin(d * D2R), cos = (d) => Math.cos(d * D2R);

  // Giorno giuliano da data gregoriana (UT, ore decimali)
  function jd(y, m, d, h) {
    if (m <= 2) { y -= 1; m += 12; }
    const A = Math.floor(y / 100), B = 2 - A + Math.floor(A / 4);
    return Math.floor(365.25 * (y + 4716)) + Math.floor(30.6001 * (m + 1)) + d + (h || 0) / 24 + B - 1524.5;
  }

  // Posizioni apparenti dei satelliti medicei, in raggi equatoriali di Giove.
  // X > 0 verso occidente, Y > 0 verso nord (convenzione di Meeus).
  function satelliti(JD) {
    const d = JD - 2451545.0;
    const V = 172.74 + 0.00111588 * d;
    const M = 357.529 + 0.9856003 * d;
    const N = 20.020 + 0.0830853 * d + 0.329 * sin(V);
    const J = 66.115 + 0.9025179 * d - 0.329 * sin(V);
    const A = 1.915 * sin(M) + 0.020 * sin(2 * M);
    const B = 5.555 * sin(N) + 0.168 * sin(2 * N);
    const K = J + A - B;
    const R = 1.00014 - 0.01671 * cos(M) - 0.00014 * cos(2 * M);
    const r = 5.20872 - 0.25208 * cos(N) - 0.00611 * cos(2 * N);
    const Delta = Math.sqrt(r * r + R * R - 2 * r * R * cos(K));
    const psi = Math.asin(R / Delta * sin(K)) * R2D;
    const lam = 34.35 + 0.083091 * d + 0.329 * sin(V) + B;
    const DS = 3.12 * sin(lam + 42.8);
    const DE = DS - 2.22 * sin(psi) * cos(lam + 22) - 1.30 * (r - Delta) / Delta * sin(lam - 100.5);
    const t = d - Delta / 173;
    let u1 = 163.8069 + 203.4058646 * t + psi - B;
    let u2 = 358.4140 + 101.2916335 * t + psi - B;
    let u3 = 5.7176 + 50.2345180 * t + psi - B;
    let u4 = 224.8092 + 21.4879800 * t + psi - B;
    const G = 331.18 + 50.310482 * t, H = 87.45 + 21.569231 * t;
    const c1 = 0.473 * sin(2 * (u1 - u2)), c2 = 1.065 * sin(2 * (u2 - u3));
    const c3 = 0.165 * sin(G), c4 = 0.843 * sin(H);
    const r1 = 5.9057 - 0.0244 * cos(2 * (u1 - u2));
    const r2 = 9.3966 - 0.0882 * cos(2 * (u2 - u3));
    const r3 = 14.9883 - 0.0216 * cos(G);
    const r4 = 26.3627 - 0.1939 * cos(H);
    u1 += c1; u2 += c2; u3 += c3; u4 += c4;
    const s = [[r1, u1], [r2, u2], [r3, u3], [r4, u4]].map(([ri, ui]) => ({
      r: ri, u: ((ui % 360) + 360) % 360,
      X: ri * sin(ui),
      Y: -ri * cos(ui) * sin(DE),
      dietro: cos(ui) < 0, // cos u > 0: satellite dalla parte della Terra (davanti a Giove)
    }));
    // semidiametro equatoriale di Giove visto dalla Terra, in primi d'arco
    const raggioArcmin = Math.atan(71492 / (Delta * 149597870.7)) * R2D * 60;
    return { sat: s, Delta, raggioArcmin, DE };
  }

  // Tramonto del Sole (UT, ore) in una data gregoriana, a latitudine/longitudine date.
  function tramontoUT(y, m, d, lat, lonEst) {
    let tUT = 17 - lonEst / 15; // prima stima
    for (let k = 0; k < 3; k++) {
      const n = jd(y, m, d, tUT) - 2451545.0;
      const L = 280.460 + 0.9856474 * n, g = 357.528 + 0.9856003 * n;
      const lamS = L + 1.915 * sin(g) + 0.020 * sin(2 * g);
      const eps = 23.439 - 0.0000004 * n;
      const dec = Math.asin(sin(eps) * sin(lamS)) * R2D;
      const ra = Math.atan2(cos(eps) * sin(lamS), cos(lamS)) * R2D;
      let EoT = (L - ra) % 360; if (EoT > 180) EoT -= 360; if (EoT < -180) EoT += 360; // gradi
      const cosH = (sin(-0.833) - sin(lat) * sin(dec)) / (cos(lat) * cos(dec));
      const H0 = Math.acos(cosH) * R2D;
      tUT = 12 + (H0 - lonEst - EoT) / 15;
    }
    return tUT;
  }

  const PADOVA = { lat: 45.407, lon: 11.876 };

  // "a h ore di notte" = h ore dopo il tramonto (ore all'italiana).
  function jdOsservazione(y, m, d, oreDopoTramonto) {
    const ts = tramontoUT(y, m, d, PADOVA.lat, PADOVA.lon);
    return jd(y, m, d, ts + oreDopoTramonto);
  }

  const api = { jd, satelliti, tramontoUT, jdOsservazione, PADOVA };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.Astro = api;
})(this);
