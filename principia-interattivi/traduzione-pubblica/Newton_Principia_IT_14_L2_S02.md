> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 14 — Libro II, Sezione II: il moto dei corpi che incontrano una resistenza in rapporto duplicato delle velocità

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo prosegue il Fascicolo 13 (Libro II, Sezione I). Traduce integralmente la **Sezione II** del Libro II, *De motu corporum quibus resistitur in duplicata ratione velocitatum*: le Proposizioni V–X con tutti i corollari, il **Lemma II** (i momenti) con il suo Scolio sulla lettera a Collins, i quattro esempi della Prop. X e lo Scolio finale con le otto regole e il capoverso sulle parabole. È una traduzione di lavoro, non un’edizione critica validata.

Gli identificatori **II.S2.01–II.S2.77** e i titoli tematici tra parentesi sono aggiunte editoriali. I numeri romani delle proposizioni, dei teoremi, dei problemi e del lemma, e i numeri dei corollari, dei casi, degli esempi e delle regole appartengono al testo originale. Le integrazioni del curatore sono tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton.

In coda al fascicolo c’è la **Parte B**, con i dati per 13 pagine interattive (116 passi): Prop. V e il suo Cor. 3; Prop. VI; Lemma II; Prop. VIII; Prop. IX e il suo Cor. 1; Prop. X con gli Esempi 1–4; Regola 8 dello Scolio.

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro II, Sezione II, **pp. 239–264** (i marcatori della trascrizione vanno da ‹240› a ‹264›; il titolo della Sezione e l’inizio della Prop. V sono a p. 239). Trascrizione normalizzata del Newton Project, documento **NATP00088**, estratta in testo semplice senza correzioni: `fonti/latino-1726-L2-S02.md`.
2. **Inglese di confronto.** *Newton’s Principia*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, Book II, Section II. Estratto: `fonti/motte-1846-L2-S02.md`. L’estratto non contiene marcatori di pagina: nelle tabelle si indica «sezione corrispondente». Le formule stampate come immagini (**SVG 372–535**, più 2, 223 e 342 riusate da sezioni precedenti) sono state controllate tutte sull’EPUB Gutenberg #76404 (`src_epub/OEBPS`), attraverso la tabella `svg_tex.tsv` (LaTeX dell’attributo `data-tex`) e la resa grafica con `rsvg-convert` per le formule del Lemma II, delle Propp. IX–X e per i casi dubbi.
3. **Brief comune**, **istruzioni del Libro II**, **Fascicoli 3 e 5** come modelli di formato.

Non ho consultato né riprodotto traduzioni moderne. Non ho potuto vedere la stampa del 1726 né le figure originali (NATP00088-8…24): le relazioni geometriche sono ricostruite dalle sole lettere del testo. Non ho consultato Motte 1729.

### Criteri di traduzione

- Il testo guida è il latino; Motte serve al confronto ed è annotato quando aggiunge, omette o sbaglia.
- Si applicano il glossario comune del brief e il glossario aggiuntivo del Libro II: *resistentia* «resistenza», *medium* «mezzo», *densitas* «densità», *momentum* «momento», *genita* «quantità generata», *in duplicata ratione velocitatis* «in rapporto duplicato della velocità», *vis insita* «forza insita», *medium uniforme / similare* «mezzo uniforme / omogeneo», *spatium non resistens / vacuum* «spazio non resistente / vuoto», *hyperbola* «iperbole», *asymptotos* «asintoto», *area hyperbolica* «area iperbolica», *progressio geometrica* «progressione geometrica», *gravitas specifica* «gravità specifica», *pondus* «peso», *globus* «globo», *Scholium* «Scolio»; *sagitta* «saetta»; *applicare ad* «dividere per»; *coire* «riunirsi»; *motus* come grandezza «quantità di moto»; *conjunctim* «considerati congiuntamente»; *exponens* «esponente» (grandezza che rappresenta); Q.E.D. «C.V.D.», Q.E.I. «C.V.T.».
- Le estensioni del glossario proprie di questo fascicolo sono nel § A.0.
- Gli enunciati all’infinito o al congiuntivo sono resi con l’indicativo; l’enunciato del problema (*Tendat … requiritur*) conserva il congiuntivo esortativo.
- **Formule.** Le abbreviazioni «ABq», «AB quad.», «APq» sono scritte AB², AP². Le frazioni appiattite dalla trascrizione sono rese con la barra (GH/T, S/(R√(1+QQ))); le radici, che la trascrizione perde sistematicamente, sono ripristinate con √ quando la matematica e la formula di Motte lo richiedono (elenco nel § A.10). Gli esponenti frazionari del Lemma II sono scritti A^(1/2), A^(m/n). Nessuna formula moderna entra nel testo tradotto: √ e le frazioni sono la notazione di Newton.
- *Divisim*, *vicissim*, *componendo / composite*, *ex æquo* sono resi «separando», «permutando», «componendo», «per uguaglianza».

---

## Traduzione italiana

### Sezione II. Il moto dei corpi che incontrano una resistenza in rapporto duplicato delle velocità

### Proposizione V. Teorema III (tempi in progressione geometrica, spazi uguali)

**[II.S2.01]** **Se un corpo incontra una resistenza in rapporto duplicato della velocità e si muove per la sola forza insita in un mezzo omogeneo, e se i tempi si prendono in progressione geometrica, procedendo dai termini minori ai maggiori, dico che le velocità all’inizio dei singoli tempi sono nella stessa progressione geometrica, inversamente, e che sono uguali gli spazi descritti nei singoli tempi.**

**[II.S2.02]** Infatti, poiché la resistenza del mezzo è proporzionale al quadrato della velocità e il decremento della velocità è proporzionale alla resistenza, se si divide il tempo in innumerevoli particelle uguali, i quadrati delle velocità all’inizio dei singoli tempi saranno proporzionali alle differenze delle velocità stesse. Siano AK, KL, LM, ecc. quelle particelle di tempo, prese sulla retta CD, e si innalzino le perpendicolari AB, Kk, Ll, Mm, ecc., che incontrino in B, k, l, m, ecc. l’iperbole BklmG, descritta con centro C e con gli asintoti ortogonali CD, CH: AB starà a Kk come CK sta a CA; e, separando, AB − Kk starà a Kk come AK sta a CA; e, permutando, AB − Kk starà ad AK come Kk sta a CA, e quindi come AB×Kk sta ad AB×CA. Di qui, poiché AK e AB×CA sono dati, AB − Kk sarà come AB×Kk; e alla fine, quando AB e Kk si riuniscono, come AB². E con un argomento simile Kk − Ll, Ll − Mm, ecc. saranno come Kk², Ll², ecc. Dunque i quadrati delle linee AB, Kk, Ll, Mm stanno come le loro differenze; e perciò, poiché anche i quadrati delle velocità stavano come le loro differenze, la progressione delle une e delle altre sarà simile. Dimostrato ciò, ne segue anche che le aree descritte da queste linee sono in una progressione del tutto simile a quella degli spazi descritti con le velocità. Dunque, se la velocità all’inizio del primo tempo AK si rappresenta con la linea AB, la velocità all’inizio del secondo, KL, con la linea Kk, e la lunghezza descritta nel primo tempo con l’area AKkB, tutte le velocità successive saranno rappresentate dalle linee successive Ll, Mm, ecc., e le lunghezze descritte dalle aree Kl, Lm, ecc. E, componendo, se il tempo intero si rappresenta con AM, somma delle sue parti, la lunghezza intera descritta sarà rappresentata da AMmB, somma delle sue parti. Immagina ora che il tempo AM sia diviso nelle parti AK, KL, LM, ecc. in modo che CA, CK, CL, CM, ecc. siano in progressione geometrica: quelle parti saranno nella stessa progressione, le velocità AB, Kk, Ll, Mm, ecc. nella stessa progressione inversa, e gli spazi descritti Ak, Kl, Lm, ecc. uguali. C.V.D.

**[II.S2.03]** *Cor. 1.* È dunque evidente che, se il tempo si rappresenta con una parte qualsiasi AD dell’asintoto e la velocità all’inizio del tempo con l’ordinata AB, la velocità alla fine del tempo sarà rappresentata dall’ordinata DG, e l’intero spazio descritto dall’area iperbolica adiacente ABGD; e così pure lo spazio che un corpo potrebbe descrivere nello stesso tempo AD, con la velocità iniziale AB, in un mezzo non resistente, dal rettangolo AB×AD.

**[II.S2.04]** *Cor. 2.* Di qui è dato lo spazio descritto nel mezzo resistente, prendendolo in modo che stia allo spazio che si potrebbe descrivere nello stesso tempo con la velocità uniforme AB in un mezzo non resistente come l’area iperbolica ABGD sta al rettangolo AB×AD.

**[II.S2.05]** *Cor. 3.* È data anche la resistenza del mezzo, stabilendo che proprio all’inizio del moto essa sia uguale alla forza centripeta uniforme che, in un corpo che cade in un mezzo non resistente, potrebbe generare nel tempo AC la velocità AB. Se infatti si conduce BT tangente all’iperbole in B, che incontri l’asintoto in T, la retta AT sarà uguale ad AC e rappresenterà il tempo nel quale la resistenza iniziale, continuata uniformemente, potrebbe togliere l’intera velocità AB.

**[II.S2.06]** *Cor. 4.* E di qui è data anche la proporzione di questa resistenza alla forza di gravità o a qualsiasi altra forza centripeta data.

**[II.S2.07]** *Cor. 5.* E, viceversa, se è data la proporzione della resistenza a una qualsiasi forza centripeta data, è dato il tempo AC nel quale una forza centripeta uguale alla resistenza potrebbe generare una velocità qualsiasi AB; e di qui è dato il punto B per il quale si deve descrivere l’iperbole di asintoti CH, CD; e così pure lo spazio ABGD che il corpo, cominciando il suo moto con quella velocità AB, può descrivere in un tempo qualsiasi AD in un mezzo omogeneo resistente.

### Proposizione VI. Teorema IV (globi uguali: tempi inversamente come le velocità)

**[II.S2.08]** **Corpi sferici omogenei e uguali, ostacolati da resistenze in rapporto duplicato delle velocità e mossi soltanto dalle forze insite, in tempi che sono inversamente come le velocità iniziali descrivono sempre spazi uguali e perdono parti delle velocità proporzionali alle velocità intere.**

**[II.S2.09]** Descritta con gli asintoti ortogonali CD, CH un’iperbole qualsiasi BbEe, che tagli in B, b, E, e le perpendicolari AB, ab, DE, de, si rappresentino le velocità iniziali con le perpendicolari AB, DE e i tempi con le linee Aa, Dd. Dunque Aa sta a Dd come (per ipotesi) DE sta ad AB, e come (per la natura dell’iperbole) CA sta a CD; e, componendo, come Ca sta a Cd. Dunque le aree ABba, DEed, cioè gli spazi descritti, sono uguali fra loro; e le velocità iniziali AB, DE sono proporzionali alle finali ab, de, e perciò, separando, anche alle loro parti perdute AB − ab, DE − de. C.V.D.

### Proposizione VII. Teorema V (tempi come le quantità di moto divise per le resistenze)

**[II.S2.10]** **Corpi sferici che incontrano una resistenza in rapporto duplicato delle velocità, in tempi che sono direttamente come le quantità di moto iniziali e inversamente come le resistenze iniziali, perderanno parti delle quantità di moto proporzionali alle intere e descriveranno spazi proporzionali a quei tempi e alle velocità iniziali considerati congiuntamente.**

**[II.S2.11]** Infatti le parti perdute delle quantità di moto stanno come le resistenze e i tempi considerati congiuntamente. Dunque, perché quelle parti siano proporzionali alle intere, la resistenza e il tempo considerati congiuntamente dovranno stare come la quantità di moto. Perciò il tempo starà direttamente come la quantità di moto e inversamente come la resistenza. Prendendo dunque le particelle dei tempi in quel rapporto, i corpi perderanno sempre particelle delle quantità di moto proporzionali alle intere, e quindi conserveranno velocità sempre proporzionali alle loro velocità iniziali. E, poiché il rapporto delle velocità è dato, descriveranno sempre spazi che stanno come le velocità iniziali e i tempi considerati congiuntamente. C.V.D.

**[II.S2.12]** *Cor. 1.* Dunque, se corpi ugualmente veloci incontrano una resistenza in rapporto duplicato dei diametri, globi omogenei mossi con velocità qualsiasi, descrivendo spazi proporzionali ai loro diametri, perderanno parti delle quantità di moto proporzionali alle intere. Infatti la quantità di moto di ciascun globo starà come la sua velocità e la sua massa considerate congiuntamente, cioè come la velocità e il cubo del diametro; la resistenza (per ipotesi) starà come il quadrato del diametro e il quadrato della velocità considerati congiuntamente; e il tempo (per questa proposizione) sta direttamente nel primo rapporto e inversamente nel secondo, cioè direttamente come il diametro e inversamente come la velocità; e perciò lo spazio, proporzionale al tempo e alla velocità, sta come il diametro.

**[II.S2.13]** *Cor. 2.* Se corpi ugualmente veloci incontrano una resistenza in rapporto sesquiplicato dei diametri, globi omogenei mossi con velocità qualsiasi, descrivendo spazi in rapporto sesquiplicato dei diametri, perderanno parti delle quantità di moto proporzionali alle intere.

**[II.S2.14]** *Cor. 3.* E in generale, se corpi ugualmente veloci incontrano una resistenza nel rapporto di una potenza qualsiasi dei diametri, gli spazi nei quali globi omogenei, mossi con velocità qualsiasi, perderanno parti delle quantità di moto proporzionali alle intere staranno come i cubi dei diametri divisi per quella potenza. Siano D ed E i diametri; e se le resistenze, quando le velocità si pongono uguali, stanno come Dⁿ ed Eⁿ, gli spazi nei quali i globi, mossi con velocità qualsiasi, perderanno parti delle quantità di moto proporzionali alle intere staranno come D³⁻ⁿ ed E³⁻ⁿ. E perciò globi omogenei, descrivendo spazi proporzionali a D³⁻ⁿ ed E³⁻ⁿ, conserveranno le velocità nello stesso rapporto fra loro che avevano all’inizio.

**[II.S2.15]** *Cor. 4.* Se poi i globi non sono omogenei, lo spazio descritto dal globo più denso deve essere aumentato nel rapporto della densità. Infatti la quantità di moto, a parità di velocità, è maggiore nel rapporto della densità; e il tempo (per questa proposizione) aumenta direttamente nel rapporto della quantità di moto, e lo spazio descritto nel rapporto del tempo.

**[II.S2.16]** *Cor. 5.* E se i globi si muovono in mezzi diversi, lo spazio, nel mezzo che a parità delle altre condizioni resiste di più, dovrà essere diminuito nel rapporto della resistenza maggiore. Infatti il tempo (per questa proposizione) diminuirà nel rapporto della resistenza aumentata, e lo spazio nel rapporto del tempo.

### Lemma II (il momento della quantità generata)

**[II.S2.17]** **Il momento di una quantità generata è uguale ai momenti dei singoli lati generanti moltiplicati successivamente per gli indici delle potenze di quei lati e per i loro coefficienti.**

**[II.S2.18]** Chiamo quantità generata ogni quantità che, senza addizione e sottrazione, si genera da lati o termini qualsiasi: in aritmetica per moltiplicazione, divisione ed estrazione di radici; in geometria per ritrovamento o di contenuti e di lati, o di estreme e di medie proporzionali. Quantità di questo genere sono i prodotti, i quozienti, le radici, i rettangoli, i quadrati, i cubi, i lati quadrati, i lati cubici e simili. Considero qui queste quantità come indeterminate e variabili, e quasi crescenti o decrescenti per un moto o flusso perpetuo; e con il nome di momenti intendo i loro incrementi o decrementi momentanei, in modo che gli incrementi si considerino momenti additivi o affermativi, e i decrementi momenti sottrattivi o negativi. Bada però di non intendere particelle finite. Le particelle finite non sono momenti, ma le quantità stesse generate dai momenti. Si devono intendere come i principi appena nascenti delle grandezze finite. In questo lemma, infatti, non si considera la grandezza dei momenti, ma la prima proporzione dei [momenti] nascenti. Torna allo stesso se al posto dei momenti si usano o le velocità degli incrementi e dei decrementi (che si possono chiamare anche moti, mutazioni e flussioni delle quantità), o quantità finite qualsiasi proporzionali a queste velocità. Il coefficiente di ciascun lato generante, poi, è la quantità che si ottiene dividendo la quantità generata per questo lato.

**[II.S2.19]** Il senso del lemma è dunque che, se i momenti di quantità qualsiasi A, B, C, ecc., crescenti o decrescenti con moto perpetuo, o le velocità delle mutazioni a essi proporzionali, si chiamano a, b, c, ecc., il momento o mutazione del rettangolo generato AB è aB + bA, e il momento del contenuto generato ABC è aBC + bAC + cAB; e i momenti delle potenze generate A², A³, A⁴, A^(1/2), A^(3/2), A^(1/3), A^(2/3), A⁻¹, A⁻² e A^(−1/2) sono rispettivamente 2aA, 3aA², 4aA³, ½aA^(−1/2), (3/2)aA^(1/2), (1/3)aA^(−2/3), (2/3)aA^(−1/3), −aA⁻², −2aA⁻³ e −½aA^(−3/2). E in generale, che il momento di una potenza qualsiasi A^(n/m) è (n/m)aA^((n−m)/m). Così pure, che il momento della quantità generata A²B è 2aAB + bA²; il momento della quantità generata A³B⁴C² è 3aA²B⁴C² + 4bA³B³C² + 2cA³B⁴C; e il momento della quantità generata A³/B², ossia A³B⁻², è 3aA²B⁻² − 2bA³B⁻³; e così negli altri casi. Il lemma si dimostra in questo modo.

**[II.S2.20]** *Caso 1.* Un rettangolo qualsiasi AB, accresciuto con moto perpetuo, quando ai lati A e B mancavano le metà dei momenti, ½a e ½b, era (A − ½a) per (B − ½b), ossia AB − ½aB − ½bA + ¼ab; e non appena i lati A e B sono stati accresciuti delle altre metà dei momenti, diventa (A + ½a) per (B + ½b), ossia AB + ½aB + ½bA + ¼ab. Da questo rettangolo si sottragga il rettangolo precedente, e resterà l’eccesso aB + bA. Dunque con gli incrementi interi a e b dei lati si genera l’incremento aB + bA del rettangolo. C.V.D.

**[II.S2.21]** *Caso 2.* Si ponga AB sempre uguale a G: il momento del contenuto ABC, ossia GC, sarà (per il Caso 1) gC + cG, cioè (se al posto di G e g si scrivono AB e aB + bA) aBC + bAC + cAB. E lo stesso ragionamento vale per il contenuto sotto un numero qualsiasi di lati. C.V.D.

**[II.S2.22]** *Caso 3.* Si pongano i lati A, B, C sempre uguali fra loro: il momento aB + bA di A², cioè del rettangolo AB, sarà 2aA, e il momento aBC + bAC + cAB di A³, cioè del contenuto ABC, sarà 3aA². E con lo stesso argomento il momento di una potenza qualsiasi Aⁿ è naAⁿ⁻¹. C.V.D.

**[II.S2.23]** *Caso 4.* Di qui, poiché 1/A per A fa 1, il momento di 1/A moltiplicato per A, insieme con 1/A moltiplicato per a, sarà il momento di 1, cioè nulla. Perciò il momento di 1/A, ossia di A⁻¹, è −a/A². E in generale, poiché 1/Aⁿ per Aⁿ fa 1, il momento di 1/Aⁿ moltiplicato per Aⁿ, insieme con 1/Aⁿ per naAⁿ⁻¹, sarà nulla. E perciò il momento di 1/Aⁿ, ossia di A⁻ⁿ, sarà −na/Aⁿ⁺¹. C.V.D.

**[II.S2.24]** *Caso 5.* E poiché A^(1/2) per A^(1/2) fa A, il momento di A^(1/2) moltiplicato per 2A^(1/2) sarà a, per il Caso 3; e perciò il momento di A^(1/2) sarà a/(2A^(1/2)), ossia ½aA^(−1/2). E in generale, se si pone A^(m/n) uguale a B, Aᵐ sarà uguale a Bⁿ, e quindi maAᵐ⁻¹ uguale a nbBⁿ⁻¹, e maA⁻¹ uguale a nbB⁻¹, ossia a nbA^(−m/n); e quindi (m/n)aA^((m−n)/n) uguale a b, cioè al momento di A^(m/n). C.V.D.

**[II.S2.25]** *Caso 6.* Dunque il momento di una quantità generata qualsiasi AᵐBⁿ è il momento di Aᵐ moltiplicato per Bⁿ, insieme con il momento di Bⁿ moltiplicato per Aᵐ, cioè maAᵐ⁻¹Bⁿ + nbBⁿ⁻¹Aᵐ; e ciò sia che gli indici m e n delle potenze siano numeri interi o fratti, sia che siano affermativi o negativi. E lo stesso ragionamento vale per il contenuto sotto più potenze. C.V.D.

**[II.S2.26]** *Cor. 1.* Di qui, in quantità in proporzione continua, se un termine è dato, i momenti dei termini rimanenti staranno come gli stessi termini moltiplicati per il numero degli intervalli fra essi e il termine dato. Siano A, B, C, D, E, F in proporzione continua: se è dato il termine C, i momenti dei termini rimanenti staranno fra loro come −2A, −B, D, 2E, 3F.

**[II.S2.27]** *Cor. 2.* E se in quattro proporzionali sono date le due medie, i momenti delle estreme staranno come le estreme stesse. Lo stesso si deve intendere dei lati di un rettangolo dato qualsiasi.

**[II.S2.28]** *Cor. 3.* E se è data la somma o la differenza di due quadrati, i momenti dei lati staranno inversamente come i lati.

### Scolio [al Lemma II] (la lettera a Collins del 10 dicembre 1672)

**[II.S2.29]** *Scolio.* In una lettera al signor J. Collins, nostro connazionale, datata 10 dicembre 1672, dopo aver descritto un metodo delle tangenti che sospettavo fosse lo stesso del metodo di Sluse, allora non ancora reso pubblico, aggiunsi: «Questo è un caso particolare, o piuttosto un corollario, di un metodo generale che si estende, senza alcun calcolo fastidioso, non soltanto a condurre le tangenti a curve qualsiasi, sia geometriche sia meccaniche, o comunque riferite a rette o ad altre curve, ma anche a risolvere altri generi più astrusi di problemi sulle curvature, le aree, le lunghezze, i centri di gravità delle curve ecc.; e non è limitato (come il metodo di Hudde sui massimi e minimi) alle sole equazioni prive di quantità sorde. Questo metodo l’ho intrecciato con quell’altro con cui conduco la risoluzione delle equazioni riducendole a serie infinite.» Fin qui la lettera. E queste ultime parole si riferiscono al trattato che avevo scritto su questi argomenti nell’anno 1671. Il fondamento di questo metodo generale è poi contenuto nel lemma precedente.

### Proposizione VIII. Teorema VI (moto rettilineo verticale: forze assolute in progressione geometrica)

**[II.S2.30]** **Se un corpo, in un mezzo uniforme, sotto l’azione uniforme della gravità, sale o scende in linea retta, e lo spazio totale descritto si divide in parti uguali, e all’inizio delle singole parti si cercano le forze assolute (aggiungendo la resistenza del mezzo alla forza di gravità quando il corpo sale, o sottraendola quando il corpo scende), dico che quelle forze assolute sono in progressione geometrica.**

**[II.S2.31]** Si rappresenti infatti la forza di gravità con la linea data AC; la resistenza con la linea indefinita AK; la forza assoluta nella discesa del corpo con la differenza KC; la velocità del corpo con la linea AP, che sia media proporzionale fra AK e AC, e quindi in rapporto subduplicato della resistenza; l’incremento della resistenza fatto in una particella di tempo data con la lineetta KL, e l’incremento contemporaneo della velocità con la lineetta PQ; e con centro C e asintoti ortogonali CA, CH si descriva un’iperbole qualsiasi BNS, che incontri in B, N, O le perpendicolari innalzate AB, KN, LO. Poiché AK sta come AP², il momento KL della prima starà come il momento 2AP×PQ del secondo, cioè come AP per KC; infatti l’incremento PQ della velocità (per la Legge II del moto) è proporzionale alla forza generante KC. Si componga il rapporto di KL con il rapporto di KN, e il rettangolo KL×KN starà come AP×KC×KN; cioè, poiché il rettangolo KC×KN è dato, come AP. Ma il rapporto ultimo dell’area iperbolica KNOL al rettangolo KL×KN, quando i punti K e L si riuniscono, è di uguaglianza. Dunque quell’area iperbolica evanescente sta come AP. L’intera area iperbolica ABOL si compone dunque delle particelle KNOL, sempre proporzionali alla velocità AP, e perciò è proporzionale allo spazio descritto con quella velocità. Si divida ora quell’area in parti uguali ABMI, IMNK, KNOL, ecc.: le forze assolute AC, IC, KC, LC, ecc. saranno in progressione geometrica. C.V.D. E con un argomento simile, nella salita del corpo, prendendo dalla parte opposta del punto A le aree uguali ABmi, imnk, knol, ecc., risulterà che le forze assolute AC, iC, kC, lC, ecc. sono in proporzione continua. E perciò, se si prendono uguali tutti gli spazi, in salita e in discesa, tutte le forze assolute lC, kC, iC, AC, IC, KC, LC, ecc. saranno in proporzione continua. C.V.D.

**[II.S2.32]** *Cor. 1.* Di qui, se lo spazio descritto si rappresenta con l’area iperbolica ABNK, la forza di gravità, la velocità del corpo e la resistenza del mezzo si possono rappresentare rispettivamente con le linee AC, AP e AK; e viceversa.

**[II.S2.33]** *Cor. 2.* E l’esponente della velocità massima che il corpo può mai acquistare scendendo all’infinito è la linea AC.

**[II.S2.34]** *Cor. 3.* Dunque, se per una velocità data si conosce la resistenza del mezzo, si troverà la velocità massima prendendola in modo che stia a quella velocità data nel rapporto subduplicato di quello che la forza di gravità ha con quella resistenza nota del mezzo.

### Proposizione IX. Teorema VII (tempi di salita e di discesa come settori di cerchio e di iperbole)

**[II.S2.35]** **Posto quanto si è già dimostrato, dico che, se le tangenti degli angoli di un settore circolare e di un settore iperbolico si prendono proporzionali alle velocità, essendo il raggio di grandezza opportuna, l’intero tempo della salita fino al luogo [più alto] sarà come il settore del cerchio, e l’intero tempo della discesa dal luogo [più alto] come il settore dell’iperbole.**

**[II.S2.36]** Alla retta AC, con cui si rappresenta la forza di gravità, si conduca perpendicolare e uguale AD. Con centro D e semidiametro AD si descrivano sia il quadrante di cerchio AtE, sia l’iperbole rettangola AVZ, che ha per asse AX, per vertice principale A e per asintoto DC. Si conducano Dp, DP: il settore circolare AtD starà come l’intero tempo della salita fino al luogo più alto, e il settore iperbolico ATD come l’intero tempo della discesa dal luogo più alto; purché le tangenti dei settori, Ap e AP, stiano come le velocità.

**[II.S2.37]** *Caso 1.* Si conduca infatti Dvq, che stacchi i momenti del settore ADt e del triangolo ADp, cioè le particelle piccolissime tDv e qDp descritte nello stesso tempo. Poiché queste particelle, per l’angolo comune D, stanno in rapporto duplicato dei lati, la particella tDv starà come qDp×tD²/pD², cioè, poiché tD è data, come qDp/pD². Ma pD² è AD² + Ap², cioè AD² + AD×Ak, ossia AD×Ck; e qDp è ½AD×pq. Dunque la particella tDv del settore sta come pq/Ck; cioè direttamente come il decremento piccolissimo pq della velocità e inversamente come la forza Ck che diminuisce la velocità; e perciò come la particella di tempo che corrisponde al decremento. E, componendo, la somma di tutte le particelle tDv nel settore ADt diventa come la somma delle particelle di tempo che corrispondono alle singole particelle pq perdute dalla velocità decrescente Ap, finché quella velocità, diminuita fino a nulla, sia svanita; cioè l’intero settore ADt sta come l’intero tempo della salita fino al luogo più alto. C.V.D.

**[II.S2.38]** *Caso 2.* Si conduca DQV, che stacchi sia del settore DAV sia del triangolo DAQ le particelle piccolissime TDV e PDQ: queste particelle staranno fra loro come DT² sta a DP², cioè (se TX e AP sono parallele) come DX² sta a DA², o TX² ad AP², e, separando, come DX² − TX² sta a DA² − AP². Ma per la natura dell’iperbole DX² − TX² è AD², e per ipotesi AP² è AD×AK. Dunque le particelle stanno fra loro come AD² sta ad AD² − AD×AK, cioè come AD sta ad AD − AK, ossia come AC sta a CK; e perciò la particella TDV del settore è PDQ×AC/CK; e quindi, poiché AC e AD sono date, sta come PQ/CK, cioè direttamente come l’incremento della velocità e inversamente come la forza che genera l’incremento; e perciò come la particella di tempo che corrisponde all’incremento. E, componendo, la somma delle particelle di tempo nelle quali si generano tutte le particelle PQ della velocità AP diventa come la somma delle particelle del settore ADT, cioè il tempo intero come il settore intero. C.V.D.

**[II.S2.39]** *Cor. 1.* Di qui, se AB è uguale alla quarta parte di AC, lo spazio che un corpo descrive cadendo in un tempo qualsiasi starà allo spazio che il corpo potrebbe descrivere nello stesso tempo procedendo uniformemente con la velocità massima AC come l’area ABNK, con cui si rappresenta lo spazio descritto cadendo, sta all’area ATD, con cui si rappresenta il tempo. Infatti, poiché AC sta ad AP come AP sta ad AK, LK starà a PQ (per il Cor. 1 del Lemma II di questo libro) come 2AK sta ad AP, cioè come 2AP sta ad AC; e di qui LK starà a ½PQ come AP sta a ¼AC, ossia ad AB; e KN sta ad AC, ossia ad AD, come AB sta a CK; perciò, per uguaglianza, LKNO sta a DPQ come AP sta a CK. Ma DPQ stava a DTV come CK sta ad AC. Dunque, di nuovo per uguaglianza, LKNO sta a DTV come AP sta ad AC; cioè come la velocità del corpo che cade sta alla velocità massima che il corpo può acquistare cadendo. Poiché dunque i momenti LKNO e DTV delle aree ABNK e ATD stanno come le velocità, tutte le parti di quelle aree generate nello stesso tempo staranno come gli spazi descritti nello stesso tempo, e perciò le aree intere ABNK e ATD, generate dall’inizio, come gli spazi interi descritti dall’inizio della discesa. C.V.D.

**[II.S2.40]** *Cor. 2.* Lo stesso segue anche per lo spazio descritto in salita: cioè che tutto quello spazio sta allo spazio descritto nello stesso tempo con la velocità uniforme AC come l’area ABnk sta al settore ADt.

**[II.S2.41]** *Cor. 3.* La velocità del corpo che cade nel tempo ATD sta alla velocità che acquisterebbe nello stesso tempo in uno spazio non resistente come il triangolo APD sta al settore iperbolico ATD. Infatti la velocità nel mezzo non resistente sarebbe come il tempo ATD, e nel mezzo resistente è come AP, cioè come il triangolo APD. E quelle velocità, all’inizio della discesa, sono uguali fra loro, così come quelle aree ATD, APD.

**[II.S2.42]** *Cor. 4.* Con lo stesso argomento, la velocità in salita sta alla velocità con cui il corpo, nello stesso tempo, in uno spazio non resistente potrebbe perdere tutto il suo moto di salita, come il triangolo ApD sta al settore circolare AtD, ossia come la retta Ap sta all’arco At.

**[II.S2.43]** *Cor. 5.* Dunque il tempo nel quale un corpo, cadendo in un mezzo resistente, acquista la velocità AP sta al tempo nel quale potrebbe acquistare la velocità massima AC cadendo in uno spazio non resistente come il settore ADT sta al triangolo ADC; e il tempo nel quale, salendo in un mezzo resistente, potrebbe perdere la velocità Ap sta al tempo nel quale potrebbe perdere la stessa velocità salendo in uno spazio non resistente come l’arco At sta alla sua tangente Ap.

**[II.S2.44]** *Cor. 6.* Di qui, dato il tempo, è dato lo spazio descritto in salita o in discesa. Infatti è data la velocità massima di un corpo che scende all’infinito (per i Cor. 2 e 3 del Teorema VI del Libro II [cioè della Prop. VIII]), e di qui è dato il tempo nel quale il corpo potrebbe acquistare quella velocità cadendo in uno spazio non resistente. E, prendendo il settore ADT o ADt in modo che stia al triangolo ADC nel rapporto del tempo dato al tempo ora trovato, saranno dati sia la velocità AP o Ap, sia l’area ABNK o ABnk, che sta al settore ADT o ADt come lo spazio cercato sta allo spazio che, nel tempo dato, si può descrivere uniformemente con quella velocità massima già trovata prima.

**[II.S2.45]** *Cor. 7.* E, procedendo all’inverso, dato lo spazio di salita o di discesa ABnk o ABNK, sarà dato il tempo ADt o ADT.

### Proposizione X. Problema III (la densità del mezzo che fa descrivere una curva data)

**[II.S2.46]** **La forza uniforme di gravità tenda direttamente verso il piano dell’orizzonte, e la resistenza stia come la densità del mezzo e il quadrato della velocità considerati congiuntamente: si richiede sia la densità del mezzo nei singoli luoghi, che faccia muovere il corpo lungo una qualsiasi linea curva data, sia la velocità del corpo e la resistenza del mezzo nei singoli luoghi.**

**[II.S2.47]** Sia PQ quel piano, perpendicolare al piano della figura; PFHQ una linea curva che incontra questo piano nei punti P e Q; G, H, I, K quattro luoghi del corpo che procede lungo questa curva da F verso Q; GB, HC, ID, KE quattro ordinate parallele condotte da questi punti all’orizzonte, che poggiano sulla linea orizzontale PQ nei punti B, C, D, E; e le distanze BC, CD, DE delle ordinate fra loro siano uguali. Dai punti G e H si conducano le rette GL, HN tangenti alla curva in G e H, che incontrino in L e N le ordinate CH, DI prolungate verso l’alto, e si completi il parallelogramma HCDM. I tempi nei quali il corpo descrive gli archi GH, HI staranno in rapporto subduplicato delle altezze LH, NI che il corpo potrebbe descrivere in quei tempi cadendo dalle tangenti; e le velocità staranno direttamente come le lunghezze descritte GH, HI e inversamente come i tempi. Si rappresentino i tempi con T e t, e le velocità con GH/T e HI/t: il decremento della velocità fatto nel tempo t sarà rappresentato da GH/T − HI/t. Questo decremento nasce dalla resistenza che ritarda il corpo e dalla gravità che lo accelera. La gravità, in un corpo che cade e che cadendo descrive lo spazio NI, genera una velocità con la quale si sarebbe potuto descrivere nello stesso tempo il doppio di quello spazio, come ha dimostrato Galileo, cioè la velocità 2NI/t; ma in un corpo che descrive l’arco HI essa accresce quell’arco soltanto della lunghezza HI − HN, ossia MI×NI/HI, e perciò genera soltanto la velocità 2MI×NI/(t×HI). Si aggiunga questa velocità al decremento detto prima, e si avrà il decremento della velocità che nasce dalla sola resistenza, cioè GH/T − HI/t + 2MI×NI/(t×HI). Perciò, poiché la gravità nello stesso tempo genera in un corpo che cade la velocità 2NI/t, la resistenza starà alla gravità come GH/T − HI/t + 2MI×NI/(t×HI) sta a 2NI/t, ossia come t×GH/T − HI + 2MI×NI/HI sta a 2NI.

**[II.S2.48]** Ora, al posto delle ascisse CB, CD, CE si scrivano −o, o, 2o. Al posto dell’ordinata CH si scriva P, e al posto di MI una serie qualsiasi Qo + Roo + So³ + ecc. Tutti i termini della serie dopo il primo, cioè Roo + So³ + ecc., saranno NI; e le ordinate DI, EK e BG saranno rispettivamente P − Qo − Roo − So³ − ecc., P − 2Qo − 4Roo − 8So³ − ecc. e P + Qo − Roo + So³ − ecc. E, elevando al quadrato le differenze delle ordinate BG − CH e CH − DI, e aggiungendo ai quadrati risultanti i quadrati di BC e CD, si avranno i quadrati degli archi GH, HI: oo + QQoo − 2QRo³ + ecc. e oo + QQoo + 2QRo³ + ecc. Le loro radici, o√(1+QQ) − QRoo/√(1+QQ) e o√(1+QQ) + QRoo/√(1+QQ), sono gli archi GH e HI. Inoltre, se dall’ordinata CH si sottrae la semisomma delle ordinate BG e DI, e dall’ordinata DI la semisomma delle ordinate CH ed EK, resteranno Roo e Roo + 3So³, saette degli archi GI e HK. E queste sono proporzionali alle lineette LH e NI, e quindi in rapporto duplicato dei tempi infinitamente piccoli T e t; e di qui il rapporto t/T è √((R + 3So)/R), ossia (R + (3/2)So)/R; e t×GH/T − HI + 2MI×NI/HI, sostituendo i valori di t/T, GH, HI, MI e NI ora trovati, diventa (3Soo/2R)√(1+QQ). E poiché 2NI è 2Roo, la resistenza starà ora alla gravità come (3Soo/2R)√(1+QQ) sta a 2Roo, cioè come 3S√(1+QQ) sta a 4RR.

**[II.S2.49]** La velocità, poi, è quella con cui un corpo, uscendo da un luogo qualsiasi H secondo la tangente HN, potrebbe poi muoversi nel vuoto lungo una parabola che ha per diametro HC e per lato retto HN²/NI, ossia (1+QQ)/R.

**[II.S2.50]** E la resistenza sta come la densità del mezzo e il quadrato della velocità considerati congiuntamente; e perciò la densità del mezzo sta direttamente come la resistenza e inversamente come il quadrato della velocità, cioè direttamente come 3S√(1+QQ)/4RR e inversamente come (1+QQ)/R, ossia come S/(R√(1+QQ)). C.V.T.

**[II.S2.51]** *Cor. 1.* Se la tangente HN si prolunga da entrambe le parti finché incontri in T un’ordinata qualsiasi AF, HT/AC sarà uguale a √(1+QQ), e perciò in quanto precede la si può scrivere al posto di √(1+QQ). In questo modo la resistenza starà alla gravità come 3S×HT sta a 4RR×AC, la velocità starà come HT/(AC√R), e la densità del mezzo starà come S×AC/(R×HT).

**[II.S2.52]** *Cor. 2.* E di qui, se la linea curva PFHQ è definita, come si suole, mediante la relazione fra la base, ossia ascissa, AC e l’ordinata CH, e il valore dell’ordinata si risolve in una serie convergente, il problema si risolverà speditamente per mezzo dei primi termini della serie, come negli esempi seguenti.

#### Esempio 1 (il semicerchio)

**[II.S2.53]** *Es. 1.* Sia la linea PFHQ un semicerchio descritto sul diametro PQ, e si richieda la densità del mezzo che faccia muovere un proiettile lungo questa linea.

**[II.S2.54]** Si divida a metà il diametro PQ in A; si chiami AQ n, AC a, CH e e CD o: DI², ossia AQ² − AD², sarà = nn − aa − 2ao − oo, ossia ee − 2ao − oo; ed estraendo la radice con il nostro metodo si avrà DI = e − ao/e − oo/2e − aaoo/2e³ − ao³/2e³ − a³o³/2e⁵ − ecc. Qui si scriva nn al posto di ee + aa, e risulterà DI = e − ao/e − nnoo/2e³ − anno³/2e⁵ − ecc.

**[II.S2.55]** Serie di questo genere le distinguo in termini successivi in questo modo. Chiamo primo il termine in cui non compare la quantità infinitamente piccola o; secondo quello in cui quella quantità è di una dimensione; terzo quello in cui compare con due; quarto quello in cui è di tre; e così all’infinito. E il primo termine, che qui è e, denoterà sempre la lunghezza dell’ordinata CH che poggia all’inizio della quantità indefinita o. Il secondo termine, che qui è ao/e, denoterà la differenza fra CH e DN, cioè la lineetta MN, che si stacca completando il parallelogramma HCDM, e perciò determina sempre la posizione della tangente HN: come in questo caso, prendendo MN in modo che stia a HM come ao/e sta a o, ossia come a sta a e. Il terzo termine, che qui è nnoo/2e³, designerà la lineetta IN, che giace fra la tangente e la curva, e perciò determina l’angolo di contatto IHN, ossia la curvatura che la linea curva ha in H. Se quella lineetta IN è di grandezza finita, sarà designata dal terzo termine insieme con quelli che seguono all’infinito. Ma se quella lineetta diminuisce all’infinito, i termini successivi diventano infinitamente minori del terzo, e perciò si possono trascurare. Il quarto termine determina la variazione della curvatura, il quinto la variazione della variazione, e così via. Di qui, di passaggio, risulta evidente l’uso non disprezzabile di queste serie nella soluzione dei problemi che dipendono dalle tangenti e dalla curvatura delle curve.

**[II.S2.56]** Si confronti ora la serie e − ao/e − nnoo/2e³ − anno³/2e⁵ − ecc. con la serie P − Qo − Roo − So³ − ecc., e corrispondentemente al posto di P, Q, R e S si scriva e, a/e, nn/2e³ e ann/2e⁵, e al posto di √(1+QQ) si scriva √(1+aa/ee), ossia n/e: la densità del mezzo risulterà come a/ne, cioè (poiché n è data) come a/e, ossia AC/CH, cioè come quella lunghezza della tangente HT che termina sul semidiametro AF perpendicolare a PQ; e la resistenza starà alla gravità come 3a sta a 2n, cioè come 3AC sta al diametro PQ del cerchio; la velocità, poi, starà come √CH. Perciò, se il corpo esce dal luogo F con la velocità giusta lungo una linea parallela a PQ, e la densità del mezzo nei singoli luoghi H sta come la lunghezza della tangente HT, e anche la resistenza in un luogo qualsiasi H sta alla forza di gravità come 3AC sta a PQ, quel corpo descriverà il quadrante di cerchio FHQ. C.V.T.

**[II.S2.57]** Ma se lo stesso corpo uscisse dal luogo P secondo una linea perpendicolare a PQ e cominciasse a muoversi nell’arco di semicerchio PFQ, si dovrebbe prendere AC, cioè a, dalla parte opposta del centro A, e perciò se ne dovrebbe cambiare il segno e scrivere −a al posto di +a. In questo modo la densità del mezzo risulterebbe come −a/e. Ma la natura non ammette una densità negativa, cioè una densità che acceleri i moti dei corpi; e perciò non può avvenire naturalmente che un corpo, salendo da P, descriva il quadrante di cerchio PF. Per ottenere questo effetto il corpo dovrebbe essere accelerato da un mezzo che spinge, non impedito da un mezzo che resiste.

#### Esempio 2 (la parabola)

**[II.S2.58]** *Es. 2.* Sia la linea PFQ una parabola, con l’asse AF perpendicolare all’orizzonte PQ, e si richieda la densità del mezzo che faccia muovere un proiettile lungo di essa.

**[II.S2.59]** Per la natura della parabola, il rettangolo PDQ è uguale al rettangolo sotto l’ordinata DI e una retta data: cioè, se si chiamano b quella retta, a PC, c PQ, e CH e o CD, il rettangolo (a + o) per (c − a − o), ossia ac − aa − 2ao + co − oo, è uguale al rettangolo b per DI, e perciò DI è uguale a (ac − aa)/b + ((c − 2a)/b)o − oo/b. Ora si dovrebbe scrivere il secondo termine di questa serie, ((c − 2a)/b)o, al posto di Qo, e anche il terzo termine, oo/b, al posto di Roo. Ma poiché non ci sono altri termini, il coefficiente S del quarto dovrà annullarsi, e perciò la quantità S/(R√(1+QQ)), alla quale è proporzionale la densità del mezzo, sarà nulla. Dunque il proiettile si muoverà lungo una parabola senza alcuna densità del mezzo, come dimostrò un tempo Galileo. C.V.T.

#### Esempio 3 (l’iperbole conica)

**[II.S2.60]** *Es. 3.* Sia la linea AGK un’iperbole con l’asintoto NX perpendicolare al piano orizzontale AK, e si cerchi la densità del mezzo che faccia muovere un proiettile lungo questa linea.

**[II.S2.61]** Sia MX l’altro asintoto, che incontri in V l’ordinata DG prolungata; per la natura dell’iperbole, il rettangolo XV per VG sarà dato. Ma è dato anche il rapporto di DN a VX, e perciò è dato anche il rettangolo DN per VG. Sia esso bb; e, completato il parallelogramma DNXZ, si chiami BN a, BD o, NX c, e si ponga che il rapporto dato di VZ a ZX, ossia a DN, sia quello di m a n. DN sarà uguale ad a − o, VG a bb/(a − o), VZ a (m/n)(a − o), e GD, ossia NX − VZ − VG, a c − (m/n)a + (m/n)o − bb/(a − o). Si risolva il termine bb/(a − o) nella serie convergente bb/a + (bb/aa)o + (bb/a³)oo + (bb/a⁴)o³ ecc., e GD diventerà uguale a c − (m/n)a − bb/a + (m/n)o − (bb/aa)o − (bb/a³)o² − (bb/a⁴)o³ ecc. Di questa serie il secondo termine, (m/n)o − (bb/aa)o, si deve usare al posto di Qo; il terzo, con il segno cambiato, (bb/a³)o², al posto di Ro²; e il quarto, anch’esso con il segno cambiato, (bb/a⁴)o³, al posto di So³; e i loro coefficienti m/n − bb/aa, bb/a³ e bb/a⁴ si devono scrivere nella regola precedente al posto di Q, R e S. Fatto ciò, la densità del mezzo risulta come (bb/a⁴) / ((bb/a³)√(1 + mm/nn − 2mbb/naa + b⁴/a⁴)), ossia 1/√(aa + mmaa/nn − 2mbb/n + b⁴/aa), cioè, se su VZ si prende VY uguale a VG, come 1/XY. Infatti aa e mmaa/nn − 2mbb/n + b⁴/aa sono i quadrati di XZ e di ZY. La resistenza, poi, si trova stare alla gravità nel rapporto che 3XY ha con 2YG; e la velocità è quella con cui il corpo procederebbe lungo una parabola con vertice G, diametro DG e lato retto XY²/VG. Si ponga dunque che le densità del mezzo nei singoli luoghi G siano inversamente come le distanze XY, e che la resistenza in un luogo qualsiasi G stia alla gravità come 3XY sta a 2YG: il corpo, lanciato dal luogo A con la velocità giusta, descriverà quell’iperbole AGK. C.V.T.

#### Esempio 4 (iperboli di grado qualsiasi)

**[II.S2.62]** *Es. 4.* Si ponga, in modo indeterminato, che la linea AGK sia un’iperbole descritta con centro X e asintoti MX, NX secondo questa legge: costruito il rettangolo XZDN, il cui lato ZD tagli l’iperbole in G e il suo asintoto in V, VG sia inversamente come una potenza qualsiasi DNⁿ di ZX, ossia di DN, il cui indice è il numero n; e si cerchi la densità del mezzo nel quale un proiettile proceda lungo questa curva.

**[II.S2.63]** Al posto di BN, BD, NX si scrivano rispettivamente A, O, C; sia VZ a XZ, ossia a DN, come d sta a e, e VG uguale a bb/DNⁿ: DN sarà uguale ad A − O, VG = bb/(A − O)ⁿ, VZ = (d/e)(A − O), e GD, ossia NX − VZ − VG, uguale a C − (d/e)A + (d/e)O − bb/(A − O)ⁿ. Si risolva quel termine bb/(A − O)ⁿ nella serie infinita bb/Aⁿ + (nbb/Aⁿ⁺¹)O + ((nn + n)/2Aⁿ⁺²)bbO² + ((n³ + 3nn + 2n)/6Aⁿ⁺³)bbO³ ecc., e GD diventerà uguale a C − (d/e)A − bb/Aⁿ + (d/e)O − (nbb/Aⁿ⁺¹)O − ((nn + n)/2Aⁿ⁺²)bbO² − ((n³ + 3nn + 2n)/6Aⁿ⁺³)bbO³ ecc. Di questa serie il secondo termine, (d/e)O − (nbb/Aⁿ⁺¹)O, si deve usare al posto di Qo, il terzo, ((nn + n)/2Aⁿ⁺²)bbO², al posto di Ro², il quarto, ((n³ + 3nn + 2n)/6Aⁿ⁺³)bbO³, al posto di So³. E di qui la densità del mezzo S/(R√(1+QQ)), in un luogo qualsiasi G, diventa (n + 2)/(3√(A² + (dd/ee)A² − (2dnbb/eAⁿ)A + nnb⁴/A²ⁿ)); e perciò, se su VZ si prende VY uguale a n×VG, quella densità è inversamente come XY. Infatti A² e (dd/ee)A² − (2dnbb/eAⁿ)A + nnb⁴/A²ⁿ sono i quadrati di XZ e di ZY. La resistenza, poi, nello stesso luogo G diventa alla gravità come 3S per XY/A sta a 4RR, cioè come XY sta a ((2nn + 2n)/(n + 2))VG. E la velocità, nello stesso luogo, è proprio quella con cui il corpo lanciato procederebbe lungo una parabola con vertice G, diametro GD e lato retto (1+QQ)/R, ossia 2XY²/((nn + n)×VG). C.V.T.

### Scolio [alla Prop. X] (uso pratico delle iperboli)

**[II.S2.64]** *Scolio.* Nello stesso modo in cui, nel Cor. 1, la densità del mezzo è risultata come S×AC/(R×HT), se si pone la resistenza come una potenza qualsiasi Vⁿ della velocità V, la densità del mezzo risulterà come (S/R^((4−n)/2))×(AC/HT)ⁿ⁻¹.

**[II.S2.65]** E perciò, se si può trovare una curva secondo la legge che sia dato il rapporto di S/R^((4−n)/2) a (HT/AC)ⁿ⁻¹, ossia di S²/R⁴⁻ⁿ a (1+QQ)ⁿ⁻¹, il corpo si muoverà lungo questa curva in un mezzo uniforme con una resistenza che stia come la potenza Vⁿ della velocità. Ma torniamo alle curve più semplici.

**[II.S2.66]** Poiché il moto lungo una parabola non avviene se non in un mezzo non resistente, mentre lungo le iperboli qui descritte avviene per effetto di una resistenza continua, è evidente che la linea che un proiettile descrive in un mezzo che resiste uniformemente si avvicina più a queste iperboli che alla parabola. Quella linea è certamente di genere iperbolico, ma presso il vertice dista di più dagli asintoti, e nelle parti più lontane dal vertice si avvicina a essi più di quanto comporti il rapporto delle iperboli che ho descritto qui. La differenza fra queste e quella non è però tanto grande che queste non si possano usare senza inconvenienti, nella pratica, al posto di quella. E forse queste saranno più utili di un’iperbole più accurata e insieme più composta. Esse si applicheranno all’uso in questo modo.

**[II.S2.67]** Si completi il parallelogramma XYGT: la retta GT sarà tangente all’iperbole in G, e perciò la densità del mezzo in G è inversamente come la tangente GT, la velocità nello stesso luogo come √(GT²/GV), e la resistenza sta alla forza di gravità come GT sta a ((2nn + 2n)/(n + 2))×GV.

**[II.S2.68]** Perciò, se un corpo lanciato dal luogo A secondo la retta AH descrive l’iperbole AGK, e AH prolungata incontra in H l’asintoto NX, e AI, condotta parallela a esso, incontra in I l’altro asintoto MX, la densità del mezzo in A sarà inversamente come AH, la velocità del corpo come √(AH²/AI), e la resistenza nello stesso luogo starà alla gravità come AH sta a ((2nn + 2n)/(n + 2))×AI. Di qui derivano le regole seguenti.

**[II.S2.69]** *Regola 1.* Se si conservano sia la densità del mezzo in A sia la velocità con cui il corpo è lanciato, e si cambia l’angolo NAH, resteranno invariate le lunghezze AH, AI, HX. Perciò, se quelle lunghezze si trovano in un caso qualsiasi, l’iperbole si potrà poi determinare speditamente per un qualsiasi angolo dato NAH.

**[II.S2.70]** *Regola 2.* Se si conservano sia l’angolo NAH sia la densità del mezzo in A, e si cambia la velocità con cui il corpo è lanciato, si conserverà la lunghezza AH, e AI cambierà inversamente in rapporto duplicato della velocità.

**[II.S2.71]** *Regola 3.* Se si conservano tanto l’angolo NAH quanto la velocità del corpo in A e la gravità acceleratrice, e la proporzione della resistenza in A alla gravità motrice aumenta in un rapporto qualsiasi, la proporzione di AH ad AI aumenterà nello stesso rapporto, mentre restano invariati il lato retto della parabola detta sopra e la lunghezza AH²/AI, a esso proporzionale; e perciò AH diminuirà nello stesso rapporto, e AI diminuirà in quel rapporto duplicato. La proporzione della resistenza al peso aumenta poi quando o la gravità specifica, a parità di grandezza, diventa minore, o la densità del mezzo maggiore, o la resistenza, per la diminuzione della grandezza, diminuisce in un rapporto minore del peso.

**[II.S2.72]** *Regola 4.* Poiché la densità del mezzo vicino al vertice dell’iperbole è maggiore che nel luogo A, per avere una densità media si deve trovare il rapporto della minima delle tangenti GT alla tangente AH, e aumentare la densità in A in un rapporto un poco minore di quello della semisomma di queste tangenti alla minima delle tangenti GT.

**[II.S2.73]** *Regola 5.* Se sono date le lunghezze AH, AI, e si deve descrivere la figura AGK, prolunga HN fino a X in modo che HX stia ad AI come n + 1 sta a 1; e con centro X e asintoti MX, NX descrivi per il punto A un’iperbole secondo la legge che AI stia a una VG qualsiasi come XVⁿ sta a XIⁿ.

**[II.S2.74]** *Regola 6.* Quanto maggiore è il numero n, tanto più accurate sono queste iperboli nella salita del corpo da A, e tanto meno accurate nella sua discesa verso K; e viceversa. L’iperbole conica tiene una posizione intermedia, ed è più semplice delle altre. Perciò, se l’iperbole è di questo genere, e si cerca il punto K in cui il corpo lanciato cadrà su una retta qualsiasi AN passante per il punto A, la AN prolungata incontri gli asintoti MX, NX in M e N, e si prenda NK uguale ad AM.

**[II.S2.75]** *Regola 7.* E di qui risulta evidente un metodo spedito per determinare questa iperbole dai fenomeni. Si lancino due corpi simili e uguali, con la stessa velocità, sotto angoli diversi HAK, hAK, e cadano sul piano dell’orizzonte in K e k; e si annoti la proporzione di AK ad Ak. Sia essa come d sta a e. Poi, innalzata una perpendicolare AI di lunghezza qualsiasi, assumi in un modo qualsiasi la lunghezza AH o Ah, e di qui ricava graficamente le lunghezze AK, Ak, per la Regola 6. Se il rapporto di AK ad Ak è lo stesso del rapporto di d a e, la lunghezza AH è stata assunta correttamente. Altrimenti prendi sulla retta illimitata SM la lunghezza SM uguale alla AH assunta, e innalza la perpendicolare MN uguale alla differenza dei rapporti, AK/Ak − d/e, moltiplicata per una retta data qualsiasi. Con un metodo simile, da più lunghezze AH assunte, si devono trovare più punti N, e per tutti si deve condurre una linea curva regolare NNXN, che tagli in X la retta SMMM. Si assuma infine AH uguale all’ascissa SX, e di qui si trovi di nuovo la lunghezza AK; e le lunghezze che stanno alla lunghezza assunta AI e a quest’ultima AH come la lunghezza AK conosciuta per esperimento sta all’ultima lunghezza AK trovata saranno le vere lunghezze AI e AH che si dovevano trovare. Date queste, sarà data anche la resistenza del mezzo nel luogo A, poiché essa sta alla forza di gravità come AH sta a 2AI. Si deve poi aumentare la densità del mezzo per la Regola 4; e la resistenza ora trovata, se si aumenta nello stesso rapporto, diventerà più accurata.

**[II.S2.76]** *Regola 8.* Trovate le lunghezze AH, HX, se ora si desidera la posizione della retta AH secondo la quale il proiettile, lanciato con quella velocità data, cade in un punto qualsiasi K: nei punti A e K si innalzino le rette AC, KF perpendicolari all’orizzonte, delle quali AC sia diretta verso il basso e sia uguale ad AI, ossia a ½HX. Con asintoti AK, KF si descriva un’iperbole la cui coniugata passi per il punto C; e con centro A e raggio AH si descriva un cerchio che tagli quell’iperbole nel punto H: il proiettile lanciato secondo la retta AH cadrà nel punto K. C.V.T. Infatti il punto H, poiché la lunghezza AH è data, si trova in qualche punto del cerchio descritto. Si conduca CH, che incontri AK e KF, la prima in E, la seconda in F; e, per le parallele CH, MX e le uguali AC, AI, AE sarà uguale ad AM, e perciò anche uguale a KN. Ma CE sta ad AE come FH sta a KN, e perciò CE e FH sono uguali. Dunque il punto H cade sull’iperbole descritta con asintoti AK, KF, la cui coniugata passa per il punto C, e perciò si trova nell’intersezione comune di questa iperbole e del cerchio descritto. C.V.D. Si deve poi notare che questa operazione procede allo stesso modo sia che la retta AKN sia parallela all’orizzonte, sia che sia inclinata sull’orizzonte con un angolo qualsiasi; che dalle due intersezioni H, H nascono due angoli NAH, NAH; e che nella pratica meccanica basta descrivere il cerchio una volta e poi applicare al punto C una riga illimitata CH in modo che la sua parte FH, compresa fra il cerchio e la retta FK, sia uguale alla sua parte CE, situata fra il punto C e la retta AK.

**[II.S2.77]** Ciò che si è detto delle iperboli si applica facilmente alle parabole. Infatti, se XAGK designa una parabola, toccata nel vertice X dalla retta XV, e le ordinate IA, VG stanno come potenze qualsiasi XIⁿ, XVⁿ delle ascisse XI, XV, si conducano XT, GT, AH, delle quali XT sia parallela a VG, e GT, AH tocchino la parabola in G e in A: un corpo lanciato da un luogo qualsiasi A secondo la retta AH prolungata, con la velocità giusta, descriverà questa parabola, purché la densità del mezzo nei singoli luoghi G sia inversamente come la tangente GT. La velocità in G sarà poi quella con cui un proiettile procederebbe, in uno spazio non resistente, lungo una parabola conica che ha per vertice G, per diametro VG prolungata verso il basso e per lato retto 2GT²/((nn − n)×VG). E la resistenza in G starà alla forza di gravità come GT sta a ((2nn − 2n)/(n − 2))×VG. Perciò, se NAK designa una linea orizzontale, e, restando invariate sia la densità del mezzo in A sia la velocità con cui il corpo è lanciato, l’angolo NAH si cambia in un modo qualsiasi, resteranno invariate le lunghezze AH, AI, HX; e di qui sono dati il vertice X della parabola e la posizione della retta XI; e, prendendo VG in modo che stia a IA come XVⁿ sta a XIⁿ, sono dati tutti i punti G della parabola per i quali passerà il proiettile.

**Fine della Sezione II. Nel testo originale segue la Sezione III, *De motu corporum quibus resistitur partim in ratione velocitatis, partim in ejusdem ratione duplicata*.**

---

## Apparato

### A.0 Estensioni del glossario

| Latino | Italiano | Motivazione |
|---|---|---|
| *corpori resistitur*, *quibus resistitur* | «il corpo incontra una resistenza», «che incontrano una resistenza» | Il passivo impersonale latino non ha un calco italiano naturale («al quale si resiste»). Motte: «is resisted». |
| *medium similare* | «mezzo omogeneo» | Termine fissato dal coordinatore; prima occorrenza in II.S2.01. *Similaris* è il mezzo le cui parti sono simili fra loro, cioè di densità uniforme; Motte «similar medium». |
| *asymptoti rectangulæ* | «asintoti ortogonali» | Asintoti perpendicolari fra loro. |
| *hyperbola rectangula* | «iperbole rettangola» | L’iperbole equilatera (asintoti ortogonali). Si conserva il termine storico; equivalente moderno in N4. |
| *particula temporis* | «particella di tempo» | Come *particula* nel glossario comune. |
| *exponere* | «rappresentare» | *Exponatur per lineam* = sia rappresentata da una linea. |
| *vis absoluta* (Propp. VIII–IX) | «forza assoluta» | Glossario comune; qui però indica la forza risultante sul corpo, gravità più o meno resistenza (N3), non la *vis absoluta* della Def. VIII. |
| *vis generans* | «forza generante» | La forza che genera l’incremento di velocità. |
| *genitum*, *geniti contenti* | «generato», «del contenuto generato» | Accordato con *genita* «quantità generata» (glossario del Libro II). Motte conserva il latino «genitum». |
| *latera generantia* | «lati generanti» | I fattori della quantità generata. |
| *coefficiens* | «coefficiente» | Definito da Newton stesso (II.S2.18): la quantità generata divisa per il lato. |
| *dignitas*; *index dignitatis* | «potenza»; «indice della potenza» | Come nei Fascicoli 9–12. |
| *continue ducere in* | «moltiplicare successivamente per» | *Ducere in* «moltiplicare per» (glossario); *continue* indica le moltiplicazioni in sequenza. |
| *contentum* | «contenuto» | Prodotto di più lati (Fascicolo 5, *contentum sub*). |
| *factus*, *quotus* | «prodotto», «quoziente» | |
| *latus quadratum*, *latus cubicum* | «lato quadrato», «lato cubico» | Radice quadrata e cubica in linguaggio geometrico (il lato del quadrato o del cubo di area o volume dato). |
| *momenta addititia / subductitia* | «momenti additivi / sottrattivi» | |
| *incrementa momentanea* | «incrementi momentanei» | Si conserva l’aggettivo affine a *momentum*. |
| *fluxio* | «flussione» | Termine tecnico di Newton; prima e unica occorrenza in II.S2.18. |
| *quantitates surdæ* | «quantità sorde» | Le quantità irrazionali (radicali). Motte «surd quantities». |
| *æquationum exegesis* | «risoluzione delle equazioni» | *Exegesis* è il termine di Viète per la risoluzione numerica. |
| *lineola* | «lineetta» | Come nei fascicoli precedenti. |
| *justa velocitas* | «la velocità giusta» | La velocità iniziale richiesta dalla costruzione. |
| *densitas mediocris* | «densità media» | Regola 4. |
| *parabola conica*, *hyperbola conica* | «parabola conica», «iperbole conica» | Le coniche ordinarie, contrapposte alle «parabole» e «iperboli» di grado n. |
| *regula interminata* | «riga illimitata» | Strumento della costruzione meccanica (Regola 8). |
| *graphice colligere* | «ricavare graficamente» | Motte amplia in «graphically, or by scale and compass». |
| *gravitas acceleratrix / motrix* | «gravità acceleratrice / motrice» | Regola 3, in parallelo con *vis acceleratrix / motrix*. |
| *æquivelox* | «ugualmente veloce» | Prop. VII, corollari. |
| *Exempl.*; *Reg.* | «Es.»; «Regola» | |

Termini richiesti dal coordinatore non presenti in questa sezione: *fluidum*, *compressio*, *vis elastica*, *vortex*, *unda*, *pulsus*, *oscillatio*, unità di misura. *Gravitas specifica* e *pondus* compaiono solo nella Regola 3.

### A.1 Titolo della Sezione e Proposizione V

**Latino:** *Si corpori resistitur in velocitatis ratione duplicata, & idem sola vi insita per medium similare movetur; tempora vero sumantur in progressione geometrica a minoribus terminis ad majores pergente: dico quod velocitates initio singulorum temporum sunt in eadem progressione geometrica inverse; & quod spatia sunt æqualia, quæ singulis temporibus describuntur.*

**Inglese:** “If a body is resisted in the duplicate ratio of its velocity, and moves by its innate force only through a similar medium; and the times be taken in a geometrical progression, proceeding from less to greater terms: I say, that the velocities at the beginning of each of the times are in the same geometrical progression inversely; and that the spaces are equal, which are described in each of the times.”

**Scelte.**

- *divisim* → «separando»; *vicissim* → «permutando»; *composite* → «componendo».
- *ABq*, *Kk quad.* → AB², Kk². *ultimo, ubi coeunt AB & Kk* → «alla fine, quando AB e Kk si riuniscono»: è il passaggio al limite.
- *spatia descripta Ak, Kl, Lm*: le sigle indicano le aree AKkB, KLlk, LMml per le diagonali. Motte conserva le stesse sigle.
- *Concipe* (imperativo) → «immagina».
- **Aggiunta di Motte:** «since the squares of the velocities **were shewn above** to be as their differences»; il latino ha solo *cum … fuerint etiam*.
- Corollari: nel Cor. 3 *vi uniformi centripetæ* → «forza centripeta uniforme»; *in cadente corpore* → «in un corpo che cade». Nel Cor. 5 *in medio similari resistente* → «in un mezzo omogeneo resistente».

### A.2 Proposizione VI

**Latino:** *Corpora sphærica homogenea & æqualia, resistentiis in duplicata ratione velocitatum impedita, & solis viribus insitis incitata, temporibus, quæ sunt reciproce ut velocitates sub initio, describunt semper æqualia spatia, & amittunt partes velocitatum proportionales totis.*

**Inglese:** “Homogeneous and equal spherical bodies, opposed by resistances that are in the duplicate ratio of the velocities, and moving on by their innate force only, will, in times which are reciprocally as the velocities at the beginning, describe equal spaces, and lose parts of their velocities proportional to the wholes.”

**Scelte.** *incitata* → «mossi»; *proportionales totis* → «proporzionali alle velocità intere». *dividendo* (operazione delle proporzioni) → «separando». La trascrizione spezza *æquan‹242›tur*; nessuna perdita.

### A.3 Proposizione VII

**Latino:** *Corpora sphærica quibus resistitur in duplicata ratione velocitatum, temporibus, quæ sunt ut motus primi directe & resistentiæ primæ inverse, amittent partes motuum proportionales totis, & spatia describent temporibus istis & velocitatibus primis conjunctim proportionalia.*

**Inglese:** “If spherical bodies are resisted in the duplicate ratio of their velocities, in times which are as the first motions directly, and the first resistances inversely, they will lose parts of their motions proportional to the wholes, and will describe spaces proportional to those times and the first velocities conjunctly.”

**Scelte.** *motus* è sempre «quantità di moto» (è la grandezza che si perde in parti). *Cor. 3*: *cubi diametrorum ad dignitatem illam applicati* → «i cubi dei diametri divisi per quella potenza» (glossario: *applicare ad*). La trascrizione ha *Dn*, *D3−n*: letti Dⁿ, D³⁻ⁿ; Motte (SVG 372–373) ha D³⁻ⁿ, E³⁻ⁿ. *per hanc propositionem* → «per questa proposizione».

### A.4 Lemma II

**Latino:** *Momentum genitæ æquatur momentis laterum singulorum generantium in eorundem laterum indices dignitatum & coefficientia continue ductis.*

**Inglese:** “The moment of any genitum is equal to the moments of each of the generating sides drawn into the indices of the powers of those sides, and into their co-efficients continually.”

**Scelte.**

- *genita* → «quantità generata» (glossario del Libro II); *momentum* → «momento»; *fluxiones* → «flussioni» (unica occorrenza).
- *Cave tamen intellexeris* → «Bada però di non intendere»: imperativo negativo di seconda persona, conservato.
- *prima nascentium proportio* → «la prima proporzione dei [momenti] nascenti»: il genitivo plurale sottintende *momentorum*; l’integrazione è tra parentesi quadre. Motte: «their first proportion, as nascent».
- *Lateris … coefficiens est quantitas, quæ oritur applicando genitam ad hoc latus* → «dividendo la quantità generata per questo lato».
- **Formule.** La trascrizione appiattisce frazioni ed esponenti: «A12» = A^(1/2), «A32» = A^(3/2), «12aA−12» = ½aA^(−1/2), «Anm» = A^(n/m), «nmaAn−mm» = (n/m)aA^((n−m)/m), «12a» = ½a, «14ab» = ¼ab, «1A» = 1/A, «−aA2» = −a/A², «1An» = 1/Aⁿ, «−naAn+1» = −na/Aⁿ⁺¹, «a2A12» = a/(2A^(1/2)), «mnaAm−nn» = (m/n)aA^((m−n)/n), «A3B2» = A³/B². Tutte le letture sono confermate dalle formule di Motte (SVG 374–429, 2, 223, 342), viste una per una: **nessun errore di Motte nel Lemma II**.
- Il Cor. 1 ha nella trascrizione «−2A{,} −B»: artefatto di marcatura, letto «−2A, −B».
- La dimostrazione del Caso 1 per semimomenti dà la differenza aB + bA **esatta**, senza il termine ab: è la scelta che permette a Newton di non trascurare nulla (N5).

**Motte (testo).** Motte riordina la definizione («not made by addition or subduction of divers parts, but is generated…») senza cambiare il senso; rende *momentanea* con «momentaneous». Nessuna omissione.

### A.5 Scolio al Lemma II: la lettera a Collins

**Scelte.**

- *ad D. J. Collinium nostratem* → «al signor J. Collins, nostro connazionale»; *D.* è *Dominum*. **Motte omette *nostratem*.**
- *Slusius* → Sluse (René-François de Sluse); *Huddenius* → Hudde (Johann Hudde). Le forme moderne non sono nel testo; quelle latine sono qui.
- *citra molestum ullum calculum* → «senza alcun calcolo fastidioso».
- *curvitatibus* → «curvature»; Motte «crookedness».
- *æquationum exegesin instituo* → «conduco la risoluzione delle equazioni»; Motte «working in equations».
- La citazione della lettera è chiusa da *Hactenus epistola*: la traduzione la mette tra virgolette.

**Differenze rispetto alle edizioni precedenti.** Le fonti allegate (latino 1726 e Motte 1846, che traduce il 1726) **non permettono di stabilire alcuna differenza di edizione**: Motte e il latino coincidono, e una loro divergenza non sarebbe comunque una differenza fra edizioni. Si osserva soltanto, sulle fonti, che **nello Scolio del 1726 Leibniz non è nominato**: i nomi sono Collins, Sluse e Hudde. Da conoscenza generale, *non verificata sulle fonti allegate*: nelle edizioni del 1687 e del 1713 lo Scolio parlava invece del carteggio di circa dieci anni prima con Leibniz, riconoscendogli un metodo simile; la versione del 1726, con la sola lettera a Collins del 1672, fu sostituita dopo la disputa sulla priorità del calcolo. Per confermarlo servono il testo del 1687 e del 1713 (registro del lavoro successivo).

### A.6 Proposizione VIII

**Latino:** *Si corpus in medio uniformi, gravitate uniformiter agente, recta ascendat vel descendat, & spatium totum descriptum distinguatur in partes æquales, inque principiis singularum partium (addendo resistentiam medii ad vim gravitatis, quando corpus ascendit, vel subducendo ipsam quando corpus descendit) investigentur vires absolutæ; dico quod vires illæ absolutæ sunt in progressione geometrica.*

**Inglese:** “If a body in an uniform medium, being uniformly acted upon by the force of gravity, ascends or descends in a right line; and the whole space described be distinguished into equal parts, and in the beginning of each of the parts (by adding or subducting the resisting force of the medium to or from the force of gravity, when the body ascends or descends) you collect the absolute forces; I say, that those absolute forces are in a geometrical progression.”

**Scelte.** *recta* (avverbio) → «in linea retta». *indenfinitam* → refuso probabile della trascrizione per *indefinitam*. «2APQ» → 2AP×PQ (momento di AP², Lemma II, Caso 3; Motte stampa anch’egli «2APQ»). *ut AP in KC* → «come AP per KC». *per motus leg. II.* → «per la Legge II del moto». Motte: «the **force of** resistance» per *resistentia* (aggiunta lieve).

### A.7 Proposizione IX

**Latino:** *Positis jam demonstratis, dico quod, si tangentes angulorum sectoris circularis & sectoris hyperbolici sumantur velocitatibus proportionales, existente radio justæ magnitudinis: erit tempus omne ascendendi ad locum ut sector circuli, & tempus omne descendendi a loco ut sector hyperbolæ.*

**Inglese:** “Supposing what is above demonstrated, I say, that if the tangents of the angles of the sector of a circle, and of an hyperbola, be taken proportional to the velocities, the radius being of a fit magnitude, all the time of the ascent to the highest place will be as the sector of the circle, and all the time of descending from the highest place as the sector of the hyperbola.”

**Scelte e divergenze.**

- *ad locum / a loco* senza *summum* nell’enunciato: integrato «[più alto]», come fa la dimostrazione (*ad locum summum*). Motte integra senza segnalarlo.
- **Errore di Motte: «whose axis is AK»** per *axem habens AX*. K sta sulla retta AC, perpendicolare all’asse: l’asse dell’iperbole di centro D e vertice A è la retta DA prolungata, su cui cade X (DX² − TX² = AD² nel Caso 2). La lettera latina è corretta.
- Caso 1: «qDp×tD quad.pD quad.» = qDp×tD²/pD²; «pqCk» = pq/Ck; «12AD×pq» = ½AD×pq. Ak e Ck usano la k minuscola della salita: Ap² = AD×Ak e Ck = AC + Ak è la forza assoluta in salita (gravità più resistenza, Prop. VIII).
- Caso 2: «PDQ×ACCK» = PDQ×AC/CK; «PQCK» = PQ/CK. La trascrizione spezza *incremen‹250›to*.
- Cor. 1: *ipsus* → refuso probabile per *ipsius*; *rurfus* → refuso probabile per *rursus* (s lunga). «12PQ», «14AC» = ½PQ, ¼AC. *per corol. i. lem. II hujus* → «per il Cor. 1 del Lemma II di questo libro». Motte: «areas ABNK and **ADT**» per *ATD* (stesso settore, lettere permutate).
- Cor. 6: *per corol. 2. & 3. theor. VI. lib. II.* → «per i Cor. 2 e 3 del Teorema VI del Libro II [cioè della Prop. VIII]». Il Teorema VI è la Prop. VIII: il Cor. 2 dà la velocità massima AC, il Cor. 3 la ricava dalla resistenza nota. Rimando verificato.
- Cas 1 senza punto nella trascrizione («Cas 1.»): tipografico.

### A.8 Proposizione X

**Latino:** *Tendat uniformis vis gravitatis directe ad planum horizontis, sitque resistentia ut medii densitas & quadratum velocitatis conjunctim: requiritur tum medii densitas in locis singulis, quæ faciat ut corpus in data quavis linea curva moveatur, tum corporis velocitas & medii resistentia in locis singulis.*

**Inglese:** “Suppose the uniform force of gravity to tend directly to the plane of the horizon, and the resistance to be as the density of the medium and the square of the velocity conjunctly: it is proposed to find the density of the medium in each place, which shall make the body move in any given curve line; the velocity of the body and the resistance of the medium in each place.”

**Scelte e divergenze.**

- *plano schematis* → «al piano della figura». *occurens* → refuso probabile per *occurrens*.
- *sagittæ* → «saette»; **Motte: «versed sines»** (stessa confusione segnalata nel Fascicolo 5).
- *quas corpus … describere posset* (singolare): Motte «which **the bodies** would describe» (plurale).
- *ut Galilæus demonstravit* → «come ha dimostrato Galileo»; *in vacuo* → «nel vuoto».
- *ordinate cuilibet AF* (Cor. 1) → refuso probabile per *ordinatæ*.
- Formule della dimostrazione: lette come nel § A.10 e controllate con le SVG 442–468 di Motte (errori di Motte nel § A.11).

### A.9 Esempi della Prop. X

- **Es. 1.** *dic AQ, n; AC, a; CH, e;, & CD, o* (punteggiatura «e;,» della trascrizione); *per methodum nostram* → «con il nostro metodo» (il metodo delle serie). **«velocitas autem erit ut CH»**: la trascrizione non ha la radice; Motte (SVG 481) ha **√CH**, e il calcolo dà v² ∝ (1+QQ)/R = 2CH (N9). Tradotto «√CH».
- **Es. 2.** La serie DI = (ac − aa)/b + ((c − 2a)/b)o − oo/b: rispetto alla forma P − Qo − Roo, Q vale −(c − 2a)/b; Newton dice «il secondo termine … al posto di Qo» senza curarsi del segno, che non conta (S = 0).
- **Es. 3.** «VZ æqualis mna−o¯» = (m/n)(a − o) (il trattino alto è il vincolo). *ratio … ponatur esse mn* → «sia quello di m a n». Motte: «a body **let go** from the place A» per *emissum* («lanciato»): attenuazione; «XZand» refuso tipografico di Motte 1846.
- **Es. 4.** *Ponatur indefinite* → «Si ponga, in modo indeterminato». «bbA−O¯n» = bb/(A − O)ⁿ; i segni «−+» davanti agli ultimi due termini di GD sono un artefatto della trascrizione (letti «−», come in Motte SVG 509). La trascrizione spezza *æqua‹259›lis*.

### A.10 Letture delle formule appiattite (Prop. X e Scolio)

| Luogo | Trascrizione | Lettura | Conferma |
|---|---|---|---|
| II.S2.47 | GHT, HIt, GHT−HIt | GH/T, HI/t, GH/T − HI/t | Motte SVG 442–444 |
| II.S2.47 | 2NIt; MI×NIHI; 2MI×NIt×HI | 2NI/t; MI×NI/HI; 2MI×NI/(t×HI) | SVG 445–448 |
| II.S2.47 | t×GHT−HI+2MI×NIHI | t×GH/T − HI + 2MI×NI/HI | SVG 451 |
| II.S2.48 | o1+QQ∓QRoo1+QQ | o√(1+QQ) ∓ QRoo/√(1+QQ) | SVG 454 (453 errata, A.11) |
| II.S2.48 | tT est R+3SoR seu R+32SoR | t/T = √((R+3So)/R) ≈ (R + (3/2)So)/R | SVG 455, 457 (456 errata) |
| II.S2.48 | 3Soo2R1+QQ; 3S1+QQ | (3Soo/2R)√(1+QQ); 3S√(1+QQ) | SVG 459, 460 |
| II.S2.49–50 | HNqNI seu 1+QQR; SR1+QQ | HN²/NI, (1+QQ)/R; S/(R√(1+QQ)) | SVG 461–464 |
| II.S2.51 | HTAC; HTACR; S×ACR×HT | HT/AC; HT/(AC√R); S×AC/(R×HT) | SVG 465–468 |
| II.S2.56 | ane; ae; ACCH; **ut CH** | a/ne; a/e; AC/CH; **√CH** | SVG 479–481 |
| II.S2.61 | bba4bba31+mmnn−2mbbnaa+b4a4 | (bb/a⁴)/((bb/a³)√(1 + mm/nn − 2mbb/naa + b⁴/a⁴)) | SVG 498 |
| II.S2.63 | n+23A2+ddeeA2−2dnbbeAnA+nnb4A2n | (n+2)/(3√(A² + (dd/ee)A² − (2dnbb/eAⁿ)A + nnb⁴/A²ⁿ)) | SVG 515 |
| II.S2.64–65 | SR4−n2×AC¯HTn−1; S2R4−n | (S/R^((4−n)/2))×(AC/HT)ⁿ⁻¹; S²/R⁴⁻ⁿ | SVG 521–523 (524 errata) |
| II.S2.67–68 | GTqGV; AHqAI (velocità) | √(GT²/GV); √(AH²/AI) | SVG 526, 528 |
| II.S2.67–68 | 2nn+2nn+2 in GV | ((2nn + 2n)/(n + 2))×GV | SVG 527, 529 |
| II.S2.71 | longitudine AHqAI | AH²/AI (senza radice: è una lunghezza) | SVG 530 |
| II.S2.75 | **ut AH ad 2AI** | tradotto «2AI» come nella trascrizione | **Motte SVG 532: (4/3)AI**; vedi A.12 |
| II.S2.77 | 2GTqnn−n¯×VG; 2nn−2nn−2VG | 2GT²/((nn − n)×VG); ((2nn − 2n)/(n − 2))×VG | SVG 534, 535 |

### A.11 Formule di Motte 1846 che non tornano con il latino

Tutte le SVG della sezione (372–535, più 2, 223, 342) sono state controllate. Sono **corrette** tutte le formule del Lemma II (374–429) e della Prop. VII (372–373). Non tornano:

| SVG | Luogo | Motte 1846 | Latino 1726 (e calcolo) |
|---|---|---|---|
| 434 | Prop. IX, Caso 1 | AD² + AD AD × Ak (AD ripetuto) | AD² + AD×Ak |
| 453 | Prop. X | o·1/√(1+QQ) − QRoo/√(1+QQ) | o√(1+QQ) − QRoo/√(1+QQ) (la SVG 454, gemella, è giusta) |
| 456 | Prop. X | √(R+3So)/R | √((R+3So)/R) |
| 469 | Es. 1 | … − ao²/2e³ − … | … − ao³/2e³ − … (verificato con lo sviluppo in serie) |
| 501 | Es. 3 | (mm/nn)aa − 2mbb/**a** + b⁴/**a⁴** | mmaa/nn − 2mbb/**n** + b⁴/**aa** (quadrato di ZY) |
| 524 | Scolio | **S³**/R⁴⁻ⁿ | S²/R⁴⁻ⁿ (quadrato di S/R^((4−n)/2)) |

Nella resa LaTeX dell’EPUB alcune formule hanno «QR_{oo}», «S_o» come pedici (453, 454, 456, 459): è un artefatto della codifica, non un errore di contenuto. Non ho potuto stabilire se gli errori della tabella risalgano a Motte 1729 o all’edizione del 1846 (Motte 1729, vol. II, non consultato).

**Formule SVG da controllare:** nessuna rimasta non vista. Restano da confrontare su Motte 1729 le sei formule della tabella precedente e la SVG 532.

### A.12 Refusi e anomalie della trascrizione latina

| Luogo | Trascrizione | Lettura | Tipo |
|---|---|---|---|
| II.S2.26 | −2A{,} −B | −2A, −B | artefatto di marcatura |
| II.S2.31 | *indenfinitam* | *indefinitam* | refuso probabile |
| II.S2.37 | *Cas 1.* | *Cas. 1.* | tipografico |
| II.S2.39 | *ipsus*; *rurfus* | *ipsius*; *rursus* | refusi probabili (il secondo da s lunga) |
| II.S2.47 | *occurens* | *occurrens* | refuso probabile |
| II.S2.51 | *ordinate cuilibet* | *ordinatæ* | refuso probabile |
| II.S2.54 | *CH, e;, & CD* | *CH, e; & CD* | punteggiatura |
| II.S2.48 | *&CH−DI* | *& CH−DI* | spaziatura |
| II.S2.56 | *velocitas autem erit ut CH* | √CH | **radice perduta** (Motte SVG 481 e calcolo) |
| II.S2.63 | *−+nn+n2…*, *−+n3+…* | − | artefatto |
| II.S2.66 | *Quoniam motus non sit in parabola* | *fit* | refuso probabile (s lunga) |
| II.S2.75 | *ex phænominis* | *phænomenis* | refuso probabile |
| II.S2.75 | *ut AH ad 2AI* | (4/3)AI secondo la formula generale con n = 1 e secondo Motte | **da verificare sulla stampa** (N13) |
| II.S2.76 | *punctum K.Q.E.I.* | *K. Q.E.I.* | spaziatura |
| II.S2.77 | *per quae* | *per quæ* | grafia |
| passim | radici e frazioni appiattite | § A.10 | artefatto della pagina web |

**Punti da controllare sulla stampa ECCO.**

| Pagina 1726 | Trascrizione | Lettura attesa | Motivo |
|---|---|---|---|
| 247 | *indenfinitam* | *indefinitam* | refuso |
| 250, 251 | *ipsus*; *rurfus* | *ipsius*; *rursus* | refusi |
| 252 | *occurens* | *occurrens* | refuso |
| 254 | *ordinate cuilibet AF* | *ordinatæ* | refuso |
| 256 | *velocitas autem erit ut CH* | √CH | radice: la stampa ha probabilmente il segno di radice |
| 260 | *Quoniam motus non sit* | *fit* | s lunga |
| 263 | *phænominis* | *phænomenis* | refuso |
| 263 | *ut AH ad 2AI* | (4/3)AI? | discordanza con la formula generale e con Motte (N13) |
| 248 | *axem habens AX* | AX | controllare che la stampa non abbia AK (Motte) |
| 263 | *angulis diversis HAK, hAK* | hAK o hAk | Motte ha hAk |

### A.13 Riepilogo: dove Motte aggiunge, omette o sbaglia (testo)

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| II.S2.02 | *cum … fuerint* | «were **shewn above**» | aggiunta |
| II.S2.29 | *nostratem* | — | omissione |
| II.S2.29 | *curvitatibus*; *exegesin* | «crookedness»; «working in equations» | resa libera |
| II.S2.31 | *resistentia* | «the **force of** resistance» | aggiunta |
| II.S2.36 | *axem habens AX* | «whose axis is **AK**» | **lettera errata** |
| II.S2.39 | *ATD* (area intera) | «ADT» | lettere permutate (stesso settore) |
| II.S2.47 | *corpus … posset* | «the bodies would» | numero |
| II.S2.48 | *sagittæ* | «versed sines» | **termine errato** |
| II.S2.61 | *emissum* | «let go» | attenuazione |
| II.S2.61 | — | «XZand» | refuso tipografico 1846 |
| II.S2.72 | *in ratione **paulo minore*** | «in a ratio a little **greater**» | **senso rovesciato** (N14) |
| II.S2.75 | *graphice* | «graphically, **or by scale and compass**» | aggiunta |
| II.S2.75 | *HAK, hAK* | «HAK, hAk» | lettera diversa (stesso angolo se K, k sono sulla stessa orizzontale) |
| II.S2.76 | *H, H*; *NAH, NAH* | «H, h»; «NAH, NAh» | distinzione aggiunta |

### A.14 Rimandi

- **Al Libro I:** nessun rimando esplicito in questa sezione (ricerca su tutto il latino: nessun *lib. i.*, *prop.* o *lem.* del Libro I). Nessuna verifica sui Fascicoli 04–12 è stata quindi necessaria.
- **Interni al Libro II e altri, verificati:** Legge II del moto (II.S2.31); Lemma II, Casi 1 e 3 (II.S2.21, II.S2.24); Lemma II, Cor. 1 (II.S2.39: con AC dato, i momenti di AK e AP stanno come 2AK e AP); Teorema VI = Prop. VIII, Cor. 2 e 3 (II.S2.44); Regola 6 e Regola 4 (II.S2.75); «per questa proposizione» (Prop. VII, Cor. 1, 4, 5). Tutti reggono l’uso che ne fa Newton.
- **Rimandi impliciti:** nella Regola 8 l’uguaglianza AM = KN è la Regola 6, non citata; nella Prop. VIII il momento 2AP×PQ è il Lemma II, Caso 3, non citato.

---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. Le verifiche sono nello script `tmp/14/verifica14.py` (Python, sympy e numpy): **71 controlli, tutti superati**.

### N1. Prop. V: la resistenza quadratica senza gravità

Con *dv/dt* = −*kv*² si ha *v* = *v*₀/(1 + *kv*₀*t*): la velocità è un’iperbole nel tempo, contato da un’origine C posta a distanza CA = 1/(*kv*₀) prima dell’istante iniziale. Lo spazio è l’area sotto l’iperbole, *s* = (1/*k*) ln(1 + *kv*₀*t*), cioè un logaritmo: tempi in progressione geometrica (contati da C) danno spazi uguali. Verificato numericamente con rapporto 1,5. Il Cor. 3 è la sottotangente: AT = AC = *v*₀/(*kv*₀²), il tempo in cui la resistenza iniziale, se costante, annullerebbe la velocità.

### N2. Prop. VII e corollari

La legge di scala è dimensionale: con resistenza ∝ *D*ⁿ*v*² e quantità di moto ∝ *D*³*v*, la lunghezza caratteristica di smorzamento è ∝ *D*³⁻ⁿ (Cor. 3), cioè ∝ *D* per la resistenza «di superficie» *D*² (Cor. 1). Nel linguaggio moderno è la lunghezza *m*/(½ρ*C*_D*A*).

### N3. Prop. VIII: forze assolute

La «forza assoluta» è la forza netta: *g* − *kv*² in discesa, *g* + *kv*² in salita. Con *d*(*v*²)/*ds* = 2(*g* − *kv*²) la forza netta decresce esponenzialmente con lo spazio, *F* = *g*·exp(−2*ks*): spazi uguali danno forze in progressione geometrica, anche in salita (verificato). La linea AC rappresenta insieme la gravità e la velocità limite *V* = √(*g*/*k*) (Cor. 2): è il senso di AP media proporzionale fra AK e AC.

### N4. Prop. IX: tangente e tangente iperbolica

Con l’iperbole equilatera di semiasse AD = *V*, il settore iperbolico di «tangente» AP = *v* ha area ½*V*²·artanh(*v*/*V*), e il tempo di discesa è (*V*/*g*)·artanh(*v*/*V*): proporzionale al settore. In salita il settore circolare dà (*V*/*g*)·arctan(*v*/*V*), il tempo totale di salita. Verificato, con la stessa scala per i due settori. È la prima comparsa nei *Principia* delle funzioni oggi dette iperboliche.

### N5. Lemma II: momenti e derivate

Il lemma è la regola del prodotto e della potenza: il momento è la derivata (o il differenziale) e il «coefficiente» è la derivata parziale divisa per l’indice. Sono stati verificati simbolicamente i 17 momenti dell’enunciato e dei Casi, il Cor. 1 (momenti ∝ −2A, −B, 0, D, 2E, 3F) e il Cor. 3. Il Caso 1 evita il termine ab prendendo gli incrementi a metà prima e a metà dopo: la differenza (A + ½a)(B + ½b) − (A − ½a)(B − ½b) è **esattamente** aB + bA. Il Caso 5 deriva la potenza fratta per derivazione implicita; il Caso 6 non dimostra il caso di indici irrazionali, che il testo non menziona.

### N6. Lo Scolio: che cosa dicono le fonti

Lo Scolio del 1726 rivendica a Newton, con la lettera del 10 dicembre 1672 e il trattato del 1671, un metodo generale delle tangenti e delle curvature fondato sul Lemma II. Le fonti allegate non contengono le versioni del 1687 e del 1713 (vedi A.5).

### N7. Prop. X: verifica meccanica indipendente

Per una curva *y*(*x*) data, la componente normale della gravità fornisce *v*² = *g*(1 + *y*′²)/(−*y*″) e il bilancio tangenziale fornisce la decelerazione dovuta alla resistenza; il rapporto con *g* è stato confrontato con la regola di Newton 3S√(1+QQ) : 4RR, calcolata dai coefficienti della serie nel verso del moto. Coincidono per il semicerchio, per la parabola (resistenza nulla) e per le iperboli dell’Es. 4 con n = 1, 3/2, 2. Anche la catena simbolica della dimostrazione (archi, saette Roo e Roo + 3So³, t/T, l’espressione (3Soo/2R)√(1+QQ)) è stata verificata con sympy fino all’ordine o².

### N8. La saetta

*Sagitta* è la freccia dell’arco: il segmento fra il punto medio della corda e l’arco. Qui sono le saette degli archi GI e HK, misurate lungo le ordinate.

### N9. Es. 1: velocità come √CH

Per il semicerchio il lato retto (1+QQ)/R vale 2CH, e la velocità, il cui quadrato è proporzionale al lato retto, sta come √CH. La trascrizione ha «CH»: è la radice perduta, come in molti altri luoghi della pagina web. Il resto dell’esempio torna: densità ∝ HT e resistenza : gravità = 3AC : PQ (verificato in tre punti). Partendo da P con AC dall’altra parte del centro la densità risulta negativa, come dice Newton.

### N10. Es. 3–4 e lo Scolio: le iperboli

Verificati: densità ∝ 1/XY con VY = n×VG; resistenza : gravità = XY : ((2nn + 2n)/(n + 2))VG (per n = 1, 3XY : 2YG); lato retto 2XY²/((nn + n)VG). Per le «parabole» VG ∝ XVⁿ del capoverso finale, con il corpo che si allontana da X: resistenza GT : ((2nn − 2n)/(n − 2))VG, lato retto 2GT²/((nn − n)VG), densità ∝ 1/GT (verificato per n = 5/2, 3, 4). Per n = 2 la parabola conica dà resistenza nulla.

### N11. Regole 5, 6 e 8

Regola 5: HX : AI = n + 1 : 1 (verificato per n = 1, 2). Regola 6: NK = AM per l’iperbole conica (verificato). Regola 8: con A nell’origine e AK orizzontale, H soddisfa (x_K − x_H)·y_H = x_K·AI; l’iperbole di asintoti AK, KF che passa per H ha dunque la coniugata per C = (0, −AI). Verificato algebricamente.

### N12. Scolio: resistenza come Vⁿ

La regola generalizzata, densità ∝ (S/R^((4−n)/2))×(AC/HT)ⁿ⁻¹, segue dividendo la resistenza richiesta, che dipende solo dalla geometria, per *v*ⁿ con *v*² ∝ (1+QQ)/R. Verificato numericamente (fattore costante 3/4).

### N13. Regola 7: «AH ad 2AI»

La Regola 7 usa l’iperbole conica (n = 1, Regola 6). La formula generale del capoverso II.S2.68 dà allora resistenza : gravità = AH : (4/3)AI, non AH : 2AI. Motte (SVG 532) stampa (4/3)AI. La trascrizione ha «2AI»: va controllata la stampa del 1726. Se la stampa ha «2AI», è un residuo da segnalare in nota alla pagina; la traduzione, per ora, segue la trascrizione.

### N14. Regola 4: «paulo minore» o «a little greater»

Il latino aumenta la densità in A in un rapporto «un poco minore» di (AH + GT_min)/(2GT_min), cioè fino a poco meno della media aritmetica fra la densità in A e quella al vertice; Motte scrive «a little greater». Le fonti non permettono di decidere quale fosse l’intenzione. La traduzione segue il latino.

### N15. Il problema inverso

La Prop. X è un problema inverso (dalla traiettoria alla densità), non il problema diretto del proiettile in un mezzo uniforme. Lo Scolio lo dice: la traiettoria vera è «di genere iperbolico» e le iperboli proposte sono approssimazioni pratiche.

---

## Controllo della copertura

Pagine 1726 dai marcatori ‹n› della trascrizione; per Motte, «sezione corrispondente» (l’estratto non ha marcatori di pagina).

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| II.S2.01–II.S2.02 | *Si corpori resistitur in velocitatis ratione duplicata* | Prop. V, enunciato e dimostrazione | pp. 239–240 | sez. corrisp. |
| II.S2.03–II.S2.07 | *Patet ergo quod* … *Et viceversa* | Prop. V, Cor. 1–5 | pp. 240–241 | sez. corrisp. |
| II.S2.08–II.S2.09 | *Corpora sphærica homogenea & æqualia* | Prop. VI | pp. 241–242 | sez. corrisp. |
| II.S2.10–II.S2.16 | *Corpora sphærica quibus resistitur* | Prop. VII e Cor. 1–5 | pp. 242–243 | sez. corrisp. |
| II.S2.17–II.S2.19 | *Momentum genitæ æquatur* | Lemma II, enunciato, definizioni, senso | pp. 243–244 | sez. corrisp. |
| II.S2.20–II.S2.25 | *Rectangulum quodvis* … *Igitur genitæ cujuscunque* | Lemma II, Casi 1–6 | pp. 244–245 | sez. corrisp. |
| II.S2.26–II.S2.28 | *Hinc in continue proportionalibus* … | Lemma II, Cor. 1–3 | pp. 245–246 | sez. corrisp. |
| II.S2.29 | *In epistola quadam ad D. J. Collinium* | Scolio al Lemma II | p. 246 | sez. corrisp. |
| II.S2.30–II.S2.34 | *Si corpus in medio uniformi* | Prop. VIII e Cor. 1–3 | pp. 246–248 | sez. corrisp. |
| II.S2.35–II.S2.38 | *Positis jam demonstratis* | Prop. IX, costruzione, Casi 1–2 | pp. 248–250 | sez. corrisp. |
| II.S2.39–II.S2.45 | *Hinc si AB æquetur quartæ parti* … *Et regrediendo* | Prop. IX, Cor. 1–7 | pp. 250–251 | sez. corrisp. |
| II.S2.46–II.S2.50 | *Tendat uniformis vis gravitatis* | Prop. X, soluzione | pp. 252–254 | sez. corrisp. |
| II.S2.51–II.S2.52 | *Si tangens HN producatur* … *Et hinc, si curva linea* | Prop. X, Cor. 1–2 | p. 254 | sez. corrisp. |
| II.S2.53–II.S2.57 | *Sit linea PFHQ semicirculus* | Es. 1 | pp. 254–256 | sez. corrisp. |
| II.S2.58–II.S2.59 | *Sit linea PFQ parabola* | Es. 2 | pp. 256–257 | sez. corrisp. |
| II.S2.60–II.S2.61 | *Sit linea AGK hyperbola* | Es. 3 | pp. 257–258 | sez. corrisp. |
| II.S2.62–II.S2.63 | *Ponatur indefinite* | Es. 4 | pp. 258–259 | sez. corrisp. |
| II.S2.64–II.S2.68 | *Eadem ratione qua prodiit densitas* … *Proinde si corpus de loco A* | Scolio, parte generale | pp. 259–261 | sez. corrisp. |
| II.S2.69–II.S2.76 | *Si servetur tum medii densitas* … *Inventis longitudinibus AH, HX* | Scolio, Regole 1–8 | pp. 261–264 | sez. corrisp. |
| II.S2.77 | *Quæ de hyperbolis dicta sunt* | Scolio, parabole | p. 264 | sez. corrisp. |

**Controlli eseguiti.**

1. **Copertura.** Ho riletto in sequenza ogni periodo della trascrizione, da *De motu corporum quibus resistitur* a *per quae projectile transibit*, contro la traduzione: nessuna frase manca. I periodi molto lunghi (Prop. X, Es. 3–4) sono tradotti per membri senza omissioni. Per le 116 frasi della Parte B la corrispondenza latino–italiano è garantita per costruzione: il testo tradotto e i passi sono generati dagli stessi dati. I 77 identificatori sono consecutivi e unici.
2. **Parte B.** `check.py` sul file finale: esito nel messaggio di consegna.
3. **Matematica.** `verifica14.py`, 71 controlli superati (N1–N12): Lemma II simbolico; Propp. V, VIII, IX con i corollari principali; Prop. X simbolica e meccanica; Es. 1–4; Scolio (Vⁿ, Regole 5, 6, parabole); Regola 8 algebrica. Discordanze trovate: «2AI» della Regola 7 (N13); «ut CH» dell’Es. 1 (radice perduta, N9).
4. **Motte.** Confronto di tutta la sezione e di tutte le formule SVG (A.11, A.13).
5. **Tabelle numeriche:** la sezione non contiene tabelle né esempi con cifre (gli «esempi» della Prop. X sono simbolici).

**Non ho potuto verificare:**

- la stampa del 1726 (punti elencati in A.12) e le figure NATP00088-8…24: le disposizioni dei punti in `figura_base` sono ricostruite dal testo; in particolare la posizione di P, Q nella Prop. VIII e di k nella Prop. IX;
- Motte 1729, per attribuire gli errori di formula (A.11) e «a little greater» (N14);
- le versioni del 1687 e del 1713 dello Scolio al Lemma II (A.5);
- la paginazione di Motte 1846.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Libro II, Sezione II (Propp. V–X, Lemma II e Scolii) | **Fascicolo 14, presente documento, prima versione** |
| Regola 7, «2AI» / (4/3)AI | Da controllare sulla stampa del 1726 (p. 263) |
| Es. 1, √CH | Da controllare sulla stampa (p. 256); traduzione già con √ |
| Refusi della trascrizione (A.12) | Da verificare sulla scansione ECCO |
| Formule errate di Motte 1846 (A.11) e Regola 4 | Da confrontare con Motte 1729, vol. II |
| Scolio al Lemma II nelle edizioni 1687 e 1713 | Da reperire per documentare la variante (Leibniz) |
| Figure NATP00088-8…24 | Da consultare per `figura_base` |
| Revisione filologica e scientifica indipendente | Da eseguire |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce traduzioni moderne. **Licenza prevista** (decisione del curatore): testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project; i testi di Motte sono di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Unità incluse: le proposizioni con dimostrazione e figura (V, VI, VIII, IX, X), i corollari con dimostrazione geometrica propria (Prop. V, Cor. 3; Prop. IX, Cor. 1), gli Esempi 1–4 della Prop. X, la Regola 8 dello Scolio (costruzione con dimostrazione) e, benché senza figura, il **Lemma II** (fondamento del calcolo dei momenti). **Escluse:** la Prop. VII (argomento per rapporti, senza figura), i corollari senza dimostrazione propria, le Regole 1–7 (enunciati pratici; la Regola 7 potrebbe diventare una pagina-esperimento).

Convenzioni:

- `la`: testo esatto della trascrizione, con spazi normalizzati e senza i marcatori ‹n› e [FIG n]; refusi e frazioni appiattite compresi (letture nel § A.10);
- `it`: la traduzione di questo fascicolo;
- `en`: Motte 1846, con i marcatori `[SVG n]` delle formule (ignorati da check.py; contenuti nel § A.10–A.11);
- `dipende_da`: soltanto i rimandi citati nella frase latina;
- `figura.mostra`: elementi da rendere visibili, cumulativi; `figura.evidenzia`: relazioni da mettere in risalto.

```json
{
 "fascicolo": "14-L2-S2",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase latina",
  "en": "Motte 1846, allineato per senso; le formule stampate come immagini compaiono come [SVG n] (ignorate da check.py)",
  "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione",
  "la": ""
 },
 "unita": [
  {
   "id": "L2-P5",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. V — resistenza come v²: tempi in progressione geometrica, spazi uguali",
   "copertura": [
    "II.S2.01",
    "II.S2.02"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Section II (sezione corrispondente; l’estratto non ha marcatori di pagina)"
   },
   "enunciato": {
    "la": "",
    "it": "Se un corpo incontra una resistenza in rapporto duplicato della velocità e si muove per la sola forza insita in un mezzo omogeneo, e se i tempi si prendono in progressione geometrica, procedendo dai termini minori ai maggiori, dico che le velocità all’inizio dei singoli tempi sono nella stessa progressione geometrica, inversamente, e che sono uguali gli spazi descritti nei singoli tempi.",
    "en": "If a body is resisted in the duplicate ratio of its velocity, and moves by its innate force only through a similar medium; and the times be taken in a geometrical progression, proceeding from less to greater terms: I say, that the velocities at the beginning of each of the times are in the same geometrical progression inversely; and that the spaces are equal, which are described in each of the times."
   },
   "figura_base": {
    "punti": [
     "C",
     "D",
     "H",
     "A",
     "K",
     "L",
     "M",
     "B",
     "k",
     "l",
     "m",
     "G"
    ],
    "vincoli": [
     "CD, CH asintoti ortogonali",
     "iperbole BklmG di centro C: CA×AB = CK×Kk = …",
     "AB, Kk, Ll, Mm perpendicolari a CD",
     "CA, CK, CL, CM in progressione geometrica (ultimo passo)"
    ]
   },
   "passi": [
    {
     "id": "L2-P5-p1",
     "la": "",
     "it": "Infatti, poiché la resistenza del mezzo è proporzionale al quadrato della velocità e il decremento della velocità è proporzionale alla resistenza, se si divide il tempo in innumerevoli particelle uguali, i quadrati delle velocità all’inizio dei singoli tempi saranno proporzionali alle differenze delle velocità stesse.",
     "en": "For since the resistance of the medium is proportional to the square of the velocity, and the decrement of the velocity is proportional to the resistance: if the time be divided into innumerable equal particles, the squares of the velocities at the beginning of each of the times will be proportional to the differences of the same velocities.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "resistenza ∝ v²",
       "decremento di v ∝ resistenza"
      ]
     },
     "nota": "Passo senza figura: premessa fisica."
    },
    {
     "id": "L2-P5-p2",
     "la": "",
     "it": "Siano AK, KL, LM, ecc. quelle particelle di tempo, prese sulla retta CD, e si innalzino le perpendicolari AB, Kk, Ll, Mm, ecc., che incontrino in B, k, l, m, ecc. l’iperbole BklmG, descritta con centro C e con gli asintoti ortogonali CD, CH: AB starà a Kk come CK sta a CA; e, separando, AB − Kk starà a Kk come AK sta a CA; e, permutando, AB − Kk starà ad AK come Kk sta a CA, e quindi come AB×Kk sta ad AB×CA.",
     "en": "Let those particles of time be AK, KL, LM, &c., taken in the right line CD; and erect the perpendiculars AB, Kk, Ll, Mm, &c., meeting the hyperbola BklmG, described with the centre C, and the rectangular asymptotes CD, CH, in B, k, l, m, &c.; then AB will be to Kk as CK to CA, and, by division, AB - Kk to Kk as AK to CA, and alternately, AB - Kk to AK as Kk to CA; and therefore as AB × Kk to AB × CA.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "C",
       "asintoti CD, CH",
       "iperbole BklmG",
       "A, K, L, M su CD",
       "perpendicolari AB, Kk, Ll, Mm"
      ],
      "evidenzia": [
       "AB : Kk = CK : CA"
      ]
     }
    },
    {
     "id": "L2-P5-p3",
     "la": "",
     "it": "Di qui, poiché AK e AB×CA sono dati, AB − Kk sarà come AB×Kk; e alla fine, quando AB e Kk si riuniscono, come AB².",
     "en": "Therefore since AK and AB × CA are given, AB - Kk will be as AB × Kk; and, lastly, when AB and Kk coincide, as AB2.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "AB − Kk ∝ AB×Kk → AB²"
      ]
     }
    },
    {
     "id": "L2-P5-p4",
     "la": "",
     "it": "E con un argomento simile Kk − Ll, Ll − Mm, ecc. saranno come Kk², Ll², ecc.",
     "en": "And, by the like reasoning, Kk - Ll, Ll - Mm, &c., will be as Kk2, Ll2, &c.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "Kk − Ll ∝ Kk²",
       "Ll − Mm ∝ Ll²"
      ]
     }
    },
    {
     "id": "L2-P5-p5",
     "la": "",
     "it": "Dunque i quadrati delle linee AB, Kk, Ll, Mm stanno come le loro differenze; e perciò, poiché anche i quadrati delle velocità stavano come le loro differenze, la progressione delle une e delle altre sarà simile.",
     "en": "Therefore the squares of the lines AB, Kk, Ll, Mm, &c., are as their differences; and, therefore, since the squares of the velocities were shewn above to be as their differences, the progression of both will be alike.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "le ordinate si comportano come le velocità"
      ]
     }
    },
    {
     "id": "L2-P5-p6",
     "la": "",
     "it": "Dimostrato ciò, ne segue anche che le aree descritte da queste linee sono in una progressione del tutto simile a quella degli spazi descritti con le velocità.",
     "en": "This being demonstrated it follows also that the areas described by these lines are in a like progression with the spaces described by these velocities.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "aree AKkB, KLlk, LMml"
      ],
      "evidenzia": [
       "aree ↔ spazi"
      ]
     }
    },
    {
     "id": "L2-P5-p7",
     "la": "",
     "it": "Dunque, se la velocità all’inizio del primo tempo AK si rappresenta con la linea AB, la velocità all’inizio del secondo, KL, con la linea Kk, e la lunghezza descritta nel primo tempo con l’area AKkB, tutte le velocità successive saranno rappresentate dalle linee successive Ll, Mm, ecc., e le lunghezze descritte dalle aree Kl, Lm, ecc.",
     "en": "Therefore if the velocity at the beginning of the first time AK be expounded by the line AB, and the velocity at the beginning of the second time KL by the line Kk and the length described in the first time by the area AKkB, all the following velocities will be expounded by the following lines Ll, Mm, &c. and the lengths described, by the areas Kl, Lm, &c.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "AB, Kk, Ll, Mm = velocità",
       "AKkB, Kl, Lm = spazi"
      ]
     }
    },
    {
     "id": "L2-P5-p8",
     "la": "",
     "it": "E, componendo, se il tempo intero si rappresenta con AM, somma delle sue parti, la lunghezza intera descritta sarà rappresentata da AMmB, somma delle sue parti.",
     "en": "And, by composition, if the whole time be expounded by AM, the sum of its parts, the whole length described will be expounded by AMmB the sum of its parts.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area AMmB"
      ],
      "evidenzia": [
       "AM = tempo totale",
       "AMmB = spazio totale"
      ]
     }
    },
    {
     "id": "L2-P5-p9",
     "la": "",
     "it": "Immagina ora che il tempo AM sia diviso nelle parti AK, KL, LM, ecc. in modo che CA, CK, CL, CM, ecc. siano in progressione geometrica: quelle parti saranno nella stessa progressione, le velocità AB, Kk, Ll, Mm, ecc. nella stessa progressione inversa, e gli spazi descritti Ak, Kl, Lm, ecc. uguali. C.V.D.",
     "en": "Now conceive the time AM to be divided into the parts AK, KL, LM, &c. so that CA, CK, CL, CM, &c. may be in a geometrical progression; and those parts will be in the same progression, and the velocities AB, Kk, Ll, Mm, &c., will be in the same progression inversely, and the spaces described Ak, Kl, Lm, &c., will be equal. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "CA, CK, CL, CM in progressione geometrica"
      ],
      "evidenzia": [
       "aree Ak, Kl, Lm uguali (proprietà dell’iperbole)"
      ]
     },
     "nota": "«Ak» indica l’area AKkB (diagonale A–k), come Kl, Lm."
    }
   ]
  },
  {
   "id": "L2-P5-Cor3",
   "tipo": "Corollarium",
   "titolo": "Prop. V, Cor. 3 — la resistenza iniziale dalla sottotangente",
   "copertura": [
    "II.S2.05"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Section II (sezione corrispondente; l’estratto non ha marcatori di pagina)"
   },
   "enunciato": {
    "la": "",
    "it": "È data anche la resistenza del mezzo, stabilendo che proprio all’inizio del moto essa sia uguale alla forza centripeta uniforme che, in un corpo che cade in un mezzo non resistente, potrebbe generare nel tempo AC la velocità AB.",
    "en": "The resistance of the medium is also given, by making it equal, in the very beginning of the motion, to an uniform centripetal force, which could generate, in a body falling through a non-resisting medium, the velocity AB in the time AC."
   },
   "figura_base": {
    "punti": [
     "C",
     "A",
     "B",
     "T"
    ],
    "vincoli": [
     "BT tangente all’iperbole in B",
     "T sull’asintoto CD",
     "AT = AC"
    ]
   },
   "passi": [
    {
     "id": "L2-P5-Cor3-p1",
     "la": "",
     "it": "Se infatti si conduce BT tangente all’iperbole in B, che incontri l’asintoto in T, la retta AT sarà uguale ad AC e rappresenterà il tempo nel quale la resistenza iniziale, continuata uniformemente, potrebbe togliere l’intera velocità AB.",
     "en": "For if BT be drawn touching the hyperbola in B, and meeting the asymptote in T, the right line AT will be equal to AC, and will express the time in which the first resistance, uniformly continued, may take away the whole velocity AB.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tangente BT",
       "T sull’asintoto"
      ],
      "evidenzia": [
       "AT = AC (sottotangente dell’iperbole)"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P6",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. VI — globi uguali: tempi inversamente come le velocità iniziali",
   "copertura": [
    "II.S2.08",
    "II.S2.09"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Section II (sezione corrispondente; l’estratto non ha marcatori di pagina)"
   },
   "enunciato": {
    "la": "",
    "it": "Corpi sferici omogenei e uguali, ostacolati da resistenze in rapporto duplicato delle velocità e mossi soltanto dalle forze insite, in tempi che sono inversamente come le velocità iniziali descrivono sempre spazi uguali e perdono parti delle velocità proporzionali alle velocità intere.",
    "en": "Homogeneous and equal spherical bodies, opposed by resistances that are in the duplicate ratio of the velocities, and moving on by their innate force only, will, in times which are reciprocally as the velocities at the beginning, describe equal spaces, and lose parts of their velocities proportional to the wholes."
   },
   "figura_base": {
    "punti": [
     "C",
     "A",
     "a",
     "D",
     "d",
     "B",
     "b",
     "E",
     "e"
    ],
    "vincoli": [
     "CD, CH asintoti ortogonali",
     "iperbole BbEe",
     "Aa : Dd = DE : AB"
    ]
   },
   "passi": [
    {
     "id": "L2-P6-p1",
     "la": "",
     "it": "Descritta con gli asintoti ortogonali CD, CH un’iperbole qualsiasi BbEe, che tagli in B, b, E, e le perpendicolari AB, ab, DE, de, si rappresentino le velocità iniziali con le perpendicolari AB, DE e i tempi con le linee Aa, Dd.",
     "en": "To the rectangular asymptotes CD, CH describe any hyperbola BbEe, cutting the perpendiculars AB, ab, DE, de in B, b, E, e; let the initial velocities be expounded by the perpendiculars AB, DE, and the times by the lines Aa, Dd.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "C",
       "asintoti CD, CH",
       "iperbole BbEe",
       "perpendicolari AB, ab, DE, de"
      ],
      "evidenzia": [
       "AB, DE velocità iniziali",
       "Aa, Dd tempi"
      ]
     }
    },
    {
     "id": "L2-P6-p2",
     "la": "",
     "it": "Dunque Aa sta a Dd come (per ipotesi) DE sta ad AB, e come (per la natura dell’iperbole) CA sta a CD; e, componendo, come Ca sta a Cd.",
     "en": "Therefore as Aa is to Dd, so (by the hypothesis) is DE to AB, and so (from the nature of the hyperbola) is CA to CD; and, by composition, so is Ca to Cd.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "Aa : Dd = DE : AB = CA : CD = Ca : Cd"
      ]
     },
     "nota": "«per ipotesi» e «per la natura dell’iperbole» non sono rimandi a proposizioni: dipende_da vuoto."
    },
    {
     "id": "L2-P6-p3",
     "la": "",
     "it": "Dunque le aree ABba, DEed, cioè gli spazi descritti, sono uguali fra loro; e le velocità iniziali AB, DE sono proporzionali alle finali ab, de, e perciò, separando, anche alle loro parti perdute AB − ab, DE − de. C.V.D.",
     "en": "Therefore the areas ABba, DEed, that is, the spaces described, are equal among themselves, and the first velocities AB, DE are proportional to the last ab, de; and therefore, by division, proportional to the parts of the velocities lost, AB - ab, DE - de. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "aree ABba, DEed"
      ],
      "evidenzia": [
       "ABba = DEed",
       "AB : ab = DE : de"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-Lem2",
   "tipo": "Lemma",
   "titolo": "Lemma II — il momento della quantità generata",
   "copertura": [
    "II.S2.17",
    "II.S2.18",
    "II.S2.19",
    "II.S2.20",
    "II.S2.21",
    "II.S2.22",
    "II.S2.23",
    "II.S2.24",
    "II.S2.25"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Section II (sezione corrispondente; l’estratto non ha marcatori di pagina)"
   },
   "enunciato": {
    "la": "",
    "it": "Il momento di una quantità generata è uguale ai momenti dei singoli lati generanti moltiplicati successivamente per gli indici delle potenze di quei lati e per i loro coefficienti.",
    "en": "The moment of any genitum is equal to the moments of each of the generating sides drawn into the indices of the powers of those sides, and into their co-efficients continually."
   },
   "figura_base": {
    "punti": [],
    "vincoli": [
     "pagina algebrica: nessuna figura nel testo"
    ]
   },
   "passi": [
    {
     "id": "L2-Lem2-p1",
     "la": "",
     "it": "Un rettangolo qualsiasi AB, accresciuto con moto perpetuo, quando ai lati A e B mancavano le metà dei momenti, ½a e ½b, era (A − ½a) per (B − ½b), ossia AB − ½aB − ½bA + ¼ab; e non appena i lati A e B sono stati accresciuti delle altre metà dei momenti, diventa (A + ½a) per (B + ½b), ossia AB + ½aB + ½bA + ¼ab.",
     "en": "Any rectangle, as AB, augmented by a perpetual flux, when, as yet, there wanted of the sides A and B half their moments [SVG 401] and [SVG 402], was [SVG 403] into [SVG 404], or [SVG 405]; but as soon as the sides A and B are augmented by the other half moments, the rectangle becomes [SVG 406] into [SVG 407], or [SVG 408].",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "(A − ½a)(B − ½b)",
       "(A + ½a)(B + ½b)"
      ]
     },
     "nota": "Nessuna figura: pagina algebrica. La trascrizione appiattisce ½, ¼ in «12», «14»."
    },
    {
     "id": "L2-Lem2-p2",
     "la": "",
     "it": "Da questo rettangolo si sottragga il rettangolo precedente, e resterà l’eccesso aB + bA.",
     "en": "From this rectangle subduct the former rectangle, and there will remain the excess aB + bA.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "differenza = aB + bA (esatta)"
      ]
     }
    },
    {
     "id": "L2-Lem2-p3",
     "la": "",
     "it": "Dunque con gli incrementi interi a e b dei lati si genera l’incremento aB + bA del rettangolo. C.V.D.",
     "en": "Therefore with the whole increments a and b of the sides, the increment aB + bA of the rectangle is generated. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "momento di AB = aB + bA"
      ]
     }
    },
    {
     "id": "L2-Lem2-p4",
     "la": "",
     "it": "Si ponga AB sempre uguale a G: il momento del contenuto ABC, ossia GC, sarà (per il Caso 1) gC + cG, cioè (se al posto di G e g si scrivono AB e aB + bA) aBC + bAC + cAB.",
     "en": "Suppose AB always equal to G, and then the moment of the content ABC or GC (by Case 1) will be gC + cG, that is (putting AB and aB + bA for G and g), aBC + bAC + cAB.",
     "dipende_da": [
      "Lemma II, Caso 1"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "GC con G = AB"
      ]
     }
    },
    {
     "id": "L2-Lem2-p5",
     "la": "",
     "it": "E lo stesso ragionamento vale per il contenuto sotto un numero qualsiasi di lati. C.V.D.",
     "en": "And the reasoning is the same for contents under ever so many sides. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-Lem2-p6",
     "la": "",
     "it": "Si pongano i lati A, B, C sempre uguali fra loro: il momento aB + bA di A², cioè del rettangolo AB, sarà 2aA, e il momento aBC + bAC + cAB di A³, cioè del contenuto ABC, sarà 3aA².",
     "en": "Suppose the sides A, B, and C, to be always equal among themselves; and the moment aB + bA, of [SVG 374], that is, of the rectangle AB, will be 2aA; and the moment aBC + bAC + cAB of [SVG 375], that is, of the content ABC, will be [SVG 383].",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "A = B = C"
      ]
     }
    },
    {
     "id": "L2-Lem2-p7",
     "la": "",
     "it": "E con lo stesso argomento il momento di una potenza qualsiasi Aⁿ è naAⁿ⁻¹. C.V.D.",
     "en": "And by the same reasoning the moment of any power [SVG 409] is [SVG 410]. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "momento di Aⁿ = naAⁿ⁻¹ (n intero)"
      ]
     }
    },
    {
     "id": "L2-Lem2-p8",
     "la": "",
     "it": "Di qui, poiché 1/A per A fa 1, il momento di 1/A moltiplicato per A, insieme con 1/A moltiplicato per a, sarà il momento di 1, cioè nulla.",
     "en": "Therefore since [SVG 411] into A is 1, the moment of [SVG 411] drawn into A, together with [SVG 411] drawn into a, will be the moment of 1, that is, nothing.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "(1/A)·A = 1"
      ]
     }
    },
    {
     "id": "L2-Lem2-p9",
     "la": "",
     "it": "Perciò il momento di 1/A, ossia di A⁻¹, è −a/A².",
     "en": "Therefore the moment of [SVG 411], or of [SVG 381], is [SVG 412].",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-Lem2-p10",
     "la": "",
     "it": "E in generale, poiché 1/Aⁿ per Aⁿ fa 1, il momento di 1/Aⁿ moltiplicato per Aⁿ, insieme con 1/Aⁿ per naAⁿ⁻¹, sarà nulla.",
     "en": "And generally since [SVG 413] into [SVG 409] is 1, the moment of [SVG 413] drawn into [SVG 409] together with [SVG 413] into [SVG 410] will be nothing.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-Lem2-p11",
     "la": "",
     "it": "E perciò il momento di 1/Aⁿ, ossia di A⁻ⁿ, sarà −na/Aⁿ⁺¹. C.V.D.",
     "en": "And, therefore, the moment of [SVG 413] or [SVG 414] will be [SVG 415]. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "momento di A⁻ⁿ = −na/Aⁿ⁺¹"
      ]
     }
    },
    {
     "id": "L2-Lem2-p12",
     "la": "",
     "it": "E poiché A^(1/2) per A^(1/2) fa A, il momento di A^(1/2) moltiplicato per 2A^(1/2) sarà a, per il Caso 3; e perciò il momento di A^(1/2) sarà a/(2A^(1/2)), ossia ½aA^(−1/2).",
     "en": "And since [SVG 377] into [SVG 377] is [SVG 2], the moment of [SVG 377] drawn into [SVG 416] will be a (by Case 3); and, therefore, the moment of [SVG 377] will be [SVG 417] or [SVG 385].",
     "dipende_da": [
      "Lemma II, Caso 3"
     ],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-Lem2-p13",
     "la": "",
     "it": "E in generale, se si pone A^(m/n) uguale a B, Aᵐ sarà uguale a Bⁿ, e quindi maAᵐ⁻¹ uguale a nbBⁿ⁻¹, e maA⁻¹ uguale a nbB⁻¹, ossia a nbA^(−m/n); e quindi (m/n)aA^((m−n)/n) uguale a b, cioè al momento di A^(m/n). C.V.D.",
     "en": "And, generally, putting [SVG 342] equal to [SVG 418], then [SVG 419] will be equal to [SVG 420], and therefore [SVG 421] equal to [SVG 422], and [SVG 423] equal to [SVG 424], or [SVG 425]; and therefore [SVG 426] is equal to b, that is, equal to the moment of [SVG 342]. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "A^(m/n) = B ⇒ Aᵐ = Bⁿ"
      ]
     },
     "nota": "Il passaggio «e quindi maAᵐ⁻¹ uguale a nbBⁿ⁻¹» usa il Caso 3 senza citarlo di nuovo."
    },
    {
     "id": "L2-Lem2-p14",
     "la": "",
     "it": "Dunque il momento di una quantità generata qualsiasi AᵐBⁿ è il momento di Aᵐ moltiplicato per Bⁿ, insieme con il momento di Bⁿ moltiplicato per Aᵐ, cioè maAᵐ⁻¹Bⁿ + nbBⁿ⁻¹Aᵐ; e ciò sia che gli indici m e n delle potenze siano numeri interi o fratti, sia che siano affermativi o negativi.",
     "en": "Therefore the moment of any generated quantity [SVG 427] is the moment of [SVG 428] drawn into [SVG 420], together with the moment of [SVG 420] drawn into [SVG 428], that is, [SVG 429]; and that whether the indices m and n of the powers be whole numbers or fractions, affirmative or negative.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Il «Dunque» combina il Caso 1 (prodotto) con i Casi 3–5 (potenze), senza citarli."
    },
    {
     "id": "L2-Lem2-p15",
     "la": "",
     "it": "E lo stesso ragionamento vale per il contenuto sotto più potenze. C.V.D.",
     "en": "And the reasoning is the same for contents under more powers. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    }
   ],
   "nota": "Incluso, benché senza figura, per richiesta del coordinatore (fondamento del calcolo dei momenti). Le formule di Motte sono tutte immagini SVG (374–429), controllate: corrette."
  },
  {
   "id": "L2-P8",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. VIII — moto verticale: forze assolute in progressione geometrica",
   "copertura": [
    "II.S2.30",
    "II.S2.31"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Section II (sezione corrispondente; l’estratto non ha marcatori di pagina)"
   },
   "enunciato": {
    "la": "",
    "it": "Se un corpo, in un mezzo uniforme, sotto l’azione uniforme della gravità, sale o scende in linea retta, e lo spazio totale descritto si divide in parti uguali, e all’inizio delle singole parti si cercano le forze assolute (aggiungendo la resistenza del mezzo alla forza di gravità quando il corpo sale, o sottraendola quando il corpo scende), dico che quelle forze assolute sono in progressione geometrica.",
    "en": "If a body in an uniform medium, being uniformly acted upon by the force of gravity, ascends or descends in a right line; and the whole space described be distinguished into equal parts, and in the beginning of each of the parts (by adding or subducting the resisting force of the medium to or from the force of gravity, when the body ascends or descends) you collect the absolute forces; I say, that those absolute forces are in a geometrical progression."
   },
   "figura_base": {
    "punti": [
     "A",
     "C",
     "K",
     "L",
     "P",
     "Q",
     "H",
     "B",
     "N",
     "O",
     "S",
     "I",
     "M",
     "i",
     "k",
     "l",
     "m",
     "n",
     "o"
    ],
    "vincoli": [
     "AC gravità (data)",
     "AK resistenza, KC forza assoluta in discesa",
     "AP² = AK×AC",
     "CA, CH asintoti ortogonali",
     "iperbole BNS: CA×AB = CK×KN = …"
    ]
   },
   "passi": [
    {
     "id": "L2-P8-p1",
     "la": "",
     "it": "Si rappresenti infatti la forza di gravità con la linea data AC; la resistenza con la linea indefinita AK; la forza assoluta nella discesa del corpo con la differenza KC; la velocità del corpo con la linea AP, che sia media proporzionale fra AK e AC, e quindi in rapporto subduplicato della resistenza; l’incremento della resistenza fatto in una particella di tempo data con la lineetta KL, e l’incremento contemporaneo della velocità con la lineetta PQ; e con centro C e asintoti ortogonali CA, CH si descriva un’iperbole qualsiasi BNS, che incontri in B, N, O le perpendicolari innalzate AB, KN, LO.",
     "en": "For let the force of gravity be expounded by the given line AC; the force of resistance by the indefinite line AK; the absolute force in the descent of the body by the difference KC; the velocity of the body by a line AP, which shall be a mean proportional between AK and AC, and therefore in a subduplicate ratio of the resistance; the increment of the resistance made in a given particle of time by the lineola KL, and the contemporaneous increment of the velocity by the lineola PQ; and with the centre C, and rectangular asymptotes CA, CH, describe any hyperbola BNS meeting the erected perpendiculars AB, KN, LO in B, N and O.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A",
       "C",
       "K, L su AC",
       "P, Q",
       "asintoti CA, CH",
       "iperbole BNS",
       "perpendicolari AB, KN, LO"
      ],
      "evidenzia": [
       "AC gravità",
       "AK resistenza",
       "KC forza assoluta",
       "AP² = AK×AC"
      ]
     },
     "nota": "La trascrizione ha «indenfinitam»: refuso probabile per «indefinitam». La posizione di P e Q (su una retta a parte o sulla stessa AC) non risulta dal testo."
    },
    {
     "id": "L2-P8-p2",
     "la": "",
     "it": "Poiché AK sta come AP², il momento KL della prima starà come il momento 2AP×PQ del secondo, cioè come AP per KC; infatti l’incremento PQ della velocità (per la Legge II del moto) è proporzionale alla forza generante KC.",
     "en": "Because AK is as AP2, the moment KL of the one will be as the moment 2APQ of the other, that is, as AP × KC; for the increment PQ of the velocity is (by Law II) proportional to the generating force KC.",
     "dipende_da": [
      "Legge II",
      "Lemma II (implicito)"
     ],
     "figura": {
      "mostra": [
       "KL",
       "PQ"
      ],
      "evidenzia": [
       "KL ∝ 2AP×PQ ∝ AP×KC"
      ]
     },
     "nota": "«2APQ» della trascrizione è 2AP×PQ (momento del quadrato, Lemma II, Caso 3, non citato)."
    },
    {
     "id": "L2-P8-p3",
     "la": "",
     "it": "Si componga il rapporto di KL con il rapporto di KN, e il rettangolo KL×KN starà come AP×KC×KN; cioè, poiché il rettangolo KC×KN è dato, come AP.",
     "en": "Let the ratio of KL be compounded with the ratio KN, and the rectangle KL × KN will become as AP × KC × KN; that is (because the rectangle KC × KN is given), as AP.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "rettangolo KL×KN"
      ],
      "evidenzia": [
       "KC×KN costante (iperbole)",
       "KL×KN ∝ AP"
      ]
     }
    },
    {
     "id": "L2-P8-p4",
     "la": "",
     "it": "Ma il rapporto ultimo dell’area iperbolica KNOL al rettangolo KL×KN, quando i punti K e L si riuniscono, è di uguaglianza.",
     "en": "But the ultimate ratio of the hyperbolic area KNOL to the rectangle KL × KN becomes, when the points K and L coincide, the ratio of equality.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area KNOL"
      ],
      "evidenzia": [
       "KNOL / (KL×KN) → 1"
      ]
     }
    },
    {
     "id": "L2-P8-p5",
     "la": "",
     "it": "Dunque quell’area iperbolica evanescente sta come AP.",
     "en": "Therefore that hyperbolic evanescent area is as AP.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "KNOL ∝ AP"
      ]
     }
    },
    {
     "id": "L2-P8-p6",
     "la": "",
     "it": "L’intera area iperbolica ABOL si compone dunque delle particelle KNOL, sempre proporzionali alla velocità AP, e perciò è proporzionale allo spazio descritto con quella velocità.",
     "en": "Therefore the whole hyperbolic area ABOL is composed of particles KNOL which are always proportional to the velocity AP; and therefore is itself proportional to the space described with that velocity.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area ABOL"
      ],
      "evidenzia": [
       "area ABOL ∝ spazio percorso"
      ]
     }
    },
    {
     "id": "L2-P8-p7",
     "la": "",
     "it": "Si divida ora quell’area in parti uguali ABMI, IMNK, KNOL, ecc.: le forze assolute AC, IC, KC, LC, ecc. saranno in progressione geometrica. C.V.D.",
     "en": "Let that area be now divided into equal parts, as ABMI, IMNK, KNOL, &c., and the absolute forces AC, IC, KC, LC, &c., will be in a geometrical progression. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "I, M",
       "aree ABMI, IMNK, KNOL"
      ],
      "evidenzia": [
       "aree uguali ⇒ CA, CI, CK, CL in progressione geometrica"
      ]
     }
    },
    {
     "id": "L2-P8-p8",
     "la": "",
     "it": "E con un argomento simile, nella salita del corpo, prendendo dalla parte opposta del punto A le aree uguali ABmi, imnk, knol, ecc., risulterà che le forze assolute AC, iC, kC, lC, ecc. sono in proporzione continua.",
     "en": "And by a like reasoning, in the ascent of the body, taking, on the contrary side of the point A, the equal areas ABmi, imnk, knol, &c., it will appear that the absolute forces AC, iC, kC, lC, &c., are continually proportional.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "i, k, l oltre A, dalla parte opposta a C",
       "aree ABmi, imnk, knol"
      ],
      "evidenzia": [
       "salita: forza assoluta = gravità + resistenza"
      ]
     }
    },
    {
     "id": "L2-P8-p9",
     "la": "",
     "it": "E perciò, se si prendono uguali tutti gli spazi, in salita e in discesa, tutte le forze assolute lC, kC, iC, AC, IC, KC, LC, ecc. saranno in proporzione continua. C.V.D.",
     "en": "Therefore if all the spaces in the ascent and descent are taken equal, all the absolute forces lC, kC, iC, AC, IC, KC, LC, &c., will be continually proportional. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "un’unica progressione geometrica per salita e discesa"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P9",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. IX — tempi di salita e discesa come settori circolare e iperbolico",
   "copertura": [
    "II.S2.35",
    "II.S2.36",
    "II.S2.37",
    "II.S2.38"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Section II (sezione corrispondente; l’estratto non ha marcatori di pagina)"
   },
   "enunciato": {
    "la": "",
    "it": "Posto quanto si è già dimostrato, dico che, se le tangenti degli angoli di un settore circolare e di un settore iperbolico si prendono proporzionali alle velocità, essendo il raggio di grandezza opportuna, l’intero tempo della salita fino al luogo [più alto] sarà come il settore del cerchio, e l’intero tempo della discesa dal luogo [più alto] come il settore dell’iperbole.",
    "en": "Supposing what is above demonstrated, I say, that if the tangents of the angles of the sector of a circle, and of an hyperbola, be taken proportional to the velocities, the radius being of a fit magnitude, all the time of the ascent to the highest place will be as the sector of the circle, and all the time of descending from the highest place as the sector of the hyperbola."
   },
   "figura_base": {
    "punti": [
     "A",
     "C",
     "D",
     "E",
     "t",
     "T",
     "V",
     "Z",
     "X",
     "p",
     "P",
     "q",
     "Q",
     "v",
     "k",
     "K"
    ],
    "vincoli": [
     "AD ⊥ AC, AD = AC",
     "cerchio di centro D e raggio AD (quadrante AtE)",
     "iperbole equilatera di centro D, vertice A, asintoto DC",
     "p, P sulla tangente in A (perpendicolare a AD)",
     "Ap, AP proporzionali alle velocità"
    ]
   },
   "passi": [
    {
     "id": "L2-P9-p1",
     "la": "",
     "it": "Alla retta AC, con cui si rappresenta la forza di gravità, si conduca perpendicolare e uguale AD.",
     "en": "To the right line AC, which expresses the force of gravity, let AD be drawn perpendicular and equal.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A",
       "C",
       "D",
       "AD ⊥ AC, AD = AC"
      ],
      "evidenzia": [
       "AC gravità"
      ]
     }
    },
    {
     "id": "L2-P9-p2",
     "la": "",
     "it": "Con centro D e semidiametro AD si descrivano sia il quadrante di cerchio AtE, sia l’iperbole rettangola AVZ, che ha per asse AX, per vertice principale A e per asintoto DC.",
     "en": "From the centre D with the semi-diameter AD describe as well the quadrant AtE of a circle, as the rectangular hyperbola AVZ, whose axis is AK, principal vertex A, and asymptote DC.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "quadrante AtE",
       "iperbole AVZ (centro D, vertice A)",
       "asintoto DC",
       "asse DAX"
      ],
      "evidenzia": [
       "DX² − TX² = AD² sull’iperbole"
      ]
     },
     "nota": "Motte scrive «whose axis is AK»; il latino ha AX (apparato A.9)."
    },
    {
     "id": "L2-P9-p3",
     "la": "",
     "it": "Si conducano Dp, DP: il settore circolare AtD starà come l’intero tempo della salita fino al luogo più alto, e il settore iperbolico ATD come l’intero tempo della discesa dal luogo più alto; purché le tangenti dei settori, Ap e AP, stiano come le velocità.",
     "en": "Let Dp, DP be drawn; and the circular sector AtD will be as all the time of the ascent to the highest place; and the hyperbolic sector ATD as all the time of descent from the highest place; if so be that the tangents Ap, AP of those sectors be as the velocities.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "p, P sulla tangente in A",
       "Dp, DP",
       "t = Dp ∩ cerchio",
       "T = DP ∩ iperbole",
       "settori AtD, ATD"
      ],
      "evidenzia": [
       "Ap, AP velocità"
      ]
     }
    },
    {
     "id": "L2-P9-p4",
     "la": "",
     "it": "Si conduca infatti Dvq, che stacchi i momenti del settore ADt e del triangolo ADp, cioè le particelle piccolissime tDv e qDp descritte nello stesso tempo.",
     "en": "Draw Dvq cutting off the moments or least particles tDv and qDp, described in the same time, of the sector ADt and of the triangle ADp.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Dvq",
       "particelle tDv, qDp"
      ],
      "evidenzia": [
       "momenti del settore e del triangolo"
      ]
     }
    },
    {
     "id": "L2-P9-p5",
     "la": "",
     "it": "Poiché queste particelle, per l’angolo comune D, stanno in rapporto duplicato dei lati, la particella tDv starà come qDp×tD²/pD², cioè, poiché tD è data, come qDp/pD².",
     "en": "Since those particles (because of the common angle D) are in a duplicate ratio of the sides, the particle tDv will be as [SVG 430], that is (because tD is given), as [SVG 431].",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "tDv : qDp = tD² : pD²"
      ]
     }
    },
    {
     "id": "L2-P9-p6",
     "la": "",
     "it": "Ma pD² è AD² + Ap², cioè AD² + AD×Ak, ossia AD×Ck; e qDp è ½AD×pq.",
     "en": "But [SVG 432] is [SVG 433], that is, [SVG 434], or [SVG 435]; and qDp is [SVG 436].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "k sulla retta CA prolungata oltre A"
      ],
      "evidenzia": [
       "Ap² = AD×Ak (salita)",
       "Ck = AC + Ak"
      ]
     },
     "nota": "In salita la resistenza Ak si aggiunge alla gravità: Ck è la forza assoluta (Prop. VIII). La posizione di k non è descritta nel testo."
    },
    {
     "id": "L2-P9-p7",
     "la": "",
     "it": "Dunque la particella tDv del settore sta come pq/Ck; cioè direttamente come il decremento piccolissimo pq della velocità e inversamente come la forza Ck che diminuisce la velocità; e perciò come la particella di tempo che corrisponde al decremento.",
     "en": "Therefore tDv, the particle of the sector, is as [SVG 437]; that is, as the least decrement pq of the velocity directly, and the force Ck which diminishes the velocity, inversely; and therefore as the particle of time answering to the decrement of the velocity.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "tDv ∝ pq/Ck ∝ dt"
      ]
     }
    },
    {
     "id": "L2-P9-p8",
     "la": "",
     "it": "E, componendo, la somma di tutte le particelle tDv nel settore ADt diventa come la somma delle particelle di tempo che corrispondono alle singole particelle pq perdute dalla velocità decrescente Ap, finché quella velocità, diminuita fino a nulla, sia svanita; cioè l’intero settore ADt sta come l’intero tempo della salita fino al luogo più alto. C.V.D.",
     "en": "And, by composition, the sum of all the particles tDv in the sector ADt will be as the sum of the particles of time answering to each of the lost particles pq of the decreasing velocity Ap, till that velocity, being diminished into nothing, vanishes; that is, the whole sector ADt is as the whole time of ascent to the highest place. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "settore ADt intero"
      ],
      "evidenzia": [
       "settore ADt ∝ tempo totale di salita"
      ]
     }
    },
    {
     "id": "L2-P9-p9",
     "la": "",
     "it": "Si conduca DQV, che stacchi sia del settore DAV sia del triangolo DAQ le particelle piccolissime TDV e PDQ: queste particelle staranno fra loro come DT² sta a DP², cioè (se TX e AP sono parallele) come DX² sta a DA², o TX² ad AP², e, separando, come DX² − TX² sta a DA² − AP².",
     "en": "Draw DQV cutting off the least particles TDV and PDQ of the sector DAV, and of the triangle DAQ; and these particles will be to each other as DT2 to DP2, that is (if TX and AP are parallel), as DX2 to DA2 or TX2 to AP2; and, by division, as DX2 - TX2 to DA2 - AP2.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "DQV",
       "particelle TDV, PDQ",
       "X sull’asse, TX ∥ AP"
      ],
      "evidenzia": [
       "TDV : PDQ = DT² : DP²"
      ]
     }
    },
    {
     "id": "L2-P9-p10",
     "la": "",
     "it": "Ma per la natura dell’iperbole DX² − TX² è AD², e per ipotesi AP² è AD×AK.",
     "en": "But, from the nature of the hyperbola, DX2 - TX2 is AD2; and, by the supposition, AP2 is AD × AK.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "K su AC"
      ],
      "evidenzia": [
       "DX² − TX² = AD²",
       "AP² = AD×AK"
      ]
     }
    },
    {
     "id": "L2-P9-p11",
     "la": "",
     "it": "Dunque le particelle stanno fra loro come AD² sta ad AD² − AD×AK, cioè come AD sta ad AD − AK, ossia come AC sta a CK; e perciò la particella TDV del settore è PDQ×AC/CK; e quindi, poiché AC e AD sono date, sta come PQ/CK, cioè direttamente come l’incremento della velocità e inversamente come la forza che genera l’incremento; e perciò come la particella di tempo che corrisponde all’incremento.",
     "en": "Therefore the particles are to each other as AD2 to AD2 - AD × AK; that is, as AD to AD - AK or AC to CK: and therefore the particle TDV of the sector is [SVG 438]; and therefore (because AC and AD are given) as [SVG 439]; that is, as the increment of the velocity directly, and as the force generating the increment inversely; and therefore as the particle of the time answering to the increment.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "TDV ∝ PQ/CK ∝ dt"
      ]
     },
     "nota": "La trascrizione spezza «incremen‹250›to»: nel campo la resta «incremen to»."
    },
    {
     "id": "L2-P9-p12",
     "la": "",
     "it": "E, componendo, la somma delle particelle di tempo nelle quali si generano tutte le particelle PQ della velocità AP diventa come la somma delle particelle del settore ADT, cioè il tempo intero come il settore intero. C.V.D.",
     "en": "And, by composition, the sum of the particles of time, in which all the particles PQ of the velocity AP are generated, will be as the sum of the particles of the sector ATD; that is, the whole time will be as the whole sector. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "settore ADT intero"
      ],
      "evidenzia": [
       "settore ADT ∝ tempo di discesa"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P9-Cor1",
   "tipo": "Corollarium",
   "titolo": "Prop. IX, Cor. 1 — spazio di caduta come area ABNK",
   "copertura": [
    "II.S2.39"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Section II (sezione corrispondente; l’estratto non ha marcatori di pagina)"
   },
   "enunciato": {
    "la": "",
    "it": "Di qui, se AB è uguale alla quarta parte di AC, lo spazio che un corpo descrive cadendo in un tempo qualsiasi starà allo spazio che il corpo potrebbe descrivere nello stesso tempo procedendo uniformemente con la velocità massima AC come l’area ABNK, con cui si rappresenta lo spazio descritto cadendo, sta all’area ATD, con cui si rappresenta il tempo.",
    "en": "Hence if AB be equal to a fourth part of AC, the space which a body will describe by falling in any time will be to the space which the body could describe, by moving uniformly on in the same time with its greatest velocity AC, as the area ABNK, which expresses the space described in falling to the area ATD, which expresses the time."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "K",
     "L",
     "N",
     "O",
     "P",
     "Q",
     "D",
     "T",
     "V"
    ],
    "vincoli": [
     "AB = AC/4",
     "iperbole BNS della Prop. VIII",
     "AP² = AC×AK"
    ]
   },
   "passi": [
    {
     "id": "L2-P9-Cor1-p1",
     "la": "",
     "it": "Infatti, poiché AC sta ad AP come AP sta ad AK, LK starà a PQ (per il Cor. 1 del Lemma II di questo libro) come 2AK sta ad AP, cioè come 2AP sta ad AC; e di qui LK starà a ½PQ come AP sta a ¼AC, ossia ad AB; e KN sta ad AC, ossia ad AD, come AB sta a CK; perciò, per uguaglianza, LKNO sta a DPQ come AP sta a CK.",
     "en": "For since AC is to AP as AP to AK, then (by Cor. 1, Lem. II, of this Book) LK is to PQ as 2AK to AP, that is, as 2AP to AC, and thence LK is to [SVG 440] as AP to [SVG 441] or AB; and KN is to AC or AD as AB to CK; and therefore, ex æquo, LKNO to DPQ as AP to CK.",
     "dipende_da": [
      "Lemma II, Cor. 1"
     ],
     "figura": {
      "mostra": [
       "iperbole BNS della Prop. VIII con AB = AC/4",
       "LKNO",
       "DPQ"
      ],
      "evidenzia": [
       "LK : PQ = 2AK : AP",
       "KN : AD = AB : CK",
       "LKNO : DPQ = AP : CK"
      ]
     }
    },
    {
     "id": "L2-P9-Cor1-p2",
     "la": "",
     "it": "Ma DPQ stava a DTV come CK sta ad AC.",
     "en": "But DPQ was to DTV as CK to AC.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "dal Caso 2"
      ]
     }
    },
    {
     "id": "L2-P9-Cor1-p3",
     "la": "",
     "it": "Dunque, di nuovo per uguaglianza, LKNO sta a DTV come AP sta ad AC; cioè come la velocità del corpo che cade sta alla velocità massima che il corpo può acquistare cadendo.",
     "en": "Therefore, ex æquo, LKNO is to DTV as AP to AC; that is, as the velocity of the falling body to the greatest velocity which the body by falling can acquire.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "LKNO : DTV = AP : AC"
      ]
     },
     "nota": "«rurfus» è refuso probabile della trascrizione per «rursus»."
    },
    {
     "id": "L2-P9-Cor1-p4",
     "la": "",
     "it": "Poiché dunque i momenti LKNO e DTV delle aree ABNK e ATD stanno come le velocità, tutte le parti di quelle aree generate nello stesso tempo staranno come gli spazi descritti nello stesso tempo, e perciò le aree intere ABNK e ATD, generate dall’inizio, come gli spazi interi descritti dall’inizio della discesa. C.V.D.",
     "en": "Since, therefore, the moments LKNO and DTV of the areas ABNK and ATD are as the velocities, all the parts of those areas generated in the same time will be as the spaces described in the same time; and therefore the whole areas ABNK and ADT, generated from the beginning, will be as the whole spaces described from the beginning of the descent. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "aree ABNK, ATD"
      ],
      "evidenzia": [
       "ABNK : ATD = spazio : (velocità massima × tempo)"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P10",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. X — densità del mezzo per una traiettoria data",
   "copertura": [
    "II.S2.46",
    "II.S2.47",
    "II.S2.48",
    "II.S2.49",
    "II.S2.50"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Section II (sezione corrispondente; l’estratto non ha marcatori di pagina)"
   },
   "enunciato": {
    "la": "",
    "it": "La forza uniforme di gravità tenda direttamente verso il piano dell’orizzonte, e la resistenza stia come la densità del mezzo e il quadrato della velocità considerati congiuntamente: si richiede sia la densità del mezzo nei singoli luoghi, che faccia muovere il corpo lungo una qualsiasi linea curva data, sia la velocità del corpo e la resistenza del mezzo nei singoli luoghi.",
    "en": "Suppose the uniform force of gravity to tend directly to the plane of the horizon, and the resistance to be as the density of the medium and the square of the velocity conjunctly: it is proposed to find the density of the medium in each place, which shall make the body move in any given curve line; the velocity of the body and the resistance of the medium in each place."
   },
   "figura_base": {
    "punti": [
     "P",
     "Q",
     "F",
     "G",
     "H",
     "I",
     "K",
     "B",
     "C",
     "D",
     "E",
     "L",
     "N",
     "M"
    ],
    "vincoli": [
     "PQ orizzontale",
     "GB, HC, ID, KE ordinate verticali",
     "BC = CD = DE = o",
     "GL, HN tangenti in G, H",
     "HCDM parallelogramma"
    ]
   },
   "passi": [
    {
     "id": "L2-P10-p1",
     "la": "",
     "it": "Sia PQ quel piano, perpendicolare al piano della figura; PFHQ una linea curva che incontra questo piano nei punti P e Q; G, H, I, K quattro luoghi del corpo che procede lungo questa curva da F verso Q; GB, HC, ID, KE quattro ordinate parallele condotte da questi punti all’orizzonte, che poggiano sulla linea orizzontale PQ nei punti B, C, D, E; e le distanze BC, CD, DE delle ordinate fra loro siano uguali.",
     "en": "Let PQ be a plane perpendicular to the plane of the scheme itself; PFHQ a curve line meeting that plane in the points P and Q; G, H, I, K four places of the body going on in this curve from F to Q; and GB, HC, ID, KE four parallel ordinates let fall from these points to the horizon, and standing on the horizontal line PQ at the points B, C, D, E; and let the distances BC, CD, DE, of the ordinates be equal among themselves.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "orizzontale PQ",
       "curva PFHQ",
       "G, H, I, K sulla curva",
       "ordinate GB, HC, ID, KE",
       "BC = CD = DE"
      ],
      "evidenzia": [
       "passo costante delle ascisse"
      ]
     },
     "nota": "La trascrizione ha «occurens»: refuso probabile per «occurrens»."
    },
    {
     "id": "L2-P10-p2",
     "la": "",
     "it": "Dai punti G e H si conducano le rette GL, HN tangenti alla curva in G e H, che incontrino in L e N le ordinate CH, DI prolungate verso l’alto, e si completi il parallelogramma HCDM.",
     "en": "From the points G and H let the right lines GL, HN, be drawn touching the curve in G and H, and meeting the ordinates CH, DI, produced upwards, in L and N: and complete the parallelogram HCDM.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tangente GL (L su CH prolungata)",
       "tangente HN (N su DI prolungata)",
       "M: HM ∥ CD, DM ∥ CH"
      ],
      "evidenzia": [
       "LH, NI: scarti fra tangente e curva"
      ]
     }
    },
    {
     "id": "L2-P10-p3",
     "la": "",
     "it": "I tempi nei quali il corpo descrive gli archi GH, HI staranno in rapporto subduplicato delle altezze LH, NI che il corpo potrebbe descrivere in quei tempi cadendo dalle tangenti; e le velocità staranno direttamente come le lunghezze descritte GH, HI e inversamente come i tempi.",
     "en": "And the times in which the body describes the arcs GH, HI, will be in a subduplicate ratio of the altitudes LH, NI, which the bodies would describe in those times, by falling from the tangents; and the velocities will be as the lengths described GH, HI directly, and the times inversely.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "T : t = √LH : √NI",
       "v ∝ arco / tempo"
      ]
     }
    },
    {
     "id": "L2-P10-p4",
     "la": "",
     "it": "Si rappresentino i tempi con T e t, e le velocità con GH/T e HI/t: il decremento della velocità fatto nel tempo t sarà rappresentato da GH/T − HI/t.",
     "en": "Let the times be expounded by T and t, and the velocities by [SVG 442] and [SVG 443]; the decrement of the velocity produced in the time t will be expounded by [SVG 444].",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "decremento = GH/T − HI/t"
      ]
     }
    },
    {
     "id": "L2-P10-p5",
     "la": "",
     "it": "Questo decremento nasce dalla resistenza che ritarda il corpo e dalla gravità che lo accelera.",
     "en": "This decrement arises from the resistance which retards the body, and from the gravity which accelerates it.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P10-p6",
     "la": "",
     "it": "La gravità, in un corpo che cade e che cadendo descrive lo spazio NI, genera una velocità con la quale si sarebbe potuto descrivere nello stesso tempo il doppio di quello spazio, come ha dimostrato Galileo, cioè la velocità 2NI/t; ma in un corpo che descrive l’arco HI essa accresce quell’arco soltanto della lunghezza HI − HN, ossia MI×NI/HI, e perciò genera soltanto la velocità 2MI×NI/(t×HI).",
     "en": "Gravity, in a falling body, which in its fall describes the space NI, produces a velocity with which it would be able to describe twice that space in the same time, as Galileo has demonstrated; that is, the velocity [SVG 445]: but if the body describes the arc HI, it augments that arc only by the length [SVG 446] or [SVG 447]; and therefore generates only the velocity [SVG 448].",
     "dipende_da": [
      "Galileo (caduta dei gravi)"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "componente tangenziale della gravità: fattore MI/HI"
      ]
     }
    },
    {
     "id": "L2-P10-p7",
     "la": "",
     "it": "Si aggiunga questa velocità al decremento detto prima, e si avrà il decremento della velocità che nasce dalla sola resistenza, cioè GH/T − HI/t + 2MI×NI/(t×HI).",
     "en": "Let this velocity be added to the before-mentioned decrement, and we shall have the decrement of the velocity arising from the resistance alone, that is, [SVG 449].",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "decremento dovuto alla resistenza"
      ]
     }
    },
    {
     "id": "L2-P10-p8",
     "la": "",
     "it": "Perciò, poiché la gravità nello stesso tempo genera in un corpo che cade la velocità 2NI/t, la resistenza starà alla gravità come GH/T − HI/t + 2MI×NI/(t×HI) sta a 2NI/t, ossia come t×GH/T − HI + 2MI×NI/HI sta a 2NI.",
     "en": "Therefore since, in the same time, the action of gravity generates, in a falling body, the velocity [SVG 445], the resistance will be to the gravity as [SVG 450] to [SVG 445] or as [SVG 451] to [SVG 452].",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "resistenza : gravità = (t×GH/T − HI + 2MI×NI/HI) : 2NI"
      ]
     }
    },
    {
     "id": "L2-P10-p9",
     "la": "",
     "it": "Ora, al posto delle ascisse CB, CD, CE si scrivano −o, o, 2o.",
     "en": "Now for the abscissas CB, CD, CE, put -o, o, 2o.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "o: passo infinitamente piccolo"
      ]
     }
    },
    {
     "id": "L2-P10-p10",
     "la": "",
     "it": "Al posto dell’ordinata CH si scriva P, e al posto di MI una serie qualsiasi Qo + Roo + So³ + ecc.",
     "en": "For the ordinate CH put P; and for MI put any series Qo + Ro2 + So3 +, &c.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P10-p11",
     "la": "",
     "it": "Tutti i termini della serie dopo il primo, cioè Roo + So³ + ecc., saranno NI; e le ordinate DI, EK e BG saranno rispettivamente P − Qo − Roo − So³ − ecc., P − 2Qo − 4Roo − 8So³ − ecc. e P + Qo − Roo + So³ − ecc.",
     "en": "And all the terms of the series after the first, that is, Ro2 + So3 +, &c., will be NI; and the ordinates DI, EK, and BG will be P - Qo - Ro2 - So3 -, &c., P - 2Qo - 4Ro2 - 8So3 -, &c., and P + Qo - Ro2 + So3 -, &c., respectively.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "NI = Roo + So³",
       "DI, EK, BG come serie in o"
      ]
     }
    },
    {
     "id": "L2-P10-p12",
     "la": "",
     "it": "E, elevando al quadrato le differenze delle ordinate BG − CH e CH − DI, e aggiungendo ai quadrati risultanti i quadrati di BC e CD, si avranno i quadrati degli archi GH, HI: oo + QQoo − 2QRo³ + ecc. e oo + QQoo + 2QRo³ + ecc.",
     "en": "And by squaring the differences of the ordinates BG - CH and CH - DI, and to the squares thence produced adding the squares of BC and CD themselves, you will have oo + QQoo - 2QRo3 +, &c., and oo + QQoo + 2QRo3 +, &c., the squares of the arcs GH, HI;",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P10-p13",
     "la": "",
     "it": "Le loro radici, o√(1+QQ) − QRoo/√(1+QQ) e o√(1+QQ) + QRoo/√(1+QQ), sono gli archi GH e HI.",
     "en": "whose roots [SVG 453], and [SVG 454] are the arcs GH and HI.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Motte 1846, SVG 453, stampa o·1/√(1+QQ) al posto di o√(1+QQ): errore della formula di Motte (SVG 454 è corretta)."
    },
    {
     "id": "L2-P10-p14",
     "la": "",
     "it": "Inoltre, se dall’ordinata CH si sottrae la semisomma delle ordinate BG e DI, e dall’ordinata DI la semisomma delle ordinate CH ed EK, resteranno Roo e Roo + 3So³, saette degli archi GI e HK.",
     "en": "Moreover, if from the ordinate CH there be subducted half the sum of the ordinates BG and DI, and from the ordinate DI there be subducted half the sum of the ordinates CH and EK, there will remain Roo and Roo + 3So3, the versed sines of the arcs GI and HK.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "saette Roo, Roo + 3So³"
      ]
     },
     "nota": "Motte rende sagittæ con «versed sines»."
    },
    {
     "id": "L2-P10-p15",
     "la": "",
     "it": "E queste sono proporzionali alle lineette LH e NI, e quindi in rapporto duplicato dei tempi infinitamente piccoli T e t; e di qui il rapporto t/T è √((R + 3So)/R), ossia (R + (3/2)So)/R; e t×GH/T − HI + 2MI×NI/HI, sostituendo i valori di t/T, GH, HI, MI e NI ora trovati, diventa (3Soo/2R)√(1+QQ).",
     "en": "And these are proportional to the lineolæ LH and NI, and therefore in the duplicate ratio of the infinitely small times T and t: and thence the ratio [SVG 455] is [SVG 456] or [SVG 457]; and [SVG 458], by substituting the values of [SVG 455], GH, HI, MI and NI just found, becomes [SVG 459].",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Motte 1846, SVG 456, stampa √(R+3So)/R (radice sul solo numeratore) per √((R+3So)/R)."
    },
    {
     "id": "L2-P10-p16",
     "la": "",
     "it": "E poiché 2NI è 2Roo, la resistenza starà ora alla gravità come (3Soo/2R)√(1+QQ) sta a 2Roo, cioè come 3S√(1+QQ) sta a 4RR.",
     "en": "And since 2NI is 2Roo, the resistance will be now to the gravity as [SVG 459] to 2Roo, that is, as [SVG 460] to 4RR.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "resistenza : gravità = 3S√(1+QQ) : 4RR"
      ]
     }
    },
    {
     "id": "L2-P10-p17",
     "la": "",
     "it": "La velocità, poi, è quella con cui un corpo, uscendo da un luogo qualsiasi H secondo la tangente HN, potrebbe poi muoversi nel vuoto lungo una parabola che ha per diametro HC e per lato retto HN²/NI, ossia (1+QQ)/R.",
     "en": "And the velocity will be such, that a body going off therewith from any place H, in the direction of the tangent HN, would describe, in vacuo, a parabola, whose diameter is HC, and its latus rectum [SVG 461] or [SVG 462].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "parabola osculatrice in H, diametro HC"
      ],
      "evidenzia": [
       "v² ∝ lato retto (1+QQ)/R"
      ]
     }
    },
    {
     "id": "L2-P10-p18",
     "la": "",
     "it": "E la resistenza sta come la densità del mezzo e il quadrato della velocità considerati congiuntamente; e perciò la densità del mezzo sta direttamente come la resistenza e inversamente come il quadrato della velocità, cioè direttamente come 3S√(1+QQ)/4RR e inversamente come (1+QQ)/R, ossia come S/(R√(1+QQ)). C.V.T.",
     "en": "And the resistance is as the density of the medium and the square of the velocity conjunctly; and therefore the density of the medium is as the resistance directly, and the square of the velocity inversely; that is, as [SVG 463] directly and [SVG 462] inversely; that is, as [SVG 464] Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "densità ∝ S/(R√(1+QQ))"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P10-Es1",
   "tipo": "Exemplum",
   "titolo": "Prop. X, Es. 1 — il semicerchio",
   "copertura": [
    "II.S2.53",
    "II.S2.54",
    "II.S2.55",
    "II.S2.56",
    "II.S2.57"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Section II (sezione corrispondente; l’estratto non ha marcatori di pagina)"
   },
   "enunciato": {
    "la": "",
    "it": "Sia la linea PFHQ un semicerchio descritto sul diametro PQ, e si richieda la densità del mezzo che faccia muovere un proiettile lungo questa linea.",
    "en": "Let the line PFHQ be a semi-circle described upon the diameter PQ, to find the density of the medium that shall make a projectile move in that line."
   },
   "figura_base": {
    "punti": [
     "P",
     "Q",
     "A",
     "F",
     "C",
     "H",
     "D",
     "I",
     "M",
     "N",
     "T"
    ],
    "vincoli": [
     "semicerchio di diametro PQ, centro A",
     "AF ⊥ PQ",
     "AQ = n, AC = a, CH = e, CD = o"
    ]
   },
   "passi": [
    {
     "id": "L2-P10-Es1-p1",
     "la": "",
     "it": "Si divida a metà il diametro PQ in A; si chiami AQ n, AC a, CH e e CD o: DI², ossia AQ² − AD², sarà = nn − aa − 2ao − oo, ossia ee − 2ao − oo; ed estraendo la radice con il nostro metodo si avrà DI = e − ao/e − oo/2e − aaoo/2e³ − ao³/2e³ − a³o³/2e⁵ − ecc.",
     "en": "Bisect the diameter PQ in A; and call AQ, n; AC, a; CH, e; and CD, o; then DI2 or AQ2 - AD2 = nn - aa - 2ao - oo, or ee - 2ao - oo; and the root being extracted by our method, will give [SVG 469], &c.",
     "dipende_da": [
      "metodo delle serie di Newton («per methodum nostram»)"
     ],
     "figura": {
      "mostra": [
       "centro A",
       "AQ = n",
       "AC = a",
       "CH = e",
       "CD = o"
      ],
      "evidenzia": [
       "DI² = ee − 2ao − oo"
      ]
     },
     "nota": "Motte 1846, SVG 469, stampa ao²/2e³ al posto di ao³/2e³."
    },
    {
     "id": "L2-P10-Es1-p2",
     "la": "",
     "it": "Qui si scriva nn al posto di ee + aa, e risulterà DI = e − ao/e − nnoo/2e³ − anno³/2e⁵ − ecc.",
     "en": "Here put nn for ee + aa, and DI will become [SVG 470], &c.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "nn = ee + aa"
      ]
     }
    },
    {
     "id": "L2-P10-Es1-p3",
     "la": "",
     "it": "Serie di questo genere le distinguo in termini successivi in questo modo.",
     "en": "Such series I distinguish into successive terms after this manner:",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Capoverso esplicativo senza figura propria."
    },
    {
     "id": "L2-P10-Es1-p4",
     "la": "",
     "it": "Chiamo primo il termine in cui non compare la quantità infinitamente piccola o; secondo quello in cui quella quantità è di una dimensione; terzo quello in cui compare con due; quarto quello in cui è di tre; e così all’infinito.",
     "en": "I call that the first term in which the infinitely small quantity o is not found; the second, in which that quantity is of one dimension only; the third, in which it arises to two dimensions; the fourth, in which it is of three; and so ad infinitum.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P10-Es1-p5",
     "la": "",
     "it": "E il primo termine, che qui è e, denoterà sempre la lunghezza dell’ordinata CH che poggia all’inizio della quantità indefinita o.",
     "en": "And the first term, which here is e, will always denote the length of the ordinate CH, standing at the beginning of the indefinite quantity o.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "primo termine = CH"
      ]
     }
    },
    {
     "id": "L2-P10-Es1-p6",
     "la": "",
     "it": "Il secondo termine, che qui è ao/e, denoterà la differenza fra CH e DN, cioè la lineetta MN, che si stacca completando il parallelogramma HCDM, e perciò determina sempre la posizione della tangente HN: come in questo caso, prendendo MN in modo che stia a HM come ao/e sta a o, ossia come a sta a e.",
     "en": "The second term, which here is [SVG 471], will denote the difference between CH and DN; that is, the lineola MN which is cut off by completing the parallelogram HCDM; and therefore always determines the position of the tangent HN; as, in this case, by taking MN to HM as [SVG 471] to o, or a to e.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "MN",
       "tangente HN"
      ],
      "evidenzia": [
       "secondo termine = MN → tangente"
      ]
     }
    },
    {
     "id": "L2-P10-Es1-p7",
     "la": "",
     "it": "Il terzo termine, che qui è nnoo/2e³, designerà la lineetta IN, che giace fra la tangente e la curva, e perciò determina l’angolo di contatto IHN, ossia la curvatura che la linea curva ha in H.",
     "en": "The third term, which here is [SVG 472], will represent the lineola IN, which lies between the tangent and the curve; and therefore determines the angle of contact IHN, or the curvature which the curve line has in H.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "IN"
      ],
      "evidenzia": [
       "terzo termine = IN → curvatura"
      ]
     }
    },
    {
     "id": "L2-P10-Es1-p8",
     "la": "",
     "it": "Se quella lineetta IN è di grandezza finita, sarà designata dal terzo termine insieme con quelli che seguono all’infinito.",
     "en": "If that lineola IN is of a finite magnitude, it will be expressed by the third term, together with those that follow in infinitum.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P10-Es1-p9",
     "la": "",
     "it": "Ma se quella lineetta diminuisce all’infinito, i termini successivi diventano infinitamente minori del terzo, e perciò si possono trascurare.",
     "en": "But if that lineola be diminished in infinitum, the terms following become infinitely less than the third term, and therefore may be neglected.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P10-Es1-p10",
     "la": "",
     "it": "Il quarto termine determina la variazione della curvatura, il quinto la variazione della variazione, e così via.",
     "en": "The fourth term determines the variation of the curvature; the fifth, the variation of the variation; and so on.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "quarto termine (S) → variazione della curvatura"
      ]
     }
    },
    {
     "id": "L2-P10-Es1-p11",
     "la": "",
     "it": "Di qui, di passaggio, risulta evidente l’uso non disprezzabile di queste serie nella soluzione dei problemi che dipendono dalle tangenti e dalla curvatura delle curve.",
     "en": "Whence, by the way, appears no contemptible use of these series in the solution of problems that depend upon tangents, and the curvature of curves.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P10-Es1-p12",
     "la": "",
     "it": "Si confronti ora la serie e − ao/e − nnoo/2e³ − anno³/2e⁵ − ecc. con la serie P − Qo − Roo − So³ − ecc., e corrispondentemente al posto di P, Q, R e S si scriva e, a/e, nn/2e³ e ann/2e⁵, e al posto di √(1+QQ) si scriva √(1+aa/ee), ossia n/e: la densità del mezzo risulterà come a/ne, cioè (poiché n è data) come a/e, ossia AC/CH, cioè come quella lunghezza della tangente HT che termina sul semidiametro AF perpendicolare a PQ; e la resistenza starà alla gravità come 3a sta a 2n, cioè come 3AC sta al diametro PQ del cerchio; la velocità, poi, starà come √CH.",
     "en": "Now compare the series [SVG 470] &c., with the series P - Qo - Roo - So3 - &c., and for P, Q, R and S, put e, [SVG 473], [SVG 474] and [SVG 475], and for [SVG 476] put [SVG 477] or [SVG 478]; and the density of the medium will come out as [SVG 479]; that is (because n is given), as [SVG 473] or [SVG 480], that is, as that length of the tangent HT, which is terminated at the semi-diameter AF standing perpendicularly on PQ: and the resistance will be to the gravity as 3a to 2n, that is, as 3AC to the diameter PQ of the circle; and the velocity will be as [SVG 481].",
     "dipende_da": [
      "Prop. X (regola della densità)"
     ],
     "figura": {
      "mostra": [
       "semidiametro AF ⊥ PQ",
       "T = HN ∩ AF",
       "HT"
      ],
      "evidenzia": [
       "densità ∝ HT",
       "resistenza : gravità = 3AC : PQ",
       "v ∝ √CH"
      ]
     },
     "nota": "La trascrizione ha «ut CH» senza radice; Motte (SVG 481) ha √CH, e il calcolo dà √CH (apparato A.10)."
    },
    {
     "id": "L2-P10-Es1-p13",
     "la": "",
     "it": "Perciò, se il corpo esce dal luogo F con la velocità giusta lungo una linea parallela a PQ, e la densità del mezzo nei singoli luoghi H sta come la lunghezza della tangente HT, e anche la resistenza in un luogo qualsiasi H sta alla forza di gravità come 3AC sta a PQ, quel corpo descriverà il quadrante di cerchio FHQ. C.V.T.",
     "en": "Therefore if the body goes from the place F, with a due velocity, in the direction of a line parallel to PQ, and the density of the medium in each of the places H is as the length of the tangent HT, and the resistance also in any place H is to the force of gravity as 3AC to PQ, that body will describe the quadrant FHQ of a circle. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "F (sommità)",
       "quadrante FHQ"
      ],
      "evidenzia": [
       "partenza orizzontale da F"
      ]
     }
    },
    {
     "id": "L2-P10-Es1-p14",
     "la": "",
     "it": "Ma se lo stesso corpo uscisse dal luogo P secondo una linea perpendicolare a PQ e cominciasse a muoversi nell’arco di semicerchio PFQ, si dovrebbe prendere AC, cioè a, dalla parte opposta del centro A, e perciò se ne dovrebbe cambiare il segno e scrivere −a al posto di +a.",
     "en": "But if the same body should go from the place P, in the direction of a line perpendicular to PQ, and should begin to move in an arc of the semi-circle PFQ, we must take AC or a on the contrary side of the centre A; and therefore its sign must be changed, and we must put -a for +a.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "P",
       "quadrante PF"
      ],
      "evidenzia": [
       "a → −a"
      ]
     }
    },
    {
     "id": "L2-P10-Es1-p15",
     "la": "",
     "it": "In questo modo la densità del mezzo risulterebbe come −a/e.",
     "en": "Then the density of the medium would come out as [SVG 482].",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "densità negativa"
      ]
     }
    },
    {
     "id": "L2-P10-Es1-p16",
     "la": "",
     "it": "Ma la natura non ammette una densità negativa, cioè una densità che acceleri i moti dei corpi; e perciò non può avvenire naturalmente che un corpo, salendo da P, descriva il quadrante di cerchio PF.",
     "en": "But nature does not admit of a negative density, that is, a density which accelerates the motion of bodies; and therefore it cannot naturally come to pass that a body by ascending from P should describe the quadrant PF of a circle.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P10-Es1-p17",
     "la": "",
     "it": "Per ottenere questo effetto il corpo dovrebbe essere accelerato da un mezzo che spinge, non impedito da un mezzo che resiste.",
     "en": "To produce such an effect, a body ought to be accelerated by an impelling medium, and not impeded by a resisting one.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    }
   ]
  },
  {
   "id": "L2-P10-Es2",
   "tipo": "Exemplum",
   "titolo": "Prop. X, Es. 2 — la parabola",
   "copertura": [
    "II.S2.58",
    "II.S2.59"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Section II (sezione corrispondente; l’estratto non ha marcatori di pagina)"
   },
   "enunciato": {
    "la": "",
    "it": "Sia la linea PFQ una parabola, con l’asse AF perpendicolare all’orizzonte PQ, e si richieda la densità del mezzo che faccia muovere un proiettile lungo di essa.",
    "en": "Let the line PFQ be a parabola, having its axis AF perpendicular to the horizon PQ, to find the density of the medium, which will make a projectile move in that line."
   },
   "figura_base": {
    "punti": [
     "P",
     "F",
     "Q",
     "A",
     "C",
     "H",
     "D",
     "I"
    ],
    "vincoli": [
     "parabola di asse AF verticale",
     "PD×DQ = b×DI"
    ]
   },
   "passi": [
    {
     "id": "L2-P10-Es2-p1",
     "la": "",
     "it": "Per la natura della parabola, il rettangolo PDQ è uguale al rettangolo sotto l’ordinata DI e una retta data: cioè, se si chiamano b quella retta, a PC, c PQ, e CH e o CD, il rettangolo (a + o) per (c − a − o), ossia ac − aa − 2ao + co − oo, è uguale al rettangolo b per DI, e perciò DI è uguale a (ac − aa)/b + ((c − 2a)/b)o − oo/b.",
     "en": "From the nature of the parabola, the rectangle PDQ is equal to the rectangle under the ordinate DI and some given right line; that is, if that right line be called b; PC, a; PQ, c; CH, e; and CD, o; the rectangle a + o into c - a - o or ac - aa - 2ao + co - oo, is equal to the rectangle b into DI, and therefore DI is equal to [SVG 483].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "parabola PFQ",
       "asse AF",
       "PC = a",
       "PQ = c",
       "CD = o",
       "retta data b"
      ],
      "evidenzia": [
       "PD×DQ = b×DI"
      ]
     }
    },
    {
     "id": "L2-P10-Es2-p2",
     "la": "",
     "it": "Ora si dovrebbe scrivere il secondo termine di questa serie, ((c − 2a)/b)o, al posto di Qo, e anche il terzo termine, oo/b, al posto di Roo.",
     "en": "Now the second term [SVG 484] of this series is to be put for Qo, and the third term [SVG 485] for Roo.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Rispetto alla forma P − Qo − Roo, il secondo termine dà propriamente Q = −(c − 2a)/b; il segno non incide sul risultato."
    },
    {
     "id": "L2-P10-Es2-p3",
     "la": "",
     "it": "Ma poiché non ci sono altri termini, il coefficiente S del quarto dovrà annullarsi, e perciò la quantità S/(R√(1+QQ)), alla quale è proporzionale la densità del mezzo, sarà nulla.",
     "en": "But since there are no more terms, the co-efficient S of the fourth term will vanish; and therefore the quantity [SVG 464], to which the density of the medium is proportional, will be nothing.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "S = 0 ⇒ densità nulla"
      ]
     }
    },
    {
     "id": "L2-P10-Es2-p4",
     "la": "",
     "it": "Dunque il proiettile si muoverà lungo una parabola senza alcuna densità del mezzo, come dimostrò un tempo Galileo. C.V.T.",
     "en": "Therefore, where the medium is of no density, the projectile will move in a parabola; as Galileo hath heretofore demonstrated. Q.E.I.",
     "dipende_da": [
      "Galileo (moto parabolico dei proiettili)"
     ],
     "figura": {
      "mostra": []
     }
    }
   ]
  },
  {
   "id": "L2-P10-Es3",
   "tipo": "Exemplum",
   "titolo": "Prop. X, Es. 3 — l’iperbole conica",
   "copertura": [
    "II.S2.60",
    "II.S2.61"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Section II (sezione corrispondente; l’estratto non ha marcatori di pagina)"
   },
   "enunciato": {
    "la": "",
    "it": "Sia la linea AGK un’iperbole con l’asintoto NX perpendicolare al piano orizzontale AK, e si cerchi la densità del mezzo che faccia muovere un proiettile lungo questa linea.",
    "en": "Let the line AGK be an hyperbola, having its asymptote NX perpendicular to the horizontal plane AK, to find the density of the medium that will make a projectile move in that line."
   },
   "figura_base": {
    "punti": [
     "A",
     "G",
     "K",
     "N",
     "X",
     "M",
     "V",
     "D",
     "B",
     "Z",
     "Y"
    ],
    "vincoli": [
     "asintoto NX verticale",
     "DN×VG = bb",
     "DNXZ parallelogramma",
     "VZ : DN = m : n",
     "VY = VG"
    ]
   },
   "passi": [
    {
     "id": "L2-P10-Es3-p1",
     "la": "",
     "it": "Sia MX l’altro asintoto, che incontri in V l’ordinata DG prolungata; per la natura dell’iperbole, il rettangolo XV per VG sarà dato.",
     "en": "Let MX be the other asymptote, meeting the ordinate DG produced in V; and from the nature of the hyperbola, the rectangle of XV into VG will be given.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "asintoti NX (verticale), MX",
       "iperbole AGK",
       "D su AK",
       "V = DG ∩ MX"
      ],
      "evidenzia": [
       "XV×VG costante"
      ]
     }
    },
    {
     "id": "L2-P10-Es3-p2",
     "la": "",
     "it": "Ma è dato anche il rapporto di DN a VX, e perciò è dato anche il rettangolo DN per VG.",
     "en": "There is also given the ratio of DN to VX, and therefore the rectangle of DN into VG is given.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "DN×VG costante"
      ]
     }
    },
    {
     "id": "L2-P10-Es3-p3",
     "la": "",
     "it": "Sia esso bb; e, completato il parallelogramma DNXZ, si chiami BN a, BD o, NX c, e si ponga che il rapporto dato di VZ a ZX, ossia a DN, sia quello di m a n.",
     "en": "Let that be bb: and, completing the parallelogram DNXZ, let BN be called a; BD, o; NX, c; and let the given ratio of VZ to ZX or DN be [SVG 486].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Z",
       "parallelogramma DNXZ",
       "B su AK"
      ],
      "evidenzia": [
       "BN = a",
       "BD = o",
       "NX = c",
       "VZ : ZX = m : n"
      ]
     }
    },
    {
     "id": "L2-P10-Es3-p4",
     "la": "",
     "it": "DN sarà uguale ad a − o, VG a bb/(a − o), VZ a (m/n)(a − o), e GD, ossia NX − VZ − VG, a c − (m/n)a + (m/n)o − bb/(a − o).",
     "en": "Then DN will be equal to a - o, VG equal to [SVG 487], VZ equal to [SVG 488], and GD or NX - VZ - VG equal to [SVG 489].",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "GD = NX − VZ − VG"
      ]
     }
    },
    {
     "id": "L2-P10-Es3-p5",
     "la": "",
     "it": "Si risolva il termine bb/(a − o) nella serie convergente bb/a + (bb/aa)o + (bb/a³)oo + (bb/a⁴)o³ ecc., e GD diventerà uguale a c − (m/n)a − bb/a + (m/n)o − (bb/aa)o − (bb/a³)o² − (bb/a⁴)o³ ecc.",
     "en": "Let the term [SVG 487] be resolved into the converging series [SVG 490], &c., and GD will become equal to [SVG 491] &c.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P10-Es3-p6",
     "la": "",
     "it": "Di questa serie il secondo termine, (m/n)o − (bb/aa)o, si deve usare al posto di Qo; il terzo, con il segno cambiato, (bb/a³)o², al posto di Ro²; e il quarto, anch’esso con il segno cambiato, (bb/a⁴)o³, al posto di So³; e i loro coefficienti m/n − bb/aa, bb/a³ e bb/a⁴ si devono scrivere nella regola precedente al posto di Q, R e S.",
     "en": "The second term [SVG 492] of this series is to be used for Qo; the third [SVG 493], with its sign changed for Ro2; and the fourth [SVG 494], with its sign changed also for So3, and their coefficients [SVG 495], [SVG 496] and [SVG 497] are to be put for Q, R, and S in the former rule.",
     "dipende_da": [
      "Prop. X (regola della densità)"
     ],
     "figura": {
      "mostra": []
     },
     "nota": "Il corpo procede verso l’asintoto NX: le ascisse BD = o crescono nel verso del moto, come nella Prop. X."
    },
    {
     "id": "L2-P10-Es3-p7",
     "la": "",
     "it": "Fatto ciò, la densità del mezzo risulta come (bb/a⁴) / ((bb/a³)√(1 + mm/nn − 2mbb/naa + b⁴/a⁴)), ossia 1/√(aa + mmaa/nn − 2mbb/n + b⁴/aa), cioè, se su VZ si prende VY uguale a VG, come 1/XY.",
     "en": "Which being done, the density of the medium will come out as [SVG 498], or [SVG 499], that is, if in VZ you take VY equal to VG, as [SVG 500].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Y su VZ con VY = VG",
       "XY"
      ],
      "evidenzia": [
       "densità ∝ 1/XY"
      ]
     }
    },
    {
     "id": "L2-P10-Es3-p8",
     "la": "",
     "it": "Infatti aa e mmaa/nn − 2mbb/n + b⁴/aa sono i quadrati di XZ e di ZY.",
     "en": "For aa and [SVG 501] are the squares of XZand ZY.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "XY² = XZ² + ZY²"
      ]
     },
     "nota": "Motte 1846, SVG 501, stampa (mm/nn)aa − 2mbb/a + b⁴/a⁴: due denominatori errati rispetto al latino (2mbb/n, b⁴/aa)."
    },
    {
     "id": "L2-P10-Es3-p9",
     "la": "",
     "it": "La resistenza, poi, si trova stare alla gravità nel rapporto che 3XY ha con 2YG; e la velocità è quella con cui il corpo procederebbe lungo una parabola con vertice G, diametro DG e lato retto XY²/VG.",
     "en": "But the ratio of the resistance to gravity is found to be that of 3XY to 2YG; and the velocity is that with which the body would describe a parabola, whose vertex is G, diameter DG, latus rectum [SVG 502].",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "resistenza : gravità = 3XY : 2YG",
       "lato retto XY²/VG"
      ]
     }
    },
    {
     "id": "L2-P10-Es3-p10",
     "la": "",
     "it": "Si ponga dunque che le densità del mezzo nei singoli luoghi G siano inversamente come le distanze XY, e che la resistenza in un luogo qualsiasi G stia alla gravità come 3XY sta a 2YG: il corpo, lanciato dal luogo A con la velocità giusta, descriverà quell’iperbole AGK. C.V.T.",
     "en": "Suppose, therefore, that the densities of the medium in each of the places G are reciprocally as the distances XY, and that the resistance in any place G is to the gravity as 3XY to 2YG; and a body let go from the place A, with a due velocity, will describe that hyperbola AGK. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "traiettoria da A"
      ],
      "evidenzia": [
       "soluzione"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P10-Es4",
   "tipo": "Exemplum",
   "titolo": "Prop. X, Es. 4 — iperboli con VG ∝ 1/DNⁿ",
   "copertura": [
    "II.S2.62",
    "II.S2.63"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Section II (sezione corrispondente; l’estratto non ha marcatori di pagina)"
   },
   "enunciato": {
    "la": "",
    "it": "Si ponga, in modo indeterminato, che la linea AGK sia un’iperbole descritta con centro X e asintoti MX, NX secondo questa legge: costruito il rettangolo XZDN, il cui lato ZD tagli l’iperbole in G e il suo asintoto in V, VG sia inversamente come una potenza qualsiasi DNⁿ di ZX, ossia di DN, il cui indice è il numero n; e si cerchi la densità del mezzo nel quale un proiettile proceda lungo questa curva.",
    "en": "Suppose, indefinitely, the line AGK to be an hyperbola described with the centre X, and the asymptotes MX, NX, so that, having constructed the rectangle XZDN, whose side ZD cuts the hyperbola in G and its asymptote in V, VG may be reciprocally as any power DNn of the line ZX or DN, whose index is the number n: to find the density of the medium in which a projected body will describe this curve."
   },
   "figura_base": {
    "punti": [
     "A",
     "G",
     "K",
     "X",
     "M",
     "N",
     "Z",
     "D",
     "V",
     "B",
     "Y"
    ],
    "vincoli": [
     "VG = bb/DNⁿ",
     "VZ : DN = d : e",
     "VY = n×VG"
    ]
   },
   "passi": [
    {
     "id": "L2-P10-Es4-p1",
     "la": "",
     "it": "Al posto di BN, BD, NX si scrivano rispettivamente A, O, C; sia VZ a XZ, ossia a DN, come d sta a e, e VG uguale a bb/DNⁿ: DN sarà uguale ad A − O, VG = bb/(A − O)ⁿ, VZ = (d/e)(A − O), e GD, ossia NX − VZ − VG, uguale a C − (d/e)A + (d/e)O − bb/(A − O)ⁿ.",
     "en": "For BN, BD, NX, put A, O, C, respectively, and let VZ be to XZ or DN as d to e, and VG be equal to [SVG 503]; then DN will be equal to A - O, [SVG 504], [SVG 505], and GD or NX - VZ - VG equal to [SVG 506].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "asintoti MX, NX",
       "rettangolo XZDN",
       "V, G su ZD"
      ],
      "evidenzia": [
       "VG = bb/DNⁿ"
      ]
     }
    },
    {
     "id": "L2-P10-Es4-p2",
     "la": "",
     "it": "Si risolva quel termine bb/(A − O)ⁿ nella serie infinita bb/Aⁿ + (nbb/Aⁿ⁺¹)O + ((nn + n)/2Aⁿ⁺²)bbO² + ((n³ + 3nn + 2n)/6Aⁿ⁺³)bbO³ ecc., e GD diventerà uguale a C − (d/e)A − bb/Aⁿ + (d/e)O − (nbb/Aⁿ⁺¹)O − ((nn + n)/2Aⁿ⁺²)bbO² − ((n³ + 3nn + 2n)/6Aⁿ⁺³)bbO³ ecc.",
     "en": "Let the term [SVG 507] be resolved into an infinite series [SVG 508], &c., and GD will be equal to [SVG 509], &c.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "La trascrizione ha «−+» davanti agli ultimi due termini: artefatto, letto «−»."
    },
    {
     "id": "L2-P10-Es4-p3",
     "la": "",
     "it": "Di questa serie il secondo termine, (d/e)O − (nbb/Aⁿ⁺¹)O, si deve usare al posto di Qo, il terzo, ((nn + n)/2Aⁿ⁺²)bbO², al posto di Ro², il quarto, ((n³ + 3nn + 2n)/6Aⁿ⁺³)bbO³, al posto di So³.",
     "en": "The second term [SVG 510] of this series is to be used for Qo, the third [SVG 511] for Roo, the fourth [SVG 512] for [SVG 513].",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P10-Es4-p4",
     "la": "",
     "it": "E di qui la densità del mezzo S/(R√(1+QQ)), in un luogo qualsiasi G, diventa (n + 2)/(3√(A² + (dd/ee)A² − (2dnbb/eAⁿ)A + nnb⁴/A²ⁿ)); e perciò, se su VZ si prende VY uguale a n×VG, quella densità è inversamente come XY.",
     "en": "And thence the density of the medium [SVG 514], in any place G, will be [SVG 515] and therefore if in VZ you take VY equal to n × VG, that density is reciprocally as XY.",
     "dipende_da": [
      "Prop. X (regola della densità)"
     ],
     "figura": {
      "mostra": [
       "Y su VZ con VY = n×VG",
       "XY"
      ],
      "evidenzia": [
       "densità ∝ 1/XY"
      ]
     }
    },
    {
     "id": "L2-P10-Es4-p5",
     "la": "",
     "it": "Infatti A² e (dd/ee)A² − (2dnbb/eAⁿ)A + nnb⁴/A²ⁿ sono i quadrati di XZ e di ZY.",
     "en": "For A2 and [SVG 516] are the squares of XZ and ZY.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P10-Es4-p6",
     "la": "",
     "it": "La resistenza, poi, nello stesso luogo G diventa alla gravità come 3S per XY/A sta a 4RR, cioè come XY sta a ((2nn + 2n)/(n + 2))VG.",
     "en": "But the resistance in the same place G is to the force of gravity as [SVG 517] to 4RR, that is, as XY to [SVG 518].",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "resistenza : gravità = XY : ((2nn + 2n)/(n + 2))VG"
      ]
     }
    },
    {
     "id": "L2-P10-Es4-p7",
     "la": "",
     "it": "E la velocità, nello stesso luogo, è proprio quella con cui il corpo lanciato procederebbe lungo una parabola con vertice G, diametro GD e lato retto (1+QQ)/R, ossia 2XY²/((nn + n)×VG). C.V.T.",
     "en": "And the velocity there is the same wherewith the projected body would move in a parabola, whose vertex is G, diameter GD, and latus rectum [SVG 462] or [SVG 519]. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "lato retto 2XY²/((nn + n)VG)"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P10-Sch-R8",
   "tipo": "Scholium/Regula",
   "titolo": "Scolio alla Prop. X, Regola 8 — direzione di lancio per colpire K",
   "copertura": [
    "II.S2.76"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Section II (sezione corrispondente; l’estratto non ha marcatori di pagina)"
   },
   "enunciato": {
    "la": "",
    "it": "Trovate le lunghezze AH, HX, si desidera la posizione della retta AH secondo la quale il proiettile, lanciato con quella velocità data, cade in un punto qualsiasi K.",
    "en": "The lengths AH, HX being found; let there be now required the position of the line AH, according to which a projectile thrown with that given velocity shall fall upon any point K."
   },
   "figura_base": {
    "punti": [
     "A",
     "K",
     "C",
     "F",
     "H",
     "E",
     "M",
     "N",
     "X",
     "I"
    ],
    "vincoli": [
     "AC ⊥ AK, verso il basso, AC = AI = ½HX",
     "KF ⊥ AK",
     "iperbole di asintoti AK, KF con la coniugata per C",
     "cerchio di centro A e raggio AH"
    ]
   },
   "passi": [
    {
     "id": "L2-P10-Sch-R8-p1",
     "la": "",
     "it": "Trovate le lunghezze AH, HX, se ora si desidera la posizione della retta AH secondo la quale il proiettile, lanciato con quella velocità data, cade in un punto qualsiasi K: nei punti A e K si innalzino le rette AC, KF perpendicolari all’orizzonte, delle quali AC sia diretta verso il basso e sia uguale ad AI, ossia a ½HX.",
     "en": "The lengths AH, HX being found; let there be now required the position of the line AH, according to which a projectile thrown with that given velocity shall fall upon any point K. At the points A and K, erect the lines AC, KF perpendicular to the horizon; whereof let AC be drawn downwards, and be equal to AI or [SVG 533].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A, K sulla retta AK",
       "AC verso il basso, AC = AI",
       "KF verticale"
      ],
      "evidenzia": [
       "AC = AI = ½HX (n = 1)"
      ]
     }
    },
    {
     "id": "L2-P10-Sch-R8-p2",
     "la": "",
     "it": "Con asintoti AK, KF si descriva un’iperbole la cui coniugata passi per il punto C; e con centro A e raggio AH si descriva un cerchio che tagli quell’iperbole nel punto H: il proiettile lanciato secondo la retta AH cadrà nel punto K. C.V.T.",
     "en": "With the asymptotes AK, KF, describe an hyperbola, whose conjugate shall pass through the point C; and from the centre A, with the interval AH, describe a circle cutting that hyperbola in the point H; then the projectile thrown in the direction of the right line AH will fall upon the point K. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "iperbole di asintoti AK, KF (coniugata per C)",
       "cerchio di centro A e raggio AH",
       "H intersezione"
      ],
      "evidenzia": [
       "direzione di lancio AH"
      ]
     }
    },
    {
     "id": "L2-P10-Sch-R8-p3",
     "la": "",
     "it": "Infatti il punto H, poiché la lunghezza AH è data, si trova in qualche punto del cerchio descritto.",
     "en": "For the point H, because of the given length AH, must be somewhere in the circumference of the described circle.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P10-Sch-R8-p4",
     "la": "",
     "it": "Si conduca CH, che incontri AK e KF, la prima in E, la seconda in F; e, per le parallele CH, MX e le uguali AC, AI, AE sarà uguale ad AM, e perciò anche uguale a KN.",
     "en": "Draw CH meeting AK and KF in E and F; and because CH, MX are parallel, and AC, AI equal, AE will be equal to AM, and therefore also equal to KN.",
     "dipende_da": [
      "Regola 6"
     ],
     "figura": {
      "mostra": [
       "retta CH",
       "E su AK",
       "F su KF",
       "M, N della Regola 6"
      ],
      "evidenzia": [
       "AE = AM = KN"
      ]
     },
     "nota": "«etiam æqualis KN» usa NK = AM della Regola 6, senza citarla: il rimando è implicito."
    },
    {
     "id": "L2-P10-Sch-R8-p5",
     "la": "",
     "it": "Ma CE sta ad AE come FH sta a KN, e perciò CE e FH sono uguali.",
     "en": "But CE is to AE as FH to KN, and therefore CE and FH are equal.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "CE = FH"
      ]
     }
    },
    {
     "id": "L2-P10-Sch-R8-p6",
     "la": "",
     "it": "Dunque il punto H cade sull’iperbole descritta con asintoti AK, KF, la cui coniugata passa per il punto C, e perciò si trova nell’intersezione comune di questa iperbole e del cerchio descritto. C.V.D.",
     "en": "Therefore the point H falls upon the hyperbolic curve described with the asymptotes AK, KF whose conjugate passes through the point C; and is therefore found in the common intersection of this hyperbolic curve and the circumference of the described circle. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "CE = FH: proprietà delle secanti dell’iperbole fra gli asintoti"
      ]
     }
    },
    {
     "id": "L2-P10-Sch-R8-p7",
     "la": "",
     "it": "Si deve poi notare che questa operazione procede allo stesso modo sia che la retta AKN sia parallela all’orizzonte, sia che sia inclinata sull’orizzonte con un angolo qualsiasi; che dalle due intersezioni H, H nascono due angoli NAH, NAH; e che nella pratica meccanica basta descrivere il cerchio una volta e poi applicare al punto C una riga illimitata CH in modo che la sua parte FH, compresa fra il cerchio e la retta FK, sia uguale alla sua parte CE, situata fra il punto C e la retta AK.",
     "en": "It is to be observed that this operation is the same, whether the right line AKN be parallel to the horizon, or inclined thereto in any angle; and that from two intersections H, h, there arise two angles NAH, NAh; and that in mechanical practice it is sufficient once to describe a circle, then to apply a ruler CH, of an indeterminate length, so to the point C, that its part FH, intercepted between the circle and the right line FK, may be equal to its part CE placed between the point C and the right line AK.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "seconda intersezione H"
      ],
      "evidenzia": [
       "due soluzioni"
      ]
     },
     "nota": "Motte distingue le due soluzioni con H, h e NAH, NAh; il latino ripete H, H e NAH, NAH."
    }
   ]
  }
 ]
}
```
