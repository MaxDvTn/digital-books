> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 5 — Libro I, Sezione II: la ricerca delle forze centripete

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo prosegue il Fascicolo 4 (Libro I, Sezione I, Lemmi I–XI). Traduce integralmente la **Sezione II** del Libro I, *De inventione virium centripetarum*: le Proposizioni I–X, il Lemma XII, tutti i corollari e i cinque scolii (alle Propp. II, III, IV, VIII e X). È una traduzione di lavoro, non un’edizione critica validata.

Gli identificatori **S2.01–S2.67** e i titoli tematici tra parentesi sono aggiunte editoriali. Servono a orientare la lettura e a controllare la completezza. I numeri romani delle proposizioni, dei teoremi, dei problemi e dei lemmi, e i numeri dei corollari, appartengono al testo originale. Le integrazioni del curatore sono tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton.

In coda al fascicolo c’è la **Parte B**, con i dati strutturati per le pagine interattive di 14 unità con dimostrazione geometrica: Prop. I e i suoi Cor. 1 e 3; Prop. II; Prop. V; Cor. 1–3 della Prop. VI; Prop. VII e i suoi Cor. 2 e 3; Propp. VIII, IX e X.

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro I, Sezione II, **pp. 38–54** (inizio della Prop. I a p. 38; i marcatori di pagina della trascrizione vanno da ‹39› a ‹54›). Trascrizione normalizzata del Newton Project, documento **NATP00087**, estratta in testo semplice senza correzioni: `fonti/latino-1726-L1-S02.md`.
2. **Inglese di confronto.** *Newton’s Principia*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, Section II, **pp. 103–116** secondo i marcatori di pagina dell’EPUB (Project Gutenberg n. 76404). Estratto: `fonti/motte-1846-L1-S02.md`. I numeri di pagina sono stati ricavati dagli ancoraggi `Page_n` del file XHTML dell’EPUB; le formule stampate come immagini (`[SVG 28]`–`[SVG 83]`) sono state rese con `rsvg-convert` e lette una per una.
3. **Brief comune** del Libro I e **Fascicolo 3** (modello di formato, glossario, decisioni del curatore F2 e F3).

Non ho consultato né riprodotto traduzioni moderne. Non ho potuto vedere la stampa del 1726 né le figure originali (NATP00087-9…19): le relazioni geometriche sono ricostruite dalle sole lettere del testo.

### Criteri di traduzione

- Il testo guida è il latino; l’inglese di Motte serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o si discosta.
- Si applica il **glossario comune** del brief (Fascicoli 1–3 e termini tecnici del Libro I): *vis insita* «forza insita», *vis centripeta* «forza centripeta», *vis acceleratrix* «forza acceleratrice», *sagitta* «saetta», *sinus versus* «seno verso», *ratio duplicata / subduplicata / sesquiplicata* «rapporto duplicato / subduplicato / sesquiplicato», *reciproce* «inversamente», *conjunctim* «considerate congiuntamente», *in directum* «in linea retta», *in consequentia / in antecedentia* «in conseguenza / in antecedenza», *tempus periodicum* «tempo periodico», *ordinatim applicata* «ordinata», *specie datus* «dato di forma», *diametri conjugatæ* «diametri coniugati», *ultimo* «alla fine», *ratio ultima* «rapporto ultimo», Q.E.D. «C.V.D.», Q.E.I. «C.V.T.».
- **Decisioni del curatore** applicate: nella Prop. I *impulsu unico sed magno* → «con un impulso unico ma grande»; *vi insita* → «per la forza insita».
- Le estensioni del glossario proprie di questo fascicolo sono elencate e motivate nel § A.0.
- Gli enunciati latini all’infinito sono resi con l’indicativo; gli enunciati dei problemi (*Gyretur corpus… requiritur…*) conservano il congiuntivo esortativo e il presente.
- Le abbreviazioni «SP quad.», «SPq», «PV cub.» sono scritte SP², PV³; i rapporti appiattiti dalla trascrizione («SP quad.×QT quad.QR») sono resi con la barra (SP²×QT²/QR), dichiarando la lettura nell’apparato. Nessuna formula moderna entra nel testo tradotto.

---

## Traduzione italiana

### Sezione II. La ricerca delle forze centripete

### Proposizione I. Teorema I (legge delle aree)

**[S2.01]** **Le aree che i corpi mossi in giro descrivono con raggi condotti a un centro immobile delle forze giacciono in piani immobili e sono proporzionali ai tempi.**

**[S2.02]** Si divida il tempo in parti uguali, e nella prima parte del tempo il corpo descriva per la forza insita la retta AB. Nella seconda parte del tempo, se nulla lo impedisse, lo stesso corpo procederebbe in linea retta fino a c (per la Legge I), descrivendo la linea Bc uguale ad AB; così che, condotti al centro i raggi AS, BS, cS, risulterebbero descritte aree uguali ASB, BSc. Ma quando il corpo giunge in B, agisca la forza centripeta con un impulso unico ma grande, e faccia sì che il corpo devii dalla retta Bc e prosegua lungo la retta BC. Si conduca cC parallela a BS, che incontri BC in C; e, compiuta la seconda parte del tempo, il corpo (per il Cor. I delle leggi) si troverà in C, nello stesso piano del triangolo ASB. Si congiunga SC: il triangolo SBC, per le parallele SB, Cc, sarà uguale al triangolo SBc, e quindi anche al triangolo SAB. Con un argomento simile, se la forza centripeta agisce successivamente in C, D, E, ecc., facendo sì che il corpo, nelle singole particelle di tempo, descriva le singole rette CD, DE, EF, ecc., queste giaceranno tutte nello stesso piano; e il triangolo SCD sarà uguale al triangolo SBC, SDE a SCD, e SEF a SDE. In tempi uguali, dunque, si descrivono aree uguali in un piano immobile; e, componendo, somme qualsiasi di aree SADS, SAFS stanno fra loro come i tempi in cui sono descritte. Si aumenti ora il numero dei triangoli e se ne diminuisca la larghezza all’infinito: il loro perimetro ultimo ADF (per il Cor. 4 del Lemma III) sarà una linea curva; e perciò la forza centripeta, dalla quale il corpo è continuamente ritratto dalla tangente di questa curva, agirà incessantemente; e le aree descritte qualsiasi SADS, SAFS, che erano sempre proporzionali ai tempi della descrizione, saranno anche in questo caso proporzionali a quei tempi. C.V.D.

**[S2.03]** *Cor. 1.* La velocità di un corpo attratto verso un centro immobile, in spazi non resistenti, è inversamente proporzionale alla perpendicolare condotta da quel centro sulla tangente rettilinea dell’orbita. Infatti la velocità in quei luoghi A, B, C, D, E sta come le basi dei triangoli uguali AB, BC, CD, DE, EF; e queste basi sono inversamente proporzionali alle perpendicolari condotte su di esse.

**[S2.04]** *Cor. 2.* Se le corde AB, BC di due archi descritti successivamente in tempi uguali dallo stesso corpo, in spazi non resistenti, si completano nel parallelogramma ABCU, e la diagonale BU di questo, nella posizione che assume alla fine, quando quegli archi diminuiscono all’infinito, si prolunga da entrambe le parti, essa passerà per il centro delle forze.

**[S2.05]** *Cor. 3.* Se le corde AB, BC e DE, EF di archi descritti in tempi uguali, in spazi non resistenti, si completano nei parallelogrammi ABCU, DEFZ, le forze in B e in E stanno fra loro nel rapporto ultimo delle diagonali BU, EZ, quando quegli archi diminuiscono all’infinito. Infatti i moti BC ed EF del corpo si compongono (per il Cor. I delle leggi) dei moti Bc, BU ed Ef, EZ; ma BU ed EZ, uguali a Cc e Ff, nella dimostrazione di questa proposizione erano generate dagli impulsi della forza centripeta in B e in E, e perciò sono proporzionali a questi impulsi.

**[S2.06]** *Cor. 4.* Le forze con cui corpi qualsiasi, in spazi non resistenti, sono ritratti dai moti rettilinei e piegati in orbite curve stanno fra loro come quelle saette degli archi descritti in tempi uguali che convergono verso il centro delle forze e dividono a metà le corde, quando quegli archi diminuiscono all’infinito. Infatti queste saette sono le metà delle diagonali di cui abbiamo trattato nel Cor. 3.

**[S2.07]** *Cor. 5.* E perciò le stesse forze stanno alla forza di gravità come queste saette stanno alle saette, perpendicolari all’orizzonte, degli archi parabolici che i proiettili descrivono nello stesso tempo.

**[S2.08]** *Cor. 6.* Tutte le stesse cose valgono, per il Cor. V delle leggi, quando i piani nei quali i corpi si muovono, insieme con i centri delle forze che sono situati in essi, non sono in quiete, ma si muovono uniformemente in linea retta.

### Proposizione II. Teorema II (dalla legge delle aree alla forza centrale)

**[S2.09]** **Ogni corpo che si muove lungo una linea curva descritta in un piano e che, con un raggio condotto a un punto o immobile o avanzante uniformemente di moto rettilineo, descrive attorno a quel punto aree proporzionali ai tempi, è sollecitato da una forza centripeta diretta verso quello stesso punto.**

**[S2.10]** *Caso 1.* Infatti ogni corpo che si muove lungo una linea curva è piegato dal corso rettilineo da qualche forza che agisce su di esso (per la Legge I). E quella forza dalla quale il corpo è piegato dal corso rettilineo, ed è costretto a descrivere in tempi uguali triangoli uguali piccolissimi SAB, SBC, SCD, ecc. attorno al punto immobile S, agisce nel luogo B lungo una linea parallela a cC (per la Prop. XL del Libro I degli *Elementi* e per la Legge II), cioè lungo la linea BS; e nel luogo C lungo una linea parallela a dD, cioè lungo la linea SC, ecc. Agisce dunque sempre lungo linee dirette a quel punto immobile S. C.V.D.

**[S2.11]** *Caso 2.* E, per il Cor. V delle leggi, è indifferente che la superficie nella quale il corpo descrive la figura curvilinea sia in quiete, oppure si muova uniformemente in linea retta insieme con il corpo, con la figura descritta e con il suo punto S.

**[S2.12]** *Cor. 1.* In spazi o mezzi non resistenti, se le aree non sono proporzionali ai tempi, le forze non tendono al punto d’incontro dei raggi, ma deviano da esso in conseguenza, cioè verso la parte verso cui avviene il moto, se la descrizione delle aree è accelerata; se invece è ritardata, deviano in antecedenza.

**[S2.13]** *Cor. 2.* Anche nei mezzi resistenti, se la descrizione delle aree è accelerata, le direzioni delle forze deviano dal punto d’incontro dei raggi verso la parte verso cui avviene il moto.

**[S2.14]** *Scolio.* Un corpo può essere sollecitato da una forza centripeta composta di più forze. In questo caso il senso della proposizione è che la forza composta di tutte tende al punto S. Inoltre, se una forza agisce continuamente lungo una linea perpendicolare alla superficie descritta, essa farà deviare il corpo dal piano del suo moto; ma non accrescerà né diminuirà la quantità della superficie descritta, e perciò nella composizione delle forze va trascurata.

### Proposizione III. Teorema III (aree attorno a un corpo che si muove)

**[S2.15]** **Ogni corpo che, con un raggio condotto al centro di un altro corpo comunque mosso, descrive attorno a quel centro aree proporzionali ai tempi, è sollecitato da una forza composta della forza centripeta diretta verso quell’altro corpo e di tutta la forza acceleratrice da cui quell’altro corpo è sollecitato.**

**[S2.16]** Sia L il primo corpo e T l’altro corpo. Se (per il Cor. VI delle leggi) entrambi i corpi vengono sollecitati lungo linee parallele da una nuova forza, uguale e contraria a quella da cui è sollecitato l’altro corpo T, il primo corpo L continuerà a descrivere attorno all’altro corpo T le stesse aree di prima; la forza da cui era sollecitato l’altro corpo T sarà ora annullata da una forza uguale e contraria; e perciò (per la Legge I) quell’altro corpo T, ormai lasciato a sé stesso, o starà in quiete o si muoverà uniformemente in linea retta; e il primo corpo L, sollecitato dalla differenza delle forze, cioè dalla forza rimanente, continuerà a descrivere attorno all’altro corpo T aree proporzionali ai tempi. La differenza delle forze tende dunque (per il Teorema II) verso quell’altro corpo T come centro. C.V.D.

**[S2.17]** *Cor. 1.* Di qui, se un corpo L, con un raggio condotto all’altro T, descrive aree proporzionali ai tempi, e dalla forza totale da cui è sollecitato il primo corpo L (sia essa semplice, sia composta di più forze secondo il Cor. II delle leggi) si sottrae (per lo stesso corollario delle leggi) tutta la forza acceleratrice da cui è sollecitato l’altro corpo, tutta la forza rimanente da cui è sollecitato il primo corpo tenderà verso l’altro corpo T come centro.

**[S2.18]** *Cor. 2.* E, se quelle aree sono proporzionali ai tempi con ottima approssimazione, la forza rimanente tenderà verso l’altro corpo T con ottima approssimazione.

**[S2.19]** *Cor. 3.* E viceversa, se la forza rimanente tende con ottima approssimazione verso l’altro corpo T, quelle aree saranno proporzionali ai tempi con ottima approssimazione.

**[S2.20]** *Cor. 4.* Se il corpo L, con un raggio condotto all’altro corpo T, descrive aree che, confrontate con i tempi, sono molto disuguali, e quell’altro corpo T o è in quiete o si muove uniformemente in linea retta, l’azione della forza centripeta diretta verso quell’altro corpo T o è nulla, o è mescolata e composta con azioni assai potenti di altre forze; e la forza totale composta di tutte, se le forze sono più d’una, è diretta verso un altro centro (immobile o mobile). Lo stesso vale quando l’altro corpo si muove di un moto qualsiasi, purché si prenda la forza centripeta che rimane dopo aver sottratto tutta la forza che agisce su quell’altro corpo T.

**[S2.21]** *Scolio.* Poiché la descrizione uniforme delle aree è indice del centro a cui guarda quella forza da cui il corpo è affetto in sommo grado, e dalla quale è ritratto dal moto rettilineo e trattenuto nella sua orbita, perché non dovremmo usare, in ciò che segue, la descrizione uniforme delle aree come indice del centro attorno al quale si compie ogni moto circolare negli spazi liberi?

### Proposizione IV. Teorema IV (moto circolare uniforme)

**[S2.22]** **Le forze centripete dei corpi che descrivono cerchi diversi con moto uniforme tendono ai centri di quei cerchi, e stanno fra loro come i quadrati degli archi descritti nello stesso tempo, applicati ai raggi dei cerchi.**

**[S2.23]** Queste forze tendono ai centri dei cerchi per la Prop. II e per il Cor. 2 della Prop. I; e stanno fra loro come i seni versi degli archi piccolissimi descritti in tempi uguali, per il Cor. 4 della Prop. I, cioè come i quadrati di quegli stessi archi applicati ai diametri dei cerchi, per il Lemma VII; e perciò, poiché questi archi stanno come gli archi descritti in tempi uguali qualsiasi, e i diametri stanno come i loro raggi, le forze staranno come i quadrati di archi qualsiasi descritti nello stesso tempo, applicati ai raggi dei cerchi. C.V.D.

**[S2.24]** *Cor. 1.* Poiché quegli archi stanno come le velocità dei corpi, le forze centripete saranno nel rapporto composto dal rapporto duplicato delle velocità direttamente e dal rapporto semplice dei raggi inversamente.

**[S2.25]** *Cor. 2.* E, poiché i tempi periodici sono nel rapporto composto dal rapporto dei raggi direttamente e dal rapporto delle velocità inversamente, le forze centripete sono nel rapporto composto dal rapporto dei raggi direttamente e dal rapporto duplicato dei tempi periodici inversamente.

**[S2.26]** *Cor. 3.* Di qui, se i tempi periodici sono uguali, e perciò le velocità stanno come i raggi, anche le forze centripete staranno come i raggi; e viceversa.

**[S2.27]** *Cor. 4.* Se sia i tempi periodici sia le velocità sono nel rapporto subduplicato dei raggi, le forze centripete saranno uguali fra loro; e viceversa.

**[S2.28]** *Cor. 5.* Se i tempi periodici stanno come i raggi, e perciò le velocità sono uguali, le forze centripete saranno inversamente proporzionali ai raggi; e viceversa.

**[S2.29]** *Cor. 6.* Se i tempi periodici sono nel rapporto sesquiplicato dei raggi, e perciò le velocità sono inversamente nel rapporto subduplicato dei raggi, le forze centripete saranno inversamente proporzionali ai quadrati dei raggi; e viceversa.

**[S2.30]** *Cor. 7.* E in generale, se il tempo periodico è come una potenza qualsiasi Rⁿ del raggio R, e perciò la velocità è inversamente come la potenza Rⁿ⁻¹ del raggio, la forza centripeta sarà inversamente come la potenza R²ⁿ⁻¹ del raggio; e viceversa.

**[S2.31]** *Cor. 8.* Tutte le stesse conclusioni sui tempi, sulle velocità e sulle forze con cui i corpi descrivono parti simili di figure simili qualsiasi, che abbiano i centri situati in modo simile in quelle figure, seguono dalla dimostrazione dei casi precedenti applicata a questi casi. E la si applica sostituendo la descrizione uniforme delle aree al moto uniforme e usando le distanze dei corpi dai centri al posto dei raggi.

**[S2.32]** *Cor. 9.* Dalla stessa dimostrazione segue anche che l’arco che un corpo, ruotando uniformemente in un cerchio per una forza centripeta data, descrive in un tempo qualsiasi [è] medio proporzionale fra il diametro del cerchio e la discesa compiuta dallo stesso corpo cadendo per la stessa forza data e nello stesso tempo.

**[S2.33]** *Scolio.* Il caso del Cor. 6 si verifica nei corpi celesti (come hanno ricavato separatamente anche i nostri connazionali Wren, Hooke e Halley); e perciò ho deciso di esporre più diffusamente nel seguito ciò che riguarda la forza centripeta che decresce in rapporto duplicato delle distanze dai centri.

**[S2.34]** Inoltre, con l’aiuto della proposizione precedente e dei suoi corollari, si ricava anche la proporzione della forza centripeta rispetto a una forza nota qualsiasi, come quella di gravità. Infatti, se un corpo ruota per la propria gravità in un cerchio concentrico alla Terra, questa gravità è la sua forza centripeta. Ora, dalla discesa dei gravi sono dati, per il Cor. 9 di questa proposizione, sia il tempo di una rivoluzione sia l’arco descritto in un tempo dato qualsiasi. E con proposizioni di questo genere Huygens, nel suo eccellente trattato *De horologio oscillatorio*, ha confrontato la forza di gravità con le forze centrifughe dei corpi che ruotano.

**[S2.35]** Le cose precedenti si possono dimostrare anche in questo modo. Si immagini inscritto in un cerchio qualsiasi un poligono di un numero qualsiasi di lati. E se un corpo, muovendosi lungo i lati del poligono con una velocità data, viene riflesso dal cerchio in ciascuno dei suoi angoli, la forza con cui a ogni riflessione urta contro il cerchio sarà come la sua velocità; e perciò la somma delle forze in un tempo dato sarà come quella velocità e il numero delle riflessioni considerati congiuntamente: cioè (se il poligono è dato di forma) come la lunghezza descritta in quel tempo dato, accresciuta o diminuita nel rapporto della stessa lunghezza al raggio del cerchio suddetto; cioè come il quadrato di quella lunghezza applicato al raggio; e perciò, se il poligono, con i lati diminuiti all’infinito, coincide con il cerchio, come il quadrato dell’arco descritto in un tempo dato applicato al raggio. Questa è la forza centrifuga con cui il corpo preme il cerchio; e a essa è uguale la forza contraria con cui il cerchio respinge continuamente il corpo verso il centro.

### Proposizione V. Problema I (trovare il centro dalle velocità)

**[S2.36]** **Data in luoghi qualsiasi la velocità con cui un corpo descrive una figura data per effetto di forze dirette a un centro comune, trovare quel centro.**

**[S2.37]** Tre rette PT, TQV, VR tocchino la figura descritta in altrettanti punti P, Q, R, e si incontrino in T e V. Sulle tangenti si innalzino le perpendicolari PA, QB, RC inversamente proporzionali alle velocità del corpo nei punti P, Q, R dai quali sono innalzate; cioè in modo che PA stia a QB come la velocità in Q sta alla velocità in P, e QB stia a RC come la velocità in R sta alla velocità in Q. Per gli estremi A, B, C delle perpendicolari si conducano ad angoli retti AD, DBE, EC, che si incontrino in D ed E; e le rette TD, VE, una volta condotte, si incontreranno nel centro cercato S.

**[S2.38]** Infatti le perpendicolari condotte dal centro S sulle tangenti PT, QT sono inversamente proporzionali alle velocità del corpo nei punti P e Q (per il Cor. 1 della Prop. I); e perciò, per costruzione, direttamente proporzionali alle perpendicolari AP, BQ, cioè alle perpendicolari condotte dal punto D sulle tangenti. Di qui si ricava facilmente che i punti S, D, T sono su una stessa retta. E con un argomento simile anche i punti S, E, V sono su una stessa retta; e perciò il centro S si trova nell’incontro delle rette TD, VE. C.V.D.

### Proposizione VI. Teorema V (la forza misurata dalla saetta)

**[S2.39]** **Se un corpo, in uno spazio non resistente, ruota attorno a un centro immobile in un’orbita qualsiasi, e descrive in un tempo piccolissimo un arco qualsiasi appena nascente, e si immagina condotta la saetta dell’arco, che divida a metà la corda e, prolungata, passi per il centro delle forze, la forza centripeta nel mezzo dell’arco sarà come la saetta direttamente e come il tempo due volte inversamente.**

**[S2.40]** Infatti la saetta, in un tempo dato, è come la forza (per il Cor. 4 della Prop. I); e, aumentando il tempo in un rapporto qualsiasi, poiché l’arco aumenta nello stesso rapporto, la saetta aumenta nel rapporto duplicato di quello (per i Cor. 2 e 3 del Lemma XI); e perciò è come la forza una volta e il tempo due volte. Si tolga da entrambe le parti il rapporto duplicato del tempo, e la forza risulterà come la saetta direttamente e come il tempo due volte inversamente. C.V.D.

**[S2.41]** La stessa cosa si dimostra facilmente anche per il Cor. 4 del Lemma X.

**[S2.42]** *Cor. 1.* Se un corpo P, ruotando attorno al centro S, descrive la linea curva APQ, e la retta ZPR tocca quella curva in un punto qualsiasi P, e da un altro punto qualsiasi Q della curva si conduce alla tangente QR parallela alla distanza SP, e si abbassa QT perpendicolare a quella distanza SP, la forza centripeta sarà inversamente proporzionale al solido SP²×QT²/QR, purché di quel solido si prenda sempre la quantità che risulta alla fine, quando i punti P e Q si riuniscono. Infatti QR è uguale alla saetta dell’arco doppio di QP, nel cui mezzo sta P; e il doppio del triangolo SQP, ossia SP×QT, è proporzionale al tempo in cui è descritto quell’arco doppio, e perciò lo si può scrivere come esponente del tempo.

**[S2.43]** *Cor. 2.* Con lo stesso argomento la forza centripeta è inversamente proporzionale al solido SY²×QP²/QR, purché SY sia la perpendicolare condotta dal centro delle forze sulla tangente PR dell’orbita. Infatti i rettangoli SY×QP e SP×QT sono uguali.

**[S2.44]** *Cor. 3.* Se l’orbita è un cerchio, oppure tocca o taglia un cerchio concentricamente, cioè forma con il cerchio un angolo di contatto o di sezione il più piccolo possibile, avendo la stessa curvatura e lo stesso raggio di curvatura nel punto di contatto P; e se PV è la corda di questo cerchio condotta dal corpo attraverso il centro delle forze, la forza centripeta sarà inversamente proporzionale al solido SY²×PV. Infatti PV è QP²/QR.

**[S2.45]** *Cor. 4.* Poste le stesse cose, la forza centripeta è come la velocità due volte direttamente e come quella corda inversamente. Infatti la velocità è inversamente proporzionale alla perpendicolare SY, per il Cor. 1 della Prop. I.

**[S2.46]** *Cor. 5.* Di qui, se è data una figura curvilinea qualsiasi APQ, e in essa è dato anche il punto S verso cui la forza centripeta è diretta continuamente, si può trovare la legge della forza centripeta per la quale un corpo qualsiasi P, continuamente ritratto dal corso rettilineo, sarà trattenuto sul perimetro di quella figura e lo descriverà ruotando. Si deve cioè calcolare o il solido SP²×QT²/QR o il solido SY²×PV, inversamente proporzionale a questa forza. Di ciò daremo esempi nei problemi seguenti.

### Proposizione VII. Problema II (orbita circolare, centro delle forze qualsiasi)

**[S2.47]** **Un corpo giri sulla circonferenza di un cerchio: si chiede la legge della forza centripeta diretta verso un punto dato qualsiasi.**

**[S2.48]** Sia VQPA la circonferenza del cerchio; S il punto dato verso cui la forza tende come al suo centro; P il corpo portato sulla circonferenza; Q il luogo immediatamente successivo in cui si muoverà; e PRZ la tangente al cerchio nel luogo precedente. Per il punto S si conduca la corda PV; e, condotto il diametro VA del cerchio, si congiunga AP; si abbassi su SP la perpendicolare QT, che, prolungata, incontri la tangente PR in Z; e infine per il punto Q si conduca LR, parallela a SP, che incontri sia il cerchio in L sia la tangente PZ in R. Per la similitudine dei triangoli ZQR, ZTP, VPA, RP², cioè QR×RL, starà a QT² come AV² sta a PV². Perciò QR×RL×PV²/AV² è uguale a QT². Si moltiplichino questi uguali per SP²/QR e, riunendosi i punti P e Q, si scriva PV al posto di RL. Così SP²×PV³/AV² risulterà uguale a SP²×QT²/QR. Dunque (per i Cor. 1 e [5] della Prop. VI) la forza centripeta è inversamente proporzionale a SP²×PV³/AV²; cioè, poiché AV² è dato, inversamente proporzionale al quadrato della distanza, o altezza, SP e al cubo della corda PV considerati congiuntamente. C.V.T.

**[S2.49]** *La stessa cosa altrimenti.* Sulla tangente PR prolungata si abbassi la perpendicolare SY: per la similitudine dei triangoli SYP, VPA, AV starà a PV come SP sta a SY; e perciò SP×PV/AV è uguale a SY, e SP²×PV³/AV² è uguale a SY²×PV. E perciò (per i Cor. 3 e 5 della Prop. VI) la forza centripeta è inversamente proporzionale a SP²×PV³/AV², cioè, poiché AV è dato, inversamente proporzionale a SP²×PV³. C.V.T.

**[S2.50]** *Cor. 1.* Di qui, se il punto dato S, verso cui la forza centripeta tende sempre, è collocato sulla circonferenza di questo cerchio, per esempio in V, la forza centripeta sarà inversamente proporzionale al quadrato-cubo dell’altezza SP.

**[S2.51]** *Cor. 2.* La forza con cui il corpo P ruota nel cerchio APTV attorno al centro delle forze S sta alla forza con cui lo stesso corpo P può ruotare nello stesso cerchio e nello stesso tempo periodico attorno a un altro centro delle forze qualsiasi R, come RP²×SP sta al cubo della retta SG, che è condotta dal primo centro delle forze S fino alla tangente PG dell’orbita ed è parallela alla distanza del corpo dal secondo centro delle forze. Infatti, per la costruzione di questa proposizione, la prima forza sta alla seconda come RP²×PT³ sta a SP²×PV³, cioè come SP×RP² sta a SP³×PV³/PT³, ossia (per la similitudine dei triangoli PSG, TPV) a SG³.

**[S2.52]** *Cor. 3.* La forza con cui il corpo P ruota in un’orbita qualsiasi attorno al centro delle forze S sta alla forza con cui lo stesso corpo P può ruotare nella stessa orbita e nello stesso tempo periodico attorno a un altro centro delle forze qualsiasi R, come SP×RP², cioè la grandezza contenuta sotto la distanza del corpo dal primo centro delle forze S e il quadrato della sua distanza dal secondo centro delle forze R, sta al cubo della retta SG, condotta dal primo centro delle forze S fino alla tangente PG dell’orbita e parallela alla distanza RP del corpo dal secondo centro delle forze. Infatti le forze in quest’orbita, in un suo punto qualsiasi P, sono le stesse che in un cerchio della stessa curvatura.

### Proposizione VIII. Problema III (semicerchio, centro delle forze lontanissimo)

**[S2.53]** **Un corpo si muova nel semicerchio PQA: a questo scopo si chiede la legge della forza centripeta diretta verso un punto S così lontano che tutte le linee PS, RS condotte a esso si possano considerare parallele.**

**[S2.54]** Dal centro C del semicerchio si conduca il semidiametro CA, che tagli perpendicolarmente quelle parallele in M e N, e si congiunga CP. Per la similitudine dei triangoli CPM, PZT e RZQ, CP² sta a PM² come PR² sta a QT²; e, per la natura del cerchio, PR² è uguale al rettangolo QR×(RN+QN), ossia, riunendosi i punti P e Q, al rettangolo QR×2PM. Dunque CP² sta a PM² come QR×2PM sta a QT²; e perciò QT²/QR è uguale a 2PM³/CP², e QT²×SP²/QR è uguale a 2PM³×SP²/CP². Dunque (per i Cor. 1 e 5 della Prop. VI) la forza centripeta è inversamente proporzionale a 2PM³×SP²/CP², cioè (trascurato il rapporto determinato 2SP²/CP²) inversamente proporzionale a PM³. C.V.T.

**[S2.55]** La stessa cosa si ricava facilmente anche dalla proposizione precedente.

**[S2.56]** *Scolio.* E con un argomento non molto dissimile si troverà che un corpo si muove in un’ellisse, o anche in un’iperbole o in una parabola, per una forza centripeta che sia inversamente proporzionale al cubo dell’ordinata diretta a un centro delle forze lontanissimo.

### Proposizione IX. Problema IV (spirale che taglia i raggi sotto un angolo dato)

**[S2.57]** **Un corpo giri in una spirale PQS che tagli tutti i raggi SP, SQ, ecc. sotto un angolo dato: si chiede la legge della forza centripeta diretta verso il centro della spirale.**

**[S2.58]** Sia dato l’angolo indefinitamente piccolo PSQ; poiché tutti gli angoli sono dati, sarà data di forma la figura SPQRT. È dunque dato il rapporto QT/QR, e QT²/QR è come QT, cioè (poiché quella figura è data di forma) come SP. Si cambi ora in un modo qualsiasi l’angolo PSQ: la retta QR, che sottende l’angolo di contatto QPR, cambierà (per il Lemma XI) nel rapporto duplicato di PR o di QT. Dunque QT²/QR resterà lo stesso di prima, cioè come SP. Perciò QT²×SP²/QR è come SP³, e quindi (per i Cor. 1 e 5 della Prop. VI) la forza centripeta è inversamente proporzionale al cubo della distanza SP. C.V.T.

**[S2.59]** *La stessa cosa altrimenti.* La perpendicolare SY condotta sulla tangente e la corda PV del cerchio che taglia concentricamente la spirale stanno all’altezza SP in rapporti dati; e perciò SP³ è come SY²×PV, cioè (per i Cor. 3 e 5 della Prop. VI) inversamente come la forza centripeta.

### Lemma XII (parallelogrammi sui diametri coniugati)

**[S2.60]** **Tutti i parallelogrammi descritti attorno a diametri coniugati qualsiasi di un’ellisse o di un’iperbole data sono uguali fra loro.**

**[S2.61]** Risulta dalle coniche.

### Proposizione X. Problema V (ellisse, forza diretta al centro)

**[S2.62]** **Un corpo giri in un’ellisse: si chiede la legge della forza centripeta diretta verso il centro dell’ellisse.**

**[S2.63]** Siano CA, CB i semiassi dell’ellisse; GP, DK altri diametri coniugati; PF, QT perpendicolari ai diametri; Qv l’ordinata al diametro GP; e, se si completa il parallelogramma QvPR, il rettangolo PvG starà (per le coniche) a Qv² come PC² sta a CD²; e (per la similitudine dei triangoli QvT, PCF) Qv² sta a QT² come PC² sta a PF²; e, congiungendo i rapporti, il rettangolo PvG sta a QT² come PC² sta a CD² e PC² sta a PF², cioè vG sta a QT²/Pv come PC² sta a CD²×PF²/PC². Si scriva QR al posto di Pv, e (per il Lemma XII) BC×CA al posto di CD×PF, e inoltre (riunendosi i punti P e Q) 2PC al posto di vG; e, moltiplicati fra loro gli estremi e i medi, QT²×PC²/QR risulterà uguale a 2BC²×CA²/PC. Dunque (per il Cor. 5 della Prop. VI) la forza centripeta è inversamente proporzionale a 2BC²×CA²/PC; cioè (poiché 2BC²×CA² è dato) inversamente proporzionale a 1/PC; cioè direttamente proporzionale alla distanza PC. C.V.T.

**[S2.64]** *La stessa cosa altrimenti.* Sulla retta PG, dall’altra parte del punto T, si prenda u in modo che Tu sia uguale a Tv; poi si prenda uV che stia a vG come DC² sta a PC². E poiché, per le coniche, Qv² sta a PvG come DC² sta a PC², Qv² sarà uguale a Pv×uV. Si aggiunga da entrambe le parti il rettangolo uPv: ne risulterà il quadrato della corda dell’arco PQ uguale al rettangolo VPv; e perciò il cerchio che tocca la sezione conica in P e passa per il punto Q passerà anche per il punto V. Si riuniscano i punti P e Q: il rapporto di uV a vG, che è lo stesso del rapporto di DC² a PC², diventerà il rapporto di PV a PG, ossia di PV a 2PC; e perciò PV sarà uguale a 2DC²/PC. Pertanto la forza con cui il corpo P ruota nell’ellisse sarà inversamente proporzionale a 2DC²/PC moltiplicato per PF² (per il Cor. 3 della Prop. VI), cioè (poiché 2DC² moltiplicato per PF² è dato) direttamente proporzionale a PC. C.V.T.

**[S2.65]** *Cor. 1.* La forza è dunque come la distanza del corpo dal centro dell’ellisse; e, viceversa, se la forza è come la distanza, il corpo si muoverà in un’ellisse che ha il centro nel centro delle forze, o eventualmente in un cerchio, nel quale l’ellisse può comunque trasformarsi.

**[S2.66]** *Cor. 2.* E i tempi periodici delle rivoluzioni compiute in tutte le ellissi attorno allo stesso centro saranno uguali. Infatti quei tempi, nelle ellissi simili, sono uguali (per i Cor. 3 e 8 della Prop. IV); nelle ellissi che hanno in comune l’asse maggiore, invece, stanno fra loro come le aree totali delle ellissi direttamente e le particelle di area descritte nello stesso tempo inversamente; cioè come gli assi minori direttamente e le velocità dei corpi nei vertici principali inversamente; cioè come quegli assi minori direttamente e le ordinate allo stesso punto dell’asse comune inversamente; e perciò (per l’uguaglianza dei rapporti diretti e inversi) nel rapporto di uguaglianza.

**[S2.67]** *Scolio.* Se l’ellisse, allontanandosi il suo centro all’infinito, si trasforma in una parabola, il corpo si muoverà in questa parabola; e la forza, ormai diretta a un centro infinitamente distante, diventerà uniforme. Questo è il teorema di Galileo. E se la sezione conica parabolica (mutata l’inclinazione del piano rispetto al cono tagliato) si trasforma in un’iperbole, il corpo si muoverà sul perimetro di questa con la forza centripeta mutata in centrifuga. E come nel cerchio o nell’ellisse, se le forze tendono al centro della figura posto sull’ascissa, queste forze, aumentando o diminuendo le ordinate in un rapporto dato qualsiasi, o anche cambiando l’angolo d’inclinazione delle ordinate sull’ascissa, aumentano o diminuiscono sempre nel rapporto delle distanze dal centro, purché i tempi periodici restino uguali; così anche in tutte le figure, se le ordinate vengono aumentate o diminuite in un rapporto dato qualsiasi, o l’angolo delle ordinate viene cambiato in un modo qualsiasi, restando invariato il tempo periodico, le forze dirette a un centro qualsiasi posto sull’ascissa aumentano o diminuiscono, nelle singole ordinate, nel rapporto delle distanze dal centro.

**Fine della Sezione II. Nel testo originale segue la Sezione III, *De motu corporum in conicis sectionibus excentricis*.**

---

## Apparato

### A.0 Estensioni del glossario

I termini seguenti non comparivano nel glossario comune. Ognuno è reso in modo costante in tutto il fascicolo.

| Latino | Italiano | Motivazione |
|---|---|---|
| *inventio*, *invenire* | «ricerca», «trovare» | Titolo della Sezione e Prop. V (*centrum illud invenire*, «trovare quel centro»). «Invenzione» sarebbe un falso amico; Motte ha «Invention». |
| *corpora in gyros acta*; *gyrari*; *revolvi* | «corpi mossi in giro»; «girare»; «ruotare» | *Gyrus* è il giro, la rivoluzione; *revolvi* indica la rivoluzione attorno a un centro. «Ruotare» non implica qui la rotazione su sé stessi. |
| *centrum virium* | «centro delle forze» | Calco del plurale latino; Motte «centre of force». |
| *urgere* | «sollecitare» | Come nel Fascicolo 3 (Cor. VI): verbo delle forze acceleratrici. |
| *retrahere*; *detorquere*; *declinare*; *deflectere* | «ritrarre»; «piegare»; «deviare»; «far deviare» | Quattro verbi distinti nel latino, tenuti distinti in italiano. *Retrahere a tangente* è «ritrarre dalla tangente», cioè tirare indietro. |
| *indesinenter*; *perpetuo* | «incessantemente»; «continuamente» | *Constanter* ha già la resa «senza interruzione» (decisione del curatore, F1): qui si usano rese diverse per avverbi diversi. |
| *quam minimus*; *quamproxime*; *jamjam nascens*; *indefinite parvus* | «piccolissimo» (o «il più piccolo possibile»); «con ottima approssimazione»; «appena nascente»; «indefinitamente piccolo» | *Quamproxime* come *quam proxime* nel Fascicolo 3. |
| *æquabilis*, *æquabiliter* | «uniforme», «uniformemente» | Coincide con *uniformiter*; nel Libro I non c’è una distinzione di senso. |
| *applicare ad* | «applicare a» | Termine tecnico: «il quadrato dell’arco applicato al raggio» è il quadrato diviso per il raggio (un’area «applicata» a un segmento dà un altro segmento). Motte «applied to». Equivalente moderno nella nota N6. |
| *semel*, *bis* | «una volta», «due volte» | Nella Prop. VI (*tempus bis inverse*, *ut vis semel & tempus bis*) e nel Cor. 4 (*velocitas bis*): la grandezza presa come fattore due volte, cioè al quadrato. Equivale a *ratio duplicata*. Motte scioglie in «square». |
| *solidum*; *rectangulum*; *contentum sub* | «solido»; «rettangolo»; «contenuto sotto» | Prodotti di tre e di due lunghezze. Il «solido» SP²×QT²/QR è dimensionalmente una lunghezza al cubo. |
| *quadrato-cubus* | «quadrato-cubo» | La quinta potenza (quadrato per cubo). Motte aggiunge «(or fifth power)». |
| *exponens* | «esponente» | Nel senso seicentesco di grandezza che *rappresenta* (*exponit*) un’altra (Prop. VI, Cor. 1: il doppio del triangolo «come esponente del tempo»); non è l’esponente di una potenza. Si veda anche *exponatur per lineam* nel Fascicolo 3, Cor. II. |
| *coire* (*punctis P & Q coeuntibus*) | «riunirsi» | Il passaggio al limite in cui Q tende a P. |
| *altitudo* | «altezza» | La distanza del corpo dal centro (Propp. VII, IX). |
| *ex conicis*; *constat ex conicis* | «per le coniche»; «risulta dalle coniche» | Rinvio alla teoria delle sezioni coniche, non a un’opera precisa. |
| *destruere* | «annullare» | Prop. III: la forza su T è «annullata» dalla forza uguale e contraria. |
| *& contra*; *vice versa*; *vicissim* | «e viceversa»; «viceversa»; «viceversa» | |
| *in consequentia* / *in antecedentia* | «in conseguenza» / «in antecedenza» | Glossario comune; prima occorrenza in S2.12, dove Newton stesso spiega *in consequentia* con *versus plagam in quam fit motus*. Nota N4. |
| *plaga* | «parte» | Come nel Fascicolo 3. |
| *locus proximus* | «il luogo immediatamente successivo» | Prop. VII: il luogo Q in cui il corpo si muoverà subito dopo P. |
| *nostrates* | «i nostri connazionali» | Scolio della Prop. IV; Motte lo omette. |

*Impulsus* compare nella Prop. I (*impulsu unico sed magno*, decisione del curatore) e nel Cor. 3 (*ab impulsibus vis centripetæ*, «dagli impulsi della forza centripeta»): in entrambi i casi è un’azione istantanea che cambia la quantità di moto, e la resa «impulso» è quella prevista dal glossario. *Vis insita* compare una sola volta (Prop. I), resa «forza insita».

### A.1 Proposizione I

**Latino:** *Areas, quas corpora in gyros acta radiis ad immobile centrum virium ductis describunt, & in planis immobilibus consistere, & esse temporibus proportionales.*

**Inglese:** “The areas, which revolving bodies describe by radii drawn to an immovable centre of force do lie in the same immovable planes, and are proportional to the times in which they are described.”

**Scelte.**

- *vi insita* → «per la forza insita» e *impulsu unico sed magno* → «con un impulso unico ma grande»: decisioni del curatore (Fascicolo 3, F2). Motte ha «by its innate force» e «acts at once with a great impulse»: «at once» rende *unico* in senso temporale e perde l’opposizione *unico **sed** magno*.
- *recta pergeret ad c*: *recta* è avverbio, «procederebbe in linea retta»; Motte «proceed directly».
- **Aggiunta di Motte nell’enunciato:** «in the **same** immovable planes». Il latino dice soltanto *in planis immobilibus*.
- **Aggiunta di Motte:** «compels it **afterwards** to continue». Motte rende inoltre *efficiatque ut … declinet & pergat* con due participi coordinati («turning aside … compels»).
- *componendo* → «componendo»: è l’operazione delle proporzioni (*componendo*), non la composizione dei moti. Motte «by composition».
- *ultima perimeter* → «perimetro ultimo», secondo il glossario (*ratio ultima*).
- La pagina ‹39› cade dentro *si ‹39› nil impediret*; nessuna perdita di testo.

**Corollari (S2.03–S2.08).**

- Cor. 2 e 3: la trascrizione ha **ABCU**, **BU**; Motte **ABCV**, **BV**. Nella tipografia latina del Settecento U e V maiuscole sono la stessa lettera: non è una divergenza di sostanza, ma nelle pagine interattive va scelta una sola grafia (si propone V, come in Motte, segnalandolo).
- Cor. 2: *producator* è **refuso probabile della trascrizione** per *producatur*; *ubi arcus illi infinitum diminuuntur* manca probabilmente di *in* (*in infinitum*, come nel Cor. 3). Da verificare sulla stampa. La traduzione segue il senso.
- Cor. 4 e 5: *sagittæ* → «saette» (glossario). **Motte rende «versed sines»**, e così anche nella Prop. VI e nel suo Cor. 1: confonde il termine con *sinus versus*, che Newton usa a parte nella Prop. IV. Nota N1.
- Cor. 4: *retrahuntur ac detorquentur in orbes curvos* → «sono ritratti … e piegati in orbite curve».
- Cor. 6: *per legum corol. v.* → «per il Cor. V delle leggi».

### A.2 Proposizione II

**Latino:** *Corpus omne, quod movetur in linea aliqua curva in plano descripta, & radio ducto ad punctum vel immobile, vel motu rectilineo uniformiter progrediens, describit areas circa punctum illud temporibus proportionales, urgetur a vi centripeta tendente ad idem punctum.*

**Inglese:** “Every body that moves in any curve line described in a plane, and by a radius, drawn to a point either immovable, or moving forward with an uniform rectilinear motion, describes about that point areas proportional to the times, is urged by a centripetal force directed to that point.”

**Scelte e divergenze.**

- *ad punctum vel immobile, vel motu rectilineo uniformiter progrediens* → «a un punto o immobile o avanzante uniformemente di moto rettilineo».
- *per prop. xl. lib. i. elem.*: è la Prop. XL del Libro I degli *Elementi* di Euclide (triangoli uguali su basi uguali e dalla stessa parte stanno fra le stesse parallele). Motte «Prop. XL. Book I, Elem.». Nota N4.
- *triangula quam minima* → «triangoli … piccolissimi»; *SC* nel latino, *CS* in Motte (stessa retta).
- **Aggiunta di Motte (Caso 1):** «some force that **impels** it» per *per vim aliquam in ipsum agentem*.
- **Refuso di Motte 1846 (Caso 2):** «superfices» per «superficies».
- Cor. 1: *rediorum* e *accelaratur* sono **refusi probabili della trascrizione** per *radiorum* e *acceleratur*. Da verificare sulla stampa.
- Cor. 2: la trascrizione non ha il punto finale (*fit motus*); il testo è completo per senso.
- Scolio: *vis aliqua agat perpetuo secundum lineam superficiei descriptæ perpendicularem*: «una forza … lungo una linea perpendicolare alla superficie descritta». Motte ha il plurale «lines».

### A.3 Proposizione III

**Latino:** *Corpus omne, quod radio ad centrum corporis alterius utcunque moti ducto describit areas circa centrum illud temporibus proportionales, urgetur vi composita ex vi centripeta tendente ad corpus illud alterum, & ex vi omni acceleratrice qua corpus illud alterum urgetur.*

**Inglese:** “Every body, that by a radius drawn to the centre of another body, howsoever moved, describes areas about that centre proportional to the times, is urged by a force compounded out of the centripetal force tending to that other body, and of all the accelerative force by which that other body is impelled.”

**Artefatto della trascrizione (segnalato dal curatore).** Nella trascrizione l’intestazione **PROPOSITIO III. THEOREMA III.** compare **due volte** di seguito. È un doppione della pagina web o dell’estrazione, non del testo del 1726: Motte ha una sola intestazione e il testo non ha lacune. La traduzione riporta l’intestazione una sola volta.

**Scelte e divergenze.**

- *urgetur vi composita ex vi centripeta … & ex vi omni acceleratrice*: «da una forza composta della forza centripeta … e di tutta la forza acceleratrice». Motte «impelled» per il secondo *urgetur*: il latino usa lo stesso verbo due volte.
- *destruetur* → «sarà annullata»; Motte «destroyed».
- *per theor. ii.* → «per il Teorema II», cioè la Prop. II; Motte «by Theor. II».
- Cor. 2–3: *quamproxime* → «con ottima approssimazione»; Motte «nearly».
- Cor. 4: *ad aliud (sive immobile sive mobile) centrum* → «verso un altro centro (immobile o mobile)».
- Scolio: *index centri, quod vis illa respicit* → «indice del centro a cui guarda quella forza». Motte parafrasa: «indicates that a centre is respected by that force».

### A.4 Proposizione IV

**Latino:** *Corporum, quæ diversos circulos æquabili motu describunt, vires centripetas ad centra eorundem circulorum tendere; & esse inter se, ut sunt arcuum simul descriptorum quadrata applicata ad circulorum radios.*

**Inglese:** “The centripetal forces of bodies, which by equable motions describe different circles, tend to the centres of the same circles; and are one to the other as the squares of the arcs described in equal times applied to the radii of the circles.”

**Scelte e divergenze.**

- *simul descriptorum* → «descritti nello stesso tempo»; Motte «described in equal times». La differenza è minima ma il latino dice «contemporaneamente».
- *quam mi ‹44› nimis*: la parola è spezzata dal cambio di pagina; si legge *quam minimis*.
- *sinus versi* → «seni versi»; il rimando *per lem. vii.* è riportato come nel latino (anche Motte ha «by Lem. VII»). Nota N6.
- Cor. 6: *reciproce ut quadrata radiorum* → «inversamente proporzionali ai quadrati dei raggi»; Motte «in the duplicate ratio of the radii inversely» (equivalente).
- Cor. 7: la trascrizione ha **Rn**, **Rn-1**, **R2n-1** con gli apici appiattiti: si leggono Rⁿ, Rⁿ⁻¹, R²ⁿ⁻¹. Motte stampa Rⁿ nel testo e R^(n−1), R^(2n−1) come immagini (SVG 28, 29): concordano.
- Cor. 8: *ex demonstratione præcedentium* → «dalla dimostrazione dei casi precedenti»; Motte aggiunge «as appears by».
- Cor. 9: nella trascrizione manca il verbo della proposizione dipendente (*quod arcus … medius proportionalis inter …*): manca probabilmente *sit* o *est*. La traduzione lo integra tra parentesi quadre: «[è]». Motte ha «is». Da verificare sulla stampa.
- Scolio, primo capoverso: *susius* è **refuso probabile della trascrizione** per *fusius* (s lunga letta come s). *Nostrates* («i nostri connazionali») e *etiam* sono **omessi da Motte**, che aggiunge invece i titoli «Sir» e «Dr.».
- Scolio, secondo capoverso: *Datur … per hujus corol. ix.* → «per il Cor. 9 di questa proposizione»; Motte «(by Cor. 9 of this Prop.)».
- Scolio, terzo capoverso: *Demonstrari etiam possunt præcedentia* → «le cose precedenti si possono dimostrare»; Motte restringe al singolare «The preceding Proposition». Più avanti Motte scioglie la condizionale *si polygonum … coincidat cum circulo* in un indicativo («and therefore the polygon … coincides with the circle, as the square …»), che rende la frase sintatticamente zoppa.
- *impingit in circulum* → «urta contro il cerchio»; *urget circulum* → «preme il cerchio»; Motte «strikes», «impels».

### A.5 Proposizione V

**Latino:** *Data quibuscunque in locis velocitate, qua corpus figuram datam viribus ad commune aliquod centrum tendentibus describit, centrum illud invenire.*

**Inglese:** “There being given, in any places, the velocity with which a body describes a given figure, by means of forces directed to some common centre: to find that centre.”

**Scelte e divergenze.**

- L’intestazione della trascrizione è *PROPOSITIO. V.* con un punto in più: irrilevante.
- *ad angulos rectos ducantur AD, DBE, EC*: «si conducano ad angoli retti», cioè perpendicolari ai raggi PA, QB, RC e quindi parallele alle rispettive tangenti.
- **Aggiunta di Motte:** «the right lines TD, VE **produced**».
- Motte: «the velocities of the **bodies**» per *velocitates corporis* (singolare).
- La dimostrazione termina con Q.E.D., benché sia un problema; si conserva «C.V.D.».

### A.6 Proposizione VI

**Latino:** *Si corpus in spatio non resistente circa centrum immobile in orbe quocunque revolvatur, & arcum quemvis jamjam nascentem tempore quam minimo describat, & sagitta arcus duci intelligatur, quæ chordam bisecet, & producta transeat per centrum virium: erit vis centripeta in medio arcus, ut sagitta directe & tempus bis inverse.*

**Inglese:** “In a space void of resistance, if a body revolves in any orbit about an immovable centre, and in the least time describes any arc just then nascent; and the versed sine of that arc is supposed to be drawn bisecting the chord, and produced passing through the centre of force: the centripetal force in the middle of the arc will be as the versed sine directly and the square of the time inversely.”

**Scelte e divergenze.**

- *tempus bis inverse* → «come il tempo due volte inversamente»; *ut vis semel & tempus bis* → «come la forza una volta e il tempo due volte». § A.0. Motte scioglie in «the square of the time».
- *sagitta* → «saetta»; Motte «versed sine» (A.1, nota N1).
- **Letture delle frazioni appiattite** (Cor. 1, 2, 3, 5): «SP quad.×QT quad.QR» = SP²×QT²/QR; «SYq×QPqQR» = SY²×QP²/QR; «QPqQR» = QP²/QR; «SPq×QTqQR» = SP²×QT²/QR. Motte (SVG 30–35) conferma tutte le letture.
- Cor. 1: *ad tangentem … agatur QR* → «si conduce alla tangente QR»; Motte esplicita «meeting the tangent in R». *Sagittæ dupli arcus QP* → «saetta dell’arco doppio di QP»; *pro temporis exponente scribi potest* → «lo si può scrivere come esponente del tempo» (§ A.0).
- Cor. 3: *concentrice* qui non significa «con lo stesso centro» in senso ordinario, ma «con lo stesso centro di curvatura»: il testo stesso lo spiega (*eandem habens curvaturam eundemque radium curvaturæ*). Si conserva «concentricamente».
- Cor. 4: *velocitas bis* → «la velocità due volte»; Motte «the square of the velocity».
- *perpetuò* con l’accento grafico è nella trascrizione; irrilevante.

### A.7 Proposizione VII

**Latino:** *Gyretur corpus in circumferentia circuli, requiritur lex vis centripetæ tendentis ad punctum quodcunque datum.*

**Inglese:** “If a body revolves in the circumference of a circle; it is proposed to find the law of centripetal force directed to any given point.”

**Scelte e divergenze.**

- **Letture.** «RP quad. hoc est QRL» = RP², cioè il rettangolo QR×RL (la trascrizione scrive QRL senza segno di prodotto, come Motte); «QRL×PV quad.AV quad.» = QR×RL×PV²/AV²; «SP quad.QR» = SP²/QR; «SP quad.×PV cub.AV quad.» = SP²×PV³/AV²; «SP×PVAV» = SP×PV/AV. Motte (SVG 36–46) concorda in tutto.
- La frase *Sic fiet … SP quad.×QT quad.QR* non ha il punto finale nella trascrizione.
- **Rimando incompleto.** La trascrizione ha *Ergo (per corol. 1 & prop vi.)*. Motte ha «by Cor. 1 and 5, Prop. VI», e i passi paralleli delle Propp. VIII e IX hanno *per corol. 1. & 5. prop. vi.* Il «5» è probabilmente caduto nella trascrizione: la traduzione lo integra tra parentesi quadre, «per i Cor. 1 e [5] della Prop. VI». Da verificare sulla stampa.
- *ceu ad centrum suum* → «come al suo centro».
- Cor. 1: *quadrato-cubus* → «quadrato-cubo»; Motte aggiunge «(or fifth power)».
- Cor. 2: la trascrizione ha la lettera accentata *à secundo* (grafia del 1726). **Motte esplicita** «parallel to the distance PR of the body from the second centre of force **R**, meeting the tangent PG of the orbit **in G**»: le lettere R e G sono implicite nel latino. «RPq×PT cub. ad SPq×PV cub.» = RP²×PT³ a SP²×PV³; «SP cub.×PV cub.PT cub.» = SP³×PV³/PT³.
- Cor. 3: *contentum utique sub distantia … & quadrato distantiæ* → «la grandezza contenuta sotto la distanza … e il quadrato della distanza»; Motte «the solid … contained under». Motte rende *vires … eædem sunt* al singolare («the force … is the same»).
- **Verifica richiesta dal curatore** del Cor. 3, nella forma usata dalla Prop. XI (forza verso S : forza verso R = SP·RP² : SG³): eseguita numericamente, nota N10.

### A.8 Proposizione VIII

**Latino:** *Moveatur corpus in semicirculo PQA: ad hunc effectum requiritur lex vis centripetæ tendentis ad punctum adeo longinquum S, ut lineæ omnes PS, RS ad id ductæ, pro parallelis haberi possint.*

**Inglese:** “If a body moves in the semi-circumference PQA; it is proposed to find the law of the centripetal force tending to a point S, so remote, that all the lines PS, RS drawn thereto, may be taken for parallels.”

**Scelte e divergenze.**

- *semcirculi* è **refuso probabile della trascrizione** per *semicirculi*.
- **Letture.** «QR×RN+QN» = QR×(RN+QN): Motte (SVG 55) stampa il vincolo sopra RN+QN, cioè la somma va presa intera; la trascrizione l’ha perso. «QT quad.QR æquale 2PM cub.CP quad.» = QT²/QR = 2PM³/CP²; la trascrizione ha *CP quad.,&QT* senza spazio e *CP quad..* con due punti. «2SP quad.CP quad.» = 2SP²/CP².
- Le lettere Z, T, R non sono definite nella Prop. VIII: vengono dalla figura e dalla costruzione delle Propp. VI–VII (tangente PRZ, QT perpendicolare, QR parallela a SP). Nella pagina interattiva vanno introdotte esplicitamente. Nota N11.
- *neglecta ratione determinata* → «trascurato il rapporto determinato»; Motte «neglecting the given ratio».
- Scolio: *ad centrum virium maxime longinquum* → «a un centro delle forze lontanissimo»; Motte «infinitely remote» intensifica.

### A.9 Proposizione IX

**Latino:** *Gyretur corpus in spirali PQS secante radios omnes SP, SQ, &c. in angulo dato: requiritur Lex vis centripetæ tendentis ad centrum spiralis.*

**Inglese:** “If a body revolves in a spiral PQS, cutting all the radii SP, SQ, &c., in a given angle; it is proposed to find the law of the centripetal force tending to the centre of that spiral.”

**Scelte e divergenze.**

- **Lettere diverse:** il latino ha la figura **SPQRT**, Motte **SPRQT**. Le due sigle elencano gli stessi cinque punti in ordine diverso; senza la figura originale non si può dire quale segua il contorno. Si conserva quella del latino.
- **Letture.** «ratio QTQR» = rapporto QT/QR; «QT quad.QR» = QT²/QR; «QTq×SPqQR» = QT²×SP²/QR. Motte (SVG 62–66) concorda.
- *per lemma xi.* → «per il Lemma XI».
- *circuli spiralem concentrice secantis chorda PV* → «la corda PV del cerchio che taglia concentricamente la spirale», nel senso del Cor. 3 della Prop. VI.

### A.10 Lemma XII

**Latino:** *Parallelogramma omnia circa datæ ellipseos vel hyperbolæ diametros quasvis conjugatas descripta esse inter se æqualia.* — *Constat ex conicis.*

**Inglese:** “All parallelograms circumscribed about any conjugate diameters of a given ellipsis or hyperbola are equal among themselves.” — “This is demonstrated by the writers on the conic sections.”

**Scelte.** *Circa … descripta* → «descritti attorno a»; Motte «circumscribed about». *Constat ex conicis* → «Risulta dalle coniche»; Motte amplia in «is demonstrated by the writers on the conic sections». Il lemma non ha dimostrazione né figura propria: per questo non è nella Parte B. Verifica numerica nella nota N13.

### A.11 Proposizione X

**Latino:** *Gyretur corpus in ellipsi: requiritur lex vis centripetæ tendentis ad centrum ellipseos.*

**Inglese:** “If a body revolves in an ellipsis; it is proposed to find the law of the centripetal force tending to the centre of the ellipsis.”

**Scelte e divergenze.**

- *GP, DK diametri aliæ conjugatæ* → «GP, DK altri diametri coniugati»: *aliæ* (al femminile, come spesso *diameter* in latino) li distingue dagli assi CA, CB. **Motte omette** «other».
- *ex conicis* → «per le coniche»; Motte «by the properties of the conic sections». *Conjunctis rationibus* → «congiungendo i rapporti»; Motte «by composition».
- **Letture.** «vG ad QT quad.Pv» = vG a QT²/Pv; «CDq×PFqPCq» = CD²×PF²/PC²; «QT quad.×PCqQR» = QT²×PC²/QR; «2BCq×CAqPC» = 2BC²×CA²/PC; «1PC» = 1/PC; «2DCqPC» = 2DC²/PC; «2DCqPC in PFq» = (2DC²/PC)×PF². Motte (SVG 67–83) concorda in tutto.
- La trascrizione ha *&prodibit* senza spazio: irrilevante.
- Cor. 2: *ad idem punctum axis communis* → «allo stesso punto dell’asse comune»; Motte «of the common **axes**», plurale erroneo. *Ellipseon* è il genitivo plurale alla greca.
- Scolio: *tempra* è **refuso probabile della trascrizione** per *tempora*. *In abscissa positum* → «posto sull’ascissa». *Angulus ordinationis* → «l’angolo delle ordinate».

### A.12 Refusi e anomalie della trascrizione

| Luogo | Trascrizione | Lettura | Tipo |
|---|---|---|---|
| S2.04 | *producator* | *producatur* | refuso probabile |
| S2.04 | *infinitum diminuuntur* | *in infinitum diminuuntur* | omissione probabile di *in* |
| S2.12 | *rediorum*; *accelaratur* | *radiorum*; *acceleratur* | refusi probabili |
| S2.13 | *fit motus* senza punto | — | punteggiatura |
| prima di S2.15 | intestazione *PROPOSITIO III. THEOREMA III.* due volte | una volta | **artefatto (segnalato dal curatore)** |
| S2.30 | *Rn*, *Rn-1*, *R2n-1* | Rⁿ, Rⁿ⁻¹, R²ⁿ⁻¹ | apici appiattiti |
| S2.32 | verbo assente (*quod arcus … medius proportionalis*) | [*est*] | omissione probabile |
| S2.33 | *susius* | *fusius* | refuso probabile (s lunga) |
| S2.48 | *per corol. 1 & prop vi.* | *per corol. 1 & 5 prop. vi.* | omissione probabile di «5» |
| S2.48 | *… SP quad.×QT quad.QR* senza punto | — | punteggiatura |
| S2.54 | *semcirculi* | *semicirculi* | refuso probabile |
| S2.54 | *QR×RN+QN* | QR×(RN+QN) | vincolo perso |
| S2.54 | *CP quad.,&QT*; *CP quad..* | — | spaziatura e punteggiatura |
| S2.64 | *&prodibit* | *& prodibit* | spaziatura |
| S2.67 | *tempra* | *tempora* | refuso probabile |
| passim | frazioni appiattite («SP quad.×QT quad.QR» ecc.) | SP²×QT²/QR ecc. | lette come dichiarato in A.6–A.11 e confermate da Motte |

Nessuno di questi punti è stato verificato sulla stampa del 1726 (vedi «Non ho potuto verificare»). La traduzione segue il senso; la Parte B riporta il latino esatto della trascrizione.

### A.13 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| S2.01 | *in planis immobilibus* | «in the **same** immovable planes» | aggiunta |
| S2.02 | *impulsu unico sed magno* | «at once with a great impulse» | perde l’opposizione *unico sed magno* |
| S2.02 | *vi insita* | «by its innate force» | termine non conforme al glossario |
| S2.02 | *efficiatque ut … pergat* | «compels it **afterwards** to continue» | aggiunta |
| S2.04–S2.05 | *ABCU, BU* | «ABCV, BV» | grafia (U = V) |
| S2.06–S2.07, S2.39–S2.42 | *sagitta* | «versed sine» | **termine errato** (confusione con *sinus versus*) |
| S2.10 | *per vim aliquam in ipsum agentem* | «some force that **impels** it» | aggiunta |
| S2.11 | *superficies* | «superfices» | refuso dell’edizione 1846 |
| S2.14 | *secundum lineam* | «in the direction of lines» | numero |
| S2.15 | *urgetur* (secondo) | «impelled» | verbo non uniforme |
| S2.22 | *simul descriptorum* | «described in equal times» | lieve divergenza |
| S2.33 | *etiam nostrates* | — ; «Sir», «Dr.» | omissione; aggiunta di titoli |
| S2.35 | *præcedentia* | «The preceding Proposition» | restrizione |
| S2.35 | *si polygonum … coincidat* | «the polygon … coincides» | condizionale reso indicativo; sintassi zoppa |
| S2.37 | *actæ TD, VE* | «TD, VE **produced**» | aggiunta |
| S2.38 | *corporis* | «of the bodies» | numero |
| S2.39, S2.40, S2.45 | *tempus bis*, *velocitas bis* | «the square of the time», «the square of the velocity» | resa moderna (corretta nel senso) |
| S2.48 | *per corol. 1 & prop vi.* | «by Cor. 1 and 5, Prop. VI» | Motte ha il «5» che manca nella trascrizione |
| S2.50 | *quadrato-cubus* | «quadrato-cube (or fifth power)» | glossa aggiunta |
| S2.51 | *distantiæ corporis à secundo virium centro parallela* | «parallel to the distance PR … from the second centre of force **R**, meeting the tangent PG … **in G**» | esplicitazione delle lettere |
| S2.52 | *vires … eædem sunt* | «the force … is the same» | numero |
| S2.56 | *maxime longinquum* | «infinitely remote» | intensificazione |
| S2.58 | *SPQRT* | «SPRQT» | lettere in ordine diverso |
| S2.61 | *Constat ex conicis* | «demonstrated by the writers on the conic sections» | ampliamento |
| S2.63 | *diametri aliæ conjugatæ* | «conjugate diameters» | omissione di *aliæ* |
| S2.66 | *axis communis* | «common axes» | numero errato |

Nessuna formula di Motte 1846 in questa sezione risulta sbagliata: tutte le 56 immagini SVG (28–83) sono state rese e confrontate con le letture della trascrizione.

---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. Le verifiche numeriche sono state eseguite con uno script Python (`verifica.py`, conservato con i materiali di lavoro): per una curva data e un centro dato, il punto percorre la curva con velocità areolare costante attorno al centro, e l’accelerazione è calcolata per differenze finite, senza usare la formula da verificare.

### N1. La saetta

La *sagitta* («saetta») è la **freccia dell’arco**: il segmento che, nell’arco piccolissimo, va dal punto medio della corda all’arco, condotto verso il centro delle forze (Prop. I, Cor. 4; Prop. VI). Il nome viene dall’immagine dell’arco teso con la freccia incoccata. Nel cerchio, quando la saetta è perpendicolare alla corda, coincide con il *sinus versus* («seno verso») del semiarco, ed è per questo che nella Prop. IV Newton parla di seni versi. In un’orbita qualsiasi, e con un centro qualsiasi, la saetta è condotta verso il centro e in generale non è perpendicolare alla corda: per questo Motte, che traduce sempre «versed sine», perde una distinzione che il latino mantiene.

### N2. Prop. I: la legge delle aree

In termini moderni è la conservazione del momento angolare per una forza centrale: il doppio dell’area spazzata nell’unità di tempo è *h* = |**r** × **v**|, costante. La dimostrazione di Newton è discreta: il corpo procede per inerzia (Legge I) e riceve a intervalli uguali un **impulso unico ma grande** diretto verso S; poi si passa al limite. Il cuore è geometrico: un impulso diretto verso S sposta C lungo una parallela a SB, e i triangoli SBC, SBc hanno la stessa base SB e la stessa altezza.

*Controllo numerico.* Moto in tre dimensioni con otto impulsi verso S di intensità casuale: le otto aree dei triangoli sono uguali a 0,113636 con tutte le cifre stampate, e le normali ai triangoli coincidono entro 10⁻¹⁶ (stesso piano).

### N3. Prop. I, corollari

- **Cor. 1.** Poiché *v*·*p* = *h* (con *p* perpendicolare dal centro alla tangente), *v* ∝ 1/*p*. Verifica su un’ellisse di prova (*a* = 2, *b* = 1,2) percorsa attorno al fuoco: *v*·*p* = 1,0000000000 in cinque punti.
- **Cor. 3–4.** La diagonale BU = Cc è lo spostamento prodotto dall’impulso; la saetta ne è la metà. In termini moderni, lo scostamento dalla tangente in un tempo *t* è ½*a t*², proporzionale alla forza a parità di tempo: è il contenuto della Prop. VI.
- **Cor. 5.** Il confronto con le saette verticali degli archi parabolici dei proiettili è il confronto fra due scostamenti ½*a t*² e ½*g t*² nello stesso tempo.

### N4. Prop. II e «in conseguenza / in antecedenza»

- La Prop. II è l’inverso della Prop. I. Il rimando a Euclide I.40 serve a concludere che, se i triangoli SBC e SBc sono uguali, C e c stanno su una parallela a SB: dunque lo spostamento Cc, e con esso la forza (Legge II), è diretto lungo BS.
- *In consequentia* («in conseguenza») significa **nel verso del moto**, *in antecedentia* («in antecedenza») **contro il verso del moto**. Newton stesso glossa il primo con «verso la parte verso cui avviene il moto». Nel Cor. 1: se le aree crescono più in fretta dei tempi, la forza ha una componente nel verso del moto (in termini moderni, un momento della forza positivo rispetto al punto).
- Il Cor. 2, per i mezzi resistenti, considera soltanto il caso dell’accelerazione delle aree: un ritardo, infatti, potrebbe essere dovuto alla resistenza stessa, e non permetterebbe di concludere nulla sulla direzione della forza. È un’interpretazione del curatore, non detta da Newton.
- Lo Scolio: una componente della forza perpendicolare al piano non cambia le aree proiettate e va «trascurata nella composizione delle forze».

### N5. Prop. III: moto relativo

Con il Cor. VI delle leggi Newton applica a entrambi i corpi una forza acceleratrice uguale e contraria a quella che agisce su T: il moto relativo non cambia e T diventa inerziale. In termini moderni: se **a**_L − **a**_T è diretta verso T, le aree descritte da L attorno a T sono proporzionali ai tempi, e viceversa. È la premessa per trattare il moto della Luna attorno alla Terra, che a sua volta si muove attorno al Sole; lo Scolio dichiara il metodo: usare l’uniformità delle aree come indice del centro della forza.

### N6. Prop. IV: il moto circolare uniforme

- «Il quadrato dell’arco applicato al raggio», per archi descritti nello stesso tempo *t*, è (*v t*)²/*R*: la Prop. IV dice che la forza centripeta è proporzionale a *v*²/*R*, a parità di tempo. Il passaggio dai seni versi ai quadrati degli archi applicati ai diametri usa la proprietà del cerchio per cui il quadrato della corda è uguale al diametro per il seno verso, e il Lemma VII per sostituire la corda con l’arco; il latino cita soltanto il Lemma VII.
- **Cor. 6.** Se i tempi periodici stanno come *R*^(3/2) (terza legge di Keplero), le forze stanno come 1/*R*². Newton nello Scolio attribuisce l’osservazione anche a Wren, Hooke e Halley.
- **Cor. 7.** Con *T* ∝ *R*ⁿ: *v* ∝ *R*/*T* = *R*^(1−n), quindi *v* inversamente come *R*^(n−1), e *F* ∝ *v*²/*R* = *R*^(1−2n), cioè inversamente come *R*^(2n−1). Verifica: per *n* = ½, 1, 3/2, 2, il prodotto *F*·*R*^(2n−1) è lo stesso (39,478418 = 4π²) per tre raggi diversi.
- **Cor. 9.** Arco *s* = *v t*; caduta *d* = ½ (*v*²/*R*) *t*²; diametro × caduta = 2*R*·½ (*v*²/*R*) *t*² = *v*²*t*² = *s*². Verifica: 0,1296 = 0,1296.
- **Scolio, il poligono.** Ogni riflessione in un vertice cambia la quantità di moto di 2*mv* sin(π/*n*); in un tempo *t* le riflessioni sono *v t* / (2*R* sin(π/*n*)). La somma è *m v*² *t*/*R* **per qualunque numero di lati**: il controllo numerico per *n* = 3, 6, 50, 1000 dà sempre 0,476470588… = *m v*²/*R*. Il passaggio al limite di Newton è quindi esatto già per il poligono, purché le «forze» delle singole riflessioni si sommino in valore assoluto. La «forza centrifuga» di questo Scolio è la spinta del corpo sul cerchio, cioè la reazione alla forza centripeta: non la forza apparente dei sistemi rotanti.

### N7. Prop. V: il centro dalle velocità

Il luogo dei punti le cui distanze da due rette incidenti in T stanno in un rapporto dato è una retta per T. Il punto D ha distanze PA e QB dalle tangenti in P e Q; il centro S ha distanze proporzionali a 1/*v*_P e 1/*v*_Q (Cor. 1 della Prop. I), cioè a PA e QB: dunque S, D, T sono allineati. *Controllo numerico:* ellisse (*a* = 2, *b* = 1,2), centro vero nel fuoco (1,6; 0); tre punti P, Q, R presi a caso, perpendicolari con una costante di proporzionalità arbitraria: il punto d’incontro di TD e VE risulta (1,6; 0) con tutte le cifre. La costruzione presuppone che le perpendicolari siano innalzate dalla parte del centro.

### N8. Prop. VI e i suoi corollari

- In termini moderni: lo scostamento dalla tangente in un tempo *t* piccolo è ½*a t*², quindi *a* = 2·(saetta)/*t*². «Il tempo due volte» è *t*².
- **Cor. 1.** Con *h* doppio della velocità areolare, SP×QT = *h t*, e QR ≈ ½*a t*²: si ottiene *a* = 2*h*² QR/(SP²×QT²). *Controllo:* sull’ellisse di prova con centro nel fuoco e *h* = 1, il prodotto *a*·SP²×QT²/QR vale 2,003 e 2,001 in due punti diversi, con Q a distanza 10⁻³ da P: costante, come richiesto (il valore limite è 2).
- **Cor. 3.** PV è la corda del cerchio osculatore condotta per il centro; vale *F* = 2*h*²/(SY²×PV). **Cor. 4**: poiché *v* = *h*/SY, *F* = 2*v*²/PV.
- Il Cor. 5 è il **metodo** delle Propp. VII–X: data l’orbita e il centro, calcolare SP²×QT²/QR o SY²×PV.

### N9. Prop. VII: cerchio e centro qualsiasi

- Risultato: *F* ∝ 1/(SP²×PV³). *Controllo:* cerchio di raggio 1, S = (0,35; −0,5), cinque posizioni di P: *F*·SP²×PV³ = 8,000000 in tutti i casi (con *h* = 1 il valore atteso è 2*h*²·AV² = 8). Il rapporto fra QT²×SP²/QR e SP²×PV³/AV² tende a 1 (scarti di 5·10⁻⁵ con Q a 10⁻⁴ da P).
- La proporzione RP² : QT² = AV² : PV² risulta **esatta** anche per Q a distanza finita (1,210195 in entrambi i membri), e RP² = QR×RL è la potenza del punto R rispetto al cerchio (verificata a 10⁻¹⁰). Solo la sostituzione di RL con PV è un passaggio al limite (RL/PV = 1,0046 e 1,00046 per due distanze di Q).
- **Cor. 1.** Con S sulla circonferenza, PV = SP e *F* ∝ 1/SP⁵. *Controllo:* *F*·SP⁵ = 8,000000 in tre posizioni.

### N10. Prop. VII, Cor. 2 e Cor. 3 (verifica richiesta dal curatore)

**Enunciato da verificare:** forza verso S : forza verso R = SP·RP² : SG³, con SG condotta da S parallela a RP fino alla tangente, a parità di orbita e di tempo periodico.

**Metodo.** A parità di tempo periodico l’area totale dell’orbita è la stessa, quindi è la stessa la velocità areolare *h*/2 attorno a S e attorno a R. Per ciascun centro ho calcolato l’accelerazione effettiva del punto che percorre l’orbita con velocità areolare costante attorno a quel centro, e ne ho preso il rapporto; poi ho calcolato SG geometricamente. Lo stesso calcolo controlla che ciascuna accelerazione sia diretta verso il proprio centro (scarto angolare ≤ 1,2·10⁻⁸).

**Cor. 2, cerchio** (raggio 1, S = (0,35; −0,5), R = (−0,2; 0,6)):

| posizione di P | *F*_S / *F*_R | SP·RP²/SG³ |
|---|---|---|
| θ = 0,4 | 1,19891332 | 1,19891332 |
| θ = 1,7 | 0,05866398 | 0,05866398 |
| θ = 3,0 | 0,21091258 | 0,21091258 |
| θ = 4,4 | 6,99438037 | 6,99438032 |

Anche il passaggio intermedio del Cor. 2, SG = SP×PV/PT (triangoli simili PSG, TPV), è verificato (1,04679996 = 1,04679996).

**Cor. 3, ellisse** (*a* = 2, *b* = 1,2; S = (0,7; 0,3), R = (−0,9; −0,4), entrambi interni ma non notevoli):

| anomalia eccentrica di P | *F*_S / *F*_R | SP·RP²/SG³ |
|---|---|---|
| 0,3 | 7,17533370 | 7,17533370 |
| 1,2 | 4,49237448 | 4,49237450 |
| 2,5 | 0,72378218 | 0,72378219 |
| 3,9 | 0,10525244 | 0,10525243 |
| 5,3 | 0,57216207 | 0,57216207 |

Accordo entro 3·10⁻⁸ (errore delle differenze finite). **Il Cor. 3 è corretto.** In termini moderni, la forza centrale che mantiene un’orbita è *F* = *h*² *r* / (*p*³ ρ), con *p* perpendicolare dal centro alla tangente e ρ raggio di curvatura; a parità di *h* e di ρ il rapporto è SP·*p*_R³ / (RP·*p*_S³), e poiché SG = *p*_S·RP/*p*_R si ottiene proprio SP·RP²/SG³.

**Uso nella Prop. XI** (S fuoco, R = C centro; E intersezione di SP con il diametro DK parallelo alla tangente): sull’ellisse di prova, in quattro punti, SG = CP·SP/PE (0,45809657 = 0,45809657 ecc.), PE = 2,00000000 = AC, *F*_S·SP² costante (1,38888889) e *F*_C/CP costante (0,17361111). Combinando con la Prop. X (*F*_C ∝ CP) si ottiene *F*_S ∝ PE³/SP², cioè ∝ 1/SP²: è la lettura **PE cub.** del latino 1726, confermata nel Fascicolo 3 (F3).

### N11. Prop. VIII: forza parallela

Se il centro è all’infinito, le «aree» diventano strisce fra parallele e la loro uniformità equivale a una velocità costante nella direzione di CA. Con il cerchio *x*² + *y*² = 1, forza parallela all’asse *y* e *ẋ* costante, si ha esattamente *ÿ* = −*ẋ*²/*y*³: la forza è inversamente proporzionale a PM³. *Controllo:* *ÿ*·PM³ = −1,00000000 in quattro posizioni (calcolo esatto e numerico). Le due proporzioni intermedie (CP² : PM² = PR² : QT² e PR² = QR×(RN+QN)) risultano esatte anche a distanza finita (1,259049 = 1,259049; 1,0000000000). Lo Scolio estende il risultato alle coniche con la forza inversamente come il cubo dell’ordinata; non l’ho verificato.

### N12. Prop. IX: la spirale

La spirale che taglia tutti i raggi sotto un angolo dato è la spirale logaritmica (equiangola), *r* = e^(*k*θ). *Controllo:* con *k* = 0,3 e *h* = 1, *F*·SP³ = 1,09 = 1 + *k*² in quattro punti: la forza è inversamente come il cubo della distanza. Le orbite di questo tipo si avvolgono verso il centro o se ne allontanano: non sono chiuse.

### N13. Lemma XII

È il teorema classico per cui i parallelogrammi circoscritti su due diametri coniugati hanno area costante, uguale a 4*ab* (il rettangolo degli assi). Newton non lo dimostra. *Controllo:* ellisse *a* = 2, *b* = 1,2, tre coppie di diametri coniugati: area 9,6 = 4*ab*; iperbole con gli stessi semiassi, tre coppie: area 9,6. Nella Prop. X il lemma serve nella forma CD×PF = BC×CA (verificato: 2,40000000 = *ab* in quattro punti).

### N14. Prop. X: la forza proporzionale alla distanza

- È l’**oscillatore armonico isotropo**: *F* = *k r* dà ellissi centrate nel centro delle forze. *Controllo:* sull’ellisse di prova *F*/PC = 0,17361111 in quattro punti; la proprietà PvG : Qv² = PC² : CD² è esatta (0,9728906055 in entrambi i membri); la corda di curvatura per C vale PV = 2DC²/PC (4,3985786 contro 4,3985787).
- **Cor. 1** afferma anche l’inverso («se la forza è come la distanza, il corpo si muoverà in un’ellisse»): qui è solo enunciato; l’unicità della traiettoria non è discussa.
- **Cor. 2.** Il periodo è 2π/√*k*, indipendente dall’ellisse. *Controllo:* tre ellissi diverse; in ciascuna il periodo 2π*ab*/*h* coincide con 2π/√*k*, dove *k* è ricavato dall’accelerazione (6,283185 = 6,283185; 47,123890 = 47,123889). L’argomento di Newton per le ellissi con lo stesso asse maggiore usa il fatto che le velocità nei vertici stanno come le ordinate in uno stesso punto dell’asse: in termini moderni, la componente del moto lungo l’asse comune è la stessa oscillazione armonica per tutte.

### N15. Scolio della Prop. X

- Allontanando il centro all’infinito, la forza ∝ distanza diventa, nella regione finita, una forza uniforme: si ritrova la parabola di Galileo (Fascicolo 3, nota N8). Con la forza «mutata in centrifuga», cioè repulsiva e proporzionale alla distanza, le orbite sono iperboli.
- **Ultima affermazione** (dilatando le ordinate in un rapporto dato e conservando il tempo periodico, le forze verso un centro posto sull’ascissa cambiano nel rapporto delle distanze): in termini moderni, una trasformazione affine delle ordinate conserva i rapporti fra le aree, e quindi la legge delle aree; l’accelerazione si trasforma con la stessa mappa lineare e resta diretta al centro. *Controllo:* ellisse attorno a un punto S = (0,9; 0) dell’asse, ordinate dilatate di 1,7 con velocità areolare moltiplicata per 1,7 (stesso periodo): rapporto delle forze = rapporto delle distanze (1,17182666 = 1,17182666; 1,53247904 contro 1,53247902; 1,01911116 = 1,01911116), e la nuova forza è ancora centrale (scarto ≤ 10⁻⁸). L’affermazione vale per un centro qualsiasi sull’ascissa, non solo per il centro dell’ellisse.

### N16. Che cosa *non* dice la Sezione II

La Sezione II determina la legge di forza **data l’orbita e il centro**; non risolve il problema inverso (data la forza, trovare l’orbita), che Newton affronta più avanti. Le conclusioni «inversamente come SP²×PV³», «come PC» ecc. sono proporzionalità lungo una singola orbita: non dicono come la stessa legge si applichi a orbite diverse se non attraverso il tempo periodico (Prop. IV, Cor. 8; Prop. X, Cor. 2).

---

## Controllo della copertura

Pagine 1726 dai marcatori ‹n› della trascrizione; pagine Motte dagli ancoraggi `Page_n` dell’EPUB.

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| S2.01–S2.02 | *Areas, quas corpora in gyros acta* | Prop. I, enunciato e dimostrazione | pp. 38–39 | pp. 103–104 |
| S2.03–S2.08 | *Velocitas corporis in centrum immobile* … *Eadem omnia obtinent* | Prop. I, Cor. 1–6 | pp. 40–41 | pp. 104–105 |
| S2.09–S2.11 | *Corpus omne, quod movetur in linea aliqua curva* | Prop. II, enunciato, Casi 1–2 | p. 41 | pp. 105–106 |
| S2.12–S2.14 | *In spatiis vel mediis non resistentibus* … *Urgeri potest corpus* | Prop. II, Cor. 1–2, Scolio | pp. 41–42 | p. 106 |
| S2.15–S2.16 | *Corpus omne, quod radio ad centrum corporis alterius* | Prop. III, enunciato e dimostrazione | p. 42 | pp. 106–107 |
| S2.17–S2.21 | *Hinc si corpus unum L* … *Quoniam æquabilis arearum descriptio* | Prop. III, Cor. 1–4, Scolio | pp. 42–43 | p. 107 |
| S2.22–S2.23 | *Corporum, quæ diversos circulos* | Prop. IV, enunciato e dimostrazione | pp. 43–44 | p. 107 |
| S2.24–S2.32 | *Cum arcus illi sint ut velocitates* … *Ex eadem demonstratione* | Prop. IV, Cor. 1–9 | pp. 44–45 | pp. 107–108 |
| S2.33–S2.35 | *Casus Corollarii sexti* … *Demonstrari etiam possunt* | Prop. IV, Scolio (tre capoversi) | p. 45 | pp. 108–109 |
| S2.36–S2.38 | *Data quibuscunque in locis velocitate* | Prop. V | p. 46 | pp. 109–110 |
| S2.39–S2.41 | *Si corpus in spatio non resistente* | Prop. VI, enunciato, dimostrazione, *Idem facile* | pp. 46–47 | p. 110 |
| S2.42–S2.46 | *Si corpus P revolvendo* … *Hinc si detur figura* | Prop. VI, Cor. 1–5 | pp. 47–48 | pp. 110–111 |
| S2.47–S2.49 | *Gyretur corpus in circumferentia circuli* | Prop. VII, due dimostrazioni | pp. 48–49 | pp. 111–112 |
| S2.50–S2.52 | *Hinc si punctum datum S* … *Vis, qua corpus P in orbe quocunque* | Prop. VII, Cor. 1–3 | pp. 49–50 | pp. 112–113 |
| S2.53–S2.56 | *Moveatur corpus in semicirculo PQA* | Prop. VIII, *Idem facile*, Scolio | pp. 50–51 | p. 113 |
| S2.57–S2.59 | *Gyretur corpus in spirali PQS* | Prop. IX, due dimostrazioni | pp. 51–52 | pp. 113–114 |
| S2.60–S2.61 | *Parallelogramma omnia circa datæ ellipseos* | Lemma XII | p. 52 | p. 114 |
| S2.62–S2.64 | *Gyretur corpus in ellipsi* | Prop. X, due dimostrazioni | pp. 52–53 | pp. 114–115 |
| S2.65–S2.67 | *Est igitur vis ut distantia* … *Si ellipsis centro in infinitum abeunte* | Prop. X, Cor. 1–2, Scolio | pp. 53–54 | pp. 115–116 |

**Controlli eseguiti.**

1. **Copertura.** Ho riletto in sequenza ogni periodo della trascrizione, da *Areas, quas corpora* a *in ratione distantiarum a centro*, contro la traduzione: nessuna frase manca. Il doppione dell’intestazione della Prop. III è segnalato (A.3, A.12). I 67 identificatori sono consecutivi e unici (controllo automatico).
2. **Parte B.** `check.py` sul file finale: JSON valido, 14 unità, 52 passi; tutte le stringhe `la` (enunciati e passi) sono sottostringhe esatte della trascrizione, tutte le stringhe `en` sono sottostringhe esatte di Motte; ogni identificatore di `copertura` è presente nel testo. Esito riportato nel messaggio di consegna.
3. **Matematica.** Verifiche numeriche (note N2–N15) per le Propp. I, II (implicita nella I), IV (Cor. 7, Cor. 9, Scolio), V, VI (Cor. 1), VII (con Cor. 1, 2, 3 e l’uso nella Prop. XI), VIII, IX, X (con Cor. 2 e Scolio), Lemma XII. Tutti i risultati di Newton risultano corretti; nessun errore aritmetico o geometrico nel testo.
4. **Motte.** Confronto di tutta la sezione corrispondente (pp. 103–116), comprese le 56 formule stampate come immagini (SVG 28–83), rese e lette una per una. Divergenze nel § A.13.
5. **Separazione fra testo e commento.** Il testo tradotto non contiene formule moderne; le integrazioni del curatore sono tra parentesi quadre («[è]» in S2.32, «[5]» in S2.48).

**Non ho potuto verificare:**

- **la stampa del 1726**: nessuno dei refusi elencati in A.12 (*producator*, *rediorum*, *accelaratur*, *susius*, *semcirculi*, *tempra*, il «5» mancante in S2.48, il verbo mancante in S2.32) è stato controllato sulla scansione; sono segnalati come «probabili»;
- **le figure originali** NATP00087-9…19: la disposizione dei punti (per esempio l’ordine SPQRT/SPRQT nella Prop. IX, il lato su cui sono innalzate le perpendicolari della Prop. V) è ricostruita dal testo;
- **lo Scolio della Prop. VIII** (coniche con forza inversamente come il cubo dell’ordinata) e le affermazioni sull’iperbole dello Scolio della Prop. X: non verificati numericamente;
- **la paginazione di Motte** su un esemplare a stampa: deriva dagli ancoraggi dell’EPUB.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Libro I, Sezione II (Propp. I–X, Lemma XII) | **Fascicolo 5, presente documento, prima versione** |
| Refusi della trascrizione (A.12) | Da verificare sulla stampa del 1726 (scansione ECCO), come per il Fascicolo 3 |
| Grafia U/V nei Cor. 2–3 della Prop. I | Da decidere (si propone V, come Motte, con nota) |
| Prop. I nel pilota | Allineare alla traduzione di S2.02 (decisioni F2 già applicate) |
| Prop. VII, Cor. 3 | Verificato numericamente (N10); può essere citato nel Fascicolo della Sezione III per la Prop. XI |
| Pagine interattive | Parte B: 14 unità, 52 passi; nella Prop. X il primo passo (una sola frase latina molto lunga) andrà mostrato in più tempi |
| Figure NATP00087-9…19 | Da consultare per confermare le ricostruzioni di `figura_base` |
| Revisione filologica e scientifica indipendente | Da eseguire |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce traduzioni italiane o inglesi moderne. **Licenza prevista** (decisione del curatore, Fascicolo 3): testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project; i testi di Motte sono di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Unità incluse: le proposizioni e i corollari con dimostrazione geometrica propria. **Escluse**: la Prop. III (argomento fisico senza figura), la Prop. IV (dimostrazione per rapporti, senza figura; lo Scolio del poligono potrebbe diventare una pagina a sé), la Prop. VI nella sua dimostrazione principale (senza figura: le figure 12 e 13 appartengono ai Cor. 1 e 2, inclusi), i corollari senza dimostrazione propria, il Lemma XII (*Constat ex conicis*, nessuna dimostrazione).

Convenzioni:

- `la`: testo latino esatto della trascrizione, refusi e frazioni appiattite compresi; le letture sono in `nota` e nell’apparato;
- `it`: la traduzione di questo fascicolo;
- `en`: Motte 1846, allineato per senso. Le formule che Motte stampa come immagini (`[SVG n]`) sono eliminate dallo strumento di controllo: nelle stringhe `en` restano come spazi vuoti («we shall have , that is, QRL to as to .»). Nella pagina vanno reinserite dalle immagini SVG indicate in nota o nell’apparato;
- `dipende_da`: soltanto i rimandi citati nella frase latina («Leggi, Cor. I» per *per legum corol. 1.*; «Euclide, Elementi I.40» per *per prop. xl. lib. i. elem.*);
- `figura.mostra`: elementi da rendere visibili, cumulativi; `figura.evidenzia`: relazioni da mettere in risalto.

```json
{
 "fascicolo": "05-L1-S2",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase latina",
  "en": "Motte 1846, allineato per senso; le formule stampate come immagini (SVG) sono eliminate dallo strumento di controllo e restano come vuoti nelle stringhe en",
  "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione",
  "la": ""
 },
 "unita": [
  {
   "id": "L1-P1",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. I — legge delle aree",
   "copertura": [
    "S2.01",
    "S2.02"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 103–104"
   },
   "enunciato": {
    "la": "",
    "it": "Le aree che i corpi mossi in giro descrivono con raggi condotti a un centro immobile delle forze giacciono in piani immobili e sono proporzionali ai tempi.",
    "en": "The areas, which revolving bodies describe by radii drawn to an immovable centre of force do lie in the same immovable planes, and are proportional to the times in which they are described."
   },
   "figura_base": {
    "punti": [
     "S",
     "A",
     "B",
     "c",
     "C",
     "D",
     "E",
     "F"
    ],
    "vincoli": [
     "S centro immobile delle forze",
     "AB = Bc, A, B, c allineati (moto per la forza insita)",
     "cC ∥ BS, C su BC",
     "triangoli SAB, SBC, SCD, SDE, SEF di area uguale",
     "tutti i punti nello stesso piano"
    ]
   },
   "passi": [
    {
     "id": "L1-P1-p1",
     "la": "",
     "it": "Si divida il tempo in parti uguali, e nella prima parte del tempo il corpo descriva per la forza insita la retta AB.",
     "en": "For suppose the time to be divided into equal parts, and in the first part of that time let the body by its innate force describe the right line AB.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "S",
       "A",
       "B",
       "segmento AB"
      ],
      "evidenzia": [
       "AB percorso per la forza insita"
      ]
     }
    },
    {
     "id": "L1-P1-p2",
     "la": "",
     "it": "Nella seconda parte del tempo, se nulla lo impedisse, lo stesso corpo procederebbe in linea retta fino a c (per la Legge I), descrivendo la linea Bc uguale ad AB; così che, condotti al centro i raggi AS, BS, cS, risulterebbero descritte aree uguali ASB, BSc.",
     "en": "In the second part of that time, the same would (by Law I.), if not hindered, proceed directly to c, along the line Bc equal to AB; so that by the radii AS, BS, cS, drawn to the centre, the equal areas ASB, BSc, would be described.",
     "dipende_da": [
      "Legge I"
     ],
     "figura": {
      "mostra": [
       "c sul prolungamento di AB",
       "Bc = AB",
       "raggi AS, BS, cS"
      ],
      "evidenzia": [
       "area ASB = area BSc"
      ]
     }
    },
    {
     "id": "L1-P1-p3",
     "la": "",
     "it": "Ma quando il corpo giunge in B, agisca la forza centripeta con un impulso unico ma grande, e faccia sì che il corpo devii dalla retta Bc e prosegua lungo la retta BC.",
     "en": "But when the body is arrived at B, suppose that a centripetal force acts at once with a great impulse, and, turning aside the body from the right line Bc, compels it afterwards to continue its motion along the right line BC.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "impulso in B diretto verso S",
       "nuova direzione BC"
      ],
      "evidenzia": [
       "impulso unico ma grande in B"
      ]
     },
     "nota": "Decisione del curatore: «con un impulso unico ma grande». Motte: «at once with a great impulse»."
    },
    {
     "id": "L1-P1-p4",
     "la": "",
     "it": "Si conduca cC parallela a BS, che incontri BC in C; e, compiuta la seconda parte del tempo, il corpo (per il Cor. I delle leggi) si troverà in C, nello stesso piano del triangolo ASB.",
     "en": "Draw cC parallel to BS meeting BC in C; and at the end of the second part of the time, the body (by Cor. 1. of the Laws) will be found in C, in the same plane with the triangle ASB.",
     "dipende_da": [
      "Leggi, Cor. I"
     ],
     "figura": {
      "mostra": [
       "cC ∥ BS",
       "C = BC ∩ (retta per c parallela a BS)"
      ],
      "evidenzia": [
       "parallelogramma dei moti Bc, cC"
      ]
     }
    },
    {
     "id": "L1-P1-p5",
     "la": "",
     "it": "Si congiunga SC: il triangolo SBC, per le parallele SB, Cc, sarà uguale al triangolo SBc, e quindi anche al triangolo SAB.",
     "en": "Join SC, and, because SB and Cc are parallel, the triangle SBC will be equal to the triangle SBc, and therefore also to the triangle SAB.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "SC",
       "triangoli SBC, SBc"
      ],
      "evidenzia": [
       "area SBC = area SBc (stessa base SB, vertici su una parallela) = area SAB"
      ]
     }
    },
    {
     "id": "L1-P1-p6",
     "la": "",
     "it": "Con un argomento simile, se la forza centripeta agisce successivamente in C, D, E, ecc., facendo sì che il corpo, nelle singole particelle di tempo, descriva le singole rette CD, DE, EF, ecc., queste giaceranno tutte nello stesso piano; e il triangolo SCD sarà uguale al triangolo SBC, SDE a SCD, e SEF a SDE.",
     "en": "By the like argument, if the centripetal force acts successively in C, D, E, &c., and makes the body, in each single particle of time, to describe the right lines CD, DE, EF, &c., they will all lie in the same plane; and the triangle SCD will be equal to the triangle SBC, and SDE to SCD, and SEF to SDE.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "D",
       "E",
       "F",
       "SD",
       "SE",
       "SF",
       "CD",
       "DE",
       "EF"
      ],
      "evidenzia": [
       "triangoli SCD, SDE, SEF uguali a SBC"
      ]
     }
    },
    {
     "id": "L1-P1-p7",
     "la": "",
     "it": "In tempi uguali, dunque, si descrivono aree uguali in un piano immobile; e, componendo, somme qualsiasi di aree SADS, SAFS stanno fra loro come i tempi in cui sono descritte.",
     "en": "And therefore, in equal times, equal areas are described in one immovable plane: and, by composition, any sums SADS, SAFS, of those areas, are one to the other as the times in which they are described.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "aree SADS, SAFS"
      ],
      "evidenzia": [
       "somme di aree proporzionali ai tempi"
      ]
     }
    },
    {
     "id": "L1-P1-p8",
     "la": "",
     "it": "Si aumenti ora il numero dei triangoli e se ne diminuisca la larghezza all’infinito: il loro perimetro ultimo ADF (per il Cor. 4 del Lemma III) sarà una linea curva; e perciò la forza centripeta, dalla quale il corpo è continuamente ritratto dalla tangente di questa curva, agirà incessantemente; e le aree descritte qualsiasi SADS, SAFS, che erano sempre proporzionali ai tempi della descrizione, saranno anche in questo caso proporzionali a quei tempi. C.V.D.",
     "en": "Now let the number of those triangles be augmented, and their breadth diminished in infinitum; and (by Cor. 4, Lem. III.) their ultimate perimeter ADF will be a curve line: and therefore the centripetal force, by which the body is perpetually drawn back from the tangent of this curve, will act continually; and any described areas SADS, SAFS, which are always proportional to the times of description, will, in this case also, be proportional to those times. Q.E.D.",
     "dipende_da": [
      "Lemma III, Cor. 4"
     ],
     "figura": {
      "mostra": [
       "poligonale ADF che tende alla curva"
      ],
      "evidenzia": [
       "passaggio al limite: forza che agisce incessantemente"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P1-Cor1",
   "tipo": "Corollarium",
   "titolo": "Prop. I, Cor. 1 — velocità inversamente come la perpendicolare",
   "copertura": [
    "S2.03"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 104"
   },
   "enunciato": {
    "la": "",
    "it": "La velocità di un corpo attratto verso un centro immobile, in spazi non resistenti, è inversamente proporzionale alla perpendicolare condotta da quel centro sulla tangente rettilinea dell’orbita.",
    "en": "The velocity of a body attracted towards an immovable centre, in spaces void of resistance, is reciprocally as the perpendicular let fall from that centre on the right line that touches the orbit."
   },
   "figura_base": {
    "punti": [
     "S",
     "A",
     "B",
     "C",
     "D",
     "E",
     "F"
    ],
    "vincoli": [
     "triangoli SAB, SBC, SCD, SDE, SEF di area uguale (Prop. I)",
     "perpendicolari da S sulle basi AB, BC, …"
    ]
   },
   "passi": [
    {
     "id": "L1-P1-Cor1-p1",
     "la": "",
     "it": "Infatti la velocità in quei luoghi A, B, C, D, E sta come le basi dei triangoli uguali AB, BC, CD, DE, EF; e queste basi sono inversamente proporzionali alle perpendicolari condotte su di esse.",
     "en": "For the velocities in those places A, B, C, D, E, are as the bases AB, BC, CD, DE, EF, of equal triangles; and these bases are reciprocally as the perpendiculars let fall upon them.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "basi AB, BC, CD, DE, EF",
       "perpendicolari da S sulle basi"
      ],
      "evidenzia": [
       "base × perpendicolare = doppio dell’area, costante"
      ]
     },
     "nota": "Il rimando implicito alla Prop. I non è citato: dipende_da vuoto."
    }
   ]
  },
  {
   "id": "L1-P1-Cor3",
   "tipo": "Corollarium",
   "titolo": "Prop. I, Cor. 3 — forze come le diagonali BU, EZ",
   "copertura": [
    "S2.05"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 104–105"
   },
   "enunciato": {
    "la": "",
    "it": "Se le corde AB, BC e DE, EF di archi descritti in tempi uguali, in spazi non resistenti, si completano nei parallelogrammi ABCU, DEFZ, le forze in B e in E stanno fra loro nel rapporto ultimo delle diagonali BU, EZ, quando quegli archi diminuiscono all’infinito.",
    "en": "If the chords AB, BC, and DE, EF, of arcs described in equal times, in spaces void of resistance, are completed into the parallelograms ABCV, DEFZ; the forces in B and E are one to the other in the ultimate ratio of the diagonals BV, EZ, when those arcs are diminished in infinitum."
   },
   "figura_base": {
    "punti": [
     "S",
     "A",
     "B",
     "C",
     "c",
     "U",
     "D",
     "E",
     "F",
     "f",
     "Z"
    ],
    "vincoli": [
     "ABCU, DEFZ parallelogrammi",
     "BU = Cc, EZ = Ff",
     "BU, EZ dirette verso S"
    ]
   },
   "passi": [
    {
     "id": "L1-P1-Cor3-p1",
     "la": "",
     "it": "Infatti i moti BC ed EF del corpo si compongono (per il Cor. I delle leggi) dei moti Bc, BU ed Ef, EZ; ma BU ed EZ, uguali a Cc e Ff, nella dimostrazione di questa proposizione erano generate dagli impulsi della forza centripeta in B e in E, e perciò sono proporzionali a questi impulsi.",
     "en": "For the motions BC and EF of the body (by Cor. 1 of the Laws) are compounded of the motions Bc, BV, and Ef, EZ: but BV and EZ, which are equal to Cc and Ff, in the demonstration of this Proposition, were generated by the impulses of the centripetal force in B and E, and are therefore proportional to those impulses.",
     "dipende_da": [
      "Leggi, Cor. I",
      "Prop. I (dimostrazione)"
     ],
     "figura": {
      "mostra": [
       "Bc, BU",
       "Ef, EZ",
       "Cc, Ff"
      ],
      "evidenzia": [
       "BU = Cc ∝ impulso in B; EZ = Ff ∝ impulso in E"
      ]
     },
     "nota": "Motte scrive ABCV, BV per ABCU, BU (U e V sono la stessa lettera nella tipografia antica). «in demonstratione propositionis hujus» rimanda alla dimostrazione della Prop. I."
    }
   ]
  },
  {
   "id": "L1-P2",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. II — dalla legge delle aree alla forza centripeta",
   "copertura": [
    "S2.09",
    "S2.10",
    "S2.11"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 105–106"
   },
   "enunciato": {
    "la": "",
    "it": "Ogni corpo che si muove lungo una linea curva descritta in un piano e che, con un raggio condotto a un punto o immobile o avanzante uniformemente di moto rettilineo, descrive attorno a quel punto aree proporzionali ai tempi, è sollecitato da una forza centripeta diretta verso quello stesso punto.",
    "en": "Every body that moves in any curve line described in a plane, and by a radius, drawn to a point either immovable, or moving forward with an uniform rectilinear motion, describes about that point areas proportional to the times, is urged by a centripetal force directed to that point."
   },
   "figura_base": {
    "punti": [
     "S",
     "A",
     "B",
     "c",
     "C",
     "d",
     "D"
    ],
    "vincoli": [
     "triangoli SAB, SBC, SCD uguali",
     "Bc prolungamento di AB, Cd prolungamento di BC",
     "cC ∥ BS, dD ∥ CS (conclusione)"
    ]
   },
   "passi": [
    {
     "id": "L1-P2-p1",
     "la": "",
     "it": "Infatti ogni corpo che si muove lungo una linea curva è piegato dal corso rettilineo da qualche forza che agisce su di esso (per la Legge I).",
     "en": "For every body that moves in a curve line, is (by Law I) turned aside from its rectilinear course by the action of some force that impels it.",
     "dipende_da": [
      "Legge I"
     ],
     "figura": {
      "mostra": [
       "curva",
       "tangente in B"
      ],
      "evidenzia": [
       "scostamento dal moto rettilineo"
      ]
     },
     "nota": "Motte aggiunge «that impels it»."
    },
    {
     "id": "L1-P2-p2",
     "la": "",
     "it": "E quella forza dalla quale il corpo è piegato dal corso rettilineo, ed è costretto a descrivere in tempi uguali triangoli uguali piccolissimi SAB, SBC, SCD, ecc. attorno al punto immobile S, agisce nel luogo B lungo una linea parallela a cC (per la Prop. XL del Libro I degli *Elementi* e per la Legge II), cioè lungo la linea BS; e nel luogo C lungo una linea parallela a dD, cioè lungo la linea SC, ecc.",
     "en": "And that force by which the body is turned off from its rectilinear course, and is made to describe, in equal times, the equal least triangles SAB, SBC, SCD, &c., about the immovable point S (by Prop. XL. Book I, Elem. and Law II), acts in the place B, according to the direction of a line parallel to cC, that is, in the direction of the line BS, and in the place C, according to the direction of a line parallel to dD, that is, in the direction of the line CS, &c.;",
     "dipende_da": [
      "Euclide, Elementi I.40",
      "Legge II"
     ],
     "figura": {
      "mostra": [
       "triangoli uguali SBC, SBc",
       "cC",
       "dD"
      ],
      "evidenzia": [
       "triangoli uguali sulla stessa base SB ⇒ cC ∥ SB"
      ]
     }
    },
    {
     "id": "L1-P2-p3",
     "la": "",
     "it": "Agisce dunque sempre lungo linee dirette a quel punto immobile S. C.V.D.",
     "en": "and therefore acts always in the direction of lines tending to the immovable point S. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "direzioni della forza in B, C, D"
      ],
      "evidenzia": [
       "tutte passano per S"
      ]
     }
    },
    {
     "id": "L1-P2-p4",
     "la": "",
     "it": "E, per il Cor. V delle leggi, è indifferente che la superficie nella quale il corpo descrive la figura curvilinea sia in quiete, oppure si muova uniformemente in linea retta insieme con il corpo, con la figura descritta e con il suo punto S.",
     "en": "And (by Cor. 5 of the Laws) it is indifferent whether the superfices in which a body describes a curvilinear figure be quiescent, or moves together with the body, the figure described, and its point S, uniformly forward in right lines.",
     "dipende_da": [
      "Leggi, Cor. V"
     ],
     "figura": {
      "mostra": [
       "piano della figura in moto uniforme"
      ]
     },
     "nota": "Caso 2. Motte ha «superfices» (refuso per «superficies»)."
    }
   ]
  },
  {
   "id": "L1-P5",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. V — trovare il centro delle forze dalle velocità",
   "copertura": [
    "S2.36",
    "S2.37",
    "S2.38"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 109–110"
   },
   "enunciato": {
    "la": "",
    "it": "Data in luoghi qualsiasi la velocità con cui un corpo descrive una figura data per effetto di forze dirette a un centro comune, trovare quel centro.",
    "en": "There being given, in any places, the velocity with which a body describes a given figure, by means of forces directed to some common centre: to find that centre."
   },
   "figura_base": {
    "punti": [
     "P",
     "Q",
     "R",
     "T",
     "V",
     "A",
     "B",
     "C",
     "D",
     "E",
     "S"
    ],
    "vincoli": [
     "PT, TQV, VR tangenti in P, Q, R",
     "PA ⊥ PT, QB ⊥ TQV, RC ⊥ VR",
     "PA : QB : RC inversamente come le velocità in P, Q, R",
     "AD ∥ PT, DBE ∥ TQV, EC ∥ VR (ad angoli retti con le perpendicolari)",
     "S = TD ∩ VE"
    ]
   },
   "passi": [
    {
     "id": "L1-P5-p1",
     "la": "",
     "it": "Tre rette PT, TQV, VR tocchino la figura descritta in altrettanti punti P, Q, R, e si incontrino in T e V.",
     "en": "Let the three right lines PT, TQV, VR touch the figure described in as many points, P, Q, R, and meet in T and V.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "curva",
       "P",
       "Q",
       "R",
       "tangenti PT, TQV, VR",
       "T",
       "V"
      ]
     }
    },
    {
     "id": "L1-P5-p2",
     "la": "",
     "it": "Sulle tangenti si innalzino le perpendicolari PA, QB, RC inversamente proporzionali alle velocità del corpo nei punti P, Q, R dai quali sono innalzate; cioè in modo che PA stia a QB come la velocità in Q sta alla velocità in P, e QB stia a RC come la velocità in R sta alla velocità in Q.",
     "en": "On the tangents erect the perpendiculars PA, QB, RC, reciprocally proportional to the velocities of the body in the points P, Q, R, from which the perpendiculars were raised; that is, so that PA may be to QB as the velocity in Q to the velocity in P, and QB to RC as the velocity in R to the velocity in Q.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "PA",
       "QB",
       "RC"
      ],
      "evidenzia": [
       "lunghezze inversamente proporzionali alle velocità"
      ]
     }
    },
    {
     "id": "L1-P5-p3",
     "la": "",
     "it": "Per gli estremi A, B, C delle perpendicolari si conducano ad angoli retti AD, DBE, EC, che si incontrino in D ed E; e le rette TD, VE, una volta condotte, si incontreranno nel centro cercato S.",
     "en": "Through the ends A, B, C, of the perpendiculars draw AD, DBE, EC, at right angles, meeting in D and E: and the right lines TD, VE produced, will meet in S, the centre required.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "AD",
       "DBE",
       "EC",
       "D",
       "E",
       "TD",
       "VE",
       "S"
      ],
      "evidenzia": [
       "S = TD ∩ VE"
      ]
     },
     "nota": "Motte aggiunge «produced»."
    },
    {
     "id": "L1-P5-p4",
     "la": "",
     "it": "Infatti le perpendicolari condotte dal centro S sulle tangenti PT, QT sono inversamente proporzionali alle velocità del corpo nei punti P e Q (per il Cor. 1 della Prop. I); e perciò, per costruzione, direttamente proporzionali alle perpendicolari AP, BQ, cioè alle perpendicolari condotte dal punto D sulle tangenti.",
     "en": "For the perpendiculars let fall from the centre S on the tangents PT, QT, are reciprocally as the velocities of the bodies in the points P and Q (by Cor. 1, Prop. I.), and therefore, by construction, as the perpendiculars AP, BQ directly; that is, as the perpendiculars let fall from the point D on the tangents.",
     "dipende_da": [
      "Prop. I, Cor. 1"
     ],
     "figura": {
      "mostra": [
       "perpendicolari da S su PT, QT",
       "perpendicolari da D su PT, QT"
      ],
      "evidenzia": [
       "distanze di S e di D dalle due tangenti nello stesso rapporto"
      ]
     },
     "nota": "Motte: «of the bodies» (plurale) per «corporis»."
    },
    {
     "id": "L1-P5-p5",
     "la": "",
     "it": "Di qui si ricava facilmente che i punti S, D, T sono su una stessa retta.",
     "en": "Whence it is easy to infer that the points S, D, T, are in one right line.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "retta TDS"
      ],
      "evidenzia": [
       "luogo dei punti con rapporto dato delle distanze da due rette per T: una retta per T"
      ]
     }
    },
    {
     "id": "L1-P5-p6",
     "la": "",
     "it": "E con un argomento simile anche i punti S, E, V sono su una stessa retta; e perciò il centro S si trova nell’incontro delle rette TD, VE. C.V.D.",
     "en": "And by the like argument the points S, E, V are also in one right line; and therefore the centre S is in the point where the right lines TD, VE meet. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "retta VES"
      ],
      "evidenzia": [
       "S = TD ∩ VE"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P6-Cor1",
   "tipo": "Corollarium",
   "titolo": "Prop. VI, Cor. 1 — la forza come SP²×QT²/QR inversamente",
   "copertura": [
    "S2.42"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 110–111"
   },
   "enunciato": {
    "la": "",
    "it": "Se un corpo P, ruotando attorno al centro S, descrive la linea curva APQ, e la retta ZPR tocca quella curva in un punto qualsiasi P, e da un altro punto qualsiasi Q della curva si conduce alla tangente QR parallela alla distanza SP, e si abbassa QT perpendicolare a quella distanza SP, la forza centripeta sarà inversamente proporzionale al solido SP²×QT²/QR, purché di quel solido si prenda sempre la quantità che risulta alla fine, quando i punti P e Q si riuniscono.",
    "en": "If a body P revolving about the centre S describes a curve line APQ, which a right line ZPR touches in any point P; and from any other point Q of the curve, QR is drawn parallel to the distance SP, meeting the tangent in R; and QT is drawn perpendicular to the distance SP; the centripetal force will be reciprocally as the solid , if the solid be taken of that magnitude which it ultimately acquires when the points P and Q coincide."
   },
   "figura_base": {
    "punti": [
     "S",
     "A",
     "P",
     "Q",
     "Z",
     "R",
     "T"
    ],
    "vincoli": [
     "curva APQ",
     "ZPR tangente in P",
     "QR ∥ SP, R sulla tangente",
     "QT ⊥ SP, T su SP",
     "Q → P (rapporto ultimo)"
    ]
   },
   "passi": [
    {
     "id": "L1-P6-Cor1-p1",
     "la": "",
     "it": "Infatti QR è uguale alla saetta dell’arco doppio di QP, nel cui mezzo sta P; e il doppio del triangolo SQP, ossia SP×QT, è proporzionale al tempo in cui è descritto quell’arco doppio, e perciò lo si può scrivere come esponente del tempo.",
     "en": "For QR is equal to the versed sine of double the arc QP, whose middle is P: and double the triangle SQP, or is proportional to the time in which that double arc is described; and therefore may be used for the exponent of the time.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "QR",
       "arco doppio di QP con P nel mezzo",
       "triangolo SQP",
       "QT"
      ],
      "evidenzia": [
       "QR = saetta",
       "2·area SQP = SP×QT ∝ tempo"
      ]
     },
     "nota": "Motte rende sagitta con «versed sine». «exponens» = grandezza che rappresenta il tempo."
    }
   ]
  },
  {
   "id": "L1-P6-Cor2",
   "tipo": "Corollarium",
   "titolo": "Prop. VI, Cor. 2 — la forza come SY²×QP²/QR inversamente",
   "copertura": [
    "S2.43"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 111"
   },
   "enunciato": {
    "la": "",
    "it": "Con lo stesso argomento la forza centripeta è inversamente proporzionale al solido SY²×QP²/QR, purché SY sia la perpendicolare condotta dal centro delle forze sulla tangente PR dell’orbita.",
    "en": "By a like reasoning, the centripetal force is reciprocally as the solid ; if SY is a perpendicular from the centre of force on PR the tangent of the orbit."
   },
   "figura_base": {
    "punti": [
     "S",
     "P",
     "Q",
     "R",
     "T",
     "Y"
    ],
    "vincoli": [
     "SY ⊥ tangente PR, Y sulla tangente",
     "QT ⊥ SP"
    ]
   },
   "passi": [
    {
     "id": "L1-P6-Cor2-p1",
     "la": "",
     "it": "Infatti i rettangoli SY×QP e SP×QT sono uguali.",
     "en": "For the rectangles and are equal.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "SY",
       "QP",
       "SP",
       "QT"
      ],
      "evidenzia": [
       "SY×QP = SP×QT = 2·area SQP (alla fine)"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P6-Cor3",
   "tipo": "Corollarium",
   "titolo": "Prop. VI, Cor. 3 — la forza come SY²×PV inversamente (cerchio di curvatura)",
   "copertura": [
    "S2.44"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 111"
   },
   "enunciato": {
    "la": "",
    "it": "Se l’orbita è un cerchio, oppure tocca o taglia un cerchio concentricamente, cioè forma con il cerchio un angolo di contatto o di sezione il più piccolo possibile, avendo la stessa curvatura e lo stesso raggio di curvatura nel punto di contatto P; e se PV è la corda di questo cerchio condotta dal corpo attraverso il centro delle forze, la forza centripeta sarà inversamente proporzionale al solido SY²×PV.",
    "en": "If the orbit is either a circle, or touches or cuts a circle concentrically, that is, contains with a circle the least angle of contact or section, having the same curvature and the same radius of curvature at the point P; and if PV be a chord of this circle, drawn from the body through the centre of force; the centripetal force will be reciprocally as the solid"
   },
   "figura_base": {
    "punti": [
     "S",
     "P",
     "Q",
     "R",
     "Y",
     "V"
    ],
    "vincoli": [
     "cerchio con la stessa curvatura dell’orbita in P",
     "PV corda di quel cerchio passante per S"
    ]
   },
   "passi": [
    {
     "id": "L1-P6-Cor3-p1",
     "la": "",
     "it": "Infatti PV è QP²/QR.",
     "en": "For PV is",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio di curvatura",
       "corda PV"
      ],
      "evidenzia": [
       "PV = limite di QP²/QR"
      ]
     },
     "nota": "Lettura della trascrizione: «QPqQR» = QP²/QR (frazione appiattita). Motte stampa la formula come immagine (SVG 35 = QP²/QR), che lo strumento di controllo elimina: la stringa en è quindi troncata a «For PV is»; in pagina scrivere «For PV is QP²/QR.»"
    }
   ]
  },
  {
   "id": "L1-P7",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. VII — orbita circolare, centro delle forze qualsiasi",
   "copertura": [
    "S2.47",
    "S2.48",
    "S2.49"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 111–112"
   },
   "enunciato": {
    "la": "",
    "it": "Un corpo giri sulla circonferenza di un cerchio: si chiede la legge della forza centripeta diretta verso un punto dato qualsiasi.",
    "en": "If a body revolves in the circumference of a circle; it is proposed to find the law of centripetal force directed to any given point."
   },
   "figura_base": {
    "punti": [
     "V",
     "Q",
     "P",
     "A",
     "S",
     "R",
     "Z",
     "T",
     "L",
     "Y"
    ],
    "vincoli": [
     "cerchio VQPA",
     "S punto dato, PV corda per S",
     "VA diametro",
     "PRZ tangente in P",
     "QT ⊥ SP, prolungata incontra la tangente in Z",
     "LR per Q, LR ∥ SP, L sul cerchio, R sulla tangente",
     "SY ⊥ tangente (seconda dimostrazione)"
    ]
   },
   "passi": [
    {
     "id": "L1-P7-p1",
     "la": "",
     "it": "Sia VQPA la circonferenza del cerchio; S il punto dato verso cui la forza tende come al suo centro; P il corpo portato sulla circonferenza; Q il luogo immediatamente successivo in cui si muoverà; e PRZ la tangente al cerchio nel luogo precedente.",
     "en": "Let VQPA be the circumference of the circle; S the given point to which as to a centre the force tends; P the body moving in the circumference; Q the next place into which it is to move; and PRZ the tangent of the circle at the preceding place.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio VQPA",
       "S",
       "P",
       "Q",
       "tangente PRZ"
      ]
     }
    },
    {
     "id": "L1-P7-p2",
     "la": "",
     "it": "Per il punto S si conduca la corda PV; e, condotto il diametro VA del cerchio, si congiunga AP; si abbassi su SP la perpendicolare QT, che, prolungata, incontri la tangente PR in Z; e infine per il punto Q si conduca LR, parallela a SP, che incontri sia il cerchio in L sia la tangente PZ in R.",
     "en": "Through the point S draw the chord PV, and the diameter VA of the circle: join AP, and draw QT perpendicular to SP, which produced, may meet the tangent PR in Z; and lastly, through the point Q, draw LR parallel to SP, meeting the circle in L, and the tangent PZ in R.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "corda PV",
       "diametro VA",
       "AP",
       "QT",
       "Z",
       "LR",
       "L",
       "R"
      ]
     }
    },
    {
     "id": "L1-P7-p3",
     "la": "",
     "it": "Per la similitudine dei triangoli ZQR, ZTP, VPA, RP², cioè QR×RL, starà a QT² come AV² sta a PV².",
     "en": "And, because of the similar triangles ZQR, ZTP, VPA, we shall have , that is, QRL to as to .",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangoli ZQR, ZTP, VPA"
      ],
      "evidenzia": [
       "RP² = QR×RL (potenza di R)",
       "RP² : QT² = AV² : PV²"
      ]
     },
     "nota": "Motte stampa le formule come immagini (SVG 36–39: RP², QT², AV², PV²), eliminate dallo strumento di controllo: la stringa en resta con i vuoti."
    },
    {
     "id": "L1-P7-p4",
     "la": "",
     "it": "Perciò QR×RL×PV²/AV² è uguale a QT².",
     "en": "And therefore is equal to .",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "QR, RL, QT"
      ],
      "evidenzia": [
       "QR×RL×PV²/AV² = QT²"
      ]
     },
     "nota": "Lettura: «QRL×PV quad.AV quad.» = QR×RL×PV²/AV². Formule di Motte come immagini (SVG 40, 37)."
    },
    {
     "id": "L1-P7-p5",
     "la": "",
     "it": "Si moltiplichino questi uguali per SP²/QR e, riunendosi i punti P e Q, si scriva PV al posto di RL.",
     "en": "Multiply those equals by , and the points P and Q coinciding, for RL write PV;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Q → P",
       "RL → PV"
      ],
      "evidenzia": [
       "RL tende a PV quando Q si riunisce a P"
      ]
     }
    },
    {
     "id": "L1-P7-p6",
     "la": "",
     "it": "Così SP²×PV³/AV² risulterà uguale a SP²×QT²/QR.",
     "en": "then we shall have",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "SP",
       "PV",
       "QT",
       "QR"
      ],
      "evidenzia": [
       "SP²×PV³/AV² = lim SP²×QT²/QR"
      ]
     },
     "nota": "La trascrizione non ha il punto finale. Formula di Motte come immagine (SVG 42)."
    },
    {
     "id": "L1-P7-p7",
     "la": "",
     "it": "Dunque (per i Cor. 1 e [5] della Prop. VI) la forza centripeta è inversamente proporzionale a SP²×PV³/AV²; cioè, poiché AV² è dato, inversamente proporzionale al quadrato della distanza, o altezza, SP e al cubo della corda PV considerati congiuntamente. C.V.T.",
     "en": "And therefore (by Cor. 1 and 5, Prop. VI.) the centripetal force is reciprocally as ; that is (because is given), reciprocally as the square of the distance or altitude SP, and the cube of the chord PV conjunctly. Q.E.I.",
     "dipende_da": [
      "Prop. VI, Cor. 1"
     ],
     "figura": {
      "mostra": [
       "SP",
       "PV"
      ],
      "evidenzia": [
       "forza ∝ 1/(SP²×PV³)"
      ]
     },
     "nota": "La trascrizione ha «per corol. 1 & prop vi.»: manca probabilmente «5» (Motte: «Cor. 1 and 5»; cfr. Propp. VIII e IX). Refuso probabile, da verificare sulla stampa."
    },
    {
     "id": "L1-P7-p8",
     "la": "",
     "it": "Sulla tangente PR prolungata si abbassi la perpendicolare SY: per la similitudine dei triangoli SYP, VPA, AV starà a PV come SP sta a SY; e perciò SP×PV/AV è uguale a SY, e SP²×PV³/AV² è uguale a SY²×PV.",
     "en": "On the tangent PR produced let fall the perpendicular SY; and (because of the similar triangles SYP, VPA), we shall have AV to PV as SP to SY, and therefore , and .",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "SY",
       "Y",
       "triangoli SYP, VPA"
      ],
      "evidenzia": [
       "AV : PV = SP : SY",
       "SY = SP×PV/AV"
      ]
     },
     "nota": "Seconda dimostrazione («Idem aliter»). Formule di Motte come immagini (SVG 44, 45)."
    },
    {
     "id": "L1-P7-p9",
     "la": "",
     "it": "E perciò (per i Cor. 3 e 5 della Prop. VI) la forza centripeta è inversamente proporzionale a SP²×PV³/AV², cioè, poiché AV è dato, inversamente proporzionale a SP²×PV³. C.V.T.",
     "en": "And therefore (by Corol. 3 and 5, Prop. VI), the centripetal force is reciprocally as ; that is (because AV is given), reciprocally as . Q.E.I.",
     "dipende_da": [
      "Prop. VI, Cor. 3",
      "Prop. VI, Cor. 5"
     ],
     "figura": {
      "mostra": [
       "SP",
       "PV"
      ],
      "evidenzia": [
       "forza ∝ 1/(SP²×PV³)"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P7-Cor2",
   "tipo": "Corollarium",
   "titolo": "Prop. VII, Cor. 2 — confronto fra due centri nel cerchio",
   "copertura": [
    "S2.51"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 112–113"
   },
   "enunciato": {
    "la": "",
    "it": "La forza con cui il corpo P ruota nel cerchio APTV attorno al centro delle forze S sta alla forza con cui lo stesso corpo P può ruotare nello stesso cerchio e nello stesso tempo periodico attorno a un altro centro delle forze qualsiasi R, come RP²×SP sta al cubo della retta SG, che è condotta dal primo centro delle forze S fino alla tangente PG dell’orbita ed è parallela alla distanza del corpo dal secondo centro delle forze.",
    "en": "The force by which the body P in the circle APTV revolves about the centre of force S is to the force by which the same body P may revolve in the same circle, and in the same periodic time, about any other centre of force R, as to the cube of the right line SG, which from the first centre of force S is drawn parallel to the distance PR of the body from the second centre of force R, meeting the tangent PG of the orbit in G."
   },
   "figura_base": {
    "punti": [
     "A",
     "P",
     "T",
     "V",
     "S",
     "R",
     "G"
    ],
    "vincoli": [
     "cerchio APTV",
     "PV corda per S, PT corda per R",
     "PG tangente in P",
     "SG ∥ RP, G sulla tangente",
     "stesso tempo periodico per i due centri"
    ]
   },
   "passi": [
    {
     "id": "L1-P7-Cor2-p1",
     "la": "",
     "it": "Infatti, per la costruzione di questa proposizione, la prima forza sta alla seconda come RP²×PT³ sta a SP²×PV³, cioè come SP×RP² sta a SP³×PV³/PT³, ossia (per la similitudine dei triangoli PSG, TPV) a SG³.",
     "en": "For by the construction of this Proposition, the former force is to the latter as to ; that is, as to ; or (because of the similar triangles PSG, TPV) to .",
     "dipende_da": [
      "Prop. VII"
     ],
     "figura": {
      "mostra": [
       "corda PT",
       "corda PV",
       "SG",
       "triangoli PSG, TPV"
      ],
      "evidenzia": [
       "F_S : F_R = RP²×PT³ : SP²×PV³",
       "SG = SP×PV/PT"
      ]
     },
     "nota": "Lettura: «SP cub.×PV cub.PT cub.» = SP³×PV³/PT³. Formule di Motte come immagini (SVG 48, 46, 49, 50, 51)."
    }
   ]
  },
  {
   "id": "L1-P7-Cor3",
   "tipo": "Corollarium",
   "titolo": "Prop. VII, Cor. 3 — confronto fra due centri in un’orbita qualsiasi (usato nella Prop. XI)",
   "copertura": [
    "S2.52"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 113"
   },
   "enunciato": {
    "la": "",
    "it": "La forza con cui il corpo P ruota in un’orbita qualsiasi attorno al centro delle forze S sta alla forza con cui lo stesso corpo P può ruotare nella stessa orbita e nello stesso tempo periodico attorno a un altro centro delle forze qualsiasi R, come SP×RP², cioè la grandezza contenuta sotto la distanza del corpo dal primo centro delle forze S e il quadrato della sua distanza dal secondo centro delle forze R, sta al cubo della retta SG, condotta dal primo centro delle forze S fino alla tangente PG dell’orbita e parallela alla distanza RP del corpo dal secondo centro delle forze.",
    "en": "The force by which the body P in any orbit revolves about the centre of force S, is to the force by which the same body may revolve in the same orbit, and the same periodic time, about any other centre of force R, as the solid , contained under the distance of the body from the first centre of force S, and the square of its distance from the second centre of force R, to the cube of the right line SG, drawn from the first centre of the force S, parallel to the distance RP of the body from the second centre of force R, meeting the tangent PG of the orbit in G."
   },
   "figura_base": {
    "punti": [
     "P",
     "S",
     "R",
     "G"
    ],
    "vincoli": [
     "orbita qualsiasi per P",
     "PG tangente in P",
     "SG ∥ RP, G sulla tangente",
     "stesso tempo periodico (stessa velocità areolare) per i due centri"
    ]
   },
   "passi": [
    {
     "id": "L1-P7-Cor3-p1",
     "la": "",
     "it": "Infatti le forze in quest’orbita, in un suo punto qualsiasi P, sono le stesse che in un cerchio della stessa curvatura.",
     "en": "For the force in this orbit at any point P is the same as in a circle of the same curvature.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio di curvatura in P"
      ],
      "evidenzia": [
       "F_S : F_R = SP×RP² : SG³ (verificato numericamente, nota N10)"
      ]
     },
     "nota": "Motte usa il singolare «the force». Il passo rimanda implicitamente al Cor. 2 e al Cor. 3 della Prop. VI, che non cita."
    }
   ]
  },
  {
   "id": "L1-P8",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. VIII — semicerchio, centro delle forze lontanissimo",
   "copertura": [
    "S2.53",
    "S2.54",
    "S2.55"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 113"
   },
   "enunciato": {
    "la": "",
    "it": "Un corpo si muova nel semicerchio PQA: a questo scopo si chiede la legge della forza centripeta diretta verso un punto S così lontano che tutte le linee PS, RS condotte a esso si possano considerare parallele.",
    "en": "If a body moves in the semi-circumference PQA; it is proposed to find the law of the centripetal force tending to a point S, so remote, that all the lines PS, RS drawn thereto, may be taken for parallels."
   },
   "figura_base": {
    "punti": [
     "P",
     "Q",
     "A",
     "C",
     "M",
     "N",
     "R",
     "Z",
     "T",
     "S"
    ],
    "vincoli": [
     "semicerchio PQA di centro C",
     "CA ⊥ alle parallele PS, RS, in M e N",
     "PRZ tangente in P; QR ∥ PS; QT ⊥ PS (come nella Prop. VII)",
     "R, Q, N sulla stessa parallela"
    ]
   },
   "passi": [
    {
     "id": "L1-P8-p1",
     "la": "",
     "it": "Dal centro C del semicerchio si conduca il semidiametro CA, che tagli perpendicolarmente quelle parallele in M e N, e si congiunga CP.",
     "en": "From C, the centre of the semi-circle, let the semi-diameter CA be drawn, cutting the parallels at right angles in M and N, and join CP.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "C",
       "CA",
       "M",
       "N",
       "CP"
      ]
     },
     "nota": "«semcirculi» è refuso probabile della trascrizione per «semicirculi», da verificare sulla stampa."
    },
    {
     "id": "L1-P8-p2",
     "la": "",
     "it": "Per la similitudine dei triangoli CPM, PZT e RZQ, CP² sta a PM² come PR² sta a QT²; e, per la natura del cerchio, PR² è uguale al rettangolo QR×(RN+QN), ossia, riunendosi i punti P e Q, al rettangolo QR×2PM.",
     "en": "Because of the similar triangles CPM, PZT, and RZQ, we shall have to as to ; and, from the nature of the circle, is equal to the rectangle , or, the points P, Q coinciding, to the rectangle .",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangoli CPM, PZT, RZQ",
       "RN",
       "QN"
      ],
      "evidenzia": [
       "CP² : PM² = PR² : QT²",
       "PR² = QR×(RN+QN) → QR×2PM"
      ]
     },
     "nota": "Lettura: «QR×RN+QN» = QR×(RN+QN); Motte stampa il vincolo sopra RN+QN (SVG 55)."
    },
    {
     "id": "L1-P8-p3",
     "la": "",
     "it": "Dunque CP² sta a PM² come QR×2PM sta a QT²; e perciò QT²/QR è uguale a 2PM³/CP², e QT²×SP²/QR è uguale a 2PM³×SP²/CP².",
     "en": "Therefore is to as to ; and , and .",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "QT",
       "QR",
       "PM"
      ],
      "evidenzia": [
       "QT²/QR = 2PM³/CP²"
      ]
     }
    },
    {
     "id": "L1-P8-p4",
     "la": "",
     "it": "Dunque (per i Cor. 1 e 5 della Prop. VI) la forza centripeta è inversamente proporzionale a 2PM³×SP²/CP², cioè (trascurato il rapporto determinato 2SP²/CP²) inversamente proporzionale a PM³. C.V.T.",
     "en": "And therefore (by Corol. 1 and 5, Prop. VI.), the centripetal force is reciprocally as ; that is , reciprocally as . Q.E.I.",
     "dipende_da": [
      "Prop. VI, Cor. 1",
      "Prop. VI, Cor. 5"
     ],
     "figura": {
      "mostra": [
       "PM"
      ],
      "evidenzia": [
       "forza ∝ 1/PM³"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P9",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. IX — spirale che taglia i raggi sotto un angolo dato",
   "copertura": [
    "S2.57",
    "S2.58",
    "S2.59"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 113–114"
   },
   "enunciato": {
    "la": "",
    "it": "Un corpo giri in una spirale PQS che tagli tutti i raggi SP, SQ, ecc. sotto un angolo dato: si chiede la legge della forza centripeta diretta verso il centro della spirale.",
    "en": "If a body revolves in a spiral PQS, cutting all the radii SP, SQ, &c., in a given angle; it is proposed to find the law of the centripetal force tending to the centre of that spiral."
   },
   "figura_base": {
    "punti": [
     "S",
     "P",
     "Q",
     "R",
     "T",
     "Y",
     "V"
    ],
    "vincoli": [
     "spirale PQS che taglia i raggi sotto un angolo dato",
     "angolo PSQ indefinitamente piccolo",
     "QR ∥ SP, R sulla tangente in P; QT ⊥ SP",
     "SY ⊥ tangente; PV corda del cerchio di curvatura per S"
    ]
   },
   "passi": [
    {
     "id": "L1-P9-p1",
     "la": "",
     "it": "Sia dato l’angolo indefinitamente piccolo PSQ; poiché tutti gli angoli sono dati, sarà data di forma la figura SPQRT.",
     "en": "Suppose the indefinitely small angle PSQ to be given; because, then, all the angles are given, the figure SPRQT will be given in specie.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "S",
       "P",
       "Q",
       "R",
       "T",
       "angolo PSQ"
      ],
      "evidenzia": [
       "figura SPQRT data di forma"
      ]
     },
     "nota": "Motte: «SPRQT» per «SPQRT»."
    },
    {
     "id": "L1-P9-p2",
     "la": "",
     "it": "È dunque dato il rapporto QT/QR, e QT²/QR è come QT, cioè (poiché quella figura è data di forma) come SP.",
     "en": "Therefore the ratio is also given, and is as QT, that is (because the figure is given in specie), as SP.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "QT",
       "QR"
      ],
      "evidenzia": [
       "QT²/QR ∝ QT ∝ SP"
      ]
     }
    },
    {
     "id": "L1-P9-p3",
     "la": "",
     "it": "Si cambi ora in un modo qualsiasi l’angolo PSQ: la retta QR, che sottende l’angolo di contatto QPR, cambierà (per il Lemma XI) nel rapporto duplicato di PR o di QT.",
     "en": "But if the angle PSQ is any way changed, the right line QR, subtending the angle of contact QPR (by Lemma XI) will be changed in the duplicate ratio of PR or QT.",
     "dipende_da": [
      "Lemma XI"
     ],
     "figura": {
      "mostra": [
       "angolo di contatto QPR"
      ],
      "evidenzia": [
       "QR ∝ PR² (rapporto duplicato)"
      ]
     }
    },
    {
     "id": "L1-P9-p4",
     "la": "",
     "it": "Dunque QT²/QR resterà lo stesso di prima, cioè come SP.",
     "en": "Therefore the ratio remains the same as before, that is, as SP.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "QT",
       "QR"
      ],
      "evidenzia": [
       "QT²/QR ∝ SP indipendentemente dall’angolo"
      ]
     }
    },
    {
     "id": "L1-P9-p5",
     "la": "",
     "it": "Perciò QT²×SP²/QR è come SP³, e quindi (per i Cor. 1 e 5 della Prop. VI) la forza centripeta è inversamente proporzionale al cubo della distanza SP. C.V.T.",
     "en": "And is as , and therefore (by Corol. 1 and 5, Prop. VI) the centripetal force is reciprocally as the cube of the distance SP. Q.E.I.",
     "dipende_da": [
      "Prop. VI, Cor. 1",
      "Prop. VI, Cor. 5"
     ],
     "figura": {
      "mostra": [
       "SP"
      ],
      "evidenzia": [
       "forza ∝ 1/SP³"
      ]
     }
    },
    {
     "id": "L1-P9-p6",
     "la": "",
     "it": "La perpendicolare SY condotta sulla tangente e la corda PV del cerchio che taglia concentricamente la spirale stanno all’altezza SP in rapporti dati; e perciò SP³ è come SY²×PV, cioè (per i Cor. 3 e 5 della Prop. VI) inversamente come la forza centripeta.",
     "en": "The perpendicular SY let fall upon the tangent, and the chord PV of the circle concentrically cutting the spiral, are in given ratios to the height SP; and therefore is as , that is (by Corol. 3 and 5, Prop. VI) reciprocally as the centripetal force.",
     "dipende_da": [
      "Prop. VI, Cor. 3",
      "Prop. VI, Cor. 5"
     ],
     "figura": {
      "mostra": [
       "SY",
       "Y",
       "corda PV"
      ],
      "evidenzia": [
       "SY : SP e PV : SP dati ⇒ SY²×PV ∝ SP³"
      ]
     },
     "nota": "Seconda dimostrazione («Idem aliter»)."
    }
   ]
  },
  {
   "id": "L1-P10",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. X — ellisse, forza diretta al centro",
   "copertura": [
    "S2.62",
    "S2.63",
    "S2.64"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 114–115"
   },
   "enunciato": {
    "la": "",
    "it": "Un corpo giri in un’ellisse: si chiede la legge della forza centripeta diretta verso il centro dell’ellisse.",
    "en": "If a body revolves in an ellipsis; it is proposed to find the law of the centripetal force tending to the centre of the ellipsis."
   },
   "figura_base": {
    "punti": [
     "C",
     "A",
     "B",
     "G",
     "P",
     "D",
     "K",
     "F",
     "Q",
     "T",
     "v",
     "R",
     "u",
     "V"
    ],
    "vincoli": [
     "CA, CB semiassi",
     "GP, DK diametri coniugati",
     "PF ⊥ DK (F su DK); QT ⊥ GP",
     "Qv ordinata al diametro GP (Qv ∥ DK)",
     "QvPR parallelogramma (R sulla tangente in P)",
     "seconda dimostrazione: Tu = Tv su PG dall’altra parte di T; uV : vG = DC² : PC²"
    ]
   },
   "passi": [
    {
     "id": "L1-P10-p1",
     "la": "",
     "it": "Siano CA, CB i semiassi dell’ellisse; GP, DK altri diametri coniugati; PF, QT perpendicolari ai diametri; Qv l’ordinata al diametro GP; e, se si completa il parallelogramma QvPR, il rettangolo PvG starà (per le coniche) a Qv² come PC² sta a CD²; e (per la similitudine dei triangoli QvT, PCF) Qv² sta a QT² come PC² sta a PF²; e, congiungendo i rapporti, il rettangolo PvG sta a QT² come PC² sta a CD² e PC² sta a PF², cioè vG sta a QT²/Pv come PC² sta a CD²×PF²/PC².",
     "en": "Suppose CA, CB to be semi-axes of the ellipsis; GP, DK, conjugate diameters; PF, QT perpendiculars to those diameters; Qv an ordinate to the diameter GP; and if the parallelogram QvPR be completed, then (by the properties of the conic sections) the rectangle PvG will be to as to ; and (because of the similar triangles QvT, PCF), to as to ; and, by composition, the ratio of PvG to is compounded of the ratio of to , and of the ratio of to , that is, vG to as to .",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "CA",
       "CB",
       "GP",
       "DK",
       "PF",
       "QT",
       "Qv",
       "parallelogramma QvPR"
      ],
      "evidenzia": [
       "PvG : Qv² = PC² : CD²",
       "Qv² : QT² = PC² : PF²"
      ]
     },
     "nota": "Una sola frase latina; nella pagina conviene mostrarla in tre tempi (costruzione, due proporzioni, composizione). Formule di Motte come immagini (SVG 67–72)."
    },
    {
     "id": "L1-P10-p2",
     "la": "",
     "it": "Si scriva QR al posto di Pv, e (per il Lemma XII) BC×CA al posto di CD×PF, e inoltre (riunendosi i punti P e Q) 2PC al posto di vG; e, moltiplicati fra loro gli estremi e i medi, QT²×PC²/QR risulterà uguale a 2BC²×CA²/PC.",
     "en": "Put QR for Pv, and (by Lem. XII) for ; also (the points P and Q coinciding) 2PC for vG; and multiplying the extremes and means together, we shall have equal to .",
     "dipende_da": [
      "Lemma XII"
     ],
     "figura": {
      "mostra": [
       "QR = Pv",
       "vG → 2PC"
      ],
      "evidenzia": [
       "CD×PF = BC×CA",
       "QT²×PC²/QR = 2BC²×CA²/PC"
      ]
     }
    },
    {
     "id": "L1-P10-p3",
     "la": "",
     "it": "Dunque (per il Cor. 5 della Prop. VI) la forza centripeta è inversamente proporzionale a 2BC²×CA²/PC; cioè (poiché 2BC²×CA² è dato) inversamente proporzionale a 1/PC; cioè direttamente proporzionale alla distanza PC. C.V.T.",
     "en": "Therefore (by Cor. 5, Prop. VI), the centripetal force is reciprocally as ; that is (because is given), reciprocally as ; that is, directly as the distance PC. Q.E.I.",
     "dipende_da": [
      "Prop. VI, Cor. 5"
     ],
     "figura": {
      "mostra": [
       "PC"
      ],
      "evidenzia": [
       "forza ∝ PC"
      ]
     }
    },
    {
     "id": "L1-P10-p4",
     "la": "",
     "it": "Sulla retta PG, dall’altra parte del punto T, si prenda u in modo che Tu sia uguale a Tv; poi si prenda uV che stia a vG come DC² sta a PC².",
     "en": "In the right line PG on the other side of the point T, take the point u so that Tu may be equal to Tv; then take uV, such as shall be to vG as to .",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "u",
       "Tu = Tv",
       "V",
       "uV"
      ],
      "evidenzia": [
       "uV : vG = DC² : PC²"
      ]
     },
     "nota": "Seconda dimostrazione («Idem aliter»)."
    },
    {
     "id": "L1-P10-p5",
     "la": "",
     "it": "E poiché, per le coniche, Qv² sta a PvG come DC² sta a PC², Qv² sarà uguale a Pv×uV.",
     "en": "And because is to PvG as to (by the conic sections), we shall have .",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Qv",
       "Pv",
       "uV"
      ],
      "evidenzia": [
       "Qv² = Pv×uV"
      ]
     }
    },
    {
     "id": "L1-P10-p6",
     "la": "",
     "it": "Si aggiunga da entrambe le parti il rettangolo uPv: ne risulterà il quadrato della corda dell’arco PQ uguale al rettangolo VPv; e perciò il cerchio che tocca la sezione conica in P e passa per il punto Q passerà anche per il punto V.",
     "en": "Add the rectangle uPv to both sides, and the square of the chord of the arc PQ will be equal to the rectangle VPv; and therefore a circle which touches the conic section in P, and passes through the point Q, will pass also through the point V.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "corda PQ",
       "cerchio tangente in P per Q e V"
      ],
      "evidenzia": [
       "PQ² = VP×Pv"
      ]
     },
     "nota": "La trascrizione ha «&prodibit» senza spazio."
    },
    {
     "id": "L1-P10-p7",
     "la": "",
     "it": "Si riuniscano i punti P e Q: il rapporto di uV a vG, che è lo stesso del rapporto di DC² a PC², diventerà il rapporto di PV a PG, ossia di PV a 2PC; e perciò PV sarà uguale a 2DC²/PC.",
     "en": "Now let the points P and Q meet, and the ratio of uV to vG, which is the same with the ratio of to , will become the ratio of PV to PG, or PV to 2PC; and therefore PV will be equal to .",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Q → P",
       "PV corda di curvatura per C"
      ],
      "evidenzia": [
       "PV = 2DC²/PC"
      ]
     }
    },
    {
     "id": "L1-P10-p8",
     "la": "",
     "it": "Pertanto la forza con cui il corpo P ruota nell’ellisse sarà inversamente proporzionale a 2DC²/PC moltiplicato per PF² (per il Cor. 3 della Prop. VI), cioè (poiché 2DC² moltiplicato per PF² è dato) direttamente proporzionale a PC. C.V.T.",
     "en": "And therefore the force by which the body P revolves in the ellipsis will be reciprocally as (by Cor. 3, Prop. VI); that is (because is given) directly as PC. Q.E.I.",
     "dipende_da": [
      "Prop. VI, Cor. 3"
     ],
     "figura": {
      "mostra": [
       "PF",
       "PV"
      ],
      "evidenzia": [
       "forza ∝ 1/(PF²×PV) ∝ PC, perché PF×DC = BC×CA"
      ]
     }
    }
   ]
  }
 ]
}
```

**Fine del Fascicolo 5.**
