> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 15 — Libro II, Sezioni III e IV: resistenza in parte come la velocità e in parte come il suo quadrato; moto circolare nei mezzi resistenti

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo prosegue il Fascicolo 14 (Libro II, Sezione II). Traduce integralmente due sezioni del Libro II, *De motu corporum*:

- la **Sezione III**, *De motu corporum quibus resistitur partim in ratione velocitatis, partim in ejusdem ratione duplicata*: le Proposizioni XI–XIV con tutti i corollari, lo Scolio della Prop. XIII e lo Scolio finale della Sezione;
- la **Sezione IV**, *De corporum circulari motu in mediis resistentibus*: il Lemma III, le Proposizioni XV–XVIII, i nove corollari della Prop. XV, i tre della Prop. XVI, lo Scolio della Prop. XVI e il capoverso conclusivo.

È una traduzione di lavoro, non un’edizione critica validata.

Gli identificatori **II.S3.01–II.S3.31** e **II.S4.01–II.S4.28** e i titoli tematici tra parentesi sono aggiunte editoriali. Servono a orientare la lettura e a controllare la completezza. I numeri romani delle proposizioni, dei teoremi, dei problemi e del lemma, e i numeri dei corollari, appartengono al testo originale. Le integrazioni del curatore sono tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton.

In coda al fascicolo c’è la **Parte B**, con i dati strutturati per le pagine interattive di 10 unità con dimostrazione geometrica: Propp. XI, XII, XIII (e il suo corollario), XIV (e il suo corollario), Lemma III, Propp. XV, XVI e XVII.

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro II, Sezione III, **pp. 265–274**, e Sezione IV, **pp. 274–282** (i marcatori di pagina della trascrizione vanno da ‹266› a ‹274› e da ‹275› a ‹282›). Trascrizione normalizzata del Newton Project, documento **NATP00088**, estratta in testo semplice senza correzioni: `fonti/latino-1726-L2-S03.md` e `fonti/latino-1726-L2-S04.md`. Figure citate: NATP00088-25…37 (non disponibili).
2. **Inglese di confronto.** *Newton’s Principia*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, sezioni corrispondenti (Section III e Section IV del Libro II); Project Gutenberg n. 76404. Estratti: `fonti/motte-1846-L2-S03.md` e `fonti/motte-1846-L2-S04.md`. Gli estratti non hanno marcatori di pagina: nelle tabelle si indica «sezione corrispondente». Le formule stampate come immagini compaiono come `[SVG 536]`–`[SVG 599]`: tutte le 64 immagini sono state rese con `rsvg-convert` dall’EPUB (`src_epub/OEBPS/3191938728343764116_n.svg`) e lette una per una (§ A.14).
3. **Per i rimandi:** Fascicoli 4 (Libro I, Sez. I: Lemma X), 5 (Sez. II: Prop. IX) e 8 (Sezz. VI–VIII: Prop. XXXIV) del progetto; per i rimandi interni al Libro II, la trascrizione latina della Sezione II (`fonti/latino-1726-L2-S02.md`: Lemma II, Propp. VIII, IX, X).
4. **Brief comune** del Libro I, istruzioni del Libro II e Fascicoli 3 e 5 come modelli di formato.

Non ho consultato né riprodotto traduzioni moderne. Non ho potuto vedere la stampa del 1726, la stampa di Motte del 1729 né le figure originali: le relazioni geometriche sono ricostruite dalle sole lettere del testo e controllate con figure di prova numeriche (note N3–N13).

### Criteri di traduzione

- Il testo guida è il latino; l’inglese di Motte serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o si discosta.
- Si applica il **glossario comune** del brief e il **glossario del Libro II** (istruzioni del coordinatore): *resistentia* «resistenza», *medium* «mezzo», *fluidum* «fluido», *densitas* «densità», *momentum* «momento», *in ratione velocitatis* «in rapporto alla velocità», *in duplicata ratione velocitatis* «in rapporto duplicato della velocità», *vis insita* «forza insita», *spatium non resistens* «spazio non resistente», *medium similare* «mezzo omogeneo» (nota N1), *hyperbola* «iperbole», *asymptotos* «asintoto», *area hyperbolica* «area iperbolica», *progressio geometrica* «progressione geometrica», *gravitas* «gravità», *vis centripeta* «forza centripeta», *lineola* «lineetta», *applicare ad* «dividere per», *coire* «riunirsi», *reciproce* «inversamente», *conjunctim* «considerate congiuntamente», *quam minimus* «piccolissimo», *quam proxime* «con ottima approssimazione», Q.E.D. «C.V.D.».
- Le estensioni del glossario proprie di questo fascicolo sono elencate e motivate nel § A.0.
- Gli enunciati latini all’infinito o al congiuntivo (*Si corpori resistitur …*, *Invenire …*) sono resi con l’indicativo e, nei problemi, con l’infinito.
- **Formule.** Le abbreviazioni «APq», «AP quad.», «BD cub.» sono scritte AP², BD³. La trascrizione appiattisce le frazioni («DdGDq» = Dd/GD²; «1GD» = 1/GD) e **perde i radicali** nella Prop. XV («PQ×SP» = PQ×√SP): le frazioni sono rese con la barra e i radicali con √, dichiarando ogni lettura in § A.12. Gli esponenti frazionari sono scritti AS^(3/2), SP^(½n). La notazione di Newton **2BAP** (= 2BA×AP, il doppio rettangolo di BA e AP) e simili (2APQ = 2AP×PQ; 2BPQ = 2BP×PQ) è conservata: nota N2.
- Nessuna formula moderna entra nel testo tradotto: le equazioni differenziali corrispondenti stanno nelle note.

---

## Traduzione italiana

### Sezione III. Il moto dei corpi ai quali si resiste in parte in rapporto alla velocità, in parte in rapporto duplicato di essa

### Proposizione XI. Teorema VIII (resistenza mista, moto per la sola forza insita: velocità e tempo)

**[II.S3.01]** **Se a un corpo si resiste in parte in rapporto alla velocità, in parte in rapporto duplicato della velocità, e il corpo si muove per la sola forza insita in un mezzo omogeneo, e si prendono i tempi in progressione aritmetica, le quantità inversamente proporzionali alle velocità, aumentate di una certa quantità data, saranno in progressione geometrica.**

**[II.S3.02]** Con centro C e con gli asintoti ortogonali CADd e CH si descriva l’iperbole BEe, e siano AB, DE, de parallele all’asintoto CH. Sull’asintoto CD siano dati i punti A, G. E se il tempo è rappresentato dall’area iperbolica ABED, che cresce uniformemente, dico che la velocità può essere rappresentata dalla lunghezza DF, la cui inversa GD, insieme con la CG data, compone la lunghezza CD crescente in progressione geometrica.

**[II.S3.03]** Sia infatti l’areola DEed l’incremento dato, piccolissimo, del tempo; e Dd sarà inversamente come DE, e quindi direttamente come CD. Il decremento di 1/GD, poi, che (per il Lemma II di questo Libro) è Dd/GD², sarà come CD/GD², ossia (CG+GD)/GD², cioè come 1/GD + CG/GD². Dunque, mentre il tempo ABED cresce uniformemente per l’aggiunta delle particelle date EDde, 1/GD decresce nello stesso rapporto della velocità. Infatti il decremento della velocità è come la resistenza, cioè (per ipotesi) come la somma di due quantità, delle quali una è come la velocità, l’altra come il quadrato della velocità; e il decremento di 1/GD è come la somma delle quantità 1/GD e CG/GD², delle quali la prima è la stessa 1/GD, e la seconda, CG/GD², è come 1/GD²: perciò 1/GD, per l’analogia dei decrementi, è come la velocità. E se la quantità GD, inversamente proporzionale a 1/GD, è aumentata della quantità data CG, la somma CD, mentre il tempo ABED cresce uniformemente, crescerà in progressione geometrica. C.V.D.

**[II.S3.04]** *Cor. 1.* Dunque, se, dati i punti A, G, il tempo è rappresentato dall’area iperbolica ABED, la velocità può essere rappresentata da 1/GD, inversa della GD.

**[II.S3.05]** *Cor. 2.* Prendendo poi GA che stia a GD come l’inversa della velocità all’inizio sta all’inversa della velocità alla fine di un tempo qualsiasi ABED, si troverà il punto G. E, trovato questo, la velocità si può trovare a partire da qualsiasi altro tempo dato.

### Proposizione XII. Teorema IX (resistenza mista: velocità e spazio)

**[II.S3.06]** **Poste le stesse cose, dico che, se si prendono gli spazi descritti in progressione aritmetica, le velocità, aumentate di una certa quantità data, saranno in progressione geometrica.**

**[II.S3.07]** Sull’asintoto CD sia dato il punto R e, innalzata la perpendicolare RS, che incontri l’iperbole in S, si rappresenti lo spazio descritto con l’area iperbolica RSED; e la velocità sarà come la lunghezza GD, che con la CG data compone la lunghezza CD decrescente in progressione geometrica, mentre lo spazio RSED aumenta in progressione aritmetica.

**[II.S3.08]** Infatti, poiché l’incremento EDde dello spazio è dato, la lineetta Dd, che è il decremento della GD, sarà inversamente come ED, e quindi direttamente come CD, cioè come la somma della stessa GD e della lunghezza data CG. Ma il decremento della velocità, nel tempo a essa inversamente proporzionale in cui è descritta la particella data DdeE dello spazio, è come la resistenza e il tempo considerati congiuntamente, cioè direttamente come la somma di due quantità, delle quali una è come la velocità, l’altra come il quadrato della velocità, e inversamente come la velocità; e quindi direttamente come la somma di due quantità, delle quali una è data, l’altra è come la velocità. Dunque il decremento sia della velocità sia della linea GD è come una quantità data e una quantità decrescente considerate congiuntamente; e, poiché i decrementi sono analoghi, saranno sempre analoghe le quantità decrescenti, cioè la velocità e la linea GD. C.V.D.

**[II.S3.09]** *Cor. 1.* Se la velocità è rappresentata dalla lunghezza GD, lo spazio descritto sarà come l’area iperbolica DESR.

**[II.S3.10]** *Cor. 2.* E se il punto R è preso a piacere, si troverà il punto G prendendo GR a GD come la velocità all’inizio sta alla velocità dopo che è stato descritto uno spazio qualsiasi RSED. Trovato poi il punto G, è dato lo spazio a partire dalla velocità data, e viceversa.

**[II.S3.11]** *Cor. 3.* Di qui, poiché (per la Prop. XI) è data la velocità a partire dal tempo dato, e per questa proposizione è dato lo spazio a partire dalla velocità data, sarà dato lo spazio a partire dal tempo dato; e viceversa.

### Proposizione XIII. Teorema X (salita e discesa con gravità uniforme: i tempi come settori di cerchio e d’iperbole)

**[II.S3.12]** **Posto che un corpo, attratto verso il basso da una gravità uniforme, salga o scenda in linea retta, e che gli si resista in parte in rapporto alla velocità, in parte in rapporto duplicato di essa, dico che, se per gli estremi di diametri coniugati di un cerchio e di un’iperbole si conducono rette parallele ai diametri, e le velocità sono come certi segmenti di queste parallele, i tempi saranno come i settori delle aree tagliati da rette condotte dal centro agli estremi dei segmenti; e viceversa.**

**[II.S3.13]** *Caso 1.* Supponiamo dapprima che il corpo salga. Con centro D e con un semidiametro qualsiasi DB si descriva il quadrante di cerchio BETF, e per l’estremo B del semidiametro DB si conduca la retta illimitata BAP, parallela al semidiametro DF. Su di essa sia dato il punto A, e si prenda il segmento AP proporzionale alla velocità. E poiché una parte della resistenza è come la velocità e l’altra parte come il quadrato della velocità, sia la resistenza totale in [P] come AP²+2BAP. Si congiungano DA, DP, che taglino il cerchio in E e in T, e si rappresenti la gravità con DA², in modo che la gravità stia alla resistenza come DA² sta ad AP²+2BAP: e il tempo dell’intera salita sarà come il settore di cerchio EDT.

**[II.S3.14]** Si conduca infatti DVQ, che tagli via sia il momento PQ della velocità AP, sia il momento DTV del settore DET corrispondente a un momento dato del tempo; e quel decremento PQ della velocità sarà come la somma delle forze, la gravità DA² e la resistenza AP²+2BAP, cioè (per la Prop. 12 del Libro II degli *Elementi*) come DP². Perciò l’area DPQ, proporzionale a PQ, è come DP²; e l’area DTV, che sta all’area DPQ come DT² sta a DP², è come DT², che è dato. L’area EDT decresce dunque uniformemente, alla maniera del tempo futuro, per la sottrazione delle particelle date DTV, e perciò è proporzionale al tempo dell’intera salita. C.V.D.

**[II.S3.15]** *Caso 2.* Se la velocità nella salita del corpo è rappresentata dalla lunghezza AP come prima, e la resistenza si pone come AP²+2BAP, e se la forza di gravità è minore di quella che può essere rappresentata da DA², si prenda BD di lunghezza tale che AB²−BD² sia proporzionale alla gravità; sia DF perpendicolare e uguale a DB, e per il vertice F si descriva l’iperbole FTVE, i cui semidiametri coniugati siano DB e DF, e che tagli DA in E, e DP, DQ in T e V; e il tempo dell’intera salita sarà come il settore d’iperbole TDE.

**[II.S3.16]** Infatti il decremento PQ della velocità, prodotto in una particella data di tempo, è come la somma della resistenza AP²+2BAP e della gravità AB²−BD², cioè come BP²−BD². Ora l’area DTV sta all’area DPQ come DT² sta a DP²; e perciò, se su DF si abbassa la perpendicolare GT, come GT², ossia GD²−DF², sta a BD², e come GD² sta a BP², e, separando, come DF² sta a BP²−BD². Poiché dunque l’area DPQ è come PQ, cioè come BP²−BD², l’area DTV sarà come DF², che è dato. L’area EDT decresce dunque uniformemente in singole particelle di tempo uguali, per la sottrazione di altrettante particelle date DTV, e perciò è proporzionale al tempo. C.V.D.

**[II.S3.17]** *Caso 3.* Sia AP la velocità nella discesa del corpo, AP²+2BAP la resistenza e BD²−AB² la forza di gravità, essendo retto l’angolo DBA. E se con centro D e vertice principale B si descrive l’iperbole rettangola BETV, che tagli i prolungamenti di DA, DP e DQ in E, T e V, il settore DET di questa iperbole sarà come il tempo della discesa.

**[II.S3.18]** Infatti l’incremento PQ della velocità, e l’area DPQ a esso proporzionale, è come l’eccesso della gravità sulla resistenza, cioè come BD²−AB²−2BAP−AP², ossia BD²−BP². E l’area DTV sta all’area DPQ come DT² sta a DP², e quindi come GT², ossia GD²−BD², sta a BP², e come GD² sta a BD², e, separando, come BD² sta a BD²−BP². Poiché dunque l’area DPQ è come BD²−BP², l’area DTV sarà come BD², che è dato. L’area EDT cresce dunque uniformemente in singole particelle di tempo uguali, per l’aggiunta di altrettante particelle date DTV, e perciò è proporzionale al tempo della discesa. C.V.D.

**[II.S3.19]** *Cor.* Se con centro D e con semidiametro DA si conduce per il vertice A un arco At simile all’arco ET, che sottenda in modo simile l’angolo ADT, la velocità AP starà alla velocità che il corpo, nel tempo EDT, potrebbe perdere salendo o acquistare scendendo in uno spazio non resistente, come l’area del triangolo DAP sta all’area del settore DAt; e quindi è data a partire dal tempo dato. Infatti la velocità, in un mezzo non resistente, è proporzionale al tempo, e perciò a questo settore; in un mezzo resistente è come il triangolo; e nell’uno e nell’altro mezzo, quando è piccolissima, si avvicina al rapporto di uguaglianza, come fanno il settore e il triangolo.

**[II.S3.20]** *Scolio.* Si potrebbe dimostrare anche il caso della salita del corpo in cui la forza di gravità è minore di quella che può essere rappresentata da DA², ossia da AB²+BD², e maggiore di quella che può essere rappresentata da AB²−BD², e deve essere rappresentata da AB². Ma mi affretto ad altro.

### Proposizione XIV. Teorema XI (gli spazi di salita e di discesa come differenza di due aree)

**[II.S3.21]** **Poste le stesse cose, dico che lo spazio descritto nella salita o nella discesa è come la differenza fra l’area con cui è rappresentato il tempo e un’altra certa area, che aumenta o diminuisce in progressione aritmetica, se le forze composte della resistenza e della gravità si prendono in progressione geometrica.**

**[II.S3.22]** Si prenda AC (nelle tre ultime figure) proporzionale alla gravità, e AK proporzionale alla resistenza. Si prendano poi dalla stessa parte del punto A se il corpo scende, altrimenti da parti contrarie. Si innalzi Ab, che stia a DB come DB² sta a 4BAC; e, descritta l’iperbole bN con gli asintoti ortogonali CK, CH, e innalzata KN perpendicolare a CK, l’area AbNK aumenterà o diminuirà in progressione aritmetica, mentre le forze CK si prendono in progressione geometrica. Dico dunque che la distanza del corpo dalla sua altezza massima è come l’eccesso dell’area AbNK sull’area DET.

**[II.S3.23]** Infatti, poiché AK è come la resistenza, cioè come AP²+2BAP, si assuma una quantità data qualsiasi Z, e si ponga AK uguale a (AP²+2BAP)/Z; e (per il Lemma II di questo Libro) il momento KL di AK sarà uguale a (2APQ+2BA×PQ)/Z, ossia 2BPQ/Z, e il momento KLON dell’area AbNK sarà uguale a 2BPQ×LO/Z, ossia BPQ×BD³/(2Z×CK×AB).

**[II.S3.24]** *Caso 1.* Ora, se il corpo sale, e la gravità è come AB²+BD², essendo BET un cerchio (nella prima figura), la linea AC, che è proporzionale alla gravità, sarà (AB²+BD²)/Z, e DP², ossia AP²+2BAP+AB²+BD², sarà AK×Z+AC×Z, ossia CK×Z; e perciò l’area DTV starà all’area DPQ come DT², o DB², sta a CK×Z.

**[II.S3.25]** *Caso 2.* Se invece il corpo sale, e la gravità è come AB²−BD², la linea AC (nella seconda figura) sarà (AB²−BD²)/Z, e DT² starà a DP² come DF², ossia DB², sta a BP²−BD², ossia ad AP²+2BAP+AB²−BD², cioè ad AK×Z+AC×Z, ossia a CK×Z. E perciò l’area DTV starà all’area DPQ come DB² sta a CK×Z.

**[II.S3.26]** *Caso 3.* E con lo stesso argomento, se il corpo scende, e perciò la gravità è come BD²−AB², e la linea AC (nella terza figura) è uguale a (BD²−AB²)/Z, l’area DTV starà all’area DPQ come DB² sta a CK×Z, come sopra.

**[II.S3.27]** Poiché dunque quelle aree sono sempre in questo rapporto, se al posto dell’area DTV, con cui è rappresentato il momento del tempo, sempre uguale a sé stesso, si scrive un rettangolo determinato qualsiasi, per esempio BD×m, l’area DPQ, cioè ½BD×PQ, starà a BD×m come CK×Z sta a BD². E di qui PQ×BD³ risulta uguale a 2BD×m×CK×Z, e il momento KLON dell’area AbNK, trovato sopra, diventa BP×BD×m/AB. Si tolga il momento DTV dell’area DET, ossia BD×m, e resterà AP×BD×m/AB. La differenza dei momenti, cioè il momento della differenza delle aree, è dunque uguale ad AP×BD×m/AB; e perciò, essendo dato BD×m/AB, è come la velocità AP, cioè come il momento dello spazio che il corpo descrive salendo o scendendo. E quindi la differenza delle aree e quello spazio, che crescono o decrescono per momenti proporzionali e cominciano insieme o svaniscono insieme, sono proporzionali. C.V.D.

**[II.S3.28]** *Cor.* Se la lunghezza che si ottiene dividendo l’area DET per la linea ED [il calcolo che segue richiede BD: § A.4] si chiama M, e si prende un’altra lunghezza V che stia alla lunghezza M nel rapporto che la linea DA ha con la linea DE, lo spazio che il corpo descrive in un mezzo resistente nell’intera salita o discesa starà allo spazio che il corpo, cadendo dalla quiete, può descrivere nello stesso tempo in un mezzo non resistente, come la differenza delle aree suddette sta a BD×V²/AB; e quindi è dato a partire dal tempo dato.

**[II.S3.29]** Infatti lo spazio in un mezzo non resistente è in rapporto duplicato del tempo, ossia come V²; e, essendo dati BD e AB, come BD×V²/AB. Quest’area è uguale all’area DA²×BD×M²/(DE²×AB), e il momento di M è m; e perciò il momento di quest’area è DA²×BD×2M×m/(DE²×AB). Ora questo momento sta al momento della differenza delle aree suddette DET e AbNK, cioè ad AP×BD×m/AB, come DA²×BD×M/DE² sta a ½BD×AP, ossia come DA²/DE² moltiplicato per DET sta a DAP; e quindi, quando le aree DET e DAP sono piccolissime, in rapporto di uguaglianza. Dunque l’area BD×V²/AB e la differenza delle aree DET e AbNK, quando tutte queste aree sono piccolissime, hanno momenti uguali; e perciò sono uguali. Di qui, poiché le velocità, e perciò anche gli spazi descritti nello stesso tempo nei due mezzi, all’inizio della discesa o alla fine della salita si avvicinano all’uguaglianza, e quindi stanno allora fra loro come l’area BD×V²/AB e la differenza delle aree DET e AbNK; e poiché inoltre lo spazio nel mezzo non resistente è continuamente come BD×V²/AB, e lo spazio nel mezzo resistente è continuamente come la differenza delle aree DET e AbNK; è necessario che gli spazi descritti nei due mezzi in tempi uguali qualsiasi stiano fra loro come quell’area BD×V²/AB e la differenza delle aree DET e AbNK. C.V.D.

### Scolio (le tre origini della resistenza)

**[II.S3.30]** La resistenza dei corpi sferici nei fluidi nasce in parte dalla tenacità, in parte dall’attrito e in parte dalla densità del mezzo. E la parte della resistenza che nasce dalla densità del fluido abbiamo detto che è in rapporto duplicato della velocità; l’altra parte, che nasce dalla tenacità del fluido, è uniforme, ossia come il momento del tempo; e quindi si potrebbe ora passare al moto dei corpi ai quali si resiste in parte con una forza uniforme, ossia in rapporto ai momenti del tempo, e in parte in rapporto duplicato della velocità. Ma basta aver aperto l’accesso a questa indagine nelle Proposizioni VIII e IX precedenti e nei loro corollari.

**[II.S3.31]** In esse, infatti, al posto della resistenza uniforme del corpo che sale, che nasce dalla sua gravità, si può sostituire la resistenza uniforme che nasce dalla tenacità del mezzo, quando il corpo si muove per la sola forza insita; e, quando il corpo sale in linea retta, si può aggiungere questa resistenza uniforme alla forza di gravità, e sottrarla quando il corpo scende in linea retta. Si potrebbe anche passare al moto dei corpi ai quali si resiste in parte uniformemente, in parte in rapporto alla velocità e in parte in rapporto duplicato della velocità. E ho aperto la via nelle Proposizioni XIII e XIV precedenti, nelle quali la resistenza uniforme che nasce dalla tenacità del mezzo può anche essere sostituita alla forza di gravità, o essere composta con essa, come prima. Ma mi affretto ad altro.

### Sezione IV. Il moto circolare dei corpi nei mezzi resistenti

### Lemma III (la spirale che taglia i raggi sotto angoli uguali)

**[II.S4.01]** **Sia PQR una spirale che tagli tutti i raggi SP, SQ, SR, ecc. sotto angoli uguali. Si conduca la retta PT, che la tocchi in un punto qualsiasi P e tagli il raggio SQ in T; e, innalzate sulla spirale le perpendicolari PO, QO, che concorrono in O, si congiunga SO. Dico che, se i punti P e Q si avvicinano l’uno all’altro e si riuniscono, l’angolo PSO diventerà retto, e il rapporto ultimo del rettangolo TQ×2PS a PQ² sarà il rapporto di uguaglianza.**

**[II.S4.02]** Infatti dagli angoli retti OPQ, OQR si sottraggano gli angoli uguali SPQ, SQR, e resteranno uguali gli angoli OPS, OQS. Dunque il cerchio che passa per i punti O, S, P passerà anche per il punto Q. Si riuniscano i punti P e Q: questo cerchio, nel luogo PQ della loro riunione, toccherà la spirale, e quindi taglierà perpendicolarmente la retta OP. OP diventerà dunque un diametro di questo cerchio, e l’angolo OSP, nel semicerchio, sarà retto. C.V.D.

**[II.S4.03]** Su OP si abbassino le perpendicolari QD, SE, e i rapporti ultimi delle linee saranno di questo genere: TQ sta a PD come TS, o PS, sta a PE, ossia come 2PO sta a 2PS; inoltre PD sta a PQ come PQ sta a 2PO; e, per uguaglianza perturbata, TQ sta a PQ come PQ sta a 2PS. Di qui PQ² risulta uguale a TQ×2PS. C.V.D.

### Proposizione XV. Teorema XII (la spirale in un mezzo di densità inversamente come la distanza)

**[II.S4.04]** **Se la densità del mezzo nei singoli luoghi è inversamente come la distanza dei luoghi da un centro immobile, e la forza centripeta è in rapporto duplicato della densità, dico che il corpo può girare in una spirale che interseca sotto un angolo dato tutti i raggi condotti da quel centro.**

**[II.S4.05]** Si pongano le stesse cose del lemma precedente, e si prolunghi SQ fino a V, in modo che SV sia uguale a SP. In un tempo qualsiasi, in un mezzo resistente, il corpo descriva l’arco piccolissimo PQ, e in un tempo doppio l’arco piccolissimo PR; e i decrementi di questi archi dovuti alla resistenza, ossia i difetti rispetto agli archi che sarebbero descritti negli stessi tempi in un mezzo non resistente, staranno fra loro come i quadrati dei tempi in cui sono generati. Il decremento dell’arco PQ è dunque la quarta parte del decremento dell’arco PR. Di qui, anche, se si prende l’area QSr uguale all’area PSQ, il decremento dell’arco PQ sarà uguale alla metà della lineetta Rr; e quindi la forza di resistenza e la forza centripeta stanno fra loro come le lineette ½Rr e TQ, che esse generano nello stesso tempo.

**[II.S4.06]** Poiché la forza centripeta da cui il corpo è sollecitato in P è inversamente come SP², e (per il Lemma X del Libro I) la lineetta TQ, che è generata da quella forza, è nel rapporto composto del rapporto di questa forza e del rapporto duplicato del tempo in cui è descritto l’arco PQ (trascuro infatti in questo caso la resistenza, come infinitamente minore della forza centripeta), TQ×SP², cioè (per l’ultimo lemma) ½PQ²×SP, sarà in rapporto duplicato del tempo; e quindi il tempo è come PQ×√SP, e la velocità del corpo con cui in quel tempo è descritto l’arco PQ è come PQ/(PQ×√SP), ossia 1/√SP, cioè inversamente in rapporto subduplicato di SP. E con un argomento simile la velocità con cui è descritto l’arco QR è inversamente in rapporto subduplicato di SQ.

**[II.S4.07]** Ora quegli archi PQ e QR stanno fra loro come le velocità con cui sono descritti, cioè in rapporto subduplicato di SQ a SP, ossia come SQ sta a √(SP×SQ); e, per gli angoli uguali SPQ, SQr e le aree uguali PSQ, QSr, l’arco PQ sta all’arco Qr come SQ sta a SP. Si prendano le differenze dei conseguenti proporzionali, e l’arco PQ starà all’arco Rr come SQ sta a SP−√(SP×SQ), ossia a ½VQ. Infatti, quando i punti P e Q si riuniscono, il rapporto ultimo di SP−√(SP×SQ) a ½VQ è di uguaglianza.

**[II.S4.08]** Poiché il decremento dell’arco PQ dovuto alla resistenza, ossia il suo doppio Rr, è come la resistenza e il quadrato del tempo considerati congiuntamente, la resistenza sarà come Rr/(PQ²×SP). Ma PQ stava a Rr come SQ sta a ½VQ, e di qui Rr/(PQ²×SP) diventa come ½VQ/(PQ×SP×SQ), ossia come ½OS/(OP×SP²). Infatti, quando i punti P e Q si riuniscono, SP e SQ coincidono, e l’angolo PVQ diventa retto; e, per la similitudine dei triangoli PVQ, PSO, PQ sta a ½VQ come OP sta a ½OS. Dunque OS/(OP×SP²) è come la resistenza, cioè nel rapporto della densità del mezzo in P e nel rapporto duplicato della velocità considerati congiuntamente. Si tolga il rapporto duplicato della velocità, cioè il rapporto 1/SP, e resterà la densità del mezzo in P come OS/(OP×SP). Sia data la spirale: poiché è dato il rapporto di OS a OP, la densità del mezzo in P sarà come 1/SP. Dunque in un mezzo la cui densità è inversamente come la distanza SP dal centro il corpo può girare in questa spirale. C.V.D.

**[II.S4.09]** *Cor. 1.* La velocità in un luogo qualsiasi P è sempre quella con cui un corpo, in un mezzo non resistente, con la stessa forza centripeta, può girare in un cerchio alla stessa distanza SP dal centro.

**[II.S4.10]** *Cor. 2.* La densità del mezzo, se è data la distanza SP, è come OS/OP; se invece quella distanza non è data, come OS/(OP×SP). E di qui si può adattare una spirale a qualsiasi densità del mezzo.

**[II.S4.11]** *Cor. 3.* La forza di resistenza in un luogo qualsiasi P sta alla forza centripeta nello stesso luogo come ½OS sta a OP. Quelle forze, infatti, stanno fra loro come ½Rr e TQ, ossia come ¼VQ×PQ/SQ e ½PQ²/SP, cioè come ½VQ e PQ, ossia come ½OS e OP. Data dunque la spirale, è data la proporzione della resistenza alla forza centripeta; e, viceversa, da quella proporzione data è data la spirale.

**[II.S4.12]** *Cor. 4.* Il corpo, dunque, non può girare in questa spirale se non dove la forza di resistenza è minore della metà della forza centripeta. Si faccia la resistenza uguale alla metà della forza centripeta, e la spirale coinciderà con la retta PS; e lungo questa retta il corpo scenderà verso il centro con una velocità che sta alla velocità con cui, come abbiamo provato sopra nel caso della parabola (Teorema X del Libro I [Prop. XXXIV]), avviene la discesa in un mezzo non resistente, in rapporto subduplicato dell’unità al numero due. E i tempi della discesa saranno qui inversamente come le velocità, e quindi sono dati.

**[II.S4.13]** *Cor. 5.* E poiché a distanze uguali dal centro la velocità è la stessa nella spirale PQR e nella retta SP, e la lunghezza della spirale sta alla lunghezza della retta PS in un rapporto dato, cioè nel rapporto di OP a OS, il tempo della discesa lungo la spirale starà al tempo della discesa lungo la retta SP in quello stesso rapporto dato, e perciò è dato.

**[II.S4.14]** *Cor. 6.* Se con centro S e con due intervalli dati qualsiasi si descrivono due cerchi e, restando fermi questi cerchi, si cambia in un modo qualsiasi l’angolo che la spirale forma con il raggio PS, il numero delle rivoluzioni che il corpo può compiere fra le circonferenze dei cerchi, procedendo lungo la spirale da una circonferenza all’altra, è come PS/OS, ossia come la tangente dell’angolo che la spirale forma con il raggio PS; il tempo delle stesse rivoluzioni, invece, è come OP/OS, cioè come la secante dello stesso angolo, o anche inversamente come la densità del mezzo.

**[II.S4.15]** *Cor. 7.* Se un corpo, in un mezzo la cui densità è inversamente come la distanza dei luoghi dal centro, compie attorno a quel centro una rivoluzione lungo una curva qualsiasi AEB, e taglia in B il primo raggio AS sotto lo stesso angolo sotto cui prima lo aveva tagliato in A, e con una velocità che stia alla sua prima velocità in A inversamente in rapporto subduplicato delle distanze dal centro (cioè come AS sta alla media proporzionale fra AS e BS), quel corpo continuerà a compiere innumerevoli rivoluzioni simili BFC, CGD, ecc., e con le intersezioni dividerà il raggio AS nelle parti AS, BS, CS, DS, ecc., continuamente proporzionali. I tempi delle rivoluzioni, poi, staranno direttamente come i perimetri delle orbite AEB, BFC, CGD, ecc., e inversamente come le velocità agli inizi A, B, C; cioè come AS^(3/2), BS^(3/2), CS^(3/2). E il tempo totale in cui il corpo giungerà al centro starà al tempo della prima rivoluzione come la somma di tutte le continuamente proporzionali AS^(3/2), BS^(3/2), CS^(3/2), che procedono all’infinito, sta al primo termine AS^(3/2); cioè come quel primo termine AS^(3/2) sta alla differenza dei primi due, AS^(3/2)−BS^(3/2), ossia, con ottima approssimazione, come ⅔AS sta ad AB. Di qui quel tempo totale si trova speditamente.

**[II.S4.16]** *Cor. 8.* Da queste cose si possono anche ricavare, all’incirca, i moti dei corpi nei mezzi la cui densità o è uniforme o segue qualsiasi altra legge assegnata. Con centro S e con intervalli continuamente proporzionali SA, SB, SC, ecc. descrivi quanti cerchi vuoi, e stabilisci che il numero [il senso richiede: il tempo; § A.9] delle rivoluzioni fra i perimetri di due qualsiasi di questi cerchi, nel mezzo di cui abbiamo trattato, stia al tempo delle rivoluzioni fra gli stessi cerchi nel mezzo proposto come la densità media del mezzo proposto fra questi cerchi sta, con ottima approssimazione, alla densità media fra gli stessi cerchi del mezzo di cui abbiamo trattato; ma anche che nello stesso rapporto stia la secante dell’angolo sotto cui la spirale prima determinata, nel mezzo di cui abbiamo trattato, taglia il raggio AS, alla secante dell’angolo sotto cui la nuova spirale taglia lo stesso raggio nel mezzo proposto; e inoltre che, come stanno le tangenti degli stessi angoli, così stiano, con ottima approssimazione, i numeri di tutte le rivoluzioni fra gli stessi due cerchi. Se si fa questo dappertutto fra ogni coppia di cerchi, il moto proseguirà attraverso tutti i cerchi. E in questo modo possiamo immaginare senza difficoltà in quali modi e in quali tempi i corpi dovranno girare in un mezzo regolare qualsiasi.

**[II.S4.17]** *Cor. 9.* E, sebbene i moti eccentrici si compiano in spirali che si avvicinano alla forma di ovali, tuttavia, concependo che le singole rivoluzioni di quelle spirali distino l’una dall’altra degli stessi intervalli e si avvicinino al centro per gli stessi gradi della spirale descritta sopra, capiremo anche come si compiano i moti dei corpi in spirali di questo genere.

### Proposizione XVI. Teorema XIII (la stessa spirale, con forza centripeta inversamente come una potenza qualsiasi della distanza)

**[II.S4.18]** **Se la densità del mezzo nei singoli luoghi è inversamente come la distanza dei luoghi da un centro immobile, e la forza centripeta è inversamente come una potenza qualsiasi della stessa distanza, dico che il corpo può girare in una spirale che interseca sotto un angolo dato tutti i raggi condotti da quel centro.**

**[II.S4.19]** Si dimostra con lo stesso metodo della proposizione precedente. Infatti, se la forza centripeta in P è inversamente come una potenza qualsiasi SPⁿ⁺¹ della distanza SP, il cui indice è n+1, si ricaverà come sopra che il tempo in cui il corpo descrive un arco qualsiasi PQ sarà come PQ×SP^(½n); e la resistenza in P come Rr/(PQ²×SPⁿ), ossia come (1−½n)×VQ/(PQ×SPⁿ×SQ), e quindi come (1−½n)×OS/(OP×SPⁿ⁺¹), cioè, essendo dato (1−½n)×OS/OP, inversamente come SPⁿ⁺¹. E perciò, poiché la velocità è inversamente come SP^(½n), la densità in P sarà inversamente come SP.

**[II.S4.20]** *Cor. 1.* La resistenza sta alla forza centripeta come (1−½n)×OS sta a OP.

**[II.S4.21]** *Cor. 2.* Se la forza centripeta è inversamente come SP³, sarà 1−½n = 0; e perciò la resistenza e la densità del mezzo saranno nulle, come nella Prop. IX del Libro I.

**[II.S4.22]** *Cor. 3.* Se la forza centripeta è inversamente come una potenza del raggio SP il cui indice è maggiore del numero 3, la resistenza positiva si cambierà in negativa.

**[II.S4.23]** *Scolio.* Del resto, questa proposizione e le precedenti, che riguardano mezzi di densità disuguale, vanno intese del moto di corpi tanto piccoli che non sia da prendere in considerazione la maggiore densità del mezzo da una parte del corpo rispetto all’altra. Suppongo anche che la resistenza, a parità di altre condizioni, sia proporzionale alla densità. Di qui, nei mezzi la cui forza di resistere non è come la densità, la densità deve essere aumentata o diminuita fino al punto che si tolga l’eccesso della resistenza o se ne supplisca il difetto.

### Proposizione XVII. Problema IV (dalla spirale e dalla legge della velocità alla forza e alla resistenza)

**[II.S4.24]** **Trovare sia la forza centripeta sia la resistenza del mezzo per cui un corpo può ruotare in una spirale data, con una legge data della velocità.**

**[II.S4.25]** Sia PQR quella spirale. Dalla velocità con cui il corpo percorre l’arco piccolissimo PQ sarà dato il tempo, e dall’altezza TQ, che è come la forza centripeta e il quadrato del tempo, sarà data la forza. Poi dalla differenza RSr delle aree PSQ e QSR, compiute in particelle uguali di tempo, sarà dato il ritardo del corpo, e dal ritardo si troveranno la resistenza e la densità del mezzo.

### Proposizione XVIII. Problema V (dalla legge della forza alla densità del mezzo)

**[II.S4.26]** **Data la legge della forza centripeta, trovare la densità del mezzo nei singoli luoghi per cui il corpo descriverà una spirale data.**

**[II.S4.27]** Dalla forza centripeta si deve trovare la velocità nei singoli luoghi; poi dal ritardo della velocità si deve ricavare la densità del mezzo, come nella proposizione precedente.

**[II.S4.28]** Il metodo di trattare questi problemi, del resto, l’ho mostrato nella Proposizione X e nel Lemma II di questo Libro; e non voglio trattenere più a lungo il lettore in ricerche così intricate. Ora si devono aggiungere alcune cose sulle forze dei corpi nell’avanzare, e sulla densità e sulla resistenza dei mezzi nei quali si compiono i moti finora esposti e quelli affini.

**Fine della Sezione IV. Nel testo originale segue la Sezione V, *De densitate & compressione fluidorum, deque hydrostatica*.**

---

## Apparato

### A.0 Estensioni del glossario

I termini seguenti non comparivano nel glossario comune né nel glossario del Libro II. Ognuno è reso in modo costante in tutto il fascicolo.

| Latino | Italiano | Motivazione |
|---|---|---|
| *resistitur* (passivo impersonale: *corpori resistitur*, *quibus resistitur*) | «si resiste a» («a un corpo si resiste», «ai quali si resiste») | Conserva la costruzione impersonale del latino e il verbo dello stesso tema di *resistentia*. Motte: «be resisted». Da armonizzare con i Fascicoli 13–14. |
| *medium similare* | «mezzo omogeneo» | Termine fissato dal coordinatore; prima occorrenza in II.S3.01. *Similaris* è il mezzo «simile in ogni sua parte», cioè di densità uguale dappertutto (nota N1). Motte: «a similar medium». |
| *asymptoti rectangulæ* | «asintoti ortogonali» | Asintoti perpendicolari fra loro (II.S3.02, II.S3.22). |
| *hyperbola rectangula* | «iperbole rettangola» | L’iperbole con asintoti ortogonali, oggi «equilatera» (II.S3.17). Si conserva il termine dell’epoca. |
| *areola* | «areola» | Diminutivo di *area* (II.S3.03), parallelo a *lineola* «lineetta». |
| *particula* (*temporis*, *spatii*) | «particella» (di tempo, di spazio) | Come nel Libro I. |
| *incrementum*, *decrementum* | «incremento», «decremento» | |
| *exponere*, *exponi per* | «rappresentare», «essere rappresentato da» | Come nel Fascicolo 3 (Cor. II); Motte «expound», «express». |
| *reciproca* (sostantivo: *cujus reciproca GD*) | «inversa» | La grandezza inversa (1/x); coerente con *reciproce* «inversamente». |
| *progressio arithmetica* | «progressione aritmetica» | Parallelo a *progressio geometrica* (glossario del Libro II). |
| *analogus* (*decrementa analoga*) | «analogo» | «Proporzionale nello stesso modo» (II.S3.03, II.S3.08). |
| *linea infinita* | «retta illimitata» | II.S3.13: *infinita BAP* è la retta prolungata senza limite; Motte «indefinite line». |
| *semidiameter*; *quadrans*; *sector* | «semidiametro»; «quadrante»; «settore» | |
| *ad modum temporis futuri* | «alla maniera del tempo futuro» | II.S3.14: l’area residua EDT diminuisce come diminuisce il tempo che resta fino alla fine della salita. Resa letterale, spiegata qui. |
| *pro more sectoris & trianguli* | «come fanno il settore e il triangolo» | II.S3.19. |
| *divisim* | «separando» | Operazione delle proporzioni del libro V degli *Elementi*. Qui (II.S3.16, II.S3.18) da GD² : BP² = GT² : BD² si passa a (GD² − GT²) : (BP² − BD²), cioè si sottraggono antecedenti e conseguenti. Il Libro I non è uniforme («separando», «per separazione», «dividendo», «per divisione» nei Fascicoli 6–12). Armonizzazione del coordinatore per il Libro II: «separando», come nei Fascicoli 13, 14 e 17 (la proposta originaria di questo fascicolo era «dividendo»). |
| *ex æquo perturbate* | «per uguaglianza perturbata» | II.S4.03; come nei fascicoli del Libro I. Motte lascia «ex æquo perturbatè». |
| *altitudo maxima*; *altitudo TQ* | «altezza massima»; «altezza TQ» | II.S3.22; II.S4.25 (la saetta TQ intesa come caduta verso il centro). |
| *tenacitas*; *frictio* | «tenacità»; «attrito» | Scolio della Sez. III. Motte: «tenacity», «attrition». |
| *speculatio* | «indagine» | II.S3.30. |
| *spiralis* | «spirale» | Come nel Libro I (Prop. IX). |
| *gyrari*; *revolvi*; *revolutio* | «girare»; «ruotare»; «rivoluzione» | Come nel Fascicolo 5. |
| *velocitates descriptrices* | «le velocità con cui sono descritti» | II.S4.07: le velocità che «descrivono» gli archi. |
| *vis resistentiæ*; *vis resistendi* | «forza di resistenza»; «forza di resistere» | II.S4.05, II.S4.11; II.S4.23. |
| *defectus ab arcubus* | «difetti rispetto agli archi» | II.S4.05: quanto manca all’arco descritto nel mezzo resistente rispetto a quello del vuoto. |
| *tangens*, *secans* (*anguli*) | «tangente», «secante» | Funzioni trigonometriche come linee (II.S4.14). |
| *dignitas*; *index* | «potenza»; «indice» | Come nel Libro I. |
| *resistentia affirmativa / negativa* | «resistenza positiva / negativa» | II.S4.22. «Affermativa» sarebbe un latinismo opaco. |
| *densitas mediocris* | «densità media» | Come *mediocris* nel Libro I. |
| *præter propter* | «all’incirca» | II.S4.16. |
| *medium regulare* | «mezzo regolare» | II.S4.16: mezzo la cui densità segue una legge. |
| *retardatio* | «ritardo» | II.S4.25, II.S4.27. |
| *ad progrediendum* | «nell’avanzare» | II.S4.28. |

*Vis insita* compare due volte (II.S3.01, II.S3.31): «forza insita». *Conjunctim* compare in II.S3.08 in un senso particolare: «come una quantità data e una quantità decrescente considerate congiuntamente», dove il contesto mostra che il decremento è come la **somma** delle due (nota N3); la resa del glossario è conservata.

### A.1 Proposizione XI

**Latino:** *Si corpori resistitur partim in ratione velocitatis, partim in velocitatis ratione duplicata, & idem sola vi insita in medio similari movetur: sumantur autem tempora in progressione arithmetica; quantitates velocitatibus reciproce proportionales, data quadam quantitate auctæ, erunt in progressione geometrica.*

**Inglese:** “If a body be resisted partly in the ratio and partly in the duplicate ratio of its velocity, and moves in a similar medium by its innate force only; and the times be taken in arithmetical progression; then quantities reciprocally proportional to the velocities, increased by a certain given quantity, will be in geometrical progression.”

**Scelte.**

- *vi insita* → «per la forza insita» (glossario); Motte «by its innate force».
- *Et fi tempus exponatur*: *fi* è **refuso probabile della trascrizione** per *si* (s lunga letta come f).
- *velocitas exponi potest per longitudinem DF, cujus reciproca GD*: la trascrizione e Motte concordano su **DF**. DF è dunque una lunghezza (verosimilmente segnata in figura) la cui inversa è GD, cioè DF ∝ 1/GD; il Cor. 1 dice lo stesso con 1/GD. Non è un refuso.
- Frazioni: «1GD» = 1/GD; «DdGDq» = Dd/GD²; «CDGDq» = CD/GD²; «CG+GDGDq» = (CG+GD)/GD²; «1GD+CGGDq» = 1/GD + CG/GD²; «1GDq» = 1/GD². Lette dal ragionamento (la derivata di 1/GD rispetto a GD è −1/GD²: Lemma II del Libro II).
- *per hujus lem. II* → «per il Lemma II di questo Libro». Motte «(by Lem. II, Book II)».
- *ob analogum decrementum* → «per l’analogia dei decrementi».

### A.2 Proposizione XII

**Latino:** *Iisdem positis, dico quod si spatia descripta sumantur in progressione arithmetica, velocitates data quadam quantitate auctæ erunt in progressione geometrica.*

**Inglese:** “The same things being supposed, I say, that if the spaces described are taken in arithmetical progression, the velocities augmented by a certain given quantity will be in geometrical progression.”

**Scelte.**

- *tempore sibi reciproce proportionali*: il tempo in cui si descrive la particella data di spazio è inversamente come la velocità; *sibi* si riferisce a *velocitatis*: «nel tempo a essa inversamente proporzionale».
- *ut quantitas data & quantitas decrescens conjunctim*: vedi § A.0 e nota N3.
- **Errore di Motte nel Cor. 2:** il latino ha *si utcunque assumatur punctum* **R**, *invenietur punctum G*; Motte scrive «if the point **G** be assumed any how, the point G will be found». Il punto preso a piacere è R.
- Cor. 3: *per prop. XI.* → «per la Prop. XI».

### A.3 Proposizione XIII

**Latino:** *Posito quod corpus ab uniformi gravitate deorsum attractum recta ascendit vel descendit; & quod eidem resistitur partim in ratione velocitatis, partim in ejusdem ratione duplicata: dico quod, si circuli & hyperbolæ diametris parallelæ rectæ per conjugatarum diametrorum terminos ducantur, & velocitates sint ut segmenta quædam parallelarum ducta; tempora erunt ut arearum sectores, rectis a centro ad segmentorum terminos ductis abscissi: & contra.*

**Inglese:** “Supposing that a body attracted downwards by an uniform gravity ascends or descends in a right line; and that the same is resisted partly in the ratio of its velocity, and partly in the duplicate ratio thereof: I say, that, if right lines parallel to the diameters of a circle and an hyperbola, be drawn through the ends of the conjugate diameters, and the velocities be as some segments of those parallels drawn from a given point, the times will be as the sectors of the areas cut off by right lines drawn from the centre to the ends of the segments; and the contrary.”

**Scelte.**

- *recta ascendit*: *recta* avverbio, «in linea retta».
- *segmenta quædam parallelarum ducta* → «certi segmenti di queste parallele». **Aggiunta di Motte:** «drawn from a given point», che nel latino dell’enunciato non c’è (il punto dato A compare solo nella costruzione).
- **Caso 1, lettera errata in Motte:** il latino ha *per semidiametri* **DB** *terminum B*; Motte «through the end B of the semi-diameter **DF**». B è estremo di DB, non di DF.
- **Caso 1, *resistentia tota in ut AP quad.+2BAP*:** il *in* non regge nulla. Motte ha «let the whole resistance be as AP² + 2BAP» e poi «the gravity shall be to the resistance **in P**». È probabile che la stampa abbia *in P* e che la *P* sia caduta nella trascrizione (o che la stampa stessa sia difettosa). La traduzione integra «in [P]». Da controllare (§ A.13).
- *2BAP* = 2BA×AP: nota N2.
- *per prop. 12. lib. 2. elem.* → «per la Prop. 12 del Libro II degli *Elementi*» (di Euclide): nel triangolo ottusangolo DAP, con B piede della perpendicolare da D sul prolungamento di PA, DP² = DA² + AP² + 2BA×AP. Verificato (nota N4).
- *summa virium gravitatis DAq & resistentiæ APq+2BAP* → «la somma delle forze, la gravità DA² e la resistenza AP²+2BAP».
- Caso 2: *si ad DF demittatur perpendiculum GT*: G è il piede su DF della perpendicolare da T. Caso 3: GT è la perpendicolare da T su DB (G sulla retta DB). Le due relazioni GT² = GD² − DF² e GT² = GD² − BD² sono le equazioni delle due iperboli (nota N4).
- Caso 3: *hyperbola rectangula* → «iperbole rettangola» (§ A.0). **Aggiunta di Motte:** «the **whole** time of descent» per *tempus descensus*.
- Cor.: *similiter subtendes angulun ADT*: **refusi probabili della trascrizione** per *subtendens angulum*.
- Scolio: *Demonstrati etiam posset*: **refuso probabile della trascrizione** per *Demonstrari*.

### A.4 Proposizione XIV

**Latino:** *Iisdem positis, dico quod spatium ascensu vel descensu descriptum, est ut differentia areæ per quam tempus exponitur, & areæ cujusdam alterius quæ augetur vel diminuitur in progressione arithmetica; si vires ex resistentia & gravitate compositæ sumantur in progressione geometrica.*

**Inglese:** “The same things being supposed, I say, that the space described in the ascent or descent is as the difference of the area by which the time is expressed, and of some other area which is augmented or diminished in an arithmetical progression; if the forces compounded of the resistance and the gravity be taken in a geometrical progression.”

**Scelte.**

- *in fig. tribus ultimis* → «nelle tre ultime figure» (le tre figure dei Casi della Prop. XIII); Motte «in these three figures».
- *4BAC* = 4BA×AC.
- Frazioni (confermate dalle formule SVG 543–554 di Motte, salvo l’esponente di 547: § A.14): AK = (AP²+2BAP)/Z; KL = (2APQ+2BA×PQ)/Z = 2BPQ/Z; KLON = 2BPQ×LO/Z = BPQ×BD³/(2Z×CK×AB); AC = (AB²±BD²)/Z o (BD²−AB²)/Z; poi BP×BD×m/AB, AP×BD×m/AB, BD×m/AB. Tutte ricalcolate (nota N6).
- **Errore di Motte:** «AK is as the resistance, that is, as AP² **×** 2BAP» per *APq***+***2BAP*.
- *Auferatur æreae DET momentum DTV*: *æreae* è **refuso probabile della trascrizione** per *areæ*. Il senso è: dal momento KLON appena trovato si tolga il momento DTV dell’area DET. Motte scrive «**From the area DET** subduct its moment DTV», che fraintende la costruzione: il resto AP×BD×m/AB è KLON − DTV, non DET − DTV.
- **Cor., *applicando aream DET ad lineam ED*:** la trascrizione ha **ED**, Motte **BD**. Il calcolo che segue richiede **BD**: Newton scrive che DA²×BD×M/DE² è come «DA²/DE² per DET», il che vale solo se BD×M = DET, cioè M = DET/BD; e il momento di M è m perché il momento di DET è DTV = BD×m. Nel Caso 1 (cerchio) DE = DB e la differenza non conta; nei Casi 2–3 (iperbole) sì. La traduzione rende il latino («ED») e segnala tra parentesi quadre che il calcolo richiede BD. Da controllare sulla stampa (§ A.13).
- Cor.: «BD×V2AB» = BD×V²/AB; «DAq×BD×M2DEq×AB» = DA²×BD×M²/(DE²×AB); «DAq×BD×2M×mDEq×AB» = DA²×BD×2M×m/(DE²×AB); «DAqDEq in DET» = (DA²/DE²)×DET. La lettura «V²» (e non «V/2») è imposta dalla frase *spatium … est in duplicata ratione temporis, sive ut V2* e dal momento 2M×m (nota N6).
- *applicando … ad* → «dividendo … per» (glossario consolidato).

### A.5 Scolio della Sezione III

- *partim ex frictione* → «in parte dall’attrito»; Motte «attrition».
- *diximus* → «abbiamo detto»; Motte «as I said».
- *vi insita*: Motte lascia il latino «vis insita».
- *Sed sufficit aditum patefecisse* → «Ma basta aver aperto l’accesso»; *viam aperui* → «ho aperto la via».
- *in propositionibus VIII. & IX.* e *XIII. & XIV.*: rimandi interni al Libro II (§ A.15).

### A.6 Lemma III

**Latino:** *Sit PQR spiralis quæ secet radios omnes SP, SQ, SR, &c. in æqualibus angulis. Agatur recta PT quæ tangat eandem in puncto quovis P, secetque radium SQ in T; & ad spiralem erectis perpendiculis PO, QO concurrentibus in O, jungatur SO. Dico quod si puncta P & Q accedant ad invicem & coeant, angulus PSO evadet rectus, & ultima ratio rectanguli TQ×2PS ad PQquad. erit ratio æqualitatis.*

**Inglese:** “Let PQR be a spiral cutting all the radii SP, SQ, SR, &c., in equal angles. Draw the right line PT touching the spiral in any point P, and cutting the radius SQ in T; draw PO, QO perpendicular to the spiral, and meeting in O, and join SO. I say, that if the points P and Q approach and coincide, the angle PSO will become a right angle, and the ultimate ratio of the rectangle TQ × 2PS to PQ² will be the ratio of equality.”

**Scelte.**

- *coeant* → «si riuniscano» (glossario); *in loco coitus PQ* → «nel luogo PQ della loro riunione».
- *angulus OSP in semicirculo rectus* → «l’angolo OSP, nel semicerchio, sarà retto» (Euclide III.31, non citato).
- *ex æquo perturbate* → «per uguaglianza perturbata». Motte stampa «to TQ to PQ», con un «to» superfluo (refuso dell’edizione 1846).
- Motte scrive «the points OSP» per *puncta O, S, P*: solo grafia.
- Il primo C.V.D. chiude la prima parte (angolo retto), il secondo la seconda (rapporto ultimo). Verifica numerica in N8.

### A.7 Proposizione XV

**Latino:** *Si medii densitas in locis singulis sit reciproce ut distantia locorum a centro immobili, sitque vis centripeta in duplicata ratione densitatis: dico quod corpus gyrari potest in spirali, quæ radios omnes a centro illo ductos intersecat in angulo dato.*

**Inglese:** “If the density of a medium in each place thereof be reciprocally as the distance of the places from an immovable centre, and the centripetal force be in the duplicate ratio of the density; I say, that a body may revolve in a spiral which cuts all the radii drawn from that centre in a given angle.”

**Scelte.**

- *si areæ PSQ æqualis capitaur area QSr*: *capitaur* è **refuso probabile della trascrizione** per *capiatur*.
- **Radicali perduti.** La trascrizione scrive «PQ×SP», «PQPQ×SP», «1SP», «SP×SQ», «SP−SP×SQ»; il ragionamento (*tempus … in ratione duplicata*; *in subduplicata ratione ipsius SP reciproce*) impone PQ×√SP, PQ/(PQ×√SP), 1/√SP, √(SP×SQ), SP−√(SP×SQ). Il segno di radice era probabilmente stampato come vincolo sopra la grandezza e si è perso nell’estrazione. Le formule di Motte (SVG 567–571, 573) hanno la radice e confermano la lettura. La traduzione usa √ (§ A.12).
- Lo stesso «1SP» compare più avanti con valore 1/SP (*ratio 1SP* come rapporto duplicato della velocità; *densitas … ut 1SP*): lì non c’è radice. La lettura è decisa dal contesto in ciascun luogo.
- *per lem. X. lib. I.* → «per il Lemma X del Libro I»: § A.15.
- *per lemma novissimum* → «per l’ultimo lemma», cioè il Lemma III appena dimostrato.
- *Sumantur proportionalium consequentium differentiæ* → «Si prendano le differenze dei conseguenti proporzionali»: da PQ:QR = SQ:√(SP×SQ) e PQ:Qr = SQ:SP si ricava PQ:(Qr−QR) = SQ:(SP−√(SP×SQ)), con Rr = Qr − QR.
- *in ratione densitatis medii in P & ratione duplicata velocitatis conjunctim* → «nel rapporto della densità del mezzo in P e nel rapporto duplicato della velocità considerati congiuntamente».

### A.8 Proposizione XV, Corollari 1–6

- Cor. 3: «14VQ×PQSQ & 12PQqSP» = ¼VQ×PQ/SQ e ½PQ²/SP.
- Cor. 4: *ad numerum bianrium*: **refuso probabile della trascrizione** per *binarium*. *in casu parabolæ (theor. X. lib. I.)* → «nel caso della parabola (Teorema X del Libro I [Prop. XXXIV])»: § A.15.
- Cor. 6: *pergendo in spriali*: **refuso probabile della trascrizione** per *spirali*. «PSOS» = PS/OS; «OPOS» = OP/OS.
- *Corol 2.* senza punto dopo *Corol*: punteggiatura della trascrizione.

### A.9 Proposizione XV, Corollari 7–9

- Cor. 7: «AS32» = AS^(3/2) (esponente appiattito); «23AS» = ⅔AS. *expedite* → «speditamente».
- **Cor. 8, *statue numerum revolutionum … esse ad tempus revolutionum*.** Il latino della trascrizione mette a rapporto un **numero** di rivoluzioni (nel primo mezzo) con un **tempo** di rivoluzioni (nel mezzo proposto), e uguaglia il rapporto a quello inverso delle densità medie. Il rapporto fra un numero e un tempo non ha senso in questa proporzione; per il Cor. 6, poi, è il **tempo** delle rivoluzioni che è inversamente come la densità (e come la secante, che compare subito dopo nella stessa frase). Motte traduce «suppose the **time** of the revolutions … to be to the time of the revolutions». La lettura richiesta dal senso è dunque *tempus*. La traduzione rende il latino («il numero») e segnala tra parentesi quadre che il senso richiede «il tempo». Da controllare sulla stampa: può essere un refuso della trascrizione o un *lapsus* dell’edizione del 1726 (§ A.13).
- Cor. 8: *in medio de quo egimus* → «nel mezzo di cui abbiamo trattato»; *spiralis præfinita* → «la spirale prima determinata»; *passim inter circulos binos* → «dappertutto fra ogni coppia di cerchi».
- Cor. 9: *iisdemque gradibus* → «per gli stessi gradi», cioè con la stessa gradualità dell’avvicinamento al centro.

### A.10 Proposizione XVI

**Latino:** *Si medii densitas in locis singulis sit reciproce ut distantia locorum a centro immobili, sitque vis centripeta reciproce ut dignitas quælibet ejusdem distantiæ: dico quod corpus gyrari potest in spirali quæ radios omnes a centro illo ductos intersecat in angulo dato.*

**Inglese:** “If the density of the medium in each of the places be reciprocally as the distance of the places from the immoveable centre, and the centripetal force be reciprocally as any power of the same distance, I say, that the body may revolve in a spiral intersecting all the radii drawn from that centre in a given angle.”

**Scelte.**

- *si vis centripeta in P sit reciproce ut distantiæ SP, dignitas quælibet SPn+1*: la virgola dopo *distantiæ SP* è da intendere come apposizione: «come una potenza qualsiasi SPⁿ⁺¹ della distanza SP».
- Frazioni ed esponenti: «SP12n» = SP^(½n); «RrPQq×SPn» = Rr/(PQ²×SPⁿ); «1−12n¯×VQPQ×SPn×SQ» = (1−½n)×VQ/(PQ×SPⁿ×SQ); «1−12n¯×OSOP×SPn+1» = (1−½n)×OS/(OP×SPⁿ⁺¹). Il segno «¯» è il resto del vincolo che raccoglie 1−½n come fattore.
- Cor. 2: *erit 1−12n=o*: la «o» è lo zero; «come nella Prop. IX del Libro I»: § A.15.
- Cor. 3: *resistentia affirmativa in negativam mutabitur* → «la resistenza positiva si cambierà in negativa».
- Motte, nella dimostrazione: «that is, [SVG 596] is a given quantity), reciprocally as …»: la parentesi si apre dentro l’immagine SVG 596, che contiene «(because (1−½n)×OS/OP»; il testo è completo.
- Motte (SVG 592) scrive PQ×**PS**^(½n) per PQ×SP^(½n): stessa retta, lettere in ordine inverso.
- Scolio: *non consideranda veniat* → «non sia da prendere in considerazione»; *cæteris paribus* → «a parità di altre condizioni».

### A.11 Proposizioni XVII–XVIII e capoverso finale

**Latino (XVII):** *Invenire & vim centripetam & medii resistentiam, qua corpus in data spirali, data velocitatis lege, revolvi potest.*

**Inglese (XVII):** “To find the centripetal force and the resisting force of the medium, by which a body, the law of the velocity being given, shall revolve in a given spiral.”

**Latino (XVIII):** *Data lege vis centripetæ, invenire medii densitatem in locis singulis, qua corpus datam spiralem describet.*

**Inglese (XVIII):** “The law of centripetal force being given, to find the density of the medium in each of the places thereof, by which a body may describe a given spiral.”

**Scelte.**

- XVII: *medii resistentiam* → «la resistenza del mezzo»; Motte «the resisting **force** of the medium» (aggiunta).
- XVII: *arearum … PSQ & QSR, differentia RSr*: RSr è la differenza fra l’area QSr (uguale a PSQ) e l’area QSR, come nella Prop. XV.
- Finale: *diutius detenere*: **refuso probabile della trascrizione** per *detinere*. *in hujus propositione decima, & lemmate secundo* → «nella Proposizione X e nel Lemma II di questo Libro».
- *de viribus corporum ad progrediendum* → «sulle forze dei corpi nell’avanzare»; Motte «the forces of progressive bodies».

### A.12 Refusi e anomalie della trascrizione

| Luogo | Trascrizione | Lettura | Tipo |
|---|---|---|---|
| II.S3.02 | *Et fi tempus* | *Et si tempus* | refuso probabile (s lunga) |
| II.S3.03 | «1GD», «DdGDq», «CG+GDGDq», «1GD+CGGDq», «1GDq» | 1/GD, Dd/GD², (CG+GD)/GD², 1/GD + CG/GD², 1/GD² | frazioni appiattite |
| II.S3.13 | *resistentia tota in ut* | *in P ut* (?) | lettera caduta probabile (Motte «in P» poco dopo) |
| II.S3.19 | *subtendes angulun* | *subtendens angulum* | refusi probabili |
| II.S3.20 | *Demonstrati* | *Demonstrari* | refuso probabile |
| II.S3.22 | *si cor ‹271› pus* | *si corpus* | parola spezzata dal marcatore di pagina |
| II.S3.23–27 | «APq+2BAPZ», «2BPQZ», «BPQ×BD cub.2Z×CK×AB», «BP×BD×mAB» ecc. | (AP²+2BAP)/Z, 2BPQ/Z, BPQ×BD³/(2Z×CK×AB), BP×BD×m/AB | frazioni appiattite |
| II.S3.24 | riga spezzata dopo «APq+2BAP+ABq+BDq» | — | a capo spurio |
| II.S3.27 | *æreae DET* | *areæ DET* | refuso probabile |
| II.S3.27 | *crescen ‹273› tia* | *crescentia* | parola spezzata |
| II.S3.28 | *ad lineam ED* | *ad lineam BD* (?) | lettera dubbia: il calcolo richiede BD (§ A.4) |
| II.S3.28–29 | «BD×V2AB», «DAq×BD×M2DEq×AB», «12BD×AP», «DAqDEq» | BD×V²/AB, DA²×BD×M²/(DE²×AB), ½BD×AP, DA²/DE² | frazioni ed esponenti appiattiti |
| II.S4.01 | *PQquad.* | PQ² | spaziatura |
| II.S4.05 | *capitaur* | *capiatur* | refuso probabile |
| II.S4.05 | «12Rr» | ½Rr | frazione appiattita |
| II.S4.06–07 | «PQ×SP», «PQPQ×SP», «1SP», «SP×SQ», «SP−SP×SQ» | PQ×√SP, PQ/(PQ×√SP), 1/√SP, √(SP×SQ), SP−√(SP×SQ) | **radicali perduti** |
| II.S4.08 | «RrPQq×SP», «12VQPQ×SP×SQ», «12OSOP×SPq», «OSOP×SP», «1SP» | Rr/(PQ²×SP), ½VQ/(PQ×SP×SQ), ½OS/(OP×SP²), OS/(OP×SP), 1/SP | frazioni appiattite |
| II.S4.08 | riga spezzata dopo «SP & SQ coincidunt,» | — | a capo spurio |
| II.S4.10 | *Corol 2.* | *Corol. 2.* | punteggiatura |
| II.S4.12 | *bianrium* | *binarium* | refuso probabile |
| II.S4.14 | *spriali* | *spirali* | refuso probabile |
| II.S4.15 | «AS32», «23AS» | AS^(3/2), ⅔AS | esponenti e frazioni appiattiti |
| II.S4.16 | *statue numerum revolutionum … esse ad tempus* | *tempus revolutionum* (?) | lettura dubbia (§ A.9) |
| II.S4.19 | «SPn+1», «SP12n», «1−12n¯» | SPⁿ⁺¹, SP^(½n), (1−½n) | esponenti e vincolo appiattiti |
| II.S4.21 | *1−12n=o* | 1−½n = 0 | «o» per zero |
| II.S4.28 | *detenere* | *detinere* | refuso probabile |

La traduzione segue il senso; la Parte B riporta il latino esatto della trascrizione.

### A.13 Punti da controllare sulla stampa ECCO

| Pagina 1726 | Lettura della trascrizione | Lettura attesa | Motivo |
|---|---|---|---|
| 265 | *Et fi tempus exponatur* | *Et si tempus* | s lunga; *fi* non dà senso |
| 267–268 | *sit resistentia tota in ut AP quad.+2BAP* | *tota in P ut* oppure *tota ut* | *in* senza complemento; Motte ha «in P» nella frase seguente |
| 269 | *similiter subtendes angulun ADT* | *subtendens angulum* | doppio refuso |
| 269 | *Demonstrati etiam posset* | *Demonstrari* | infinito passivo richiesto |
| 270 | *quæ sit ad DB ut DBq ad 4BAC* | conferma di *4BAC* (= 4BA×AC) | formula decisiva per l’iperbole bN; verificata numericamente (N6) |
| 272 | *Auferatur æreae DET* | *areæ* | grafia |
| 273 | *applicando aream DET ad lineam ED* | *ad lineam BD* | il calcolo richiede M = DET/BD; Motte «BD» |
| 273 | «BD×V2AB», «DAq×BD×M2DEq×AB» | BD×V²/AB; DA²×BD×M²/(DE²×AB) | posizione degli esponenti e dei denominatori |
| 276 | *capitaur area QSr* | *capiatur* | grafia |
| 276 | «PQ×SP», «PQPQ×SP», «1SP», «SP×SQ» | con radice su SP e su SP×SQ | i radicali mancano nella trascrizione; il senso li richiede |
| 277 | *numerum bianrium* | *binarium* | grafia |
| 278 | *pergendo in spriali* | *spirali* | grafia |
| 279 | *statue numerum revolutionum … esse ad tempus revolutionum* | *tempus revolutionum … ad tempus* | rapporto numero/tempo senza senso; Motte «time» |
| 280 | «1−12n¯×VQPQ×SPn×SQ» | (1−½n)×VQ/(PQ×SPⁿ×SQ) | estensione del vincolo |
| 282 | *diutius detenere* | *detinere* | grafia |

### A.14 Formule di Motte (SVG 536–599)

Tutte le 64 immagini SVG di Motte per queste due sezioni sono state rese con `rsvg-convert` e lette. Corrispondono alle letture della trascrizione latina dichiarate in § A.12, comprese quelle decisive: i radicali della Prop. XV (SVG 567–571, 573: PQ√SP, PQ/(PQ√SP), 1/√SP, √(SP×SQ), SP−√(SP×SQ)), che confermano la lettura con radice; BD×V²/AB (556, 563–564) e DA²×BD×M²/(DE²×AB) (557), che confermano «V²» e «M²»; il vincolo su 1−½n (594–596, 598). Divergenze dal latino:

| SVG | Luogo | Motte 1846 | Latino (e calcolo) | Esito |
|---|---|---|---|---|
| 547 | Prop. XIV, momento KLON | BPQ×**BD²**/(2Z×CK×AB) | «BPQ×BD cub.2Z×CK×AB» = BPQ×BD³/(2Z×CK×AB) | **errore di Motte 1846**: il calcolo (LO = DB³/(4AB×CK)) richiede BD³, e Motte stesso scrive poi «PQ × BD3» |
| 559 | Prop. XIV, Cor. | AP×BD×**×**m/AB | AP×BD×m/AB | doppio segno «×»: refuso tipografico |
| 582 | Prop. XV, Cor. 3 | **½**VQ×PQ/SQ | «14VQ×PQSQ» = ¼VQ×PQ/SQ | **errore di Motte 1846**: ½Rr = ¼VQ×PQ/SQ, perché Rr = PQ×½VQ/SQ; con ½ il rapporto con ½PQ²/SP darebbe VQ : PQ, non ½VQ : PQ come conclude il testo |
| 592 | Prop. XVI | PQ×**PS**^(½n) | PQ×SP^(½n) | lettere in ordine inverso, stesso segmento |
| 555 | Prop. XIV | «(because of the given quantity BD×m/AB)» | *ob datum BD×mAB* | l’inciso intero è nell’immagine; corrisponde |
| 596 | Prop. XVI | «(because (1−½n)×OS/OP» | *ob datum 1−½n×OSOP* | la parentesi si apre nell’immagine; corrisponde |

Per gli errori di 547 e 582 non ho visto Motte 1729: non so se risalgano alla prima edizione inglese o all’edizione del 1846. **SVG da controllare:** nessuno (tutti visti).

### A.15 Rimandi verificati

**Al Libro I (3):**

| Luogo | Latino | Resa | Verifica |
|---|---|---|---|
| II.S4.06 | *per lem. X. lib. I.* | «per il Lemma X del Libro I» | Fascicolo 4, S1.27–S1.31. L’enunciato del Lemma X dà gli spazi iniziali in rapporto duplicato dei tempi; il rapporto composto **della forza e del quadrato del tempo** usato qui è il **Cor. 3** (S1.31). Il rimando regge, ma propriamente tramite il Cor. 3. |
| II.S4.12 | *in casu parabolæ (theor. X. lib. I.)* | «(Teorema X del Libro I [Prop. XXXIV])» | Fascicolo 8, S7.09–S7.10: la Prop. XXXIV è il Teorema X; la velocità di caduta in C è uguale a quella del moto circolare uniforme alla metà della distanza BC. Per la forza come 1/r² la velocità circolare alla distanza r/2 è √2 volte quella alla distanza r; la velocità nella spirale (Cor. 1) è quella circolare alla distanza r: rapporto 1 : √2, *in subduplicata ratione unitatis ad numerum binarium*. Regge (nota N10). |
| II.S4.21 | *ut in propositione nona libri primi* | «come nella Prop. IX del Libro I» | Fascicolo 5, S2.57–S2.59: nella spirale che taglia i raggi sotto un angolo dato la forza è inversamente come il cubo della distanza. Coerente con resistenza nulla per 1−½n = 0. Regge. |

**A Euclide (1):** II.S3.14, *per prop. 12. lib. 2. elem.* — *Elementi* II.12 (triangolo ottusangolo): DP² = DA² + AP² + 2BA×AP. Regge (verificato sulla figura di prova, N4).

**Interni al Libro II (controllati sul latino della Sezione II):** Lemma II (II.S3.03, II.S3.23, II.S4.28: momento della «quantità generata»; usato per i momenti di 1/GD e di AK), Prop. XI (II.S3.11), Propp. VIII e IX (II.S3.30: salita e discesa in mezzo uniforme con gravità uniforme e resistenza come il quadrato della velocità; la sostituzione della resistenza uniforme alla gravità è coerente con il loro enunciato, in cui la resistenza si somma o si sottrae alla gravità), Propp. XIII e XIV (II.S3.31), Prop. X (II.S4.28: problema della densità per una curva data). Nessun rimando risulta non pertinente.

### A.16 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| II.S3.01, II.S3.31 | *vi insita* | «innate force»; «vis insita» | termine non conforme al glossario |
| II.S3.10 | *si utcunque assumatur punctum R* | «if the point **G** be assumed any how» | **lettera errata** |
| II.S3.12 | *segmenta quædam parallelarum ducta* | «… drawn **from a given point**» | aggiunta |
| II.S3.13 | *semidiametri DB terminum B* | «the end B of the semi-diameter **DF**» | **lettera errata** |
| II.S3.13 | *resistentia tota in ut …* | «whole resistance be as …»; «to the resistance **in P**» | spostamento (Motte ha la lettura «in P») |
| II.S3.16 | *decrementum PQ* | «decrement PQ.» | punteggiatura dell’edizione 1846 |
| II.S3.17 | *tempus descensus* | «the **whole** time of descent» | aggiunta |
| II.S3.22 | *in fig. tribus ultimis* | «in these three figures» | lieve divergenza |
| II.S3.23 | *APq+2BAP* | «AP² **×** 2BAP» | **segno errato** |
| II.S3.23 | *BPQ×BD cub.…* | «BPQ × BD²…» (SVG 547) | **esponente errato** |
| II.S3.29 | *AP×BD×m/AB* | «AP × BD × × m» (SVG 559) | refuso tipografico |
| II.S3.27 | *Auferatur areæ DET momentum DTV* | «**From the area DET** subduct its moment DTV» | fraintendimento della costruzione |
| II.S3.28 | *ad lineam ED* | «to the line **BD**» | Motte ha la lettura richiesta dal calcolo |
| II.S3.30 | *frictione* | «attrition» | resa diversa |
| II.S4.11 | *¼VQ×PQ/SQ* | «½VQ × PQ/SQ» (SVG 582) | **coefficiente errato** |
| II.S4.02 | *O, S, P* | «OSP» | grafia |
| II.S4.03 | *ex æquo perturbate TQ ad PQ* | «ex æquo perturbatè, **to** TQ to PQ» | refuso dell’edizione 1846 |
| II.S4.16 | *numerum revolutionum … esse ad tempus* | «the **time** of the revolutions … to the time» | Motte ha la lettura richiesta dal senso |
| II.S4.19 | *SP12n* | «PS^(½n)» (SVG 592) | lettere in ordine inverso |
| II.S4.24 | *medii resistentiam* | «the resisting **force** of the medium» | aggiunta |
| II.S4.28 | *ad progrediendum* | «of progressive bodies» | resa libera |

Le formule di Motte stampate come immagini (SVG 536–599) sono state viste tutte; le divergenze sono nella tabella qui sopra e nel § A.14.

---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. Le verifiche numeriche sono state eseguite con uno script Python (`tmp/15/verifica.py`, conservato con i materiali di lavoro), che integra le equazioni del moto con il metodo di Runge–Kutta del quarto ordine e misura le grandezze geometriche sulla figura di prova, senza usare la tesi da verificare.

### N1. «Mezzo omogeneo» (*medium similare*)

*Similaris* è il mezzo le cui parti sono tutte simili fra loro: in pratica, di densità costante. La resa «omogeneo» è fissata dal coordinatore; Motte conserva il calco «similar medium». Nella Sezione IV, al contrario, la densità varia da luogo a luogo (*media inæqualiter densa*, II.S4.23).

### N2. La notazione 2BAP e le frazioni appiattite

Newton scrive **2BAP** per il doppio rettangolo di BA e AP, cioè 2·BA·AP: le due lettere centrali sono condivise. Allo stesso modo 2APQ = 2·AP·PQ e 2BPQ = 2·BP·PQ. La traduzione conserva la notazione, come fa Motte. La trascrizione appiattisce le frazioni («DdGDq» per Dd/GD²): le letture sono dichiarate in § A.12 e ricalcolate nelle note seguenti.

### N3. Propp. XI–XII: la resistenza *a v + b v²*

In termini moderni, con resistenza (per unità di massa) *a v + b v²* e nessun’altra forza:

- **Prop. XI** (velocità e tempo): d*v*/d*t* = −(*a v* + *b v*²) dà 1/*v* + *b*/*a* = (1/*v*₀ + *b*/*a*)·e^(*a t*). Dunque GD ∝ 1/*v*, CG ∝ *b*/*a*, e CD = CG + GD cresce in progressione geometrica quando *t* cresce in progressione aritmetica. L’area iperbolica ABED è proporzionale a ln(CD/CA): l’area sotto l’iperbole equilatera è il logaritmo.
- **Prop. XII** (velocità e spazio): *v* d*v*/d*s* = −(*a v* + *b v*²), cioè d*v*/d*s* = −(*a* + *b v*), dà *v* + *a*/*b* = (*v*₀ + *a*/*b*)·e^(−*b s*). Qui GD ∝ *v*, CG ∝ *a*/*b*, e CD decresce in progressione geometrica.
- **Controllo numerico** (*a* = 0,7, *b* = 1,3, *v*₀ = 2): nella Prop. XI il rapporto fra valori successivi di 1/*v* + *b*/*a* a intervalli di tempo unitari è 2,0137527 tre volte di seguito, contro e^0,7 = 2,0137527; nella Prop. XII il rapporto fra valori successivi di *v* + *a*/*b* a intervalli di spazio unitari è 0,2725318 contro e^(−1,3) = 0,2725318.
- **Il *conjunctim* di II.S3.08.** Il decremento della velocità per particella di spazio è come *a* + *b v*: una quantità data **più** una quantità decrescente. Newton scrive *ut quantitas data & quantitas decrescens conjunctim*: qui *conjunctim* indica le due grandezze prese insieme come somma, non il prodotto del linguaggio delle proporzioni composte. La resa del glossario («considerate congiuntamente») è mantenuta; il senso è chiarito qui.

### N4. Prop. XIII: salita e discesa con gravità e resistenza mista

In termini moderni, con gravità *g* e resistenza *k*₁*v* + *k*₂*v*², nella salita d*v*/d*t* = −(*g* + *k*₁*v* + *k*₂*v*²) = −*k*₂[(*v* + *k*₁/2*k*₂)² + *g*/*k*₂ − (*k*₁/2*k*₂)²]. Nella figura di Newton AB = *k*₁/2*k*₂ (così che AP² + 2BAP = (*v*² + 2AB·*v*) è proporzionale alla resistenza) e BP = AB + *v*.

- **Caso 1** (*g*/*k*₂ > AB²): gravità ∝ AB² + BD² = DA², e la somma delle forze è ∝ DP². Il tempo è un arcotangente, cioè un **settore di cerchio**.
- **Caso 2** (*g*/*k*₂ < AB²): gravità ∝ AB² − BD², somma ∝ BP² − BD²: il tempo è un’arcotangente iperbolica, cioè un **settore d’iperbole** (iperbole y² − x² = DB² con vertice F).
- **Caso 3** (discesa): gravità ∝ BD² − AB², forza netta ∝ BD² − BP²: di nuovo un settore d’iperbole (x² − y² = DB², vertice B).
- **Scolio**: il caso limite *g*/*k*₂ = AB² (BD = 0) dà d*v*/d*t* ∝ −BP², con tempo ∝ 1/AB − 1/BP: una funzione algebrica, senza settore. Newton lo lascia al lettore.
- **Euclide II.12** (II.S3.14): con D nell’origine, B = (DB, 0), A e P sulla retta x = DB, si ha DP² = DB² + BP² = DB² + (AB + AP)² = DA² + AP² + 2BA·AP. Verificato.
- **Controllo numerico.** Con DB = 1 e coefficienti unitari, integrando d*v*/d*t* e misurando l’area del settore tagliato da DP, la variazione del settore divisa per il tempo trascorso vale 0,500000 in tutti e quattro gli istanti di controllo, in ciascuno dei tre casi (valore atteso DB³/2 = 0,5). Il settore è dunque proporzionale al tempo, come afferma Newton.

### N5. Prop. XIII, Corollario

Nel Caso 1 il tempo dell’intera salita è *t* = 2·EDT/DB³ (con le unità di N4) e la velocità che la gravità DA² toglierebbe nel vuoto nello stesso tempo è DA²·*t*. Il settore DAt, simile a EDT con raggio DA, vale EDT·DA²/DB²; il triangolo DAP vale ½·DB·AP. Il rapporto AP : (DA²·*t*) coincide allora **esattamente** con triangolo DAP : settore DAt, non solo al limite. Controllo numerico (AB = 0,6, AP = 0,9): 1,495936 contro 1,495939 (la differenza viene dal passo d’integrazione).

### N6. Prop. XIV e Corollario: lo spazio come differenza di aree

- **Iperbole bN.** Con asintoti CK, CH e Ab = DB³/(4BA×AC), si ha LO×CL = Ab×CA, quindi LO = DB³/(4AB×CK); il momento KLON = KL×LO coincide con BPQ×BD³/(2Z×CK×AB). L’area AbNK è proporzionale a ln(CK/CA): cresce in progressione aritmetica mentre CK cresce in progressione geometrica.
- **Catena dei momenti.** Da DTV = BD×m e DPQ = ½BD×PQ si ricava PQ×BD³ = 2BD×m×CK×Z; sostituendo, KLON = BP×BD×m/AB e KLON − DTV = (BP − AB)×BD×m/AB = AP×BD×m/AB. Tutti i passaggi sono stati ricalcolati simbolicamente: tornano.
- **Controllo numerico** (Caso 1, DB = 1, AB = 0,6, salita da AP = 0,9 fino all’altezza massima): il rapporto fra la variazione di (AbNK − DET) e lo spazio percorso vale 0,833333 in otto istanti, uguale al valore atteso BD×m/AB = 0,5/0,6.
- **Corollario.** Con M = DET/BD e V = M×DA/DE, V è proporzionale al tempo (perché DET lo è) e BD×V²/AB è proporzionale allo spazio di caduta nel vuoto ½·DA²·*t*². Il rapporto fra lo spazio nel mezzo resistente e quello nel vuoto risulta esattamente quello di (AbNK − DET) a BD×V²/AB. Questo controllo richiede **M = DET/BD**, non DET/ED (§ A.4): con ED il passaggio «DA²×BD×M/DE² è come (DA²/DE²)×DET» fallisce nei Casi 2 e 3, dove DE ≠ DB.

### N7. Scolio della Sezione III: le tre parti della resistenza

Newton distingue tre origini della resistenza: tenacità, attrito, densità. Attribuisce alla densità la parte in rapporto duplicato della velocità e alla tenacità una parte **uniforme**, indipendente dalla velocità («come il momento del tempo»: la velocità che essa toglie è proporzionale al tempo, come per la gravità). Per l’attrito non dice qui quale legge segua. Di qui la proposta di trattare la resistenza uniforme come una gravità aggiunta o sottratta (Propp. VIII–IX del Libro II) e la combinazione con la parte lineare (Propp. XIII–XIV). Nella fisica moderna la resistenza viscosa a basse velocità è proporzionale alla velocità (legge di Stokes), non uniforme: la classificazione di Newton non coincide con quella attuale (non verificato sulle fonti allegate).

### N8. Lemma III: la spirale equiangola

Sulla spirale *r* = e^(0,4θ), con Q che si avvicina a P, il rapporto TQ×2PS/PQ² vale 0,979129, 0,997394 e 0,999734 per Δθ = 0,1, 0,01 e 0,001, e l’angolo PSO vale 92,88°, 90,29° e 90,03°: tendono a 1 e a 90°, come afferma il lemma. In termini moderni, O è al limite il centro di curvatura della spirale in P, e il lemma dice che lo scarto TQ fra tangente e curva, misurato lungo il raggio, vale PQ²/(2PS): è la relazione che nella Prop. XV permette di trasformare la saetta TQ in una funzione di PQ e SP.

### N9. Prop. XV e Corollari 1–6: verifica

- Sia α l’angolo fra la spirale e il raggio. Nel triangolo OSP, retto in S (Lemma III), l’angolo OPS vale 90° − α: quindi **OS/OP = cos α**, **PS/OS = tan α**, **OP/OS = sec α**. Sono le «tangente» e «secante» del Cor. 6.
- In termini moderni: con forza *g* = μ/*r*² e velocità circolare *v* = √(μ/*r*) (Cor. 1), mentre il corpo scende la velocità deve crescere al ritmo d*v*/d*t* = ½*g* cos α; la componente della gravità lungo la traiettoria darebbe *g* cos α, e la resistenza deve togliere la differenza. Ne segue resistenza = ½*g* cos α, cioè **resistenza : forza centripeta = ½OS : OP** (Cor. 3), e densità = resistenza/*v*² ∝ cos α/*r* (Cor. 2 e tesi).
- **Controllo numerico.** Integrando il moto con forza μ/*r*², resistenza *c*ρ*v*² e ρ ∝ 1/*r*, con ρ scelto secondo il Cor. 2 e la velocità iniziale circolare inclinata di α sul raggio, l’angolo con il raggio resta 70,0000° (α = 70°) e 40,0000° (α = 40°) mentre *r* scende da 1 a 0,93 e a 0,84, e il rapporto *v*/*v*_circ resta 1,000000: il corpo segue la spirale equiangola con la velocità del Cor. 1.
- Cor. 4: per α → 0 la resistenza tende a ½*g* (retta PS); per α > 0 è minore: il corpo «non può girare in questa spirale» se la resistenza supera metà della forza centripeta. Cor. 5: lunghezza della spirale / lunghezza del raggio = sec α = OP/OS. Cor. 6: il numero di giri fra due cerchi è proporzionale a dθ/d ln *r* = tan α; il tempo è proporzionale alla lunghezza, cioè a sec α, e la densità è proporzionale a cos α: tutto torna.

### N10. Prop. XV, Cor. 4: il rapporto 1 : √2

Nella discesa lungo la retta, con resistenza pari a metà della forza, la velocità è ancora quella circolare alla stessa distanza (√(μ/*r*)). La caduta libera dall’infinito («caso della parabola», Prop. XXXIV del Libro I) dà la velocità circolare alla distanza *r*/2, cioè √(2μ/*r*). Il rapporto è 1 : √2 = 0,7071, *in subduplicata ratione unitatis ad numerum binarium*. Verificato.

### N11. Prop. XV, Cor. 7: tempo totale di caduta al centro

Il tempo di ogni rivoluzione è come perimetro/velocità ∝ AS/AS^(−1/2) = AS^(3/2); le distanze AS, BS, CS… sono in progressione geometrica, e così i tempi. La somma della serie sta al primo termine come AS^(3/2) : (AS^(3/2) − BS^(3/2)), che per AB piccolo vale circa ⅔AS : AB. Controllo con AS = 1, BS = 0,97: valore esatto 22,391, approssimazione ⅔AS/AB = 22,222 (scarto 0,75 %): *quam proxime* è giustificato per rivoluzioni strette.

### N12. Prop. XV, Cor. 8: «numero» o «tempo»?

Il Cor. 8 adatta la spirale a un mezzo di densità qualsiasi, cerchio per cerchio. Per il Cor. 6, a parità di cerchi, il tempo delle rivoluzioni è come la secante e inversamente come la densità; il numero delle rivoluzioni è come la tangente. La frase del Cor. 8 contiene tutte e tre le proporzioni (tempo–densità, secanti, tangenti–numeri). La prima, nella trascrizione, comincia con *numerum* ma prosegue con *ad tempus*: solo la lettura *tempus … ad tempus* (quella di Motte) è coerente con il Cor. 6 e con la secante che segue «nello stesso rapporto». Si segnala senza correggere il testo.

### N13. Prop. XVI: forza come una potenza qualsiasi

Con forza μ/*r*^(n+1) e velocità circolare √(μ/*r*^n), lo stesso calcolo di N9 dà resistenza = (1 − ½*n*)·*g* cos α, cioè il Cor. 1, e densità ∝ (resistenza)/*v*² ∝ 1/*r* per ogni *n*. Controllo numerico con *n* = 0,5 e *n* = 1,5, α = 60°: angolo costante 60,0000°, *v*/*v*_circ = 1,000000. Per *n* = 2 (forza come l’inverso del cubo) la resistenza è nulla: è la spirale della Prop. IX del Libro I. Per *n* > 2 la resistenza dovrebbe essere negativa, cioè il mezzo dovrebbe spingere il corpo in avanti (Cor. 3).

### N14. Scolio della Prop. XVI e Propp. XVII–XVIII

Lo Scolio introduce due ipotesi: corpi piccoli rispetto alla scala di variazione della densità, e resistenza proporzionale alla densità a parità del resto. Le Propp. XVII e XVIII sono enunciati di metodo senza calcolo: dalla legge della velocità si ottengono i tempi; dalla saetta TQ la forza (Lemma X del Libro I); dal difetto d’area RSr il ritardo e quindi la resistenza. Il rinvio finale alla Prop. X e al Lemma II del Libro II indica il metodo dei momenti già usato per i mezzi di densità variabile.

---

## Controllo della copertura

Pagine 1726 dai marcatori ‹n› della trascrizione. Per Motte gli estratti non hanno marcatori di pagina: si indica la sezione.

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| (titolo) | *De motu corporum quibus resistitur* | Titolo della Sez. III | p. 265 | Section III |
| II.S3.01–II.S3.03 | *Si corpori resistitur partim* | Prop. XI, enunciato e dimostrazione | pp. 265–266 | Section III |
| II.S3.04–II.S3.05 | *Igitur si, datis punctis A, G* … *Sumendo autem GA* | Prop. XI, Cor. 1–2 | p. 266 | Section III |
| II.S3.06–II.S3.08 | *Iisdem positis, dico quod si spatia* | Prop. XII, enunciato e dimostrazione | pp. 266–267 | Section III |
| II.S3.09–II.S3.11 | *Si velocitas exponatur per longitudinem GD* … *Unde cum* | Prop. XII, Cor. 1–3 | p. 267 | Section III |
| II.S3.12–II.S3.14 | *Posito quod corpus ab uniformi gravitate* | Prop. XIII, enunciato, Caso 1 | pp. 267–268 | Section III |
| II.S3.15–II.S3.16 | *Si velocitas in ascensu corporis* | Prop. XIII, Caso 2 | pp. 268–269 | Section III |
| II.S3.17–II.S3.18 | *Sit AP velocitas in descensu* | Prop. XIII, Caso 3 | p. 269 | Section III |
| II.S3.19–II.S3.20 | *Si centro D semidiametro DA* … *Demonstrati etiam posset* | Prop. XIII, Cor., Scolio | pp. 269–270 | Section III |
| II.S3.21–II.S3.23 | *Iisdem positis, dico quod spatium ascensu* | Prop. XIV, enunciato, costruzione, momenti | pp. 270–271 | Section III |
| II.S3.24–II.S3.27 | *Jam si corpus ascendit* … *Cum igitur areæ illæ* | Prop. XIV, Casi 1–3 e conclusione | pp. 271–273 | Section III |
| II.S3.28–II.S3.29 | *Si longitudo, quæ oritur applicando* | Prop. XIV, Cor. e sua dimostrazione | pp. 273–274 | Section III |
| II.S3.30–II.S3.31 | *Resistentia corporum sphæricorum* | Scolio della Sezione III | p. 274 | Section III |
| (titolo) | *De corporum circulari motu* | Titolo della Sez. IV | p. 274 | Section IV |
| II.S4.01–II.S4.03 | *Sit PQR spiralis* | Lemma III | pp. 274–275 | Section IV |
| II.S4.04–II.S4.08 | *Si medii densitas … sitque vis centripeta in duplicata* | Prop. XV, enunciato e dimostrazione | pp. 275–277 | Section IV |
| II.S4.09–II.S4.14 | *Velocitas in loco quovis P* … *Si centro S intervallis duobus* | Prop. XV, Cor. 1–6 | pp. 277–278 | Section IV |
| II.S4.15–II.S4.17 | *Si corpus, in medio cujus densitas* … *Et quamvis motus excentrici* | Prop. XV, Cor. 7–9 | pp. 278–279 | Section IV |
| II.S4.18–II.S4.19 | *Si medii densitas … reciproce ut dignitas quælibet* | Prop. XVI, enunciato e dimostrazione | p. 280 | Section IV |
| II.S4.20–II.S4.23 | *Resistentia est ad vim centripetam* … *Cæterum hæc propositio* | Prop. XVI, Cor. 1–3, Scolio | pp. 280–281 | Section IV |
| II.S4.24–II.S4.25 | *Invenire & vim centripetam* | Prop. XVII | p. 281 | Section IV |
| II.S4.26–II.S4.28 | *Data lege vis centripetæ* … *Methodum vero tractandi* | Prop. XVIII e capoverso finale | pp. 281–282 | Section IV |

**Controlli eseguiti.**

1. **Copertura frase per frase.** Ho riletto in sequenza ogni periodo della trascrizione, da *De motu corporum quibus resistitur* a *his affines peraguntur*, contro la traduzione: nessuna frase manca. I periodi lunghi sono divisi in più frasi senza omettere membri. I 59 identificatori (31 + 28) sono consecutivi e unici (controllo automatico).
2. **Parte B.** `check.py` sul file finale (esito nel messaggio di consegna): JSON valido; tutte le stringhe `la` e `en` sottostringhe esatte delle fonti (le `en` con i marcatori `[SVG n]`, ignorati dallo strumento); identificatori di `copertura` presenti nel testo.
3. **Matematica.** Verifiche numeriche e simboliche per Propp. XI, XII, XIII (tre casi e Cor.), XIV (con Cor.), Lemma III, Prop. XV (tesi, Cor. 1–7), Prop. XVI (tesi e Cor. 1–3), Euclide II.12 (note N3–N13). Tutti i risultati di Newton tornano; l’unico punto che non torna con il testo della trascrizione è la lettera ED nel Cor. della Prop. XIV (deve essere BD), più la lettura *numerum* del Cor. 8 della Prop. XV. Non ci sono tabelle numeriche in queste sezioni.
4. **Motte.** Confronto di tutto il testo inglese delle due sezioni, comprese le 64 formule SVG (536–599), rese e lette una per una; divergenze nel § A.16 e nel § A.14 (due errori di formula di Motte 1846: SVG 547 e 582).
5. **Rimandi.** Tre rimandi al Libro I verificati sui Fascicoli 4, 5 e 8; uno a Euclide; rimandi interni al Libro II controllati sul latino della Sezione II (§ A.15).
6. **Separazione fra testo e commento.** Il testo tradotto non contiene formule moderne; le integrazioni sono tra parentesi quadre («in [P]» in II.S3.13; «[il calcolo che segue richiede BD]» in II.S3.28; «[Prop. XXXIV]» in II.S4.12; «[il senso richiede: il tempo]» in II.S4.16).

**Non ho potuto verificare:**

- **la stampa del 1726** (scansione ECCO) e **Motte 1729**: nessuno dei punti di § A.13 è stato controllato; in particolare restano aperti *ED/BD* (p. 273), *numerum/tempus* (p. 279), *in [P]* (p. 267) e la presenza dei radicali (p. 276);
- **Motte 1729**: non so se gli errori delle formule SVG 547 e 582 risalgano alla prima edizione inglese;
- **le figure originali** NATP00088-25…37: la posizione dei punti (per esempio il punto F della Prop. XI, il punto G nei Casi 2 e 3 della Prop. XIII, la disposizione di C e K nelle tre figure della Prop. XIV) è ricostruita dal testo;
- **la paginazione di Motte**: gli estratti non hanno marcatori.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Libro II, Sezioni III–IV (Propp. XI–XVIII, Lemma III) | **Fascicolo 15, presente documento, prima versione** |
| Punti di § A.13 | Da verificare sulla stampa del 1726 (ECCO) e su Motte 1729 |
| SVG 536–599 | Viste tutte; errori di Motte 1846 in 547 (BD² per BD³) e 582 (½ per ¼) da controllare su Motte 1729 |
| *divisim* | Resa da armonizzare con il Libro I («separando» / «dividendo») |
| *resistitur* impersonale | Resa «si resiste a» da armonizzare con i Fascicoli 13–14 |
| Figure NATP00088-25…37 | Da consultare per confermare `figura_base` |
| Pagine interattive | Parte B: 10 unità; la Prop. XIV e il suo Cor. hanno passi con molte formule: andranno mostrati in più tempi |
| Revisione filologica e scientifica indipendente | Da eseguire |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce traduzioni italiane o inglesi moderne. **Licenza prevista** (decisione del curatore, Fascicolo 3): testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project; i testi di Motte sono di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Unità incluse: le proposizioni con dimostrazione geometrica e figura (Propp. XI, XII, XIII, XIV, XV, XVI, XVII; Lemma III) e i due corollari con dimostrazione propria (Prop. XIII, Cor.; Prop. XIV, Cor.). **Escluse**: i corollari senza dimostrazione propria (anche il Cor. 7 della Prop. XV, che ha figura ma non dimostrazione), gli scolii, la Prop. XVIII (senza figura).

Convenzioni: `la` è il testo esatto della trascrizione (refusi, frazioni appiattite e radicali perduti compresi); `it` è la traduzione di questo fascicolo; `en` è Motte 1846 allineato per senso, con i marcatori `[SVG n]` conservati; `dipende_da` contiene soltanto i rimandi citati nella frase latina.

```json
{
 "fascicolo": "15-L2-S3-4",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase latina",
  "en": "Motte 1846, allineato per senso; i marcatori [SVG n] sono conservati e ignorati dallo strumento di controllo; le formule corrispondenti sono state viste e confrontate (apparato A.14)",
  "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione",
  "la": ""
 },
 "unita": [
  {
   "id": "L2-P11",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XI — resistenza mista, moto per la sola forza insita: velocità e tempo",
   "copertura": [
    "II.S3.01",
    "II.S3.02",
    "II.S3.03"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente"
   },
   "enunciato": {
    "la": "",
    "it": "Se a un corpo si resiste in parte in rapporto alla velocità, in parte in rapporto duplicato della velocità, e il corpo si muove per la sola forza insita in un mezzo omogeneo, e si prendono i tempi in progressione aritmetica, le quantità inversamente proporzionali alle velocità, aumentate di una certa quantità data, saranno in progressione geometrica.",
    "en": "If a body be resisted partly in the ratio and partly in the duplicate ratio of its velocity, and moves in a similar medium by its innate force only; and the times be taken in arithmetical progression; then quantities reciprocally proportional to the velocities, increased by a certain given quantity, will be in geometrical progression."
   },
   "figura_base": {
    "punti": [
     "C",
     "A",
     "G",
     "D",
     "d",
     "B",
     "E",
     "e",
     "H",
     "F"
    ],
    "vincoli": [
     "CADd e CH asintoti ortogonali dell'iperbole BEe con centro C",
     "AB, DE, de parallele a CH",
     "A, G dati sull'asintoto CD",
     "area ABED proporzionale al tempo",
     "GD inversamente come la velocità; DF come la velocità (DF ∝ 1/GD)",
     "CD = CG + GD in progressione geometrica"
    ]
   },
   "passi": [
    {
     "id": "L2-P11-p1",
     "la": "",
     "it": "Con centro C e con gli asintoti ortogonali CADd e CH si descriva l’iperbole BEe, e siano AB, DE, de parallele all’asintoto CH.",
     "en": "With the centre C, and the rectangular asymptotes CADd and CH, describe an hyperbola BEe, and let AB, DE, de, be parallel to the asymptote CH.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "C",
       "asintoti CADd e CH",
       "iperbole BEe",
       "AB, DE, de ∥ CH"
      ]
     }
    },
    {
     "id": "L2-P11-p2",
     "la": "",
     "it": "Sull’asintoto CD siano dati i punti A, G. E se il tempo è rappresentato dall’area iperbolica ABED, che cresce uniformemente, dico che la velocità può essere rappresentata dalla lunghezza DF, la cui inversa GD, insieme con la CG data, compone la lunghezza CD crescente in progressione geometrica.",
     "en": "In the asymptote CD let A, G be given points; and if the time be expounded by the hyperbolic area ABED uniformly increasing, I say, that the velocity may be expressed by the length DF, whose reciprocal GD, together with the given line CG, compose the length CD increasing in a geometrical progression.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A",
       "G",
       "area ABED",
       "DF",
       "GD",
       "CG"
      ],
      "evidenzia": [
       "area ABED = tempo",
       "CD = CG + GD"
      ]
     },
     "nota": "«fi tempus» è refuso probabile della trascrizione per «si tempus» (apparato A.1)."
    },
    {
     "id": "L2-P11-p3",
     "la": "",
     "it": "Sia infatti l’areola DEed l’incremento dato, piccolissimo, del tempo; e Dd sarà inversamente come DE, e quindi direttamente come CD.",
     "en": "For let the areola DEed be the least given increment of the time, and Dd will be reciprocally as DE, and therefore directly as CD.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "d",
       "e",
       "areola DEed",
       "Dd"
      ],
      "evidenzia": [
       "Dd × DE = costante (iperbole)"
      ]
     }
    },
    {
     "id": "L2-P11-p4",
     "la": "",
     "it": "Il decremento di 1/GD, poi, che (per il Lemma II di questo Libro) è Dd/GD², sarà come CD/GD², ossia (CG+GD)/GD², cioè come 1/GD + CG/GD².",
     "en": "Therefore the decrement of [SVG 536], which (by Lem. II, Book II) is [SVG 537], will be also as [SVG 538] or [SVG 539], that is, as [SVG 540].",
     "dipende_da": [
      "Libro II, Lemma II"
     ],
     "figura": {
      "mostra": [
       "GD",
       "CG"
      ],
      "evidenzia": [
       "decremento di 1/GD = Dd/GD²"
      ]
     },
     "nota": "Frazioni appiattite: «1GD» = 1/GD, «DdGDq» = Dd/GD², «CG+GDGDq» = (CG+GD)/GD². SVG 536–540."
    },
    {
     "id": "L2-P11-p5",
     "la": "",
     "it": "Dunque, mentre il tempo ABED cresce uniformemente per l’aggiunta delle particelle date EDde, 1/GD decresce nello stesso rapporto della velocità.",
     "en": "Therefore the time ABED uniformly increasing by the addition of the given particles EDde, it follows that [SVG 536] decreases in the same ratio with the velocity.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area ABED che cresce",
       "particelle EDde"
      ],
      "evidenzia": [
       "1/GD decresce come la velocità"
      ]
     }
    },
    {
     "id": "L2-P11-p6",
     "la": "",
     "it": "Infatti il decremento della velocità è come la resistenza, cioè (per ipotesi) come la somma di due quantità, delle quali una è come la velocità, l’altra come il quadrato della velocità; e il decremento di 1/GD è come la somma delle quantità 1/GD e CG/GD², delle quali la prima è la stessa 1/GD, e la seconda, CG/GD², è come 1/GD²: perciò 1/GD, per l’analogia dei decrementi, è come la velocità.",
     "en": "For the decrement of the velocity is as the resistance, that is (by the supposition), as the sum of two quantities, whereof one is as the velocity, and the other as the square of the velocity; and the decrement of [SVG 536] is as the sum of the quantities [SVG 536] and [SVG 541], whereof the first is [SVG 536] itself, and the last [SVG 541] is as [SVG 542]: therefore [SVG 536] is as the velocity, the decrements of both being analogous.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "GD"
      ],
      "evidenzia": [
       "decremento ∝ 1/GD + CG/GD² ↔ a v + b v²"
      ]
     }
    },
    {
     "id": "L2-P11-p7",
     "la": "",
     "it": "E se la quantità GD, inversamente proporzionale a 1/GD, è aumentata della quantità data CG, la somma CD, mentre il tempo ABED cresce uniformemente, crescerà in progressione geometrica. C.V.D.",
     "en": "And if the quantity GD reciprocally proportional to [SVG 536], be augmented by the given quantity CG; the sum CD, the time ABED uniformly increasing, will increase in a geometrical progression. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "CD"
      ],
      "evidenzia": [
       "CD in progressione geometrica"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P12",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XII — resistenza mista: velocità e spazio",
   "copertura": [
    "II.S3.06",
    "II.S3.07",
    "II.S3.08"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente"
   },
   "enunciato": {
    "la": "",
    "it": "Poste le stesse cose, dico che, se si prendono gli spazi descritti in progressione aritmetica, le velocità, aumentate di una certa quantità data, saranno in progressione geometrica.",
    "en": "The same things being supposed, I say, that if the spaces described are taken in arithmetical progression, the velocities augmented by a certain given quantity will be in geometrical progression."
   },
   "figura_base": {
    "punti": [
     "C",
     "R",
     "S",
     "G",
     "D",
     "d",
     "E",
     "e"
    ],
    "vincoli": [
     "stessa iperbole e asintoti della Prop. XI",
     "RS perpendicolare all'asintoto CD, S sull'iperbole",
     "area RSED proporzionale allo spazio",
     "GD come la velocità",
     "CD = CG + GD decrescente in progressione geometrica"
    ]
   },
   "passi": [
    {
     "id": "L2-P12-p1",
     "la": "",
     "it": "Sull’asintoto CD sia dato il punto R e, innalzata la perpendicolare RS, che incontri l’iperbole in S, si rappresenti lo spazio descritto con l’area iperbolica RSED; e la velocità sarà come la lunghezza GD, che con la CG data compone la lunghezza CD decrescente in progressione geometrica, mentre lo spazio RSED aumenta in progressione aritmetica.",
     "en": "In the asymptote CD let there be given the point R, and, erecting the perpendicular RS meeting the hyperbola in S, let the space described be expounded by the hyperbolic area RSED; and the velocity will be as the length GD, which, together with the given line CG, composes a length CD decreasing in a geometrical progression, while the space RSED increases in an arithmetical progression.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "R",
       "S",
       "RS",
       "area RSED",
       "GD",
       "CG"
      ],
      "evidenzia": [
       "area RSED = spazio",
       "GD = velocità"
      ]
     }
    },
    {
     "id": "L2-P12-p2",
     "la": "",
     "it": "Infatti, poiché l’incremento EDde dello spazio è dato, la lineetta Dd, che è il decremento della GD, sarà inversamente come ED, e quindi direttamente come CD, cioè come la somma della stessa GD e della lunghezza data CG.",
     "en": "For, because the increment EDde of the space is given, the lineola Dd, which is the decrement of GD, will be reciprocally as ED, and therefore directly as CD; that is, as the sum of the same GD and the given length CG.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "particella EDde",
       "Dd"
      ],
      "evidenzia": [
       "Dd ∝ CD = GD + CG"
      ]
     }
    },
    {
     "id": "L2-P12-p3",
     "la": "",
     "it": "Ma il decremento della velocità, nel tempo a essa inversamente proporzionale in cui è descritta la particella data DdeE dello spazio, è come la resistenza e il tempo considerati congiuntamente, cioè direttamente come la somma di due quantità, delle quali una è come la velocità, l’altra come il quadrato della velocità, e inversamente come la velocità; e quindi direttamente come la somma di due quantità, delle quali una è data, l’altra è come la velocità.",
     "en": "But the decrement of the velocity, in a time reciprocally proportional thereto, in which the given particle of space DdeE is described, is as the resistance and the time conjunctly, that is, directly as the sum of two quantities, whereof one is as the velocity, the other as the square of the velocity, and inversely as the velocity; and therefore directly as the sum of two quantities, one of which is given, the other is as the velocity.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "particella DdeE"
      ],
      "evidenzia": [
       "decremento della velocità ∝ a + b v"
      ]
     }
    },
    {
     "id": "L2-P12-p4",
     "la": "",
     "it": "Dunque il decremento sia della velocità sia della linea GD è come una quantità data e una quantità decrescente considerate congiuntamente; e, poiché i decrementi sono analoghi, saranno sempre analoghe le quantità decrescenti, cioè la velocità e la linea GD. C.V.D.",
     "en": "Therefore the decrement both of the velocity and the line GD is as a given quantity and a decreasing quantity conjunctly; and, because the decrements are analogous, the decreasing quantities will always be analogous; viz., the velocity, and the line GD. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "GD"
      ],
      "evidenzia": [
       "velocità ∝ GD"
      ]
     },
     "nota": "«conjunctim» indica qui la somma di una quantità data e di una decrescente (nota N3)."
    }
   ]
  },
  {
   "id": "L2-P13",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XIII — salita e discesa con gravità uniforme: i tempi come settori",
   "copertura": [
    "II.S3.12",
    "II.S3.13",
    "II.S3.14",
    "II.S3.15",
    "II.S3.16",
    "II.S3.17",
    "II.S3.18"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente"
   },
   "enunciato": {
    "la": "",
    "it": "Posto che un corpo, attratto verso il basso da una gravità uniforme, salga o scenda in linea retta, e che gli si resista in parte in rapporto alla velocità, in parte in rapporto duplicato di essa, dico che, se per gli estremi di diametri coniugati di un cerchio e di un’iperbole si conducono rette parallele ai diametri, e le velocità sono come certi segmenti di queste parallele, i tempi saranno come i settori delle aree tagliati da rette condotte dal centro agli estremi dei segmenti; e viceversa.",
    "en": "Supposing that a body attracted downwards by an uniform gravity ascends or descends in a right line; and that the same is resisted partly in the ratio of its velocity, and partly in the duplicate ratio thereof: I say, that, if right lines parallel to the diameters of a circle and an hyperbola, be drawn through the ends of the conjugate diameters, and the velocities be as some segments of those parallels drawn from a given point, the times will be as the sectors of the areas cut off by right lines drawn from the centre to the ends of the segments; and the contrary."
   },
   "figura_base": {
    "punti": [
     "D",
     "B",
     "F",
     "E",
     "T",
     "V",
     "A",
     "P",
     "Q",
     "G"
    ],
    "vincoli": [
     "Caso 1: cerchio di centro D e raggio DB (quadrante BETF); retta BAP per B parallela a DF (perpendicolare a DB)",
     "AP = velocità; resistenza ∝ AP² + 2BA×AP; gravità ∝ DA²",
     "DA, DP tagliano il cerchio in E, T; DQ in V; PQ momento della velocità",
     "Caso 2: DF ⊥ DB, DF = DB; iperbole FTVE con semidiametri coniugati DB, DF; gravità ∝ AB² − BD²; G piede su DF della perpendicolare da T",
     "Caso 3: iperbole rettangola BETV di centro D e vertice principale B; angolo DBA retto; gravità ∝ BD² − AB²; G piede su DB della perpendicolare da T"
    ]
   },
   "passi": [
    {
     "id": "L2-P13-p1",
     "la": "",
     "it": "Caso 1. Supponiamo dapprima che il corpo salga. Con centro D e con un semidiametro qualsiasi DB si descriva il quadrante di cerchio BETF, e per l’estremo B del semidiametro DB si conduca la retta illimitata BAP, parallela al semidiametro DF.",
     "en": "CASE 1. Suppose first that the body is ascending, and from the centre D, with any semi-diameter DB, describe a quadrant BETF of a circle, and through the end B of the semi-diameter DF draw the indefinite line BAP, parallel to the semi-diameter DF.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "D",
       "B",
       "F",
       "quadrante BETF",
       "retta BAP ∥ DF"
      ]
     },
     "nota": "Motte: «the end B of the semi-diameter DF» (errore: DB)."
    },
    {
     "id": "L2-P13-p2",
     "la": "",
     "it": "Su di essa sia dato il punto A, e si prenda il segmento AP proporzionale alla velocità.",
     "en": "In that line let there be given the point A, and take the segment AP proportional to the velocity.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A",
       "P",
       "AP"
      ],
      "evidenzia": [
       "AP = velocità"
      ]
     }
    },
    {
     "id": "L2-P13-p3",
     "la": "",
     "it": "E poiché una parte della resistenza è come la velocità e l’altra parte come il quadrato della velocità, sia la resistenza totale in [P] come AP²+2BAP.",
     "en": "And since one part of the resistance is as the velocity, and another part as the square of the velocity, let the whole resistance be as AP2 + 2BAP.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "BA",
       "AP"
      ],
      "evidenzia": [
       "resistenza ∝ AP² + 2BA×AP"
      ]
     },
     "nota": "«tota in ut»: «in» senza complemento; probabile «in P» (Motte «in P» nella frase seguente). Apparato A.3."
    },
    {
     "id": "L2-P13-p4",
     "la": "",
     "it": "Si congiungano DA, DP, che taglino il cerchio in E e in T, e si rappresenti la gravità con DA², in modo che la gravità stia alla resistenza come DA² sta ad AP²+2BAP: e il tempo dell’intera salita sarà come il settore di cerchio EDT.",
     "en": "Join DA, DP, cutting the circle in E and T, and let the gravity be expounded by DA2, so that the gravity shall be to the resistance in P as DA2 to AP2 + 2BAP; and the time of the whole ascent will be as the sector EDT of the circle.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "DA",
       "DP",
       "E",
       "T",
       "settore EDT"
      ],
      "evidenzia": [
       "gravità ∝ DA²",
       "tempo ∝ settore EDT"
      ]
     }
    },
    {
     "id": "L2-P13-p5",
     "la": "",
     "it": "Si conduca infatti DVQ, che tagli via sia il momento PQ della velocità AP, sia il momento DTV del settore DET corrispondente a un momento dato del tempo; e quel decremento PQ della velocità sarà come la somma delle forze, la gravità DA² e la resistenza AP²+2BAP, cioè (per la Prop. 12 del Libro II degli Elementi) come DP².",
     "en": "For draw DVQ, cutting off the moment PQ, of the velocity AP, and the moment DTV of the sector DET answering to a given moment of time; and that decrement PQ of the velocity will be as the sum of the forces of gravity DA2 and of resistance AP2 + 2BAP, that is (by Prop. XII, Book II, Elem.), as DP2.",
     "dipende_da": [
      "Euclide, Elementi II.12"
     ],
     "figura": {
      "mostra": [
       "DVQ",
       "Q",
       "V",
       "PQ",
       "settore DTV"
      ],
      "evidenzia": [
       "DA² + AP² + 2BA×AP = DP²"
      ]
     }
    },
    {
     "id": "L2-P13-p6",
     "la": "",
     "it": "Perciò l’area DPQ, proporzionale a PQ, è come DP²; e l’area DTV, che sta all’area DPQ come DT² sta a DP², è come DT², che è dato.",
     "en": "Then the area DPQ, which is proportional to PQ, is as DP2, and the area DTV, which is to the area DPQ as DT2 to DP2, is as the given quantity DT2.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangolo DPQ",
       "settore DTV"
      ],
      "evidenzia": [
       "DTV : DPQ = DT² : DP²"
      ]
     }
    },
    {
     "id": "L2-P13-p7",
     "la": "",
     "it": "L’area EDT decresce dunque uniformemente, alla maniera del tempo futuro, per la sottrazione delle particelle date DTV, e perciò è proporzionale al tempo dell’intera salita. C.V.D.",
     "en": "Therefore the area EDT decreases uniformly according to the rate of the future time, by subduction of given particles DTV, and is therefore proportional to the time of the whole ascent. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "settore EDT che si riduce"
      ],
      "evidenzia": [
       "EDT ∝ tempo residuo"
      ]
     }
    },
    {
     "id": "L2-P13-p8",
     "la": "",
     "it": "Caso 2. Se la velocità nella salita del corpo è rappresentata dalla lunghezza AP come prima, e la resistenza si pone come AP²+2BAP, e se la forza di gravità è minore di quella che può essere rappresentata da DA², si prenda BD di lunghezza tale che AB²−BD² sia proporzionale alla gravità; sia DF perpendicolare e uguale a DB, e per il vertice F si descriva l’iperbole FTVE, i cui semidiametri coniugati siano DB e DF, e che tagli DA in E, e DP, DQ in T e V; e il tempo dell’intera salita sarà come il settore d’iperbole TDE.",
     "en": "CASE 2. If the velocity in the ascent of the body be expounded by the length AP as before, and the resistance be made as AP2 + 2BAP, and if the force of gravity be less than can be expressed by DA2; take BD of such a length, that AB2 - BD2 may be proportional to the gravity, and let DF be perpendicular and equal to DB, and through the vertex F describe the hyperbola FTVE, whose conjugate semi-diameters are DB and DF, and which cuts DA in E, and DP, DQ in T and V; and the time of the whole ascent will be as the hyperbolic sector TDE.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "iperbole FTVE",
       "DF = DB, DF ⊥ DB",
       "E",
       "T",
       "V",
       "settore TDE"
      ],
      "evidenzia": [
       "gravità ∝ AB² − BD²"
      ]
     }
    },
    {
     "id": "L2-P13-p9",
     "la": "",
     "it": "Infatti il decremento PQ della velocità, prodotto in una particella data di tempo, è come la somma della resistenza AP²+2BAP e della gravità AB²−BD², cioè come BP²−BD².",
     "en": "For the decrement PQ. of the velocity, produced in a given particle of time, is as the sum of the resistance AP2 + 2BAP and of the gravity AB2 - BD2, that is, as BP2 - BD2.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "PQ",
       "BP"
      ],
      "evidenzia": [
       "AP² + 2BA×AP + AB² − BD² = BP² − BD²"
      ]
     }
    },
    {
     "id": "L2-P13-p10",
     "la": "",
     "it": "Ora l’area DTV sta all’area DPQ come DT² sta a DP²; e perciò, se su DF si abbassa la perpendicolare GT, come GT², ossia GD²−DF², sta a BD², e come GD² sta a BP², e, separando, come DF² sta a BP²−BD².",
     "en": "But the area DTV is to the area DPQ as DT2 to DP2; and, therefore, if GT be drawn perpendicular to DF, as GT2 or GD2 - DF2 to BD2, and as GD2 to BP2, and, by division, as DF2 to BP2 - BD2.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "G",
       "GT ⊥ DF"
      ],
      "evidenzia": [
       "GT² = GD² − DF² (iperbole)"
      ]
     }
    },
    {
     "id": "L2-P13-p11",
     "la": "",
     "it": "Poiché dunque l’area DPQ è come PQ, cioè come BP²−BD², l’area DTV sarà come DF², che è dato.",
     "en": "Therefore since the area DPQ is as PQ, that is, as BP2 - BD2, the area DTV will be as the given quantity DF2.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "settore DTV"
      ],
      "evidenzia": [
       "DTV ∝ DF² costante"
      ]
     }
    },
    {
     "id": "L2-P13-p12",
     "la": "",
     "it": "L’area EDT decresce dunque uniformemente in singole particelle di tempo uguali, per la sottrazione di altrettante particelle date DTV, e perciò è proporzionale al tempo. C.V.D.",
     "en": "Therefore the area EDT decreases uniformly in each of the equal particles of time, by the subduction of so many given particles DTV, and therefore is proportional to the time. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "settore EDT"
      ],
      "evidenzia": [
       "EDT ∝ tempo"
      ]
     }
    },
    {
     "id": "L2-P13-p13",
     "la": "",
     "it": "Caso 3. Sia AP la velocità nella discesa del corpo, AP²+2BAP la resistenza e BD²−AB² la forza di gravità, essendo retto l’angolo DBA.",
     "en": "CASE 3. Let AP be the velocity in the descent of the body, and AP2 + 2BAP the force of resistance, and BD2 - AB2 the force of gravity, the angle DBA being a right one.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "angolo DBA retto",
       "AP"
      ],
      "evidenzia": [
       "gravità ∝ BD² − AB²"
      ]
     }
    },
    {
     "id": "L2-P13-p14",
     "la": "",
     "it": "E se con centro D e vertice principale B si descrive l’iperbole rettangola BETV, che tagli i prolungamenti di DA, DP e DQ in E, T e V, il settore DET di questa iperbole sarà come il tempo della discesa.",
     "en": "And if with the centre D, and the principal vertex B, there be described a rectangular hyperbola BETV cutting DA, DP, and DQ produced in E, T, and V; the sector DET of this hyperbola will be as the whole time of descent.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "iperbole rettangola BETV",
       "E",
       "T",
       "V",
       "settore DET"
      ]
     },
     "nota": "Motte aggiunge «whole»."
    },
    {
     "id": "L2-P13-p15",
     "la": "",
     "it": "Infatti l’incremento PQ della velocità, e l’area DPQ a esso proporzionale, è come l’eccesso della gravità sulla resistenza, cioè come BD²−AB²−2BAP−AP², ossia BD²−BP².",
     "en": "For the increment PQ of the velocity, and the area DPQ proportional to it, is as the excess of the gravity above the resistance, that is, as BD2 - AB2 - 2BAP - AP2 or BD2 - BP2.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "PQ",
       "triangolo DPQ"
      ],
      "evidenzia": [
       "forza netta ∝ BD² − BP²"
      ]
     }
    },
    {
     "id": "L2-P13-p16",
     "la": "",
     "it": "E l’area DTV sta all’area DPQ come DT² sta a DP², e quindi come GT², ossia GD²−BD², sta a BP², e come GD² sta a BD², e, separando, come BD² sta a BD²−BP².",
     "en": "And the area DTV is to the area DPQ as DT2 to DP2; and therefore as GT2 or GD2 - BD2 to BP2, and as GD2 to BD2, and, by division, as BD2 to BD2 - BP2.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "G",
       "GT ⊥ DB"
      ],
      "evidenzia": [
       "GT² = GD² − BD² (iperbole rettangola)"
      ]
     }
    },
    {
     "id": "L2-P13-p17",
     "la": "",
     "it": "Poiché dunque l’area DPQ è come BD²−BP², l’area DTV sarà come BD², che è dato.",
     "en": "Therefore since the area DPQ is as BD2 - BP2, the area DTV will be as the given quantity BD2.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "settore DTV"
      ],
      "evidenzia": [
       "DTV ∝ BD² costante"
      ]
     }
    },
    {
     "id": "L2-P13-p18",
     "la": "",
     "it": "L’area EDT cresce dunque uniformemente in singole particelle di tempo uguali, per l’aggiunta di altrettante particelle date DTV, e perciò è proporzionale al tempo della discesa. C.V.D.",
     "en": "Therefore the area EDT increases uniformly in the several equal particles of time by the addition of as many given particles DTV, and therefore is proportional to the time of the descent. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "settore EDT che cresce"
      ],
      "evidenzia": [
       "EDT ∝ tempo di discesa"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P13-Cor",
   "tipo": "Corollarium",
   "titolo": "Prop. XIII, Cor. — confronto con il vuoto: triangolo e settore",
   "copertura": [
    "II.S3.19"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente"
   },
   "enunciato": {
    "la": "",
    "it": "Se con centro D e con semidiametro DA si conduce per il vertice A un arco At simile all’arco ET, che sottenda in modo simile l’angolo ADT, la velocità AP starà alla velocità che il corpo, nel tempo EDT, potrebbe perdere salendo o acquistare scendendo in uno spazio non resistente, come l’area del triangolo DAP sta all’area del settore DAt; e quindi è data a partire dal tempo dato.",
    "en": "If with the centre D and the semi-diameter DA there be drawn through the vertex A an arc At similar to the arc ET, and similarly subtending the angle ADT, the velocity AP will be to the velocity which the body in the time EDT, in a non-resisting space, can lose in its ascent, or acquire in its descent, as the area of the triangle DAP to the area of the sector DAt; and therefore is given from the time given."
   },
   "figura_base": {
    "punti": [
     "D",
     "A",
     "t",
     "E",
     "T",
     "P"
    ],
    "vincoli": [
     "figura della Prop. XIII",
     "arco At di centro D e raggio DA, simile all'arco ET, sotteso dall'angolo ADT"
    ]
   },
   "passi": [
    {
     "id": "L2-P13-Cor-p1",
     "la": "",
     "it": "Se con centro D e con semidiametro DA si conduce per il vertice A un arco At simile all’arco ET, che sottenda in modo simile l’angolo ADT, la velocità AP starà alla velocità che il corpo, nel tempo EDT, potrebbe perdere salendo o acquistare scendendo in uno spazio non resistente, come l’area del triangolo DAP sta all’area del settore DAt; e quindi è data a partire dal tempo dato.",
     "en": "COR. If with the centre D and the semi-diameter DA there be drawn through the vertex A an arc At similar to the arc ET, and similarly subtending the angle ADT, the velocity AP will be to the velocity which the body in the time EDT, in a non-resisting space, can lose in its ascent, or acquire in its descent, as the area of the triangle DAP to the area of the sector DAt; and therefore is given from the time given.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "arco At",
       "triangolo DAP",
       "settore DAt"
      ],
      "evidenzia": [
       "AP : velocità nel vuoto = DAP : DAt"
      ]
     },
     "nota": "«subtendes angulun» refusi probabili per «subtendens angulum»."
    },
    {
     "id": "L2-P13-Cor-p2",
     "la": "",
     "it": "Infatti la velocità, in un mezzo non resistente, è proporzionale al tempo, e perciò a questo settore; in un mezzo resistente è come il triangolo; e nell’uno e nell’altro mezzo, quando è piccolissima, si avvicina al rapporto di uguaglianza, come fanno il settore e il triangolo.",
     "en": "For the velocity in a non-resisting medium is proportional to the time, and therefore to this sector; in a resisting medium, it is as the triangle; and in both mediums, where it is least, it approaches to the ratio of equality, as the sector and triangle do.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "settore DAt",
       "triangolo DAP"
      ],
      "evidenzia": [
       "per AP → 0 settore e triangolo coincidono"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P14",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XIV — lo spazio di salita o di discesa come differenza di due aree",
   "copertura": [
    "II.S3.21",
    "II.S3.22",
    "II.S3.23",
    "II.S3.24",
    "II.S3.25",
    "II.S3.26",
    "II.S3.27"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente"
   },
   "enunciato": {
    "la": "",
    "it": "Poste le stesse cose, dico che lo spazio descritto nella salita o nella discesa è come la differenza fra l’area con cui è rappresentato il tempo e un’altra certa area, che aumenta o diminuisce in progressione aritmetica, se le forze composte della resistenza e della gravità si prendono in progressione geometrica.",
    "en": "The same things being supposed, I say, that the space described in the ascent or descent is as the difference of the area by which the time is expressed, and of some other area which is augmented or diminished in an arithmetical progression; if the forces compounded of the resistance and the gravity be taken in a geometrical progression."
   },
   "figura_base": {
    "punti": [
     "A",
     "C",
     "K",
     "L",
     "b",
     "N",
     "O",
     "H",
     "D",
     "B",
     "E",
     "T",
     "V",
     "P",
     "Q"
    ],
    "vincoli": [
     "figure della Prop. XIII (tre casi)",
     "AC ∝ gravità, AK ∝ resistenza; dalla stessa parte di A nella discesa, da parti contrarie nella salita",
     "Ab ⊥ CK, Ab : DB = DB² : 4BA×AC",
     "iperbole bN con asintoti ortogonali CK, CH; KN, LO ⊥ CK",
     "AK = (AP² + 2BA×AP)/Z con Z data; DTV = BD×m"
    ]
   },
   "passi": [
    {
     "id": "L2-P14-p1",
     "la": "",
     "it": "Si prenda AC (nelle tre ultime figure) proporzionale alla gravità, e AK proporzionale alla resistenza.",
     "en": "Take AC (in these three figures) proportional to the gravity, and AK to the resistance;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A",
       "C",
       "K",
       "AC",
       "AK"
      ],
      "evidenzia": [
       "AC ∝ gravità",
       "AK ∝ resistenza"
      ]
     }
    },
    {
     "id": "L2-P14-p2",
     "la": "",
     "it": "Si prendano poi dalla stessa parte del punto A se il corpo scende, altrimenti da parti contrarie.",
     "en": "but take them on the same side of the point A, if the body is descending, otherwise on the contrary.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "C e K rispetto ad A"
      ]
     },
     "nota": "La trascrizione spezza «cor ‹271› pus»."
    },
    {
     "id": "L2-P14-p3",
     "la": "",
     "it": "Si innalzi Ab, che stia a DB come DB² sta a 4BAC; e, descritta l’iperbole bN con gli asintoti ortogonali CK, CH, e innalzata KN perpendicolare a CK, l’area AbNK aumenterà o diminuirà in progressione aritmetica, mentre le forze CK si prendono in progressione geometrica.",
     "en": "Erect Ab, which make to DB as DB2 to 4BAC: and to the rectangular asymptotes CK, CH, describe the hyperbola bN; and, erecting KN perpendicular to CK, the area AbNK will be augmented or diminished in an arithmetical progression, while the forces CK are taken in a geometrical progression.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "b",
       "Ab",
       "iperbole bN",
       "asintoti CK, CH",
       "N",
       "KN",
       "area AbNK"
      ],
      "evidenzia": [
       "Ab = DB³/(4BA×AC)",
       "area AbNK ∝ log CK"
      ]
     }
    },
    {
     "id": "L2-P14-p4",
     "la": "",
     "it": "Dico dunque che la distanza del corpo dalla sua altezza massima è come l’eccesso dell’area AbNK sull’area DET.",
     "en": "I say, therefore, that the distance of the body from its greatest altitude is as the excess of the area AbNK above the area DET.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area AbNK",
       "settore DET"
      ],
      "evidenzia": [
       "spazio ∝ AbNK − DET"
      ]
     }
    },
    {
     "id": "L2-P14-p5",
     "la": "",
     "it": "Infatti, poiché AK è come la resistenza, cioè come AP²+2BAP, si assuma una quantità data qualsiasi Z, e si ponga AK uguale a (AP²+2BAP)/Z; e (per il Lemma II di questo Libro) il momento KL di AK sarà uguale a (2APQ+2BA×PQ)/Z, ossia 2BPQ/Z, e il momento KLON dell’area AbNK sarà uguale a 2BPQ×LO/Z, ossia BPQ×BD³/(2Z×CK×AB).",
     "en": "For since AK is as the resistance, that is, as AP2 × 2BAP; assume any given quantity Z, and put AK equal to [SVG 543]; then (by Lem. II of this Book) the moment KL of AK will be equal to [SVG 544] or [SVG 545], and the moment KLON of the area AbNK will be equal to [SVG 546] or [SVG 547].",
     "dipende_da": [
      "Libro II, Lemma II"
     ],
     "figura": {
      "mostra": [
       "L",
       "O",
       "KL",
       "area KLON"
      ],
      "evidenzia": [
       "KL = 2BP×PQ/Z",
       "KLON = BP×PQ×BD³/(2Z×CK×AB)"
      ]
     },
     "nota": "Motte: «AP² × 2BAP» (segno errato) e, in SVG 547, BD² per BD³ (errore di Motte 1846). SVG 543–547."
    },
    {
     "id": "L2-P14-p6",
     "la": "",
     "it": "Caso 1. Ora, se il corpo sale, e la gravità è come AB²+BD², essendo BET un cerchio (nella prima figura), la linea AC, che è proporzionale alla gravità, sarà (AB²+BD²)/Z, e DP², ossia AP²+2BAP+AB²+BD², sarà AK×Z+AC×Z, ossia CK×Z; e perciò l’area DTV starà all’area DPQ come DT², o DB², sta a CK×Z.",
     "en": "CASE 1. Now if the body ascends, and the gravity be as AB2 + BD2 BET being a circle, the line AC, which is proportional to the gravity, will be [SVG 548], and DP2 or AP2 + 2BAP + AB2 + BD2 will be AK × Z + AC × Z or CK × Z; and therefore the area DTV will be to the area DPQ as DT2 or DB2 to CK × Z.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio BET",
       "CK = AC + AK"
      ],
      "evidenzia": [
       "DP² = CK×Z"
      ]
     }
    },
    {
     "id": "L2-P14-p7",
     "la": "",
     "it": "Caso 2. Se invece il corpo sale, e la gravità è come AB²−BD², la linea AC (nella seconda figura) sarà (AB²−BD²)/Z, e DT² starà a DP² come DF², ossia DB², sta a BP²−BD², ossia ad AP²+2BAP+AB²−BD², cioè ad AK×Z+AC×Z, ossia a CK×Z.",
     "en": "CASE 2. If the body ascends, and the gravity be as AB2 - BD2, the line AC will be [SVG 549], and DT2 will be to DP2 as DF2 or DB2 to BP2 - BD2 or AP2 + 2BAP + AB2 - BD2, that is, to AK × Z + AC × Z or CK × Z.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "iperbole FTVE"
      ],
      "evidenzia": [
       "BP² − BD² = CK×Z"
      ]
     }
    },
    {
     "id": "L2-P14-p8",
     "la": "",
     "it": "E perciò l’area DTV starà all’area DPQ come DB² sta a CK×Z.",
     "en": "And therefore the area DTV will be to the area DPQ as DB2 to CK × Z.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "settore DTV",
       "triangolo DPQ"
      ]
     }
    },
    {
     "id": "L2-P14-p9",
     "la": "",
     "it": "Caso 3. E con lo stesso argomento, se il corpo scende, e perciò la gravità è come BD²−AB², e la linea AC (nella terza figura) è uguale a (BD²−AB²)/Z, l’area DTV starà all’area DPQ come DB² sta a CK×Z, come sopra.",
     "en": "CASE 3. And by the same reasoning, if the body descends, and therefore the gravity is as BD2 - AB2, and the line AC becomes equal to [SVG 550]; the area DTV will be to the area DPQ as DB2 to CK × Z: as above.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "iperbole BETV",
       "CK = AC − AK"
      ]
     }
    },
    {
     "id": "L2-P14-p10",
     "la": "",
     "it": "Poiché dunque quelle aree sono sempre in questo rapporto, se al posto dell’area DTV, con cui è rappresentato il momento del tempo, sempre uguale a sé stesso, si scrive un rettangolo determinato qualsiasi, per esempio BD×m, l’area DPQ, cioè ½BD×PQ, starà a BD×m come CK×Z sta a BD².",
     "en": "Since, therefore, these areas are always in this ratio, if for the area DTV, by which the moment of the time, always equal to itself, is expressed, there be put any determinate rectangle, as BD × m, the area DPQ, that is, [SVG 551], will be to BD × m as CK × Z to BD2.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "DTV = BD×m",
       "DPQ = ½BD×PQ"
      ]
     }
    },
    {
     "id": "L2-P14-p11",
     "la": "",
     "it": "E di qui PQ×BD³ risulta uguale a 2BD×m×CK×Z, e il momento KLON dell’area AbNK, trovato sopra, diventa BP×BD×m/AB.",
     "en": "And thence PQ × BD3 becomes equal to 2BD × m × CK × Z, and the moment KLON of the area AbNK, found before, becomes [SVG 552].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area KLON"
      ],
      "evidenzia": [
       "KLON = BP×BD×m/AB"
      ]
     }
    },
    {
     "id": "L2-P14-p12",
     "la": "",
     "it": "Si tolga il momento DTV dell’area DET, ossia BD×m, e resterà AP×BD×m/AB.",
     "en": "From the area DET subduct its moment DTV or BD × m, and there will remain [SVG 553].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "KLON − DTV"
      ],
      "evidenzia": [
       "KLON − DTV = AP×BD×m/AB"
      ]
     },
     "nota": "«æreae» refuso probabile per «areæ». Motte fraintende: il momento DTV si toglie da KLON, non dall’area DET."
    },
    {
     "id": "L2-P14-p13",
     "la": "",
     "it": "La differenza dei momenti, cioè il momento della differenza delle aree, è dunque uguale ad AP×BD×m/AB; e perciò, essendo dato BD×m/AB, è come la velocità AP, cioè come il momento dello spazio che il corpo descrive salendo o scendendo.",
     "en": "Therefore the difference of the moments, that is, the moment of the difference of the areas, is equal to [SVG 554]; and therefore [SVG 555] as the velocity AP; that is, as the moment of the space which the body describes in its ascent or descent.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "AP"
      ],
      "evidenzia": [
       "momento di (AbNK − DET) ∝ AP"
      ]
     }
    },
    {
     "id": "L2-P14-p14",
     "la": "",
     "it": "E quindi la differenza delle aree e quello spazio, che crescono o decrescono per momenti proporzionali e cominciano insieme o svaniscono insieme, sono proporzionali. C.V.D.",
     "en": "And therefore the difference of the areas, and that space, increasing or decreasing by proportional moments, and beginning together or vanishing together, are proportional. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "AbNK − DET",
       "spazio percorso"
      ],
      "evidenzia": [
       "spazio ∝ AbNK − DET"
      ]
     },
     "nota": "La trascrizione spezza «crescen ‹273› tia»."
    }
   ]
  },
  {
   "id": "L2-P14-Cor",
   "tipo": "Corollarium",
   "titolo": "Prop. XIV, Cor. — confronto con la caduta nel vuoto",
   "copertura": [
    "II.S3.28",
    "II.S3.29"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente"
   },
   "enunciato": {
    "la": "",
    "it": "Se la lunghezza che si ottiene dividendo l’area DET per la linea ED [il calcolo che segue richiede BD] si chiama M, e si prende un’altra lunghezza V che stia alla lunghezza M nel rapporto che la linea DA ha con la linea DE, lo spazio che il corpo descrive in un mezzo resistente nell’intera salita o discesa starà allo spazio che il corpo, cadendo dalla quiete, può descrivere nello stesso tempo in un mezzo non resistente, come la differenza delle aree suddette sta a BD×V²/AB; e quindi è dato a partire dal tempo dato.",
    "en": "If the length, which arises by applying the area DET to the line BD, be called M; and another length V be taken in that ratio to the length M, which the line DA has to the line DE; the space which a body, in a resisting medium, describes in its whole ascent or descent, will be to the space which a body, in a non-resisting medium, falling from rest, can describe in the same time, as the difference of the aforesaid areas to [SVG 556]; and therefore is given from the time given."
   },
   "figura_base": {
    "punti": [
     "D",
     "A",
     "E",
     "T",
     "B",
     "P"
    ],
    "vincoli": [
     "figure della Prop. XIV",
     "M = DET/BD (il latino ha ED; apparato A.4)",
     "V : M = DA : DE",
     "momento di M = m"
    ]
   },
   "passi": [
    {
     "id": "L2-P14-Cor-p1",
     "la": "",
     "it": "Se la lunghezza che si ottiene dividendo l’area DET per la linea ED [il calcolo che segue richiede BD] si chiama M, e si prende un’altra lunghezza V che stia alla lunghezza M nel rapporto che la linea DA ha con la linea DE, lo spazio che il corpo descrive in un mezzo resistente nell’intera salita o discesa starà allo spazio che il corpo, cadendo dalla quiete, può descrivere nello stesso tempo in un mezzo non resistente, come la differenza delle aree suddette sta a BD×V²/AB; e quindi è dato a partire dal tempo dato.",
     "en": "COR. If the length, which arises by applying the area DET to the line BD, be called M; and another length V be taken in that ratio to the length M, which the line DA has to the line DE; the space which a body, in a resisting medium, describes in its whole ascent or descent, will be to the space which a body, in a non-resisting medium, falling from rest, can describe in the same time, as the difference of the aforesaid areas to [SVG 556]; and therefore is given from the time given.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "M",
       "V"
      ],
      "evidenzia": [
       "spazio resistente : spazio nel vuoto = (AbNK − DET) : BD×V²/AB"
      ]
     },
     "nota": "Latino «ad lineam ED», Motte «BD»: il calcolo richiede BD."
    },
    {
     "id": "L2-P14-Cor-p2",
     "la": "",
     "it": "Infatti lo spazio in un mezzo non resistente è in rapporto duplicato del tempo, ossia come V²; e, essendo dati BD e AB, come BD×V²/AB.",
     "en": "For the space in a non-resisting medium is in a duplicate ratio of the time, or as V2; and, because BD and AB are given, as [SVG 556].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "V"
      ],
      "evidenzia": [
       "V ∝ tempo"
      ]
     }
    },
    {
     "id": "L2-P14-Cor-p3",
     "la": "",
     "it": "Quest’area è uguale all’area DA²×BD×M²/(DE²×AB), e il momento di M è m; e perciò il momento di quest’area è DA²×BD×2M×m/(DE²×AB).",
     "en": "This area is equal to the area [SVG 557] and the moment of M is m; and therefore the moment of this area is [SVG 558].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "M",
       "m"
      ],
      "evidenzia": [
       "d(M²) = 2M×m"
      ]
     }
    },
    {
     "id": "L2-P14-Cor-p4",
     "la": "",
     "it": "Ora questo momento sta al momento della differenza delle aree suddette DET e AbNK, cioè ad AP×BD×m/AB, come DA²×BD×M/DE² sta a ½BD×AP, ossia come DA²/DE² moltiplicato per DET sta a DAP; e quindi, quando le aree DET e DAP sono piccolissime, in rapporto di uguaglianza.",
     "en": "But this moment is to the moment of the difference of the aforesaid areas DET and AbNK, viz., to [SVG 559], as[SVG 560] to [SVG 561], or as [SVG 562] into DET to DAP; and, therefore, when the areas DET and DAP are least, in the ratio of equality.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "settore DET",
       "triangolo DAP"
      ],
      "evidenzia": [
       "(DA²/DE²)×DET : DAP → 1"
      ]
     }
    },
    {
     "id": "L2-P14-Cor-p5",
     "la": "",
     "it": "Dunque l’area BD×V²/AB e la differenza delle aree DET e AbNK, quando tutte queste aree sono piccolissime, hanno momenti uguali; e perciò sono uguali.",
     "en": "Therefore the area [SVG 563] and the difference of the areas DET and AbNK, when all these areas are least, have equal moments; and are therefore equal.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "BD×V²/AB",
       "AbNK − DET"
      ]
     }
    },
    {
     "id": "L2-P14-Cor-p6",
     "la": "",
     "it": "Di qui, poiché le velocità, e perciò anche gli spazi descritti nello stesso tempo nei due mezzi, all’inizio della discesa o alla fine della salita si avvicinano all’uguaglianza, e quindi stanno allora fra loro come l’area BD×V²/AB e la differenza delle aree DET e AbNK; e poiché inoltre lo spazio nel mezzo non resistente è continuamente come BD×V²/AB, e lo spazio nel mezzo resistente è continuamente come la differenza delle aree DET e AbNK; è necessario che gli spazi descritti nei due mezzi in tempi uguali qualsiasi stiano fra loro come quell’area BD×V²/AB e la differenza delle aree DET e AbNK. C.V.D.",
     "en": "Therefore since the velocities, and therefore also the spaces in both mediums described together, in the beginning of the descent, or the end of the ascent, approach to equality, and therefore are then one to another as the area [SVG 564], and the difference of the areas DET and AbNK; and moreover since the space, in a non-resisting medium, is perpetually as [SVG 556], and the space, in a resisting medium, is perpetually as the difference of the areas DET and AbNK; it necessarily follows, that the spaces, in both mediums, described in any equal times, are one to another as that area [SVG 556], and the difference of the areas DET and AbNK. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "spazi nei due mezzi"
      ],
      "evidenzia": [
       "rapporto costante"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-Lem3",
   "tipo": "Lemma",
   "titolo": "Lemma III — la spirale equiangola: PQ² = TQ×2PS al limite",
   "copertura": [
    "II.S4.01",
    "II.S4.02",
    "II.S4.03"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente"
   },
   "enunciato": {
    "la": "",
    "it": "Sia PQR una spirale che tagli tutti i raggi SP, SQ, SR, ecc. sotto angoli uguali. Si conduca la retta PT, che la tocchi in un punto qualsiasi P e tagli il raggio SQ in T; e, innalzate sulla spirale le perpendicolari PO, QO, che concorrono in O, si congiunga SO. Dico che, se i punti P e Q si avvicinano l’uno all’altro e si riuniscono, l’angolo PSO diventerà retto, e il rapporto ultimo del rettangolo TQ×2PS a PQ² sarà il rapporto di uguaglianza.",
    "en": "Let PQR be a spiral cutting all the radii SP, SQ, SR, &c., in equal angles. Draw the right line PT touching the spiral in any point P, and cutting the radius SQ in T; draw PO, QO perpendicular to the spiral, and meeting in O, and join SO. I say, that if the points P and Q approach and coincide, the angle PSO will become a right angle, and the ultimate ratio of the rectangle TQ × 2PS to PQ2 will be the ratio of equality."
   },
   "figura_base": {
    "punti": [
     "S",
     "P",
     "Q",
     "R",
     "T",
     "O",
     "D",
     "E"
    ],
    "vincoli": [
     "PQR spirale equiangola di centro S",
     "PT tangente in P, T sul raggio SQ",
     "PO, QO normali alla spirale, concorrenti in O",
     "QD, SE perpendicolari a OP"
    ]
   },
   "passi": [
    {
     "id": "L2-Lem3-p1",
     "la": "",
     "it": "Infatti dagli angoli retti OPQ, OQR si sottraggano gli angoli uguali SPQ, SQR, e resteranno uguali gli angoli OPS, OQS.",
     "en": "For from the right angles OPQ, OQR, subduct the equal angles SPQ, SQR, and there will remain the equal angles OPS, OQS.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "S",
       "P",
       "Q",
       "R",
       "O",
       "PO",
       "QO"
      ],
      "evidenzia": [
       "angolo OPS = angolo OQS"
      ]
     }
    },
    {
     "id": "L2-Lem3-p2",
     "la": "",
     "it": "Dunque il cerchio che passa per i punti O, S, P passerà anche per il punto Q.",
     "en": "Therefore a circle which passes through the points OSP will pass also through the point Q.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio per O, S, P, Q"
      ]
     }
    },
    {
     "id": "L2-Lem3-p3",
     "la": "",
     "it": "Si riuniscano i punti P e Q: questo cerchio, nel luogo PQ della loro riunione, toccherà la spirale, e quindi taglierà perpendicolarmente la retta OP.",
     "en": "Let the points P and Q coincide, and this circle will touch the spiral in the place of coincidence PQ, and will therefore cut the right line OP perpendicularly.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Q → P"
      ],
      "evidenzia": [
       "cerchio tangente alla spirale in P"
      ]
     }
    },
    {
     "id": "L2-Lem3-p4",
     "la": "",
     "it": "OP diventerà dunque un diametro di questo cerchio, e l’angolo OSP, nel semicerchio, sarà retto. C.V.D.",
     "en": "Therefore OP will become a diameter of this circle, and the angle OSP, being in a semi-circle, becomes a right one. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "diametro OP"
      ],
      "evidenzia": [
       "angolo OSP retto"
      ]
     }
    },
    {
     "id": "L2-Lem3-p5",
     "la": "",
     "it": "Su OP si abbassino le perpendicolari QD, SE, e i rapporti ultimi delle linee saranno di questo genere: TQ sta a PD come TS, o PS, sta a PE, ossia come 2PO sta a 2PS; inoltre PD sta a PQ come PQ sta a 2PO; e, per uguaglianza perturbata, TQ sta a PQ come PQ sta a 2PS.",
     "en": "Draw QD, SE perpendicular to OP, and the ultimate ratios of the lines will be as follows: TQ to PD as TS or PS to PE, or 2PO to 2PS; and PD to PQ as PQ to 2PO; and, ex æquo perturbatè, to TQ to PQ as PQ to 2PS.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "D",
       "E",
       "QD",
       "SE",
       "T",
       "TQ"
      ],
      "evidenzia": [
       "TQ : PD = PO : PS",
       "PD : PQ = PQ : 2PO"
      ]
     },
     "nota": "Motte: «to TQ to PQ» (refuso dell’edizione 1846)."
    },
    {
     "id": "L2-Lem3-p6",
     "la": "",
     "it": "Di qui PQ² risulta uguale a TQ×2PS. C.V.D.",
     "en": "Whence PQ2 becomes equal to TQ × 2PS. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "TQ",
       "PQ"
      ],
      "evidenzia": [
       "PQ² = TQ×2PS (al limite)"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P15",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XV — la spirale in un mezzo di densità inversamente come la distanza",
   "copertura": [
    "II.S4.04",
    "II.S4.05",
    "II.S4.06",
    "II.S4.07",
    "II.S4.08"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente"
   },
   "enunciato": {
    "la": "",
    "it": "Se la densità del mezzo nei singoli luoghi è inversamente come la distanza dei luoghi da un centro immobile, e la forza centripeta è in rapporto duplicato della densità, dico che il corpo può girare in una spirale che interseca sotto un angolo dato tutti i raggi condotti da quel centro.",
    "en": "If the density of a medium in each place thereof be reciprocally as the distance of the places from an immovable centre, and the centripetal force be in the duplicate ratio of the density; I say, that a body may revolve in a spiral which cuts all the radii drawn from that centre in a given angle."
   },
   "figura_base": {
    "punti": [
     "S",
     "P",
     "Q",
     "R",
     "r",
     "T",
     "O",
     "V"
    ],
    "vincoli": [
     "figura del Lemma III",
     "V su SQ prolungato, SV = SP",
     "PQ, PR archi descritti in tempi t e 2t",
     "area QSr = area PSQ; Rr = difetto d'arco dovuto alla resistenza"
    ]
   },
   "passi": [
    {
     "id": "L2-P15-p1",
     "la": "",
     "it": "Si pongano le stesse cose del lemma precedente, e si prolunghi SQ fino a V, in modo che SV sia uguale a SP.",
     "en": "Suppose every thing to be as in the foregoing Lemma, and produce SQ to V so that SV may be equal to SP.",
     "dipende_da": [
      "Libro II, Lemma III"
     ],
     "figura": {
      "mostra": [
       "S",
       "P",
       "Q",
       "T",
       "O",
       "V",
       "SV = SP"
      ]
     }
    },
    {
     "id": "L2-P15-p2",
     "la": "",
     "it": "In un tempo qualsiasi, in un mezzo resistente, il corpo descriva l’arco piccolissimo PQ, e in un tempo doppio l’arco piccolissimo PR; e i decrementi di questi archi dovuti alla resistenza, ossia i difetti rispetto agli archi che sarebbero descritti negli stessi tempi in un mezzo non resistente, staranno fra loro come i quadrati dei tempi in cui sono generati.",
     "en": "In any time let a body, in a resisting medium, describe the least arc PQ, and in double the time the least arc PR; and the decrements of those arcs arising from the resistance, or their differences from the arcs which would be described in a non-resisting medium in the same times, will be to each other as the squares of the times in which they are generated;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "arco PQ",
       "arco PR",
       "R"
      ],
      "evidenzia": [
       "difetti d'arco ∝ t²"
      ]
     }
    },
    {
     "id": "L2-P15-p3",
     "la": "",
     "it": "Il decremento dell’arco PQ è dunque la quarta parte del decremento dell’arco PR.",
     "en": "therefore the decrement of the arc PQ, is the fourth part of the decrement of the arc PR.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "arco PQ",
       "arco PR"
      ]
     }
    },
    {
     "id": "L2-P15-p4",
     "la": "",
     "it": "Di qui, anche, se si prende l’area QSr uguale all’area PSQ, il decremento dell’arco PQ sarà uguale alla metà della lineetta Rr; e quindi la forza di resistenza e la forza centripeta stanno fra loro come le lineette ½Rr e TQ, che esse generano nello stesso tempo.",
     "en": "Whence also if the area QSr be taken equal to the area PSQ, the decrement of the arc PQ will be equal to half the lineola Rr; and therefore the force of resistance and the centripetal force are to each other as the lineola [SVG 565] and TQ which they generate in the same time.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "r",
       "area QSr = area PSQ",
       "Rr",
       "TQ"
      ],
      "evidenzia": [
       "resistenza : forza centripeta = ½Rr : TQ"
      ]
     },
     "nota": "«capitaur» refuso probabile per «capiatur»."
    },
    {
     "id": "L2-P15-p5",
     "la": "",
     "it": "Poiché la forza centripeta da cui il corpo è sollecitato in P è inversamente come SP², e (per il Lemma X del Libro I) la lineetta TQ, che è generata da quella forza, è nel rapporto composto del rapporto di questa forza e del rapporto duplicato del tempo in cui è descritto l’arco PQ (trascuro infatti in questo caso la resistenza, come infinitamente minore della forza centripeta), TQ×SP², cioè (per l’ultimo lemma) ½PQ²×SP, sarà in rapporto duplicato del tempo; e quindi il tempo è come PQ×√SP, e la velocità del corpo con cui in quel tempo è descritto l’arco PQ è come PQ/(PQ×√SP), ossia 1/√SP, cioè inversamente in rapporto subduplicato di SP.",
     "en": "Because the centripetal force with which the body is urged in P is reciprocally as SP2, and (by Lem. X, Book I) the lineola TQ, which is generated by that force, is in a ratio compounded of the ratio of this force and the duplicate ratio of the time in which the arc PQ is described (for in this case I neglect the resistance, as being infinitely less than the centripetal force), it follows that TQ × SP2, that is (by the last Lemma), [SVG 566], will be in a duplicate ratio of the time, and therefore the time is as [SVG 567]; and the velocity of the body, with which the arc PQ is described in that time, as [SVG 568] or [SVG 569], that is, in the subduplicate ratio of SP reciprocally.",
     "dipende_da": [
      "Libro I, Lemma X",
      "Libro II, Lemma III"
     ],
     "figura": {
      "mostra": [
       "TQ"
      ],
      "evidenzia": [
       "TQ×SP² = ½PQ²×SP ∝ t²",
       "v ∝ 1/√SP"
      ]
     },
     "nota": "Radicali perduti nella trascrizione: «PQ×SP» = PQ×√SP, «1SP» = 1/√SP; le formule di Motte (SVG 566–569) hanno la radice. Il Lemma X regge tramite il suo Cor. 3."
    },
    {
     "id": "L2-P15-p6",
     "la": "",
     "it": "E con un argomento simile la velocità con cui è descritto l’arco QR è inversamente in rapporto subduplicato di SQ.",
     "en": "And, by a like reasoning, the velocity with which the arc QR is described, is in the subduplicate ratio of SQ reciprocally.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "arco QR"
      ]
     }
    },
    {
     "id": "L2-P15-p7",
     "la": "",
     "it": "Ora quegli archi PQ e QR stanno fra loro come le velocità con cui sono descritti, cioè in rapporto subduplicato di SQ a SP, ossia come SQ sta a √(SP×SQ); e, per gli angoli uguali SPQ, SQr e le aree uguali PSQ, QSr, l’arco PQ sta all’arco Qr come SQ sta a SP.",
     "en": "Now those arcs PQ and QR are as the describing velocities to each other; that is, in the subduplicate ratio of SQ to SP, or as SQ to [SVG 570]; and, because of the equal angles SPQ, SQr, and the equal areas PSQ, QSr, the arc PQ is to the arc Qr as SQ to SP.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "arco Qr"
      ],
      "evidenzia": [
       "PQ : QR = SQ : √(SP×SQ)",
       "PQ : Qr = SQ : SP"
      ]
     }
    },
    {
     "id": "L2-P15-p8",
     "la": "",
     "it": "Si prendano le differenze dei conseguenti proporzionali, e l’arco PQ starà all’arco Rr come SQ sta a SP−√(SP×SQ), ossia a ½VQ.",
     "en": "Take the differences of the proportional consequents, and the arc PQ will be to the arc Rr as SQ to [SVG 571], or [SVG 572].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Rr",
       "VQ"
      ],
      "evidenzia": [
       "PQ : Rr = SQ : ½VQ"
      ]
     }
    },
    {
     "id": "L2-P15-p9",
     "la": "",
     "it": "Infatti, quando i punti P e Q si riuniscono, il rapporto ultimo di SP−√(SP×SQ) a ½VQ è di uguaglianza.",
     "en": "For the points P and Q coinciding, the ultimate ratio of [SVG 573] to [SVG 572] is the ratio of equality.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "VQ"
      ]
     }
    },
    {
     "id": "L2-P15-p10",
     "la": "",
     "it": "Poiché il decremento dell’arco PQ dovuto alla resistenza, ossia il suo doppio Rr, è come la resistenza e il quadrato del tempo considerati congiuntamente, la resistenza sarà come Rr/(PQ²×SP).",
     "en": "Because the decrement of the arc PQ arising from the resistance, or its double Rr, is as the resistance and the square of the time conjunctly, the resistance will be as [SVG 574].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Rr"
      ],
      "evidenzia": [
       "resistenza ∝ Rr/t² ∝ Rr/(PQ²×SP)"
      ]
     }
    },
    {
     "id": "L2-P15-p11",
     "la": "",
     "it": "Ma PQ stava a Rr come SQ sta a ½VQ, e di qui Rr/(PQ²×SP) diventa come ½VQ/(PQ×SP×SQ), ossia come ½OS/(OP×SP²).",
     "en": "But PQ was to Rr as SQ to [SVG 572], and thence [SVG 574] becomes as [SVG 575], or as [SVG 576].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "OS",
       "OP"
      ]
     }
    },
    {
     "id": "L2-P15-p12",
     "la": "",
     "it": "Infatti, quando i punti P e Q si riuniscono, SP e SQ coincidono, e l’angolo PVQ diventa retto; e, per la similitudine dei triangoli PVQ, PSO, PQ sta a ½VQ come OP sta a ½OS.",
     "en": "For the points P and Q coinciding, SP and SQ coincide also, and the angle PVQ becomes a right one; and, because of the similar triangles PVQ, PSO, PQ becomes to [SVG 572] as OP to [SVG 577].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangolo PVQ",
       "triangolo PSO"
      ],
      "evidenzia": [
       "PVQ ~ PSO"
      ]
     }
    },
    {
     "id": "L2-P15-p13",
     "la": "",
     "it": "Dunque OS/(OP×SP²) è come la resistenza, cioè nel rapporto della densità del mezzo in P e nel rapporto duplicato della velocità considerati congiuntamente.",
     "en": "Therefore [SVG 578] is as the resistance, that is, in the ratio of the density of the medium in P and the duplicate ratio of the velocity conjunctly.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "P"
      ],
      "evidenzia": [
       "resistenza ∝ densità × v²"
      ]
     }
    },
    {
     "id": "L2-P15-p14",
     "la": "",
     "it": "Si tolga il rapporto duplicato della velocità, cioè il rapporto 1/SP, e resterà la densità del mezzo in P come OS/(OP×SP).",
     "en": "Subduct the duplicate ratio of the velocity, namely, the ratio [SVG 579], and there will remain the density of the medium in P, as [SVG 580].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "P"
      ],
      "evidenzia": [
       "densità ∝ OS/(OP×SP)"
      ]
     }
    },
    {
     "id": "L2-P15-p15",
     "la": "",
     "it": "Sia data la spirale: poiché è dato il rapporto di OS a OP, la densità del mezzo in P sarà come 1/SP.",
     "en": "Let the spiral be given, and, because of the given ratio of OS to OP, the density of the medium in P will be as [SVG 579].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "spirale"
      ],
      "evidenzia": [
       "OS : OP costante; densità ∝ 1/SP"
      ]
     }
    },
    {
     "id": "L2-P15-p16",
     "la": "",
     "it": "Dunque in un mezzo la cui densità è inversamente come la distanza SP dal centro il corpo può girare in questa spirale. C.V.D.",
     "en": "Therefore in a medium whose density is reciprocally as SP the distance from the centre, a body will revolve in this spiral. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "spirale PQR"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P16",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XVI — la stessa spirale, con forza inversamente come una potenza qualsiasi della distanza",
   "copertura": [
    "II.S4.18",
    "II.S4.19"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente"
   },
   "enunciato": {
    "la": "",
    "it": "Se la densità del mezzo nei singoli luoghi è inversamente come la distanza dei luoghi da un centro immobile, e la forza centripeta è inversamente come una potenza qualsiasi della stessa distanza, dico che il corpo può girare in una spirale che interseca sotto un angolo dato tutti i raggi condotti da quel centro.",
    "en": "If the density of the medium in each of the places be reciprocally as the distance of the places from the immoveable centre, and the centripetal force be reciprocally as any power of the same distance, I say, that the body may revolve in a spiral intersecting all the radii drawn from that centre in a given angle."
   },
   "figura_base": {
    "punti": [
     "S",
     "P",
     "Q",
     "R",
     "r",
     "T",
     "O",
     "V"
    ],
    "vincoli": [
     "figura della Prop. XV",
     "forza centripeta ∝ 1/SPⁿ⁺¹"
    ]
   },
   "passi": [
    {
     "id": "L2-P16-p1",
     "la": "",
     "it": "Si dimostra con lo stesso metodo della proposizione precedente.",
     "en": "This is demonstrated in the same manner as the foregoing Proposition.",
     "dipende_da": [
      "Libro II, Prop. XV"
     ],
     "figura": {
      "mostra": [
       "figura della Prop. XV"
      ]
     }
    },
    {
     "id": "L2-P16-p2",
     "la": "",
     "it": "Infatti, se la forza centripeta in P è inversamente come una potenza qualsiasi SPⁿ⁺¹ della distanza SP, il cui indice è n+1, si ricaverà come sopra che il tempo in cui il corpo descrive un arco qualsiasi PQ sarà come PQ×SP^(½n); e la resistenza in P come Rr/(PQ²×SPⁿ), ossia come (1−½n)×VQ/(PQ×SPⁿ×SQ), e quindi come (1−½n)×OS/(OP×SPⁿ⁺¹), cioè, essendo dato (1−½n)×OS/OP, inversamente come SPⁿ⁺¹.",
     "en": "For if the centripetal force in P be reciprocally as any power [SVG 591] of the distance SP whose index is n + 1; it will be collected, as above, that the time in which the body describes any arc PQ, will be as [SVG 592]; and the resistance in P as [SVG 593], or as [SVG 594], and therefore as [SVG 595], that is, [SVG 596] is a given quantity), reciprocally as [SVG 591].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Rr",
       "VQ",
       "OS",
       "OP"
      ],
      "evidenzia": [
       "resistenza ∝ (1−½n)×OS/(OP×SPⁿ⁺¹)"
      ]
     },
     "nota": "Esponenti appiattiti: «SPn+1» = SPⁿ⁺¹, «SP12n» = SP^(½n). Motte (SVG 592) scrive PS^(½n)."
    },
    {
     "id": "L2-P16-p3",
     "la": "",
     "it": "E perciò, poiché la velocità è inversamente come SP^(½n), la densità in P sarà inversamente come SP.",
     "en": "And therefore, since the velocity is reciprocally as [SVG 597], the density in P will be reciprocally as SP.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "P"
      ],
      "evidenzia": [
       "densità ∝ resistenza/v² ∝ 1/SP"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P17",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XVII — dalla spirale e dalla legge della velocità alla forza e alla resistenza",
   "copertura": [
    "II.S4.24",
    "II.S4.25"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare sia la forza centripeta sia la resistenza del mezzo per cui un corpo può ruotare in una spirale data, con una legge data della velocità.",
    "en": "To find the centripetal force and the resisting force of the medium, by which a body, the law of the velocity being given, shall revolve in a given spiral."
   },
   "figura_base": {
    "punti": [
     "S",
     "P",
     "Q",
     "R",
     "r",
     "T"
    ],
    "vincoli": [
     "spirale data PQR di centro S",
     "PQ, QR archi descritti in particelle uguali di tempo",
     "area QSr = area PSQ; RSr differenza delle aree"
    ]
   },
   "passi": [
    {
     "id": "L2-P17-p1",
     "la": "",
     "it": "Sia PQR quella spirale.",
     "en": "Let that spiral be PQR.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "S",
       "spirale PQR"
      ]
     }
    },
    {
     "id": "L2-P17-p2",
     "la": "",
     "it": "Dalla velocità con cui il corpo percorre l’arco piccolissimo PQ sarà dato il tempo, e dall’altezza TQ, che è come la forza centripeta e il quadrato del tempo, sarà data la forza.",
     "en": "From the velocity, with which the body goes over the very small arc PQ, the time will be given; and from the altitude TQ, which is as the centripetal force, and the square of the time, that force will be given.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "arco PQ",
       "T",
       "TQ"
      ],
      "evidenzia": [
       "TQ ∝ forza × t²"
      ]
     }
    },
    {
     "id": "L2-P17-p3",
     "la": "",
     "it": "Poi dalla differenza RSr delle aree PSQ e QSR, compiute in particelle uguali di tempo, sarà dato il ritardo del corpo, e dal ritardo si troveranno la resistenza e la densità del mezzo.",
     "en": "Then from the difference RSr of the areas PSQ and QSR described in equal particles of time, the retardation of the body will be given; and from the retardation will be found the resisting force and density of the medium.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area PSQ",
       "area QSR",
       "r",
       "area RSr"
      ],
      "evidenzia": [
       "RSr misura il ritardo"
      ]
     }
    }
   ]
  }
 ]
}
```

**Fine del Fascicolo 15.**
