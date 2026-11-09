> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 7 — Libro I, Sezione V: determinazione delle orbite quando non è dato nessuno dei due fuochi

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo traduce integralmente la **Sezione V del Libro I** (*Inventio orbium ubi umbilicus neuter datur*): i Lemmi XVII–XXVII, le Proposizioni XXII–XXIX (Problemi XIV–XXI), con i loro casi, corollari e scolii, fino alla frase di passaggio alla Sezione VI. Il perimetro indicato nell’incarico, «Lemmi XVII–XXV», va esteso: la sezione comprende anche i **Lemmi XXVI e XXVII**, che preparano le Proposizioni XXVIII e XXIX, e sono tradotti qui. È una traduzione di lavoro, non un’edizione critica validata.

Gli identificatori **S5.01–S5.87** e i titoli tematici tra parentesi sono aggiunte editoriali. Servono a orientare la lettura e a controllare la completezza. I numeri romani dei lemmi, delle proposizioni e dei problemi appartengono al testo originale. Le integrazioni del curatore sono tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton.

La sezione è quasi tutta geometria delle coniche: Newton costruisce una conica a partire da cinque condizioni (punti o tangenti), e la trasformazione proiettiva del Lemma XXII riduce i casi con molte tangenti a quelli con molti punti. In coda al fascicolo, la **Parte B** contiene i dati strutturati per le pagine interattive dei lemmi e delle proposizioni con figura (22 unità).

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro I, Sezione V, pp. 73–104. Trascrizione normalizzata del Newton Project, documento **NATP00087**, nell’estratto `fonti/latino-1726-L1-S05.md` (scaricato l’8 novembre 2026, testo semplice senza correzioni). Le pagine sono quelle dei marcatori della trascrizione; le figure sono citate con i numeri [FIG 38]–[FIG 72] della trascrizione (immagini NATP00087-38…72, **non disponibili**).
2. **Inglese di confronto.** *Newton’s Principia. The Mathematical Principles of Natural Philosophy*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, Section V, **pp. 131–153** secondo i marcatori di pagina dell’EPUB Project Gutenberg n. 76404 (file `OEBPS/…76404-h-11.htm.xhtml`). Estratto di lavoro: `fonti/motte-1846-L1-S05.md`. Le quattro formule stampate come immagine (SVG 108–111) sono state rese con `rsvg-convert` e lette: BG²/AG; OA × AB/ad; OA × dg/ad; √ahb + ik + √alb.
3. **Fascicolo 3** del progetto (`Newton_Principia_IT_03_Leggi.md`), per il formato, i criteri e il glossario, e per il rimando del Cor. IV delle Leggi al Lemma XXIII; il latino di quel rimando è stato letto nella trascrizione NATP00086 conservata in `work/fonte_la.md`.
4. **Brief comune** dei fascicoli 4–12 (`brief/BRIEF.md`), con il glossario del Libro I.

Non ho consultato né riprodotto traduzioni moderne (Cajori, Cohen–Whitman, Pala, Giudice). Non ho potuto consultare la stampa del 1726 né le figure originali: i refusi della trascrizione sono segnalati come «probabili», da verificare.

### Criteri di traduzione

- Il testo guida è il latino; l’inglese serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o si discosta.
- Italiano contemporaneo, con la struttura argomentativa e il lessico storico conservati: i rapporti restano rapporti («A sta a B come C sta a D»), i prodotti restano «rettangoli», le radici quadrate restano «medie proporzionali» o «lati quadrati». Nel testo non compaiono formule moderne; i quadrati sono scritti con l’apice (HA², BG²) e le frazioni appiattite della trascrizione con la barra (BG²/AG).
- Il glossario comune del brief è rispettato: *sectio conica* «sezione conica»; *trajectoria* «traiettoria»; *orbis* «orbita»; *umbilicus* «fuoco»; *latus rectum / transversum* «lato retto / trasverso»; *diametri conjugatæ* «diametri coniugati»; *ordinatim applicata* «ordinata»; *abscissa* «ascissa»; *positione / specie / magnitudine datus* «dato di posizione / di forma / di grandezza»; *ratio subduplicata* «rapporto subduplicato»; *ducere in* «moltiplicare per»; *Cas.* «Caso»; *Corol.* «Cor.»; Q.E.D. «C.V.D.», Q.E.I. «C.V.T.», Q.E.F. «C.V.F.».
- Le estensioni del glossario, numerose in questa sezione geometrica, sono elencate e motivate nel § A.0.
- Gli enunciati dei lemmi, all’infinito o al congiuntivo retto da *dico*, sono resi con l’indicativo; i titoli dei problemi (*Trajectoriam describere …*) con l’infinito («Descrivere una traiettoria …»).
- Le lettere delle figure restano come nel latino, comprese le minuscole; i nomi dei rettangoli (PQK, AQB, XHY) sono conservati.

---

## Traduzione italiana

### Sezione V

### Determinazione delle orbite quando non è dato nessuno dei due fuochi

### Lemma XVII (rettangoli delle rette condotte da un punto della conica ai lati di un trapezio inscritto)

**[S5.01]** **Se da un punto qualsiasi P di una sezione conica data si conducono, sotto angoli dati, ai quattro lati AB, CD, AC, DB, prolungati indefinitamente, di un trapezio qualsiasi ABCD inscritto in quella sezione conica, altrettante rette PQ, PR, PS, PT, una a ciascun lato, il rettangolo PQ × PR delle rette condotte a due lati opposti sta al rettangolo PS × PT delle rette condotte agli altri due lati opposti in un rapporto dato.**

**[S5.02]** Caso 1. Supponiamo anzitutto che le linee condotte a due lati opposti siano parallele a uno degli altri lati: per esempio PQ e PR al lato AC, e PS e PT al lato AB. Siano inoltre paralleli fra loro due lati opposti, per esempio AC e BD. La retta che divide a metà quei lati paralleli sarà allora uno dei diametri della sezione conica, e dividerà a metà anche RQ. Sia O il punto in cui RQ è divisa a metà: PO sarà un’ordinata rispetto a quel diametro. Si prolunghi PO fino a K, in modo che OK sia uguale a PO: OK sarà l’ordinata dalla parte opposta del diametro. Poiché dunque i punti A, B, P e K stanno sulla sezione conica, e PK taglia AB sotto un angolo dato, il rettangolo PQK starà al rettangolo AQB in un rapporto dato (per le Prop. 17, 19, 21 e 23 del Libro III delle *Coniche* di Apollonio). Ma QK e PR sono uguali, in quanto differenze delle uguali OK, OP e OQ, OR; e di qui sono uguali anche i rettangoli PQK e PQ × PR. Perciò il rettangolo PQ × PR sta al rettangolo AQB, cioè al rettangolo PS × PT, in un rapporto dato. C.V.D.

**[S5.03]** Caso 2. Supponiamo ora che i lati opposti AC e BD del trapezio non siano paralleli. Si conduca Bd parallela ad AC, che incontri la retta ST in t e la sezione conica in d. Si congiunga Cd, che tagli PQ in r, e si conduca DM parallela a PQ, che tagli Cd in M e AB in N. Ora, per la similitudine dei triangoli BTt, DBN, Bt, ossia PQ, sta a Tt come DN sta a NB. Così anche Rr sta ad AQ, ossia a PS, come DM sta ad AN. Dunque, moltiplicando gli antecedenti per gli antecedenti e i conseguenti per i conseguenti, come il rettangolo PQ per Rr sta al rettangolo PS per Tt, così il rettangolo NDM sta al rettangolo ANB, e (per il Caso 1) così il rettangolo PQ per Pr sta al rettangolo PS per Pt; e, separando, così il rettangolo PQ × PR sta al rettangolo PS × PT. C.V.D.

**[S5.04]** Caso 3. Supponiamo infine che le quattro linee PQ, PR, PS, PT non siano parallele ai lati AC, AB, ma inclinate su di essi in un modo qualsiasi. Al loro posto si conducano Pq, Pr parallele ad AC, e Ps, Pt parallele ad AB: poiché gli angoli dei triangoli PQq, PRr, PSs, PTt sono dati, saranno dati i rapporti di PQ a Pq, di PR a Pr, di PS a Ps e di PT a Pt, e quindi i rapporti composti di PQ × PR a Pq × Pr e di PS × PT a Ps × Pt. Ma, per quanto si è dimostrato sopra, il rapporto di Pq × Pr a Ps × Pt è dato; dunque è dato anche il rapporto di PQ × PR a PS × PT. C.V.D.

### Lemma XVIII (il luogo è una sezione conica)

**[S5.05]** **Poste le stesse cose, se il rettangolo PQ × PR delle rette condotte a due lati opposti del trapezio sta al rettangolo PS × PT delle rette condotte agli altri due lati in un rapporto dato, il punto P, dal quale sono condotte le linee, si troverà su una sezione conica descritta intorno al trapezio.**

**[S5.06]** Immagina che per i punti A, B, C, D e per uno degli infiniti punti P, per esempio p, sia descritta una sezione conica: dico che il punto P si trova sempre su di essa. Se lo neghi, congiungi AP, che tagli questa sezione conica, se è possibile, in un punto diverso da P, per esempio in b. Dunque, se da questi punti p e b si conducono sotto gli angoli dati ai lati del trapezio le rette pq, pr, ps, pt e bk, bn, bf, bd, come bk × bn sta a bf × bd, così (per il Lemma XVII) pq × pr sta a ps × pt, e così (per ipotesi) PQ × PR sta a PS × PT. Inoltre, per la similitudine dei trapezi bkAf, PQAS, come bk sta a bf così PQ sta a PS. Perciò, dividendo i termini della proporzione precedente per i termini corrispondenti di questa, bn starà a bd come PR sta a PT. Dunque i trapezi equiangoli Dnbd, DRPT sono simili, e perciò le loro diagonali Db, DP coincidono. Quindi b cade nell’intersezione delle rette AP, DP, e perciò coincide con il punto P. Perciò il punto P, dovunque sia preso, cade sulla sezione conica assegnata. C.V.D.

**[S5.07]** Cor. Di qui, se da un punto comune P si conducono sotto angoli dati tre rette PQ, PR, PS ad altrettante rette date di posizione AB, CD, AC, una a ciascuna, e il rettangolo PQ × PR di due delle rette condotte sta al quadrato PS² della terza in un rapporto dato, il punto P, dal quale sono condotte le rette, sarà situato su una sezione conica che tocca le linee AB, CD in A e C; e viceversa. Infatti, restando ferma la posizione delle tre rette AB, CD, AC, la linea BD venga a coincidere con la linea AC; poi anche la linea PT venga a coincidere con la linea PS: il rettangolo PS × PT diventerà PS², e le rette AB, CD, che tagliavano la curva nei punti A e B, C e D, non potranno più tagliarla in quei punti venuti a coincidere, ma la toccheranno soltanto.

#### Scolio

**[S5.08]** In questo lemma il nome di sezione conica è preso in senso ampio, così da comprendere sia la sezione rettilinea passante per il vertice del cono, sia quella circolare parallela alla base. Infatti, se il punto p cade sulla retta che congiunge i punti A e D, oppure C e B, la sezione conica si muterà in una coppia di rette: l’una è la retta su cui cade il punto p, l’altra è la retta che congiunge gli altri due dei quattro punti. Se due angoli opposti del trapezio, presi insieme, sono uguali a due retti, e le quattro linee PQ, PR, PS, PT sono condotte ai suoi lati o perpendicolarmente o sotto angoli qualsiasi uguali fra loro, e il rettangolo PQ × PR di due delle rette condotte è uguale al rettangolo PS × PT delle altre due, la sezione conica diventerà un cerchio. Lo stesso avverrà se le quattro linee sono condotte sotto angoli qualsiasi, e il rettangolo PQ × PR di due delle rette condotte sta al rettangolo PS × PT delle altre due come il rettangolo dei seni degli angoli S, T, sotto i quali sono condotte le ultime due, PS e PT, sta al rettangolo dei seni degli angoli Q, R, sotto i quali sono condotte le prime due, PQ e PR. Negli altri casi il luogo del punto P sarà una delle tre figure che comunemente si chiamano sezioni coniche. Al posto del trapezio ABCD si può poi sostituire un quadrilatero i cui due lati opposti si incrociano a vicenda come diagonali. Ma anche dei quattro punti A, B, C, D uno o due possono andarsene all’infinito, e in tal modo i lati della figura che convergono verso quei punti possono diventare paralleli: in questo caso la sezione conica passerà per gli altri punti e se ne andrà all’infinito nella direzione delle parallele.

### Lemma XIX (trovare un punto del luogo delle quattro rette)

**[S5.09]** **Trovare un punto P tale che, se da esso si conducono sotto angoli dati quattro rette PQ, PR, PS, PT ad altrettante rette date di posizione AB, CD, AC, BD, una a ciascuna, il rettangolo PQ × PR di due delle rette condotte stia al rettangolo PS × PT delle altre due in un rapporto dato.**

**[S5.10]** Le linee AB, CD, alle quali sono condotte le due rette PQ, PR che comprendono uno dei rettangoli, incontrino le altre due linee date di posizione nei punti A, B, C, D. Da uno di essi, A, si conduca una retta qualsiasi AH, sulla quale si voglia trovare il punto P. Essa tagli le linee opposte BD, CD, cioè BD in H e CD in I; poiché tutti gli angoli della figura sono dati, saranno dati i rapporti di PQ a PA e di PA a PS, e quindi il rapporto di PQ a PS. Togliendo questo rapporto dal rapporto dato di PQ × PR a PS × PT, sarà dato il rapporto di PR a PT; e aggiungendo i rapporti dati di PI a PR e di PT a PH, sarà dato il rapporto di PI a PH, e perciò il punto P. C.V.T.

**[S5.11]** Cor. 1. Di qui si può anche condurre la tangente in un punto qualsiasi D del luogo degli infiniti punti P. Infatti la corda PD, quando i punti P e D si riuniscono, cioè quando AH è condotta per il punto D, diventa tangente. In questo caso il rapporto ultimo delle evanescenti IP e PH si troverà come sopra. Si conduca dunque CF parallela ad AD, che incontri BD in F e sia divisa in E in quel rapporto ultimo: DE sarà la tangente, perché CF e l’evanescente IH sono parallele e sono divise in modo simile in E e in P.

**[S5.12]** Cor. 2. Di qui si può anche determinare il luogo di tutti i punti P. Per uno qualsiasi dei punti A, B, C, D, per esempio A, si conduca la tangente AE al luogo, e per un altro punto qualsiasi, B, si conduca BF parallela alla tangente, che incontri il luogo in F. Il punto F si troverà per il Lemma XIX. Si divida BF a metà in G: la retta indefinita AG, una volta condotta, darà la posizione del diametro rispetto al quale BG e FG sono ordinate. Questa AG incontri il luogo in H: AH sarà il lato trasverso, al quale il lato retto starà come BG² sta ad AG × GH. Se AG non incontra il luogo in alcun punto, poiché la linea AH è infinita, il luogo sarà una parabola, e il suo lato retto relativo al diametro AG sarà BG²/AG. Se invece lo incontra in qualche punto, il luogo sarà un’iperbole quando i punti A e H sono situati dalla stessa parte di G, e un’ellisse quando G è in mezzo, a meno che l’angolo AGB sia retto e inoltre BG² sia uguale al rettangolo AGH: in questo caso si avrà un cerchio.

**[S5.13]** E così in questo corollario si presenta, del problema degli antichi sulle quattro linee, iniziato da Euclide e proseguito da Apollonio, non un calcolo, ma una composizione geometrica, quale gli antichi cercavano.

### Lemma XX (rapporto costante dei segmenti staccati sui lati di un parallelogramma)

**[S5.14]** **Se un parallelogramma qualsiasi ASPQ tocca con due angoli opposti, A e P, una sezione conica qualsiasi nei punti A e P; se con i lati AQ, AS di uno di quegli angoli, prolungati indefinitamente, incontra la stessa sezione conica in B e C; e se dai punti d’incontro B e C a un quinto punto qualsiasi D della sezione conica si conducono due rette BD, CD, che incontrino gli altri due lati del parallelogramma, PS e PQ, prolungati indefinitamente, in T e R: le parti PR e PT staccate dai lati staranno sempre fra loro in un rapporto dato. E viceversa, se quelle parti staccate stanno fra loro in un rapporto dato, il punto D si troverà su una sezione conica passante per i quattro punti A, B, C, P.**

**[S5.15]** Caso 1. Si congiungano BP, CP e dal punto D si conducano due rette DG, DE: la prima, DG, sia parallela ad AB e incontri PB, PQ, CA in H, I, G; l’altra, DE, sia parallela ad AC e incontri PC, PS, AB in F, K, E. Per il Lemma XVII il rettangolo DE × DF starà al rettangolo DG × DH in un rapporto dato. Ma PQ sta a DE (ossia a IQ) come PB sta a HB, e quindi come PT sta a DH; e, permutando, PQ sta a PT come DE sta a DH. Inoltre PR sta a DF come RC sta a DC, e quindi come (IG, ossia) PS sta a DG; e, permutando, PR sta a PS come DF sta a DG. Componendo i rapporti, il rettangolo PQ × PR sta al rettangolo PS × PT come il rettangolo DE × DF sta al rettangolo DG × DH, e quindi in un rapporto dato. Ma PQ e PS sono date, e perciò è dato il rapporto di PR a PT. C.V.D.

**[S5.16]** Caso 2. Se invece si pone che PR e PT stiano fra loro in un rapporto dato, ripercorrendo all’indietro un ragionamento simile ne seguirà che il rettangolo DE × DF sta al rettangolo DG × DH in un rapporto dato, e quindi (per il Lemma XVIII) che il punto D si trova su una sezione conica passante per i punti A, B, C, P. C.V.D.

**[S5.17]** Cor. 1. Di qui, se si conduce BC, che tagli PQ in r, e [su] PT si prende Pt che stia a Pr nel rapporto che PT ha a PR, Bt sarà tangente alla sezione conica nel punto B. Immagina infatti che il punto D si riunisca con il punto B, così che, svanendo la corda BD, BT diventi tangente: CD e BT coincideranno con CB e Bt.

**[S5.18]** Cor. 2. E viceversa, se Bt è tangente, e BD, CD si incontrano in un punto qualsiasi D della sezione conica, PR starà a PT come Pr sta a Pt. E, al contrario, se PR sta a PT come Pr sta a Pt, BD e CD si incontreranno in qualche punto D della sezione conica.

**[S5.19]** Cor. 3. Una sezione conica non taglia un’altra sezione conica in più di quattro punti. Infatti, se è possibile, due sezioni coniche passino per i cinque punti A, B, C, P, O; la retta BD le tagli nei punti D, d, e la retta Cd tagli PQ in q. Dunque PR sta a PT come Pq sta a PT; perciò PR e Pq sono uguali fra loro, contro l’ipotesi.

### Lemma XXI (descrizione organica della conica: due angoli che ruotano intorno a due poli)

**[S5.20]** **Se due rette mobili e infinite BM, CM, condotte per i punti dati B, C come per due poli, descrivono con il loro punto d’incontro M una terza retta MN data di posizione; e se si conducono altre due rette infinite BD, CD, che formino con le prime due, nei punti dati B, C, gli angoli dati MBD, MCD: dico che queste due rette BD, CD descriveranno con il loro punto d’incontro D una sezione conica passante per i punti B, C. E viceversa, se le rette BD, CD descrivono con il loro punto d’incontro D una sezione conica passante per i punti dati B, C, A, e l’angolo DBM è sempre uguale all’angolo dato ABC e l’angolo DCM sempre uguale all’angolo dato ACB, il punto M si troverà su una retta data di posizione.**

**[S5.21]** Sia infatti dato sulla retta MN il punto N, e quando il punto mobile M cade sul punto fisso N, il punto mobile D cada sul punto fisso P. Congiungi CN, BN, CP, BP, e dal punto P conduci le rette PT, PR, che incontrino BD, CD in T e R e formino l’angolo BPT uguale all’angolo dato BNM e l’angolo CPR uguale all’angolo dato CNM. Poiché dunque (per ipotesi) gli angoli MBD, NBP sono uguali, come pure gli angoli MCD, NCP, togli gli angoli comuni NBD e NCD: resteranno uguali NBM e PBT, NCM e PCR; e perciò i triangoli NBM, PBT sono simili, come pure i triangoli NCM, PCR. Perciò PT sta a NM come PB sta a NB, e PR sta a NM come PC sta a NC. Ma i punti B, C, N, P sono fissi. Dunque PT e PR hanno un rapporto dato con NM, e quindi un rapporto dato fra loro; e perciò (per il Lemma XX) il punto D, nel quale si incontrano in ogni istante le rette mobili BT e CR, si trova su una sezione conica passante per i punti B, C, P. C.V.D.

**[S5.22]** E viceversa, se il punto mobile D si trova su una sezione conica passante per i punti dati B, C, A, l’angolo DBM è sempre uguale all’angolo dato ABC e l’angolo DCM sempre uguale all’angolo dato ACB, e quando il punto D cade successivamente su due punti fissi qualsiasi p, P della sezione il punto mobile M cade successivamente su due punti fissi n, N: per questi stessi n, N si conduca la retta nN, e questa sarà il luogo costante di quel punto mobile M. Infatti, se è possibile, il punto M si trovi su una linea curva. Il punto D si troverà dunque su una sezione conica passante per i cinque punti B, C, A, p, P, quando il punto M si trova sempre su una linea curva. Ma, per quanto già dimostrato, il punto D si troverà anche su una sezione conica passante per gli stessi cinque punti B, C, A, p, P, quando il punto M si trova sempre su una linea retta. Dunque due sezioni coniche passeranno per gli stessi cinque punti, contro il Cor. 3 del Lemma XX. È dunque assurdo che il punto M si trovi su una linea curva. C.V.D.

### Proposizione XXII. Problema XIV (traiettoria per cinque punti)

**[S5.23]** **Descrivere una traiettoria per cinque punti dati.**

**[S5.24]** Siano dati i cinque punti A, B, C, P, D. Da uno di essi, A, ad altri due qualsiasi, B e C, che si chiameranno poli, conduci le rette AB, AC, e per il quarto punto P le rette TPS, PRQ, parallele a queste. Poi dai due poli B, C conduci per il quinto punto D due rette infinite BDT, CRD, che incontrino le rette TPS, PRQ condotte per ultime (la prima con la prima e la seconda con la seconda) in T e R. Infine, conducendo una retta tr parallela a TR, stacca dalle rette PT, PR due segmenti qualsiasi Pt, Pr proporzionali a PT, PR; e se le rette Bt, Cr, condotte per i loro estremi t, r e per i poli B, C, si incontrano in d, quel punto d sarà situato sulla traiettoria cercata. Infatti quel punto d (per il Lemma XX) si trova su una sezione conica passante per i quattro punti A, B, C, P; e, quando le linee Rr, Tt svaniscono, il punto d si riunisce con il punto D. La sezione conica passa dunque per i cinque punti A, B, C, P, D. C.V.D.

#### Lo stesso, altrimenti

**[S5.25]** Dei punti dati congiungi tre qualsiasi, A, B, C; e, facendo ruotare intorno a due di essi, B e C, come intorno a poli, gli angoli ABC, ACB, dati di grandezza, si portino i bracci BA, CA prima sul punto D, poi sul punto P, e si segnino i punti M, N nei quali gli altri bracci BL, CL si incrociano nell’uno e nell’altro caso. Si conduca la retta infinita MN, e quegli angoli mobili ruotino intorno ai loro poli B, C con la regola che l’intersezione dei bracci BL, CL, ossia BM, CM, che ora sia m, cada sempre su quella retta infinita MN: l’intersezione dei bracci BA, CA, ossia BD, CD, che ora sia d, traccerà la traiettoria cercata PADdB. Infatti il punto d (per il Lemma XXI) si troverà su una sezione conica passante per i punti B, C; e quando il punto m giunge ai punti L, M, N, il punto d (per costruzione) giungerà ai punti A, D, P. Si descriverà dunque una sezione conica passante per i cinque punti A, B, C, P, D. C.V.F.

#### Corollari

**[S5.26]** Cor. 1. Di qui si può condurre speditamente una retta che tocchi la traiettoria cercata in un qualsiasi punto dato B. Il punto d si avvicini al punto B: la retta Bd diventerà la tangente cercata.

**[S5.27]** Cor. 2. Di qui si possono trovare anche i centri, i diametri e i lati retti delle traiettorie, come nel Cor. 2 del Lemma XIX.

#### Scolio

**[S5.28]** La prima costruzione diventerà un poco più semplice congiungendo BP e prendendo su di essa, prolungata se occorre, Bp che stia a BP come PR sta a PT; conducendo per p la retta infinita pe parallela a SPT e prendendo su di essa pe sempre uguale a Pr; e conducendo le rette Be, Cr, che si incontrino in d. Infatti, poiché Pr sta a Pt, PR a PT, pB a PB, pe a Pt nello stesso rapporto, pe e Pr saranno sempre uguali. Con questo metodo i punti della traiettoria si trovano con la massima speditezza, a meno che tu non preferisca descrivere la curva meccanicamente, come nella seconda costruzione.

### Proposizione XXIII. Problema XV (traiettoria per quattro punti, tangente a una retta data)

**[S5.29]** **Descrivere una traiettoria che passi per quattro punti dati e tocchi una retta data di posizione.**

**[S5.30]** Caso 1. Siano dati la tangente HB, il punto di contatto B e altri tre punti C, D, P. Congiungi BC e, conducendo PS parallela alla retta BH e PQ parallela alla retta BC, completa il parallelogramma BSPQ. Conduci BD, che tagli SP in T, e CD, che tagli PQ in R. Infine, conducendo una qualsiasi tr parallela a TR, stacca da PQ, PS i segmenti Pr, Pt proporzionali rispettivamente a PR, PT: il punto d’incontro d delle rette Cr, Bt, una volta condotte, cadrà sempre (per il Lemma XX) sulla traiettoria da descrivere.

#### Lo stesso, altrimenti

**[S5.31]** Ruotino sia l’angolo CBH, dato di grandezza, intorno al polo B, sia un raggio rettilineo qualsiasi DC, prolungato da entrambe le parti, intorno al polo C. Si segnino i punti M, N in cui il braccio BC dell’angolo taglia quel raggio quando l’altro braccio, BH, incontra lo stesso raggio nei punti P e D. Poi quel raggio CP, ossia CD, e il braccio BC dell’angolo si incontrino continuamente sulla retta infinita MN, una volta condotta: il punto d’incontro dell’altro braccio, BH, con il raggio traccerà la traiettoria cercata.

**[S5.32]** Infatti, se nelle costruzioni del problema precedente il punto A si avvicina al punto B, le linee CA e CB coincideranno, e la linea AB, nella sua posizione ultima, diventerà la tangente BH; e perciò le costruzioni là esposte diventeranno identiche alle costruzioni qui descritte. Il punto d’incontro del braccio BH con il raggio traccerà dunque una sezione conica passante per i punti C, D, P e tangente alla retta BH nel punto B. C.V.F.

#### Caso 2

**[S5.33]** Caso 2. Siano dati quattro punti B, C, D, P situati fuori della tangente HI. Congiungili a due a due con le linee BD, CP, che si incontrino in G e incontrino la tangente in H e I. Si divida la tangente in A in modo che HA stia a IA come il rettangolo della media proporzionale fra CG e GP e della media proporzionale fra BH e HD sta al rettangolo della media proporzionale fra DG e GB e della media proporzionale fra PI e IC: A sarà il punto di contatto. Infatti, se HX, parallela alla retta PI, taglia la traiettoria in punti qualsiasi X e Y, il punto A (per la teoria delle coniche) dovrà essere collocato in modo che HA² stia ad AI² nel rapporto composto del rapporto del rettangolo XHY al rettangolo BHD, ossia del rettangolo CGP al rettangolo DGB, e del rapporto del rettangolo BHD al rettangolo PIC. Trovato poi il punto di contatto A, la traiettoria si descriverà come nel primo caso. C.V.F.

**[S5.34]** Il punto A si può prendere sia fra i punti H e I, sia fuori di essi; e di conseguenza la traiettoria si può descrivere in due modi.

### Proposizione XXIV. Problema XVI (traiettoria per tre punti, tangente a due rette date)

**[S5.35]** **Descrivere una traiettoria che passi per tre punti dati e tocchi due rette date di posizione.**

**[S5.36]** Siano date le tangenti HI, KL e i punti B, C, D. Per due punti qualsiasi, B e D, conduci la retta infinita BD, che incontri le tangenti nei punti H, K. Poi, anche per altri due punti qualsiasi, C e D, conduci la retta infinita CD, che incontri le tangenti nei punti I, L. Dividi le rette così condotte in R e S in modo che HR stia a KR come la media proporzionale fra BH e HD sta alla media proporzionale fra BK e KD, e IS stia a LS come la media proporzionale fra CI e ID sta alla media proporzionale fra CL e LD. Dividi a piacere o fra i punti K e H, I e L, o fuori di essi; poi conduci RS, che tagli le tangenti in A e P: A e P saranno i punti di contatto. Infatti, si supponga che A e P siano i punti di contatto, situati in qualche luogo sulle tangenti; per uno qualsiasi dei punti H, I, K, L, per esempio I, situato sulla tangente HI, si conduca la retta IY parallela all’altra tangente KL, che incontri la curva in X e Y, e su di essa si prenda IZ media proporzionale fra IX e IY: per la teoria delle coniche, il rettangolo XIY, ossia IZ², sta a LP² come il rettangolo CID sta al rettangolo CLD, cioè (per costruzione) come SI² sta a SL²; e perciò IZ sta a LP come SI sta a SL. I punti S, P, Z giacciono dunque su una stessa retta. Inoltre, se le tangenti si incontrano in G, il rettangolo XIY, ossia IZ², starà (per la teoria delle coniche) a IA² come GP² sta a GA², e quindi IZ starà a IA come GP sta a GA. I punti P, Z e A giacciono dunque su una stessa retta, e perciò i punti S, P e A sono su una stessa retta. E con lo stesso argomento si proverà che i punti R, P e A sono su una stessa retta. I punti di contatto A e P giacciono dunque sulla retta RS. Trovati questi, la traiettoria si descriverà come nel primo caso del problema precedente. C.V.F.

**[S5.37]** In questa proposizione e nel secondo caso della proposizione precedente le costruzioni sono le stesse, sia che la retta XY tagli la traiettoria in X e Y, sia che non la tagli; ed esse non dipendono da questa intersezione. Ma, dimostrate le costruzioni nel caso in cui quella retta taglia la traiettoria, si conoscono anche le costruzioni nel caso in cui non la taglia; e, per brevità, non mi trattengo a dimostrarle ulteriormente.

### Lemma XXII (trasformazione delle figure)

**[S5.38]** **Mutare figure in altre figure dello stesso genere.**

**[S5.39]** Si debba trasformare una figura qualsiasi HGI. Si conducano a piacere due rette parallele AO, BL, che taglino in A e B una terza retta qualsiasi AB data di posizione, e da un punto qualsiasi G della figura si conduca alla retta AB una retta GD parallela a OA. Poi da un punto O, dato sulla linea OA, si conduca al punto D la retta OD, che incontri BL in d, e dal punto d’incontro si innalzi una retta dg che formi con la retta BL un angolo dato qualsiasi e abbia con Od il rapporto che DG ha con OD: g sarà il punto della figura nuova hgi corrispondente al punto G. Allo stesso modo i singoli punti della prima figura daranno altrettanti punti della figura nuova. Immagina dunque che il punto G percorra con moto continuo tutti i punti della prima figura: anche il punto g percorrerà con moto continuo tutti i punti della figura nuova e la descriverà. Per distinguerli, chiamiamo DG prima ordinata, dg nuova ordinata; AD prima ascissa, ad nuova ascissa; O polo, OD raggio secante, OA primo raggio ordinato e Oa (con il quale si completa il parallelogramma OABa) nuovo raggio ordinato.

**[S5.40]** Dico ora che, se il punto G si trova su una linea retta data di posizione, anche il punto g si troverà su una linea retta data di posizione. Se il punto G si trova su una sezione conica, anche il punto g si troverà su una sezione conica. Qui conto il cerchio fra le sezioni coniche. Inoltre, se il punto G si trova su una linea del terzo ordine analitico, il punto g si troverà su una linea ugualmente del terzo ordine; e così per le linee curve degli ordini superiori. Le due linee su cui si trovano i punti G, g saranno sempre dello stesso ordine analitico. Infatti, come ad sta a OA, così stanno Od a OD, dg a DG e AB ad AD; e perciò AD è uguale a OA × AB/ad, e DG è uguale a OA × dg/ad. Ora, se il punto G si trova su una linea retta, e perciò in qualsiasi equazione che esprima la relazione fra l’ascissa AD e l’ordinata DG quelle indeterminate AD e DG salgono a una sola dimensione, scrivendo in questa equazione OA × AB/ad al posto di AD e OA × dg/ad al posto di DG si produrrà un’equazione nuova, nella quale l’ascissa nuova ad e l’ordinata nuova dg saliranno a una sola dimensione, e che perciò designa una linea retta. Se invece AD e DG, o una di esse, salivano a due dimensioni nella prima equazione, anche ad e dg saliranno a due nella seconda equazione. E così per tre o più dimensioni. Le indeterminate ad, dg nella seconda equazione e AD, DG nella prima saliranno sempre allo stesso numero di dimensioni, e perciò le linee su cui si trovano i punti G, g sono dello stesso ordine analitico.

**[S5.41]** Dico inoltre che, se una retta tocca una linea curva nella prima figura, questa retta, trasferita nella figura nuova nello stesso modo della curva, toccherà quella linea curva nella figura nuova; e viceversa. Infatti, se due punti qualsiasi della curva si avvicinano l’uno all’altro e si riuniscono nella prima figura, gli stessi punti, trasferiti, si avvicineranno l’uno all’altro e si riuniranno nella figura nuova; e perciò le rette che congiungono questi punti diventeranno insieme tangenti alle curve nell’una e nell’altra figura.

**[S5.42]** Le dimostrazioni di queste affermazioni si potrebbero comporre in modo più geometrico. Ma bado alla brevità.

**[S5.43]** Dunque, se si deve trasformare una figura rettilinea in un’altra, basta trasferire le intersezioni delle rette di cui è composta e condurre per esse, nella figura nuova, delle linee rette. Se invece bisogna trasformare una figura curvilinea, si devono trasferire i punti, le tangenti e le altre rette per mezzo delle quali la linea curva è definita. Questo lemma serve poi alla soluzione dei problemi più difficili, trasformando le figure proposte in figure più semplici. Infatti rette convergenti qualsiasi si trasformano in parallele assumendo come primo raggio ordinato una linea retta qualsiasi che passi per il punto d’incontro delle rette convergenti; e ciò perché in tal modo quel punto d’incontro se ne va all’infinito, e parallele sono appunto le linee che non si incontrano in alcun punto. Risolto poi il problema nella figura nuova, se questa figura si ritrasforma nella prima con le operazioni inverse, si avrà la soluzione cercata.

**[S5.44]** Questo lemma è utile anche nella soluzione dei problemi solidi. Infatti, ogni volta che si presentano due sezioni coniche con la cui intersezione il problema si può risolvere, è lecito trasformare una delle due, se è un’iperbole o una parabola, in un’ellisse; poi l’ellisse si muta facilmente in un cerchio. Allo stesso modo, nella costruzione dei problemi piani, una retta e una sezione conica si mutano in una retta e in un cerchio.

### Proposizione XXV. Problema XVII (traiettoria per due punti, tangente a tre rette date)

**[S5.45]** **Descrivere una traiettoria che passi per due punti dati e tocchi tre rette date di posizione.**

**[S5.46]** Per il punto d’incontro di due tangenti qualsiasi fra loro e per il punto d’incontro della terza tangente con la retta che passa per i due punti dati conduci una retta infinita; e, assunta questa come primo raggio ordinato, si trasformi la figura, per il lemma precedente, in una figura nuova. In questa figura quelle due tangenti diventeranno parallele fra loro, e la terza tangente diventerà parallela alla retta che passa per i due punti. Siano hi, kl quelle due tangenti parallele, ik la terza tangente, e hl la retta parallela a questa che passa per i punti a, b, per i quali la sezione conica deve passare in questa figura nuova, e che completa il parallelogramma hikl. Si dividano le rette hi, ik, kl in c, d, e in modo che hc stia al lato quadrato del rettangolo ahb, ic a id e ke a kd come la somma delle rette hi e kl sta alla somma di tre linee, delle quali la prima è la retta ik e le altre due sono i lati quadrati dei rettangoli ahb e alb: c, d, e saranno i punti di contatto. Infatti, per la teoria delle coniche, hc² sta al rettangolo ahb, ic² a id², ke² a kd² ed el² al rettangolo alb nello stesso rapporto; e perciò hc sta al lato quadrato di ahb, ic a id, ke a kd ed el al lato quadrato di alb nel rapporto subduplicato di quello, e, componendo, nel rapporto dato di tutti gli antecedenti, hi e kl, a tutti i conseguenti, che sono il lato quadrato del rettangolo ahb, la retta ik e il lato quadrato del rettangolo alb. Da quel rapporto dato si hanno dunque i punti di contatto c, d, e nella figura nuova. Con le operazioni inverse dell’ultimo lemma si trasferiscano questi punti nella prima figura, e là (per il Probl. XIV) si descriverà la traiettoria. C.V.F.

**[S5.47]** Del resto, a seconda che i punti a, b giacciano fra i punti h, l oppure fuori di essi, i punti c, d, e si devono prendere fra i punti h, i, k, l oppure fuori di essi. Se uno dei punti a, b cade fra i punti h, l e l’altro fuori, il problema è impossibile.

### Proposizione XXVI. Problema XVIII (traiettoria per un punto, tangente a quattro rette date)

**[S5.48]** **Descrivere una traiettoria che passi per un punto dato e tocchi quattro rette date di posizione.**

**[S5.49]** Dall’intersezione comune di due tangenti qualsiasi all’intersezione comune delle altre due si conduca una retta infinita e, assunta questa come primo raggio ordinato, si trasformi la figura (per il Lemma XXII) in una figura nuova: le tangenti che a due a due concorrevano sul raggio ordinato diventeranno ora parallele. Siano queste hi e kl, ik e hl, che comprendono il parallelogramma hikl. E sia p il punto che in questa figura nuova corrisponde al punto dato nella prima figura. Per il centro O della figura si conduca pq, e, se Oq è uguale a Op, q sarà l’altro punto per il quale la sezione conica deve passare in questa figura nuova. Con l’operazione inversa del Lemma XXII si trasferisca questo punto nella prima figura: là si avranno due punti per i quali si deve descrivere la traiettoria. E per essi quella traiettoria si può descrivere per il Probl. XVII. C.V.F.

### Lemma XXIII (punto che divide in un rapporto dato una retta mobile)

**[S5.50]** **Se due rette date di posizione, AC e BD, terminano nei punti dati A, B e hanno fra loro un rapporto dato, e la retta CD, che congiunge i punti indeterminati C, D, è divisa in K in un rapporto dato: dico che il punto K sarà situato su una retta data di posizione.**

**[S5.51]** Le rette AC, BD si incontrino infatti in E; su BE si prenda BG che stia ad AE come BD sta ad AC, e FD sia sempre uguale alla data EG: per costruzione EC starà a GD, cioè a EF, come AC sta a BD, e quindi in un rapporto dato; e perciò il triangolo EFC sarà dato di forma. Si divida CF in L in modo che CL stia a CF nel rapporto di CK a CD; poiché quel rapporto è dato, sarà dato di forma anche il triangolo EFL, e quindi il punto L sarà situato sulla retta EL data di posizione. Congiungi LK: i triangoli CLK, CFD saranno simili; e, poiché FD è data ed è dato il rapporto di LK a FD, sarà data LK. Si prenda EH uguale a questa: ELKH sarà sempre un parallelogramma. Il punto K è dunque situato sul lato HK di quel parallelogramma, dato di posizione. C.V.D.

**[S5.52]** Cor. Poiché la figura EFLC è data di forma, le tre rette EF, EL ed EC, cioè GD, HK ed EC, hanno fra loro rapporti dati.

### Lemma XXIV (tangenti parallele e semidiametro medio proporzionale)

**[S5.53]** **Se tre rette toccano una sezione conica qualsiasi, e due di esse sono parallele e date di posizione: dico che il semidiametro della sezione parallelo a queste due è medio proporzionale fra i loro segmenti compresi fra i punti di contatto e la terza tangente.**

**[S5.54]** Siano AF, GB due parallele che toccano la sezione conica ADB in A e B; EF una terza retta che tocca la sezione conica in I e incontra le prime tangenti in F e G; e sia CD il semidiametro della figura parallelo alle tangenti: dico che AF, CD, BG sono in proporzione continua.

**[S5.55]** Infatti, se i diametri coniugati AB, DM incontrano la tangente FG in E e H e si tagliano a vicenda in C, e si completa il parallelogramma IKCL, per la natura delle sezioni coniche come EC sta a CA così CA sta a LC, e così, separando, EC − CA sta a CA − CL, ossia EA ad AL; e, componendo, EA sta a EA + AL, ossia a EL, come EC sta a EC + CA, ossia a EB; e perciò, per la similitudine dei triangoli EAF, ELI, ECH, EBG, AF sta a LI come CH sta a BG. Parimenti, per la natura delle sezioni coniche, LI, ossia CK, sta a CD come CD sta a CH; e perciò, per uguaglianza perturbata, AF sta a CD come CD sta a BG. C.V.D.

**[S5.56]** Cor. 1. Di qui, se due tangenti FG, PQ incontrano le tangenti parallele AF, BG in F e G, P e Q, e si tagliano a vicenda in O, per uguaglianza perturbata AF starà a BQ come AP sta a BG, e, separando, come FP sta a GQ, e quindi come FO sta a OG.

**[S5.57]** Cor. 2. Di qui anche le due rette PG, FQ, condotte per i punti P e G, F e Q, si incontreranno sulla retta ACB che passa per il centro della figura e per i punti di contatto A, B.

### Lemma XXV (parallelogramma circoscritto e quinta tangente)

**[S5.58]** **Se i quattro lati di un parallelogramma, prolungati indefinitamente, toccano una sezione conica qualsiasi e sono tagliati da una quinta tangente qualsiasi, e si prendono, su due lati contigui qualsiasi, le parti staccate che terminano negli angoli opposti del parallelogramma: dico che una delle due parti staccate sta al lato dal quale è staccata come la parte dell’altro lato contiguo compresa fra il punto di contatto e il terzo lato sta all’altra parte staccata.**

**[S5.59]** I quattro lati ML, IK, KL, MI del parallelogramma MLIK tocchino la sezione conica in A, B, C, D, e la quinta tangente FQ tagli questi lati in F, Q, H ed E; si prendano poi le parti staccate ME, KQ dei lati MI, KI, oppure le parti staccate KH, MF dei lati KL, ML: dico che ME sta a MI come BK sta a KQ, e KH sta a KL come AM sta a MF. Infatti, per il corollario del lemma precedente, ME sta a EI come AM, ossia BK, sta a BQ, e, componendo, ME sta a MI come BK sta a KQ. C.V.D. Così pure KH sta a HL come (BK, ossia) AM sta ad AF, e, separando, KH sta a KL come AM sta a MF. C.V.D.

**[S5.60]** Cor. 1. Di qui, se è dato il parallelogramma IKLM descritto intorno a una sezione conica data, sarà dato il rettangolo KQ × ME, come pure il rettangolo KH × MF, uguale a questo. Quei rettangoli sono infatti uguali per la similitudine dei triangoli KQH, MFE.

**[S5.61]** Cor. 2. E se si conduce una sesta tangente eq, che incontri le tangenti KI, MI in q ed e, il rettangolo KQ × ME sarà uguale al rettangolo Kq × Me; e KQ starà a Me come Kq sta a ME, e, separando, come Qq sta a Ee.

**[S5.62]** Cor. 3. Di qui anche, se si congiungono Eq, eQ e si dividono a metà, e per i punti di bisezione si conduce una retta, questa passerà per il centro della sezione conica. Infatti, poiché Qq sta a Ee come KQ sta a Me, la stessa retta passerà per il punto di mezzo di tutte le rette Eq, eQ, MK (per il Lemma XXIII), e il punto di mezzo della retta MK è il centro della sezione.

### Proposizione XXVII. Problema XIX (traiettoria tangente a cinque rette date)

**[S5.63]** **Descrivere una traiettoria che tocchi cinque rette date di posizione.**

**[S5.64]** Siano date di posizione le tangenti ABG, BCF, GCD, FDE, EA. Dividi a metà in M e N le diagonali AF, BE della figura quadrilatera ABFE, compresa da quattro qualsiasi di esse: per il Cor. 3 del Lemma XXV la retta MN, condotta per i punti di bisezione, passerà per il centro della traiettoria. Di nuovo, dividi a metà in P e Q le diagonali (per così dire) BD, GF della figura quadrilatera BGDF, compresa da altre quattro tangenti qualsiasi: anche la retta PQ, condotta per i punti di bisezione, passerà per il centro della traiettoria. Il centro sarà dunque dato nel punto d’incontro delle bisecanti. Sia esso O. Conduci KL parallela a una tangente qualsiasi BC, a una distanza tale che il centro O si trovi a metà fra le parallele: KL, così condotta, toccherà la traiettoria da descrivere. Essa tagli due altre tangenti qualsiasi, GCD e FDE, in L e K. Per i punti d’incontro C e K, F e L di queste tangenti non parallele CL, FK con le parallele CF, KL conduci CK, FL, che si incontrino in R: la retta OR, condotta e prolungata, taglierà le tangenti parallele CF, KL nei punti di contatto. Ciò è evidente per il Cor. 2 del Lemma XXIV. Con lo stesso metodo si possono trovare gli altri punti di contatto, e infine descrivere la traiettoria con la costruzione del Probl. XIV. C.V.F.

#### Scolio

**[S5.65]** I problemi in cui sono dati i centri o gli asintoti delle traiettorie sono compresi nei precedenti. Infatti, dati dei punti e delle tangenti insieme con il centro, sono dati altrettanti altri punti e altre tangenti, ugualmente distanti dal centro dall’altra parte di esso. L’asintoto, poi, si deve considerare come una tangente, e il suo estremo infinitamente distante (se è lecito parlare così) come il punto di contatto. Immagina che il punto di contatto di una tangente qualsiasi se ne vada all’infinito: la tangente si muterà in asintoto, e le costruzioni dei problemi precedenti si muteranno nelle costruzioni in cui sono dati gli asintoti.

**[S5.66]** Dopo che la traiettoria è stata descritta, se ne possono trovare gli assi e i fuochi con questo metodo. Nella costruzione e nella figura del Lemma XXI fa’ in modo che i bracci BP, CP degli angoli mobili PBN, PCN, con il cui incontro si descriveva la traiettoria, siano paralleli fra loro e, conservando questa posizione, ruotino intorno ai loro poli B, C in quella figura. Intanto gli altri bracci CN, BN di quegli angoli descrivano con il loro punto d’incontro K, o k, il cerchio BGKC. Sia O il centro di questo cerchio. Da questo centro abbassa sulla riga MN, sulla quale quegli altri bracci CN, BN si incontravano mentre si descriveva la traiettoria, la perpendicolare OH, che incontri il cerchio in K e L. Quando quegli altri bracci CK, BK si incontrano nel punto K, quello più vicino alla riga, i primi bracci CP, BP saranno paralleli all’asse maggiore e perpendicolari al minore; e avverrà il contrario se gli stessi bracci si incontrano nel punto più lontano L. Perciò, se è dato il centro della traiettoria, saranno dati gli assi. E, dati questi, i fuochi si hanno subito.

**[S5.67]** I quadrati degli assi, poi, stanno fra loro come KH sta a LH; e di qui è facile descrivere una traiettoria data di forma per quattro punti dati. Infatti, se due dei punti dati si assumono come poli C, B, il terzo darà gli angoli mobili PCK, PBK; e, dati questi, si può descrivere il cerchio BGKC. Poi, poiché la traiettoria è data di forma, sarà dato il rapporto di OH a OK, e quindi la stessa OH. Con centro O e raggio OH descrivi un altro cerchio: la retta che tocca questo cerchio e passa per il punto d’incontro dei bracci CK, BK, quando i primi bracci CP, BP si incontrano nel quarto punto dato, sarà la riga MN per mezzo della quale si descriverà la traiettoria. Di qui, inversamente, si può anche inscrivere in una qualsiasi sezione conica data un trapezio dato di forma (se si eccettuano alcuni casi impossibili).

**[S5.68]** Vi sono anche altri lemmi per mezzo dei quali si possono descrivere traiettorie date di forma, dati dei punti e delle tangenti. Di questo genere è il seguente: se per un punto qualsiasi dato di posizione si conduce una linea retta che tagli una sezione conica data in due punti, e l’intervallo fra le intersezioni si divide a metà, il punto di bisezione si troverà su un’altra sezione conica della stessa forma della prima, con gli assi paralleli agli assi della prima. Ma mi affretto verso cose più utili.

### Lemma XXVI (porre i vertici di un triangolo dato su tre rette date)

**[S5.69]** **Porre i tre angoli di un triangolo dato di forma e di grandezza su altrettante rette date di posizione, non tutte parallele, ciascun angolo su ciascuna retta.**

**[S5.70]** Sono date di posizione tre rette infinite AB, AC, BC, e bisogna collocare il triangolo DEF in modo che il suo angolo D tocchi la linea AB, l’angolo E la linea AC e l’angolo F la linea BC. Su DE, DF ed EF descrivi tre segmenti di cerchio DRE, DGF, EMF, che siano capaci di angoli uguali rispettivamente agli angoli BAC, ABC, ACB. Questi segmenti siano descritti da quella parte delle linee DE, DF, EF per cui le lettere DRED girino in cerchio nello stesso ordine delle lettere BACB, le lettere DGFD nello stesso ordine delle lettere ABCA e le lettere EMFE nello stesso ordine delle lettere ACBA; poi si completino questi segmenti in cerchi interi. I primi due cerchi si taglino a vicenda in G, e siano P e Q i loro centri. Congiunte GP, PQ, prendi Ga che stia ad AB come GP sta a PQ, e con centro G e raggio Ga descrivi un cerchio che tagli il primo cerchio DGE in a. Si congiungano aD, che tagli il secondo cerchio DFG in b, e aE, che tagli il terzo cerchio EMF in c. Ora si può costruire la figura ABCdef simile e uguale alla figura abcDEF. Fatto ciò, il problema è risolto.

**[S5.71]** Si conduca infatti Fc, che incontri aD in n, e si congiungano aG, bG, QG, QD, PD. Per costruzione l’angolo EaD è uguale all’angolo CAB e l’angolo acF all’angolo ACB, e perciò il triangolo anc è equiangolo al triangolo ABC. Dunque l’angolo anc, ossia FnD, è uguale all’angolo ABC, e quindi all’angolo FbD; e perciò il punto n cade sul punto b. Inoltre l’angolo GPQ, che è la metà dell’angolo al centro GPD, è uguale all’angolo alla circonferenza GaD; e l’angolo GQP, che è la metà dell’angolo al centro GQD, è uguale al complemento a due retti dell’angolo alla circonferenza GbD, e quindi è uguale all’angolo Gba; perciò i triangoli GPQ, Gab sono simili, e Ga sta ad ab come GP sta a PQ, cioè (per costruzione) come Ga sta ad AB. Sono dunque uguali ab e AB; e perciò i triangoli abc, ABC, che abbiamo appena provato essere simili, sono anche uguali. Perciò, poiché inoltre gli angoli D, E, F del triangolo DEF toccano rispettivamente i lati ab, ac, bc del triangolo abc, si può completare la figura ABCdef simile e uguale alla figura abcDEF, e completandola si risolverà il problema. C.V.F.

**[S5.72]** Cor. Di qui si può condurre una retta le cui parti, date di lunghezza, saranno comprese fra tre rette date di posizione. Immagina che il triangolo DEF, mentre il punto D si avvicina al lato EF e i lati DE, DF si dispongono in linea retta, si muti in una linea retta la cui parte data DE deve essere interposta fra le rette AB, AC date di posizione, e la parte data DF fra le rette AB, BC date di posizione: applicando a questo caso la costruzione precedente si risolverà il problema.

### Proposizione XXVIII. Problema XX (traiettoria data di forma e di grandezza, tagliata da tre rette date)

**[S5.73]** **Descrivere una traiettoria data di forma e di grandezza, le cui parti date saranno comprese fra tre rette date di posizione.**

**[S5.74]** Si debba descrivere una traiettoria che sia simile e uguale alla linea curva DEF e che sia tagliata dalle tre rette AB, AC, BC, date di posizione, in parti simili e uguali alle parti date DE ed EF di questa.

**[S5.75]** Conduci le rette DE, EF, DF e poni gli angoli D, E, F di questo triangolo DEF su quelle rette date di posizione (per il Lemma XXVI); poi intorno al triangolo descrivi una traiettoria simile e uguale alla curva DEF. C.V.F.

### Lemma XXVII (porre i vertici di un trapezio dato di forma su quattro rette date)

**[S5.76]** **Descrivere un trapezio dato di forma i cui angoli stiano, ciascuno su ciascuna, su quattro rette date di posizione, che non siano tutte parallele né convergano in un punto comune.**

**[S5.77]** Siano date di posizione quattro rette ABC, AD, BD, CE, delle quali la prima tagli la seconda in A, la terza in B e la quarta in C; e si debba descrivere un trapezio fghi simile al trapezio FGHI, il cui angolo f, uguale all’angolo dato F, tocchi la retta ABC, e gli altri angoli g, h, i, uguali agli altri angoli dati G, H, I, tocchino rispettivamente le altre linee AD, BD, CE. Si congiunga FH, e su FG, FH, FI si descrivano altrettanti segmenti di cerchio FSG, FTH, FVI, dei quali il primo, FSG, sia capace di un angolo uguale all’angolo BAD, il secondo, FTH, di un angolo uguale all’angolo CBD, e il terzo, FVI, di un angolo uguale all’angolo ACE. I segmenti devono poi essere descritti da quella parte delle linee FG, FH, FI per cui l’ordine circolare delle lettere FSGF sia lo stesso delle lettere BADB, e le lettere FTHF girino in cerchio nello stesso ordine delle lettere CBDC, e le lettere FVIF nello stesso ordine delle lettere ACEA. Si completino i segmenti in cerchi interi, e sia P il centro del primo cerchio FSG e Q il centro del secondo FTH. Si congiunga PQ e la si prolunghi da entrambe le parti, e su di essa si prenda QR che abbia con PQ il rapporto che BC ha con AB. QR si prenda poi da quella parte del punto Q per cui l’ordine delle lettere P, Q, R sia lo stesso delle lettere A, B, C; e con centro R e raggio RF si descriva un quarto cerchio FNc, che tagli il terzo cerchio FVI in c. Si congiunga Fc, che tagli il primo cerchio in a e il secondo in b. Si conducano aG, bH, cI: si può costruire la figura ABCfghi simile alla figura abcFGHI. Fatto ciò, il trapezio fghi sarà proprio quello che si doveva costruire.

**[S5.78]** I primi due cerchi FSG, FTH si taglino infatti a vicenda in K. Si congiungano PK, QK, RK, aK, bK, cK, e si prolunghi QP fino a L. Gli angoli alle circonferenze FaK, FbK, FcK sono la metà degli angoli al centro FPK, FQK, FRK, e quindi sono uguali alle metà di quegli angoli, LPK, LQK, LRK. La figura PQRK è dunque equiangola e simile alla figura abcK, e perciò ab sta a bc come PQ sta a QR, cioè come AB sta a BC. Inoltre, per costruzione, agli angoli FaG, FbH, FcI sono uguali gli angoli fAg, fBh, fCi. Dunque si può completare la figura ABCfghi simile alla figura abcFGHI. Fatto ciò, il trapezio fghi risulterà simile al trapezio FGHI e con i suoi angoli f, g, h, i toccherà le rette ABC, AD, BD, CE. C.V.F.

**[S5.79]** Cor. Di qui si può condurre una retta le cui parti, comprese in un ordine dato fra quattro rette date di posizione, avranno fra loro una proporzione data. Si aumentino gli angoli FGH, GHI fino a che le rette FG, GH, HI giacciano in linea retta: costruendo il problema in questo caso si condurrà una retta fghi, le cui parti fg, gh, hi, comprese fra le quattro rette date di posizione AB e AD, AD e BD, BD e CE, staranno fra loro come le linee FG, GH, HI e conserveranno fra loro lo stesso ordine. Ma lo stesso si fa più speditamente così.

**[S5.80]** Si prolunghino AB fino a K e BD fino a L, in modo che BK stia ad AB come HI sta a GH, e DL stia a BD come GI sta a FG; e si congiunga KL, che incontri la retta CE in i. Si prolunghi iL fino a M, in modo che LM stia a iL come GH sta a HI, e si conducano MQ, parallela a LB, che incontri la retta AD in g, e gi, che tagli AB, BD in f, h. Dico che è fatto.

**[S5.81]** Mg tagli infatti la retta AB in Q, e AD tagli la retta KL in S; si conduca AP parallela a BD, che incontri iL in P: gM starà a Lh (gi a hi, Mi a Li, GI a HI, AK a BK) e AP a BL nello stesso rapporto. Si divida DL in R in modo che DL stia a RL in quello stesso rapporto; e, poiché gS sta a gM, AS ad AP e DS a DL in proporzione, per uguaglianza come gS sta a Lh così AS sta a BL e DS a RL; e, in modo misto, BL − RL sta a Lh − BL come AS − DS sta a gS − AS. Cioè BR sta a Bh come AD sta ad Ag, e quindi come BD sta a gQ. E, permutando, BR sta a BD come Bh sta a gQ, ossia come fh sta a fg. Ma per costruzione la linea BL è stata divisa in D e R nello stesso rapporto in cui la linea FI è divisa in G e H; e perciò BR sta a BD come FH sta a FG. Dunque fh sta a fg come FH sta a FG. Poiché dunque anche gi sta a hi come Mi sta a Li, cioè come GI sta a HI, è evidente che le linee FI, fi sono divise in modo simile in g e h, G e H. C.V.F.

**[S5.82]** Nella costruzione di questo corollario, dopo aver condotto LK, che taglia CE in i, si può prolungare iE fino a V, in modo che EV stia a Ei come FH sta a HI, e condurre Vf parallela a BD. Si torna allo stesso se con centro i e raggio IH si descrive un cerchio che tagli BD in X, si prolunga iX fino a Y in modo che iY sia uguale a IF, e si conduce Yf parallela a BD.

**[S5.83]** Altre soluzioni di questo problema furono escogitate un tempo da Wren e da Wallis.

### Proposizione XXIX. Problema XXI (traiettoria data di forma, tagliata da quattro rette date in parti date)

**[S5.84]** **Descrivere una traiettoria data di forma che sia tagliata da quattro rette date di posizione in parti date per ordine, per forma e per proporzione.**

**[S5.85]** Si debba descrivere una traiettoria che sia simile alla linea curva FGHI e le cui parti, simili e proporzionali alle parti FG, GH, HI di quella, siano comprese fra le rette AB e AD, AD e BD, BD e CE, date di posizione: la prima fra le prime, la seconda fra le seconde, la terza fra le terze. Condotte le rette FG, GH, HI, FI, si descriva (per il Lemma XXVII) un trapezio fghi simile al trapezio FGHI, i cui angoli f, g, h, i tocchino quelle rette date di posizione AB, AD, BD, CE, ciascuno ciascuna nell’ordine detto. Poi intorno a questo trapezio si descriva una traiettoria simile alla linea curva FGHI.

#### Scolio

**[S5.86]** Questo problema si può costruire anche come segue. Congiunte FG, GH, HI, FI, prolunga GF fino a V, congiungi FH, IG, e fa’ gli angoli CAK, DAL uguali agli angoli FGH, VFH. AK, AL incontrino la retta BD in K e L, e di qui si conducano KM, LN: KM formi l’angolo AKM uguale all’angolo GHI e stia ad AK come HI sta a GH; LN formi l’angolo ALN uguale all’angolo FHI e stia ad AL come HI sta a FH. AK, KM, AL, LN si conducano poi da quella parte delle linee AD, AK, AL per cui le lettere CAKMC, ALKA, DALND girino in cerchio nello stesso ordine delle lettere FGHIF; e MN, una volta condotta, incontri la retta CE in i. Fa’ l’angolo iEP uguale all’angolo IGF, e PE stia a Ei come FG sta a GI; per P si conduca PQf, che con la retta ADE formi l’angolo PQE uguale all’angolo FIG e incontri la retta AB in f; e si congiunga fi. PE e PQ si conducano poi da quella parte delle linee CE, PE per cui l’ordine circolare delle lettere PEiP e PEQP sia lo stesso delle lettere FGHIF; e se sulla linea fi, ancora con lo stesso ordine delle lettere, si costruisce un trapezio fghi simile al trapezio FGHI e gli si circoscrive una traiettoria data di forma, il problema sarà risolto.

**[S5.87]** Fin qui del modo di trovare le orbite. Resta da determinare i moti dei corpi nelle orbite trovate.

**Fine della Sezione V. Nel testo originale segue la Sezione VI, *De inventione motuum in orbibus datis*.**

---

## Apparato

### A.0 Estensioni del glossario

I termini seguenti non comparivano nel glossario comune. Ognuno è reso in modo costante in tutto il fascicolo.

| Latino | Italiano | Motivazione |
|---|---|---|
| *trapezium* | «trapezio» | Per Newton (e per la tradizione euclidea) è un quadrilatero qualsiasi; il Lemma XVII lo inscrive in una conica, senza lati paralleli. Si conserva il termine storico, chiarito in A.1 e N2. |
| *rectangulum* (PQ × PR, PQK, AQB) | «rettangolo» | È il prodotto di due segmenti pensato come area. «Rettangolo PQK» = PQ × QK, come in Euclide. |
| *tangere* detto di un punto mobile (*punctum P … tanget conicam sectionem*); *contingere* | «trovarsi su», «stare su» | Il punto descrive la curva, non le è tangente. Quando il soggetto è una retta (*recta … tangat lineam curvam*) si traduce «toccare». Nel Lemma XX il parallelogramma «tocca con due angoli» la conica: si conserva «toccare» (A.4). |
| *polus*, *poli* | «polo», «poli» | Punti fissi intorno ai quali ruotano rette o angoli (Lemma XXI, Prop. XXII). Nel Lemma XXII *polus* è il centro O della trasformazione. |
| *crus*, *crura* | «braccio», «bracci» | I lati di un angolo mobile (Prop. XXII, XXIII, Scolio). |
| *regula* | «riga» | La retta MN su cui scorre il punto d’incontro dei bracci (Scolio dopo la Prop. XXVII). |
| *radius* (Prop. XXIII; Lemma XXII) | «raggio» | Retta mobile intorno a un polo; nel Lemma XXII: *radius abscindens* «raggio secante», *radius ordinatus primus / novus* «primo / nuovo raggio ordinato». |
| *ordinata prima / nova*; *abscissa prima / nova* | «prima / nuova ordinata»; «prima / nuova ascissa» | Lessico del Lemma XXII, distinto da *abscissæ partes* dei Lemmi XX e XXV. |
| *abscindere*, *partes abscissæ* (Lemmi XX, XXV) | «staccare», «parti staccate» | Segmenti tagliati su un lato fra un vertice e una retta: non sono ascisse. |
| *media proportionalis* | «media proporzionale» | Il segmento x con a : x = x : b, cioè x² = ab. |
| *latus quadratum* | «lato quadrato» | Il lato del quadrato uguale a un rettangolo dato: la radice quadrata dell’area (Prop. XXV). |
| *continue proportionales* | «in proporzione continua» | a : b = b : c. |
| *vicissim* (nelle proporzioni) | «permutando» | Scambio dei medi; nell’uso non tecnico (S5.67) «inversamente». |
| *divisim*, *dividendo* | «separando» | Da a : b = c : d a (a − b) : b = (c − d) : d. |
| *componendo*, *composite* | «componendo» | Da a : b = c : d a (a + b) : b = (c + d) : d; per i rapporti composti, prodotto dei rapporti. |
| *ex æquo*, *ex æquo perturbate* | «per uguaglianza», «per uguaglianza perturbata» | Termini euclidei (Elementi V, def. 17–18). |
| *mixtim* | «in modo misto» | Combinazione di componendo e separando (Lemma XXVII, Cor.). |
| *applicare terminos ad terminos* | «dividere i termini per i termini» | Nel linguaggio dell’applicazione delle aree (Lemma XVIII). |
| *auferre / addere rationem* | «togliere / aggiungere un rapporto» | Dividere per / comporre con un rapporto (Lemma XIX). Si conserva il lessico storico; spiegazione in N4. |
| *ex conicis*; *ex natura sectionum conicarum* | «per la teoria delle coniche»; «per la natura delle sezioni coniche» | Rimando generico ai risultati noti (Apollonio), senza citazione puntuale. |
| *segmentum circuli quod capiat angulum* | «segmento di cerchio capace di un angolo» | L’arco capace della geometria italiana (Lemmi XXVI, XXVII). |
| *in orbem redire* (delle lettere) | «girare in cerchio nello stesso ordine» | Regola di orientamento delle figure. |
| *linea tertii ordinis analytici* | «linea del terzo ordine analitico» | Curva algebrica di terzo grado (Lemma XXII). |
| *ascendere ad dimensiones* | «salire a … dimensioni» | Grado delle indeterminate nell’equazione. |
| *problema solidum / planum* | «problema solido / piano» | Classificazione antica: risolubile con coniche / con riga e compasso. |
| *asymptotos* | «asintoto» | Lo Scolio dopo la Prop. XXVII lo tratta come tangente con punto di contatto all’infinito. |
| *mechanice describere* | «descrivere meccanicamente» | Con un dispositivo di angoli rotanti (descrizione «organica»). |

### A.1 Lemma XVII

**Latino:** *Si a datæ conicæ sectionis puncto quovis P ad trapezii alicujus ABCD, in conica illa sectione inscripti, latera quatuor infinite producta AB, CD, AC, DB totidem rectæ PQ, PR, PS, PT in datis angulis ducantur, singulæ ad singula: rectangulum ductarum ad opposita duo latera PQ× PR, erit ad rectangulum ductarum ad alia duo latera opposita PS× PT in data ratione.*

**Inglese:** “If from any point P of a given conic section, to the four produced sides AB, CD, AC, DB, of any trapezium ABDC inscribed in that section, as many right lines PQ, PR, PS, PT are drawn in given angles, each line to each side; the rectangle PQ × PR of those on the opposite sides AB, CD, will be to the rectangle PS × PT of those on the other two opposite sides AC, BD, in a given ratio.”

**Scelte e divergenze.**

- *trapezium* è reso «trapezio», ma per Newton è un **quadrilatero qualsiasi** (qui inscritto nella conica), non il trapezio della geometria scolastica italiana con due lati paralleli. Vedi § A.0.
- Il latino nomina il trapezio **ABCD** e i lati AB, CD, AC, DB: i vertici, in ordine di perimetro, sono dunque A, B, D, C. Motte scrive «trapezium **ABDC**», cioè nomina i vertici nell’ordine del perimetro; aggiunge inoltre, fra parentesi esplicative, «on the opposite sides AB, CD» e «AC, BD», che il latino lascia impliciti.
- *in datis angulis ducantur, singulæ ad singula*: «si conducono, sotto angoli dati, … una a ciascun lato». *rectangulum ductarum* è «il rettangolo delle rette condotte».
- Caso 1: l’uguaglianza AQB = PS × PT, che Newton dà con «hoc est», segue dal fatto che PS = AQ e PT = QB (lati opposti di parallelogrammi, perché PS, PT ∥ AB e PQ ∥ AC ∥ BD). Le citazioni di Apollonio (*Coniche* III, 17, 19, 21, 23) non sono state controllate sul testo di Apollonio.
- Caso 2: *ducendo antecedentes in antecedentes* è «moltiplicando gli antecedenti per gli antecedenti» (glossario: *ducere in*); *divisim* è «separando» (§ A.0). Il passaggio «per il Caso 1» applica il Caso 1 al quadrilatero A, B, d, C, che ha AC ∥ Bd.
- Caso 3: la trascrizione ha virgole spurie in «PR, ad Pr, PS, ad Ps»; si traduce secondo il senso.

### A.2 Lemma XVIII, corollario e scolio

**Latino:** *Iisdem positis, si rectangulum ductarum ad opposita duo latera trapezii PQ×PR sit ad rectangulum ductarum ad reliqua duo latera PS×PT in data ratione; punctum P, a quo lineæ ducuntur, tanget conicam sectionem circa trapezium descriptam.*

**Inglese:** “The same things supposed, if the rectangle PQ × PR of the lines drawn to the two opposite sides of the trapezium is to the rectangle PS × PT of those drawn to the other two sides in a given ratio, the point P, from whence those lines are drawn, will be placed in a conic section described about the trapezium.”

**Scelte e divergenze.**

- *punctum P … tanget conicam sectionem* è reso «si troverà su una sezione conica»: *tangere* detto di un punto mobile significa qui «stare su», non «essere tangente». Vedi § A.0.
- *applicando terminos prioris proportionis ad terminos correspondentes hujus*: nel linguaggio dell’applicazione delle aree *applicare* significa dividere. Motte traduce correttamente «by dividing».
- Corollario: la trascrizione ha *punctum P, a quibus rectæ ducuntur*; ci si aspetterebbe *a quo*. È forse un refuso della trascrizione o una svista dell’originale: da verificare sulla stampa. Si traduce «dal quale». Motte aggiunge «under any two of the lines drawn» e «in as many angles respectively given».
- Scolio: la trascrizione ha *si punctum p incidi in rectam*: *incidi* è un refuso probabile della trascrizione per *incidat*, da verificare sulla stampa. *in plagas parallelarum abibit in infinitum* è reso «se ne andrà all’infinito nella direzione delle parallele»; Motte: «will go the same way as the parallels in infinitum».

### A.3 Lemma XIX e corollari

**Latino:** *Invenire punctum P, a quo si rectæ quatuor PQ, PR, PS, PT ad alias totidem positione datas rectas AB, CD, AC, BD, singulæ ad singulas, in datis angulis ducantur, rectangulum sub duabus ductis, PQ×PR, sit ad rectangulum sub aliis duabus, PS ×PT, in data ratione.*

**Inglese:** “To find a point P from which if four right lines PQ, PR, PS, PT are drawn to as many other right lines AB, CD, AC, BD, given by position, each to each, at given angles, the rectangle PQ × PR, under any two of the lines drawn, shall be to the rectangle PS × PT, under the other two, in a given ratio.”

**Scelte e divergenze.**

- L’enunciato è all’infinito di problema (*Invenire*): «Trovare». La soluzione si chiude con Q.E.I., reso C.V.T.
- *Auferendo hanc a data ratione … addendo datas rationes*: nella teoria dei rapporti composti «togliere» un rapporto significa dividere per esso, «aggiungere» significa comporlo, cioè moltiplicare. Si conserva il lessico storico; vedi nota N4.
- Motte aggiunge «under any two of the lines drawn» nell’enunciato («sub duabus ductis»: «di due delle rette condotte»).
- Cor. 1: *ad Loci punctorum infinitorum P punctum quodvis D*: «in un punto qualsiasi D del luogo degli infiniti punti P»; Motte: «the locus of all the points P». *Loci* con l’iniziale maiuscola è nella trascrizione.
- Cor. 2: la trascrizione appiattisce la frazione *BGqAG*: va letta BG²/AG (Motte, SVG 108: BG²/AG). *latus transversum* è «lato trasverso» (glossario); Motte aggiunge «its diameter or». *Invenietur autem punctum F per lem. xix.* cita lo stesso lemma per numero; Motte: «by this Lemma».
- Paragrafo finale: Motte aggiunge «that **famous** Problem» e «not an **analytical** calculus»; il latino dice soltanto *problematis veterum* e *non calculus*.

### A.4 Lemma XX e corollari

**Latino:** *Si parallelogrammum quodvis ASPQ angulis duobus oppositis A & P tangit sectionem quamvis conicam in punctis A & P; & lateribus unius angulorum illorum infinite productis AQ, AS, occurrit eidem sectioni conicæ in B & C; a punctis autem occursuum B & C ad quintum quodvis sectionis conicæ punctum D agantur rectæ duæ BD, CD occurrentes alteris duobus infinite productis parallelogrammi lateribus PS, PQ in T & R: erunt semper abscissæ laterum partes PR & PT ad invicem in data ratione. Et contra, si partes illæ abscissæ sunt ad invicem in data ratione, punctum D tanget sectionem conicam per puncta quatuor A, B, C, P, transeuntem.*

**Inglese:** “If the two opposite angular points A and P of any parallelogram ASPQ touch any conic section in the points A and P; and the sides AQ, AS of one of those angles, indefinitely produced, meet the same conic section in B and C; and from, the points of concourse B and C to any fifth point D of the conic section, two right lines BD, CD are drawn meeting the two other sides PS, PQ of the parallelogram, indefinitely produced in T and R; the parts PR and PT, cut off from the sides, will always be one to the other in a given ratio. And vice versa, if those parts cut off are one to the other in a given ratio, the locus of the point D will be a, conic section passing through the four points A, B, C, P.”

**Scelte e divergenze.**

- *parallelogrammum … angulis duobus oppositis A & P tangit sectionem*: «tocca con due angoli opposti … nei punti A e P», cioè i vertici A e P stanno sulla conica. Si conserva «toccare» perché il soggetto è il parallelogramma e i vertici lo «toccano» con la curva; il senso non è quello di tangenza. Motte: «the two opposite angular points A and P … touch».
- *abscissæ laterum partes PR & PT*: «le parti PR e PT staccate dai lati». *abscindere* è reso «staccare»; vedi § A.0.
- Caso 1: *vicissim* è «permutando» (permutazione dei medi di una proporzione), come Motte «by permutation». La trascrizione ha *conjunctis rationibus sit rectangulum*: forse *fit*, da verificare sulla stampa; il senso è «risulta». Si traduce «Componendo i rapporti, il rettangolo … sta».
- Cor. 1: la trascrizione ha *& PT capiatur Pt*: manca probabilmente *in* («& [in] PT capiatur»), come intende Motte («in PT take»). La traduzione integra «[su]» tra parentesi quadre.
- Cor. 3: è il teorema per cui due coniche distinte hanno al più quattro punti comuni; il ragionamento usa il Cor. 2 (rapporto PR : PT fissato dal quinto punto O). Vedi nota N5.

### A.5 Lemma XXI

**Latino:** *Si rectæ duæ mobiles & infinitæ BM, CM per data puncta B, C, ceu polos ductæ, concursu suo M describant tertiam positione datam rectam MN; & aliæ duæ infinitæ rectæ BD, CD cum prioribus duabus ad puncta illa data B, C datos angulos MBD, MCD efficientes ducantur: dico quod hæ duæ BD, CD concursu suo D describent sectionem conicam per puncta B, C transeuntem. Et vice versa, si rectæ BD, CD concursu suo D describant sectionem conicam per data puncta B, C, A transeuntem, & sit angulus DBM semper æqualis angulo dato ABC, angulusque DCM semper æqualis angulo dato ACB: punctum M continget rectam positione datam.*

**Inglese:** “If two moveable and indefinite right lines BM, CM drawn through given points B, C, as poles, do by their point of concourse M describe a third right line MN given by position; and other two indefinite right lines BD, CD are drawn, making with the former two at those given points B, C, given angles, MBD, MCD: I say, that those two right lines BD, CD will by their point of concourse D describe a conic section passing through the points B, C. And, vice versa, if the right lines BD, CD do by their point of concourse D describe a conic section passing through the given points B, C, A, and the angle DBM is always equal to the given angle ABC, as well as the angle DCM always equal to the given angle ACB, the point M will lie in a right line given by position, as its locus.”

**Scelte e divergenze.**

- *ceu polos*: «come per due poli». *concursu suo M describant*: «descrivono con il loro punto d’incontro M».
- *punctum M continget rectam*: «si troverà su una retta» (§ A.0).
- *punctum D, perpetuus rectarum mobilium BT & CR concursus*: reso «il punto D, nel quale si incontrano in ogni istante le rette mobili BT e CR». Nella seconda parte *locus perpetuus* è «il luogo costante».
- Le pagine 81 e 82 cadono dentro frasi; i marcatori non spezzano parole.

### A.6 Proposizione XXII e scolio

**Latino:** *Trajectoriam per data quinque puncta describere.*

**Inglese:** “To describe a trajectory that shall pass through five given points.”

**Scelte e divergenze.**

- Prima costruzione: *novissime ductis TPS, PRQ (priorem priori & posteriorem posteriori)*: «le rette TPS, PRQ condotte per ultime (la prima con la prima e la seconda con la seconda)». La trascrizione ha *occurentes*: refuso probabile della trascrizione per *occurrentes*.
- La prima soluzione si chiude con Q.E.D., la seconda con Q.E.F.: le chiusure sono conservate come nel latino (C.V.D., C.V.F.). Motte fa lo stesso.
- Seconda costruzione: *crura* è reso «bracci» (§ A.0). La trascrizione ha *puncta ADP* senza virgole; Motte «A, D, P». La parola *punctum* è spezzata dal marcatore di pagina <83> («pun ctum»).
- Il punto L non è definito nel testo: è la posizione dell’intersezione dei bracci BL, CL quando i bracci BA, CA passano per A (cioè nella posizione iniziale degli angoli ABC, ACB). La lettura è ricavata dal testo («ubi punctum m accedit ad puncta L, M, N, punctum d … accedet ad puncta A, D, P»), non dalla figura.
- Scolio: *paulo simplicior* è «un poco più semplice»; Motte: «something more simple».

### A.7 Proposizione XXIII

**Latino:** *Trajectoriam describere, quæ per data quatour puncta transibit, & rectam contingent positione datam.*

**Inglese:** “To describe a trajectory that shall pass through four given points, and touch a right line given by position.”

**Scelte e divergenze.**

- L’enunciato della trascrizione ha due refusi: *quatour* per *quatuor* e *contingent* per *continget*. Refusi probabili della trascrizione, da verificare sulla stampa; si traduce secondo il senso.
- **Caso 1, errore di Motte.** Il latino dà la tangente HB, il punto di contatto B e «alia tria puncta **C, D, P**»; Motte scrive «**C, L, P**». Il punto D è usato subito dopo (BD, CD) in entrambi i testi: la L di Motte è un errore.
- **«Idem aliter», divergenza di Motte.** Il latino fa ruotare intorno al polo C *radius quilibet rectilineus & utrinque productus* ***DC***, «un raggio rettilineo qualsiasi DC». Motte scrive «the rectilinear radius **BC**» e omette *quilibet*. BC è un braccio dell’angolo che ruota intorno a B, non il raggio che ruota intorno a C: la lettura di Motte confonde i due elementi della costruzione.
- La trascrizione ha *pucta M, N* (refuso probabile per *puncta*) e *per <85> petuo* (parola spezzata dal marcatore di pagina).
- Caso 2: *ex conicis* è reso «per la teoria delle coniche» (§ A.0). *media proportionalis inter CG & GP* è «la media proporzionale fra CG e GP». La frase finale *Capi autem potest punctum A …* è un capoverso separato nel latino (S5.34); Motte la unisce al Caso 2.

### A.8 Proposizione XXIV

**Latino:** *Trajectoriam describere quæ transibit per data tria puncta, & rectas duas positione datas continget.*

**Inglese:** “To describe a trajectory that shall pass through three given points, and touch two right lines given by position.”

**Scelte e divergenze.**

- *Seca autem pro lubitu vel inter puncta K & H, I & L, vel extra eadem*: «Dividi a piacere o fra i punti … o fuori di essi». Motte: «either **within or** between the points K and H, I and L, or without them»: «within or» è un’aggiunta ridondante.
- **Formula di Motte.** Il latino ha *ut SI quad. ad SL quad.*; Motte 1846 stampa «as SI is to SL2», senza il quadrato su SI. È un refuso dell’edizione inglese (o della sua resa digitale): il rapporto successivo, IZ : LP = SI : SL, richiede i quadrati da entrambe le parti. Non ho controllato Motte 1729.
- *IZ media proportionalis inter IX & IY*: «IZ media proporzionale fra IX e IY», cioè IZ² = IX × IY.
- Ultimo capoverso (S5.37): *brevitatis gratia non immoror* è «per brevità, non mi trattengo».

### A.9 Lemma XXII

**Latino:** *Figuras in alias ejusdem generis figuras mutare.*

**Inglese:** “To transform figures into other figures of the same kind.”

**Scelte e divergenze.**

- *Figuras in alias ejusdem generis figuras mutare*: «Mutare figure in altre figure dello stesso genere». *genus* qui indica l’ordine analitico della curva (rette in rette, coniche in coniche).
- Nomi tecnici della costruzione (§ A.0): *ordinata prima / nova* «prima / nuova ordinata»; *abscissa prima / nova* «prima / nuova ascissa»; *polus* «polo»; *radius abscindens* «raggio secante» (OD, che stacca le ascisse sulla retta BL); *radius ordinatus primus / novus* «primo / nuovo raggio ordinato».
- Le formule della trascrizione sono appiattite: *OA×ABad* vale OA × AB/ad e *OA×dgad* vale OA × dg/ad (Motte, SVG 109 e 110, letti allo stesso modo).
- *ad unicam tantum dimensionem ascendunt*: «salgono a una sola dimensione», cioè compaiono al primo grado. *linea tertii ordinis analytici*: «linea del terzo ordine analitico».
- **Divergenza di Motte sulle parallele.** Il latino dice *lineæ autem parallelæ sunt, quæ nusquam concurrunt*: «parallele sono le linee che non si incontrano in alcun punto». Motte traduce «parallel lines are such as **tend to a point infinitely remote**». È un cambiamento di senso: la definizione euclidea del latino diventa in Motte la nozione di punto all’infinito. Motte aggiunge anche «if they are intricate».
- *solida problemata* e *plana problemata*: «problemi solidi» e «problemi piani», nel senso classico (risolubili con coniche, o con riga e compasso).

### A.10 Proposizione XXV

**Latino:** *Trajectoriam describere, quæ per data duo puncta transibit, & rectas tres continget positione datas.*

**Inglese:** “To describe a trajectory that shall pass through two given points, and touch three right lines given by position.”

**Scelte e divergenze.**

- *latus quadratum rectanguli ahb*: «il lato quadrato del rettangolo ahb», cioè il lato del quadrato uguale al rettangolo, √(ah × hb). Vedi § A.0. Motte: «the square root of the rectangle ahb».
- *in subduplicata illa ratione*: «nel rapporto subduplicato di quello» (glossario). *composite*: «componendo».
- *per prob. xiv.*: il Problema XIV è la Prop. XXII.
- **Errore di Motte.** Il latino dice: *Si punctorum a, b alterutrum cadit inter puncta* ***h, l*** *& alterum extra*. Motte: «If one of the points a, b, falls between the points **h, i**, and the other without the points h, l». I punti a, b stanno sulla retta hl: «h, i» è un errore.
- Sulla regola «fra / fuori» vedi la nota N10: nella verifica numerica la formula vale con i segmenti presi con il loro segno, e la posizione di a, b da sola non decide sempre la scelta.

### A.11 Proposizione XXVI

**Latino:** *Trajectoriam describere, quæ transibit per punctum datum, & rectas quatuor positione datas continget.*

**Inglese:** “To describe a trajectory that shall pass through a given point, and touch four right lines given by position.”

**Scelte e divergenze.**

- *tangentes binæ, quæ ad radium ordinatum concurrebant*: «le tangenti che a due a due concorrevano sul raggio ordinato».
- **Errore di Motte.** Il latino chiude con *describi potest trajectoria illa per* ***problema xvii***, cioè la Prop. XXV (Probl. XVII), che costruisce la traiettoria per due punti e tre tangenti. Motte scrive «by **Prop.** XVII», che rimanda a un’altra proposizione. Motte omette anche Q.E.F.
- La trascrizione ha *Sun <91> to* (parola spezzata dal marcatore di pagina).

### A.12 Lemma XXIII

**Latino:** *Si rectæ duæ positione datæ AC, BD ad data puncta A, B, terminentur, datamque habeant rationem ad invicem, & recta CD, qua puncta indeterminata C, D junguntur, secetur in ratione data in K: dico quod punctum K locabitur in recta positione data.*

**Inglese:** “If two right lines, as AC, BD given by position, and terminating in given points A, B, are in a given ratio one to the other, and the right line CD, by which the indetermined points C, D are joined is cut in K in a given ratio; I say, that the point K will be placed in a right line given by position.”

**Scelte e divergenze.**

- *rectæ duæ positione datæ AC, BD ad data puncta A, B terminentur*: le rette sono date di posizione, i segmenti AC, BD variano con C e D ma terminano nei punti fissi A, B.
- *specie dabitur triangulum EFC*: «il triangolo EFC sarà dato di forma» (glossario).
- Dalla dimostrazione risulta che F sta sulla retta BD (FD è uguale e parallelo a EG, che giace su BD): solo così EF = GD e il triangolo EFC non degenera. Il testo non lo dice esplicitamente; la lettura è confermata dalla verifica numerica (N12).
- Questo lemma e il suo corollario sono richiamati dal Cor. IV delle Leggi (Fascicolo 3, L19): vedi nota N12.

### A.13 Lemma XXIV

**Latino:** *Si rectæ tres tangant quamcunque coni sectionem, quarum duæ parallelæ sint ac dentur positione; dico quod sectionis semidiameter hisce duabus parallela, sit media proportionalis inter harum segmenta, punctis contactuum & tangenti tertiæ interjecta.*

**Inglese:** “If three right lines, two whereof are parallel, and given by position, touch any conic section; I say, that the semi-diameter of the section which is parallel to those two is a mean proportional between the segments of those two that are intercepted between the points of contact and the third tangent.”

**Scelte e divergenze.**

- *continue proportionales*: «in proporzione continua» (AF : CD = CD : BG).
- *ex natura sectionum conicarum*: «per la natura delle sezioni coniche». *divisim* «separando», *composite* «componendo», *ex æquo perturbate* «per uguaglianza perturbata» (§ A.0). Motte lascia in latino «ex æquo perturbatè».

### A.14 Lemma XXV

**Latino:** *Si parallelogrammi latera quatuor infinite producta tangant sectionem quamcunque conicam, & abscindatur ad tangentem quamvis quintam; sumantur autem laterum quorumvis duorum conterminorum abscissæ terminatæ ad angulos oppositos parallelogrammi: dico quod abscissa alterutra sit ad latus illud a quo est abscissa, ut pars lateris alterius contermini inter punctum contactus & latus tertium est ad abscissarum aletram.*

**Inglese:** “If four sides of a parallelogram indefinitely produced touch any conic section, and are cut by a fifth tangent; I say, that, taking those segments of any two conterminous sides that terminate in opposite angles of the parallelogram, either segment is to the side from which it is cut off as that part of the other conterminous side which is intercepted between the point of contact and the third side is to the other segment.”

**Scelte e divergenze.**

- L’enunciato della trascrizione ha *& abscindatur ad tangentem quamvis quintam*: la costruzione è insolita (ci si aspetterebbe *abscindantur a tangente*). Si traduce secondo il senso, «e sono tagliati da una quinta tangente qualsiasi», come Motte («and are cut by a fifth tangent»). Lettura incerta, da verificare sulla stampa. Nella stessa frase *aletram* è un refuso probabile della trascrizione per *alteram*.
- *abscissæ* (plurale, sostantivo) indica qui le **parti staccate** sui lati, non le ascisse di un sistema di coordinate; per evitare confusione con il Lemma XXII si rende «parti staccate» (§ A.0).
- Il parallelogramma è nominato MLIK, ma i lati sono ML, IK, KL, MI: i vertici in ordine di perimetro sono M, L, K, I. Il Cor. 1 lo chiama IKLM.
- Nella dimostrazione la trascrizione apre una parentesi che non chiude: *ut (BK seu AM ad AF*; va letto *(BK seu) AM*, come in Motte. Il latino cita *per corollarium lemmatis superioris*; Motte precisa «Cor. 1».
- Cor. 1: *parallelogramum* e *rectangulla* sono refusi probabili della trascrizione. Cor. 3: *punca* per *puncta*.

### A.15 Proposizione XXVII

**Latino:** *Trajectoriam describere, quæ rectas quinque positione datas continget.*

**Inglese:** “To describe a trajectory that may touch five right lines given by position.”

**Scelte e divergenze.**

- *diagonales (ut ita dicam) BD, GF*: «le diagonali (per così dire)»: il quadrilatero BGDF formato da quattro tangenti è in generale intrecciato, e BD, GF non sono diagonali nel senso ordinario.
- *per construct. prob. xiv.*: «con la costruzione del Probl. XIV» (Prop. XXII). La trascrizione ha *dia <95> gonales*.

### A.16 Scolio dopo la Prop. XXVII

**Incipit latino:** *Problemata, ubi dantur trajectoriarum vel centra vel asymptoti, includuntur in præcedentibus.* (lo scolio non ha enunciato).

**Scelte e divergenze.**

- *Asymptotos … si ita loqui fas sit*: «se è lecito parlare così» (Motte: «if we may say so»).
- **Errore di Motte.** Il latino fa ruotare i bracci paralleli *circa polos suos* ***B, C***; Motte scrive «about their poles **P, C**». I poli della costruzione del Lemma XXI sono B e C.
- Il latino nomina il cerchio **BGKC**; Motte la prima volta scrive «BKGC», poi «BGKC». La trascrizione ha *trajectoia* (refuso probabile per *trajectoria*) e *in scribi* (per *inscribi*).
- *regula*: «riga» (la retta MN su cui scorre l’intersezione dei bracci). *vicissim* nell’ultima frase di S5.67 ha il senso comune di «inversamente», non quello tecnico di «permutando».
- *Axium vero quadrata sunt ad invicem ut KH ad LH*: l’ordine dei termini non è precisato; la verifica numerica (N15) mostra che il quadrato dell’asse minore sta al quadrato dell’asse maggiore come KH sta a LH.

### A.17 Lemma XXVI e corollario

**Latino:** *Trianguli specie & magnitudine dati tres angulos ad rectas totidem positione datas, quæ non sunt omnes parallelæ, singulos ad singulas ponere.*

**Inglese:** “To place the three angles of a triangle, given both in kind and magnitude, in respect of as many right lines given by position, provided they are not all parallel among themselves, in such manner that the several angles may touch the several lines.”

**Scelte e divergenze.**

- *segmenta … quæ capiant angulos … æquales*: «segmenti di cerchio capaci di angoli uguali» (l’arco capace della geometria italiana).
- *ut literæ DRED eodem ordine cum literis BACB … in orbem redeant*: «per cui le lettere DRED girino in cerchio nello stesso ordine delle lettere BACB»: è la regola dell’orientamento.
- *complemento ad duos rectos*: «complemento a due retti», cioè il supplemento.
- Motte riassume le due frasi *Et jam licet figuram … Quo facto perficitur problema* in «Complete the figure ABCdef … : I say, the thing is done».

### A.18 Proposizione XXVIII

**Latino:** *Trajectoriam specie & magnitudine datam describere, cujus partes datæ rectis tribus positione datis interjacebunt.*

**Inglese:** “To describe a trajectory given both in kind and magnitude, given parts of which shall be interposed between three right lines given by position.”

**Scelte e divergenze.**

- *specie & magnitudine datam*: «data di forma e di grandezza» (glossario).
- Il latino non dice come dalla curva DEF si ricavi il triangolo DEF: si congiungono gli estremi delle parti date (*Age rectas DE, EF, DF*).

### A.19 Lemma XXVII, corollario e aggiunte

**Latino:** *Trapezium specie datum describere, cujus anguli ad rectas quatuor positione datas, quæ neque omnes parallelæ sunt, neque ad commune punctum convergunt, singuli ad singulas consistent.*

**Inglese:** “To describe a trapezium given in kind, the angles whereof may be so placed, in respect of four right lines given by position, that are neither all parallel among themselves, nor converge to one common point, that the several angles may touch the several lines.”

**Scelte e divergenze.**

- La trascrizione ha *rapezium* (per *trapezium*), *adL* (senza spazio), *occurat* (per *occurrat*), *linas* (per *lineas*), *secansCE* (senza spazio): refusi probabili della trascrizione.
- *mixtim*: «in modo misto», cioè combinando le operazioni di componendo e separando sulla proporzione; Motte: «mixtly».
- Nel corollario il punto E non è definito nel testo. La variante *producere licet iE ad V … & agere Vf parallelam ipsi BD* funziona soltanto se E è l’intersezione di CE con BD: lo mostra la verifica numerica (N17). Nella Prop. XXIX (Scolio), invece, la retta è chiamata *ADE*, e lì E sta su AD. Le figure non sono disponibili; il punto resta da controllare sulle figure NATP00087-70 e -72.
- *Problematis hujus solutiones alias Wrennus & Wallisius olim excogitarunt*: «Altre soluzioni … furono escogitate un tempo da Wren e da Wallis». Motte aggiunge i titoli: «**Sir** Christopher Wren and **Dr.** Wallis».

### A.20 Proposizione XXIX e scolio

**Latino:** *Trajectoriam specie datam describere, quæ a rectis quatuor positione datis in partes secabitur, ordine, specie & proportione datas.*

**Inglese:** “To describe a trajectory given in kind, that may be cut by four right lines given by position, into parts given in order, kind, and proportion.”

**Scelte e divergenze.**

- *ordine, specie & proportione datas*: «date per ordine, per forma e per proporzione».
- La trascrizione ha *linæ* per *lineæ* (refuso probabile della trascrizione). La proposizione non si chiude con Q.E.F.
- Scolio: la retta *ADE* contiene E (vedi § A.19). Motte separa con un capoverso la prima frase della costruzione.

### A.21 Refusi e anomalie della trascrizione

Nessuno di questi punti è stato verificato sulla stampa del 1726 (non disponibile in questa sessione). La traduzione segue il senso; la Parte B conserva il latino della trascrizione così com’è.

| Luogo | Trascrizione | Lettura adottata | Natura |
|---|---|---|---|
| S5.02 | *coni <74> corum* | *conicorum* | parola spezzata dal marcatore di pagina |
| S5.04 | *PR, ad Pr, PS, ad Ps* | PR ad Pr, PS ad Ps | virgole spurie |
| S5.07 | *a quibus rectæ ducuntur* | *a quo* | concordanza anomala, da verificare |
| S5.08 | *si punctum p incidi* | *incidat* | refuso probabile |
| S5.12 | *BGqAG* | BG²/AG | frazione appiattita |
| S5.15 | *conjunctis rationibus sit* | forse *fit* | lettura incerta, senso invariato |
| S5.17 | *& PT capiatur Pt* | *& [in] PT capiatur Pt* | probabile caduta di *in* |
| S5.24 | *occurentes* | *occurrentes* | refuso probabile |
| S5.25 | *pun <83> ctum*; *ad puncta ADP* | *punctum*; A, D, P | parola spezzata; virgole mancanti |
| S5.29 | *quatour*; *contingent* | *quatuor*; *continget* | refusi probabili |
| S5.31 | *pucta*; *per <85> petuo* | *puncta*; *perpetuo* | refuso probabile; parola spezzata |
| S5.40 | *Por <88> ro*; *OA×ABad*, *OA×dgad* | *Porro*; OA × AB/ad, OA × dg/ad | parola spezzata; frazioni appiattite |
| S5.49 | *Sun <91> to* | *Sunto* | parola spezzata |
| S5.58 | *abscindatur ad tangentem*; *aletram* | «sono tagliati da una tangente»; *alteram* | costruzione incerta; refuso probabile |
| S5.59 | *(BK seu AM ad AF* | *(BK seu) AM ad AF* | parentesi non chiusa |
| S5.60 | *parallelogramum*; *rectangulla* | *parallelogrammum*; *rectangula* | refusi probabili |
| S5.62 | *punca* | *puncta* | refuso probabile |
| S5.64 | *dia <95> gonales* | *diagonales* | parola spezzata |
| S5.66 | *trajectoia* | *trajectoria* | refuso probabile |
| S5.67 | *in scribi* | *inscribi* | parola divisa |
| S5.77 | *rapezium* | *trapezium* | refuso probabile |
| S5.78 | *adL* | *ad L* | spazio mancante |
| S5.81 | *occurat*; *linas* | *occurrat*; *lineas* | refusi probabili |
| S5.82 | *secansCE* | *secans CE* | spazio mancante |
| S5.85 | *linæ* | *lineæ* | refuso probabile |

### A.22 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| S5.01 | *trapezii … ABCD*; lati senza specificazione | «trapezium ABDC»; «on the opposite sides AB, CD» | lettere riordinate; aggiunta esplicativa |
| S5.07, S5.09 | *sub duabus ductis* | «under any two of the lines drawn» | aggiunta |
| S5.12 | *per lem. xix.* | «by this Lemma» | riformulazione |
| S5.12 | *latus transversum* | «its diameter or latus transversum» | aggiunta |
| S5.13 | *problematis veterum*; *non calculus* | «that **famous** Problem»; «not an **analytical** calculus» | aggiunte |
| S5.30 | *alia tria puncta C, D, P* | «C, **L**, P» | **lettera errata** |
| S5.31 | *radius quilibet … DC* | «the rectilinear radius **BC**» | **lettere errate**; omesso *quilibet* |
| S5.34 | capoverso autonomo | unito al Caso 2 | tipografia |
| S5.36 | *vel inter … vel extra* | «either **within or** between … or without» | aggiunta ridondante |
| S5.36 | *SI quad. ad SL quad.* | «as SI is to SL2» | **formula errata** (manca SI²) |
| S5.43 | *parallelæ sunt, quæ nusquam concurrunt* | «such as tend to a point infinitely remote» | **cambiamento di senso** |
| S5.43 | *in simpliciores* | «if they are intricate, into others that are more simple» | aggiunta |
| S5.47 | *inter puncta h, l* | «between the points **h, i**» | **lettere errate** |
| S5.49 | *per problema xvii.* | «by **Prop.** XVII» | **rimando errato** (è la Prop. XXV) |
| S5.49 | *Q.E.F.* | — | omissione |
| S5.59 | *per corollarium lemmatis superioris* | «by Cor. 1 of the preceding Lemma» | precisazione corretta |
| S5.66 | *circa polos suos B, C* | «about their poles **P**, C» | **lettera errata** |
| S5.66 | *circulum BGKC* | «circle BKGC» (poi «BGKC») | lettere incoerenti |
| S5.70 | due frasi finali | fuse in «I say, the thing is done» | riassunto |
| S5.83 | *Wrennus & Wallisius* | «Sir Christopher Wren and Dr. Wallis» | aggiunta di titoli |
| S5.24, S5.55 | *Q.E.D.*; *ex æquo perturbate* | Q.E.D.; «ex æquo perturbatè» lasciato in latino | — |

Motte inserisce inoltre didascalie «[FIG: …]» che nell’estratto Gutenberg sono descrizioni moderne aggiunte all’EPUB, non testo di Motte: non sono state considerate.

---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. Le verifiche numeriche sono state eseguite con script Python propri (`work/s5/v1.py`–`v8.py`) su figure di prova: di norma l’ellisse x²/9 + y²/4 = 1, talvolta trasformata con una mappa affine, e rette e punti scelti a caso. «Verificato» significa: uguaglianza dei valori fino a 10⁻⁹ o meglio.

### N1. Che cosa fa la Sezione V

Nelle Sezioni II–IV Newton ha mostrato che una forza inversa al quadrato della distanza fa descrivere una conica con un fuoco nel centro delle forze, e ha costruito l’orbita quando è dato un fuoco. Qui affronta il problema in cui **nessuno dei due fuochi è dato** (*umbilicus neuter datur*): una conica va determinata da **cinque condizioni**, punti per cui passa o rette che tocca. I casi trattati coprono tutte le combinazioni: 5 punti (Prop. XXII), 4 punti + 1 tangente (XXIII), 3 + 2 (XXIV), 2 + 3 (XXV), 1 + 4 (XXVI), 5 tangenti (XXVII); seguono due problemi con traiettoria data di forma (XXVIII, XXIX). In termini moderni, una conica ha equazione ax² + bxy + cy² + dx + ey + f = 0, con cinque parametri indipendenti: per questo bastano cinque condizioni. Newton non usa l’algebra: costruisce con riga, compasso e rapporti, e introduce nel Lemma XXII una trasformazione che oggi diremmo **proiettiva**. Il collegamento con la fisica è esplicito solo nell’ultima frase (S5.87): trovate le orbite, resta da determinare il moto dei corpi lungo di esse (Sezione VI). La sezione è la più «geometrica pura» del Libro I; in una pagina didattica conviene presentarla come il problema di **ricostruire un’orbita da osservazioni di posizione**.

### N2. Lemma XVII: il luogo delle quattro rette

È il **luogo a quattro rette**, il «problema degli antichi» che Newton nomina in S5.13, visto dal lato diretto: per ogni punto P di una conica circoscritta al quadrilatero ABDC, il rapporto (PQ × PR) : (PS × PT) è costante. «Trapezio» indica qui un quadrilatero qualsiasi (§ A.0). Il Caso 1 usa le proprietà delle corde parallele (Apollonio, *Coniche* III, citate senza che io le abbia controllate); il Caso 2 riduce il caso generale al Caso 1 tramite il punto ausiliario d; il Caso 3 passa da direzioni parallele ai lati a direzioni qualsiasi, perché ogni rapporto PQ : Pq è fissato dagli angoli.

**Verifica numerica.** Quadrilatero inscritto nell’ellisse di prova, quattro direzioni con angoli dati diversi dai lati: su nove punti P dell’ellisse il rapporto vale sempre 0,788189; per un punto esterno vale 1,132. Il teorema è confermato anche nel caso generale del Caso 3.

### N3. Lemma XVIII, corollario e scolio

Il Lemma XVIII è l’inverso: il luogo dei punti con rapporto dato è una conica per A, B, C, D. Il corollario è il caso limite in cui due lati coincidono e due vertici si fondono: le rette AB, CD diventano tangenti in A e C, e il rapporto è PQ × PR : PS². **Verifica:** con due tangenti e la corda dei contatti, su quattro punti il rapporto vale sempre 1,743984.

Scolio: con un quadrilatero ciclico (angoli opposti supplementari), rette perpendicolari ai lati e PQ × PR = PS × PT, il luogo è un cerchio. **Verificato** sul cerchio di raggio 2: il rapporto vale 1 in quattro punti. Lo scolio include anche le coniche degeneri (coppie di rette): è l’uso «largo» del nome di sezione conica.

### N4. Lemma XIX: rapporti «tolti» e «aggiunti»; lato retto

Nella teoria classica i rapporti si compongono moltiplicandoli. «Togliere» il rapporto PQ : PS dal rapporto (PQ × PR) : (PS × PT) significa dividerlo, e resta PR : PT; «aggiungere» PI : PR e PT : PH significa moltiplicare, e si ottiene PI : PH. Poiché I e H sono fissi su AH, il rapporto PI : PH individua P. È la costruzione di un punto del luogo su ogni retta per A.

Cor. 2. Il luogo è una conica di cui AG è un diametro coniugato alla direzione della tangente in A; Newton dà il rapporto lato retto : lato trasverso = BG² : (AG × GH). **Verifica:** sull’ellisse di prova BG²/(AG × GH) = 1,022716, uguale a b′²/a′² (quadrato del semidiametro coniugato su quadrato del semidiametro AH/2), che è proprio il rapporto lato retto : lato trasverso; inoltre AH passa per il centro. Il paragrafo finale rivendica la soluzione «geometrica, quale gli antichi cercavano» del problema delle quattro linee; Newton contrappone la «composizione geometrica» a un «calcolo», senza nominare chi l’avesse risolto con il calcolo.

### N5. Lemma XX e Cor. 3: due coniche si tagliano in al più quattro punti

Il Lemma XX è un caso particolare del Lemma XVII con un parallelogramma ASPQ i cui vertici opposti A, P stanno sulla conica: il rapporto PR : PT è costante al variare di D. **Verifica:** su cinque punti D, PR/PT (con segno) = 0,745192 sempre; la costruzione del Cor. 1 dà una retta Bt parallela alla tangente in B.

Il Cor. 3 è notevole: **due coniche distinte non hanno più di quattro punti comuni**. Se ne avessero cinque, A, B, C, P, O, la retta BD taglierebbe le due curve in D e d; per il Cor. 2 i rapporti PR : PT e Pq : PT sarebbero uguali allo stesso rapporto fissato dal quinto punto, e dunque R = q: le due coniche coinciderebbero. Oggi è un caso del teorema di Bézout (2 × 2 = 4). Ne segue che **per cinque punti passa una sola conica**: è la base dell’unicità nella Prop. XXII.

### N6. Lemma XXI: la descrizione «organica» delle coniche

Due angoli di ampiezza fissa ruotano intorno a due poli B, C; se l’incontro M di due bracci scorre su una retta, l’incontro D degli altri due descrive una conica per B e C. È la cosiddetta **descrizione organica** delle coniche; si presta benissimo a un’animazione. **Verifica:** con poli e angoli arbitrari, sette posizioni di D stanno sulla conica individuata dalle prime cinque (residuo 10⁻¹³), che passa per B e C. La seconda parte del lemma (l’inverso) si appoggia al Cor. 3 del Lemma XX: se M descrivesse una curva, due coniche diverse avrebbero cinque punti comuni.

### N7. Proposizione XXII: la conica per cinque punti

Due costruzioni. La prima, «puntuale», usa il Lemma XX: ogni scelta di tr ∥ TR dà un nuovo punto d. La seconda, «organica», usa il Lemma XXI e traccia la curva con il moto continuo di due angoli. **Verifica:** per tre scelte di tr (anche con segmenti di verso opposto) il punto d sta sulla conica per i cinque punti dati; la variante dello Scolio (pe = Pr) dà anch’essa punti della conica in tre prove. Il Cor. 1 (tangente in B come limite di Bd) è la stessa idea dei rapporti ultimi del Lemma I.

### N8. Proposizione XXIII: quattro punti e una tangente

Caso 1: il punto di contatto B è dato; la costruzione è quella della Prop. XXII con A → B, cioè con la tangente al posto della corda AB (passaggio al limite dichiarato nel testo). Caso 2: il punto di contatto A va trovato. **Verifica:** con quattro punti dell’ellisse e la tangente in un quinto, il rapporto HA : IA ricavato dalla costruzione di Newton (prodotto di medie proporzionali) vale 0,5368869, uguale a quello reale. Il segno della divisione (A fra H e I oppure fuori) dà **due soluzioni**, come dice S5.34.

### N9. Proposizione XXIV: tre punti e due tangenti

La retta RS, che congiunge due punti costruiti con medie proporzionali, è la **corda dei contatti**. **Verifica:** con le tangenti in A e P all’ellisse di prova e tre altri punti, la retta RS passa per A e P quando R ed S sono presi entrambi **fuori** dei segmenti HK e IL. Con le altre tre scelte (dentro/fuori) RS taglia le tangenti in punti A′, P′ diversi, ma anche in quei casi la conica per B, C, D tangente in A′ e in P′ esiste ed è tangente a entrambe le rette: le quattro scelte «a piacere» di Newton danno **fino a quattro soluzioni**. L’osservazione S5.37 (le costruzioni valgono anche quando la retta XY non taglia la curva) anticipa un ragionamento che oggi si farebbe con i numeri complessi o con la continuità.

### N10. Lemma XXII e Proposizione XXV: la trasformazione proiettiva

Il Lemma XXII definisce una trasformazione del piano che manda rette in rette, coniche in coniche e tangenti in tangenti, e conserva il grado delle curve. In coordinate: con l’ascissa nuova ad e l’ordinata nuova dg si ha AD = OA × AB/ad e DG = OA × dg/ad, cioè x = k/x′, y = k·y′/x′: è una **trasformazione proiettiva** (omografia). Le rette per il punto d’incontro di due rette, scelto come «primo raggio ordinato», vanno all’infinito: rette concorrenti diventano parallele. **Verifica:** le due formule di Newton per AD e DG sono esatte; sette punti di una retta vanno in punti allineati; nove punti di un’ellisse vanno in punti di una stessa conica.

Prop. XXV. Dopo la trasformazione, due tangenti sono parallele (hi, kl) e la terza (ik) è parallela alla retta hl dei due punti dati. **Verifica:** con un’ellisse inscritta nel parallelogramma hikl, i quattro rapporti hc : √(ahb), ic : id, ke : kd, el : √(alb) sono uguali (0,728339), come afferma Newton. Il passaggio «componendo» al rapporto (hi + kl) : (√ahb + ik + √alb) vale invece soltanto quando c, d, e cadono **dentro** i segmenti hi, ik, kl (verificato: 0,680326 in un caso con tutti i punti interni); quando uno di essi cade fuori, la somma va fatta con i segni (verificato: con el sottratto il rapporto torna 0,728339). È ciò che Newton accenna con la regola «fra / fuori» di S5.47, che però, nelle prove, non dipende soltanto dalla posizione di a, b rispetto a h, l. Da segnalare nella pagina interattiva.

### N11. Proposizione XXVI: un punto e quattro tangenti

Dopo la trasformazione le quattro tangenti formano un parallelogramma hikl; la conica inscritta ha il centro nel centro O del parallelogramma, e il simmetrico q del punto dato p sta anch’esso sulla conica. Così il problema diventa: due punti e tre (anzi quattro) tangenti, cioè la Prop. XXV. Il rimando corretto è al Problema XVII (= Prop. XXV), non alla «Prop. XVII» di Motte.

### N12. Lemma XXIII e il Corollario IV delle Leggi

**Questo lemma, con il suo corollario, è quello richiamato nel Cor. IV delle Leggi** (Fascicolo 3, L19: *Hoc postea in lemmate XXIII ejusque corollario demonstratur, si punctorum motus fiant in eodem plano*). Lì Newton deve provare che, se due punti si muovono di moto uniforme lungo rette e la loro distanza è divisa in un rapporto dato, il punto di divisione è in quiete o si muove uniformemente in linea retta: è il primo passo della dimostrazione che il **centro di gravità comune** di un sistema non soggetto ad azioni esterne si muove di moto rettilineo uniforme.

Il collegamento: se C e D si muovono uniformemente lungo le rette AC e BD, e A, B sono le loro posizioni a uno stesso istante, le lunghezze AC e BD crescono proporzionalmente al tempo, dunque hanno **rapporto dato**. Il lemma dice che K, che divide CD in rapporto dato, sta su una retta data (HK); il **corollario** aggiunge che HK ha rapporto dato con EC, cioè con lo spazio percorso da C: dunque anche K percorre spazi proporzionali ai tempi, di moto uniforme. In notazione moderna: **r**_K = (1 − λ)**r**_C + λ**r**_D, combinazione lineare di due funzioni lineari del tempo, è a sua volta lineare nel tempo; con λ = m_D/(m_C + m_D) è il centro di massa. Il lemma tratta il caso piano; per moti non complanari il Cor. IV dice che vale «la stessa ragione».

**Verifica numerica.** Con A, B, direzioni e rapporti arbitrari (AC = s, BD = 0,7 s, CK : CD = 0,35), sette posizioni di K sono allineate e, per incrementi uguali di s, i passi di K sono uguali: il moto di K è rettilineo uniforme. Nella dimostrazione F deve stare sulla retta BD (vedi A.12).

Il lemma serve poi nel Cor. 3 del Lemma XXV (tre punti di mezzo allineati).

### N13. Lemma XXIV: tangenti parallele

AF × BG = CD²: il prodotto dei segmenti staccati su due tangenti parallele da una terza tangente è il quadrato del semidiametro parallelo. **Verifica:** per tre diverse tangenti all’ellisse di prova (tangenti parallele in (±3, 0)), AF × BG = 4,000 = CD² = b². Cor. 1: i quattro rapporti AF : BQ, AP : BG, FP : GQ, FO : OG coincidono (0,568498). Cor. 2: PG e FQ si incontrano sul diametro ACB (ordinata del punto d’incontro = 0).

### N14. Lemma XXV e Proposizione XXVII: la retta di Newton

Lemma XXV: **verificato** su un parallelogramma circoscritto a un’ellisse trasformata affinemente (ME : MI = BK : KQ; KH : KL = AM : MF; KQ × ME = KH × MF = 15,3337 costante per tre quinte tangenti diverse). Il Cor. 3 è il teorema oggi chiamato **retta di Newton**: in un quadrilatero circoscritto a una conica, i punti di mezzo delle diagonali e il centro della conica sono allineati. **Verifica:** allineamento e centro confermati.

Prop. XXVII: con cinque tangenti si scelgono due quadrilateri; le due rette di Newton si incontrano nel centro O. **Verifica:** con cinque tangenti a un’ellisse il centro costruito coincide con quello vero (0,5; −0,3), e la costruzione di R e OR dà esattamente il punto di contatto sulla tangente BCF.

### N15. Scolio dopo la Prop. XXVII: assi, fuochi, asintoti

Il primo capoverso riduce i casi con centro o asintoti dati ai precedenti (simmetria centrale; asintoto come tangente con contatto all’infinito). Il secondo trova la direzione degli assi con la costruzione del Lemma XXI: con i bracci BP, CP paralleli, l’incontro degli altri bracci descrive un cerchio per B e C; la perpendicolare dal centro O alla riga MN lo taglia in K (vicino) e L (lontano). **Verifica:** per un’ellisse descritta con il Lemma XXI, quando gli altri bracci si incontrano in K i bracci BP, CP sono paralleli all’asse **maggiore**, come dice Newton; e KH : LH = 0,190555 = (asse minore)² : (asse maggiore)². Per un’iperbole H cade fra K e L, e KH : LH = 0,3134 coincide con il rapporto dei quadrati dei semiassi in valore assoluto. L’ordine dei termini nella frase di Newton («i quadrati degli assi stanno come KH a LH») va quindi letto: minore al maggiore.

Ultimo capoverso: «il punto di mezzo delle corde per un punto fisso descrive una conica della stessa specie con assi paralleli». **Verifica:** i punti di mezzo di otto corde per un punto interno all’ellisse stanno su una conica con lo stesso rapporto dei coefficienti di x² e y² (0,4444) e senza termine in xy: stessa forma, assi paralleli.

### N16. Lemma XXVI e Proposizione XXVIII

Il Lemma XXVI colloca un triangolo dato con i vertici su tre rette date usando tre archi capaci; il punto G comune ai cerchi è quello che oggi si chiama **punto di Miquel**. **Verifica:** costruendo il problema «al contrario» (triangolo DEF con vertici su tre rette note), la costruzione di Newton ritrova esattamente A, B, C: Ga = GA (2,688965), b = B, c = C, e G sta anche sul terzo cerchio. La Prop. XXVIII ne è un’applicazione immediata: si colloca il triangolo delle corde DE, EF, DF e si circoscrive la curva data.

### N17. Lemma XXVII, corollario e Proposizione XXIX

Lemma XXVII: analogo al XXVI per un quadrilatero dato di forma. **Verifica:** la costruzione con il quarto cerchio di centro R dà c = C soltanto se R è preso dalla parte indicata da Newton (ordine P, Q, R come A, B, C); dall’altra parte no. La regola di orientamento non è quindi un dettaglio.

Corollario (retta divisa da quattro rette in parti proporzionali a FG, GH, HI). **Verifica** della costruzione rapida (K, L, i, M, g, f, h): su otto scelte di verso per i prolungamenti, due danno fg : gh : hi = FG : GH : HI (la scelta del verso su BD resta libera, ed è la doppia soluzione). La variante con V (EV : Ei = FH : HI, Vf ∥ BD) ritrova lo stesso f **solo se E è l’intersezione di CE con BD** e V è preso dalla parte opposta di i; la variante con il cerchio di centro i e raggio IH ritrova f per entrambe le intersezioni con BD. Poiché E non è definito nel testo del corollario, la lettura «E = CE ∩ BD» è dedotta dalla verifica e va controllata sulla figura NATP00087-70.

### N18. Riepilogo dei controlli numerici

| Unità | Proprietà controllata | Esito |
|---|---|---|
| Lemma XVII | rapporto costante su 9 punti | 0,788189 costante |
| Lemma XVIII, Cor., Scolio | luogo; caso tangente; cerchio | confermati |
| Lemma XIX, Cor. 2 | lato retto : lato trasverso = BG² : AG × GH | 1,022716 = 1,022716 |
| Lemma XX, Cor. 1 | PR : PT costante; tangente in B | confermati |
| Lemma XXI | D su una conica per B, C | residuo 10⁻¹³ |
| Prop. XXII e Scolio | d sulla conica per i 5 punti | 6 prove su 6 |
| Prop. XXIII, Caso 2 | HA : IA | 0,5368869 = 0,5368869 |
| Prop. XXIV | RS corda dei contatti; quattro soluzioni | confermati |
| Lemma XXII | formule AD, DG; rette → rette; coniche → coniche | confermati |
| Prop. XXV | uguaglianza dei quattro rapporti; somma composta | uguaglianza sì; somma solo con segni |
| Lemma XXIII + Cor. | K su una retta, moto uniforme | confermati |
| Lemma XXIV e Cor. | AF × BG = CD² | 4 = 4 (tre tangenti) |
| Lemma XXV e Cor. 3 | rapporti, prodotto costante, retta di Newton | confermati |
| Prop. XXVII | centro e punto di contatto | esatti |
| Scolio | assi: KH : LH; punti di mezzo delle corde | confermati (ellisse e iperbole) |
| Lemma XXVI | ritrovare A, B, C; punto di Miquel | confermati |
| Lemma XXVII e Cor. | quarto cerchio; costruzione rapida e varianti | confermati con le condizioni di N17 |

Non sono stati verificati numericamente: il Caso 1 del Lemma XVII nelle citazioni di Apollonio (verificato solo il risultato), la Prop. XXVI (conseguenza della XXV) e la costruzione dello Scolio della Prop. XXIX.

---

## Controllo della copertura

Gli identificatori seguono l’ordine del testo latino. Le pagine 1726 sono quelle dei marcatori della trascrizione (la sezione comincia a p. 73, prima del primo marcatore <74>); le pagine di Motte derivano dai marcatori dell’EPUB Gutenberg.

| Identificatore | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| S5.01 | *Si a datæ conicæ* | Lemma XVII | p. 73 | pp. 131–132 |
| S5.02 | *Cas. 1. Ponamus primo* | Lemma XVII, Caso 1 | pp. 73–74 | p. 132 |
| S5.03 | *Cas. 2. Ponamus jam* | Lemma XVII, Caso 2 | p. 74 | p. 132 |
| S5.04 | *Cas. 3. Ponamus denique* | Lemma XVII, Caso 3 | p. 74 | p. 132 |
| S5.05 | *Iisdem positis, si rectangulum* | Lemma XVIII | p. 75 | p. 132 |
| S5.06 | *Per puncta A, B,* | Lemma XVIII | p. 75 | p. 133 |
| S5.07 | *Corol. Hinc si rectæ* | Lemma XVIII, Cor. | pp. 75–76 | p. 133 |
| S5.08 | *Nomen conicæ sectionis in* | Lemma XVIII, Scolio | p. 76 | pp. 133–134 |
| S5.09 | *Invenire punctum P, a* | Lemma XIX | p. 77 | p. 134 |
| S5.10 | *Lineæ AB, CD, ad* | Lemma XIX | p. 77 | p. 134 |
| S5.11 | *Corol. 1. Hinc etiam* | Lemma XIX, Cor. 1 | p. 77 | p. 134 |
| S5.12 | *Corol. 2. Hinc etiam* | Lemma XIX, Cor. 2 | pp. 77–78 | pp. 134–135 |
| S5.13 | *Atque ita problematis veterum* | Lemma XIX, Cor. 2 (problema delle quattro linee) | p. 78 | p. 135 |
| S5.14 | *Si parallelogrammum quodvis ASPQ* | Lemma XX | p. 78 | p. 135 |
| S5.15 | *Cas. 1. Jungantur BP,* | Lemma XX, Caso 1 | p. 79 | p. 135 |
| S5.16 | *Cas. 2. Quod si* | Lemma XX, Caso 2 | p. 79 | p. 136 |
| S5.17 | *Corol. 1. Hinc si* | Lemma XX, Cor. 1 | p. 79 | p. 136 |
| S5.18 | *Corol. 2. Et vice* | Lemma XX, Cor. 2 | p. 79 | p. 136 |
| S5.19 | *Corol. 3. Conica sectio* | Lemma XX, Cor. 3 | pp. 79–80 | p. 136 |
| S5.20 | *Si rectæ duæ mobiles* | Lemma XXI | p. 80 | p. 136 |
| S5.21 | *Nam in recta MN* | Lemma XXI | pp. 80–81 | pp. 136–137 |
| S5.22 | *Et contra, si punctum* | Lemma XXI | pp. 81–82 | p. 137 |
| S5.23 | *Trajectoriam per data quinque* | Prop. XXII (enunciato) | p. 82 | p. 137 |
| S5.24 | *Dentur puncta quinque A,* | Prop. XXII | p. 82 | pp. 137–138 |
| S5.25 | *E punctis datis junge* | Prop. XXII, seconda costruzione | pp. 82–83 | p. 138 |
| S5.26 | *Corol. 1. Hinc recta* | Prop. XXII, Cor. 1 | p. 83 | p. 138 |
| S5.27 | *Corol. 2. Unde etiam* | Prop. XXII, Cor. 2 | p. 83 | p. 138 |
| S5.28 | *Constructio prior evadet paulo* | Prop. XXII, Scolio | pp. 83–84 | pp. 138–139 |
| S5.29 | *Trajectoriam describere, quæ per* | Prop. XXIII (enunciato) | p. 84 | p. 139 |
| S5.30 | *Cas. 1. Dentur tangens* | Prop. XXIII, Caso 1 | p. 84 | p. 139 |
| S5.31 | *Revolvatur tum angulus magnitudine* | Prop. XXIII, Caso 1, altra costruzione | pp. 84–85 | p. 139 |
| S5.32 | *Nam si in constructionibus* | Prop. XXIII, Caso 1, altra costruzione | p. 85 | p. 139 |
| S5.33 | *Cas. 2. Dentur puncta* | Prop. XXIII, Caso 2 | p. 85 | pp. 139–140 |
| S5.34 | *Capi autem potest punctum* | Prop. XXIII, Caso 2 | p. 85 | p. 140 |
| S5.35 | *Trajectoriam describere quæ transibit* | Prop. XXIV (enunciato) | p. 86 | p. 140 |
| S5.36 | *Dentur tangentes HI, KL* | Prop. XXIV | p. 86 | pp. 140–141 |
| S5.37 | *In hac propositione, &* | Prop. XXIV: osservazione sulle costruzioni | p. 87 | p. 141 |
| S5.38 | *Figuras in alias ejusdem* | Lemma XXII | p. 87 | p. 141 |
| S5.39 | *Transmutanda sit figura quævis* | Lemma XXII | p. 87 | p. 141 |
| S5.40 | *Dico jam quod, si* | Lemma XXII | pp. 87–88 | pp. 141–142 |
| S5.41 | *Dico præterea, quod si* | Lemma XXII | p. 88 | p. 142 |
| S5.42 | *Componi possent harum assertionum* | Lemma XXII | p. 88 | p. 142 |
| S5.43 | *Igitur si figura rectilinea* | Lemma XXII | p. 89 | pp. 142–143 |
| S5.44 | *Utile est etiam hoc* | Lemma XXII | p. 89 | p. 143 |
| S5.45 | *Trajectoriam describere, quæ per* | Prop. XXV (enunciato) | p. 89 | p. 143 |
| S5.46 | *Per concursum tangentium quarumvis* | Prop. XXV | pp. 89–90 | p. 143 |
| S5.47 | *Cæterum perinde ut puncta* | Prop. XXV | p. 90 | p. 144 |
| S5.48 | *Trajectoriam describere, quæ transibit* | Prop. XXVI (enunciato) | p. 90 | p. 144 |
| S5.49 | *Ab intersectione communi duarum* | Prop. XXVI | pp. 90–91 | p. 144 |
| S5.50 | *Si rectæ duæ positione* | Lemma XXIII | p. 91 | p. 144 |
| S5.51 | *Concurrant enim rectæ AC,* | Lemma XXIII | pp. 91–92 | pp. 144–145 |
| S5.52 | *Corol. Ob datam specie* | Lemma XXIII, Cor. | p. 92 | p. 145 |
| S5.53 | *Si rectæ tres tangant* | Lemma XXIV | p. 92 | p. 145 |
| S5.54 | *Sunto AF, GB parallelæ* | Lemma XXIV | p. 92 | p. 145 |
| S5.55 | *Nam si diametri conjugatæ* | Lemma XXIV | pp. 92–93 | p. 145 |
| S5.56 | *Corol. 1. Hinc si* | Lemma XXIV, Cor. 1 | p. 93 | p. 145 |
| S5.57 | *Corol. 2. Unde etiam* | Lemma XXIV, Cor. 2 | p. 93 | p. 145 |
| S5.58 | *Si parallelogrammi latera quatuor* | Lemma XXV | p. 93 | pp. 145–146 |
| S5.59 | *Tangant parallelogrammi MLIK latera* | Lemma XXV | pp. 93–94 | p. 146 |
| S5.60 | *Corol. 1. Hinc si* | Lemma XXV, Cor. 1 | p. 94 | p. 146 |
| S5.61 | *Corol. 2. Et si* | Lemma XXV, Cor. 2 | p. 94 | p. 146 |
| S5.62 | *Corol. 3. Unde etiam* | Lemma XXV, Cor. 3 | p. 94 | p. 146 |
| S5.63 | *Trajectoriam describere, quæ rectas* | Prop. XXVII (enunciato) | p. 94 | p. 146 |
| S5.64 | *Dentur positione tangentes ABG,* | Prop. XXVII | pp. 94–95 | pp. 146–147 |
| S5.65 | *Problemata, ubi dantur trajectoriarum* | Scolio: centri e asintoti | pp. 95–96 | p. 147 |
| S5.66 | *Postquam trajectoria descripta est,* | Scolio: assi e fuochi | p. 96 | pp. 147–148 |
| S5.67 | *Axium vero quadrata sunt* | Scolio: traiettoria data di forma per quattro punti | pp. 96–97 | p. 148 |
| S5.68 | *Sunt & alia lemmata* | Scolio: altri lemmi | p. 97 | p. 148 |
| S5.69 | *Trianguli specie & magnitudine* | Lemma XXVI | p. 97 | p. 148 |
| S5.70 | *Dantur positione tres rectæ* | Lemma XXVI | p. 97 | pp. 148–149 |
| S5.71 | *Agatur enim Fc ipsi* | Lemma XXVI | pp. 98–99 | p. 149 |
| S5.72 | *Corol. Hinc recta duci* | Lemma XXVI, Cor. | p. 99 | pp. 149–150 |
| S5.73 | *Trajectoriam specie & magnitudine* | Prop. XXVIII (enunciato) | p. 99 | p. 150 |
| S5.74 | *Describenda sit trajectoria, quæ* | Prop. XXVIII | p. 99 | p. 150 |
| S5.75 | *Age rectas DE, EF,* | Prop. XXVIII | p. 99 | p. 150 |
| S5.76 | *Trapezium specie datum describere,* | Lemma XXVII | p. 100 | p. 150 |
| S5.77 | *Dentur positione rectæ quatuor* | Lemma XXVII | pp. 100–101 | pp. 150–151 |
| S5.78 | *Secent enim circuli duo* | Lemma XXVII | p. 101 | p. 151 |
| S5.79 | *Corol. Hinc recta duci* | Lemma XXVII, Cor. | p. 101 | p. 151 |
| S5.80 | *Producantur AB ad K,* | Lemma XXVII, Cor.: costruzione rapida | p. 101 | p. 151 |
| S5.81 | *Secet enim Mg rectam* | Lemma XXVII, Cor.: dimostrazione | pp. 101–102 | p. 152 |
| S5.82 | *In constructione corollarii hujus* | Lemma XXVII, Cor.: varianti | p. 102 | p. 152 |
| S5.83 | *Problematis hujus solutiones alias* | Lemma XXVII: Wren e Wallis | p. 102 | p. 152 |
| S5.84 | *Trajectoriam specie datam describere,* | Prop. XXIX (enunciato) | p. 103 | p. 152 |
| S5.85 | *Describenda sit trajectoria, quæ* | Prop. XXIX | p. 103 | p. 152 |
| S5.86 | *Construi etiam potest hoc* | Prop. XXIX, Scolio | pp. 103–104 | pp. 152–153 |
| S5.87 | *Hactenus de orbibus inveniendis.* | Chiusura della Sezione V | p. 104 | p. 153 |

**Controlli eseguiti.**

1. **Copertura frase per frase.** La traduzione è stata costruita frase per frase sulla trascrizione: ogni frase latina è associata a una frase italiana, e uno script ha verificato che le frasi associate, concatenate nell’ordine, coprono l’intero testo latino della sezione dalla prima parola (*Si a datæ conicæ sectionis*) all’ultima (*determinemus*). Gli unici scarti sono i titoli (*SECTIO V*, *LEMMA XVII*, *Scholium*, *Idem aliter*, …), resi come intestazioni. Esito: nessuna frase omessa.
2. **Matematica.** Verifiche numeriche di tutti i lemmi e di tutte le proposizioni costruttive tranne la XXVI e lo Scolio della XXIX (nota N18). Esito: tutte le affermazioni controllate sono corrette; tre richiedono una lettura precisa (Prop. XXV, somma con i segni; Scolio, ordine KH : LH; Lemma XXVII, Cor., punto E).
3. **Confronto con Motte.** Tutta la sezione, pp. 131–153; divergenze in A.22. Le quattro formule SVG sono state rese e lette.
4. **Parte B.** `check.py` eseguito sul fascicolo con le fonti della Sezione V: JSON valido, tutte le stringhe `la` ed `en` sono sottostringhe esatte delle fonti, nessun avviso.

**Non ho potuto verificare:**

- la stampa del 1726 e le figure originali NATP00087-38…72: tutti i refusi di A.21 sono «probabili»; in particolare *a quibus* (S5.07), *sit / fit* (S5.15), *abscindatur ad tangentem* (S5.58);
- il punto E del corollario del Lemma XXVII (dedotto dalla verifica numerica, N17) e il punto L della seconda costruzione della Prop. XXII (dedotto dal testo);
- le proposizioni di Apollonio citate nel Lemma XVII;
- Motte 1729, per stabilire se gli errori di A.22 (C, L, P; BC; SL2; h, i; Prop. XVII; P, C) siano di Motte o dell’edizione 1846;
- la numerazione di pagina di Motte su un esemplare a stampa.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Sezione V: Lemmi XVII–XXVII, Prop. XXII–XXIX, corollari e scolii | **Fascicolo 7, presente documento, prima versione** |
| Refusi della trascrizione (A.21) | Da controllare sulla stampa 1726 |
| Figure NATP00087-38…72 | Da consultare: punto E (Lemma XXVII, Cor.), punto L (Prop. XXII), F su BD (Lemma XXIII), orientamenti dei Lemmi XXVI–XXVII |
| Errori di Motte 1846 (A.22) | Da confrontare con Motte 1729 |
| Rimando dal Fascicolo 3 (Cor. IV delle Leggi) | Collegato: nota N12; nella pagina del Cor. IV aggiungere il link alla pagina del Lemma XXIII |
| Pagine interattive candidate | Lemma XXI e Prop. XXII (descrizione organica, animazione); Lemma XXIII (moto uniforme del punto di divisione, legato al Cor. IV); Lemma XXV, Cor. 3 (retta di Newton); Lemma XXII (trasformazione proiettiva) |
| Prop. XXV | Nella pagina interattiva segnalare il problema dei segni (N10) |
| Revisione filologica e scientifica indipendente | Da eseguire, come previsto dalla skill di verifica |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce traduzioni italiane o inglesi moderne. **Licenza prevista**: testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project e non va ridistribuita finché non se ne chiariscono le condizioni d’uso; il testo di Motte (1846) è di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Unità incluse: ogni lemma e proposizione con figura e dimostrazione o costruzione (22 unità, 185 passi): Lemmi XVII–XXVII, Prop. XXII–XXIX, e i corollari con dimostrazione propria e figura (Lemma XIX, Cor. 2; Lemma XXV, Cor. 3; Lemma XXVII, Cor.). Non sono inclusi gli scolii e i corollari senza costruzione propria.

Convenzioni:

- `la`: testo latino esatto della trascrizione, compresi i refusi, segnalati in `nota`; i marcatori di pagina e di figura sono tolti, per cui le parole spezzate dal cambio di pagina restano separate;
- `it`: la traduzione di questo fascicolo;
- `en`: Motte 1846, allineato per senso; dove Motte usa una formula in immagine il testo ne è privo (segnalato in `nota`);
- `dipende_da`: soltanto i rimandi citati nella frase («per lem. xx» → "Lemma XX"; «ex conicis» → "Coniche (ex conicis)");
- per i corollari, l’enunciato è la prima frase e i passi sono le frasi successive.

```json
{
 "fascicolo": "07-L1-S5",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase (leggi, lemmi, proposizioni, corollari, casi, Apollonio, «ex conicis»)",
  "la": "",
  "en": "Motte 1846, allineato per senso; le formule stampate come immagine (SVG) mancano nel testo",
  "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione",
  "enunciato dei corollari": "per i corollari l'enunciato è la prima frase; i passi sono le frasi successive"
 },
 "unita": [
  {
   "id": "L1-Lem17",
   "tipo": "Lemma",
   "titolo": "Lemma XVII — rettangoli delle rette condotte ai lati di un trapezio inscritto",
   "copertura": [
    "S5.01",
    "S5.02",
    "S5.03",
    "S5.04"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 131–132"
   },
   "enunciato": {
    "la": "",
    "it": "Se da un punto qualsiasi P di una sezione conica data si conducono, sotto angoli dati, ai quattro lati AB, CD, AC, DB, prolungati indefinitamente, di un trapezio qualsiasi ABCD inscritto in quella sezione conica, altrettante rette PQ, PR, PS, PT, una a ciascun lato, il rettangolo PQ × PR delle rette condotte a due lati opposti sta al rettangolo PS × PT delle rette condotte agli altri due lati opposti in un rapporto dato.",
    "en": "If from any point P of a given conic section, to the four produced sides AB, CD, AC, DB, of any trapezium ABDC inscribed in that section, as many right lines PQ, PR, PS, PT are drawn in given angles, each line to each side; the rectangle PQ × PR of those on the opposite sides AB, CD, will be to the rectangle PS × PT of those on the other two opposite sides AC, BD, in a given ratio."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "D",
     "P",
     "Q",
     "R",
     "S",
     "T",
     "O",
     "K",
     "t",
     "d",
     "r",
     "M",
     "N",
     "q",
     "s"
    ],
    "vincoli": [
     "A, B, C, D, P sulla stessa conica",
     "Q su AB, R su CD, S su AC, T su BD; PQ, PR, PS, PT sotto angoli dati",
     "Caso 1: PQ, PR ∥ AC; PS, PT ∥ AB; AC ∥ BD",
     "Caso 2: Bd ∥ AC, d sulla conica; DM ∥ PQ",
     "Caso 3: Pq, Pr ∥ AC; Ps, Pt ∥ AB"
    ]
   },
   "passi": [
    {
     "id": "L1-Lem17-p1",
     "la": "",
     "it": "Caso 1. Supponiamo anzitutto che le linee condotte a due lati opposti siano parallele a uno degli altri lati: per esempio PQ e PR al lato AC, e PS e PT al lato AB.",
     "en": "CASE 1. Let us suppose, first, that the lines drawn to one pair of opposite sides are parallel to either of the other sides; as PQ and PR to the side AC, and PS and PT to the side AB.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "trapezio ABDC inscritto",
       "P",
       "PQ, PR parallele ad AC",
       "PS, PT parallele ad AB"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem17-p2",
     "la": "",
     "it": "Siano inoltre paralleli fra loro due lati opposti, per esempio AC e BD.",
     "en": "And farther, that one pair of the opposite sides, as AC and BD, are parallel betwixt themselves;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "AC ∥ BD"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem17-p3",
     "la": "",
     "it": "La retta che divide a metà quei lati paralleli sarà allora uno dei diametri della sezione conica, e dividerà a metà anche RQ.",
     "en": "then the right line which bisects those parallel sides will be one of the diameters of the conic section, and will likewise bisect RQ.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "diametro che biseca AC e BD"
      ],
      "evidenzia": [
       "il diametro biseca anche RQ"
      ]
     }
    },
    {
     "id": "L1-Lem17-p4",
     "la": "",
     "it": "Sia O il punto in cui RQ è divisa a metà: PO sarà un’ordinata rispetto a quel diametro.",
     "en": "Let O be the point in which RQ is bisected, and PO will be an ordinate to that diameter.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "O"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem17-p5",
     "la": "",
     "it": "Si prolunghi PO fino a K, in modo che OK sia uguale a PO: OK sarà l’ordinata dalla parte opposta del diametro.",
     "en": "Produce PO to K, so that OK may be equal to PO, and OK will be an ordinate on the other side of that diameter.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "K (OK = PO)"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem17-p6",
     "la": "",
     "it": "Poiché dunque i punti A, B, P e K stanno sulla sezione conica, e PK taglia AB sotto un angolo dato, il rettangolo PQK starà al rettangolo AQB in un rapporto dato (per le Prop. 17, 19, 21 e 23 del Libro III delle *Coniche* di Apollonio).",
     "en": "Since, therefore, the points A, B, P and K are placed in the conic section, and PK cuts AB in a given angle, the rectangle PQK (by Prop. XVII., XIX., XXI. and XXIII., Book III., of Apollonius's Conics) will be to the rectangle AQB in a given ratio.",
     "dipende_da": [
      "Apollonio, Coniche III, 17, 19, 21, 23"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "rettangoli PQK e AQB"
      ]
     },
     "nota": "La trascrizione ha «coni corum»: la parola è spezzata dal marcatore di pagina <74>."
    },
    {
     "id": "L1-Lem17-p7",
     "la": "",
     "it": "Ma QK e PR sono uguali, in quanto differenze delle uguali OK, OP e OQ, OR; e di qui sono uguali anche i rettangoli PQK e PQ × PR. Perciò il rettangolo PQ × PR sta al rettangolo AQB, cioè al rettangolo PS × PT, in un rapporto dato. C.V.D.",
     "en": "But QK and PR are equal, as being the differences of the equal lines OK, OP, and OQ, OR; whence the rectangles PQK and PQ × PR are equal; and therefore the rectangle PQ × PR is to the rectangle AQB, that is, to the rectangle PS × PT in a given ratio. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "QK = PR",
       "AQ = PS, QB = PT"
      ]
     }
    },
    {
     "id": "L1-Lem17-p8",
     "la": "",
     "it": "Caso 2. Supponiamo ora che i lati opposti AC e BD del trapezio non siano paralleli.",
     "en": "CASE 2. Let us next suppose that the opposite sides AC and BD of the trapezium are not parallel.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "AC non parallelo a BD"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem17-p9",
     "la": "",
     "it": "Si conduca Bd parallela ad AC, che incontri la retta ST in t e la sezione conica in d.",
     "en": "Draw Bd parallel to AC, and meeting as well the right line ST in t, as the conic section in d.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Bd ∥ AC",
       "t",
       "d"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem17-p10",
     "la": "",
     "it": "Si congiunga Cd, che tagli PQ in r, e si conduca DM parallela a PQ, che tagli Cd in M e AB in N.",
     "en": "Join Cd cutting PQ in r, and draw DM parallel to PQ, cutting Cd in M, and AB in N.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Cd",
       "r",
       "DM ∥ PQ",
       "M",
       "N"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem17-p11",
     "la": "",
     "it": "Ora, per la similitudine dei triangoli BTt, DBN, Bt, ossia PQ, sta a Tt come DN sta a NB.",
     "en": "Then (because of the similar triangles BTt, DBN), Bt or PQ is to Tt as DN to NB.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "triangoli BTt, DBN"
      ]
     }
    },
    {
     "id": "L1-Lem17-p12",
     "la": "",
     "it": "Così anche Rr sta ad AQ, ossia a PS, come DM sta ad AN.",
     "en": "And so Rr is to AQ or PS as DM to AN.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem17-p13",
     "la": "",
     "it": "Dunque, moltiplicando gli antecedenti per gli antecedenti e i conseguenti per i conseguenti, come il rettangolo PQ per Rr sta al rettangolo PS per Tt, così il rettangolo NDM sta al rettangolo ANB, e (per il Caso 1) così il rettangolo PQ per Pr sta al rettangolo PS per Pt; e, separando, così il rettangolo PQ × PR sta al rettangolo PS × PT. C.V.D.",
     "en": "Wherefore, by multiplying the antecedents by the antecedents, and the consequents by the consequents, as the rectangle PQ × Rr is to the rectangle PS × Tt, so will the rectangle NDM be to the rectangle ANB; and (by Case 1) so is the rectangle PQ × Pr to the rectangle PS × Pt: and by division, so is the rectangle PQ × PR to the rectangle PS × PT. Q.E.D.",
     "dipende_da": [
      "Lemma XVII, Caso 1"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "conica per A, B, d, C con AC ∥ Bd"
      ]
     }
    },
    {
     "id": "L1-Lem17-p14",
     "la": "",
     "it": "Caso 3. Supponiamo infine che le quattro linee PQ, PR, PS, PT non siano parallele ai lati AC, AB, ma inclinate su di essi in un modo qualsiasi.",
     "en": "CASE 3. Let us suppose, lastly, the four lines PQ, PR, PS, PT, not to be parallel to the sides AC, AB, but any way inclined to them.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "PQ, PR, PS, PT inclinate"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem17-p15",
     "la": "",
     "it": "Al loro posto si conducano Pq, Pr parallele ad AC, e Ps, Pt parallele ad AB: poiché gli angoli dei triangoli PQq, PRr, PSs, PTt sono dati, saranno dati i rapporti di PQ a Pq, di PR a Pr, di PS a Ps e di PT a Pt, e quindi i rapporti composti di PQ × PR a Pq × Pr e di PS × PT a Ps × Pt.",
     "en": "In their place draw Pq, Pr, parallel to AC; and Ps, Pt parallel to AB; and because the angles of the triangles PQq, PRr, PSs, PTt are given, the ratios of PQ to Pq, PR to Pr, PS to Ps, PT to Pt will be also given; and therefore the compounded ratios PQ × PR to Pq × Pr, and PS × PT to Ps × Pt are given.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Pq, Pr ∥ AC",
       "Ps, Pt ∥ AB"
      ],
      "evidenzia": [
       "triangoli PQq, PRr, PSs, PTt"
      ]
     }
    },
    {
     "id": "L1-Lem17-p16",
     "la": "",
     "it": "Ma, per quanto si è dimostrato sopra, il rapporto di Pq × Pr a Ps × Pt è dato; dunque è dato anche il rapporto di PQ × PR a PS × PT. C.V.D.",
     "en": "But from what we have demonstrated before, the ratio of Pq × Pr to Ps × Pt is given; and therefore also the ratio of PQ × PR to PS × PT. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "«per superius demonstrata» rimanda ai Casi 1 e 2, senza citarli per numero."
    }
   ]
  },
  {
   "id": "L1-Lem18",
   "tipo": "Lemma",
   "titolo": "Lemma XVIII — il luogo del rapporto dato è una conica",
   "copertura": [
    "S5.05",
    "S5.06"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 132–133"
   },
   "enunciato": {
    "la": "",
    "it": "Poste le stesse cose, se il rettangolo PQ × PR delle rette condotte a due lati opposti del trapezio sta al rettangolo PS × PT delle rette condotte agli altri due lati in un rapporto dato, il punto P, dal quale sono condotte le linee, si troverà su una sezione conica descritta intorno al trapezio.",
    "en": "The same things supposed, if the rectangle PQ × PR of the lines drawn to the two opposite sides of the trapezium is to the rectangle PS × PT of those drawn to the other two sides in a given ratio, the point P, from whence those lines are drawn, will be placed in a conic section described about the trapezium."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "D",
     "P",
     "p",
     "b",
     "Q",
     "R",
     "S",
     "T",
     "q",
     "r",
     "s",
     "t",
     "k",
     "n",
     "f",
     "d"
    ],
    "vincoli": [
     "conica per A, B, C, D, p",
     "b su AP e sulla conica",
     "rette condotte sotto gli angoli dati del Lemma XVII"
    ]
   },
   "passi": [
    {
     "id": "L1-Lem18-p1",
     "la": "",
     "it": "Immagina che per i punti A, B, C, D e per uno degli infiniti punti P, per esempio p, sia descritta una sezione conica: dico che il punto P si trova sempre su di essa.",
     "en": "Conceive a conic section to be described passing through the points A, B, C, D, and any one of the infinite number of points P, as for example p; I say, the point P will be always placed in this section.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A, B, C, D",
       "p",
       "conica per A, B, C, D, p"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem18-p2",
     "la": "",
     "it": "Se lo neghi, congiungi AP, che tagli questa sezione conica, se è possibile, in un punto diverso da P, per esempio in b.",
     "en": "If you deny the thing, join AP cutting this conic section somewhere else, if possible, than in P, as in b.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "P",
       "AP",
       "b"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem18-p3",
     "la": "",
     "it": "Dunque, se da questi punti p e b si conducono sotto gli angoli dati ai lati del trapezio le rette pq, pr, ps, pt e bk, bn, bf, bd, come bk × bn sta a bf × bd, così (per il Lemma XVII) pq × pr sta a ps × pt, e così (per ipotesi) PQ × PR sta a PS × PT.",
     "en": "Therefore if from those points p and b, in the given angles to the sides of the trapezium, we draw the right lines pq, pr, ps, pt, and bk, bn, bf, bd, we shall have, as bk × bn to bf × bd, so (by Lem. XVII) pq × pr to ps × pt; and so (by supposition) PQ × PR to PS × PT.",
     "dipende_da": [
      "Lemma XVII"
     ],
     "figura": {
      "mostra": [
       "pq, pr, ps, pt",
       "bk, bn, bf, bd",
       "PQ, PR, PS, PT"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem18-p4",
     "la": "",
     "it": "Inoltre, per la similitudine dei trapezi bkAf, PQAS, come bk sta a bf così PQ sta a PS.",
     "en": "And because of the similar trapezia bkAf, PQAS, as bk to bf, so PQ to PS.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "trapezi bkAf, PQAS"
      ]
     }
    },
    {
     "id": "L1-Lem18-p5",
     "la": "",
     "it": "Perciò, dividendo i termini della proporzione precedente per i termini corrispondenti di questa, bn starà a bd come PR sta a PT.",
     "en": "Wherefore by dividing the terms of the preceding proportion by the correspondent terms of this, we shall have bn to bd as PR to PT.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem18-p6",
     "la": "",
     "it": "Dunque i trapezi equiangoli Dnbd, DRPT sono simili, e perciò le loro diagonali Db, DP coincidono.",
     "en": "And therefore the equiangular trapezia Dnbd, DRPT, are similar, and consequently their diagonals Db, DP do coincide.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "trapezi Dnbd, DRPT",
       "diagonali Db, DP"
      ]
     }
    },
    {
     "id": "L1-Lem18-p7",
     "la": "",
     "it": "Quindi b cade nell’intersezione delle rette AP, DP, e perciò coincide con il punto P.",
     "en": "Wherefore b falls in the intersection of the right lines AP, DP, and consequently coincides with the point P.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem18-p8",
     "la": "",
     "it": "Perciò il punto P, dovunque sia preso, cade sulla sezione conica assegnata. C.V.D.",
     "en": "And therefore the point P, wherever it is taken, falls to be in the assigned conic section. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L1-Lem19",
   "tipo": "Lemma (problema)",
   "titolo": "Lemma XIX — trovare un punto del luogo delle quattro rette",
   "copertura": [
    "S5.09",
    "S5.10"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 134"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare un punto P tale che, se da esso si conducono sotto angoli dati quattro rette PQ, PR, PS, PT ad altrettante rette date di posizione AB, CD, AC, BD, una a ciascuna, il rettangolo PQ × PR di due delle rette condotte stia al rettangolo PS × PT delle altre due in un rapporto dato.",
    "en": "To find a point P from which if four right lines PQ, PR, PS, PT are drawn to as many other right lines AB, CD, AC, BD, given by position, each to each, at given angles, the rectangle PQ × PR, under any two of the lines drawn, shall be to the rectangle PS × PT, under the other two, in a given ratio."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "D",
     "H",
     "I",
     "P",
     "Q",
     "R",
     "S",
     "T"
    ],
    "vincoli": [
     "AB, CD, AC, BD date di posizione",
     "P su AH; H su BD, I su CD"
    ]
   },
   "passi": [
    {
     "id": "L1-Lem19-p1",
     "la": "",
     "it": "Le linee AB, CD, alle quali sono condotte le due rette PQ, PR che comprendono uno dei rettangoli, incontrino le altre due linee date di posizione nei punti A, B, C, D.",
     "en": "Suppose the lines AB, CD, to which the two right lines PQ, PR, containing one of the rectangles, are drawn to meet two other lines, given by position, in the points A, B, C, D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "rette AB, CD, AC, BD",
       "A, B, C, D"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem19-p2",
     "la": "",
     "it": "Da uno di essi, A, si conduca una retta qualsiasi AH, sulla quale si voglia trovare il punto P.",
     "en": "From one of those, as A, draw any right line AH, in which you would find the point P.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "AH"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem19-p3",
     "la": "",
     "it": "Essa tagli le linee opposte BD, CD, cioè BD in H e CD in I; poiché tutti gli angoli della figura sono dati, saranno dati i rapporti di PQ a PA e di PA a PS, e quindi il rapporto di PQ a PS.",
     "en": "Let this cut the opposite lines BD, CD, in H and I; and, because all the angles of the figure are given, the ratio of PQ to PA, and PA to PS, and therefore of PQ to PS, will be also given.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "H",
       "I",
       "P (provvisorio)",
       "PQ, PS"
      ],
      "evidenzia": [
       "PQ : PS dato"
      ]
     }
    },
    {
     "id": "L1-Lem19-p4",
     "la": "",
     "it": "Togliendo questo rapporto dal rapporto dato di PQ × PR a PS × PT, sarà dato il rapporto di PR a PT; e aggiungendo i rapporti dati di PI a PR e di PT a PH, sarà dato il rapporto di PI a PH, e perciò il punto P. C.V.T.",
     "en": "Subducting this ratio from the given ratio of PQ × PR to PS × PT, the ratio of PR to PT will be given; and adding the given ratios of PI to PR, and PT to PH, the ratio of PI to PH, and therefore the point P will be given. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "PR, PT"
      ],
      "evidenzia": [
       "PI : PH dato",
       "P"
      ]
     },
     "nota": "«Togliere» e «aggiungere» un rapporto significano qui dividere e comporre (moltiplicare) i rapporti."
    }
   ]
  },
  {
   "id": "L1-Lem19-Cor2",
   "tipo": "Corollarium",
   "titolo": "Lemma XIX, Cor. 2 — diametro, lato trasverso e lato retto del luogo",
   "copertura": [
    "S5.12"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 134–135"
   },
   "enunciato": {
    "la": "",
    "it": "Cor. 2. Di qui si può anche determinare il luogo di tutti i punti P.",
    "en": "COR. 2. Hence also the locus of all the points P may be determined."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "E",
     "F",
     "G",
     "H"
    ],
    "vincoli": [
     "AE tangente al luogo in A",
     "BF ∥ AE, F sul luogo",
     "G punto di mezzo di BF",
     "H secondo incontro di AG con il luogo"
    ]
   },
   "passi": [
    {
     "id": "L1-Lem19-Cor2-p1",
     "la": "",
     "it": "Per uno qualsiasi dei punti A, B, C, D, per esempio A, si conduca la tangente AE al luogo, e per un altro punto qualsiasi, B, si conduca BF parallela alla tangente, che incontri il luogo in F.",
     "en": "Through any of the points A, B, C, D, as A, draw AE touching the locus, and through any other point B parallel to the tangent, draw BF meeting the locus in F;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A",
       "tangente AE",
       "B",
       "BF ∥ AE",
       "F"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem19-Cor2-p2",
     "la": "",
     "it": "Il punto F si troverà per il Lemma XIX.",
     "en": "and find the point F by this Lemma.",
     "dipende_da": [
      "Lemma XIX"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Motte: «by this Lemma»; il latino cita il Lemma XIX per numero, cioè lo stesso lemma."
    },
    {
     "id": "L1-Lem19-Cor2-p3",
     "la": "",
     "it": "Si divida BF a metà in G: la retta indefinita AG, una volta condotta, darà la posizione del diametro rispetto al quale BG e FG sono ordinate.",
     "en": "Bisect BF in G, and, drawing the indefinite line AG, this will be the position of the diameter to which BG and FG are ordinates.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "G",
       "AG"
      ],
      "evidenzia": [
       "AG diametro; BG, FG ordinate"
      ]
     }
    },
    {
     "id": "L1-Lem19-Cor2-p4",
     "la": "",
     "it": "Questa AG incontri il luogo in H: AH sarà il lato trasverso, al quale il lato retto starà come BG² sta ad AG × GH.",
     "en": "Let this AG meet the locus in H, and AH will be its diameter or latus transversum, to which the latus rectum will be as BG2 to AG × GH.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "H"
      ],
      "evidenzia": [
       "lato trasverso AH",
       "BG² : AG × GH"
      ]
     },
     "nota": "Motte aggiunge «its diameter or» prima di «latus transversum»."
    },
    {
     "id": "L1-Lem19-Cor2-p5",
     "la": "",
     "it": "Se AG non incontra il luogo in alcun punto, poiché la linea AH è infinita, il luogo sarà una parabola, e il suo lato retto relativo al diametro AG sarà BG²/AG.",
     "en": "If AG nowhere meets the locus, the line AH being infinite, the locus will be a parabola; and its latus rectum corresponding to the diameter AG will be",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "La trascrizione appiattisce la frazione: «BGqAG» vale BG²/AG. In Motte la formula è un’immagine (SVG 108), che si legge BG²/AG."
    },
    {
     "id": "L1-Lem19-Cor2-p6",
     "la": "",
     "it": "Se invece lo incontra in qualche punto, il luogo sarà un’iperbole quando i punti A e H sono situati dalla stessa parte di G, e un’ellisse quando G è in mezzo, a meno che l’angolo AGB sia retto e inoltre BG² sia uguale al rettangolo AGH: in questo caso si avrà un cerchio.",
     "en": "But if it does meet it anywhere, the locus will be an hyperbola, when the points A and H are placed on the same side the point G; and an ellipsis, if the point G falls between the points A and H; unless, perhaps, the angle AGB is a right angle, and at the same time BG2 equal to the rectangle AGH, in which case the locus will be a circle.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "posizione di G rispetto ad A e H"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-Lem20",
   "tipo": "Lemma",
   "titolo": "Lemma XX — rapporto costante PR : PT",
   "copertura": [
    "S5.14",
    "S5.15",
    "S5.16"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 135–136"
   },
   "enunciato": {
    "la": "",
    "it": "Se un parallelogramma qualsiasi ASPQ tocca con due angoli opposti, A e P, una sezione conica qualsiasi nei punti A e P; se con i lati AQ, AS di uno di quegli angoli, prolungati indefinitamente, incontra la stessa sezione conica in B e C; e se dai punti d’incontro B e C a un quinto punto qualsiasi D della sezione conica si conducono due rette BD, CD, che incontrino gli altri due lati del parallelogramma, PS e PQ, prolungati indefinitamente, in T e R: le parti PR e PT staccate dai lati staranno sempre fra loro in un rapporto dato. E viceversa, se quelle parti staccate stanno fra loro in un rapporto dato, il punto D si troverà su una sezione conica passante per i quattro punti A, B, C, P.",
    "en": "If the two opposite angular points A and P of any parallelogram ASPQ touch any conic section in the points A and P; and the sides AQ, AS of one of those angles, indefinitely produced, meet the same conic section in B and C; and from, the points of concourse B and C to any fifth point D of the conic section, two right lines BD, CD are drawn meeting the two other sides PS, PQ of the parallelogram, indefinitely produced in T and R; the parts PR and PT, cut off from the sides, will always be one to the other in a given ratio. And vice versa, if those parts cut off are one to the other in a given ratio, the locus of the point D will be a, conic section passing through the four points A, B, C, P."
   },
   "figura_base": {
    "punti": [
     "A",
     "S",
     "P",
     "Q",
     "B",
     "C",
     "D",
     "T",
     "R",
     "G",
     "H",
     "I",
     "E",
     "F",
     "K"
    ],
    "vincoli": [
     "A, P, B, C, D sulla conica",
     "ASPQ parallelogramma; B su AQ, C su AS",
     "T = BD ∩ PS, R = CD ∩ PQ",
     "DG ∥ AB, DE ∥ AC"
    ]
   },
   "passi": [
    {
     "id": "L1-Lem20-p1",
     "la": "",
     "it": "Caso 1. Si congiungano BP, CP e dal punto D si conducano due rette DG, DE: la prima, DG, sia parallela ad AB e incontri PB, PQ, CA in H, I, G; l’altra, DE, sia parallela ad AC e incontri PC, PS, AB in F, K, E. Per il Lemma XVII il rettangolo DE × DF starà al rettangolo DG × DH in un rapporto dato.",
     "en": "CASE 1. Join BP, CP, and from the point D draw the two right lines DG, DE, of which the first DG shall be parallel to AB, and meet PB, PQ, CA in H, I, G; and the other DE shall be parallel to AC, and meet PC, PS, AB, in F, K, E; and (by Lem. XVII) the rectangle DE × DF will be to the rectangle DG × DH in a given ratio.",
     "dipende_da": [
      "Lemma XVII"
     ],
     "figura": {
      "mostra": [
       "parallelogramma ASPQ",
       "conica per A, B, C, P, D",
       "BP, CP",
       "DG ∥ AB con H, I, G",
       "DE ∥ AC con F, K, E"
      ],
      "evidenzia": [
       "DE × DF : DG × DH"
      ]
     }
    },
    {
     "id": "L1-Lem20-p2",
     "la": "",
     "it": "Ma PQ sta a DE (ossia a IQ) come PB sta a HB, e quindi come PT sta a DH; e, permutando, PQ sta a PT come DE sta a DH.",
     "en": "But PQ is to DE (or IQ) as PB to HB, and consequently as PT to DH; and by permutation PQ is to PT as DE to DH.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "T"
      ],
      "evidenzia": [
       "triangoli PBQ, HBI"
      ]
     }
    },
    {
     "id": "L1-Lem20-p3",
     "la": "",
     "it": "Inoltre PR sta a DF come RC sta a DC, e quindi come (IG, ossia) PS sta a DG; e, permutando, PR sta a PS come DF sta a DG. Componendo i rapporti, il rettangolo PQ × PR sta al rettangolo PS × PT come il rettangolo DE × DF sta al rettangolo DG × DH, e quindi in un rapporto dato.",
     "en": "Likewise PR is to DF as RC to DC, and therefore as (IG or) PS to DG; and by permutation PR is to PS as DF to DG; and, by compounding those ratios, the rectangle PQ × PR will be to the rectangle PS × PT as the rectangle DE × DF is to the rectangle DG × DH, and consequently in a given ratio.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "R"
      ],
      "evidenzia": []
     },
     "nota": "La trascrizione ha «conjunctis rationibus sit»: forse «fit» (s lunga), da verificare sulla stampa; il senso non cambia."
    },
    {
     "id": "L1-Lem20-p4",
     "la": "",
     "it": "Ma PQ e PS sono date, e perciò è dato il rapporto di PR a PT. C.V.D.",
     "en": "But PQ and PS are given, and therefore the ratio of PR to PT is given. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "PR : PT costante"
      ]
     }
    },
    {
     "id": "L1-Lem20-p5",
     "la": "",
     "it": "Caso 2. Se invece si pone che PR e PT stiano fra loro in un rapporto dato, ripercorrendo all’indietro un ragionamento simile ne seguirà che il rettangolo DE × DF sta al rettangolo DG × DH in un rapporto dato, e quindi (per il Lemma XVIII) che il punto D si trova su una sezione conica passante per i punti A, B, C, P. C.V.D.",
     "en": "CASE 2. But if PR and PT are supposed to be in a given ratio one to the other, then by going back again, by a like reasoning, it will follow that the rectangle DE × DF is to the rectangle DG × DH in a given ratio; and so the point D (by Lem. XVIII) will lie in a conic section passing through the points A, B, C, P, as its locus. Q.E.D.",
     "dipende_da": [
      "Lemma XVIII"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L1-Lem21",
   "tipo": "Lemma",
   "titolo": "Lemma XXI — descrizione organica della conica",
   "copertura": [
    "S5.20",
    "S5.21",
    "S5.22"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 136–137"
   },
   "enunciato": {
    "la": "",
    "it": "Se due rette mobili e infinite BM, CM, condotte per i punti dati B, C come per due poli, descrivono con il loro punto d’incontro M una terza retta MN data di posizione; e se si conducono altre due rette infinite BD, CD, che formino con le prime due, nei punti dati B, C, gli angoli dati MBD, MCD: dico che queste due rette BD, CD descriveranno con il loro punto d’incontro D una sezione conica passante per i punti B, C. E viceversa, se le rette BD, CD descrivono con il loro punto d’incontro D una sezione conica passante per i punti dati B, C, A, e l’angolo DBM è sempre uguale all’angolo dato ABC e l’angolo DCM sempre uguale all’angolo dato ACB, il punto M si troverà su una retta data di posizione.",
    "en": "If two moveable and indefinite right lines BM, CM drawn through given points B, C, as poles, do by their point of concourse M describe a third right line MN given by position; and other two indefinite right lines BD, CD are drawn, making with the former two at those given points B, C, given angles, MBD, MCD: I say, that those two right lines BD, CD will by their point of concourse D describe a conic section passing through the points B, C. And, vice versa, if the right lines BD, CD do by their point of concourse D describe a conic section passing through the given points B, C, A, and the angle DBM is always equal to the given angle ABC, as well as the angle DCM always equal to the given angle ACB, the point M will lie in a right line given by position, as its locus."
   },
   "figura_base": {
    "punti": [
     "B",
     "C",
     "M",
     "N",
     "D",
     "P",
     "T",
     "R",
     "A",
     "p",
     "n"
    ],
    "vincoli": [
     "poli B, C fissi",
     "M sulla retta MN",
     "angoli MBD, MCD costanti"
    ]
   },
   "passi": [
    {
     "id": "L1-Lem21-p1",
     "la": "",
     "it": "Sia infatti dato sulla retta MN il punto N, e quando il punto mobile M cade sul punto fisso N, il punto mobile D cada sul punto fisso P.",
     "en": "For in the right line MN let a point N be given, and when the moveable point M falls on the immoveable point N, let the moveable point D fall on an immovable point P.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "poli B, C",
       "retta MN",
       "N",
       "P"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem21-p2",
     "la": "",
     "it": "Congiungi CN, BN, CP, BP, e dal punto P conduci le rette PT, PR, che incontrino BD, CD in T e R e formino l’angolo BPT uguale all’angolo dato BNM e l’angolo CPR uguale all’angolo dato CNM.",
     "en": "Join CN, BN, CP, BP, and from the point P draw the right lines PT, PR meeting BD, CD in T and R, and making the angle BPT equal to the given angle BNM, and the angle CPR equal to the given angle CNM.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "CN, BN, CP, BP",
       "M e D in posizione generica",
       "PT, PR",
       "T, R"
      ],
      "evidenzia": [
       "angolo BPT = BNM",
       "angolo CPR = CNM"
      ]
     }
    },
    {
     "id": "L1-Lem21-p3",
     "la": "",
     "it": "Poiché dunque (per ipotesi) gli angoli MBD, NBP sono uguali, come pure gli angoli MCD, NCP, togli gli angoli comuni NBD e NCD: resteranno uguali NBM e PBT, NCM e PCR; e perciò i triangoli NBM, PBT sono simili, come pure i triangoli NCM, PCR.",
     "en": "Wherefore since (by supposition) the angles MBD, NBP are equal, as also the angles MCD, NCP, take away the angles NBD and NCD that are common, and there will remain the angles NBM and PBT, NCM and PCR equal; and therefore the triangles NBM, PBT are similar, as also the triangles NCM, PCR.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "triangoli NBM, PBT",
       "triangoli NCM, PCR"
      ]
     }
    },
    {
     "id": "L1-Lem21-p4",
     "la": "",
     "it": "Perciò PT sta a NM come PB sta a NB, e PR sta a NM come PC sta a NC.",
     "en": "Wherefore PT is to NM as PB to NB; and PR to NM as PC to NC.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem21-p5",
     "la": "",
     "it": "Ma i punti B, C, N, P sono fissi.",
     "en": "But the points, B, C, N, P are immovable:",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem21-p6",
     "la": "",
     "it": "Dunque PT e PR hanno un rapporto dato con NM, e quindi un rapporto dato fra loro; e perciò (per il Lemma XX) il punto D, nel quale si incontrano in ogni istante le rette mobili BT e CR, si trova su una sezione conica passante per i punti B, C, P. C.V.D.",
     "en": "wherefore PT and PR have a given ratio to NM, and consequently a given ratio between themselves; and therefore, (by Lemma XX) the point D wherein the moveable right lines BT and CR perpetually concur, will be placed in a conic section passing through the points B, C, P. Q.E.D.",
     "dipende_da": [
      "Lemma XX"
     ],
     "figura": {
      "mostra": [
       "conica per B, C, P"
      ],
      "evidenzia": [
       "PT : PR costante"
      ]
     }
    },
    {
     "id": "L1-Lem21-p7",
     "la": "",
     "it": "E viceversa, se il punto mobile D si trova su una sezione conica passante per i punti dati B, C, A, l’angolo DBM è sempre uguale all’angolo dato ABC e l’angolo DCM sempre uguale all’angolo dato ACB, e quando il punto D cade successivamente su due punti fissi qualsiasi p, P della sezione il punto mobile M cade successivamente su due punti fissi n, N: per questi stessi n, N si conduca la retta nN, e questa sarà il luogo costante di quel punto mobile M.",
     "en": "And, vice versa, if the moveable point D lies in a conic section passing through the given points B, C, A; and the angle DBM is always equal to the given angle ABC, and the angle DCM always equal to the given angle ACB, and when the point D falls successively on any two immovable points p, P, of the conic section, the moveable point M falls successively on two immovable points n, N. Through these points n, N, draw the right line nN: this line nN will be the perpetual locus of that moveable point M.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "conica per B, C, A",
       "p, P",
       "n, N",
       "retta nN"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem21-p8",
     "la": "",
     "it": "Infatti, se è possibile, il punto M si trovi su una linea curva.",
     "en": "For, if possible, let the point M be placed in any curve line.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem21-p9",
     "la": "",
     "it": "Il punto D si troverà dunque su una sezione conica passante per i cinque punti B, C, A, p, P, quando il punto M si trova sempre su una linea curva.",
     "en": "Therefore the point D will be placed in a conic section passing through the five points B, C, A, p, P, when the point M is perpetually placed in a curve line.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem21-p10",
     "la": "",
     "it": "Ma, per quanto già dimostrato, il punto D si troverà anche su una sezione conica passante per gli stessi cinque punti B, C, A, p, P, quando il punto M si trova sempre su una linea retta.",
     "en": "But from what was demonstrated before, the point D will be also placed in a conic section passing through the same five points B, C, A, p, P, when the point M is perpetually placed in a right line.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "«ex jam demonstratis» rimanda alla prima parte di questo lemma."
    },
    {
     "id": "L1-Lem21-p11",
     "la": "",
     "it": "Dunque due sezioni coniche passeranno per gli stessi cinque punti, contro il Cor. 3 del Lemma XX.",
     "en": "Wherefore the two conic sections will both pass through the same five points, against Corol. 3, Lem. XX.",
     "dipende_da": [
      "Lemma XX, Cor. 3"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem21-p12",
     "la": "",
     "it": "È dunque assurdo che il punto M si trovi su una linea curva. C.V.D.",
     "en": "It is therefore absurd to suppose that the point M is placed in a curve line. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L1-P22",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXII, Probl. XIV — traiettoria per cinque punti",
   "copertura": [
    "S5.23",
    "S5.24",
    "S5.25"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 137–138"
   },
   "enunciato": {
    "la": "",
    "it": "Descrivere una traiettoria per cinque punti dati.",
    "en": "To describe a trajectory that shall pass through five given points."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "P",
     "D",
     "S",
     "Q",
     "T",
     "R",
     "t",
     "r",
     "d",
     "L",
     "M",
     "N",
     "m"
    ],
    "vincoli": [
     "cinque punti dati",
     "TPS ∥ AB, PRQ ∥ AC",
     "tr ∥ TR",
     "seconda costruzione: angoli ABC, ACB rotanti intorno a B, C; m sulla retta MN"
    ]
   },
   "passi": [
    {
     "id": "L1-P22-p1",
     "la": "",
     "it": "Siano dati i cinque punti A, B, C, P, D.",
     "en": "Let the five given points be A, B, C, P, D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A, B, C, P, D"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P22-p2",
     "la": "",
     "it": "Da uno di essi, A, ad altri due qualsiasi, B e C, che si chiameranno poli, conduci le rette AB, AC, e per il quarto punto P le rette TPS, PRQ, parallele a queste.",
     "en": "From any one of them, as A, to any other two as B, C, which may be called the poles, draw the right lines AB, AC, and parallel to those the lines TPS, PRQ through the fourth point P.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "poli B, C",
       "AB, AC",
       "TPS ∥ AB",
       "PRQ ∥ AC"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P22-p3",
     "la": "",
     "it": "Poi dai due poli B, C conduci per il quinto punto D due rette infinite BDT, CRD, che incontrino le rette TPS, PRQ condotte per ultime (la prima con la prima e la seconda con la seconda) in T e R.",
     "en": "Then from the two poles B, C, draw through the fifth point D two indefinite lines BDT, CRD, meeting with the last drawn lines TPS, PRQ (the former with the former, and the latter with the latter) in T and R.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "BDT",
       "CRD",
       "T",
       "R"
      ],
      "evidenzia": []
     },
     "nota": "La trascrizione ha «occurentes» per «occurrentes»: refuso probabile della trascrizione, da verificare sulla stampa."
    },
    {
     "id": "L1-P22-p4",
     "la": "",
     "it": "Infine, conducendo una retta tr parallela a TR, stacca dalle rette PT, PR due segmenti qualsiasi Pt, Pr proporzionali a PT, PR; e se le rette Bt, Cr, condotte per i loro estremi t, r e per i poli B, C, si incontrano in d, quel punto d sarà situato sulla traiettoria cercata.",
     "en": "Then drawing the right line tr parallel to TR, cutting off from the right lines PT, PR, any segments Pt, Pr, proportional to PT, PR; and if through their extremities, t, r, and the poles B, C, the right lines Bt, Cr are drawn, meeting in d, that point d will be placed in the trajectory required.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tr ∥ TR",
       "t, r",
       "Bt, Cr",
       "d"
      ],
      "evidenzia": [
       "Pt : Pr = PT : PR"
      ]
     }
    },
    {
     "id": "L1-P22-p5",
     "la": "",
     "it": "Infatti quel punto d (per il Lemma XX) si trova su una sezione conica passante per i quattro punti A, B, C, P; e, quando le linee Rr, Tt svaniscono, il punto d si riunisce con il punto D.",
     "en": "For (by Lem. XX) that point d is placed in a conic section passing through the four points A, B, C, P; and the lines Rr, Tt vanishing, the point d comes to coincide with the point D.",
     "dipende_da": [
      "Lemma XX"
     ],
     "figura": {
      "mostra": [
       "conica per A, B, C, P"
      ],
      "evidenzia": [
       "d → D quando tr → TR"
      ]
     }
    },
    {
     "id": "L1-P22-p6",
     "la": "",
     "it": "La sezione conica passa dunque per i cinque punti A, B, C, P, D. C.V.D.",
     "en": "Wherefore the conic section passes through the five points A, B, C, P, D. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "traiettoria per i cinque punti"
      ]
     },
     "nota": "Il latino chiude il problema con Q.E.D. (C.V.D.), non con Q.E.F.; così anche Motte."
    },
    {
     "id": "L1-P22-p7",
     "la": "",
     "it": "Dei punti dati congiungi tre qualsiasi, A, B, C; e, facendo ruotare intorno a due di essi, B e C, come intorno a poli, gli angoli ABC, ACB, dati di grandezza, si portino i bracci BA, CA prima sul punto D, poi sul punto P, e si segnino i punti M, N nei quali gli altri bracci BL, CL si incrociano nell’uno e nell’altro caso.",
     "en": "Of the given points join any three, as A, B, C; and about two of them B, C, as poles, making the angles ABC, ACB of a given magnitude to revolve, apply the legs BA, CA, first to the point D, then to the point P, and mark the points M, N, in which the other legs BL, CL intersect each other in both cases.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A, B, C",
       "angoli ABC, ACB mobili",
       "bracci BL, CL",
       "M, N"
      ],
      "evidenzia": []
     },
     "nota": "La trascrizione ha «pun ctum», parola spezzata dal marcatore di pagina <83>."
    },
    {
     "id": "L1-P22-p8",
     "la": "",
     "it": "Si conduca la retta infinita MN, e quegli angoli mobili ruotino intorno ai loro poli B, C con la regola che l’intersezione dei bracci BL, CL, ossia BM, CM, che ora sia m, cada sempre su quella retta infinita MN: l’intersezione dei bracci BA, CA, ossia BD, CD, che ora sia d, traccerà la traiettoria cercata PADdB.",
     "en": "Draw the indefinite right line MN, and let those moveable angles revolve about their poles B, C, in such manner that the intersection, which is now supposed to be m, of the legs BL, CL, or BM, CM, may always fall in that indefinite right line MN; and the intersection, which is now supposed to be d, of the legs BA, CA, or BD, CD, will describe the trajectory required, PADdB.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "retta MN",
       "m su MN",
       "d",
       "curva PADdB"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P22-p9",
     "la": "",
     "it": "Infatti il punto d (per il Lemma XXI) si troverà su una sezione conica passante per i punti B, C; e quando il punto m giunge ai punti L, M, N, il punto d (per costruzione) giungerà ai punti A, D, P.",
     "en": "For (by Lem. XXI) the point d will be placed in a conic section passing through the points B, C; and when the point m comes to coincide with the points L, M, N, the point d will (by construction) come to coincide with the points A, D, P.",
     "dipende_da": [
      "Lemma XXI"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "m in L, M, N ↔ d in A, D, P"
      ]
     },
     "nota": "La trascrizione ha «ADP» senza virgole; Motte «A, D, P»."
    },
    {
     "id": "L1-P22-p10",
     "la": "",
     "it": "Si descriverà dunque una sezione conica passante per i cinque punti A, B, C, P, D. C.V.F.",
     "en": "Wherefore a conic section will be described that shall pass through the five points A, B, C, P, D. Q.E.F.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L1-P23",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXIII, Probl. XV — quattro punti e una tangente",
   "copertura": [
    "S5.29",
    "S5.30",
    "S5.31",
    "S5.32",
    "S5.33"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 139–140"
   },
   "enunciato": {
    "la": "",
    "it": "Descrivere una traiettoria che passi per quattro punti dati e tocchi una retta data di posizione.",
    "en": "To describe a trajectory that shall pass through four given points, and touch a right line given by position."
   },
   "figura_base": {
    "punti": [
     "H",
     "B",
     "C",
     "D",
     "P",
     "S",
     "Q",
     "T",
     "R",
     "t",
     "r",
     "d",
     "M",
     "N",
     "I",
     "G",
     "A",
     "X",
     "Y"
    ],
    "vincoli": [
     "Caso 1: HB tangente in B; BSPQ parallelogramma con PS ∥ BH, PQ ∥ BC",
     "Caso 2: tangente HI; G = BD ∩ CP; H, I sulla tangente; HX ∥ PI"
    ]
   },
   "passi": [
    {
     "id": "L1-P23-p1",
     "la": "",
     "it": "Caso 1. Siano dati la tangente HB, il punto di contatto B e altri tre punti C, D, P.",
     "en": "CASE 1. Suppose that HB is the given tangent, B the point of contact, and C, L, P, the three other given points.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tangente HB",
       "B",
       "C, D, P"
      ],
      "evidenzia": []
     },
     "nota": "Motte scrive «C, L, P»: la L è un errore per D (apparato)."
    },
    {
     "id": "L1-P23-p2",
     "la": "",
     "it": "Congiungi BC e, conducendo PS parallela alla retta BH e PQ parallela alla retta BC, completa il parallelogramma BSPQ.",
     "en": "Join BC, and draw PS parallel to BH, and PQ parallel to BC; complete the parallelogram BSPQ.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "BC",
       "PS ∥ BH",
       "PQ ∥ BC",
       "parallelogramma BSPQ"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P23-p3",
     "la": "",
     "it": "Conduci BD, che tagli SP in T, e CD, che tagli PQ in R.",
     "en": "Draw BD cutting SP in T, and CD cutting PQ in R.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "BD, T",
       "CD, R"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P23-p4",
     "la": "",
     "it": "Infine, conducendo una qualsiasi tr parallela a TR, stacca da PQ, PS i segmenti Pr, Pt proporzionali rispettivamente a PR, PT: il punto d’incontro d delle rette Cr, Bt, una volta condotte, cadrà sempre (per il Lemma XX) sulla traiettoria da descrivere.",
     "en": "Lastly, draw any line tr parallel to TR, cutting off from PQ, PS, the segments Pr, Pt proportional to PR, PT respectively; and draw Cr, Bt their point of concourse d will (by Lem. XX) always fall on the trajectory to be described.",
     "dipende_da": [
      "Lemma XX"
     ],
     "figura": {
      "mostra": [
       "tr ∥ TR",
       "Cr, Bt",
       "d"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P23-p5",
     "la": "",
     "it": "Ruotino sia l’angolo CBH, dato di grandezza, intorno al polo B, sia un raggio rettilineo qualsiasi DC, prolungato da entrambe le parti, intorno al polo C.",
     "en": "Let the angle CBH of a given magnitude revolve about the pole B, as also the rectilinear radius BC, both ways produced, about the pole C.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "angolo CBH mobile intorno a B",
       "raggio DC mobile intorno a C"
      ],
      "evidenzia": []
     },
     "nota": "Motte ha «the rectilinear radius BC»: il latino ha «radius quilibet … DC» (apparato)."
    },
    {
     "id": "L1-P23-p6",
     "la": "",
     "it": "Si segnino i punti M, N in cui il braccio BC dell’angolo taglia quel raggio quando l’altro braccio, BH, incontra lo stesso raggio nei punti P e D.",
     "en": "Mark the points M, N, on which the leg BC of the angle cuts that radius when BH, the other leg thereof, meets the same radius in the points P and D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "M, N"
      ],
      "evidenzia": []
     },
     "nota": "La trascrizione ha «pucta» per «puncta»: refuso probabile della trascrizione."
    },
    {
     "id": "L1-P23-p7",
     "la": "",
     "it": "Poi quel raggio CP, ossia CD, e il braccio BC dell’angolo si incontrino continuamente sulla retta infinita MN, una volta condotta: il punto d’incontro dell’altro braccio, BH, con il raggio traccerà la traiettoria cercata.",
     "en": "Then drawing the indefinite line MN, let that radius CP or CD and the leg BC of the angle perpetually meet in this line; and the point of concourse of the other leg BH with the radius will delineate the trajectory required.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "retta MN",
       "traiettoria"
      ],
      "evidenzia": []
     },
     "nota": "La trascrizione ha «per petuo», parola spezzata dal marcatore di pagina <85>."
    },
    {
     "id": "L1-P23-p8",
     "la": "",
     "it": "Infatti, se nelle costruzioni del problema precedente il punto A si avvicina al punto B, le linee CA e CB coincideranno, e la linea AB, nella sua posizione ultima, diventerà la tangente BH; e perciò le costruzioni là esposte diventeranno identiche alle costruzioni qui descritte.",
     "en": "For if in the constructions of the preceding Problem the point A comes to a coincidence with the point B, the lines CA and CB will coincide, and the line AB, in its last situation, will become the tangent BH; and therefore the constructions there set down will become the same with the constructions here described.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "A → B: AB diventa la tangente BH"
      ]
     }
    },
    {
     "id": "L1-P23-p9",
     "la": "",
     "it": "Il punto d’incontro del braccio BH con il raggio traccerà dunque una sezione conica passante per i punti C, D, P e tangente alla retta BH nel punto B. C.V.F.",
     "en": "Wherefore the concourse of the leg BH with the radius will describe a conic section passing through the points C, D, P, and touching the line BH in the point B. Q.E.F.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P23-p10",
     "la": "",
     "it": "Caso 2. Siano dati quattro punti B, C, D, P situati fuori della tangente HI.",
     "en": "CASE 2. Suppose the four points B, C, D, P, given, being situated without the tangent HI.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tangente HI",
       "B, C, D, P"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P23-p11",
     "la": "",
     "it": "Congiungili a due a due con le linee BD, CP, che si incontrino in G e incontrino la tangente in H e I.",
     "en": "Join each two by the lines BD, CP meeting in G, and cutting the tangent in H and I.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "BD, CP",
       "G",
       "H, I"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P23-p12",
     "la": "",
     "it": "Si divida la tangente in A in modo che HA stia a IA come il rettangolo della media proporzionale fra CG e GP e della media proporzionale fra BH e HD sta al rettangolo della media proporzionale fra DG e GB e della media proporzionale fra PI e IC: A sarà il punto di contatto.",
     "en": "Cut the tangent in A in such manner that HA may be to IA as the rectangle under a mean proportional between CG and GP, and a mean proportional between BH and HD is to a rectangle under a mean proportional between GD and GB, and a mean proportional between PI and IC, and A will be the point of contact.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A"
      ],
      "evidenzia": [
       "HA : IA"
      ]
     }
    },
    {
     "id": "L1-P23-p13",
     "la": "",
     "it": "Infatti, se HX, parallela alla retta PI, taglia la traiettoria in punti qualsiasi X e Y, il punto A (per la teoria delle coniche) dovrà essere collocato in modo che HA² stia ad AI² nel rapporto composto del rapporto del rettangolo XHY al rettangolo BHD, ossia del rettangolo CGP al rettangolo DGB, e del rapporto del rettangolo BHD al rettangolo PIC.",
     "en": "For if HX, a parallel to the right line PI, cuts the trajectory in any points X and Y, the point A (by the properties of the conic sections) will come to be so placed, that HA2 will become to AI2 in a ratio that is compounded out of the ratio of the rectangle XHY to the rectangle BHD, or of the rectangle CGP to the rectangle DGB; and the ratio of the rectangle BHD to the rectangle PIC.",
     "dipende_da": [
      "Coniche (ex conicis)"
     ],
     "figura": {
      "mostra": [
       "HX ∥ PI",
       "X, Y"
      ],
      "evidenzia": [
       "XHY : BHD = CGP : DGB"
      ]
     }
    },
    {
     "id": "L1-P23-p14",
     "la": "",
     "it": "Trovato poi il punto di contatto A, la traiettoria si descriverà come nel primo caso. C.V.F.",
     "en": "But after the point of contact A is found, the trajectory will be described as in the first Case. Q.E.F.",
     "dipende_da": [
      "Prop. XXIII, Caso 1"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L1-P24",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXIV, Probl. XVI — tre punti e due tangenti",
   "copertura": [
    "S5.35",
    "S5.36"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 140–141"
   },
   "enunciato": {
    "la": "",
    "it": "Descrivere una traiettoria che passi per tre punti dati e tocchi due rette date di posizione.",
    "en": "To describe a trajectory that shall pass through three given points, and touch two right lines given by position."
   },
   "figura_base": {
    "punti": [
     "H",
     "I",
     "K",
     "L",
     "B",
     "C",
     "D",
     "R",
     "S",
     "A",
     "P",
     "X",
     "Y",
     "Z",
     "G"
    ],
    "vincoli": [
     "tangenti HI, KL",
     "H, K su BD; I, L su CD",
     "R su HK, S su IL nei rapporti dati",
     "IY ∥ KL; IZ media proporzionale fra IX e IY",
     "G = incontro delle tangenti"
    ]
   },
   "passi": [
    {
     "id": "L1-P24-p1",
     "la": "",
     "it": "Siano date le tangenti HI, KL e i punti B, C, D.",
     "en": "Suppose HI, KL to be the given tangents and B, C, D, the given points.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tangenti HI, KL",
       "B, C, D"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P24-p2",
     "la": "",
     "it": "Per due punti qualsiasi, B e D, conduci la retta infinita BD, che incontri le tangenti nei punti H, K.",
     "en": "Through any two of those points, as B, D, draw the indefinite right line BD meeting the tangents in the points H, K.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "BD",
       "H, K"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P24-p3",
     "la": "",
     "it": "Poi, anche per altri due punti qualsiasi, C e D, conduci la retta infinita CD, che incontri le tangenti nei punti I, L.",
     "en": "Then likewise through any other two of these points, as C, D, draw the indefinite right line CD meeting the tangents in the points I, L.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "CD",
       "I, L"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P24-p4",
     "la": "",
     "it": "Dividi le rette così condotte in R e S in modo che HR stia a KR come la media proporzionale fra BH e HD sta alla media proporzionale fra BK e KD, e IS stia a LS come la media proporzionale fra CI e ID sta alla media proporzionale fra CL e LD.",
     "en": "Cut the lines drawn in R and S, so that HR may be to KR as the mean proportional between BH and HD is to the mean proportional between BK and KD; and IS to LS as the mean proportional between CI and ID is to the mean proportional between CL and LD.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "R",
       "S"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P24-p5",
     "la": "",
     "it": "Dividi a piacere o fra i punti K e H, I e L, o fuori di essi; poi conduci RS, che tagli le tangenti in A e P: A e P saranno i punti di contatto.",
     "en": "But you may cut, at pleasure, either within or between the points K and H, I and L, or without them; then draw RS cutting the tangents in A and P, and A and P will be the points of contact.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "RS",
       "A, P"
      ],
      "evidenzia": []
     },
     "nota": "Motte: «either within or between … or without»; «within or» non ha corrispondente nel latino."
    },
    {
     "id": "L1-P24-p6",
     "la": "",
     "it": "Infatti, si supponga che A e P siano i punti di contatto, situati in qualche luogo sulle tangenti; per uno qualsiasi dei punti H, I, K, L, per esempio I, situato sulla tangente HI, si conduca la retta IY parallela all’altra tangente KL, che incontri la curva in X e Y, e su di essa si prenda IZ media proporzionale fra IX e IY: per la teoria delle coniche, il rettangolo XIY, ossia IZ², sta a LP² come il rettangolo CID sta al rettangolo CLD, cioè (per costruzione) come SI² sta a SL²; e perciò IZ sta a LP come SI sta a SL.",
     "en": "For if A and P are supposed to be the points of contact, situated anywhere else in the tangents, and through any of the points H, I, K, L, as I, situated in either tangent HI, a right line IY is drawn parallel to the other tangent KL, and meeting the curve in X and Y, and in that right line there be taken IZ equal to a mean proportional between IX and IY, the rectangle XIY or IZ2, will (by the properties of the conic sections) be to LP2 as the rectangle CID is to the rectangle CLD, that is (by the construction), as SI is to SL2, and therefore IZ is to LP as SI to SL.",
     "dipende_da": [
      "Coniche (ex conicis)"
     ],
     "figura": {
      "mostra": [
       "IY ∥ KL",
       "X, Y",
       "Z"
      ],
      "evidenzia": [
       "XIY : LP² = CID : CLD"
      ]
     },
     "nota": "Motte stampa «as SI is to SL2»: manca il quadrato su SI (latino: «SI quad. ad SL quad.»)."
    },
    {
     "id": "L1-P24-p7",
     "la": "",
     "it": "I punti S, P, Z giacciono dunque su una stessa retta.",
     "en": "Wherefore the points S, P, Z, are in one right line.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "S, P, Z allineati"
      ]
     }
    },
    {
     "id": "L1-P24-p8",
     "la": "",
     "it": "Inoltre, se le tangenti si incontrano in G, il rettangolo XIY, ossia IZ², starà (per la teoria delle coniche) a IA² come GP² sta a GA², e quindi IZ starà a IA come GP sta a GA.",
     "en": "Moreover, since the tangents meet in G, the rectangle XIY or IZ2 will (by the properties of the conic sections) be to IA2 as GP2 is to GA2, and consequently IZ will be to IA as GP to GA.",
     "dipende_da": [
      "Coniche (ex conicis)"
     ],
     "figura": {
      "mostra": [
       "G"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P24-p9",
     "la": "",
     "it": "I punti P, Z e A giacciono dunque su una stessa retta, e perciò i punti S, P e A sono su una stessa retta.",
     "en": "Wherefore the points P, Z, A, lie in one right line, and therefore the points S, P, and A are in one right line.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "P, Z, A allineati"
      ]
     }
    },
    {
     "id": "L1-P24-p10",
     "la": "",
     "it": "E con lo stesso argomento si proverà che i punti R, P e A sono su una stessa retta.",
     "en": "And the same argument will prove that the points R, P, and A are in one right line.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P24-p11",
     "la": "",
     "it": "I punti di contatto A e P giacciono dunque sulla retta RS.",
     "en": "Wherefore the points of contact A and P lie in the right line RS.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "A, P su RS"
      ]
     }
    },
    {
     "id": "L1-P24-p12",
     "la": "",
     "it": "Trovati questi, la traiettoria si descriverà come nel primo caso del problema precedente. C.V.F.",
     "en": "But after these points are found, the trajectory may be described, as in the first Case of the preceding Problem. Q.E.F.",
     "dipende_da": [
      "Prop. XXIII, Caso 1"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L1-Lem22",
   "tipo": "Lemma",
   "titolo": "Lemma XXII — trasformazione delle figure",
   "copertura": [
    "S5.38",
    "S5.39",
    "S5.40",
    "S5.41"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 141–142"
   },
   "enunciato": {
    "la": "",
    "it": "Mutare figure in altre figure dello stesso genere.",
    "en": "To transform figures into other figures of the same kind."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "O",
     "L",
     "a",
     "G",
     "D",
     "d",
     "g",
     "H",
     "I",
     "h",
     "i"
    ],
    "vincoli": [
     "AO ∥ BL",
     "O su AO; OABa parallelogramma",
     "GD ∥ OA; d = OD ∩ BL",
     "dg sotto angolo dato con BL; dg : Od = DG : OD"
    ]
   },
   "passi": [
    {
     "id": "L1-Lem22-p1",
     "la": "",
     "it": "Si debba trasformare una figura qualsiasi HGI.",
     "en": "Suppose that any figure HGI is to be transformed.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "figura HGI"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem22-p2",
     "la": "",
     "it": "Si conducano a piacere due rette parallele AO, BL, che taglino in A e B una terza retta qualsiasi AB data di posizione, e da un punto qualsiasi G della figura si conduca alla retta AB una retta GD parallela a OA.",
     "en": "Draw, at pleasure, two parallel lines AO, BL, cutting any third line AB, given by position, in A and B, and from any point G of the figure, draw out any right line GD, parallel to OA, till it meet the right line AB.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "AO ∥ BL",
       "AB",
       "G",
       "GD ∥ OA",
       "D"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem22-p3",
     "la": "",
     "it": "Poi da un punto O, dato sulla linea OA, si conduca al punto D la retta OD, che incontri BL in d, e dal punto d’incontro si innalzi una retta dg che formi con la retta BL un angolo dato qualsiasi e abbia con Od il rapporto che DG ha con OD: g sarà il punto della figura nuova hgi corrispondente al punto G.",
     "en": "Then from any given point O in the line OA, draw to the point D the right line OD, meeting BL in d; and from the point of concourse raise the right line dg containing any given angle with the right line BL, and having such ratio to Od as DG has to OD; and g will be the point in the new figure hgi, corresponding to the point G.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "O",
       "OD",
       "d",
       "dg",
       "g"
      ],
      "evidenzia": [
       "dg : Od = DG : OD"
      ]
     }
    },
    {
     "id": "L1-Lem22-p4",
     "la": "",
     "it": "Allo stesso modo i singoli punti della prima figura daranno altrettanti punti della figura nuova.",
     "en": "And in like manner the several points of the first figure will give as many correspondent points of the new figure.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem22-p5",
     "la": "",
     "it": "Immagina dunque che il punto G percorra con moto continuo tutti i punti della prima figura: anche il punto g percorrerà con moto continuo tutti i punti della figura nuova e la descriverà.",
     "en": "If we therefore conceive the point G to be carried along by a continual motion through all the points of the first figure, the point g will be likewise carried along by a continual motion through all the points of the new figure, and describe the same.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "figura nuova hgi"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem22-p6",
     "la": "",
     "it": "Per distinguerli, chiamiamo DG prima ordinata, dg nuova ordinata; AD prima ascissa, ad nuova ascissa; O polo, OD raggio secante, OA primo raggio ordinato e Oa (con il quale si completa il parallelogramma OABa) nuovo raggio ordinato.",
     "en": "For distinction's sake, let us call DG the first ordinate, dg the new ordinate, AD the first abscissa, ad the new abscissa; O the pole, OD the abscinding radius, OA the first ordinate radius, and Oa (by which the parallelogram OABa is completed) the new ordinate radius.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "a (parallelogramma OABa)"
      ],
      "evidenzia": [
       "nomi: ordinate, ascisse, polo, raggi"
      ]
     }
    },
    {
     "id": "L1-Lem22-p7",
     "la": "",
     "it": "Dico ora che, se il punto G si trova su una linea retta data di posizione, anche il punto g si troverà su una linea retta data di posizione.",
     "en": "I say, then, that if the point G is placed in a right line given by position, the point g will be also placed in a right line given by position.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem22-p8",
     "la": "",
     "it": "Se il punto G si trova su una sezione conica, anche il punto g si troverà su una sezione conica.",
     "en": "If the point G is placed in a conic section, the point g will be likewise placed in a conic section.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem22-p9",
     "la": "",
     "it": "Qui conto il cerchio fra le sezioni coniche.",
     "en": "And here I understand the circle as one of the conic sections.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem22-p10",
     "la": "",
     "it": "Inoltre, se il punto G si trova su una linea del terzo ordine analitico, il punto g si troverà su una linea ugualmente del terzo ordine; e così per le linee curve degli ordini superiori.",
     "en": "But farther, if the point G is placed in a line of the third analytical order, the point g will also be placed in a line of the third order, and so on in curve lines of higher orders.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "La trascrizione ha «Por ro», parola spezzata dal marcatore di pagina <88>."
    },
    {
     "id": "L1-Lem22-p11",
     "la": "",
     "it": "Le due linee su cui si trovano i punti G, g saranno sempre dello stesso ordine analitico.",
     "en": "The two lines in which the points G, g, are placed, will be always of the same analytical order.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem22-p12",
     "la": "",
     "it": "Infatti, come ad sta a OA, così stanno Od a OD, dg a DG e AB ad AD; e perciò AD è uguale a OA × AB/ad, e DG è uguale a OA × dg/ad.",
     "en": "For as ad is to OA, so are Od to OD, dg to DG, and AB to AD; and therefore AD is equal to , and DG equal to",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "AD = OA × AB/ad",
       "DG = OA × dg/ad"
      ]
     },
     "nota": "La trascrizione appiattisce le frazioni: «OA×ABad» vale OA × AB/ad, «OA×dgad» vale OA × dg/ad. In Motte sono immagini (SVG 109, 110), lette allo stesso modo."
    },
    {
     "id": "L1-Lem22-p13",
     "la": "",
     "it": "Ora, se il punto G si trova su una linea retta, e perciò in qualsiasi equazione che esprima la relazione fra l’ascissa AD e l’ordinata DG quelle indeterminate AD e DG salgono a una sola dimensione, scrivendo in questa equazione OA × AB/ad al posto di AD e OA × dg/ad al posto di DG si produrrà un’equazione nuova, nella quale l’ascissa nuova ad e l’ordinata nuova dg saliranno a una sola dimensione, e che perciò designa una linea retta.",
     "en": "Now if the point G is placed in a right line, and therefore, in any equation by which the relation between the abscissa AD and the ordinate GD is expressed, those indetermined lines AD and DG rise no higher than to one dimension, by writing this equation in place of AD, and in place of DG, a new equation will be produced, in which the new abscissa ad and new ordinate dg rise only to one dimension; and which therefore must denote a right line.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem22-p14",
     "la": "",
     "it": "Se invece AD e DG, o una di esse, salivano a due dimensioni nella prima equazione, anche ad e dg saliranno a due nella seconda equazione.",
     "en": "But if AD and DG (or either of them) had risen to two dimensions in the first equation, ad and dg would likewise have risen to two dimensions in the second equation.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem22-p15",
     "la": "",
     "it": "E così per tre o più dimensioni.",
     "en": "And so on in three or more dimensions.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem22-p16",
     "la": "",
     "it": "Le indeterminate ad, dg nella seconda equazione e AD, DG nella prima saliranno sempre allo stesso numero di dimensioni, e perciò le linee su cui si trovano i punti G, g sono dello stesso ordine analitico.",
     "en": "The indetermined lines, ad, dg in the second equation, and AD, DG, in the first, will always rise to the same number of dimensions; and therefore the lines in which the points G, g, are placed are of the same analytical order.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem22-p17",
     "la": "",
     "it": "Dico inoltre che, se una retta tocca una linea curva nella prima figura, questa retta, trasferita nella figura nuova nello stesso modo della curva, toccherà quella linea curva nella figura nuova; e viceversa.",
     "en": "I say farther, that if any right line touches the curve line in the first figure, the same right line transferred the same way with the curve into the new figure will touch that curve line in the new figure, and vice versa.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tangente nella prima figura e sua immagine"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem22-p18",
     "la": "",
     "it": "Infatti, se due punti qualsiasi della curva si avvicinano l’uno all’altro e si riuniscono nella prima figura, gli stessi punti, trasferiti, si avvicineranno l’uno all’altro e si riuniranno nella figura nuova; e perciò le rette che congiungono questi punti diventeranno insieme tangenti alle curve nell’una e nell’altra figura.",
     "en": "For if any two points of the curve in the first figure are supposed to approach one the other till they come to coincide, the same points transferred will approach one the other till they come to coincide in the new figure; and therefore the right lines with which those points are joined will become together tangents of the curves in both figures.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L1-P25",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXV, Probl. XVII — due punti e tre tangenti",
   "copertura": [
    "S5.45",
    "S5.46"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 143–144"
   },
   "enunciato": {
    "la": "",
    "it": "Descrivere una traiettoria che passi per due punti dati e tocchi tre rette date di posizione.",
    "en": "To describe a trajectory that shall pass through two given points, and touch three right lines given by position."
   },
   "figura_base": {
    "punti": [
     "h",
     "i",
     "k",
     "l",
     "a",
     "b",
     "c",
     "d",
     "e"
    ],
    "vincoli": [
     "figura nuova: hi ∥ kl tangenti, ik tangente",
     "hl ∥ ik passa per a, b",
     "c su hi, d su ik, e su kl punti di contatto"
    ]
   },
   "passi": [
    {
     "id": "L1-P25-p1",
     "la": "",
     "it": "Per il punto d’incontro di due tangenti qualsiasi fra loro e per il punto d’incontro della terza tangente con la retta che passa per i due punti dati conduci una retta infinita; e, assunta questa come primo raggio ordinato, si trasformi la figura, per il lemma precedente, in una figura nuova.",
     "en": "Through the concourse of any two of the tangents one with the other, and the concourse of the third tangent with the right line which passes through the two given points, draw an indefinite right line; and, taking this line for the first ordinate radius, transform the figure by the preceding Lemma into a new figure.",
     "dipende_da": [
      "Lemma XXII"
     ],
     "figura": {
      "mostra": [
       "tre tangenti",
       "due punti dati",
       "retta per i due punti",
       "primo raggio ordinato"
      ],
      "evidenzia": []
     },
     "nota": "«per lemma superius» rimanda al Lemma XXII."
    },
    {
     "id": "L1-P25-p2",
     "la": "",
     "it": "In questa figura quelle due tangenti diventeranno parallele fra loro, e la terza tangente diventerà parallela alla retta che passa per i due punti.",
     "en": "In this figure those two tangents will become parallel to each other, and the third tangent will be parallel to the right line that passes through the two given points.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P25-p3",
     "la": "",
     "it": "Siano hi, kl quelle due tangenti parallele, ik la terza tangente, e hl la retta parallela a questa che passa per i punti a, b, per i quali la sezione conica deve passare in questa figura nuova, e che completa il parallelogramma hikl.",
     "en": "Suppose hi, kl to be those two parallel tangents, ik the third tangent, and hl a right line parallel thereto, passing through those points a, b, through which the conic section ought to pass in this new figure; and completing the parallelogram hikl,",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "hi ∥ kl",
       "ik",
       "hl ∥ ik",
       "a, b",
       "parallelogramma hikl"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P25-p4",
     "la": "",
     "it": "Si dividano le rette hi, ik, kl in c, d, e in modo che hc stia al lato quadrato del rettangolo ahb, ic a id e ke a kd come la somma delle rette hi e kl sta alla somma di tre linee, delle quali la prima è la retta ik e le altre due sono i lati quadrati dei rettangoli ahb e alb: c, d, e saranno i punti di contatto.",
     "en": "let the right lines hi, ik, kl be so cut in c, d, e, that hc may be to the square root of the rectangle ahb, ic, to id, and ke to kd, as the sum of the right lines hi and kl is to the sum of the three lines, the first whereof is the right line ik, and the other two are the square roots of the rectangles ahb and alb; and c, d, e, will be the points of contact.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "c, d, e"
      ],
      "evidenzia": [
       "hc : √ahb = ic : id = ke : kd"
      ]
     }
    },
    {
     "id": "L1-P25-p5",
     "la": "",
     "it": "Infatti, per la teoria delle coniche, hc² sta al rettangolo ahb, ic² a id², ke² a kd² ed el² al rettangolo alb nello stesso rapporto; e perciò hc sta al lato quadrato di ahb, ic a id, ke a kd ed el al lato quadrato di alb nel rapporto subduplicato di quello, e, componendo, nel rapporto dato di tutti gli antecedenti, hi e kl, a tutti i conseguenti, che sono il lato quadrato del rettangolo ahb, la retta ik e il lato quadrato del rettangolo alb.",
     "en": "For by the properties of the conic sections, hc2 to the rectangle ahb, and ic2 to id2, and ke2 to kd2, and el2 to the rectangle alb, are all in the same ratio; and therefore hc to the square root of ahb, ic to id, ke to kd, and el to the square root of alb, are in the subduplicate of that ratio; and by composition, in the given ratio of the sum of all the antecedents hi + kl, to the sum of all the consequents",
     "dipende_da": [
      "Coniche (ex conicis)"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "rapporto composto (hi + kl) : (√ahb + ik + √alb)"
      ]
     },
     "nota": "In Motte la somma dei conseguenti è un’immagine (SVG 111): √ahb + ik + √alb."
    },
    {
     "id": "L1-P25-p6",
     "la": "",
     "it": "Da quel rapporto dato si hanno dunque i punti di contatto c, d, e nella figura nuova.",
     "en": "Wherefore from that given ratio we have the points of contact c, d, e, in the new figure.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P25-p7",
     "la": "",
     "it": "Con le operazioni inverse dell’ultimo lemma si trasferiscano questi punti nella prima figura, e là (per il Probl. XIV) si descriverà la traiettoria. C.V.F.",
     "en": "By the inverted operations of the last Lemma, let those points be transferred into the first figure, and the trajectory will be there described by Prob. XIV. Q.E.F.",
     "dipende_da": [
      "Lemma XXII",
      "Probl. XIV (Prop. XXII)"
     ],
     "figura": {
      "mostra": [
       "punti trasferiti nella prima figura",
       "traiettoria"
      ],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L1-P26",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXVI, Probl. XVIII — un punto e quattro tangenti",
   "copertura": [
    "S5.48",
    "S5.49"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 144"
   },
   "enunciato": {
    "la": "",
    "it": "Descrivere una traiettoria che passi per un punto dato e tocchi quattro rette date di posizione.",
    "en": "To describe a trajectory that shall pass through a given point, and touch four right lines given by position."
   },
   "figura_base": {
    "punti": [
     "h",
     "i",
     "k",
     "l",
     "O",
     "p",
     "q"
    ],
    "vincoli": [
     "figura nuova: hikl parallelogramma di tangenti",
     "O centro del parallelogramma",
     "Oq = Op, q opposto a p"
    ]
   },
   "passi": [
    {
     "id": "L1-P26-p1",
     "la": "",
     "it": "Dall’intersezione comune di due tangenti qualsiasi all’intersezione comune delle altre due si conduca una retta infinita e, assunta questa come primo raggio ordinato, si trasformi la figura (per il Lemma XXII) in una figura nuova: le tangenti che a due a due concorrevano sul raggio ordinato diventeranno ora parallele.",
     "en": "From the common intersections, of any two of the tangents to the common intersection of the other two, draw an indefinite right line; and taking this line for the first ordinate radius, transform the figure (by Lem. XXII) into a new figure, and the two pairs of tangents, each of which before concurred in the first ordinate radius, will now become parallel.",
     "dipende_da": [
      "Lemma XXII"
     ],
     "figura": {
      "mostra": [
       "quattro tangenti",
       "punto dato",
       "primo raggio ordinato"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P26-p2",
     "la": "",
     "it": "Siano queste hi e kl, ik e hl, che comprendono il parallelogramma hikl.",
     "en": "Let hi and kl, ik and hl, be those pairs of parallels completing the parallelogram hikl.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "parallelogramma hikl"
      ],
      "evidenzia": []
     },
     "nota": "La trascrizione ha «Sun to», parola spezzata dal marcatore di pagina <91>."
    },
    {
     "id": "L1-P26-p3",
     "la": "",
     "it": "E sia p il punto che in questa figura nuova corrisponde al punto dato nella prima figura.",
     "en": "And let p be the point in this new figure corresponding to the given point in the first figure.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "p"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P26-p4",
     "la": "",
     "it": "Per il centro O della figura si conduca pq, e, se Oq è uguale a Op, q sarà l’altro punto per il quale la sezione conica deve passare in questa figura nuova.",
     "en": "Through O the centre of the figure draw pq: and Oq being equal to Op, q will be the other point through which the conic section must pass in this new figure.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "centro O",
       "q (Oq = Op)"
      ],
      "evidenzia": [
       "simmetria centrale"
      ]
     }
    },
    {
     "id": "L1-P26-p5",
     "la": "",
     "it": "Con l’operazione inversa del Lemma XXII si trasferisca questo punto nella prima figura: là si avranno due punti per i quali si deve descrivere la traiettoria.",
     "en": "Let this point be transferred, by the inverse operation of Lem. XXII into the first figure, and there we shall have the two points through which the trajectory is to be described.",
     "dipende_da": [
      "Lemma XXII"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P26-p6",
     "la": "",
     "it": "E per essi quella traiettoria si può descrivere per il Probl. XVII. C.V.F.",
     "en": "But through those points that trajectory may be described by Prop. XVII.",
     "dipende_da": [
      "Probl. XVII (Prop. XXV)"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     },
     "nota": "Motte scrive «Prop. XVII»: il latino ha «problema xvii», cioè la Prop. XXV. Motte omette anche Q.E.F."
    }
   ]
  },
  {
   "id": "L1-Lem23",
   "tipo": "Lemma",
   "titolo": "Lemma XXIII — il punto che divide CD in rapporto dato descrive una retta",
   "copertura": [
    "S5.50",
    "S5.51"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 144–145"
   },
   "enunciato": {
    "la": "",
    "it": "Se due rette date di posizione, AC e BD, terminano nei punti dati A, B e hanno fra loro un rapporto dato, e la retta CD, che congiunge i punti indeterminati C, D, è divisa in K in un rapporto dato: dico che il punto K sarà situato su una retta data di posizione.",
    "en": "If two right lines, as AC, BD given by position, and terminating in given points A, B, are in a given ratio one to the other, and the right line CD, by which the indetermined points C, D are joined is cut in K in a given ratio; I say, that the point K will be placed in a right line given by position."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "D",
     "E",
     "G",
     "F",
     "K",
     "L",
     "H"
    ],
    "vincoli": [
     "A, B fissi; C sulla retta AC, D sulla retta BD",
     "AC : BD dato",
     "K su CD con CK : CD dato",
     "E = AC ∩ BD; G su BE; F su BD con FD = EG"
    ]
   },
   "passi": [
    {
     "id": "L1-Lem23-p1",
     "la": "",
     "it": "Le rette AC, BD si incontrino infatti in E; su BE si prenda BG che stia ad AE come BD sta ad AC, e FD sia sempre uguale alla data EG: per costruzione EC starà a GD, cioè a EF, come AC sta a BD, e quindi in un rapporto dato; e perciò il triangolo EFC sarà dato di forma.",
     "en": "For let the right lines AC, BD meet in E, and in BE take BG to AE as BD is to AC, and let FD be always equal to the given line EG; and, by construction, EC will be to GD, that is, to EF, as AC to BD, and therefore in a given ratio; and therefore the triangle EFC will be given in kind.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A, B",
       "rette AC, BD",
       "C, D",
       "E",
       "G (BG : AE = BD : AC)",
       "F (FD = EG)",
       "triangolo EFC"
      ],
      "evidenzia": [
       "EC : EF = AC : BD"
      ]
     }
    },
    {
     "id": "L1-Lem23-p2",
     "la": "",
     "it": "Si divida CF in L in modo che CL stia a CF nel rapporto di CK a CD; poiché quel rapporto è dato, sarà dato di forma anche il triangolo EFL, e quindi il punto L sarà situato sulla retta EL data di posizione.",
     "en": "Let CF be cut in L so as CL may be to CF in the ratio of CK to CD; and because that is a given ratio, the triangle EFL will be given in kind, and therefore the point L will be placed in the right line EL given by position.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "K",
       "L",
       "retta EL"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem23-p3",
     "la": "",
     "it": "Congiungi LK: i triangoli CLK, CFD saranno simili; e, poiché FD è data ed è dato il rapporto di LK a FD, sarà data LK.",
     "en": "Join LK, and the triangles CLK, CFD will be similar; and because FD is a given line, and LK is to FD in a given ratio, LK will be also given.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "LK"
      ],
      "evidenzia": [
       "triangoli CLK, CFD"
      ]
     }
    },
    {
     "id": "L1-Lem23-p4",
     "la": "",
     "it": "Si prenda EH uguale a questa: ELKH sarà sempre un parallelogramma.",
     "en": "To this let EH be taken equal, and ELKH will be always a parallelogram.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "H",
       "parallelogramma ELKH"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem23-p5",
     "la": "",
     "it": "Il punto K è dunque situato sul lato HK di quel parallelogramma, dato di posizione. C.V.D.",
     "en": "And therefore the point K is always placed in the side HK (given by position) of that parallelogram. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "retta HK luogo di K"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-Lem24",
   "tipo": "Lemma",
   "titolo": "Lemma XXIV — semidiametro medio proporzionale fra i segmenti di due tangenti parallele",
   "copertura": [
    "S5.53",
    "S5.54",
    "S5.55"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 145"
   },
   "enunciato": {
    "la": "",
    "it": "Se tre rette toccano una sezione conica qualsiasi, e due di esse sono parallele e date di posizione: dico che il semidiametro della sezione parallelo a queste due è medio proporzionale fra i loro segmenti compresi fra i punti di contatto e la terza tangente.",
    "en": "If three right lines, two whereof are parallel, and given by position, touch any conic section; I say, that the semi-diameter of the section which is parallel to those two is a mean proportional between the segments of those two that are intercepted between the points of contact and the third tangent."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "D",
     "M",
     "F",
     "G",
     "I",
     "E",
     "H",
     "K",
     "L"
    ],
    "vincoli": [
     "AF ∥ GB tangenti in A, B",
     "FG tangente in I",
     "AB, DM diametri coniugati; CD ∥ AF",
     "IKCL parallelogramma"
    ]
   },
   "passi": [
    {
     "id": "L1-Lem24-p1",
     "la": "",
     "it": "Siano AF, GB due parallele che toccano la sezione conica ADB in A e B; EF una terza retta che tocca la sezione conica in I e incontra le prime tangenti in F e G; e sia CD il semidiametro della figura parallelo alle tangenti: dico che AF, CD, BG sono in proporzione continua.",
     "en": "Let AF, GB be the two parallels touching the conic section ADB in A and B; EF the third right line touching the conic section in I, and meeting the two former tangents in F and G, and let CD be the semi-diameter of the figure parallel to those tangents; I say, that AF, CD, BG are continually proportional.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "conica ADB",
       "tangenti parallele AF, GB",
       "tangente EF in I",
       "F, G",
       "semidiametro CD"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem24-p2",
     "la": "",
     "it": "Infatti, se i diametri coniugati AB, DM incontrano la tangente FG in E e H e si tagliano a vicenda in C, e si completa il parallelogramma IKCL, per la natura delle sezioni coniche come EC sta a CA così CA sta a LC, e così, separando, EC − CA sta a CA − CL, ossia EA ad AL; e, componendo, EA sta a EA + AL, ossia a EL, come EC sta a EC + CA, ossia a EB; e perciò, per la similitudine dei triangoli EAF, ELI, ECH, EBG, AF sta a LI come CH sta a BG.",
     "en": "For if the conjugate diameters AB, DM meet the tangent FG in E and H, and cut one the other in C, and the parallelogram IKCL be completed; from the nature of the conic sections, EC will be to CA as CA to CL; and so by division, EC - CA to CA - CL, or EA to AL; and by composition, EA to EA + AL or EL, as EC to EC + CA or EB; and therefore (because of the similitude of the triangles EAF, ELI, ECH, EBG) AF is to LI as CH to BG.",
     "dipende_da": [
      "Coniche (ex natura sectionum conicarum)"
     ],
     "figura": {
      "mostra": [
       "diametri coniugati AB, DM",
       "C",
       "E, H",
       "parallelogramma IKCL"
      ],
      "evidenzia": [
       "EC : CA = CA : LC",
       "triangoli EAF, ELI, ECH, EBG"
      ]
     }
    },
    {
     "id": "L1-Lem24-p3",
     "la": "",
     "it": "Parimenti, per la natura delle sezioni coniche, LI, ossia CK, sta a CD come CD sta a CH; e perciò, per uguaglianza perturbata, AF sta a CD come CD sta a BG. C.V.D.",
     "en": "Likewise, from the nature of the conic sections, LI (or CK) is to CD as CD to CH; and therefore (ex æquo perturbatè) AF is to CD as CD to BG. Q.E.D.",
     "dipende_da": [
      "Coniche (ex natura sectionum conicarum)"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "CK : CD = CD : CH",
       "AF × BG = CD²"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-Lem25",
   "tipo": "Lemma",
   "titolo": "Lemma XXV — parallelogramma circoscritto e quinta tangente",
   "copertura": [
    "S5.58",
    "S5.59"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 145–146"
   },
   "enunciato": {
    "la": "",
    "it": "Se i quattro lati di un parallelogramma, prolungati indefinitamente, toccano una sezione conica qualsiasi e sono tagliati da una quinta tangente qualsiasi, e si prendono, su due lati contigui qualsiasi, le parti staccate che terminano negli angoli opposti del parallelogramma: dico che una delle due parti staccate sta al lato dal quale è staccata come la parte dell’altro lato contiguo compresa fra il punto di contatto e il terzo lato sta all’altra parte staccata.",
    "en": "If four sides of a parallelogram indefinitely produced touch any conic section, and are cut by a fifth tangent; I say, that, taking those segments of any two conterminous sides that terminate in opposite angles of the parallelogram, either segment is to the side from which it is cut off as that part of the other conterminous side which is intercepted between the point of contact and the third side is to the other segment."
   },
   "figura_base": {
    "punti": [
     "M",
     "L",
     "K",
     "I",
     "A",
     "B",
     "C",
     "D",
     "F",
     "Q",
     "H",
     "E"
    ],
    "vincoli": [
     "MLKI parallelogramma circoscritto: ML in A, IK in B, KL in C, MI in D",
     "quinta tangente FQ: F su ML, Q su IK, H su KL, E su MI"
    ]
   },
   "passi": [
    {
     "id": "L1-Lem25-p1",
     "la": "",
     "it": "I quattro lati ML, IK, KL, MI del parallelogramma MLIK tocchino la sezione conica in A, B, C, D, e la quinta tangente FQ tagli questi lati in F, Q, H ed E; si prendano poi le parti staccate ME, KQ dei lati MI, KI, oppure le parti staccate KH, MF dei lati KL, ML: dico che ME sta a MI come BK sta a KQ, e KH sta a KL come AM sta a MF.",
     "en": "Let the four sides ML, IK, KL, MI, of the parallelogram MLIK touch the conic section in A, B, C, D; and let the fifth tangent FQ cut those sides in F, Q, H, and E; and taking the segments ME, KQ of the sides MI, KI, or the segments KH, MF of the sides KL, ML, I say, that ME is to MI as BK to KQ; and KH to KL as AM to MF.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "parallelogramma MLKI circoscritto",
       "contatti A, B, C, D",
       "quinta tangente FQ",
       "F, Q, H, E"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem25-p2",
     "la": "",
     "it": "Infatti, per il corollario del lemma precedente, ME sta a EI come AM, ossia BK, sta a BQ, e, componendo, ME sta a MI come BK sta a KQ. C.V.D.",
     "en": "For, by Cor. 1 of the preceding Lemma, ME is to EI as (AM or) BK to BQ; and, by composition, ME is to MI as BK to KQ. Q.E.D.",
     "dipende_da": [
      "Lemma XXIV, Cor. 1"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "ME : EI = BK : BQ"
      ]
     },
     "nota": "Il latino dice «per corollarium lemmatis superioris»; Motte precisa «Cor. 1»."
    },
    {
     "id": "L1-Lem25-p3",
     "la": "",
     "it": "Così pure KH sta a HL come (BK, ossia) AM sta ad AF, e, separando, KH sta a KL come AM sta a MF. C.V.D.",
     "en": "Also KH is to HL as (BK or) AM to AF; and by division, KH to KL as AM to MF. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "KH : HL = AM : AF"
      ]
     },
     "nota": "La trascrizione apre una parentesi che non chiude: «(BK seu AM»; va letto «(BK seu) AM», come in Motte."
    }
   ]
  },
  {
   "id": "L1-Lem25-Cor3",
   "tipo": "Corollarium",
   "titolo": "Lemma XXV, Cor. 3 — la retta dei punti di mezzo passa per il centro",
   "copertura": [
    "S5.62"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 146"
   },
   "enunciato": {
    "la": "",
    "it": "Cor. 3. Di qui anche, se si congiungono Eq, eQ e si dividono a metà, e per i punti di bisezione si conduce una retta, questa passerà per il centro della sezione conica.",
    "en": "COR. 3. Hence, also, if Eq, eQ, are joined and bisected, and a right line is drawn through the points of bisection, this right line will pass through the centre of the conic section."
   },
   "figura_base": {
    "punti": [
     "M",
     "K",
     "I",
     "E",
     "Q",
     "e",
     "q"
    ],
    "vincoli": [
     "tangenti KI, MI; quinta tangente EQ; sesta tangente eq",
     "E, e su MI; Q, q su KI"
    ]
   },
   "passi": [
    {
     "id": "L1-Lem25-Cor3-p1",
     "la": "",
     "it": "Infatti, poiché Qq sta a Ee come KQ sta a Me, la stessa retta passerà per il punto di mezzo di tutte le rette Eq, eQ, MK (per il Lemma XXIII), e il punto di mezzo della retta MK è il centro della sezione.",
     "en": "For since Qq is to Ee as KQ to Me, the same right line will pass through the middle of all the lines Eq, eQ, MK (by Lem. XXIII), and the middle point of the right line MK is the centre of the section.",
     "dipende_da": [
      "Lemma XXIII"
     ],
     "figura": {
      "mostra": [
       "MK e suo punto di mezzo"
      ],
      "evidenzia": [
       "tre punti di mezzo allineati (Lemma XXIII)"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P27",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXVII, Probl. XIX — cinque tangenti",
   "copertura": [
    "S5.63",
    "S5.64"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 146–147"
   },
   "enunciato": {
    "la": "",
    "it": "Descrivere una traiettoria che tocchi cinque rette date di posizione.",
    "en": "To describe a trajectory that may touch five right lines given by position."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "D",
     "E",
     "F",
     "G",
     "M",
     "N",
     "P",
     "Q",
     "O",
     "K",
     "L",
     "R"
    ],
    "vincoli": [
     "tangenti ABG, BCF, GCD, FDE, EA",
     "M, N punti di mezzo di AF, BE; P, Q di BD, GF",
     "KL ∥ BC con O a metà"
    ]
   },
   "passi": [
    {
     "id": "L1-P27-p1",
     "la": "",
     "it": "Siano date di posizione le tangenti ABG, BCF, GCD, FDE, EA.",
     "en": "Supposing ABG, BCF, GCD, FDE, EA to be the tangents given by position.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cinque tangenti ABG, BCF, GCD, FDE, EA"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P27-p2",
     "la": "",
     "it": "Dividi a metà in M e N le diagonali AF, BE della figura quadrilatera ABFE, compresa da quattro qualsiasi di esse: per il Cor. 3 del Lemma XXV la retta MN, condotta per i punti di bisezione, passerà per il centro della traiettoria.",
     "en": "Bisect in M and N, AF, BE, the diagonals of the quadrilateral figure ABFE contained under any four of them; and (by Cor. 3, Lem. XXV) the right line MN drawn through the points of bisection will pass through the centre of the trajectory.",
     "dipende_da": [
      "Lemma XXV, Cor. 3"
     ],
     "figura": {
      "mostra": [
       "quadrilatero ABFE",
       "diagonali AF, BE",
       "M, N",
       "retta MN"
      ],
      "evidenzia": []
     },
     "nota": "La trascrizione ha «dia gonales», parola spezzata dal marcatore di pagina <95>."
    },
    {
     "id": "L1-P27-p3",
     "la": "",
     "it": "Di nuovo, dividi a metà in P e Q le diagonali (per così dire) BD, GF della figura quadrilatera BGDF, compresa da altre quattro tangenti qualsiasi: anche la retta PQ, condotta per i punti di bisezione, passerà per il centro della traiettoria.",
     "en": "Again, bisect in P and Q the diagonals (if I may so call them) BD, GF of the quadrilateral figure BGDF contained under any other four tangents, and the right line PQ drawn through the points of bisection will pass through the centre of the",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "quadrilatero BGDF",
       "P, Q",
       "retta PQ"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P27-p4",
     "la": "",
     "it": "Il centro sarà dunque dato nel punto d’incontro delle bisecanti.",
     "en": "and therefore the centre will be given in the concourse of the bisecting lines.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P27-p5",
     "la": "",
     "it": "Sia esso O.",
     "en": "Suppose it to be O.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "O"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P27-p6",
     "la": "",
     "it": "Conduci KL parallela a una tangente qualsiasi BC, a una distanza tale che il centro O si trovi a metà fra le parallele: KL, così condotta, toccherà la traiettoria da descrivere.",
     "en": "Parallel to any tangent BC draw KL at such distance that the centre O may be placed in the middle between the parallels; this KL will touch the trajectory to be described.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "KL ∥ BC, simmetrica rispetto a O"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P27-p7",
     "la": "",
     "it": "Essa tagli due altre tangenti qualsiasi, GCD e FDE, in L e K.",
     "en": "Let this cut any other two tangents GCD, FDE, in L and K.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "L, K"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P27-p8",
     "la": "",
     "it": "Per i punti d’incontro C e K, F e L di queste tangenti non parallele CL, FK con le parallele CF, KL conduci CK, FL, che si incontrino in R: la retta OR, condotta e prolungata, taglierà le tangenti parallele CF, KL nei punti di contatto.",
     "en": "Through the points C and K, F and L, where the tangents not parallel, CL, FK meet the parallel tangents CF, KL, draw CK, FL meeting in R; and the right line OR drawn and produced, will cut the parallel tangents CF, KL, in the points of contact.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "CK, FL",
       "R",
       "retta OR"
      ],
      "evidenzia": [
       "punti di contatto su CF e KL"
      ]
     }
    },
    {
     "id": "L1-P27-p9",
     "la": "",
     "it": "Ciò è evidente per il Cor. 2 del Lemma XXIV.",
     "en": "This appears from Cor. 2, Lem. XXIV.",
     "dipende_da": [
      "Lemma XXIV, Cor. 2"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P27-p10",
     "la": "",
     "it": "Con lo stesso metodo si possono trovare gli altri punti di contatto, e infine descrivere la traiettoria con la costruzione del Probl. XIV. C.V.F.",
     "en": "And by the same method the other points of contact may be found, and then the trajectory may be described by Prob. XIV. Q.E.F.",
     "dipende_da": [
      "Probl. XIV (Prop. XXII)"
     ],
     "figura": {
      "mostra": [
       "traiettoria"
      ],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L1-Lem26",
   "tipo": "Lemma (problema)",
   "titolo": "Lemma XXVI — vertici di un triangolo dato su tre rette date",
   "copertura": [
    "S5.69",
    "S5.70",
    "S5.71"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 148–149"
   },
   "enunciato": {
    "la": "",
    "it": "Porre i tre angoli di un triangolo dato di forma e di grandezza su altrettante rette date di posizione, non tutte parallele, ciascun angolo su ciascuna retta.",
    "en": "To place the three angles of a triangle, given both in kind and magnitude, in respect of as many right lines given by position, provided they are not all parallel among themselves, in such manner that the several angles may touch the several lines."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "D",
     "E",
     "F",
     "R",
     "G",
     "M",
     "P",
     "Q",
     "a",
     "b",
     "c",
     "n"
    ],
    "vincoli": [
     "rette AB, AC, BC",
     "segmenti DRE, DGF, EMF capaci di BAC, ABC, ACB",
     "G seconda intersezione dei primi due cerchi",
     "Ga : AB = GP : PQ"
    ]
   },
   "passi": [
    {
     "id": "L1-Lem26-p1",
     "la": "",
     "it": "Sono date di posizione tre rette infinite AB, AC, BC, e bisogna collocare il triangolo DEF in modo che il suo angolo D tocchi la linea AB, l’angolo E la linea AC e l’angolo F la linea BC.",
     "en": "Three indefinite right lines AB, AC, BC, are given by position, and it is required so to place the triangle DEF that its angle D may touch the line AB, its angle E the line AC, and its angle F the line BC.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "rette AB, AC, BC",
       "triangolo DEF"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem26-p2",
     "la": "",
     "it": "Su DE, DF ed EF descrivi tre segmenti di cerchio DRE, DGF, EMF, che siano capaci di angoli uguali rispettivamente agli angoli BAC, ABC, ACB.",
     "en": "Upon DE, DF, and EF, describe three segments of circles DRE, DGF, EMF, capable of angles equal to the angles BAC, ABC, ACB respectively.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "segmenti DRE, DGF, EMF"
      ],
      "evidenzia": [
       "capaci di BAC, ABC, ACB"
      ]
     }
    },
    {
     "id": "L1-Lem26-p3",
     "la": "",
     "it": "Questi segmenti siano descritti da quella parte delle linee DE, DF, EF per cui le lettere DRED girino in cerchio nello stesso ordine delle lettere BACB, le lettere DGFD nello stesso ordine delle lettere ABCA e le lettere EMFE nello stesso ordine delle lettere ACBA; poi si completino questi segmenti in cerchi interi.",
     "en": "But those segments are to be described towards such sides of the lines DE, DF, EF, that the letters DRED may turn round about in the same order with the letters BACB; the letters DGFD in the same order with the letters ABCA; and the letters EMFE in the same order with the letters ACBA; then, completing those segments into entire circles",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tre cerchi interi"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem26-p4",
     "la": "",
     "it": "I primi due cerchi si taglino a vicenda in G, e siano P e Q i loro centri.",
     "en": "let the two former circles cut one the other in G, and suppose P and Q to be their centres.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "G",
       "P, Q"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem26-p5",
     "la": "",
     "it": "Congiunte GP, PQ, prendi Ga che stia ad AB come GP sta a PQ, e con centro G e raggio Ga descrivi un cerchio che tagli il primo cerchio DGE in a.",
     "en": "Then joining GP, PQ, take Ga to AB as GP is to PQ; and about the centre G, with the interval Ga, describe a circle that may cut the first circle DGE in a.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "GP, PQ",
       "cerchio di centro G e raggio Ga",
       "a"
      ],
      "evidenzia": [
       "Ga : AB = GP : PQ"
      ]
     }
    },
    {
     "id": "L1-Lem26-p6",
     "la": "",
     "it": "Si congiungano aD, che tagli il secondo cerchio DFG in b, e aE, che tagli il terzo cerchio EMF in c.",
     "en": "Join aD cutting the second circle DFG in b, as well as aE cutting the third circle EMF in c.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "aD, b",
       "aE, c"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem26-p7",
     "la": "",
     "it": "Ora si può costruire la figura ABCdef simile e uguale alla figura abcDEF.",
     "en": "Complete the figure ABCdef similar and equal to the figure abcDEF:",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangolo abc"
      ],
      "evidenzia": []
     },
     "nota": "Motte riassume le ultime due frasi latine in una sola."
    },
    {
     "id": "L1-Lem26-p8",
     "la": "",
     "it": "Fatto ciò, il problema è risolto.",
     "en": "I say, the thing is done.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem26-p9",
     "la": "",
     "it": "Si conduca infatti Fc, che incontri aD in n, e si congiungano aG, bG, QG, QD, PD.",
     "en": "For drawing Fc meeting aD in n, and joining aG, bG, QG, QD, PD,",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Fc, n",
       "aG, bG, QG, QD, PD"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem26-p10",
     "la": "",
     "it": "Per costruzione l’angolo EaD è uguale all’angolo CAB e l’angolo acF all’angolo ACB, e perciò il triangolo anc è equiangolo al triangolo ABC.",
     "en": "by construction the angle EaD is equal to the angle CAB, and the angle acF equal to the angle ACB; and therefore the triangle anc equiangular to the triangle ABC.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "triangoli anc, ABC"
      ]
     }
    },
    {
     "id": "L1-Lem26-p11",
     "la": "",
     "it": "Dunque l’angolo anc, ossia FnD, è uguale all’angolo ABC, e quindi all’angolo FbD; e perciò il punto n cade sul punto b.",
     "en": "Wherefore the angle anc or FnD is equal to the angle ABC, and consequently to the angle FbD; and therefore the point n falls on the point b.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "n = b"
      ]
     }
    },
    {
     "id": "L1-Lem26-p12",
     "la": "",
     "it": "Inoltre l’angolo GPQ, che è la metà dell’angolo al centro GPD, è uguale all’angolo alla circonferenza GaD; e l’angolo GQP, che è la metà dell’angolo al centro GQD, è uguale al complemento a due retti dell’angolo alla circonferenza GbD, e quindi è uguale all’angolo Gba; perciò i triangoli GPQ, Gab sono simili, e Ga sta ad ab come GP sta a PQ, cioè (per costruzione) come Ga sta ad AB.",
     "en": "Moreover the angle GPQ, which is half the angle GPD at the centre, is equal to the angle GaD at the circumference; and the angle GQP, which is half the angle GQD at the centre, is equal to the complement to two right angles of the angle GbD at the circumference, and therefore equal to the angle Gba. Upon which account the triangles GPQ, Gab, are similar, and Ga is to ab as GP to PQ; that is (by construction), as Ga to AB.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "triangoli GPQ, Gab"
      ]
     }
    },
    {
     "id": "L1-Lem26-p13",
     "la": "",
     "it": "Sono dunque uguali ab e AB; e perciò i triangoli abc, ABC, che abbiamo appena provato essere simili, sono anche uguali.",
     "en": "Wherefore ab and AB are equal; and consequently the triangles abc, ABC, which we have now proved to be similar, are also equal.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "ab = AB"
      ]
     }
    },
    {
     "id": "L1-Lem26-p14",
     "la": "",
     "it": "Perciò, poiché inoltre gli angoli D, E, F del triangolo DEF toccano rispettivamente i lati ab, ac, bc del triangolo abc, si può completare la figura ABCdef simile e uguale alla figura abcDEF, e completandola si risolverà il problema. C.V.F.",
     "en": "And therefore since the angles D, E, F, of the triangle DEF do respectively touch the sides ab, ac, bc of the triangle abc, the figure ABCdef may be completed similar and equal to the figure abcDEF, and by completing it the Problem will be solved. Q.E.F.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "figura ABCdef"
      ],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L1-P28",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXVIII, Probl. XX — traiettoria data, tagliata da tre rette",
   "copertura": [
    "S5.73",
    "S5.74",
    "S5.75"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 150"
   },
   "enunciato": {
    "la": "",
    "it": "Descrivere una traiettoria data di forma e di grandezza, le cui parti date saranno comprese fra tre rette date di posizione.",
    "en": "To describe a trajectory given both in kind and magnitude, given parts of which shall be interposed between three right lines given by position."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "D",
     "E",
     "F"
    ],
    "vincoli": [
     "curva DEF data di forma e grandezza",
     "D su AB, E su AC, F su BC"
    ]
   },
   "passi": [
    {
     "id": "L1-P28-p1",
     "la": "",
     "it": "Si debba descrivere una traiettoria che sia simile e uguale alla linea curva DEF e che sia tagliata dalle tre rette AB, AC, BC, date di posizione, in parti simili e uguali alle parti date DE ed EF di questa.",
     "en": "Suppose a trajectory is to be described that may be similar and equal to the curve line DEF, and may be cut by three right lines AB, AC, BC, given by position, into parts DE and EF, similar and equal to the given parts of this curve line.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "curva data DEF",
       "rette AB, AC, BC"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P28-p2",
     "la": "",
     "it": "Conduci le rette DE, EF, DF e poni gli angoli D, E, F di questo triangolo DEF su quelle rette date di posizione (per il Lemma XXVI); poi intorno al triangolo descrivi una traiettoria simile e uguale alla curva DEF. C.V.F.",
     "en": "Draw the right lines DE, EF, DF: and place the angles D, E, F, of this triangle DEF, so as to touch those right lines given by position (by Lem. XXVI). Then about the triangle describe the trajectory, similar and equal to the curve DEF. Q.E.F.",
     "dipende_da": [
      "Lemma XXVI"
     ],
     "figura": {
      "mostra": [
       "triangolo DEF collocato sulle tre rette",
       "traiettoria circoscritta"
      ],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L1-Lem27",
   "tipo": "Lemma (problema)",
   "titolo": "Lemma XXVII — vertici di un trapezio dato di forma su quattro rette",
   "copertura": [
    "S5.76",
    "S5.77",
    "S5.78"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 150–151"
   },
   "enunciato": {
    "la": "",
    "it": "Descrivere un trapezio dato di forma i cui angoli stiano, ciascuno su ciascuna, su quattro rette date di posizione, che non siano tutte parallele né convergano in un punto comune.",
    "en": "To describe a trapezium given in kind, the angles whereof may be so placed, in respect of four right lines given by position, that are neither all parallel among themselves, nor converge to one common point, that the several angles may touch the several lines."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "D",
     "E",
     "F",
     "G",
     "H",
     "I",
     "f",
     "g",
     "h",
     "i",
     "S",
     "T",
     "V",
     "P",
     "Q",
     "R",
     "N",
     "K",
     "L",
     "a",
     "b",
     "c"
    ],
    "vincoli": [
     "rette ABC, AD, BD, CE",
     "segmenti FSG, FTH, FVI capaci di BAD, CBD, ACE",
     "QR : PQ = BC : AB",
     "cerchio di centro R per F"
    ]
   },
   "passi": [
    {
     "id": "L1-Lem27-p1",
     "la": "",
     "it": "Siano date di posizione quattro rette ABC, AD, BD, CE, delle quali la prima tagli la seconda in A, la terza in B e la quarta in C; e si debba descrivere un trapezio fghi simile al trapezio FGHI, il cui angolo f, uguale all’angolo dato F, tocchi la retta ABC, e gli altri angoli g, h, i, uguali agli altri angoli dati G, H, I, tocchino rispettivamente le altre linee AD, BD, CE.",
     "en": "Let the four right lines ABC, AD, BD, CE, be given by position; the first cutting the second in A, the third in B, and the fourth in C; and suppose a trapezium fghi is to be described that may be similar to the trapezium FGHI, and whose angle f, equal to the given angle F, may touch the right line ABC; and the other angles g, h, i, equal to the other given angles, G, H, I, may touch the other lines AD, BD, CE, respectively.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "rette ABC, AD, BD, CE",
       "A, B, C",
       "trapezio dato FGHI"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem27-p2",
     "la": "",
     "it": "Si congiunga FH, e su FG, FH, FI si descrivano altrettanti segmenti di cerchio FSG, FTH, FVI, dei quali il primo, FSG, sia capace di un angolo uguale all’angolo BAD, il secondo, FTH, di un angolo uguale all’angolo CBD, e il terzo, FVI, di un angolo uguale all’angolo ACE.",
     "en": "Join FH, and upon FG, FH, FI describe as many segments of circles FSG, FTH, FVI, the first of which FSG may be capable of an angle equal to the angle BAD; the second FTH capable of an angle equal to the angle CBD; and the third FVI of an angle equal to the angle ACE.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "FH",
       "segmenti FSG, FTH, FVI"
      ],
      "evidenzia": [
       "capaci di BAD, CBD, ACE"
      ]
     }
    },
    {
     "id": "L1-Lem27-p3",
     "la": "",
     "it": "I segmenti devono poi essere descritti da quella parte delle linee FG, FH, FI per cui l’ordine circolare delle lettere FSGF sia lo stesso delle lettere BADB, e le lettere FTHF girino in cerchio nello stesso ordine delle lettere CBDC, e le lettere FVIF nello stesso ordine delle lettere ACEA.",
     "en": "But the segments are to be described towards those sides of the lines FG, FH, FI, that the circular order of the letters FSGF may be the same as of the letters BADB, and that the letters FTHF may turn about in the same order as the letters CBDC and the letters FVIF in the same order as the letters ACEA.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem27-p4",
     "la": "",
     "it": "Si completino i segmenti in cerchi interi, e sia P il centro del primo cerchio FSG e Q il centro del secondo FTH.",
     "en": "Complete the segments into entire circles, and let P be the centre of the first circle FSG, Q the centre of the second FTH.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchi interi",
       "P, Q"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem27-p5",
     "la": "",
     "it": "Si congiunga PQ e la si prolunghi da entrambe le parti, e su di essa si prenda QR che abbia con PQ il rapporto che BC ha con AB.",
     "en": "Join and produce both ways the line PQ, and in it take QR in the same ratio to PQ as BC has to AB.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "retta PQ",
       "R"
      ],
      "evidenzia": [
       "QR : PQ = BC : AB"
      ]
     }
    },
    {
     "id": "L1-Lem27-p6",
     "la": "",
     "it": "QR si prenda poi da quella parte del punto Q per cui l’ordine delle lettere P, Q, R sia lo stesso delle lettere A, B, C; e con centro R e raggio RF si descriva un quarto cerchio FNc, che tagli il terzo cerchio FVI in c.",
     "en": "But QR is to be taken towards that side of the point Q, that the order of the letters P, Q, R may be the same as of the letters A, B, C; and about the centre R with the interval RF describe a fourth circle FNc cutting the third circle FVI in c.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio FNc",
       "c"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem27-p7",
     "la": "",
     "it": "Si congiunga Fc, che tagli il primo cerchio in a e il secondo in b.",
     "en": "Join Fc cutting the first circle in a, and the second in b.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Fc",
       "a, b"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem27-p8",
     "la": "",
     "it": "Si conducano aG, bH, cI: si può costruire la figura ABCfghi simile alla figura abcFGHI.",
     "en": "Draw aG, bH, cI, and let the figure ABCfghi be made similar to the figure abcFGHI;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "aG, bH, cI"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem27-p9",
     "la": "",
     "it": "Fatto ciò, il trapezio fghi sarà proprio quello che si doveva costruire.",
     "en": "and the trapezium fghi will be that which was required to be described.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "trapezio fghi"
      ],
      "evidenzia": []
     },
     "nota": "La trascrizione ha «rapezium» per «trapezium»: refuso probabile della trascrizione."
    },
    {
     "id": "L1-Lem27-p10",
     "la": "",
     "it": "I primi due cerchi FSG, FTH si taglino infatti a vicenda in K.",
     "en": "For let the two first circles FSG, FTH cut one the other in K;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "K"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem27-p11",
     "la": "",
     "it": "Si congiungano PK, QK, RK, aK, bK, cK, e si prolunghi QP fino a L.",
     "en": "join PK, QK, RK, aK, bK, cK, and produce QP to L.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "PK, QK, RK",
       "aK, bK, cK",
       "L"
      ],
      "evidenzia": []
     },
     "nota": "La trascrizione ha «adL» senza spazio."
    },
    {
     "id": "L1-Lem27-p12",
     "la": "",
     "it": "Gli angoli alle circonferenze FaK, FbK, FcK sono la metà degli angoli al centro FPK, FQK, FRK, e quindi sono uguali alle metà di quegli angoli, LPK, LQK, LRK.",
     "en": "The angles FaK, FbK, FcK at the circumferences are the halves of the angles FPK, FQK, FRK, at the centres, and therefore equal to LPK, LQK, LRK, the halves of those angles.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "FaK = LPK, FbK = LQK, FcK = LRK"
      ]
     }
    },
    {
     "id": "L1-Lem27-p13",
     "la": "",
     "it": "La figura PQRK è dunque equiangola e simile alla figura abcK, e perciò ab sta a bc come PQ sta a QR, cioè come AB sta a BC.",
     "en": "Wherefore the figure PQRK is equiangular and similar to the figure abcK, and consequently ab is to bc as PQ to QR, that is, as AB to BC.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "figure PQRK, abcK simili",
       "ab : bc = AB : BC"
      ]
     }
    },
    {
     "id": "L1-Lem27-p14",
     "la": "",
     "it": "Inoltre, per costruzione, agli angoli FaG, FbH, FcI sono uguali gli angoli fAg, fBh, fCi.",
     "en": "But by construction, the angles fAg, fBh, fCi, are equal to the angles FaG, FbH, FcI.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem27-p15",
     "la": "",
     "it": "Dunque si può completare la figura ABCfghi simile alla figura abcFGHI.",
     "en": "And therefore the figure ABCfghi may be completed similar to the figure abcFGHI.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem27-p16",
     "la": "",
     "it": "Fatto ciò, il trapezio fghi risulterà simile al trapezio FGHI e con i suoi angoli f, g, h, i toccherà le rette ABC, AD, BD, CE. C.V.F.",
     "en": "Which done a trapezium fghi will be constructed similar to the trapezium FGHI, and which by its angles f, g, h, i will touch the right lines ABC, AD, BD, CE. Q.E.F.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "trapezio fghi sulle quattro rette"
      ],
      "evidenzia": []
     }
    }
   ]
  },
  {
   "id": "L1-Lem27-Cor",
   "tipo": "Corollarium",
   "titolo": "Lemma XXVII, Cor. — retta divisa in parti proporzionali da quattro rette",
   "copertura": [
    "S5.79",
    "S5.80",
    "S5.81"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 151–152"
   },
   "enunciato": {
    "la": "",
    "it": "Cor. Di qui si può condurre una retta le cui parti, comprese in un ordine dato fra quattro rette date di posizione, avranno fra loro una proporzione data.",
    "en": "COR. Hence a right line may be drawn whose parts intercepted in a given order, between four right lines given by position, shall have a given proportion among themselves."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "D",
     "E",
     "K",
     "L",
     "i",
     "M",
     "g",
     "f",
     "h",
     "Q",
     "S",
     "P",
     "R"
    ],
    "vincoli": [
     "rette AB, AD, BD, CE",
     "BK : AB = HI : GH; DL : BD = GI : FG",
     "LM : iL = GH : HI; MQ ∥ LB",
     "FG, GH, HI segmenti dati in linea retta"
    ]
   },
   "passi": [
    {
     "id": "L1-Lem27-Cor-p1",
     "la": "",
     "it": "Si prolunghino AB fino a K e BD fino a L, in modo che BK stia ad AB come HI sta a GH, e DL stia a BD come GI sta a FG; e si congiunga KL, che incontri la retta CE in i.",
     "en": "Produce AB to K and BD to L, so as BK may be to AB as HI to GH; and DL to BD as GI to FG; and join KL meeting the right line CE in i.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "rette AB, AD, BD, CE",
       "K",
       "L",
       "KL",
       "i"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem27-Cor-p2",
     "la": "",
     "it": "Si prolunghi iL fino a M, in modo che LM stia a iL come GH sta a HI, e si conducano MQ, parallela a LB, che incontri la retta AD in g, e gi, che tagli AB, BD in f, h.",
     "en": "Produce iL to M, so as LM may be to iL as GH to HI; then draw MQ parallel to LB, and meeting the right line AD in g, and join gi cutting AB, BD in f, h;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "M",
       "MQ ∥ LB",
       "g",
       "retta gi",
       "f, h"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem27-Cor-p3",
     "la": "",
     "it": "Dico che è fatto.",
     "en": "I say, the thing is done.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem27-Cor-p4",
     "la": "",
     "it": "Mg tagli infatti la retta AB in Q, e AD tagli la retta KL in S; si conduca AP parallela a BD, che incontri iL in P: gM starà a Lh (gi a hi, Mi a Li, GI a HI, AK a BK) e AP a BL nello stesso rapporto.",
     "en": "For let Mg cut the right line AB in Q, and AD the right line KL in S, and draw AP parallel to BD, and meeting iL in P, and gM to Lh (gi to hi, Mi to Li, GI to HI, AK to BK) and AP to BL, will be in the same ratio.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Q",
       "S",
       "AP ∥ BD",
       "P"
      ],
      "evidenzia": []
     },
     "nota": "La trascrizione ha «occurat» per «occurrat»: refuso probabile della trascrizione."
    },
    {
     "id": "L1-Lem27-Cor-p5",
     "la": "",
     "it": "Si divida DL in R in modo che DL stia a RL in quello stesso rapporto; e, poiché gS sta a gM, AS ad AP e DS a DL in proporzione, per uguaglianza come gS sta a Lh così AS sta a BL e DS a RL; e, in modo misto, BL − RL sta a Lh − BL come AS − DS sta a gS − AS.",
     "en": "Cut DL in R, so as DL to RL may be in that same ratio; and because gS to gM, AS to AP, and DS to DL are proportional; therefore (ex æquo) as gS to Lh, so will AS be to BL, and DS to RL; and mixtly, BL - RL to Lh - BL, as AS - DS to gS - AS.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "R"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem27-Cor-p6",
     "la": "",
     "it": "Cioè BR sta a Bh come AD sta ad Ag, e quindi come BD sta a gQ.",
     "en": "That is, BR is to Bh as AD is to Ag, and therefore as BD to gQ.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem27-Cor-p7",
     "la": "",
     "it": "E, permutando, BR sta a BD come Bh sta a gQ, ossia come fh sta a fg.",
     "en": "And alternately BR is to BD as Bh to gQ, or as fh to fg.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem27-Cor-p8",
     "la": "",
     "it": "Ma per costruzione la linea BL è stata divisa in D e R nello stesso rapporto in cui la linea FI è divisa in G e H; e perciò BR sta a BD come FH sta a FG.",
     "en": "But by construction the line BL was cut in D and R in the same ratio as the line FI in G and H; and therefore BR is to BD as FH to FG.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem27-Cor-p9",
     "la": "",
     "it": "Dunque fh sta a fg come FH sta a FG.",
     "en": "Wherefore fh is to fg as FH to FG.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "fh : fg = FH : FG"
      ]
     }
    },
    {
     "id": "L1-Lem27-Cor-p10",
     "la": "",
     "it": "Poiché dunque anche gi sta a hi come Mi sta a Li, cioè come GI sta a HI, è evidente che le linee FI, fi sono divise in modo simile in g e h, G e H. C.V.F.",
     "en": "Since, therefore, gi to hi likewise is as Mi to Li, that is, as GI to HI, it is manifest that the lines FI, fi, are similarly cut in G and H, g and h. Q.E.F.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "fi divisa come FI"
      ]
     },
     "nota": "La trascrizione ha «linas» per «lineas»: refuso probabile della trascrizione."
    }
   ]
  },
  {
   "id": "L1-P29",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXIX, Probl. XXI — traiettoria data di forma, tagliata da quattro rette in parti date",
   "copertura": [
    "S5.84",
    "S5.85"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 152"
   },
   "enunciato": {
    "la": "",
    "it": "Descrivere una traiettoria data di forma che sia tagliata da quattro rette date di posizione in parti date per ordine, per forma e per proporzione.",
    "en": "To describe a trajectory given in kind, that may be cut by four right lines given by position, into parts given in order, kind, and proportion."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "D",
     "C",
     "E",
     "F",
     "G",
     "H",
     "I",
     "f",
     "g",
     "h",
     "i"
    ],
    "vincoli": [
     "rette AB, AD, BD, CE",
     "curva FGHI data di forma",
     "trapezio fghi simile a FGHI"
    ]
   },
   "passi": [
    {
     "id": "L1-P29-p1",
     "la": "",
     "it": "Si debba descrivere una traiettoria che sia simile alla linea curva FGHI e le cui parti, simili e proporzionali alle parti FG, GH, HI di quella, siano comprese fra le rette AB e AD, AD e BD, BD e CE, date di posizione: la prima fra le prime, la seconda fra le seconde, la terza fra le terze.",
     "en": "Suppose a trajectory is to be described that may be similar to the curve line FGHI, and whose parts, similar and proportional to the parts FG, GH, HI of the other, may be intercepted between the right lines AB and AD, AD, and BD, BD and CE given by position, viz., the first between the first pair of those lines, the second between the second, and the third between the third.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "curva FGHI",
       "rette AB, AD, BD, CE"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P29-p2",
     "la": "",
     "it": "Condotte le rette FG, GH, HI, FI, si descriva (per il Lemma XXVII) un trapezio fghi simile al trapezio FGHI, i cui angoli f, g, h, i tocchino quelle rette date di posizione AB, AD, BD, CE, ciascuno ciascuna nell’ordine detto.",
     "en": "Draw the right lines FG, GH, HI, FI; and (by Lem. XXVII) describe a trapezium fghi that may be similar to the trapezium FGHI, and whose angles f, g, h, i, may touch the right lines given by position AB, AD, BD, CE, severally according to their order.",
     "dipende_da": [
      "Lemma XXVII"
     ],
     "figura": {
      "mostra": [
       "trapezio FGHI",
       "trapezio fghi sulle quattro rette"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P29-p3",
     "la": "",
     "it": "Poi intorno a questo trapezio si descriva una traiettoria simile alla linea curva FGHI.",
     "en": "And then about this trapezium describe a trajectory, that trajectory will be similar to the curve line FGHI.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "traiettoria circoscritta"
      ],
      "evidenzia": []
     },
     "nota": "La trascrizione ha «linæ» per «lineæ»: refuso probabile della trascrizione. Il latino non chiude con Q.E.F."
    }
   ]
  }
 ]
}
```
