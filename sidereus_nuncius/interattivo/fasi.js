// Scheda «Le fasi della Luna» — Sidereus Nuncius, figura 1.
// Una sola scena three.js (r128): la vista "dal cannocchiale" è la camera posta sulla Terra,
// la vista "nello spazio" è la stessa scena vista da fuori. Tutto è reso come un'incisione:
// inchiostro su carta, tratteggio fitto nella parte in ombra, tratti orizzontali per i mari.
(function () {
  const PI = Math.PI, D2R = PI / 180;
  const LUNAZIONE = 29.530589;
  if (!window.THREE) { window.FasiLuna = function (r) { const s = r.querySelector(".fl-scena"); if (s) s.innerHTML = '<p class="ui" style="padding:1rem">Non è stato possibile caricare la libreria grafica (three.js): controlla la connessione.</p>'; }; return; }
  const CARTA = new THREE.Color("#f3ecdb"), INCHIOSTRO = new THREE.Color("#1e1c1a");
  // Età della Luna (giorni dalla congiunzione) stimate dai cinque disegni di Galileo.
  const FIGURE = [
    { n: 1, eta: 4.5, nome: "Figura 1", nota: "«Nel quarto o quinto giorno dopo la congiunzione»: falce crescente, il confine tra luce e ombra è «ineguale, aspro e assai sinuoso»." },
    { n: 2, eta: 6.8, nome: "Figura 2", nota: "Primo quarto. Sul confine, in basso, la grande cavità rotonda «quasi nel mezzo della Luna»." },
    { n: 3, eta: 22.0, nome: "Figura 3", nota: "Ultimo quarto: ora la luce è a sinistra. La stessa cavità rotonda, illuminata dalla parte opposta." },
    { n: 4, eta: 20.6, nome: "Figura 4", nota: "Poco prima dell'ultimo quarto: il confine oltrepassa il centro e mostra un grande anello di monti." },
    { n: 5, eta: 22.1, nome: "Figura 5", nota: "Ancora l'ultimo quarto: la cavità centrale è di nuovo sul confine, «circondata da contorni più oscuri»." },
  ];

  // ---------------------------------------------------------------- superficie
  // Mappa equirettangolare: R,G = pendenza verso est e verso nord; B = albedo (mari più scuri).
  function rng(seed) { let s = seed >>> 0; return () => ((s = (s * 1664525 + 1013904223) >>> 0) / 4294967296); }
  function rumore2(W, H, seed, scala) { // value noise periodico in longitudine
    const r = rng(seed), gw = Math.ceil(W / scala), gh = Math.ceil(H / scala) + 1, g = new Float32Array(gw * gh);
    for (let i = 0; i < g.length; i++) g[i] = r();
    const out = new Float32Array(W * H);
    for (let y = 0; y < H; y++) for (let x = 0; x < W; x++) {
      const fx = x / scala, fy = y / scala, x0 = Math.floor(fx), y0 = Math.floor(fy), tx = fx - x0, ty = fy - y0;
      const sx = tx * tx * (3 - 2 * tx), sy = ty * ty * (3 - 2 * ty);
      const a = g[(y0 * gw) + (x0 % gw)], b = g[(y0 * gw) + ((x0 + 1) % gw)], c = g[((y0 + 1) * gw) + (x0 % gw)], d = g[((y0 + 1) * gw) + ((x0 + 1) % gw)];
      out[y * W + x] = (a + (b - a) * sx) + ((c + (d - c) * sx) - (a + (b - a) * sx)) * sy;
    }
    return out;
  }
  function creaMappa() {
    const W = 1024, H = 512, h = new Float32Array(W * H), alb = new Float32Array(W * H).fill(1);
    const lonOf = (x) => (x / W - 0.5) * 360, latOf = (y) => (y / H - 0.5) * 180;
    // mari (lon, lat, semiassi in gradi), da una carta moderna, semplificati
    const MARI = [[-16, 33, 18, 13], [17, 28, 10, 9], [31, 8, 12, 9], [59, 17, 7, 6], [51, -6, 8, 11], [35, -15, 5, 5],
      [-17, -20, 11, 9], [-55, 12, 19, 24], [2, 56, 30, 4.5], [-39, -24, 5, 5], [4, 13, 5, 4], [-31, 7, 8, 6], [-23, -10, 6, 5], [-60, -20, 7, 6]];
    const nm = rumore2(W, H, 7, 24), nm2 = rumore2(W, H, 11, 9);
    const mare = new Float32Array(W * H);
    for (let y = 0; y < H; y++) { const lat = latOf(y + 0.5), cl = Math.cos(lat * D2R);
      for (let x = 0; x < W; x++) { const lon = lonOf(x + 0.5); let m = 0;
        for (const [l0, b0, rl, rb] of MARI) {
          let dl = lon - l0; if (dl > 180) dl -= 360; if (dl < -180) dl += 360;
          const d = Math.hypot(dl * cl / rl, (lat - b0) / rb) + 0.35 * (nm[y * W + x] - 0.5) + 0.12 * (nm2[y * W + x] - 0.5);
          m = Math.max(m, 1 - smooth(0.85, 1.05, d));
        }
        mare[y * W + x] = m; alb[y * W + x] = 1 - 0.42 * m;
      } }
    // crateri
    const r = rng(1610);
    const stampa = (lon0, lat0, rad, prof, picco) => {
      const cl0 = Math.max(Math.cos(lat0 * D2R), 0.15), ext = rad * 1.8;
      const x0 = Math.floor((lon0 - ext / cl0) / 360 * W + W / 2), x1 = Math.ceil((lon0 + ext / cl0) / 360 * W + W / 2);
      const y0 = Math.max(0, Math.floor((lat0 - ext) / 180 * H + H / 2)), y1 = Math.min(H - 1, Math.ceil((lat0 + ext) / 180 * H + H / 2));
      for (let y = y0; y <= y1; y++) { const lat = latOf(y + 0.5), cl = Math.cos(lat * D2R);
        for (let xx = x0; xx <= x1; xx++) { const x = ((xx % W) + W) % W; const lon = lonOf(xx + 0.5);
          const s = Math.hypot((lon - lon0) * cl, lat - lat0) / rad; if (s > 1.8) continue;
          let v = s < 1 ? prof * (s * s - 1) * 0.9 : 0;
          v += prof * 0.55 * Math.exp(-(((s - 1) / 0.22) ** 2));
          if (picco) v += prof * picco * Math.exp(-((s / 0.16) ** 2));
          h[y * W + x] += v;
        } }
    };
    for (let i = 0; i < 3800; i++) {
      const lon = (r() - 0.5) * 360, lat = Math.asin(2 * r() - 1) / D2R;
      const rad = 0.3 * Math.pow(5.5 / 0.3, Math.pow(r(), 2.6));
      const x = Math.floor((lon / 360 + 0.5) * W) % W, y = Math.min(H - 1, Math.floor((lat / 180 + 0.5) * H));
      const m = mare[y * W + x]; if (r() < m * 0.85) continue; // nei mari pochi crateri
      if (Math.hypot((lon - 4) * Math.cos(lat * D2R), lat + 12) < 13) continue; // intorno alla grande cavità, pulito come nel disegno
      stampa(lon, lat, rad, 0.9 * Math.pow(rad, 0.75), rad > 3 ? 0.35 : 0);
    }
    stampa(-11, -43, 2.6, 3.0, 0.4);       // Tycho
    stampa(-20, 10, 2.8, 2.8, 0.4);        // Copernico
    stampa(-1, 5, 2.4, 2.4, 0.3); stampa(-2, -9, 3.6, 3.4, 0.2); stampa(5, -22, 2.8, 2.6, 0.2); // Tolomeo, Arzachel, ...
    // Appennini e Caucaso: catene ai bordi del Mare Imbrium
    for (let t = 0; t <= 1; t += 0.01) { const a = (-20 + 110 * t) * D2R; // arco a sud-est dell'Imbrium
      const lon = -16 + 19 * Math.cos(a) / Math.cos(33 * D2R) * 0.95, lat = 33 - 15 * Math.sin(a) * 0.98;
      stampa(lon, lat, 1.4 + 0.6 * Math.sin(t * PI), 3.2, 0); stampa(lon, lat, 0.0001, 0, 0); }
    // rugosità e appiattimento dei mari
    const n1 = rumore2(W, H, 3, 6), n2 = rumore2(W, H, 5, 2.5);
    for (let i = 0; i < W * H; i++) h[i] = h[i] * (1 - 0.7 * mare[i]) + (0.35 * n1[i] + 0.05 * n2[i]) * (1 - 0.6 * mare[i]);
    // pendenze
    const dl = 2 * PI / W, db = PI / H, gx = new Float32Array(W * H), gy = new Float32Array(W * H);
    let mx = 0;
    for (let y = 1; y < H - 1; y++) { const cl = Math.max(Math.cos(latOf(y + 0.5) * D2R), 0.08);
      for (let x = 0; x < W; x++) { const i = y * W + x;
        gx[i] = (h[y * W + (x + 1) % W] - h[y * W + (x - 1 + W) % W]) / (2 * dl * cl);
        gy[i] = (h[(y + 1) * W + x] - h[(y - 1) * W + x]) / (2 * db);
        mx = Math.max(mx, Math.abs(gx[i]), Math.abs(gy[i])); } }
    const scala = 60; // pendenze oltre questo valore saturano
    const data = new Uint8Array(W * H * 4);
    for (let i = 0; i < W * H; i++) {
      data[4 * i] = Math.round(255 * Math.min(1, Math.max(0, 0.5 + gx[i] / (2 * scala))));
      data[4 * i + 1] = Math.round(255 * Math.min(1, Math.max(0, 0.5 + gy[i] / (2 * scala))));
      data[4 * i + 2] = Math.round(255 * alb[i]); data[4 * i + 3] = 255;
    }
    const tex = new THREE.DataTexture(data, W, H, THREE.RGBAFormat);
    tex.magFilter = THREE.LinearFilter; tex.minFilter = THREE.LinearFilter; tex.wrapS = THREE.RepeatWrapping; tex.needsUpdate = true;
    return { tex, scala };
  }
  function smooth(a, b, x) { const t = Math.min(1, Math.max(0, (x - a) / (b - a))); return t * t * (3 - 2 * t); }

  // ---------------------------------------------------------------- shader "incisione"
  const VS = `
    varying vec3 vLocal; varying vec3 vWPos;
    void main(){ vLocal = normalize(position); vec4 w = modelMatrix*vec4(position,1.0); vWPos = w.xyz; gl_Position = projectionMatrix*viewMatrix*w; }`;
  const FS = `
    precision highp float;
    uniform sampler2D mappa; uniform float usaMappa; uniform float rilievo; uniform vec3 sole; uniform vec3 camPos;
    uniform mat3 rot; uniform float cinerea; uniform float px; uniform vec3 carta; uniform vec3 inchiostro; uniform float reticolo; uniform vec3 cav; uniform float cavR; uniform float usaCav;
    varying vec3 vLocal; varying vec3 vWPos;
    float hash(vec2 p){ return fract(sin(dot(p,vec2(127.1,311.7)))*43758.5453); }
    float vnoise(vec2 p){ vec2 i=floor(p), f=fract(p); f=f*f*(3.0-2.0*f);
      return mix(mix(hash(i),hash(i+vec2(1,0)),f.x), mix(hash(i+vec2(0,1)),hash(i+vec2(1,1)),f.x), f.y); }
    float tratteggio(vec2 p, float ang, float passo, float larg){
      if (larg <= 0.001) return 0.0;
      vec2 d = vec2(cos(ang), sin(ang));
      float c = (dot(p, d) + 2.4*vnoise(p*0.035 + 3.1) + 0.7*vnoise(p*0.21))/passo;
      float f = abs(fract(c) - 0.5)*2.0;
      float aa = max(fwidth(c)*2.0, 0.02);
      float tratto = 1.0 - smoothstep(larg - aa, larg + aa, f);
      // tratti interrotti e di spessore irregolare, come nel bulino
      float rottura = vnoise(vec2(dot(p, vec2(-d.y, d.x))*0.06, floor(c)*7.3));
      return tratto * smoothstep(0.03, 0.11, rottura);
    }
    void main(){
      vec3 nL = normalize(vLocal);
      float lat = asin(clamp(nL.y,-1.0,1.0)), lon = atan(nL.x, nL.z);
      vec3 est = vec3(cos(lon), 0.0, -sin(lon));
      vec3 nord = vec3(-sin(lat)*sin(lon), cos(lat), -sin(lat)*cos(lon));
      float alb = 1.0; vec3 nB = nL;
      if (usaMappa > 0.5) {
        vec4 t = texture2D(mappa, vec2(lon/6.2831853 + 0.5, lat/3.1415927 + 0.5));
        vec2 g = (t.rg - 0.5) * 2.0;
        nB = normalize(nL - rilievo*(g.x*est + g.y*nord));
        alb = t.b;
      }
      // la «cavità maggiore di tutte» (oggi Albategnius): ombra calcolata esplicitamente,
      // perché il solo rilievo per pendenze non proietta ombre
      float dentro = 0.0, luceCav = 0.0, bordoCav = 0.0;
      if (usaCav > 0.5) {
        vec3 solL = normalize(transpose(rot) * sole);
        float s = acos(clamp(dot(nL, cav), -1.0, 1.0)) / cavR;
        if (s < 1.12) {
          float a = asin(clamp(dot(cav, solL), -1.0, 1.0));          // altezza del Sole sul centro della cavità
          vec3 uH = normalize(solL - dot(solL, cav)*cav), w = cross(cav, uH);
          vec3 dd = nL - cav; float x = dot(dd, uH)/sin(cavR), y = dot(dd, w)/sin(cavR);
          float prof = 0.32;                                          // profondità / raggio (esagerata, come nel disegno)
          float corda = sqrt(max(1.0 - y*y, 0.0));
          if (s < 1.0) {
            dentro = 1.0;
            float lungOmbra = a > 0.0 ? prof / max(tan(a), 1e-3) : 1e3;
            float illuminato = step(lungOmbra, corda - x);            // fondo fuori dall'ombra del bordo verso il Sole
            float parete = step(0.68, s) * step(x, -0.2) * step(-0.18, a); // parete opposta al Sole: prende luce radente
            luceCav = max(illuminato * step(-0.02, a), parete);
          }
          bordoCav = 1.0 - smoothstep(0.0, 0.05, abs(s - 1.0));
        }
      }
      vec3 nW = normalize(rot*nB), nG = normalize(rot*nL);
      if (dentro > 0.5) nW = nG;
      float diff = dot(nW, sole), geo = dot(nG, sole);
      if (dentro > 0.5) diff = luceCav > 0.5 ? max(diff, 0.3) : -0.2;
      // toni: 0 = carta, 1 = inchiostro pieno
      float luce = smoothstep(-0.02, 0.22, diff);          // dove il Sole è alto la carta resta pulita
      float tOmbra = 1.0 - luce;
      float tMare = (1.0 - alb) * 1.25 * luce;              // i mari, grigi
      float ombraGeo = smoothstep(0.02, -0.04, geo);        // emisfero non illuminato
      float cin = cinerea * ombraGeo;                       // luce cinerea: il tratteggio si dirada un poco
      vec2 p = gl_FragCoord.xy / px;
      float ink = 0.0;
      ink = max(ink, tratteggio(p, 0.42, 3.0, tOmbra*(0.93 - 0.3*cin)));
      ink = max(ink, tratteggio(p + vec2(1.3, 0.0), 1.5708, 3.0, clamp(tMare,0.0,0.6)*0.55*(1.0 - tOmbra)));
      vec2 cell = floor(p/1.8);
      float rilievo2 = clamp((1.0 - smoothstep(0.0, 0.5, diff)) * step(0.0, diff) * 0.9, 0.0, 1.0);
      if (hash(cell) < rilievo2*0.22 + tMare*0.08) ink = max(ink, 0.9);
      ink = max(ink, bordoCav * 0.95 * max(luceCav, smoothstep(-0.12, -0.02, geo)) * (1.0 - 0.85*smoothstep(0.35, 0.8, geo))); // con il Sole alto il contorno quasi scompare, come dice Galileo
      if (reticolo > 0.5) { // meridiani e paralleli della Terra, come nei globi a stampa
        float gl = min(abs(fract(lon/0.5235988+0.5)-0.5), abs(fract(lat/0.5235988+0.5)-0.5));
        if (gl < 0.035) ink = max(ink, 0.85);
      }
      vec3 v = normalize(camPos - vWPos);
      float bordo = dot(nG, v); float aab = fwidth(bordo)*1.5;
      ink = max(ink, 1.0 - smoothstep(0.035, 0.035 + aab, bordo)); // contorno
      gl_FragColor = vec4(mix(carta, inchiostro, ink), 1.0);
    }`;

  function materiale(mappa, opz) {
    return new THREE.ShaderMaterial({
      vertexShader: VS, fragmentShader: FS, extensions: { derivatives: true },
      uniforms: {
        mappa: { value: mappa }, usaMappa: { value: mappa ? 1 : 0 }, rilievo: { value: opz.rilievo || 0 },
        sole: { value: new THREE.Vector3(1, 0, 0) }, camPos: { value: new THREE.Vector3() }, rot: { value: new THREE.Matrix3() },
        cinerea: { value: 0 }, cav: { value: new THREE.Vector3() }, cavR: { value: 0.13 }, usaCav: { value: opz.cavita ? 1 : 0 }, px: { value: 1 }, carta: { value: CARTA }, inchiostro: { value: INCHIOSTRO }, reticolo: { value: opz.reticolo ? 1 : 0 },
      },
    });
  }

  // Sole disegnato come nelle stampe del Seicento: disco con raggi dritti e ondulati
  function spriteSole() {
    const c = document.createElement("canvas"); c.width = c.height = 512; const g = c.getContext("2d");
    g.translate(256, 256); g.strokeStyle = "#1e1c1a"; g.fillStyle = "#f3ecdb"; g.lineWidth = 4;
    for (let k = 0; k < 32; k++) { g.save(); g.rotate(k * PI / 16); g.beginPath();
      if (k % 2) { g.moveTo(0, -112); g.lineTo(0, -230); }
      else { g.moveTo(0, -112); for (let s = 0; s <= 1; s += 0.05) g.lineTo(14 * Math.sin(s * PI * 3), -112 - 110 * s); }
      g.stroke(); g.restore(); }
    g.beginPath(); g.arc(0, 0, 100, 0, 2 * PI); g.fill(); g.lineWidth = 6; g.stroke();
    g.lineWidth = 1.6; for (let y = -96; y < 96; y += 7) { const w = Math.sqrt(96 * 96 - y * y); if (y > 10) { g.beginPath(); g.moveTo(-w, y); g.lineTo(w, y); g.stroke(); } }
    const t = new THREE.CanvasTexture(c); return new THREE.Sprite(new THREE.SpriteMaterial({ map: t, transparent: true }));
  }

  // ---------------------------------------------------------------- scheda
  let MAPPA = null;
  function mappa() { return MAPPA || (MAPPA = creaMappa()); }
  function centroCavita(mat) { const lo = 4 * D2R, la = -12 * D2R; mat.uniforms.cav.value.set(Math.cos(la) * Math.sin(lo), Math.sin(la), Math.cos(la) * Math.cos(lo)); }

  // Fotogrammi di una lunazione vista dal cannocchiale, per l'animazione in loop del libro.
  // Un solo contesto WebGL temporaneo: i fotogrammi finiscono in un'unica tela 2D e il contesto si libera.
  window.FasiFotogrammi = function (n, size) {
    const cv = document.createElement("canvas");
    let r; try { r = new THREE.WebGLRenderer({ canvas: cv, antialias: true }); } catch (e) { return null; }
    r.setPixelRatio(1); r.setSize(size, size, false);
    const sc = new THREE.Scene(); sc.background = new THREE.Color("#fbf8f2");
    const mat = materiale(mappa().tex, { rilievo: 0.55, cavita: true }); centroCavita(mat);
    mat.uniforms.carta.value = new THREE.Color("#fbf8f2");
    const R_L = 0.55, ORB = 10;
    const luna = new THREE.Mesh(new THREE.SphereGeometry(R_L, 128, 96), mat); sc.add(luna);
    const cam = new THREE.PerspectiveCamera(5, 1, 0.05, 100);
    const cols = 12, rows = Math.ceil(n / cols);
    const sprite = document.createElement("canvas"); sprite.width = cols * size; sprite.height = rows * size;
    const g = sprite.getContext("2d");
    const out = { sprite, n, size, cols, pronti: 0 };
    // genera i fotogrammi a piccoli gruppi, per non bloccare la pagina; ritorna true quando ha finito
    out.avanza = function (ms) {
      const t = performance.now();
      while (out.pronti < n && performance.now() - t < ms) {
        const k = out.pronti, eta = k / n * LUNAZIONE, a = 2 * PI * eta / LUNAZIONE;
        const L = new THREE.Vector3(ORB * Math.cos(a), 0, -ORB * Math.sin(a));
        luna.position.copy(L); luna.lookAt(0, 0, 0); luna.updateMatrixWorld();
        mat.uniforms.rot.value.setFromMatrix4(luna.matrixWorld);
        mat.uniforms.cinerea.value = 0.5 * (1 + Math.cos(a));
        const pos = L.clone().normalize().multiplyScalar(1.02), dist = pos.distanceTo(L);
        cam.position.copy(pos); cam.fov = 2 * Math.atan(R_L * 1.06 / dist) / D2R; cam.up.set(0, 1, 0); cam.lookAt(L); cam.updateProjectionMatrix();
        mat.uniforms.camPos.value.copy(pos); mat.uniforms.px.value = size / 300;
        r.render(sc, cam);
        g.drawImage(cv, (k % cols) * size, Math.floor(k / cols) * size);
        out.pronti++;
      }
      if (out.pronti >= n && r) { r.dispose(); try { r.forceContextLoss(); } catch (e) { } r = null; }
      return out.pronti >= n;
    };
    return out;
  };

  window.FasiLuna = function (radice, immaginiGalileo) {
    if (!window.THREE) { radice.querySelector('.fl-scena').innerHTML = '<p class="ui" style="padding:1rem">Non è stato possibile caricare la libreria grafica (three.js): controlla la connessione.</p>'; return; }
    const tela = radice.querySelector(".fl-tela"), wrap = radice.querySelector(".fl-scena");
    let renderer;
    try { renderer = new THREE.WebGLRenderer({ canvas: tela, antialias: true }); }
    catch (e) { wrap.innerHTML = '<p class="ui" style="padding:1rem">Il tuo browser non supporta WebGL: la simulazione non si può mostrare.</p>'; return; }
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    const scena = new THREE.Scene(); scena.background = CARTA;
    const camera = new THREE.PerspectiveCamera(5, 1, 0.05, 400);
    const { tex } = mappa();

    const R_T = 1, R_L = 0.55, ORB = 10, SOLE_X = 22;
    const matL = materiale(tex, { rilievo: 0.55, cavita: true }), matT = materiale(null, { reticolo: true });
    const luna = new THREE.Mesh(new THREE.SphereGeometry(R_L, 128, 96), matL); scena.add(luna);
    centroCavita(matL);
    const terra = new THREE.Mesh(new THREE.SphereGeometry(R_T, 64, 48), matT); scena.add(terra);
    const sole = spriteSole(); sole.position.set(SOLE_X, 0, 0); sole.scale.set(6, 6, 1); scena.add(sole);
    // orbita e raggi paralleli del Sole
    const orbPts = []; for (let k = 0; k <= 180; k++) { const a = k / 180 * 2 * PI; orbPts.push(new THREE.Vector3(ORB * Math.cos(a), 0, -ORB * Math.sin(a))); }
    const orbita = new THREE.Line(new THREE.BufferGeometry().setFromPoints(orbPts), new THREE.LineDashedMaterial({ color: INCHIOSTRO, dashSize: 0.35, gapSize: 0.25 }));
    orbita.computeLineDistances(); scena.add(orbita);
    const raggi = new THREE.Group();
    for (let z = -12; z <= 12; z += 4) { const g = new THREE.BufferGeometry().setFromPoints([new THREE.Vector3(SOLE_X - 4, 0, z * 0.6), new THREE.Vector3(-14, 0, z * 0.6)]);
      const l = new THREE.Line(g, new THREE.LineDashedMaterial({ color: "#b08a2e", dashSize: 0.6, gapSize: 0.5 })); l.computeLineDistances(); raggi.add(l); }
    scena.add(raggi);
    // freccia di direzione del moto
    const etich = {}; ["Sole", "Terra", "Luna"].forEach(n => { const d = document.createElement("div"); d.className = "fl-etichetta"; d.textContent = n; wrap.appendChild(d); etich[n] = d; });
    etich["Sole"].textContent = "Sole";

    let controlli = null;
    if (THREE.OrbitControls) { controlli = new THREE.OrbitControls(camera, tela); controlli.enabled = false; controlli.enablePan = false; controlli.minDistance = 6; controlli.maxDistance = 60; }

    // stato
    let scalaL = 1, eta = 4.5, play = false, vista = 0, verso = 0, tAnim = 1, cinereaOn = true, ultimo = performance.now();
    const posSpazio = new THREE.Vector3(-4, 19, 27), bersSpazio = new THREE.Vector3(6, 0, 0); let fovSpazio = 40;
    let daPos = new THREE.Vector3(), daBers = new THREE.Vector3(), daFov = 5;

    function angolo() { return 2 * PI * eta / LUNAZIONE; } // 0 = luna nuova (Luna tra Terra e Sole)
    function posLuna() { const a = angolo(); return new THREE.Vector3(ORB * Math.cos(a), 0, -ORB * Math.sin(a)); }
    function vistaTerra() {
      const L = posLuna(), d = L.clone().normalize();
      const pos = d.clone().multiplyScalar(R_T * 1.02);
      const dist = pos.distanceTo(L); const fov = 2 * Math.atan(R_L * scalaL * 1.12 / dist) / D2R;
      return { pos, bers: L, fov };
    }
    function faseNome(e) {
      const f = e / LUNAZIONE;
      if (f < 0.03 || f > 0.97) return "luna nuova";
      if (f < 0.22) return "falce crescente"; if (f < 0.28) return "primo quarto"; if (f < 0.47) return "gibbosa crescente";
      if (f < 0.53) return "luna piena"; if (f < 0.72) return "gibbosa calante"; if (f < 0.78) return "ultimo quarto"; return "falce calante";
    }
    function ridimensiona() {
      const w = wrap.clientWidth, h = w;
      renderer.setSize(w, h, false); tela.style.width = w + "px"; tela.style.height = h + "px";
      camera.aspect = w / h; camera.updateProjectionMatrix();
      const stretto = w / h < 1.2; fovSpazio = stretto ? 50 : 40;
      posSpazio.set(-4, 19, 27).normalize().multiplyScalar(stretto ? 40 : 33).add(bersSpazio);
    }
    window.addEventListener("resize", ridimensiona); ridimensiona();

    function aggiornaUniform(cam) {
      const pr = renderer.getPixelRatio();
      [matL, matT].forEach(m => { m.uniforms.camPos.value.copy(cam.position); m.uniforms.px.value = pr; });
    }
    const v3 = new THREE.Vector3();
    function posiziona(mesh, p) { mesh.position.copy(p); }
    function disegna(ora) {
      const dt = Math.min(0.05, (ora - ultimo) / 1000); ultimo = ora;
      if (play) { eta = (eta + dt * 2.2) % LUNAZIONE; radice.querySelector(".fl-eta").value = eta; aggiornaTesto(); }
      const L = posLuna(); posiziona(luna, L); luna.lookAt(0, 0, 0); // la Luna rivolge sempre la stessa faccia alla Terra
      luna.updateMatrixWorld(); terra.updateMatrixWorld();
      matL.uniforms.rot.value.setFromMatrix4(luna.matrixWorld);
      matT.uniforms.rot.value.setFromMatrix4(terra.matrixWorld);
      matL.uniforms.cinerea.value = cinereaOn ? 0.5 * (1 + Math.cos(angolo())) : 0;
      // camera
      const vt = vistaTerra();
      if (tAnim < 1) tAnim = Math.min(1, tAnim + dt / 2.6);
      const e = tAnim * tAnim * (3 - 2 * tAnim);
      if (verso === 1) { // verso lo spazio
        camera.position.lerpVectors(daPos, posSpazio, e); v3.lerpVectors(daBers, bersSpazio, e); camera.fov = daFov + (fovSpazio - daFov) * e;
        camera.up.set(0, 1, 0); camera.lookAt(v3);
        if (tAnim === 1) { verso = 0; vista = 1; if (controlli) { controlli.target.copy(bersSpazio); controlli.enabled = true; controlli.update(); } }
      } else if (verso === -1) {
        camera.position.lerpVectors(daPos, vt.pos, e); v3.lerpVectors(daBers, vt.bers, e); camera.fov = daFov + (vt.fov - daFov) * e;
        camera.up.set(0, 1, 0); camera.lookAt(v3);
        if (tAnim === 1) { verso = 0; vista = 0; }
      } else if (vista === 0) { camera.position.copy(vt.pos); camera.fov = vt.fov; camera.up.set(0, 1, 0); camera.lookAt(vt.bers); }
      else if (controlli) controlli.update();
      camera.updateProjectionMatrix();
      const fuori = vista === 1 || verso !== 0;
      scalaL = 1 + 1.2 * (vista === 1 ? 1 : verso === 1 ? e : verso === -1 ? 1 - e : 0); // nello spazio la Luna è ingrandita per vederne la fase
      luna.scale.setScalar(scalaL);
      terra.visible = fuori; orbita.visible = fuori; sole.visible = fuori; raggi.visible = fuori;
      aggiornaUniform(camera);
      const w = renderer.domElement.width / renderer.getPixelRatio(), h = renderer.domElement.height / renderer.getPixelRatio();
      renderer.setScissorTest(false); renderer.setViewport(0, 0, w, h); renderer.render(scena, camera);
      // riquadro: la Luna vista dalla Terra
      const ins = radice.querySelector(".fl-riquadro");
      if (fuori && tAnim > 0.6) {
        const s = Math.round(Math.min(w, h) * 0.34);
        terra.visible = false; sole.visible = false; orbita.visible = false; raggi.visible = false;
        const camT = new THREE.PerspectiveCamera(vt.fov, 1, 0.05, 400); camT.position.copy(vt.pos); camT.lookAt(vt.bers);
        aggiornaUniform(camT);
        renderer.setScissorTest(true); renderer.setScissor(8, h - s - 8, s, s); renderer.setViewport(8, h - s - 8, s, s); renderer.render(scena, camT);
        renderer.setScissorTest(false); aggiornaUniform(camera);
        ins.style.display = "block"; ins.style.width = s + "px"; ins.style.height = s + "px";
      } else ins.style.display = "none";
      // etichette
      const met = (nome, p, mostra) => { const el = etich[nome]; if (!mostra) { el.style.display = "none"; return; }
        v3.copy(p).project(camera); if (v3.z > 1) { el.style.display = "none"; return; }
        el.style.display = "block"; el.style.left = ((v3.x + 1) / 2 * w) + "px"; el.style.top = ((1 - v3.y) / 2 * h) + "px"; };
      met("Terra", new THREE.Vector3(0, -1.5, 0), fuori && tAnim > 0.7);
      met("Luna", L.clone().add(new THREE.Vector3(0, -1.6, 0)), fuori && tAnim > 0.7);
      met("Sole", new THREE.Vector3(SOLE_X, -3.6, 0), fuori && tAnim > 0.7);
      requestAnimationFrame(disegna);
    }

    // ---- controlli dell'interfaccia
    const cursore = radice.querySelector(".fl-eta");
    function aggiornaTesto() {
      const giorni = eta.toLocaleString(document.documentElement.lang || "it", { minimumFractionDigits: 1, maximumFractionDigits: 1 });
      radice.querySelector(".fl-stato").textContent = `${giorni} giorni dalla luna nuova · ${faseNome(eta)} · angolo Sole–Terra–Luna ${Math.round(angolo() / D2R) % 360 > 180 ? 360 - Math.round(angolo() / D2R) % 360 : Math.round(angolo() / D2R) % 360}°`;
    }
    cursore.addEventListener("input", () => { eta = +cursore.value; scegliFigura(null); aggiornaTesto(); });
    radice.querySelector(".fl-play").addEventListener("click", (ev) => { play = !play; ev.currentTarget.setAttribute("aria-pressed", play); ev.currentTarget.textContent = play ? "❚❚ Ferma" : "▶ Anima"; if (play) scegliFigura(null); });
    const bVista = radice.querySelector(".fl-vista");
    bVista.addEventListener("click", () => {
      daPos.copy(camera.position); daFov = camera.fov;
      const dir = new THREE.Vector3(); camera.getWorldDirection(dir); daBers.copy(camera.position).add(dir.multiplyScalar(vista === 1 && controlli ? camera.position.distanceTo(controlli.target) : 9));
      if (vista === 0 && verso === 0) { verso = 1; tAnim = 0; bVista.textContent = "↩ Torna al cannocchiale"; bVista.setAttribute("aria-pressed", "true"); }
      else { verso = -1; tAnim = 0; vista = 0; if (controlli) controlli.enabled = false; bVista.textContent = "Esci nello spazio ↗"; bVista.setAttribute("aria-pressed", "false"); }
    });
    radice.querySelector(".fl-cinerea").addEventListener("click", (ev) => { cinereaOn = !cinereaOn; ev.currentTarget.setAttribute("aria-pressed", cinereaOn); });
    const bottoni = radice.querySelectorAll(".fl-fig");
    function scegliFigura(k) {
      bottoni.forEach((b, i) => b.setAttribute("aria-pressed", i === k));
      const box = radice.querySelector(".fl-galileo");
      if (k === null) { box.innerHTML = '<span class="ui" style="font-size:.8rem;color:var(--dato)">Scegli una delle cinque figure di Galileo per confrontarla.</span>'; radice.querySelector(".fl-nota").textContent = ""; return; }
      const f = FIGURE[k]; eta = f.eta; cursore.value = eta; aggiornaTesto();
      box.innerHTML = `<img alt="${f.nome} di Galileo" src="${immaginiGalileo[k]}">`;
      radice.querySelector(".fl-nota").textContent = f.nota;
    }
    bottoni.forEach((b, i) => b.addEventListener("click", () => { play = false; const p = radice.querySelector(".fl-play"); p.setAttribute("aria-pressed", false); p.textContent = "▶ Anima"; scegliFigura(i); }));
    scegliFigura(0); aggiornaTesto();
    requestAnimationFrame(disegna);
    return { imposta: (e) => { eta = e; cursore.value = e; aggiornaTesto(); }, vista: () => bVista.click() };
  };
})();
