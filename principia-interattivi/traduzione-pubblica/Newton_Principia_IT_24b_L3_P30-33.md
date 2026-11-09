> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 24b — Libro III: il moto dei nodi della Luna (Propp. XXX–XXXIII e le proposizioni di Machin)

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo è la **seconda parte** del gruppo G5 del Libro III (*De mundi systemate*), Propp. XXI–XXXIII. La **prima parte**, con le Propp. XXI–XXIX (regresso degli equinozi e nutazione, disuguaglianze lunari, satelliti di Giove e di Saturno, maree, forze del Sole sulla Luna, momento dell’area, distanza e figura dell’orbita lunare, variazione), è nel **Fascicolo 24a**. Qui si traduce integralmente il testo da «PROPOSITIO XXX.» alla fine del gruppo: le **Propp. XXX–XXXIII** sul moto dei nodi della Luna (moto orario nell’orbita circolare ed ellittica, moto medio annuo, moto vero) con i loro corollari; lo **Scolio** in cui Newton presenta il metodo di John Machin e Henry Pemberton; lo scritto di Machin *De motu nodorum lunæ* con le sue **Propp. I–II**, il corollario e lo **Scolio** numerico che chiude il gruppo. È una traduzione di lavoro, non un’edizione critica validata.

Le proposizioni sull’inclinazione dell’orbita lunare (Propp. XXXIV–XXXV) non sono in questo fascicolo: appartengono al gruppo G6 (Fascicolo 25a). Qui l’inclinazione compare solo nella Prop. XXXII (come causa possibile dello scarto dalle tavole) e nella Prop. XXXIII (variazione dell’inclinazione e latitudine della Luna).

Gli identificatori **III.G5.37–III.G5.63** proseguono la serie del Fascicolo 24a (III.G5.01–III.G5.36); numerati in origine da 101, sono stati rinumerati dal coordinatore. Gli identificatori e i titoli tematici tra parentesi sono aggiunte editoriali. I numeri romani delle proposizioni e dei problemi, i numeri dei corollari e i numeri arabi delle proposizioni di Machin appartengono al testo originale. Le integrazioni del curatore sono tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton.

In coda al fascicolo c’è la **Parte B**, con i dati strutturati per le pagine interattive di 11 unità con dimostrazione geometrica o calcolo: Prop. XXX con i Cor. 1 e 2; Prop. XXXI e il suo corollario con la correzione del moto orario; Propp. XXXII e XXXIII; le Propp. I e II di Machin, il corollario della II e lo Scolio numerico di Machin.

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro III, Propp. XXX–XXXIII e Scolio, **pp. 437–454** (la Prop. XXX comincia a p. 437, dopo il marcatore ‹437› che cade nell’ultimo capoverso della Prop. XXIX; i marcatori della trascrizione vanno da ‹438› a ‹454›). Trascrizione normalizzata del Newton Project, documento **NATP00303**, estratta in testo semplice senza correzioni: `fonti/latino-1726/latino-1726-L3-P21-33.md`, righe 104–188. Figure segnate [FIG] (non disponibili).
2. **Inglese di confronto.** *Newton’s Principia*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, Book III, Propp. XXX–XXXIII e Scholium (Project Gutenberg n. 76404), estratto `fonti/motte-1846/motte-1846-L3-P21-33.md`, righe 643–1247. L’estratto non contiene marcatori di pagina: le pagine di Motte sono indicate come «sezione corrispondente». Le formule stampate come immagini (`[SVG 1042]`–`[SVG 1055]`) sono state controllate sul LaTeX di `fonti/motte-1846/svg_tex.tsv`.
3. **Istruzioni** del Libro III (`ISTRUZIONI-TRADUTTORE.md`), **brief comune** e **addendum del Libro II**; **Fascicoli 3, 5 e 20** (modelli di formato). Per i rimandi interni: il latino delle Propp. XXV–XXIX nello stesso file della fonte 1 (tradotte nel Fascicolo 24a).

Non ho consultato né riprodotto traduzioni moderne. Non ho potuto vedere la stampa del 1726 né le figure originali: le relazioni geometriche sono ricostruite dalle sole lettere del testo. Tutti i controlli numerici sono stati eseguiti con lo script `tmp/24b/verifica.py`.

### Criteri di traduzione

- Il testo guida è il latino; l’inglese di Motte serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o si discosta.
- Si applicano il **glossario comune** del brief, quello del **Libro II** e quello del **Libro III**: *nodi*, *linea nodorum* «nodi», «linea dei nodi»; *syzygiæ*, *quadraturæ*, *octantes* «sizigie», «quadrature», «ottanti»; *motus medius* «moto medio»; *locus medius / verus* «luogo medio / vero»; *æquatio* «equazione» (nota N10); *inclinatio* «inclinazione»; *latitudo* «latitudine»; *annus sidereus* «anno siderale»; *ecliptica* «eclittica»; *stellæ fixæ* «stelle fisse»; *vis solis ad perturbandum motum lunæ* «forza del Sole che perturba il moto della Luna»; Sole, Luna, Terra con la maiuscola; *in antecedentia* «in antecedenza» (nota N2); *ratio duplicata / subduplicata* «rapporto duplicato / subduplicato»; *reciproce* «inversamente»; *conjunctim* «considerati congiuntamente»; *particula* «particella»; *sinus* «seno»; *chorda* «corda»; *trajectoria / orbis* «traiettoria / orbita»; *tempus periodicum* «tempo periodico»; *momentum* «momento»; Q.E.D. «C.V.D.».
- Le estensioni del glossario proprie di questo fascicolo sono elencate e motivate nel § A.0. La più importante: *motus mediocris* «moto mediocre», distinto da *motus medius* «moto medio».
- I valori sessagesimali sono scritti come in Newton, con i segni moderni: «33″. 10‴. 33iv. 12v.» → 33″ 10‴ 33ⁱᵛ 12ᵛ; «19gr. 49′. 3″. 55‴.» → 19° 49′ 3″ 55‴ (nota N1). Le date e i numeri non sono convertiti.
- Le abbreviazioni «AZqu.», «AZq», «ATq» sono scritte AZ², AT²; le frazioni appiattite dalla trascrizione («IT×PmTm», «ce×fYcY», «12⁤AZ», «38⁤310», «12iv⁤12», «23‴⁤23») sono rese con la barra o con la frazione (IT×Pm/Tm, ce×fY/cY, ½AZ, 38 3/10, 12½ⁱᵛ, 23⅔‴), dichiarando la lettura nell’apparato e nella Parte B. Nessuna formula moderna entra nel testo tradotto.
- Lo scritto di Machin è stampato da Newton tra virgolette, aperte all’inizio di ogni capoverso; l’italiano usa le caporali secondo l’uso tipografico italiano (« all’inizio di ogni capoverso, » alla fine dello scritto).

---

## Traduzione italiana

### Proposizione XXX. Problema XI (moto orario dei nodi nell’orbita circolare)

**[III.G5.37]** **Trovare il moto orario dei nodi della Luna in un’orbita circolare.**

**[III.G5.38]** Rappresentino S il Sole, T la Terra, P la Luna, NPn l’orbita della Luna, Npn la traccia dell’orbita sul piano dell’eclittica; N, n i nodi, nTNm la linea dei nodi prolungata all’infinito; PI, PK le perpendicolari abbassate sulle linee ST, Qq; Pp la perpendicolare abbassata sul piano dell’eclittica; A, B le sizigie della Luna nel piano dell’eclittica; AZ la perpendicolare sulla linea dei nodi Nn; Q, q le quadrature della Luna nel piano dell’eclittica, e pK la perpendicolare sulla linea Qq che sta fra le quadrature. La forza del Sole che perturba il moto della Luna (per la Prop. XXV) è duplice: l’una proporzionale alla linea LM nello schema di quella proposizione, l’altra alla linea MT. E la Luna è tirata dalla prima forza verso la Terra, dalla seconda verso il Sole, lungo una linea parallela alla retta ST condotta dalla Terra al Sole. La prima forza, LM, agisce secondo il piano dell’orbita lunare, e perciò non muta affatto la posizione del piano. Questa va dunque trascurata. La seconda forza, MT, dalla quale il piano dell’orbita lunare è perturbato, è la stessa della forza 3PK o 3IT. E questa forza (per la Prop. XXV) sta alla forza con cui la Luna, nel suo tempo periodico, potrebbe ruotare uniformemente in un cerchio attorno alla Terra in quiete, come 3IT sta al raggio del cerchio moltiplicato per il numero 178,725, ossia come IT sta al raggio moltiplicato per 59,575. Del resto, in questo calcolo e in tutto quello che segue, considero tutte le linee condotte dalla Luna al Sole come parallele alla linea che si conduce dalla Terra al Sole, perché l’inclinazione diminuisce in alcuni casi tutti gli effetti quasi quanto li aumenta in altri; e cerchiamo i moti mediocri dei nodi, trascurando minuzie di questo genere, che renderebbero il calcolo troppo complicato.

**[III.G5.39]** Rappresenti ora PM l’arco che la Luna descrive in un tempo dato piccolissimo, e ML la piccola linea di cui la Luna, per la spinta della detta forza 3IT, potrebbe descrivere la metà nello stesso tempo. Si congiungano PL, MP, e si prolunghino fino a m e l, dove tagliano il piano dell’eclittica; e su Tm si abbassi la perpendicolare PH. E poiché la retta ML è parallela al piano dell’eclittica, e perciò non può incontrare la retta ml che giace in quel piano, e tuttavia queste rette giacciono in un piano comune LMPml, queste rette saranno parallele, e perciò i triangoli LMP, lmP saranno simili. Ora, poiché MPm è nel piano dell’orbita in cui la Luna si muoveva nel luogo P, il punto m cadrà sulla linea Nn condotta per i nodi N, n di quell’orbita. E poiché la forza da cui è generata la metà della piccola linea LM, se fosse stata impressa tutta insieme e in una volta nel luogo P, genererebbe quella linea intera, e farebbe sì che la Luna si muovesse in un arco la cui corda fosse LP, e perciò trasferirebbe la Luna dal piano MPmT al piano LPlT, il moto angolare dei nodi generato da quella forza sarà uguale all’angolo mTl. Ma ml sta a mP come ML sta a MP; e perciò, poiché MP è dato, essendo dato il tempo, ml è come il rettangolo ML×mP, cioè come il rettangolo IT×mP. E l’angolo mTl, purché l’angolo Tml sia retto, è come ml/Tm, e perciò come IT×Pm/Tm, cioè (essendo proporzionali Tm e mP, TP e PH) come IT×PH/TP, e perciò, essendo data TP, come IT×PH. Se poi l’angolo Tml, ossia STN, è obliquo, l’angolo mTl sarà ancora minore, nel rapporto del seno dell’angolo STN al raggio, ossia di AZ ad AT. La velocità dei nodi è dunque come IT×PH×AZ, ossia come il prodotto dei seni dei tre angoli TPI, PTN e STN.

**[III.G5.40]** Se quegli angoli, trovandosi i nodi nelle quadrature e la Luna in sizigia, sono retti, la piccola linea ml se ne andrà all’infinito, e l’angolo mTl diventerà uguale all’angolo mPl. In questo caso, però, l’angolo mPl sta all’angolo PTM, che la Luna descrive nello stesso tempo con il suo moto apparente attorno alla Terra, come 1 sta a 59,575. Infatti l’angolo mPl è uguale all’angolo LPM, cioè all’angolo di deviazione della Luna dal cammino rettilineo che la sola detta forza solare 3IT, se allora cessasse la gravità della Luna, potrebbe generare in quel tempo dato; e l’angolo PTM è uguale all’angolo di deviazione della Luna dal cammino rettilineo che la forza da cui la Luna è trattenuta nella sua orbita, se allora cessasse la forza solare 3IT, genererebbe nello stesso tempo. E queste forze, come abbiamo detto sopra, stanno fra loro come 1 sta a 59,575. Dunque, poiché il moto medio orario della Luna rispetto alle stelle fisse è 32′ 56″ 27‴ 12½ⁱᵛ, il moto orario del nodo in questo caso sarà 33″ 10‴ 33ⁱᵛ 12ᵛ. Negli altri casi, invece, questo moto orario starà a 33″ 10‴ 33ⁱᵛ 12ᵛ come il prodotto dei seni dei tre angoli TPI, PTN e STN (ossia delle distanze della Luna dalla quadratura, della Luna dal nodo e del nodo dal Sole) sta al cubo del raggio. E ogni volta che il segno di uno qualsiasi di questi angoli cambia da positivo a negativo, e da negativo a positivo, il moto regressivo dovrà mutarsi in progressivo e il progressivo in regressivo. Ne segue che i nodi progrediscono ogni volta che la Luna si trova fra l’una o l’altra quadratura e il nodo più vicino a quella quadratura. Negli altri casi regrediscono e, per l’eccesso del regresso sul progresso, sono portati ogni mese in antecedenza.

**[III.G5.41]** *Cor. 1.* Di qui, se dagli estremi P e M di un arco dato piccolissimo PM si abbassano sulla linea Qq che congiunge le quadrature le perpendicolari PK, Mk, e queste si prolungano finché tagliano la linea dei nodi Nn in D e d, il moto orario dei nodi sarà come l’area MPDd e il quadrato della linea AZ considerati congiuntamente. Siano infatti PK, PH e AZ i tre seni predetti. Cioè PK il seno della distanza della Luna dalla quadratura, PH il seno della distanza della Luna dal nodo e AZ il seno della distanza del nodo dal Sole: e la velocità del nodo sarà come il prodotto PK×PH×AZ. Ma PT sta a PK come PM sta a Kk, e perciò, essendo date PT e PM, Kk è proporzionale a PK. E AT sta a PD come AZ sta a PH, e perciò PH è proporzionale al rettangolo PD×AZ; e, composti i rapporti, PK×PH è come il prodotto Kk×PD×AZ, e PK×PH×AZ come Kk×PD×AZ², cioè come l’area PDdM e AZ² considerate congiuntamente. C.V.D.

**[III.G5.42]** *Cor. 2.* In una posizione data qualsiasi dei nodi, il moto orario mediocre è la metà del moto orario nelle sizigie della Luna, e perciò sta a 16″ 35‴ 16ⁱᵛ 36ᵛ come il quadrato del seno della distanza dei nodi dalle sizigie sta al quadrato del raggio, ossia come AZ² sta ad AT². Infatti, se la Luna percorre con moto uniforme il semicerchio QAq, la somma di tutte le aree PDdM, nel tempo in cui la Luna va da Q a M, sarà l’area QMdE, che termina alla tangente QE del cerchio; e nel tempo in cui la Luna raggiunge il punto n, quella somma sarà l’intera area EQAn che la linea PD descrive; poi, mentre la Luna procede da n a q, la linea PD cadrà fuori del cerchio e descriverà l’area nqe, che termina alla tangente qe del cerchio; quest’area, poiché prima i nodi regredivano e ora invece progrediscono, deve essere sottratta dall’area precedente e, essendo uguale all’area QEN, lascerà il semicerchio NQAn. Dunque la somma di tutte le aree PDdM, nel tempo in cui la Luna descrive un semicerchio, è l’area del semicerchio; e la somma di tutte, nel tempo in cui la Luna descrive un cerchio, è l’area del cerchio intero. Ma l’area PDdM, quando la Luna si trova nelle sizigie, è il rettangolo formato dall’arco PM e dal raggio PT; e la somma di tutte le aree uguali a questa, nel tempo in cui la Luna descrive un cerchio, è il rettangolo formato dalla circonferenza intera e dal raggio del cerchio; e questo rettangolo, essendo uguale a due cerchi, è doppio del rettangolo precedente. Perciò i nodi, con la velocità che hanno nelle sizigie lunari continuata uniformemente, descriverebbero uno spazio doppio di quello che descrivono realmente; e perciò il moto mediocre con cui, se fosse continuato uniformemente, potrebbero descrivere lo spazio che percorrono realmente con un moto non uniforme, è la metà del moto che hanno nelle sizigie della Luna. Quindi, poiché il moto orario massimo, se i nodi si trovano nelle quadrature, è 33″ 10‴ 33ⁱᵛ 12ᵛ, il moto orario mediocre in questo caso sarà 16″ 35‴ 16ⁱᵛ 36ᵛ. E poiché il moto orario dei nodi è sempre come AZ² e l’area PDdM considerate congiuntamente, e perciò il moto orario dei nodi nelle sizigie della Luna è come AZ² e l’area PDdM considerate congiuntamente, cioè (essendo data l’area PDdM descritta nelle sizigie) come AZ², anche il moto mediocre sarà come AZ²; e perciò questo moto, quando i nodi si trovano fuori delle quadrature, starà a 16″ 35‴ 16ⁱᵛ 36ᵛ come AZ² sta ad AT². C.V.D.

### Proposizione XXXI. Problema XII (moto orario dei nodi nell’orbita ellittica)

**[III.G5.43]** **Trovare il moto orario dei nodi della Luna in un’orbita ellittica.**

**[III.G5.44]** Rappresentino Qpmaq un’ellisse descritta con l’asse maggiore Qq e il minore ab, QAqB il cerchio circoscritto, T la Terra nel centro comune di entrambi, S il Sole, p la Luna che si muove sull’ellisse e pm l’arco che essa descrive in una particella di tempo data piccolissima, N e n i nodi congiunti dalla linea Nn, pK e mk le perpendicolari abbassate sull’asse Qq e prolungate da una parte e dall’altra finché incontrano il cerchio in P e M e la linea dei nodi in D e d. E se la Luna, con il raggio condotto alla Terra, descrive un’area proporzionale al tempo, il moto orario del nodo nell’ellisse sarà come l’area pDdm e AZ² considerate congiuntamente.

**[III.G5.45]** Infatti, tocchi PF il cerchio in P e, prolungata, incontri TN in F; e pf tocchi l’ellisse in p e, prolungata, incontri la stessa TN in f; queste tangenti poi convergano sull’asse TQ in Y; e ML rappresenti lo spazio che la Luna, ruotando nel cerchio, mentre descrive l’arco PM, potrebbe descrivere con moto trasverso, sollecitata e spinta dalla detta forza 3IT, ossia 3PK; e ml rappresenti lo spazio che la Luna, ruotando nell’ellisse, potrebbe descrivere nello stesso tempo, sollecitata anch’essa dalla forza 3IT, ossia 3PK; e si prolunghino LP e lp finché incontrano il piano dell’eclittica in G e g; e si congiungano FG e fg, di cui FG, prolungata, tagli pf, pg e TQ rispettivamente in c, e e R, e fg, prolungata, tagli TQ in r. Poiché la forza 3IT, ossia 3PK, nel cerchio sta alla forza 3IT, ossia 3pK, nell’ellisse come PK sta a pK, ossia come AT sta ad aT, lo spazio ML generato dalla prima forza starà allo spazio ml generato dalla seconda come PK sta a pK, cioè, per la similitudine delle figure PYKp e FYRc, come FR sta a cR. Ma ML sta a FG (per la similitudine dei triangoli PLM, PGF) come PL sta a PG, cioè (per le parallele Lk, PK, GR) come pl sta a pe, cioè (per la similitudine dei triangoli plm, cpe) come lm sta a ce; e, invertendo, come LM sta a lm, ossia come FR sta a cR, così FG sta a ce. E perciò, se fg stesse a ce come fY sta a cY, cioè come fr sta a cR (cioè come fr sta a FR e FR sta a cR considerati congiuntamente, cioè come fT sta a FT e FG sta a ce considerati congiuntamente), poiché il rapporto di FG a ce, tolto da entrambe le parti, lascia i rapporti di fg a FG e di fT a FT, fg starebbe a FG come fT sta a FT; e perciò gli angoli che FG e fg sottenderebbero alla Terra T sarebbero uguali fra loro. Ma quegli angoli (per ciò che abbiamo esposto nella proposizione precedente) sono i moti dei nodi nel tempo in cui la Luna percorre nel cerchio l’arco PM, nell’ellisse l’arco pm; e perciò i moti dei nodi nel cerchio e nell’ellisse sarebbero uguali fra loro. Così andrebbero le cose, se fg stesse a ce come fY sta a cY, cioè se fg fosse uguale a ce×fY/cY. Ma per la similitudine dei triangoli fgp, cep, fg sta a ce come fp sta a cp; e perciò fg è uguale a ce×fp/cp; e perciò l’angolo che fg sottende realmente sta all’angolo precedente, che sottende FG, cioè il moto dei nodi nell’ellisse sta al moto dei nodi nel cerchio, come questa fg, ossia ce×fp/cp, sta alla fg precedente, ossia ce×fY/cY, cioè come fp×cY sta a fY×cp, ossia come fp sta a fY e cY sta a cp; cioè, se ph, parallela a TN, incontra FP in h, come Fh sta a FY e FY sta a FP; cioè come Fh sta a FP, ossia Dp sta a DP, e perciò come l’area Dpmd sta all’area DPMd. E perciò, poiché (per il Cor. 1 della Prop. XXX) quest’ultima area e AZ² considerate congiuntamente sono proporzionali al moto orario dei nodi nel cerchio, la prima area e AZ² considerate congiuntamente saranno proporzionali al moto orario dei nodi nell’ellisse. C.V.D.

**[III.G5.46]** *Cor.* Perciò, poiché, in una posizione data dei nodi, la somma di tutte le aree pDdm, nel tempo in cui la Luna va dalla quadratura a un luogo qualsiasi m, è l’area mpQEd, che termina alla tangente QE dell’ellisse, e la somma di tutte quelle aree, in una rivoluzione intera, è l’area dell’ellisse intera, il moto mediocre dei nodi nell’ellisse starà al moto mediocre dei nodi nel cerchio come l’ellisse sta al cerchio, cioè come Ta sta a TA, ossia come 69 sta a 70. E perciò, poiché (per il Cor. 2 della Prop. XXX) il moto orario mediocre dei nodi nel cerchio sta a 16″ 35‴ 16ⁱᵛ 36ᵛ come AZ² sta ad AT², se si prende l’angolo 16″ 21‴ 3ⁱᵛ 30ᵛ che stia all’angolo 16″ 35‴ 16ⁱᵛ 36ᵛ come 69 sta a 70, il moto orario mediocre dei nodi nell’ellisse starà a 16″ 21‴ 3ⁱᵛ 30ᵛ come AZ² sta ad AT²; cioè come il quadrato del seno della distanza del nodo dal Sole sta al quadrato del raggio.

**[III.G5.47]** Del resto la Luna, con il raggio condotto alla Terra, descrive l’area più velocemente nelle sizigie che nelle quadrature, e per questa ragione il tempo nelle sizigie si contrae, nelle quadrature si allunga; e insieme con il tempo il moto dei nodi aumenta e diminuisce. Ora, il momento dell’area nelle quadrature della Luna stava al suo momento nelle sizigie come 10973 sta a 11073; e perciò il momento mediocre negli ottanti sta all’eccesso nelle sizigie, e al difetto nelle quadrature, come la semisomma dei numeri, 11023, sta alla loro semidifferenza, 50. Quindi, poiché il tempo della Luna in singole particelle uguali dell’orbita è inversamente come la sua velocità, il tempo mediocre negli ottanti starà all’eccesso del tempo nelle quadrature, e al difetto nelle sizigie, dovuti a questa causa, come 11023 sta a 50 con ottima approssimazione. Procedendo poi dalle quadrature alle sizigie, trovo che l’eccesso dei momenti dell’area nei singoli luoghi, sul momento minimo nelle quadrature, è con ottima approssimazione come il quadrato del seno della distanza della Luna dalle quadrature; e perciò la differenza fra il momento in un luogo qualsiasi e il momento mediocre negli ottanti è come la differenza fra il quadrato del seno della distanza della Luna dalle quadrature e il quadrato del seno di 45 gradi, ossia la metà del quadrato del raggio; e l’incremento del tempo nei singoli luoghi fra gli ottanti e le quadrature, e il suo decremento fra gli ottanti e le sizigie, è nello stesso rapporto. Il moto dei nodi, poi, nel tempo in cui la Luna percorre singole particelle uguali dell’orbita, è accelerato o ritardato in rapporto duplicato del tempo. Infatti questo moto, mentre la Luna percorre PM, è (a parità delle altre condizioni) come ML, e ML è in rapporto duplicato del tempo. Perciò il moto dei nodi nelle sizigie, compiuto nel tempo in cui la Luna percorre particelle date dell’orbita, è diminuito in rapporto duplicato del numero 11073 al numero 11023; e il decremento sta al moto restante come 100 sta a 10973, e al moto totale come 100 sta a 11073, con ottima approssimazione. Il decremento nei luoghi fra gli ottanti e le sizigie, e l’incremento nei luoghi fra gli ottanti e le quadrature, sta poi a questo decremento, con ottima approssimazione, come il moto totale in quei luoghi sta al moto totale nelle sizigie e la differenza fra il quadrato del seno della distanza della Luna dalla quadratura e la metà del quadrato del raggio sta alla metà del quadrato del raggio, considerati congiuntamente. Quindi, se i nodi si trovano nelle quadrature, e si prendono due luoghi ugualmente distanti dall’ottante da una parte e dall’altra, e altri due distanti degli stessi intervalli dalla sizigia e dalla quadratura, e dai decrementi dei moti nei due luoghi fra la sizigia e l’ottante si sottraggono gli incrementi dei moti negli altri due luoghi, che sono fra l’ottante e la quadratura, il decremento restante sarà uguale al decremento nella sizigia: come sarà facile constatare a chi faccia il calcolo. Pertanto il decremento mediocre, che va sottratto dal moto mediocre dei nodi, è la quarta parte del decremento nella sizigia. Il moto orario totale dei nodi nelle sizigie, quando si supponeva che la Luna, con il raggio condotto alla Terra, descrivesse un’area proporzionale al tempo, era 32″ 42‴ 7ⁱᵛ. E il decremento del moto dei nodi, nel tempo in cui la Luna, ora più veloce, descrive lo stesso spazio, abbiamo detto che sta a questo moto come 100 sta a 11073; e perciò quel decremento è 17‴ 43ⁱᵛ 11ᵛ, la cui quarta parte, 4‴ 25ⁱᵛ 48ᵛ, sottratta dal moto orario mediocre trovato sopra, 16″ 21‴ 3ⁱᵛ 30ᵛ, lascia 16″ 16‴ 37ⁱᵛ 42ᵛ, moto orario mediocre corretto.

**[III.G5.48]** Se i nodi si trovano fuori delle quadrature, e si considerano due luoghi ugualmente distanti dalle sizigie da una parte e dall’altra, la somma dei moti dei nodi, quando la Luna si trova in questi luoghi, starà alla somma dei moti quando la Luna si trova negli stessi luoghi e i nodi nelle quadrature, come AZ² sta ad AT². E i decrementi dei moti, dovuti alle cause ora esposte, staranno fra loro come i moti stessi; e perciò i moti restanti staranno fra loro come AZ² sta ad AT², e i moti mediocri come i moti restanti. Il moto orario mediocre corretto, in una posizione data qualsiasi dei nodi, sta dunque a 16″ 16‴ 37ⁱᵛ 42ᵛ come AZ² sta ad AT², cioè come il quadrato del seno della distanza dei nodi dalle sizigie sta al quadrato del raggio.

### Proposizione XXXII. Problema XIII (moto medio dei nodi)

**[III.G5.49]** **Trovare il moto medio dei nodi della Luna.**

**[III.G5.50]** Il moto medio annuo è la somma di tutti i moti orari mediocri nell’anno. Immagina che il nodo si trovi in N e che, a ogni ora compiuta, sia riportato indietro al suo luogo precedente, così che, nonostante il suo moto proprio, conservi sempre una posizione data rispetto alle stelle fisse. Immagina inoltre che nel frattempo il Sole S, per il moto della Terra, avanzi a partire dal nodo e compia uniformemente il suo corso annuo apparente. Sia poi Aa un arco dato piccolissimo che la retta TS, condotta sempre al Sole, con la sua intersezione con il cerchio NAn descrive in un tempo dato piccolissimo; e il moto orario mediocre (per quanto si è ora mostrato) sarà come AZ², cioè (essendo proporzionali AZ e ZY) come il rettangolo formato da AZ e ZY, cioè come l’area AZYa. E la somma di tutti i moti orari mediocri dall’inizio sarà come la somma di tutte le aree aYZA, cioè come l’area NAZ. Ma la massima AZYa è uguale al rettangolo formato dall’arco Aa e dal raggio del cerchio; e perciò la somma di tutti i rettangoli nel cerchio intero sta alla somma di altrettanti rettangoli massimi come l’area del cerchio intero sta al rettangolo formato dalla circonferenza intera e dal raggio, cioè come 1 sta a 2. Ora, il moto orario che corrisponde al rettangolo massimo era 16″ 16‴ 37ⁱᵛ 42ᵛ. E questo moto, nell’intero anno siderale di 365 giorni, 6 ore e 9 minuti, diventa 39° 38′ 7″ 50‴. E perciò la sua metà, 19° 49′ 3″ 55‴, è il moto medio dei nodi che corrisponde al cerchio intero. E il moto dei nodi, nel tempo in cui il Sole va da N ad A, sta a 19° 49′ 3″ 55‴ come l’area NAZ sta al cerchio intero.

**[III.G5.51]** Così stanno le cose nell’ipotesi che il nodo sia riportato ogni ora al luogo precedente, così che il Sole, compiuto l’anno intero, ritorni allo stesso nodo da cui si era allontanato all’inizio. Ma per il moto del nodo avviene che il Sole ritorni prima al nodo, e ora si deve calcolare l’abbreviazione del tempo. Poiché il Sole nell’intero anno compie 360 gradi, e il nodo con il moto massimo compirebbe nello stesso tempo 39° 38′ 7″ 50‴, ossia 39,6355 gradi, e il moto mediocre del nodo in un luogo qualsiasi N sta al suo moto mediocre nelle sue quadrature come AZ² sta ad AT², il moto del Sole starà al moto del nodo in N come 360 AT² sta a 39,6355 AZ², cioè come 9,0827646 AT² sta ad AZ². Quindi, se la circonferenza NAn del cerchio intero si divide in particelle uguali Aa, il tempo in cui il Sole percorrerebbe la particella Aa, se il cerchio stesse in quiete, starà al tempo in cui percorre la stessa particella, se il cerchio ruota insieme con i nodi attorno al centro T, inversamente come 9,0827646 AT² sta a 9,0827646 AT² + AZ². Infatti il tempo è inversamente come la velocità con cui la particella è percorsa, e questa velocità è la somma delle velocità del Sole e del nodo. Perciò, se il tempo in cui il Sole, senza il moto del nodo, percorrerebbe l’arco NA si rappresenta con il settore NTA, e la particella di tempo in cui percorrerebbe l’arco piccolissimo Aa si rappresenta con la particella ATa del settore; e (abbassata la perpendicolare aY su Nn) se in AZ si prende dZ di lunghezza tale che il rettangolo dZ per ZY stia alla particella ATa del settore come AZ² sta a 9,0827646 AT² + AZ², cioè tale che dZ stia a ½AZ come AT² sta a 9,0827646 AT² + AZ², il rettangolo dZ per ZY rappresenterà il decremento del tempo dovuto al moto del nodo, in tutto il tempo in cui l’arco Aa è percorso. E se il punto d percorre la curva NdGn, l’area curvilinea NdZ sarà il decremento totale nel tempo in cui è percorso l’intero arco NA; e perciò l’eccesso del settore NAT sull’area NdZ sarà quel tempo totale. E poiché il moto del nodo in un tempo minore è minore in proporzione al tempo, anche l’area AaYZ dovrà essere diminuita nello stesso rapporto. Ciò avverrà se in AZ si prende una lunghezza eZ che stia alla lunghezza AZ come AZ² sta a 9,0827646 AT² + AZ². Così infatti il rettangolo eZ per ZY starà all’area AZYa come il decremento del tempo in cui è percorso l’arco Aa sta al tempo totale in cui sarebbe percorso se il nodo stesse in quiete; e perciò quel rettangolo corrisponderà al decremento del moto del nodo. E se il punto e percorre la curva NeFn, l’area totale NeZ, che è la somma di tutti i decrementi, corrisponderà al decremento totale nel tempo in cui è percorso l’arco AN; e l’area restante NAe corrisponderà al moto restante, che è il moto vero del nodo nel tempo in cui l’intero arco NA è percorso per i moti congiunti del Sole e del nodo. Ora, l’area del semicerchio sta all’area della figura NeFn, trovata con il metodo delle serie infinite, come 793 sta a 60 con ottima approssimazione. Ma il moto che corrisponde al cerchio intero era 19° 49′ 3″ 55‴; e perciò il moto che corrisponde alla figura NeFn duplicata è 1° 29′ 58″ 2‴. Questo, sottratto dal moto precedente, lascia 18° 19′ 5″ 53‴, moto totale del nodo rispetto alle stelle fisse fra due sue congiunzioni con il Sole; e questo moto, sottratto dal moto annuo del Sole di 360 gradi, lascia 341° 40′ 54″ 7‴, moto del Sole fra le stesse congiunzioni. Ma questo moto sta al moto annuo di 360° come il moto del nodo ora trovato, 18° 19′ 5″ 53‴, sta al suo moto annuo, che perciò sarà 19° 18′ 1″ 23‴. Questo è il moto medio dei nodi nell’anno siderale. Lo stesso, secondo le tavole astronomiche, è 19° 21′ 21″ 50‴. La differenza è minore della trecentesima parte del moto totale, e sembra nascere dall’eccentricità dell’orbita lunare e dalla sua inclinazione sul piano dell’eclittica. Per l’eccentricità dell’orbita il moto dei nodi è troppo accelerato, e per la sua inclinazione è a sua volta un poco ritardato e ricondotto alla giusta velocità.

### Proposizione XXXIII. Problema XIV (moto vero dei nodi)

**[III.G5.52]** **Trovare il moto vero dei nodi della Luna.**

**[III.G5.53]** Nel tempo che è come l’area NTA − NdZ (nella figura precedente), questo moto è come l’area NAe, e di qui è dato. Ma, per l’eccessiva difficoltà del calcolo, conviene usare la seguente costruzione del problema. Con centro C e intervallo qualsiasi CD si descriva il cerchio BEFD. Si prolunghi DC fino ad A, così che AB stia ad AC come il moto medio sta alla metà del moto vero mediocre quando i nodi sono nelle quadrature, cioè come 19° 18′ 1″ 23‴ sta a 19° 49′ 3″ 55‴, e perciò BC stia ad AC come la differenza dei moti, 0° 31′ 2″ 32‴, sta al secondo moto, 19° 49′ 3″ 55‴, cioè come 1 sta a 38 3/10; poi per il punto D si conduca la retta infinita Gg, che tocchi il cerchio in D; e se si prende l’angolo BCE, o BCF, uguale al doppio della distanza del Sole dal luogo del nodo trovato con il moto medio, e si conduce AE, o AF, che tagli la perpendicolare DG in G, e si prende un angolo che stia al moto totale del nodo fra le sue sizigie (cioè a 9° 11′ 3″) come la tangente DG sta all’intera circonferenza del cerchio BED, e questo angolo (al posto del quale si può usare l’angolo DAG) si aggiunge al moto medio dei nodi quando i nodi passano dalle quadrature alle sizigie, e si sottrae dallo stesso moto medio quando passano dalle sizigie alle quadrature, si avrà il loro moto vero. Infatti il moto vero così trovato concorderà con ottima approssimazione con il moto vero che risulta rappresentando il tempo con l’area NTA − NdZ e il moto del nodo con l’area NAe, come risulterà a chi esamini la cosa e faccia i calcoli. Questa è l’equazione semestrale del moto dei nodi. C’è anche un’equazione mensile, ma essa non è affatto necessaria per trovare la latitudine della Luna. Infatti, poiché la variazione dell’inclinazione dell’orbita lunare sul piano dell’eclittica è soggetta a una duplice disuguaglianza, l’una semestrale, l’altra mensile, la disuguaglianza mensile di questa e l’equazione mensile dei nodi si temperano e si correggono a vicenda in modo tale che entrambe si possono trascurare nel determinare la latitudine della Luna.

**[III.G5.54]** *Cor.* Da questa proposizione e dalla precedente risulta che i nodi nelle loro sizigie stanno in quiete, nelle quadrature invece regrediscono con un moto orario di 16″ 19‴ 26ⁱᵛ; e che l’equazione del moto dei nodi negli ottanti è 1° 30′. Tutte queste cose si accordano bene con i fenomeni celesti.

### Scolio (il metodo di Machin e Pemberton)

**[III.G5.55]** Con un altro metodo J. Machin, professore di astronomia al Gresham [College], e Henry Pemberton, dottore in medicina, hanno trovato separatamente il moto dei nodi. Di questo metodo si è fatta qualche menzione altrove. E gli scritti dell’uno e dell’altro, che ho visto, contenevano due proposizioni, e concordavano fra loro in entrambe. Aggiungerò qui lo scritto del signor Machin, poiché mi è giunto fra le mani per primo.

#### Il moto dei nodi della Luna

### Proposizione I (Machin: il moto medio del Sole dal nodo)

**[III.G5.56]** «**Il moto medio del Sole dal nodo è definito dalla media proporzionale geometrica fra il moto medio del Sole stesso e quel moto mediocre con cui il Sole si allontana più velocemente dal nodo nelle quadrature.**

**[III.G5.57]** «Sia T il luogo in cui si trova la Terra, Nn la linea dei nodi della Luna in un tempo dato qualsiasi, KTM una retta condotta ad angoli retti con essa, TA una retta che ruota attorno al centro con la velocità angolare con cui il Sole e il nodo si allontanano l’uno dall’altro, così che l’angolo fra la retta in quiete Nn e la retta rotante TA sia sempre uguale alla distanza fra i luoghi del Sole e del nodo. Ora, se una retta qualsiasi TK si divide nelle parti TS e SK, che stiano come il moto orario medio del Sole sta al moto orario mediocre del nodo nelle quadrature, e si pone la retta TH media proporzionale fra la parte TS e l’intera TK, questa retta, fra le altre, sarà proporzionale al moto medio del Sole dal nodo.

**[III.G5.58]** «Si descriva infatti il cerchio NKnM con centro T e raggio TK, e con lo stesso centro e i semiassi TH e TN si descriva l’ellisse NHnL; e, nel tempo in cui il Sole si allontana dal nodo per l’arco Na, se si conduce la retta Tba, l’area del settore NTa rappresenterà la somma dei moti del nodo e del Sole nello stesso tempo. Sia dunque aA l’arco piccolissimo che la retta Tba, ruotando secondo la legge detta, descrive uniformemente in una particella di tempo data; e il settore piccolissimo TAa sarà come la somma delle velocità con cui il Sole e il nodo sono portati, ciascuno per conto suo, in quel tempo. Ora, la velocità del Sole è quasi uniforme, poiché la sua piccola disuguaglianza non produce quasi alcuna diversità nel moto medio dei nodi. L’altra parte di questa somma, cioè la velocità del nodo nella sua quantità mediocre, aumenta, allontanandosi dalle sizigie, in rapporto duplicato del seno della sua distanza dal Sole, per il Cor. della Prop. 31 del Libro III dei *Principia*; e, quando è massima nelle quadrature, con il Sole in K, ha alla velocità del Sole lo stesso rapporto che SK ha a TS, cioè come (la differenza dei quadrati di TK e TH, ovvero) il rettangolo KHM sta al quadrato di TH. Ma l’ellisse NBH divide il settore ATa, che rappresenta la somma di queste due velocità, in due parti ABba e BTb proporzionali alle velocità stesse. Si prolunghi infatti BT fino al cerchio in β, e dal punto B si abbassi sull’asse maggiore la perpendicolare BG, che, prolungata da entrambe le parti, incontri il cerchio nei punti F e f; e poiché lo spazio ABba sta al settore TNb come il rettangolo ABβ sta al quadrato di BT (quel rettangolo infatti è uguale alla differenza dei quadrati di TA e TB, perché la retta Aβ è divisa in parti uguali in T e in parti disuguali in B). Dunque questo rapporto, quando lo spazio ABba è massimo in K, sarà lo stesso del rapporto del rettangolo KHM al quadrato di HT; ma la velocità mediocre massima del nodo stava alla velocità del Sole in questo rapporto. Dunque nelle quadrature il settore ATa è diviso in parti proporzionali alle velocità. E poiché il rettangolo KHM sta al quadrato di HT come FBf sta al quadrato di BG, e il rettangolo ABβ è uguale al rettangolo FBf. La piccola area ABba, dove è massima, starà dunque al settore restante TBb come il rettangolo ABβ sta al quadrato di BG. Ma il rapporto di queste piccole aree era sempre come il rettangolo ABβ sta al quadrato di BT; e perciò la piccola area ABba nel luogo A è minore della piccola area simile nelle quadrature in rapporto duplicato di BG a BT, cioè in rapporto duplicato del seno della distanza del Sole dal nodo. E perciò la somma di tutte le piccole aree ABba, cioè lo spazio ABN, sarà come il moto del nodo nel tempo in cui il Sole si allontana dal nodo per l’arco NA. E lo spazio restante, cioè il settore ellittico NTB, sarà come il moto medio del Sole nello stesso tempo. E perciò, poiché il moto medio annuo del nodo è quello che avviene nel tempo in cui il Sole ha compiuto il suo periodo, il moto medio del nodo dal Sole starà al moto medio del Sole stesso come l’area del cerchio sta all’area dell’ellisse, cioè come la retta TK sta alla retta TH, che è media proporzionale fra TK e TS; o, il che torna lo stesso, come la media proporzionale TH sta alla retta TS.

### Proposizione II (Machin: dal moto medio al moto vero dei nodi)

**[III.G5.59]** «**Dato il moto medio dei nodi della Luna, trovare il moto vero.**

**[III.G5.60]** «Sia l’angolo A la distanza del Sole dal luogo medio del nodo, ossia il moto medio del Sole dal nodo. Allora, se si prende un angolo B la cui tangente stia alla tangente dell’angolo A come TH sta a TK, cioè in rapporto subduplicato del moto orario mediocre del Sole al moto orario mediocre del Sole dal nodo, quando il nodo si trova nelle quadrature, questo angolo B sarà la distanza del Sole dal luogo vero del nodo. Si congiunga infatti FT, e per la dimostrazione della proposizione precedente l’angolo FTN sarà la distanza del Sole dal luogo medio del nodo, l’angolo ATN invece la distanza dal luogo vero, e le tangenti di questi angoli stanno fra loro come TK sta a TH.

**[III.G5.61]** «*Cor.* Di qui l’angolo FTA è l’equazione dei nodi della Luna, e il seno di questo angolo, dove è massimo negli ottanti, sta al raggio come KH sta a TK + TH. Il seno di questa equazione in un altro luogo qualsiasi A sta poi al seno massimo come il seno della somma degli angoli FTN + ATN sta al raggio: cioè, all’incirca, come il seno del doppio della distanza del Sole dal luogo medio del nodo (cioè di 2 FTN) sta al raggio.

### Scolio (Machin: i valori numerici)

**[III.G5.62]** «Se il moto orario mediocre dei nodi nelle quadrature è 16″ 16‴ 37ⁱᵛ 42ᵛ, cioè, nell’intero anno siderale, 39° 38′ 7″ 50‴, TH starà a TK in rapporto subduplicato del numero 9,0827646 al numero 10,0827646, cioè come 18,6524761 sta a 19,6524761. E perciò TH sta a HK come 18,6524761 sta a 1, cioè come il moto del Sole nell’anno siderale sta al moto medio del nodo, 19° 18′ 1″ 23⅔‴.

**[III.G5.63]** «Se invece il moto medio dei nodi della Luna in 20 anni giuliani è 386° 50′ 15″, come si deduce dalle osservazioni usate nella teoria della Luna, il moto medio dei nodi nell’anno siderale sarà 19° 20′ 31″ 58‴. E TH starà a HK come 360° sta a 19° 20′ 31″ 58‴, cioè come 18,61214 sta a 1; donde il moto orario mediocre dei nodi nelle quadrature risulterà 16″ 18‴ 48ⁱᵛ. E l’equazione massima dei nodi negli ottanti 1° 29′ 57″.»

**Fine del gruppo G5 (Propp. XXI–XXXIII). Nel testo originale segue la Prop. XXXIV (*Invenire variationem horariam inclinationis orbis lunaris ad planum eclipticæ*), Fascicolo 25a.**

---

## Apparato

### A.0 Estensioni del glossario

I termini seguenti non comparivano nei glossari comuni né in quelli dei Libri II e III. Ognuno è reso in modo costante in tutto il fascicolo. Quelli marcati † vanno armonizzati dal coordinatore con il Fascicolo 24a.

| Latino | Italiano | Motivazione |
|---|---|---|
| *motus mediocris* (*horarius*), *momentum / tempus / decrementum mediocre* † | «moto mediocre», «momento / tempo / decremento mediocre» | Newton distingue sistematicamente *mediocris* (il valore che compensa le disuguaglianze su un mese lunare, a posizione dei nodi data: Propp. XXX–XXXI) da *medius* (il moto medio su un anno, Prop. XXXII; il «luogo medio» del nodo). La distinzione è necessaria in tre frasi: *Motus medius annuus est summa motuum omnium horariorum mediocrium* (Prop. XXXII), *ut motus medius ad semissem motus veri mediocris* (Prop. XXXIII), *motum ipsius solis medium, & motum illum mediocrem* (Machin, Prop. I). «Mediocre» è usato nel senso antico di «medio, intermedio», non in quello spregiativo, ed è spiegato al lettore nella nota N1. Motte rende entrambi con «mean» e **perde la distinzione**. Il glossario del Libro III fissa *mediocris distantia* «distanza media»: lo conservo per la distanza (non ricorre in questo fascicolo) Il Fascicolo 24a rende *mediocris quantitas* «quantità media» (Propp. XXV–XXVI), dove la distinzione non serve; qui serve, e chiedo al coordinatore di decidere: o «mediocre» in tutto il gruppo G5 (anche «quantità mediocre» nel 24a), o «medio» per entrambi con una nota nelle tre frasi citate. In questo fascicolo *in mediocri sua quantitate* (Machin, Prop. I) è «nella sua quantità mediocre». |
| *motus horarius* | «moto orario» | Il moto in un’ora; Motte «horary motion». |
| *motus progressivus / regressivus*; *progredi / regredi*; *progressus / regressus* | «moto progressivo / regressivo»; «progredire / regredire»; «progresso / regresso» | Prop. XXX: si conserva la coppia latina; «regredire» è il moto dei nodi in antecedenza. |
| *vestigium orbis in plano eclipticæ* | «traccia dell’orbita sul piano dell’eclittica» | È la proiezione ortogonale (Motte la rende proprio «orthographic projection», esplicitando). La Prop. XXXIV usa la stessa parola per il punto (*p vestigium loci illius*): «traccia» vale per entrambi. |
| *contentum* (*sub sinubus trium angulorum*; *PK×PH×AZ*) | «prodotto» | È il prodotto di tre fattori («solido» nel linguaggio geometrico); Motte «solid content». |
| *lineola*; *areola* | «piccola linea»; «piccola area» | Diminutivi tecnici; Motte «little line», «little area». |
| *angulus deflexionis a recto tramite* | «angolo di deviazione dal cammino rettilineo» | Prop. XXX; Motte «angle of the moon’s deflexion from a rectilinear path». |
| *simul & semel* | «tutta insieme e in una volta» | Come nel Fascicolo 3 (L04). |
| *urgente & impellente vi* | «sollecitata e spinta dalla forza» | Glossario: *urgere* «sollecitare» per le forze acceleratrici, *impulsus* «spinta». |
| *motu transverso* | «con moto trasverso» | Prop. XXXI: il moto perpendicolare al piano dell’orbita. |
| *rectangulum sub A & B*; *rectangulum A in B* | «il rettangolo formato da A e B»; «il rettangolo A per B» | Due costrutti latini distinti, resi in modo distinto. |
| *quam proxime* | «con ottima approssimazione» | Come nel Fascicolo 3; dove è attenuato (*quam proxime* dopo un rapporto numerico) resta la stessa resa. |
| *cæteris paribus* | «a parità delle altre condizioni» | Come nel Fascicolo 20. |
| *punctum d tangit curvam NdGn* | «il punto d percorre la curva NdGn» | Alla lettera «tocca»: è il luogo descritto dal punto; Motte «is the locus». |
| *methodus serierum infinitarum* | «metodo delle serie infinite» | Prop. XXXII. |
| *abbreviatio temporis* | «abbreviazione del tempo» | Prop. XXXII. |
| *tabulæ astronomicæ* | «tavole astronomiche» | Prop. XXXII. |
| *æquatio semestris / menstrua* | «equazione semestrale / mensile» | *Semestris* = di sei mesi. Motte «semi-menstrual» è un errore (§ A.5). |
| *inæqualitas* | «disuguaglianza» | Termine astronomico (le «ineguaglianze» del moto); si evita «variazione», riservata a *variatio*. |
| *variatio inclinationis* | «variazione dell’inclinazione» | Non è la *variatio* della Luna (Prop. XXIX), ma il cambiamento dell’inclinazione; il contesto lo rende chiaro. |
| *signum* (*anguli*); *affirmativus / negativus* | «segno»; «positivo / negativo» | Prop. XXX (§ A.1). |
| *sector*; *sector ellipticus* | «settore»; «settore ellittico» | |
| *media proportionalis* (*geometrica*) | «media proporzionale (geometrica)» | Machin, Prop. I. |
| *æqualiter & inæqualiter secta* | «divisa in parti uguali … e in parti disuguali» | Linguaggio euclideo (il teorema del rettangolo delle parti disuguali, Elementi II.5: non verificato sulle fonti allegate). |
| *charta* | «scritto» | Lo Scolio: le carte manoscritte di Machin e Pemberton. |
| *Astron. Prof. Gresham.*; *M. D.*; *D.* (*Machin*) | «professore di astronomia al Gresham [College]»; «dottore in medicina»; «signor» | *Gresham.* abbrevia *Greshamensis*; l’integrazione è tra parentesi quadre (nota N13). |
| *annus Julianus* | «anno giuliano» | Machin, Scolio. |
| terze, quarte, quinte (‴, *iv*, *v*) | ‴, ⁱᵛ, ᵛ | Suddivisioni sessagesimali successive del secondo d’arco (nota N1). |

*Impulsus* non compare come sostantivo; compaiono *impellente* (Propp. XXX e XXXI, «per la spinta», «spinta») e *impressa* (Prop. XXX, «impressa»). *In antecedentia* compare una volta (Prop. XXX, III.G5.40): «in antecedenza», con la nota N2.

### A.1 Proposizione XXX

**Latino:** *Invenire motum horarium nodorum lunæ in orbe circulari.*

**Inglese:** “To find the horary motion of the nodes of the moon in a circular orbit.”

**Scelte.**

- Il titolo è un problema: l’infinito latino (*Invenire*) è reso «Trovare», come nei problemi dei fascicoli precedenti.
- *Designet* (congiuntivo esortativo) → «Rappresentino»: i soggetti sono molti; il latino concorda con il primo.
- *in schemate propositionis illius* → «nello schema di quella proposizione»: rimanda alla figura della Prop. XXV, in cui LM e MT sono definite (Fasc. 24a).
- *Vis posterior MT … eadem est cum vi 3PK vel 3IT*: il valore 3PK della forza MT, nella sua quantità media, è dato nella Prop. XXVI (*ut & vis TM ad mediocrem suam quantitatem 3PK*), non nella XXV; PK e IT sono uguali perché PI e PK sono le perpendicolari dalla Luna su ST e su Qq. Nella trascrizione «3⁢PK», «3⁢IT» contengono un carattere invisibile di moltiplicazione (U+2062), conservato nella Parte B.
- *Cæterum in hoc calculo …*: *quæ calculum nimis impeditum redderent* → «che renderebbero il calcolo troppo complicato». Motte amplia: «such niceties as are **of no moment**, and would only serve to render the calculus more perplexed».
- *simul & semel* → «tutta insieme e in una volta» (§ A.0). Motte: «if the whole had been together, and it once impressed in the point P», frase guasta.
- *ml … mTl … mlTm, IT×PmTm, IT×PHTP*: frazioni appiattite, lette ml/Tm, IT×Pm/Tm, IT×PH/TP; Motte (SVG 1042–1044) concorda.
- *contentum sub sinubus trium angulorum TPI, PTN & STN* → «il prodotto dei seni dei tre angoli TPI, PTN e STN»; la parentesi successiva dice che sono le distanze della Luna dalla quadratura, della Luna dal nodo e del nodo dal Sole.
- *quoties signum anguli alicujus de affirmativo in negativum … mutatur* → «ogni volta che il segno di uno qualsiasi di questi angoli cambia da positivo a negativo». Motte: «as often as the **sine** of any angle is changed from positive to negative». Il senso è lo stesso (conta il segno dei seni del prodotto), ma *signum* potrebbe anche essere una cattiva lettura di *sinus*: punto da controllare sulla stampa (§ A.7).
- *12iv⁤12* → 12½ⁱᵛ (Motte SVG 1045).
- *per excessum regressus supra progressum singulis mensibus feruntur in antecedentia* → «per l’eccesso del regresso sul progresso, sono portati ogni mese in antecedenza». Motte lascia *in antecedentia* in latino.
- La trascrizione ha *A, B syzygias lunæ in plano* **elipticæ** e *Q, q quadraturas lunæ in plano* **elipticæ** (refuso probabile per *eclipticæ*), *altera* **linæ** *MT* (per *lineæ*), *PI, PK;* **;** *perpendicula* (punto e virgola fuori posto) e *Luna* con la maiuscola una volta (*quem Luna dato tempore*): § A.7.

**Corollario 1 (III.G5.41).**

- *Hinc si a dati arcus quam minimi PM terminis P & M …* → «Di qui, se dagli estremi P e M di un arco dato piccolissimo PM …».
- *ut area MPDd & quadratum lineæ AZ conjunctim* → «come l’area MPDd e il quadrato della linea AZ considerati congiuntamente». Nella dimostrazione la stessa area è scritta PDdM e PDdM (lettere nello stesso giro): non è un errore.
- *conjunctis rationibus* → «composti i rapporti».

**Corollario 2 (III.G5.42).**

- *motus horarius mediocris est semissis motus horarii in syzygiis lunæ*: «il moto orario mediocre è la metà del moto orario nelle sizigie della Luna» (§ A.0).
- *& hoc rectangulum, cum sit æquale duobus circulis, duplo majus est quam* **rectangulum prius**: il termine di confronto è la somma delle aree trovata prima (l’area del cerchio), che non è un rettangolo. Motte interpreta «double the quantity of the **former sum**». Traduco alla lettera («del rettangolo precedente») e segnalo il punto: può essere una svista di Newton o una lettura della trascrizione (§ A.7).
- *spatium a se inæquabili cum motu revera confectum* → «lo spazio che percorrono realmente con un moto non uniforme».

### A.2 Proposizione XXXI

**Latino:** *Invenire motum horarium nodorum lunæ in orbe elliptico.*

**Inglese:** “To find the horary motion of the nodes of the moon in an elliptic orbit.”

**Scelte.**

- Il primo capoverso contiene la costruzione e, alla fine, la tesi: *Et si luna … aream describat tempori proportionalem, erit motus horarius nodi in ellipsi ut area pDdm & AZq conjunctim.* La tesi è in tondo, come parte del testo, e non in grassetto, perché il latino non la separa come enunciato.
- *urgente & impellente vi prædicta 3IT, seu 3PK motu transverso* → «con moto trasverso, sollecitata e spinta dalla detta forza 3IT, ossia 3PK».
- *Quoniam vis 3IT seu 3PK in circulo est ad vim 3IT seu 3pK in ellipsi, ut PK ad pK*: la seconda forza è scritta «3IT seu 3pK» sia nel latino sia in Motte. Si conserva.
- *si fg esset ad ce ut* **fY** *ad cY*: Motte scrive «as **fy** to cY» (minuscola), errore di stampa o di trascrizione dell’edizione 1846.
- *ce×fYcY*, *ce×fpcp* → ce×fY/cY, ce×fp/cp (Motte SVG 1046–1048, concordi).
- *seu fp ad fY & cY ad cp* → «ossia come fp sta a fY e cY sta a cp»: rapporto composto, senza *conjunctim* nel latino.
- *area posterior … area prior* → «quest’ultima area» (DPMd, nel cerchio) e «la prima area» (Dpmd, nell’ellisse).

**Corollario (III.G5.46–III.G5.48).**

- *ut Ta ad TA, seu 69 ad 70*: è il rapporto delle distanze nelle sizigie e nelle quadrature trovato nella Prop. XXVIII (*vel numeris rotundis ut 69 ad 70*, Fasc. 24a). Il rapporto dell’ellisse al cerchio circoscritto è quello del semiasse minore al maggiore.
- *Erat autem momentum areæ in quadraturis lunæ ad ejus momentum in syzygiis ut 10973 ad 11073*: il dato è della Prop. XXVI (*seu 10973 ad 11073*); *Erat* rimanda lì senza citarla.
- *decrementum ad motum reliquum ut 100 ad 10973, ad motum vero totum ut 100 ad 11073 quam proxime*: approssimazioni al primo ordine (nota N5).
- La trascrizione ha *in locis* **duabus** *inter syzygiam & octantem*: atteso *duobus* (§ A.7).
- *uti rationem ineunti facile constabit* → «come sarà facile constatare a chi faccia il calcolo»; Motte «as will easily appear by computation».
- Motte stampa due volte i secondi al posto delle terze: «32'' 42'' 7iv.» per 32″ 42‴ 7ⁱᵛ e «16'' 21'' 3iv. 30v.» per 16″ 21‴ 3ⁱᵛ 30ᵛ.

### A.3 Proposizione XXXII

**Latino:** *Invenire motum medium nodorum lunæ.*

**Inglese:** “To find the mean motion of the nodes of the moon.”

**Scelte.**

- *Concipe* (imperativo di seconda persona) → «Immagina», come nel Fascicolo 3 (L33). La frase seguente, *Interea vero solem S … progredi … complere*, dipende ancora da *Concipe*: «Immagina inoltre che nel frattempo il Sole S … avanzi … e compia».
- *per jam ostensa* → «per quanto si è ora mostrato»: rimanda alla conclusione della Prop. XXXI (moto mediocre corretto ∝ AZ²).
- *anno toto sidereo dierum 365. hor. 6. min. 9.* → «nell’intero anno siderale di 365 giorni, 6 ore e 9 minuti».
- *dZ ad 12⁤AZ* = dZ a ½AZ (Motte SVG 1049).
- *si punctum d tangit curvam NdGn* → «se il punto d percorre la curva NdGn» (§ A.0).
- *debebit etiam area AaYZ diminui in eadem ratione*: «in ratione temporis» → «in proporzione al tempo».
- La trascrizione ha *Jam* **vero vero** *area semicirculi* (parola ripetuta) e *ut 9,0827646⁢ATq ad AZq* **Unde** senza punto: § A.7.
- *Differentia minor est parte trecentesima motus totius* → «minore della trecentesima parte»; Motte «less than [SVG 1050] part», con SVG 1050 = 1/300.
- *per eccentricitatem … nimis acceleratur, & per ejus inclinationem vicissim retardatur aliquantulum* → «è troppo accelerato, e … è a sua volta un poco ritardato».
- Motte: «the sun S, by the motion of the earth, **is seen to leave** the node» (aggiunge «is seen»); «the curvilinear area NdZ will be **as** the whole decrement» (aggiunge «as», cioè la proporzionalità, dove il latino dice *erit decrementum totum*); «the motion corresponding **or proportional** to the whole circle» (aggiunta); «19° 49' 3'' 55''» per 55‴.

### A.4 Proposizione XXXIII

**Latino:** *Invenire motum verum nodorum lunæ.*

**Inglese:** “To find the true motion of the nodes of the moon.”

**Scelte.**

- *In tempore quod est ut area NTA-NdZ, (in fig. præced.)* → «Nel tempo che è come l’area NTA − NdZ (nella figura precedente)», cioè la figura della Prop. XXXII.
- La trascrizione ha *ubi* **nNodi** *sunt in quadraturis*: refuso.
- *ut motus medius ad semissem motus veri mediocris* → «come il moto medio sta alla metà del moto vero mediocre» (§ A.0): il «moto vero mediocre» nelle quadrature è 39° 38′ 7″ 50‴ all’anno, la metà 19° 49′ 3″ 55‴.
- *38⁤310* → 38 3/10 (Motte SVG 1051).
- *infinita Gg* → «la retta infinita Gg»; *perpendiculum DG* → «la perpendicolare DG».
- *ad motum totum nodi inter ipsius syzygias (id est, ad 9gr. 11′. 3″.)*: Motte stampa «9° 11'' 3'''». Il valore 9° 11′ 3″ non è la metà di 18° 19′ 5″ 53‴ (sarebbe 9° 9′ 33″): vedi nota N9.
- *Hæc est æquatio semestris motus nodorum* → «Questa è l’equazione semestrale del moto dei nodi». Motte: «the **semi-menstrual** equation», e più avanti «the one **semi-menstrual**, the other menstrual» per *alteri semestri, alteri autem menstruæ*. *Semestris* significa «di sei mesi»: l’equazione dipende dal doppio della distanza del Sole dal nodo e ha periodo di mezzo anno (rispetto al nodo). La resa di Motte («di mezzo mese») è un **errore** (nota N10).
- *se mutuo contemperant & corrigunt* → «si temperano e si correggono a vicenda».
- Cor.: *Quæ omnia cum phænomenis cœlestibus probe quadrant* → «si accordano bene»; Motte «**exactly** agree», che rafforza.

### A.5 Scolio e scritto di Machin

- **Nomi.** *J. Machin Astron. Prof. Gresham.* → «J. Machin, professore di astronomia al Gresham [College]»; *Hen. Pemberton M. D.* → «Henry Pemberton, dottore in medicina»; *D. Machin* → «del signor Machin». Motte: «Mr. Machin, Astron., Prof. Gresh., and Dr. Henry Pemberton». Nessuna notizia biografica oltre a queste risulta dalle fonti allegate (nota N13).
- *Hujus methodi mentio quædam alibi facta est* → «Di questo metodo si è fatta qualche menzione altrove». Il latino non dice dove, né se *hujus* si riferisca al metodo comune o a quello di Pemberton; non risolvo l’ambiguità.
- *& inter se in utrisque congruebant* → «e concordavano fra loro in entrambe»; Motte «**exactly** agreed».
- *cum prior in manus meas venerit* → «poiché mi è giunto fra le mani per primo»; *prior* è riferito alla carta.
- Machin, Prop. I: *hæc recta* **inter reliquas** *proportionalis erit motui medio solis a nodo* → «questa retta, fra le altre, sarà proporzionale …»: la retta TH, insieme alle altre (TS, SK, TK), rappresenta i moti nella stessa scala. Motte **omette** *inter reliquas*.
- *Solis autem velocitas ferè uniformis est, utpote cujus parva inæqualitas vix ullam inducit in medio nodorum motu varietatem* → «… non produce quasi alcuna diversità nel moto medio dei nodi»: *varietas* «diversità», per non confonderla con *variatio*.
- *per Coroll. Prop. 31. Lib. 3tii Princip.* → «per il Cor. della Prop. 31 del Libro III dei *Principia*»: Machin cita con numeri arabi; *3tii* = *tertii*. Motte: «by Cor. Prop. XXXI, of this Book».
- *velocitas nodi in mediocri sua quantitate* → «la velocità del nodo nella sua quantità mediocre» (§ A.0).
- *& cum maxima est in quadraturis ad solem in K* → «e, quando è massima nelle quadrature, con il Sole in K»: il nodo è in quadratura rispetto al Sole quando la retta rotante TA è in K.
- *spatium ABba est ad sectorem* **TNb**: il ragionamento richiede il settore **TBb** (la parte BTb del settore ATa, nominata due frasi prima e due frasi dopo). Motte ha «the sector TBb». Probabile refuso della trascrizione o della stampa (§ A.7); la traduzione conserva TNb e la Parte B lo annota.
- La frase *& quoniam spatium ABba est ad sectorem TNb …(…)* resta senza principale; la principale è la frase successiva (*Hæc igitur ratio …*). La traduzione conserva l’anacoluto. Allo stesso modo *Et quoniam rectang. KHM … æquatur rectangulo FBf.* regge la frase seguente *Erit igitur …*.
- *ocurrat* (refuso probabile per *occurrat*); *demitta‹453›tur* (marcatore di pagina dentro la parola); *datâ* (accento circonflesso della stampa).
- *motus nodi medius a sole* → «il moto medio del nodo dal Sole», cioè il moto relativo, simmetrico di «moto medio del Sole dal nodo».
- Prop. II: *in subduplicata ratione motus mediocris horarii solis ad motum mediocrem horarium solis a nodo in quadraturis versante* → «… quando il nodo si trova nelle quadrature»: l’ablativo assoluto ha come soggetto sottinteso il nodo; Motte fa la stessa lettura («when the node is in the quadrature»).
- Cor.: *ut sinus summæ angulorum FTN+ATN ad radium* → «come il seno della somma degli angoli FTN + ATN sta al raggio»; Motte «the sine of the sums» (plurale improprio). *2⁢FTN* → 2 FTN.
- Scolio: *19°. 18′, 1″. 23‴⁤23* → 19° 18′ 1″ 23⅔‴ (Motte SVG 1055); *19°. 20′ 31″. 58‴.* (punto mancante dopo 20′, punteggiatura).
- Lo Scolio di Machin si chiude, in Motte, con le virgolette di chiusura; nella trascrizione latina non ci sono virgolette di chiusura.

### A.6 Rimandi

**Rimandi ai Libri I e II.** Nel perimetro di questo fascicolo **non ce n’è nessuno**: le Propp. XXX–XXXIII e lo scritto di Machin citano soltanto proposizioni del Libro III. (La Prop. XXV, citata due volte, poggia a sua volta sul Cor. 17 della Prop. LXVI del Libro I, ma quel rimando è nel Fasc. 24a.)

**Rimandi interni al Libro III, verificati sul latino.**

| Luogo | Latino | Resa | Verifica |
|---|---|---|---|
| III.G5.38 (due volte) | *per prop. xxv.* | «per la Prop. XXV» | Regge: la Prop. XXV dà la forza ML media come TP e il rapporto alla forza centripeta 1 a 178 29/40 = 178,725 (*ut 1000 ad 178725*). Il valore 3PK di MT è nella Prop. XXVI; Newton qui cita la XXV per il numero 178,725. |
| III.G5.40 | *ut supra diximus* | «come abbiamo detto sopra» | rimanda al rapporto 1 : 59,575 dello stesso capoverso III.G5.38. |
| III.G5.45 | *per ea quæ in præcedente propositione exposuimus* | «per ciò che abbiamo esposto nella proposizione precedente» | Prop. XXX: il moto dei nodi è l’angolo mTl sotteso da ml in T. Regge. |
| III.G5.45 | *per corol. 1. prop. xxx.* | «per il Cor. 1 della Prop. XXX» | moto orario ∝ area PDdM × AZ². Regge. |
| III.G5.46 | *per corol. 2. prop. xxx.* | «per il Cor. 2 della Prop. XXX» | moto mediocre : 16″ 35‴ 16ⁱᵛ 36ᵛ = AZ² : AT². Regge. |
| III.G5.46 | *ut Ta ad TA, seu 69 ad 70* (non citato) | — | Prop. XXVIII: *ut 69 ad 70*. Regge. |
| III.G5.47 | *Erat autem momentum areæ … ut 10973 ad 11073* (non citato) | «stava» | Prop. XXVI: *seu 10973 ad 11073*. Regge. |
| III.G5.50 | *per jam ostensa* | «per quanto si è ora mostrato» | Prop. XXXI, ultimo capoverso. Regge. |
| III.G5.53 | *in fig. præced.* | «nella figura precedente» | figura della Prop. XXXII (aree NTA, NdZ, NAe). Regge. |
| III.G5.54 | *Ex hac & præcedente propositione* | «Da questa proposizione e dalla precedente» | Propp. XXXIII e XXXII. Regge per l’equazione negli ottanti (1° 30′, nota N9); il moto orario 16″ 19‴ 26ⁱᵛ non si ricava direttamente dalle due proposizioni (nota N9). |
| III.G5.58 | *per Coroll. Prop. 31. Lib. 3tii Princip.* | «per il Cor. della Prop. 31 del Libro III dei *Principia*» | Prop. XXXI, Cor. (e ultimo capoverso): il moto mediocre è come il quadrato del seno della distanza del nodo dal Sole. Regge. |
| III.G5.60 | *ex demonstratione propositionis superioris* | «per la dimostrazione della proposizione precedente» | Machin, Prop. I. Regge. |
| III.G5.55 | *Hujus methodi mentio quædam alibi facta est* | «se n’è fatta qualche menzione altrove» | **Non verificabile** sulle fonti allegate. |

**Rimandi non tornati:** nessuno. Un solo punto da segnalare: il valore 3PK (Prop. XXX) è della Prop. XXVI, non della XXV citata.

### A.7 Refusi e anomalie della trascrizione

| Luogo | Trascrizione | Lettura | Tipo |
|---|---|---|---|
| III.G5.38 | *in plano elipticæ* (due volte) | *eclipticæ* | refuso probabile |
| III.G5.38 | *altera linæ MT* | *lineæ* | refuso probabile |
| III.G5.38 | *PI, PK; perpendicula* | *PI, PK perpendicula* | punteggiatura |
| III.G5.39 | *quem Luna dato tempore* | *luna* | maiuscola isolata (irrilevante) |
| III.G5.40 | *Et quoties signum anguli alicujus* | *signum* o *sinus*? | da controllare (Motte «sine») |
| III.G5.42 | *duplo majus est quam rectangulum prius* | *summa prior*? | da controllare; il senso richiede la somma precedente |
| III.G5.47 | *in locis duabus* | *duobus* | concordanza (refuso probabile) |
| III.G5.51 | *Jam vero vero area* | *Jam vero area* | parola ripetuta |
| III.G5.51 | *ad AZq Unde* | *ad AZq. Unde* | punto mancante |
| III.G5.53 | *ubi nNodi sunt* | *nodi* | refuso |
| III.G5.58 | *ocurrat* | *occurrat* | refuso probabile |
| III.G5.58 | *ad sectorem TNb* | *TBb* | lettera probabilmente errata (Motte TBb) |
| III.G5.62 | *19°. 18′, 1″* | *18′. 1″* | punteggiatura |
| III.G5.63 | *19°. 20′ 31″* | *20′. 31″* | punteggiatura |
| passim | «12iv⁤12», «38⁤310», «12⁤AZ», «23‴⁤23», «mlTm», «IT×PmTm», «IT×PHTP», «ce×fYcY», «ce×fpcp» | 12½ⁱᵛ, 38 3/10, ½AZ, 23⅔‴, ml/Tm, IT×Pm/Tm, IT×PH/TP, ce×fY/cY, ce×fp/cp | frazioni appiattite (artefatto della pagina web), tutte confermate dagli SVG di Motte |

Nessuno di questi punti è stato verificato sulla stampa del 1726. La traduzione segue il senso; la Parte B riporta il latino esatto della trascrizione.

**Punti da controllare sulla stampa ECCO.**

| Pagina 1726 | Trascrizione | Lettura attesa | Motivo |
|---|---|---|---|
| p. 437 | *in plano elipticæ* (due volte) | *eclipticæ* | grafia anomala ripetuta: può essere della stampa |
| p. 437 | *altera linæ MT* | *lineæ* | lettera mancante |
| p. 440 | *quoties signum anguli alicujus* | *sinus*? | Motte traduce «sine»; il ragionamento riguarda i segni dei seni |
| p. 441 | *quam rectangulum prius* | *quam summa prior*? | il termine di confronto non è un rettangolo |
| p. 446 | *in locis duabus* | *duobus* | concordanza |
| p. 449 | *Jam vero vero* | *Jam vero* | parola ripetuta |
| p. 450 | *ubi nNodi* | *nodi* | lettera doppia |
| p. 451 | *ad 9gr. 11′. 3″.* | (conferma della cifra) | la cifra non è la metà di 18° 19′ 5″ 53‴ (nota N9); Motte «9° 11'' 3'''» |
| p. 453 | *ocurrat* | *occurrat* | consonante mancante |
| p. 453 | *ad sectorem TNb* | *TBb* | il ragionamento e Motte richiedono TBb |
| p. 454 | *19°. 18′, 1″. 23‴⁤23* | 23⅔‴ | confermare la frazione (il calcolo dà 23½‴, nota N12) |

### A.8 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| III.G5.38 | *vestigium orbis* | «orthographic projection» | esplicitazione corretta |
| III.G5.38 | *minutiis, quæ calculum nimis impeditum redderent* | «such niceties as are of no moment, and would only serve to render the calculus more perplexed» | ampliamento |
| III.G5.39 | *si tota simul & semel in loco P impressa esset* | «if the whole had been together, and it once impressed in the point P» | sintassi guasta |
| III.G5.40 | *signum anguli* | «the sine of any angle» | parola diversa (vedi § A.1) |
| III.G5.40 | *in antecedentia* | «in antecedentia» | lasciato in latino |
| III.G5.42 | *quam rectangulum prius* | «the former sum» | interpretazione (probabilmente giusta) |
| III.G5.45 | *fY ad cY* | «fy to cY» | lettera errata |
| III.G5.47 | *32″. 42‴. 7iv.*; *16″. 21‴. 3iv. 30v.* | «32'' 42'' 7iv.»; «16'' 21'' 3iv. 30v.» | segni sessagesimali errati |
| III.G5.50 | *progredi a nodo* | «is seen to leave the node» | aggiunta di «is seen» |
| III.G5.50 | *19gr. 49′. 3″. 55‴* | «19° 49' 3'' 55''» | segno errato |
| III.G5.51 | *erit decrementum totum* | «will be as the whole decrement» | aggiunta di «as» |
| III.G5.51 | *qui respondet circulo toti* | «corresponding or proportional to» | aggiunta |
| III.G5.53 | *19gr. 49′. 3″. 55‴.* | «19° 49' 3'' 55''» | segno errato |
| III.G5.53 | *9gr. 11′. 3″.* | «9° 11'' 3'''» | segni errati |
| III.G5.53 | *æquatio semestris*; *alteri semestri* | «semi-menstrual» (due volte) | **errore di senso** (semestrale → semimensile) |
| III.G5.54 | *probe quadrant* | «exactly agree» | rafforzamento |
| III.G5.55 | *inter se … congruebant* | «exactly agreed» | aggiunta di «exactly» |
| III.G5.57 | *inter reliquas* | — | omissione |
| III.G5.58 | *Lib. 3tii Princip.* | «of this Book» | adattamento corretto |
| III.G5.58 | *sectorem TNb* | «sector TBb» | Motte ha la lettera attesa |
| III.G5.58 | *ut rectang. ABβ ad BG quadr.* | «to BG2» senza punto | punteggiatura |
| III.G5.61 | *sinus summæ* | «the sine of the sums» | plurale improprio |

**Formule SVG di Motte.** Ho controllato tutte le 14 formule del perimetro (SVG 1042–1055) sul LaTeX di `svg_tex.tsv`: 1042 ml/Tm, 1043 IT×Pm/Tm, 1044 IT×PH/TP, 1045 12½ⁱᵛ, 1046 ce×fY/cY, 1047 e 1048 ce×fp/cp, 1049 ½AZ, 1050 1/300, 1051 38 3/10, 1052 β, 1053 ABβ, 1054 Aβ, 1055 23⅔‴. **Tutte tornano con il latino.** Tabella «SVG di Motte che non tornano con il latino»:

| n | LaTeX | Lettura attesa |
|---|---|---|
| — | — | nessuna |

(L’SVG 1041, 16 15/16, appartiene alla Prop. XXIX, Fasc. 24a.)

---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. Le verifiche numeriche sono state eseguite con lo script `tmp/24b/verifica.py` (aritmetica sessagesimale esatta con frazioni; quadrature e integrazioni numeriche con SciPy). Ciò che proviene da conoscenza generale e non dalle fonti allegate è marcato «(non verificato sulle fonti allegate)».

### N1. Unità sessagesimali; «medio» e «mediocre»

Newton divide il grado in 60 primi (′), il primo in 60 secondi (″), il secondo in 60 terze (‴), la terza in 60 quarte (ⁱᵛ), la quarta in 60 quinte (ᵛ). Una quinta d’arco vale 1/(60⁵) di grado ≈ 1,3·10⁻⁹ gradi: la precisione è aritmetica, non osservativa. Nel testo i valori sono riportati come in Newton; 12½ⁱᵛ è «dodici quarte e mezza».

«Moto medio» (*medius*) è il moto uniforme che dà, su un anno, lo stesso spostamento del moto reale. «Moto mediocre» (*mediocris*) è un valore intermedio che compensa le disuguaglianze in un mese lunare, a posizione data dei nodi: per esempio il moto orario mediocre della Prop. XXX, Cor. 2, è la media sul giro della Luna con i nodi fermi rispetto al Sole. Il moto medio annuo (Prop. XXXII) si ottiene poi sommando i moti mediocri lungo l’anno.

### N2. Prop. XXX: la regola del moto dei nodi

**La figura (ricostruita).** T è al centro dell’orbita circolare; la linea dei nodi Nn sta nel piano dell’eclittica; il Sole S è nella direzione TA; Q e q sono le quadrature. La forza perturbatrice utile è la componente MT = 3IT, parallela a ST: è perpendicolare alla linea Qq delle quadrature e proporzionale alla distanza IT = PK della Luna da quella linea. Questa forza ha una componente perpendicolare al piano dell’orbita proporzionale a PH/TP (il seno della distanza della Luna dal nodo) e ad AZ/AT (il seno della distanza del nodo dal Sole); da qui il prodotto dei tre seni.

**In formule moderne** (non nel testo). Detti *u* la distanza della Luna dal nodo, *η* la distanza del nodo dal Sole, *ψ* la distanza della Luna dalla quadratura, la regola di Newton è

Ω̇ = −Ω̇ₘₐₓ · sin ψ · sin *u* · sin *η*,  con Ω̇ₘₐₓ = *n*/59,575,

dove *n* è il moto medio della Luna e 59,575 = 178,725/3, con 178,725 = (*T*☉/*T*☾)² ≈ (365 g 6 h 9 m / 27 g 7 h 43 m)² (Prop. XXV). Il segno meno indica il regresso. Il fattore sin ψ cambia segno alle quadrature, sin *u* ai nodi: per questo i nodi progrediscono quando la Luna è fra una quadratura e il nodo più vicino, e regrediscono altrimenti.

**«In antecedenza»** (*in antecedentia*): contro il verso del moto dei corpi celesti, cioè verso le longitudini decrescenti; è il regresso dei nodi. Nel corso di un mese il regresso prevale sul progresso.

### N3. Prop. XXX: i numeri

- 178,725/3 = 59,575: esatto.
- 32′ 56″ 27‴ 12½ⁱᵛ / 59,575 = 33″ 10‴ 33ⁱᵛ 12ᵛ: esatto (all’arrotondamento della quinta).
- Il moto medio orario della Luna di Newton, 32′ 56″ 27‴ 12½ⁱᵛ, corrisponde a un mese siderale di 27 g 7 h 43 m 12 s. Con i 27 g 7 h 43 m della Prop. XXV si avrebbe 32′ 56″ 27‴ 48ⁱᵛ: la differenza (35 quarte) è trascurabile e mostra che Newton usa qui un valore del mese più preciso di quello arrotondato della Prop. XXV. Il valore moderno del mese siderale, 27,32166 g = 27 g 7 h 43 m 11,5 s, è vicinissimo (non verificato sulle fonti allegate).

### N4. Prop. XXX, Cor. 1 e 2: dall’area al moto mediocre

Il Cor. 1 trasforma il prodotto dei tre seni in un’area: PK·PH ∝ Kk·PD (perché Kk ∝ PK per archi PM uguali e PH ∝ PD·AZ), quindi il moto orario è come l’area PDdM per AZ². Il Cor. 2 somma queste aree in un mese: la somma algebrica (le aree fuori del cerchio si sottraggono, perché lì i nodi progrediscono) è l’area del cerchio, mentre con il valore massimo costante si avrebbe il rettangolo circonferenza × raggio, doppio del cerchio. In termini moderni: la media di sin²ψ su un giro vale ½. Quindi il moto mediocre, con i nodi in quadratura, è 33″ 10‴ 33ⁱᵛ 12ᵛ / 2 = 16″ 35‴ 16ⁱᵛ 36ᵛ (verificato), e in generale è proporzionale a sin²*η* = AZ²/AT².

### N5. Prop. XXXI: l’ellisse e la correzione per il momento dell’area

- **Ellisse.** La Luna percorre l’ellisse della Prop. XXVIII, con il centro in T e i semiassi nel rapporto 69 : 70. Proiettando sul cerchio circoscritto, Newton mostra che il moto dei nodi nell’ellisse sta a quello nel cerchio come le aree corrispondenti Dpmd : DPMd, quindi come le ordinate pK : PK; mediato su un giro, come l’area dell’ellisse a quella del cerchio, 69 : 70. 16″ 35‴ 16ⁱᵛ 36ᵛ × 69/70 = 16″ 21‴ 3ⁱᵛ 30ᵛ (verificato).
- **Momento dell’area.** Per la Prop. XXVI l’area descritta in tempi uguali non è costante: 10973 nelle quadrature, 11073 nelle sizigie, 11023 negli ottanti. Nelle sizigie la Luna è più veloce, resta meno tempo in ogni particella d’orbita, e il moto dei nodi (che è come ML, cioè come il quadrato del tempo) diminuisce. Il decremento relativo è (11073/11023)² − 1 ≈ 100/11023: Newton scrive 100/10973 rispetto al moto restante e 100/11073 rispetto al moto totale. I valori esatti sono 1 − (11023/11073)² = 0,009011 e (11073/11023)² − 1 = 0,009093, contro 100/11073 = 0,009031 e 100/10973 = 0,009113: le approssimazioni sono al primo ordine e coerenti fra loro (*quam proxime*).
- **La «quarta parte».** Con i nodi in quadratura il moto è ∝ sin²ψ e il decremento relativo è ∝ (sin²ψ − ½)/½. La media di sin²ψ · (sin²ψ − ½)/½ su un quarto di giro, integrata numericamente, vale **esattamente 0,25**: la regola di Newton («il decremento mediocre è la quarta parte del decremento nella sizigia») è esatta nel suo modello.
- **I numeri.** 2 × 16″ 21‴ 3ⁱᵛ 30ᵛ = 32″ 42‴ 7ⁱᵛ; × 100/11073 = 17‴ 43ⁱᵛ 11ᵛ; un quarto = 4‴ 25ⁱᵛ 48ᵛ; 16″ 21‴ 3ⁱᵛ 30ᵛ − 4‴ 25ⁱᵛ 48ᵛ = 16″ 16‴ 37ⁱᵛ 42ᵛ. **Tutte le cifre tornano.**

### N6. Il moto orario mediocre corretto come grandezza fisica

16″ 16‴ 37ⁱᵛ 42ᵛ all’ora è il moto mediocre dei nodi quando questi sono nelle quadrature (il Sole a 90° dalla linea dei nodi), cioè il massimo dei moti mediocri. In un anno siderale di 8766,15 ore farebbe 39° 38′ 7″ 50‴ (verificato). Il moto reale è circa la metà, perché il fattore sin²*η* vale in media ½: è il punto di partenza della Prop. XXXII.

### N7. Prop. XXXII: la figura NeFn e il rapporto 793 : 60

**Ricostruzione.** Sia AT = 1 e *η* l’angolo NTA (distanza del Sole dal nodo); allora AZ = sin *η* e la velocità relativa del Sole rispetto al nodo è 1 + sin²*η*/*k*, con *k* = 360/39,6355 = 9,0827646 (rapporto fra il moto annuo del Sole e il moto massimo annuo del nodo). Il punto e sta su AZ con eZ = AZ · AZ²/(*k* + AZ²); l’area della figura NeFn sopra il diametro Nn è

∫₀^π sin⁴*η* / (*k* + sin²*η*) d*η* = 0,1188497.

Il rapporto semicerchio/NeFn = (π/2)/0,1188497 = **13,216663**; Newton dà 793/60 = 13,216667. L’accordo è di tre parti su dieci milioni: il «metodo delle serie infinite» di Newton dà un risultato quasi esatto.

**Il rapporto 9,0827646.** 360/39,6355 = 9,0827667; con il valore non arrotondato 39° 38′ 7″ 50‴ = 39,6355093° si ottiene 9,0827646, la cifra di Newton.

### N8. Prop. XXXII: i numeri e un controllo indipendente

- 19° 49′ 3″ 55‴ × 60/793 = 1° 29′ 58″ 2‴; 19° 49′ 3″ 55‴ − 1° 29′ 58″ 2‴ = 18° 19′ 5″ 53‴; 360° − 18° 19′ 5″ 53‴ = 341° 40′ 54″ 7‴; 360° × 18° 19′ 5″ 53‴ / 341° 40′ 54″ 7‴ = **19° 18′ 1″ 23‴**. **Tutte le cifre tornano.**
- **Forma chiusa.** Il modello di Newton (velocità relativa Sole–nodo = *s* + *n* sin²*η*, con *s* = 360° e *n* = 39,6355° all’anno) si integra esattamente: il moto medio relativo è √(*s*(*s* + *n*)), media geometrica fra *s* e *s* + *n*. È proprio l’enunciato della Prop. I di Machin. Il moto medio dei nodi risulta √(360 × 399,6355) − 360 = 19° 18′ 1″ 23½‴, che coincide con il risultato di Newton.
- **Integrazione numerica** dell’equazione d*η*/d*t* = *s* + *n* sin²*η*: il Sole ritorna al nodo dopo 0,9491158 anni, e nel frattempo il nodo si è mosso di 18° 19′ 5″ 53‴; per anno, 19° 18′ 1″ 24‴. Conferma indipendente.
- **Tavole.** 19° 21′ 21″ 50‴ − 19° 18′ 1″ 23‴ = 3′ 20″ 27‴, cioè 1/348 del moto: «minore della trecentesima parte», come dice Newton.
- **Confronto moderno.** Il regresso dei nodi lunari è oggi di circa 19,355° per anno siderale, con un periodo di circa 18,61 anni (non verificato sulle fonti allegate). Il valore di Newton (19,300°) è più basso dello 0,3 %; quello delle tavole (19,356°) coincide con il moderno.

### N9. Prop. XXXIII: la costruzione; 9° 11′ 3″ e il corollario

**La costruzione (ricostruita).** Su una retta stanno, in ordine, D, C, B, A, con il cerchio di centro C e raggio CD = CB = 1 e AC = 38,3. L’angolo BCE è il doppio della distanza del Sole dal luogo medio del nodo; AE incontra in G la tangente in D. L’equazione è l’angolo che sta a 9° 11′ 3″ come DG sta alla circonferenza.

- BC : AC = 0° 31′ 2″ 32‴ : 19° 49′ 3″ 55‴ = 1 : 38,305 (Newton 38 3/10); la differenza 19° 49′ 3″ 55‴ − 19° 18′ 1″ 23‴ = 0° 31′ 2″ 32‴ è esatta.
- **Negli ottanti** (BCE = 90°) DG = 39,3/38,3 = 1,0261 e l’equazione vale 9° 11′ 3″ × 1,0261/(2π) = **1° 30′ 0″**, esattamente il valore del Cor.; il massimo, 1° 30′ 1″, si ha per BCE ≈ 88,5°. L’angolo DAG, che Newton permette di usare al suo posto, vale negli ottanti 1° 29′ 44″.
- **Il valore 9° 11′ 3″.** Il «moto totale del nodo fra le sue sizigie» dovrebbe essere la metà del moto del nodo fra due congiunzioni con il Sole. Con il valore della Prop. XXXII (18° 19′ 5″ 53‴) la metà sarebbe 9° 9′ 33″, e la cifra **non torna**. Torna invece se si parte dal moto annuo delle tavole astronomiche, 19° 21′ 21″ 50‴: il moto del nodo fra due congiunzioni è allora 360° × *t*/(360° + *t*) = 18° 22′ 6″, la cui metà è **9° 11′ 3″**. Newton sembra dunque usare qui il moto medio delle tavole e non il proprio. È una mia ricostruzione: il testo non lo dice. Segnalo la cifra senza correggerla.
- **Il corollario.** Il moto orario dei nodi nelle quadrature, 16″ 19‴ 26ⁱᵛ, non è il 16″ 16‴ 37ⁱᵛ 42ᵛ della Prop. XXXI. Si ottiene (16″ 19‴ 27ⁱᵛ) moltiplicando quest’ultimo per il rapporto fra il moto delle tavole e quello teorico, 19° 21′ 21″ 50‴ / 19° 18′ 1″ 23‴: anche qui Newton sembra ricondurre il valore teorico alle tavole (mia ricostruzione, non nel testo; Newton tronca a 26ⁱᵛ).

### N10. «Equazione»; equazione semestrale e mensile

L’**equazione** (*æquatio*) è, nel linguaggio astronomico, la correzione da aggiungere al moto medio (o al luogo medio) per ottenere il moto vero (o il luogo vero). Qui il luogo vero del nodo si ottiene dal luogo medio aggiungendo o sottraendo un angolo che dipende dal doppio della distanza del Sole dal nodo: si annulla nelle sizigie e nelle quadrature dei nodi ed è massimo, circa 1° 30′, negli ottanti. Poiché il Sole torna alla stessa posizione rispetto al nodo dopo circa 346 giorni, il doppio dell’angolo compie un giro in circa mezzo anno: per questo l’equazione è **semestrale**. La resa «semi-menstrual» di Motte (di mezzo mese) è sbagliata. Il termine principale moderno del moto del nodo lunare ha la stessa forma, con ampiezza di circa 1,5° (non verificato sulle fonti allegate). L’equazione «mensile» dipende invece dalla posizione della Luna nel mese; Newton afferma che essa e la corrispondente disuguaglianza dell’inclinazione si compensano nel calcolo della latitudine.

### N11. Machin, Propp. I–II: la dimostrazione e le verifiche

**Prop. I.** Detta *s* la velocità del Sole e *n* il moto mediocre massimo del nodo, la velocità relativa è *s* + *n* sin²*η*. Machin la rappresenta con un settore piccolissimo del cerchio di raggio TK, diviso dall’ellisse di semiassi TK e TH (con TH² = TS·TK e TS : SK = *s* : *n*) in una parte BTb, proporzionale al moto del Sole, e in una parte ABba, proporzionale al moto del nodo. Sommando, il cerchio rappresenta il moto relativo e l’ellisse il moto del Sole nello stesso tempo; il rapporto delle aree è TK : TH, quindi il moto medio relativo sta al moto del Sole come TK : TH = √((*s* + *n*)/*s*). È la media geometrica √(*s*(*s* + *n*)), come in N8. Con i numeri di Newton dà 19° 18′ 1″ 23½‴, d’accordo con il risultato «per serie» della Prop. XXXII.

**Prop. II.** Integrando d*η*/d*t* = *s* + *n* sin²*η* si ha tan *η* = √(*s*/(*s* + *n*)) · tan *M*, dove *M* è l’angolo medio: è esattamente «tan B : tan A = TH : TK». Un’integrazione numerica indipendente conferma la relazione con uno scarto massimo di 6·10⁻¹¹ radianti.

**Cor.** Se tan B = *k* tan A, allora sin(A − B) = ((1 − *k*)/(1 + *k*)) sin(A + B): è l’identità di Machin, con (1 − *k*)/(1 + *k*) = KH/(TK + TH). L’equazione massima si ha quando A + B = 90°, cioè negli ottanti.

**Newton e Machin.** Il rapporto AC/BC = 38,305 della costruzione di Newton coincide con 2·TH/HK + 1 = (TK + TH)/KH di Machin; per questo l’angolo DAG di Newton negli ottanti (1° 29′ 44″) coincide quasi con l’equazione massima di Machin con gli stessi dati (1° 29′ 45″). La costruzione di Newton è un’approssimazione della soluzione esatta di Machin.

### N12. Machin, Scolio: i numeri

- √(9,0827646/10,0827646) = 0,9491158 = 18,6524761/19,6524761: esatto; TH/HK = 18,6524761: esatto.
- 360°/18,6524761 = 19° 18′ 1″ 23‴ 30ⁱᵛ = 19° 18′ 1″ 23½‴. Machin scrive **23⅔‴** (SVG 1055 di Motte concorde): lo scarto è di 10 quarte, irrilevante, ma la frazione non torna con il calcolo. Segnalata senza correzione.
- 386° 50′ 15″ in 20 anni giuliani = 19° 20′ 30″ 45‴ per anno giuliano; per l’anno siderale di 365 g 6 h 9 m si ottiene 19° 20′ 31″ 56‴. Machin dà 58‴: torna con un anno siderale di 365,25638 g (365 g 6 h 9 m 11 s). Scarto di 2‴, irrilevante.
- 360°/19° 20′ 31″ 58‴ = 18,61214: esatto. Con questo valore il moto orario mediocre nelle quadrature risulta 16″ 18‴ 48ⁱᵛ (verificato) e l’equazione massima arcsin(1/(2·18,61214 + 1)) = 1° 29′ 57″ (verificato). Con il valore teorico 18,6524761 l’equazione massima sarebbe 1° 29′ 45″.
- Il numero 18,61214 è anche il numero di anni siderali in cui i nodi compiono un giro intero rispetto alle stelle (360° diviso il moto annuo): è il ciclo di circa 18,6 anni noto oggi come periodo di regressione dei nodi (non verificato sulle fonti allegate per il nome moderno).

### N13. Machin e Pemberton

Le fonti allegate dicono soltanto che J. Machin era professore di astronomia a Gresham e Henry Pemberton dottore in medicina, che trovarono il metodo separatamente e che lo scritto di Machin giunse prima a Newton. Da conoscenza generale: John Machin (1686 circa – 1751) fu professore di astronomia al Gresham College di Londra ed è noto anche per una formula per il calcolo di π; Henry Pemberton (1694–1771) curò per Newton la terza edizione dei *Principia*, quella del 1726 tradotta qui (non verificato sulle fonti allegate). La «menzione altrove» del metodo non è identificabile sulle fonti allegate.

### N14. Perché il fascicolo non contiene l’inclinazione

L’indicazione di lavoro chiedeva di ricontrollare anche l’inclinazione dell’orbita lunare. Le proposizioni sull’inclinazione (Prop. XXXIV, variazione oraria dell’inclinazione, e seguenti) sono nel file `latino-1726-L3-P34-40.md` e appartengono al Fascicolo 25a. Nel perimetro di questo fascicolo l’inclinazione compare solo in due frasi qualitative (III.G5.51 e III.G5.53), che non contengono numeri da verificare.

---

## Controllo della copertura

Pagine 1726 dai marcatori ‹n› della trascrizione. Motte: estratto senza marcatori di pagina, «sezione corrispondente».

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| III.G5.37–III.G5.40 | *Invenire motum horarium nodorum lunæ in orbe circulari* … *Designet S solem* | Prop. XXX: enunciato, costruzione, regola dei tre seni, valori | pp. 437–440 | Prop. XXX |
| III.G5.41 | *Hinc si a dati arcus quam minimi PM* | Prop. XXX, Cor. 1 | p. 440 | Cor. 1 |
| III.G5.42 | *In data quavis Nodorum positione* | Prop. XXX, Cor. 2 | p. 441 | Cor. 2 |
| III.G5.43–III.G5.45 | *Invenire motum horarium … in orbe elliptico* … *Designet Qpmaq* … *Nam si PF tangat* | Prop. XXXI: enunciato, costruzione, dimostrazione | pp. 442–444 | Prop. XXXI |
| III.G5.46–III.G5.48 | *Quare cum, in data nodorum positione* … *Cæterum luna* … *Si nodi versantur extra quadraturas* | Prop. XXXI, Cor. e correzione del moto orario | pp. 444–446 | Cor. |
| III.G5.49–III.G5.51 | *Invenire motum medium nodorum lunæ* … *Motus medius annuus* … *Hæc ita se habent* | Prop. XXXII | pp. 447–449 | Prop. XXXII |
| III.G5.52–III.G5.53 | *Invenire motum verum nodorum lunæ* … *In tempore quod est* | Prop. XXXIII | pp. 450–451 | Prop. XXXIII |
| III.G5.54 | *Ex hac & præcedente propositione* | Prop. XXXIII, Cor. | p. 451 | Cor. |
| III.G5.55 | *Alia ratione motum nodorum* | Scolio di Newton | p. 451 | Scholium |
| (titolo) | *De Motu Nodorum Lunæ.* | titolo dello scritto di Machin | p. 451 | Of the motion of the moon’s nodes |
| III.G5.56–III.G5.58 | *Motus solis medius a nodo* … *Sit T locus* … *Describatur enim* | Machin, Prop. I | pp. 451–453 | Proposition I |
| III.G5.59–III.G5.60 | *Dato motu medio nodorum* … *Sit angulus A* | Machin, Prop. II | pp. 453–454 | Proposition II |
| III.G5.61 | *Hinc angulus FTA* | Machin, Prop. II, Cor. | p. 454 | Cor. |
| III.G5.62–III.G5.63 | *Si motus nodorum mediocris horarius* … *At si motus medius* | Machin, Scolio | p. 454 | Scholium |

**Controlli eseguiti.**

1. **Copertura frase per frase.** Ho riletto in sequenza ogni periodo della trascrizione, da *PROPOSITIO XXX.* (riga 104) a *1°. 29′. 57″.* (riga 188), contro la traduzione: nessuna frase manca. Per le parti dimostrative la traduzione è costruita frase per frase dalle stesse unità della Parte B (124 passi), e il testo italiano dei capoversi è l’unione dei passi: la corrispondenza è quindi verificata automaticamente. Le frasi fuori dalla Parte B (Cor. della Prop. XXXIII, Scolio di Newton, titolo di Machin) sono state controllate a mano. I 27 identificatori (III.G5.37–III.G5.63) sono consecutivi e unici (controllo automatico).
2. **Parte B.** `check.py` sul file finale, con i file latino e Motte interi: JSON valido; tutte le stringhe `la` (enunciati e passi) sono sottostringhe esatte della trascrizione; tutte le stringhe `en` sono sottostringhe esatte di Motte; ogni identificatore di `copertura` è presente nel testo. Esito: «OK», senza avvisi.
3. **Matematica e numeri** (`verifica.py`): tutte le catene numeriche delle Propp. XXX–XXXIII e dello Scolio di Machin (note N3, N5, N7, N8, N9, N12); quadratura della figura NeFn (793 : 60); soluzione in forma chiusa e integrazione numerica del moto relativo Sole–nodo; costruzione della Prop. XXXIII; Prop. II e Cor. di Machin. **Cifre che non tornano** (segnalate, non corrette): 9° 11′ 3″ (Prop. XXXIII; torna con il moto delle tavole), 16″ 19‴ 26ⁱᵛ (Cor. della Prop. XXXIII; torna con lo stesso rapporto), 23⅔‴ di Machin (il calcolo dà 23½‴), 58‴ di Machin (56‴ con 365 g 6 h 9 m). Gli arrotondamenti dell’ultima cifra sessagesimale (per esempio 9,0827646) sono spiegati nelle note.
4. **Tabelle numeriche:** il perimetro non ne contiene.
5. **Motte.** Confronto di tutta la sezione corrispondente (righe 643–1247 dell’estratto); divergenze nel § A.8; 14 SVG controllati, nessuno che non torni.
6. **Separazione fra testo e commento.** Il testo tradotto non contiene formule moderne.

**Non ho potuto verificare:**

- **la stampa del 1726**: gli undici punti del § A.7 restano «probabili» o «da controllare»;
- **le figure originali**: le ricostruzioni di N2, N7, N9 e N11 vengono dalle sole lettere del testo (in particolare l’ordine D, C, B, A nella Prop. XXXIII e la posizione di B e β nella figura di Machin);
- **la paginazione di Motte**: l’estratto non ha marcatori di pagina;
- **la «menzione altrove»** del metodo di Machin e Pemberton (Scolio);
- l’origine delle cifre 9° 11′ 3″ e 16″ 19‴ 26ⁱᵛ: le ricostruzioni di N9 sono mie;
- i **valori moderni** e le notizie biografiche di N3, N8, N10, N12 e N13, che vengono da conoscenza generale.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Libro III, Propp. XXX–XXXIII, Scolio, Machin Propp. I–II e Scolio | **Fascicolo 24b, presente documento, prima versione** |
| Identificatori III.G5.37–III.G5.63 | Provvisori: da rinumerare in continuità con il Fascicolo 24a |
| *motus mediocris* «moto mediocre» (A.0) | Da armonizzare con il Fascicolo 24a (*in mediocri sua quantitate*, Prop. XXV) e da decidere |
| Refusi e punti dubbi (§ A.7) | Da verificare sulla stampa del 1726 (scansione ECCO) |
| Cifre 9° 11′ 3″, 16″ 19‴ 26ⁱᵛ, 23⅔‴ | Segnalate (N9, N12); da confrontare con la stampa |
| Pagine interattive | Parte B: 11 unità. Candidate migliori: Prop. XXX (regola dei tre seni, con la figura in 3D), Prop. XXXII (curva NeFn con il confronto numerico 793 : 60), Prop. XXXIII con Machin, Prop. II (confronto fra costruzione approssimata e soluzione esatta) |
| Figure NATP00303 delle Propp. XXX–XXXIII e di Machin | Da consultare per confermare le ricostruzioni di `figura_base` |
| Revisione filologica e scientifica indipendente | Da eseguire |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce traduzioni italiane o inglesi moderne. **Licenza prevista** (decisione del curatore, Fascicolo 3): testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project; i testi di Motte sono di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Unità incluse (11): **Prop. XXX** con i **Cor. 1** e **2** (dimostrazioni proprie con figura); **Prop. XXXI** e il suo **Cor.** con la correzione del moto orario (calcolo); **Prop. XXXII** (figura e calcolo del moto medio annuo); **Prop. XXXIII** (costruzione dell’equazione); **Machin, Prop. I** e **Prop. II**, il **Cor.** della II e lo **Scolio** numerico di Machin. **Escluse**: il Cor. della Prop. XXXIII (risultati senza dimostrazione) e lo Scolio di Newton (testo storico, senza dimostrazione).

Convenzioni:

- `la`: testo latino esatto della trascrizione, refusi e caratteri invisibili (U+2062, U+2064) compresi;
- `it`: la traduzione di questo fascicolo (i capoversi della traduzione sono l’unione dei passi);
- `en`: Motte 1846, allineato per senso, con i marcatori `[SVG n]`;
- `dipende_da`: soltanto i rimandi citati nella frase latina, compresi quelli espliciti ma senza numero («per ea quæ in præcedente propositione» → "Prop. XXX"; «per jam ostensa» → "Prop. XXXI"; «in fig. præced.» → "Prop. XXXII");
- `figura.mostra`: elementi da rendere visibili, cumulativi; `figura.evidenzia`: relazioni da mettere in risalto;
- `dati`: valori numerici e risultati dei controlli, dove utili.

```json
{
 "fascicolo": "24b-L3-P30-33",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase latina (compresi i rimandi impliciti dichiarati: «per ea quæ in præcedente propositione», «per jam ostensa», «in fig. præced.»)",
  "en": "Motte 1846, allineato per senso; i marcatori [SVG n] sono conservati",
  "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione",
  "la": "",
  "identificatori": "III.G5.37–III.G5.63 (parte «b», rinumerati in continuità con il 24a)"
 },
 "unita": [
  {
   "id": "L3-P30",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXX — moto orario dei nodi della Luna nell'orbita circolare",
   "copertura": [
    "III.G5.37",
    "III.G5.38",
    "III.G5.39",
    "III.G5.40"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Book III, Prop. XXX)"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare il moto orario dei nodi della Luna in un’orbita circolare.",
    "en": "To find the horary motion of the nodes of the moon in a circular orbit."
   },
   "figura_base": {
    "punti": [
     "S",
     "T",
     "P",
     "N",
     "n",
     "m",
     "l",
     "p",
     "I",
     "K",
     "A",
     "B",
     "Z",
     "Q",
     "q",
     "M",
     "L",
     "H"
    ],
    "vincoli": [
     "T centro dell’orbita circolare NPn; Npn traccia dell’orbita sul piano dell’eclittica",
     "N, n nodi; nTNm linea dei nodi; S Sole, ST nel piano dell’eclittica",
     "PI ⟂ ST, PK ⟂ Qq (quindi IT = PK); Pp ⟂ piano dell’eclittica",
     "A, B sizigie e Q, q quadrature nel piano dell’eclittica; AZ ⟂ Nn",
     "PM arco piccolissimo; ML ∥ ST (forza 3IT); PL e PM prolungate incontrano l’eclittica in l e m; PH ⟂ Tm"
    ]
   },
   "passi": [
    {
     "id": "L3-P30-p1",
     "la": "",
     "it": "Rappresentino S il Sole, T la Terra, P la Luna, NPn l’orbita della Luna, Npn la traccia dell’orbita sul piano dell’eclittica; N, n i nodi, nTNm la linea dei nodi prolungata all’infinito; PI, PK le perpendicolari abbassate sulle linee ST, Qq; Pp la perpendicolare abbassata sul piano dell’eclittica; A, B le sizigie della Luna nel piano dell’eclittica; AZ la perpendicolare sulla linea dei nodi Nn; Q, q le quadrature della Luna nel piano dell’eclittica, e pK la perpendicolare sulla linea Qq che sta fra le quadrature.",
     "en": "Let S represent the sun, T the earth, P the moon, NPn the orbit of the moon, Npn the orthographic projection of the orbit upon the plane of the ecliptic; N, n the nodes, nTNm the line of the nodes produced indefinitely; PI, PK perpendiculars upon the lines ST, Qq; Pp a perpendicular upon the plane of the ecliptic; A, B the moon's syzygies in the plane of the ecliptic; AZ a perpendicular let fall upon Nn, the line of the nodes; Q, q the quadratures of the moon in the plane of the ecliptic, and pK a perpendicular on the line Qq lying between the quadratures.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "S",
       "T",
       "orbita NPn",
       "traccia Npn sull’eclittica",
       "nodi N, n",
       "linea dei nodi nTNm",
       "PI",
       "PK",
       "Pp",
       "sizigie A, B",
       "AZ",
       "quadrature Q, q",
       "pK"
      ]
     },
     "nota": "La trascrizione ha due volte «plano elipticæ» (refuso probabile per «eclipticæ»). Motte rende vestigium con «orthographic projection»."
    },
    {
     "id": "L3-P30-p2",
     "la": "",
     "it": "La forza del Sole che perturba il moto della Luna (per la Prop. XXV) è duplice: l’una proporzionale alla linea LM nello schema di quella proposizione, l’altra alla linea MT.",
     "en": "The force of the sun to disturb the motion of the moon (by Prop. XXV) is twofold, one proportional to the line LM, the other to the line MT, in the scheme of that Proposition;",
     "dipende_da": [
      "Prop. XXV"
     ],
     "figura": {
      "mostra": [
       "forze LM e MT (schema della Prop. XXV)"
      ]
     },
     "nota": "«linæ»: refuso probabile per «lineæ»."
    },
    {
     "id": "L3-P30-p3",
     "la": "",
     "it": "E la Luna è tirata dalla prima forza verso la Terra, dalla seconda verso il Sole, lungo una linea parallela alla retta ST condotta dalla Terra al Sole.",
     "en": "and the moon by the former force is drawn towards the earth, by the latter towards the sun, in a direction parallel to the right line ST joining the earth and the sun.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "direzione di LM (verso T)",
       "direzione di MT ∥ ST"
      ]
     }
    },
    {
     "id": "L3-P30-p4",
     "la": "",
     "it": "La prima forza, LM, agisce secondo il piano dell’orbita lunare, e perciò non muta affatto la posizione del piano.",
     "en": "The former force LM acts in the direction of the plane of the moon's orbit, and therefore makes no change upon the situation thereof,",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "LM nel piano dell’orbita"
      ]
     }
    },
    {
     "id": "L3-P30-p5",
     "la": "",
     "it": "Questa va dunque trascurata.",
     "en": "and is upon that account to be neglected;",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P30-p6",
     "la": "",
     "it": "La seconda forza, MT, dalla quale il piano dell’orbita lunare è perturbato, è la stessa della forza 3PK o 3IT.",
     "en": "the latter force MT, by which the plane of the moon's orbit is disturbed, is the same with the force 3PK or 3IT.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "MT = 3IT = 3PK"
      ],
      "evidenzia": [
       "IT = PK"
      ]
     }
    },
    {
     "id": "L3-P30-p7",
     "la": "",
     "it": "E questa forza (per la Prop. XXV) sta alla forza con cui la Luna, nel suo tempo periodico, potrebbe ruotare uniformemente in un cerchio attorno alla Terra in quiete, come 3IT sta al raggio del cerchio moltiplicato per il numero 178,725, ossia come IT sta al raggio moltiplicato per 59,575.",
     "en": "And this force (by Prop. XXV) is to the force by which the moon may, in its periodic time, be uniformly revolved in a circle about the earth at rest, as 3IT to the radius of the circle multiplied by the number 178,725, or as IT to the radius thereof multiplied by 59,575.",
     "dipende_da": [
      "Prop. XXV"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "3IT : (TP × 178,725) = IT : (TP × 59,575)"
      ]
     },
     "nota": "178,725/3 = 59,575 (verificato)."
    },
    {
     "id": "L3-P30-p8",
     "la": "",
     "it": "Del resto, in questo calcolo e in tutto quello che segue, considero tutte le linee condotte dalla Luna al Sole come parallele alla linea che si conduce dalla Terra al Sole, perché l’inclinazione diminuisce in alcuni casi tutti gli effetti quasi quanto li aumenta in altri; e cerchiamo i moti mediocri dei nodi, trascurando minuzie di questo genere, che renderebbero il calcolo troppo complicato.",
     "en": "But in this calculus, and all that follows, I consider all the lines drawn from the moon to the sun as parallel to the line which joins the earth and the sun; because what inclination there is almost as much diminishes all effects in some cases as it augments them in others; and we are now inquiring after the mean motions of the nodes, neglecting such niceties as are of no moment, and would only serve to render the calculus more perplexed.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "linee dalla Luna al Sole ∥ TS"
      ]
     },
     "nota": "Motte amplia: «such niceties as are of no moment»."
    },
    {
     "id": "L3-P30-p9",
     "la": "",
     "it": "Rappresenti ora PM l’arco che la Luna descrive in un tempo dato piccolissimo, e ML la piccola linea di cui la Luna, per la spinta della detta forza 3IT, potrebbe descrivere la metà nello stesso tempo.",
     "en": "Now suppose PM to represent an arc which the moon describes in the least moment of time, and ML a little line, the half of which the moon, by the impulse of the said force 3IT, would describe in the same time;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "arco PM",
       "piccola linea ML ∥ ST"
      ]
     }
    },
    {
     "id": "L3-P30-p10",
     "la": "",
     "it": "Si congiungano PL, MP, e si prolunghino fino a m e l, dove tagliano il piano dell’eclittica; e su Tm si abbassi la perpendicolare PH.",
     "en": "and joining PL, MP, let them be produced to m and l, where they cut the plane of the ecliptic, and upon Tm let fall the perpendicular PH.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "PL prolungata fino a l",
       "PM prolungata fino a m",
       "PH ⟂ Tm"
      ]
     }
    },
    {
     "id": "L3-P30-p11",
     "la": "",
     "it": "E poiché la retta ML è parallela al piano dell’eclittica, e perciò non può incontrare la retta ml che giace in quel piano, e tuttavia queste rette giacciono in un piano comune LMPml, queste rette saranno parallele, e perciò i triangoli LMP, lmP saranno simili.",
     "en": "Now, since the right line ML is parallel to the plane of the ecliptic, and therefore can never meet with the right line ml which lies in that plane, and yet both those right lines lie in one common plane LMPml, they will be parallel, and upon that account the triangles LMP, lmP will be similar.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "ml",
       "piano LMPml"
      ],
      "evidenzia": [
       "ML ∥ ml",
       "triangoli simili LMP, lmP"
      ]
     }
    },
    {
     "id": "L3-P30-p12",
     "la": "",
     "it": "Ora, poiché MPm è nel piano dell’orbita in cui la Luna si muoveva nel luogo P, il punto m cadrà sulla linea Nn condotta per i nodi N, n di quell’orbita.",
     "en": "And seeing MPm lies in the plane of the orbit, in which the moon did move while in the place P, the point m will fall upon the line Nn, which passes through the nodes N, n, of that orbit.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "m sulla linea dei nodi"
      ]
     }
    },
    {
     "id": "L3-P30-p13",
     "la": "",
     "it": "E poiché la forza da cui è generata la metà della piccola linea LM, se fosse stata impressa tutta insieme e in una volta nel luogo P, genererebbe quella linea intera, e farebbe sì che la Luna si muovesse in un arco la cui corda fosse LP, e perciò trasferirebbe la Luna dal piano MPmT al piano LPlT, il moto angolare dei nodi generato da quella forza sarà uguale all’angolo mTl.",
     "en": "And because the force by which the half of the little line LM is generated, if the whole had been together, and it once impressed in the point P, would have generated that whole line, and caused the moon to move in the arc whose chord is LP; that is to say, would have transferred the moon from the plane MPmT into the plane LPlT; therefore the angular motion of the nodes generated by that force will be equal to the angle mTl.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "piano MPmT",
       "piano LPlT",
       "angolo mTl"
      ],
      "evidenzia": [
       "mTl = moto dei nodi"
      ]
     },
     "nota": "Motte rende simul & semel con una frase sintatticamente guasta («if the whole had been together, and it once impressed»)."
    },
    {
     "id": "L3-P30-p14",
     "la": "",
     "it": "Ma ml sta a mP come ML sta a MP; e perciò, poiché MP è dato, essendo dato il tempo, ml è come il rettangolo ML×mP, cioè come il rettangolo IT×mP.",
     "en": "But ml is to mP as ML to MP; and since MP, because of the time given, is also given, ml will be as the rectangle ML × mP, that is, as the rectangle IT × mP.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "ml ∝ IT×mP"
      ]
     }
    },
    {
     "id": "L3-P30-p15",
     "la": "",
     "it": "E l’angolo mTl, purché l’angolo Tml sia retto, è come ml/Tm, e perciò come IT×Pm/Tm, cioè (essendo proporzionali Tm e mP, TP e PH) come IT×PH/TP, e perciò, essendo data TP, come IT×PH.",
     "en": "And if Tml is a right angle, the angle mTl will be as [SVG 1042] , and therefore as [SVG 1043] , that is (because Tm and mP, TP and PH are proportional), as [SVG 1044] ; and, therefore, because TP is given, as IT × PH.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangoli TmP e PH"
      ],
      "evidenzia": [
       "mTl ∝ IT×PH"
      ]
     },
     "nota": "Trascrizione: «mlTm», «IT×PmTm», «IT×PHTP» = ml/Tm, IT×Pm/Tm, IT×PH/TP (Motte SVG 1042–1044, concordi)."
    },
    {
     "id": "L3-P30-p16",
     "la": "",
     "it": "Se poi l’angolo Tml, ossia STN, è obliquo, l’angolo mTl sarà ancora minore, nel rapporto del seno dell’angolo STN al raggio, ossia di AZ ad AT.",
     "en": "But if the angle Tml or STN is oblique, the angle mTl will be yet less, in proportion of the sine of the angle STN to the radius, or AZ to AT.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "angolo STN",
       "AZ, AT"
      ],
      "evidenzia": [
       "fattore AZ/AT"
      ]
     }
    },
    {
     "id": "L3-P30-p17",
     "la": "",
     "it": "La velocità dei nodi è dunque come IT×PH×AZ, ossia come il prodotto dei seni dei tre angoli TPI, PTN e STN.",
     "en": "And therefore the velocity of the nodes is as IT × PH × AZ, or as the solid content of the sines of the three angles TPI, PTN, and STN.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "velocità dei nodi ∝ IT×PH×AZ"
      ]
     }
    },
    {
     "id": "L3-P30-p18",
     "la": "",
     "it": "Se quegli angoli, trovandosi i nodi nelle quadrature e la Luna in sizigia, sono retti, la piccola linea ml se ne andrà all’infinito, e l’angolo mTl diventerà uguale all’angolo mPl.",
     "en": "If these are right angles, as happens when the nodes are in the quadratures, and the moon in the syzygy, the little line ml will be removed to an infinite distance, and the angle mTl will become equal to the angle mPl.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "nodi in quadratura, Luna in sizigia"
      ],
      "evidenzia": [
       "mTl = mPl"
      ]
     }
    },
    {
     "id": "L3-P30-p19",
     "la": "",
     "it": "In questo caso, però, l’angolo mPl sta all’angolo PTM, che la Luna descrive nello stesso tempo con il suo moto apparente attorno alla Terra, come 1 sta a 59,575.",
     "en": "But in this case the angle mPl is to the angle PTM, which the moon in the same time by its apparent motion describes about the earth, as 1 to 59,575.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "angolo PTM"
      ],
      "evidenzia": [
       "mPl : PTM = 1 : 59,575"
      ]
     }
    },
    {
     "id": "L3-P30-p20",
     "la": "",
     "it": "Infatti l’angolo mPl è uguale all’angolo LPM, cioè all’angolo di deviazione della Luna dal cammino rettilineo che la sola detta forza solare 3IT, se allora cessasse la gravità della Luna, potrebbe generare in quel tempo dato; e l’angolo PTM è uguale all’angolo di deviazione della Luna dal cammino rettilineo che la forza da cui la Luna è trattenuta nella sua orbita, se allora cessasse la forza solare 3IT, genererebbe nello stesso tempo.",
     "en": "For the angle mPl is equal to the angle LPM, that is, to the angle of the moon's deflexion from a rectilinear path; which angle, if the gravity of the moon should have then ceased, the said force of the sun 3IT would by itself have generated in that given time; and the angle PTM is equal to the angle of the moon's deflexion from a rectilinear path; which angle, if the force of the sun 3IT should have then ceased, the force alone by which the moon is retained in its orbit would have generated in the same time.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "angolo LPM"
      ]
     }
    },
    {
     "id": "L3-P30-p21",
     "la": "",
     "it": "E queste forze, come abbiamo detto sopra, stanno fra loro come 1 sta a 59,575.",
     "en": "And these forces (as we have above shewn) are the one to the other as 1 to 59,575.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Rimanda al passo p7 di questa proposizione."
    },
    {
     "id": "L3-P30-p22",
     "la": "",
     "it": "Dunque, poiché il moto medio orario della Luna rispetto alle stelle fisse è 32′ 56″ 27‴ 12½ⁱᵛ, il moto orario del nodo in questo caso sarà 33″ 10‴ 33ⁱᵛ 12ᵛ.",
     "en": "Since, therefore, the mean horary motion of the moon (in respect of the fixed stars) is 32' 56'' 27''' [SVG 1045] . the horary motion of the node in this case will be 33'' 10''' 33iv. 12v.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Trascrizione «12iv⁤12» = 12½ⁱᵛ (Motte SVG 1045: 12½ⁱᵛ). Verificato: 32′ 56″ 27‴ 12½ⁱᵛ / 59,575 = 33″ 10‴ 33ⁱᵛ 12ᵛ (nota N3)."
    },
    {
     "id": "L3-P30-p23",
     "la": "",
     "it": "Negli altri casi, invece, questo moto orario starà a 33″ 10‴ 33ⁱᵛ 12ᵛ come il prodotto dei seni dei tre angoli TPI, PTN e STN (ossia delle distanze della Luna dalla quadratura, della Luna dal nodo e del nodo dal Sole) sta al cubo del raggio.",
     "en": "But in other cases the horary motion will be to 33'' 10''' 33iv. 12v. as the solid content of the sines of the three angles TPI, PTN, and STN (or of the distances of the moon from the quadrature, of the moon from the node, and of the node from the sun) to the cube of the radius.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "moto orario = 33″10‴33ⁱᵛ12ᵛ × sin·sin·sin"
      ]
     }
    },
    {
     "id": "L3-P30-p24",
     "la": "",
     "it": "E ogni volta che il segno di uno qualsiasi di questi angoli cambia da positivo a negativo, e da negativo a positivo, il moto regressivo dovrà mutarsi in progressivo e il progressivo in regressivo.",
     "en": "And as often as the sine of any angle is changed from positive to negative, and from negative to positive, so often must the regressive be changed into a progressive, and the progressive into a regressive motion.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Latino «signum anguli», Motte «the sine of any angle»: vedi apparato A.2."
    },
    {
     "id": "L3-P30-p25",
     "la": "",
     "it": "Ne segue che i nodi progrediscono ogni volta che la Luna si trova fra l’una o l’altra quadratura e il nodo più vicino a quella quadratura.",
     "en": "Whence it comes to pass that the nodes are progressive as often as the moon happens to be placed between either quadrature, and the node nearest to that quadrature.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "archi fra quadratura e nodo più vicino"
      ]
     }
    },
    {
     "id": "L3-P30-p26",
     "la": "",
     "it": "Negli altri casi regrediscono e, per l’eccesso del regresso sul progresso, sono portati ogni mese in antecedenza.",
     "en": "In other cases they are regressive, and by the excess of the regress above the progress, they are monthly transferred in antecedentia.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    }
   ]
  },
  {
   "id": "L3-P30-Cor1",
   "tipo": "Corollarium",
   "titolo": "Prop. XXX, Cor. 1 — il moto orario come area MPDd per AZ²",
   "copertura": [
    "III.G5.41"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XXX, Cor. 1)"
   },
   "enunciato": {
    "la": "",
    "it": "Di qui, se dagli estremi P e M di un arco dato piccolissimo PM si abbassano sulla linea Qq che congiunge le quadrature le perpendicolari PK, Mk, e queste si prolungano finché tagliano la linea dei nodi Nn in D e d, il moto orario dei nodi sarà come l’area MPDd e il quadrato della linea AZ considerati congiuntamente.",
    "en": "Hence if from P and M, the extreme points of a least arc PM, on the line Qq joining the quadratures we let fall the perpendiculars PK Mk, and produce the same till they cut the line of the nodes Nn in D and d, the horary motion of the nodes will be as the area MPDd, and the square of the line AZ conjunctly."
   },
   "figura_base": {
    "punti": [
     "P",
     "M",
     "K",
     "k",
     "D",
     "d",
     "T",
     "A",
     "Z",
     "H",
     "Q",
     "q",
     "N",
     "n"
    ],
    "vincoli": [
     "PK, Mk ⟂ Qq, prolungate fino a Nn in D, d"
    ]
   },
   "passi": [
    {
     "id": "L3-P30-Cor1-p1",
     "la": "",
     "it": "Siano infatti PK, PH e AZ i tre seni predetti.",
     "en": "For let PK, PH, and AZ, be the three said sines,",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "PK",
       "PH",
       "AZ"
      ]
     }
    },
    {
     "id": "L3-P30-Cor1-p2",
     "la": "",
     "it": "Cioè PK il seno della distanza della Luna dalla quadratura, PH il seno della distanza della Luna dal nodo e AZ il seno della distanza del nodo dal Sole: e la velocità del nodo sarà come il prodotto PK×PH×AZ.",
     "en": "viz., PK the sine of the distance of the moon from the quadrature, PH the sine of the distance of the moon from the node, and AZ the sine of the distance of the node from the sun; and the velocity of the node will be as the solid content of PK × PH × AZ.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "velocità ∝ PK×PH×AZ"
      ]
     }
    },
    {
     "id": "L3-P30-Cor1-p3",
     "la": "",
     "it": "Ma PT sta a PK come PM sta a Kk, e perciò, essendo date PT e PM, Kk è proporzionale a PK.",
     "en": "But PT is to PK as PM to Kk; and, therefore, because PT and PM are given, Kk will be as PK.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Kk"
      ],
      "evidenzia": [
       "Kk ∝ PK"
      ]
     }
    },
    {
     "id": "L3-P30-Cor1-p4",
     "la": "",
     "it": "E AT sta a PD come AZ sta a PH, e perciò PH è proporzionale al rettangolo PD×AZ; e, composti i rapporti, PK×PH è come il prodotto Kk×PD×AZ, e PK×PH×AZ come Kk×PD×AZ², cioè come l’area PDdM e AZ² considerate congiuntamente. C.V.D.",
     "en": "Likewise AT is to PD as AZ to PH, and therefore PH is as the rectangle PD × AZ; and, by compounding those proportions, PK × PH is as the solid content Kk × PD × AZ, and PK × PH × AZ as Kk × PD × AZ2; that is, as the area PDdM and AZ2 conjunctly. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "PD",
       "area PDdM"
      ],
      "evidenzia": [
       "PK×PH×AZ ∝ area PDdM × AZ²"
      ]
     }
    }
   ]
  },
  {
   "id": "L3-P30-Cor2",
   "tipo": "Corollarium",
   "titolo": "Prop. XXX, Cor. 2 — il moto orario mediocre è la metà di quello in sizigia",
   "copertura": [
    "III.G5.42"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XXX, Cor. 2)"
   },
   "enunciato": {
    "la": "",
    "it": "In una posizione data qualsiasi dei nodi, il moto orario mediocre è la metà del moto orario nelle sizigie della Luna, e perciò sta a 16″ 35‴ 16ⁱᵛ 36ᵛ come il quadrato del seno della distanza dei nodi dalle sizigie sta al quadrato del raggio, ossia come AZ² sta ad AT².",
    "en": "In any given position of the nodes their mean horary motion is half their horary motion in the moon's syzygies; and therefore is to 16'' 35''' 16iv. 36v. as the square of the sine of the distance of the nodes from the syzygies to the square of the radius, or as AZ2 to AT2."
   },
   "figura_base": {
    "punti": [
     "Q",
     "A",
     "q",
     "n",
     "N",
     "E",
     "e",
     "M",
     "d",
     "P",
     "D",
     "T"
    ],
    "vincoli": [
     "QE, qe tangenti al cerchio in Q, q; D sulla linea dei nodi"
    ]
   },
   "passi": [
    {
     "id": "L3-P30-Cor2-p1",
     "la": "",
     "it": "Infatti, se la Luna percorre con moto uniforme il semicerchio QAq, la somma di tutte le aree PDdM, nel tempo in cui la Luna va da Q a M, sarà l’area QMdE, che termina alla tangente QE del cerchio; e nel tempo in cui la Luna raggiunge il punto n, quella somma sarà l’intera area EQAn che la linea PD descrive; poi, mentre la Luna procede da n a q, la linea PD cadrà fuori del cerchio e descriverà l’area nqe, che termina alla tangente qe del cerchio; quest’area, poiché prima i nodi regredivano e ora invece progrediscono, deve essere sottratta dall’area precedente e, essendo uguale all’area QEN, lascerà il semicerchio NQAn.",
     "en": "For if the moon, by an uniform motion, describes the semi-circle QAq, the sum of all the areas PDdM, during the time of the moon's passage from Q to M, will make up the area QMdE, terminating at the tangent QE of the circle; and by the time that the moon has arrived at the point n, that sum will make up the whole area EQAn described by the line PD: but when the moon proceeds from n to q, the line PD will fall without the circle, and describe the area nqe, terminating at the tangent qe of the circle, which area, because the nodes were before regressive, but are now progressive, must be subducted from the former area, and, being itself equal to the area QEN, will leave the semi-circle NQAn.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "tangenti QE, qe",
       "area QMdE",
       "area EQAn",
       "area nqe"
      ],
      "evidenzia": [
       "EQAn − nqe = semicerchio NQAn"
      ]
     }
    },
    {
     "id": "L3-P30-Cor2-p2",
     "la": "",
     "it": "Dunque la somma di tutte le aree PDdM, nel tempo in cui la Luna descrive un semicerchio, è l’area del semicerchio; e la somma di tutte, nel tempo in cui la Luna descrive un cerchio, è l’area del cerchio intero.",
     "en": "While, therefore, the moon describes a semi-circle, the sum of all the areas PDdM will be the area of that semi-circle; and while the moon describes a complete circle, the sum of those areas will be the area of the whole circle.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P30-Cor2-p3",
     "la": "",
     "it": "Ma l’area PDdM, quando la Luna si trova nelle sizigie, è il rettangolo formato dall’arco PM e dal raggio PT; e la somma di tutte le aree uguali a questa, nel tempo in cui la Luna descrive un cerchio, è il rettangolo formato dalla circonferenza intera e dal raggio del cerchio; e questo rettangolo, essendo uguale a due cerchi, è doppio del rettangolo precedente.",
     "en": "But the area PDdM, when the moon is in the syzygies, is the rectangle of the arc PM into the radius PT; and the sum of all the areas, every one equal to this area, in the time that the moon describes a complete circle, is the rectangle of the whole circumference into the radius of the circle; and this rectangle, being double the area of the circle, will be double the quantity of the former sum.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "circonferenza × raggio = 2 × area del cerchio"
      ]
     },
     "nota": "«rectangulum prius»: il termine di confronto è la somma precedente (l’area del cerchio), come intende Motte («the former sum»); vedi apparato A.3."
    },
    {
     "id": "L3-P30-Cor2-p4",
     "la": "",
     "it": "Perciò i nodi, con la velocità che hanno nelle sizigie lunari continuata uniformemente, descriverebbero uno spazio doppio di quello che descrivono realmente; e perciò il moto mediocre con cui, se fosse continuato uniformemente, potrebbero descrivere lo spazio che percorrono realmente con un moto non uniforme, è la metà del moto che hanno nelle sizigie della Luna.",
     "en": "If, therefore, the nodes went on with that velocity uniformly continued which they acquire in the moon's syzygies, they would describe a space double of that which they describe in fact; and, therefore, the mean motion, by which, if uniformly continued, they would describe the same space with that which they do in fact describe by an unequal motion, is but one-half of that motion which they are possessed of in the moon's syzygies.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P30-Cor2-p5",
     "la": "",
     "it": "Quindi, poiché il moto orario massimo, se i nodi si trovano nelle quadrature, è 33″ 10‴ 33ⁱᵛ 12ᵛ, il moto orario mediocre in questo caso sarà 16″ 35‴ 16ⁱᵛ 36ᵛ.",
     "en": "Wherefore since their greatest horary motion, if the nodes are in the quadratures, is 33'' 10''' 33iv. 12v. their mean horary motion in this case will be 16'' 35''' 16iv. 36v.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Verificato: metà esatta."
    },
    {
     "id": "L3-P30-Cor2-p6",
     "la": "",
     "it": "E poiché il moto orario dei nodi è sempre come AZ² e l’area PDdM considerate congiuntamente, e perciò il moto orario dei nodi nelle sizigie della Luna è come AZ² e l’area PDdM considerate congiuntamente, cioè (essendo data l’area PDdM descritta nelle sizigie) come AZ², anche il moto mediocre sarà come AZ²; e perciò questo moto, quando i nodi si trovano fuori delle quadrature, starà a 16″ 35‴ 16ⁱᵛ 36ᵛ come AZ² sta ad AT². C.V.D.",
     "en": "And seeing the horary motion of the nodes is every where as AZ2 and the area PDdM conjunctly, and, therefore, in the moon's syzygies, the horary motion of the nodes is as AZ2 and the area PDdM conjunctly, that is (because the area PDdM described in the syzygies is given), as AZ2, therefore the mean motion also will be as AZ2; and, therefore, when the nodes are without the quadratures, this motion will be to 16'' 35''' 16iv. 36v. as AZ2 to AT2. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    }
   ]
  },
  {
   "id": "L3-P31",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXXI — moto orario dei nodi nell’orbita ellittica",
   "copertura": [
    "III.G5.43",
    "III.G5.44",
    "III.G5.45"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XXXI)"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare il moto orario dei nodi della Luna in un’orbita ellittica.",
    "en": "To find the horary motion of the nodes of the moon in an elliptic orbit."
   },
   "figura_base": {
    "punti": [
     "Q",
     "p",
     "m",
     "a",
     "q",
     "b",
     "A",
     "B",
     "T",
     "S",
     "P",
     "M",
     "N",
     "n",
     "K",
     "k",
     "D",
     "d",
     "F",
     "f",
     "Y",
     "L",
     "l",
     "G",
     "g",
     "c",
     "e",
     "R",
     "r",
     "h"
    ],
    "vincoli": [
     "ellisse Qpmaq con asse maggiore Qq e minore ab; cerchio circoscritto QAqB; T centro comune",
     "pK, mk ⟂ Qq, prolungate fino al cerchio in P, M e alla linea dei nodi in D, d",
     "PF tangente al cerchio in P, pf tangente all’ellisse in p; F, f su TN; le tangenti si incontrano in Y su TQ",
     "LP, lp prolungate incontrano l’eclittica in G, g; FG taglia pf, pg, TQ in c, e, R; fg taglia TQ in r; ph ∥ TN incontra FP in h"
    ]
   },
   "passi": [
    {
     "id": "L3-P31-p1",
     "la": "",
     "it": "Rappresentino Qpmaq un’ellisse descritta con l’asse maggiore Qq e il minore ab, QAqB il cerchio circoscritto, T la Terra nel centro comune di entrambi, S il Sole, p la Luna che si muove sull’ellisse e pm l’arco che essa descrive in una particella di tempo data piccolissima, N e n i nodi congiunti dalla linea Nn, pK e mk le perpendicolari abbassate sull’asse Qq e prolungate da una parte e dall’altra finché incontrano il cerchio in P e M e la linea dei nodi in D e d.",
     "en": "Let Qpmaq represent an ellipsis described with the greater axis Qq, and the lesser axis ab; QAqB a circle circumscribed; T the earth in the common centre of both; S the sun; p the moon moving in this ellipsis; and pm an arc which it describes in the least moment of time; N and n the nodes joined by the line Nn; pK and mk perpendiculars upon the axis Qq, produced both ways till they meet the circle in P and M, and the line of the nodes in D and d.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "ellisse Qpmaq",
       "cerchio QAqB",
       "T",
       "arco pm",
       "nodi N, n",
       "pK, mk prolungate",
       "P, M",
       "D, d"
      ]
     }
    },
    {
     "id": "L3-P31-p2",
     "la": "",
     "it": "E se la Luna, con il raggio condotto alla Terra, descrive un’area proporzionale al tempo, il moto orario del nodo nell’ellisse sarà come l’area pDdm e AZ² considerate congiuntamente.",
     "en": "And if the moon, by a radius drawn to the earth, describes an area proportional to the time of description, the horary motion of the node in the ellipsis will be as the area pDdm and AZ2 conjunctly.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area pDdm"
      ],
      "evidenzia": [
       "moto orario ∝ area pDdm × AZ²"
      ]
     },
     "nota": "È la tesi del problema, enunciata alla fine della costruzione."
    },
    {
     "id": "L3-P31-p3",
     "la": "",
     "it": "Infatti, tocchi PF il cerchio in P e, prolungata, incontri TN in F; e pf tocchi l’ellisse in p e, prolungata, incontri la stessa TN in f; queste tangenti poi convergano sull’asse TQ in Y; e ML rappresenti lo spazio che la Luna, ruotando nel cerchio, mentre descrive l’arco PM, potrebbe descrivere con moto trasverso, sollecitata e spinta dalla detta forza 3IT, ossia 3PK; e ml rappresenti lo spazio che la Luna, ruotando nell’ellisse, potrebbe descrivere nello stesso tempo, sollecitata anch’essa dalla forza 3IT, ossia 3PK; e si prolunghino LP e lp finché incontrano il piano dell’eclittica in G e g; e si congiungano FG e fg, di cui FG, prolungata, tagli pf, pg e TQ rispettivamente in c, e e R, e fg, prolungata, tagli TQ in r.",
     "en": "For let PF touch the circle in P, and produced meet TN in F; and pf touch the ellipsis in p, and produced meet the same TN in f, and both tangents concur in the axis TQ at Y. And let ML represent the space which the moon, by the impulse of the above-mentioned force 3IT or 3PK, would describe with a transverse motion, in the meantime while revolving in the circle it describes the arc PM; and ml denote the space which the moon revolving in the ellipsis would describe in the same time by the impulse of the same force 3IT or 3PK; and let LP and lp be produced till they meet the plane of the ecliptic in G and g, and FG and fg be joined, of which FG produced may cut pf, pg, and TQ, in c, e, and R respectively; and fg produced may cut TQ in r.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "PF",
       "pf",
       "F",
       "f",
       "Y",
       "ML",
       "ml",
       "G",
       "g",
       "FG",
       "fg",
       "c",
       "e",
       "R",
       "r"
      ]
     }
    },
    {
     "id": "L3-P31-p4",
     "la": "",
     "it": "Poiché la forza 3IT, ossia 3PK, nel cerchio sta alla forza 3IT, ossia 3pK, nell’ellisse come PK sta a pK, ossia come AT sta ad aT, lo spazio ML generato dalla prima forza starà allo spazio ml generato dalla seconda come PK sta a pK, cioè, per la similitudine delle figure PYKp e FYRc, come FR sta a cR.",
     "en": "Because the force 3IT or 3PK in the circle is to the force 3IT or 3pK in the ellipsis as PK to pK, or as AT to aT, the space ML generated by the former force will be to the space ml generated by the latter as PK to pK; that is, because of the similar figures PYKp and FYRc, as FR to cR.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "figure simili PYKp, FYRc"
      ],
      "evidenzia": [
       "ML : ml = PK : pK = FR : cR"
      ]
     }
    },
    {
     "id": "L3-P31-p5",
     "la": "",
     "it": "Ma ML sta a FG (per la similitudine dei triangoli PLM, PGF) come PL sta a PG, cioè (per le parallele Lk, PK, GR) come pl sta a pe, cioè (per la similitudine dei triangoli plm, cpe) come lm sta a ce; e, invertendo, come LM sta a lm, ossia come FR sta a cR, così FG sta a ce.",
     "en": "But (because of the similar triangles PLM, PGF) ML is to FG as PL to PG, that is (on account of the parallels Lk, PK, GR), as pl to pe, that is (because of the similar triangles plm, cpe), as lm to ce; and inversely as LM is to lm, or as FR is to cR, so is FG to ce.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangoli PLM, PGF",
       "parallele Lk, PK, GR",
       "triangoli plm, cpe"
      ],
      "evidenzia": [
       "FG : ce = FR : cR"
      ]
     }
    },
    {
     "id": "L3-P31-p6",
     "la": "",
     "it": "E perciò, se fg stesse a ce come fY sta a cY, cioè come fr sta a cR (cioè come fr sta a FR e FR sta a cR considerati congiuntamente, cioè come fT sta a FT e FG sta a ce considerati congiuntamente), poiché il rapporto di FG a ce, tolto da entrambe le parti, lascia i rapporti di fg a FG e di fT a FT, fg starebbe a FG come fT sta a FT; e perciò gli angoli che FG e fg sottenderebbero alla Terra T sarebbero uguali fra loro.",
     "en": "And therefore if fg was to ce as fy to cY, that is, as fr to cR (that is, as fr to FR and FR to cR conjunctly, that is, as fT to FT, and FG to ce conjunctly), because the ratio of FG to ce, expunged on both sides, leaves the ratios fg to FG and fT to FT, fg would be to FG as fT to FT; and, therefore, the angles which FG and fg would subtend at the earth T would be equal to each other.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "angoli sottesi da FG e fg in T"
      ]
     },
     "nota": "Motte scrive «fy» (minuscola) per fY."
    },
    {
     "id": "L3-P31-p7",
     "la": "",
     "it": "Ma quegli angoli (per ciò che abbiamo esposto nella proposizione precedente) sono i moti dei nodi nel tempo in cui la Luna percorre nel cerchio l’arco PM, nell’ellisse l’arco pm; e perciò i moti dei nodi nel cerchio e nell’ellisse sarebbero uguali fra loro.",
     "en": "But these angles (by what we have shewn in the preceding Proposition) are the motions of the nodes, while the moon describes in the circle the arc PM, in the ellipsis the arc pm; and therefore the motions of the nodes in the circle and in the ellipsis would be equal to each other.",
     "dipende_da": [
      "Prop. XXX"
     ],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P31-p8",
     "la": "",
     "it": "Così andrebbero le cose, se fg stesse a ce come fY sta a cY, cioè se fg fosse uguale a ce×fY/cY.",
     "en": "Thus, I say, it would be, if fg was to ce as fY to cY, that is, if fg was equal to [SVG 1046] .",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Trascrizione «ce×fYcY» = ce×fY/cY (Motte SVG 1046, concorde)."
    },
    {
     "id": "L3-P31-p9",
     "la": "",
     "it": "Ma per la similitudine dei triangoli fgp, cep, fg sta a ce come fp sta a cp; e perciò fg è uguale a ce×fp/cp; e perciò l’angolo che fg sottende realmente sta all’angolo precedente, che sottende FG, cioè il moto dei nodi nell’ellisse sta al moto dei nodi nel cerchio, come questa fg, ossia ce×fp/cp, sta alla fg precedente, ossia ce×fY/cY, cioè come fp×cY sta a fY×cp, ossia come fp sta a fY e cY sta a cp; cioè, se ph, parallela a TN, incontra FP in h, come Fh sta a FY e FY sta a FP; cioè come Fh sta a FP, ossia Dp sta a DP, e perciò come l’area Dpmd sta all’area DPMd.",
     "en": "But because of the similar triangles fgp, cep, fg is to ce as fp to cp; and therefore fg is equal to [SVG 1047] ; and therefore the angle which fg subtends in fact is to the former angle which FG subtends, that is to say, the motion of the nodes in the ellipsis is to the motion of the same in the circle as this fg or [SVG 1048] to the former fg or [SVG 1046] , that is, as fp × cY to fY × cp, or as fp to fY, and cY to cp; that is, if ph parallel to TN meet FP in h, as Fh to FY and FY to FP; that is, as Fh to FP or Dp to DP, and therefore as the area Dpmd to the area DPMd.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "triangoli fgp, cep",
       "ph ∥ TN",
       "h"
      ],
      "evidenzia": [
       "moto nell’ellisse : moto nel cerchio = area Dpmd : area DPMd"
      ]
     },
     "nota": "Trascrizione «ce×fpcp» = ce×fp/cp (Motte SVG 1047, 1048)."
    },
    {
     "id": "L3-P31-p10",
     "la": "",
     "it": "E perciò, poiché (per il Cor. 1 della Prop. XXX) quest’ultima area e AZ² considerate congiuntamente sono proporzionali al moto orario dei nodi nel cerchio, la prima area e AZ² considerate congiuntamente saranno proporzionali al moto orario dei nodi nell’ellisse. C.V.D.",
     "en": "And, therefore, seeing (by Corol. 1, Prop. XXX) the latter area and AZ2 conjunctly are proportional to the horary motion of the nodes in the circle, the former area and AZ2 conjunctly will be proportional to the horary motion of the nodes in the ellipsis. Q.E.D.",
     "dipende_da": [
      "Prop. XXX, Cor. 1"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "area pDdm × AZ²"
      ]
     }
    }
   ]
  },
  {
   "id": "L3-P31-Cor",
   "tipo": "Corollarium",
   "titolo": "Prop. XXXI, Cor. — moto orario mediocre nell’ellisse e sua correzione: 16″ 16‴ 37ⁱᵛ 42ᵛ",
   "copertura": [
    "III.G5.46",
    "III.G5.47",
    "III.G5.48"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XXXI, Cor.)"
   },
   "enunciato": {
    "la": "",
    "it": "Perciò, poiché, in una posizione data dei nodi, la somma di tutte le aree pDdm, nel tempo in cui la Luna va dalla quadratura a un luogo qualsiasi m, è l’area mpQEd, che termina alla tangente QE dell’ellisse, e la somma di tutte quelle aree, in una rivoluzione intera, è l’area dell’ellisse intera, il moto mediocre dei nodi nell’ellisse starà al moto mediocre dei nodi nel cerchio come l’ellisse sta al cerchio, cioè come Ta sta a TA, ossia come 69 sta a 70.",
    "en": "Since, therefore, in any given position of the nodes, the sum of all the areas pDdm, in the time while the moon is carried from the quadrature to any place m, is the area mpQEd terminated at the tangent of the ellipsis QE; and the sum of all those areas, in one entire revolution, is the area of the whole ellipsis; the mean motion of the nodes in the ellipsis will be to the mean motion of the nodes in the circle as the ellipsis to the circle; that is, as Ta to TA, or 69 to 70."
   },
   "figura_base": {
    "punti": [
     "Q",
     "E",
     "p",
     "m",
     "d",
     "T",
     "a",
     "A"
    ],
    "vincoli": [
     "Ta : TA = 69 : 70 (Prop. XXVIII)"
    ]
   },
   "dati": {
    "moto_orario_nel_cerchio": "16″ 35‴ 16ⁱᵛ 36ᵛ",
    "moto_orario_nell_ellisse": "16″ 21‴ 3ⁱᵛ 30ᵛ",
    "momenti_area_quadratura_sizigia": [
     10973,
     11073
    ],
    "semisomma": 11023,
    "semidifferenza": 50,
    "moto_totale_in_sizigia": "32″ 42‴ 7ⁱᵛ",
    "decremento": "17‴ 43ⁱᵛ 11ᵛ",
    "quarta_parte": "4‴ 25ⁱᵛ 48ᵛ",
    "moto_orario_mediocre_corretto": "16″ 16‴ 37ⁱᵛ 42ᵛ",
    "verifica": "tutte le cifre tornano (tmp/24b/verifica.py); la media del decremento relativo, integrata, è esattamente 1/4"
   },
   "passi": [
    {
     "id": "L3-P31-Cor-p1",
     "la": "",
     "it": "E perciò, poiché (per il Cor. 2 della Prop. XXX) il moto orario mediocre dei nodi nel cerchio sta a 16″ 35‴ 16ⁱᵛ 36ᵛ come AZ² sta ad AT², se si prende l’angolo 16″ 21‴ 3ⁱᵛ 30ᵛ che stia all’angolo 16″ 35‴ 16ⁱᵛ 36ᵛ come 69 sta a 70, il moto orario mediocre dei nodi nell’ellisse starà a 16″ 21‴ 3ⁱᵛ 30ᵛ come AZ² sta ad AT²; cioè come il quadrato del seno della distanza del nodo dal Sole sta al quadrato del raggio.",
     "en": "And, therefore, since (by Corol. 2, Prop. XXX) the mean horary motion of the nodes in the circle is to 16'' 35''' 16iv. 36v. as AZ2 to AT2, if we take the angle 16'' 21''' 3iv. 30v. to the angle 16'' 35''' 16iv. 36v. as 69 to 70, the mean horary motion of the nodes in the ellipsis will be to 16'' 21''' 3iv. 30v. as AZ2 to AT2; that is, as the square of the sine of the distance of the node from the sun to the square of the radius.",
     "dipende_da": [
      "Prop. XXX, Cor. 2"
     ],
     "figura": {
      "mostra": []
     },
     "nota": "16″ 35‴ 16ⁱᵛ 36ᵛ × 69/70 = 16″ 21‴ 3ⁱᵛ 30ᵛ (verificato)."
    },
    {
     "id": "L3-P31-Cor-p2",
     "la": "",
     "it": "Del resto la Luna, con il raggio condotto alla Terra, descrive l’area più velocemente nelle sizigie che nelle quadrature, e per questa ragione il tempo nelle sizigie si contrae, nelle quadrature si allunga; e insieme con il tempo il moto dei nodi aumenta e diminuisce.",
     "en": "But the moon, by a radius drawn to the earth, describes the area in the syzygies with a greater velocity than it does that in the quadratures, and upon that account the time is contracted in the syzygies, and prolonged in the quadratures; and together with the time the motion of the nodes is likewise augmented or diminished.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P31-Cor-p3",
     "la": "",
     "it": "Ora, il momento dell’area nelle quadrature della Luna stava al suo momento nelle sizigie come 10973 sta a 11073; e perciò il momento mediocre negli ottanti sta all’eccesso nelle sizigie, e al difetto nelle quadrature, come la semisomma dei numeri, 11023, sta alla loro semidifferenza, 50.",
     "en": "But the moment of the area in the quadrature of the moon was to the moment thereof in the syzygies as 10973 to 11073; and therefore the mean moment in the octants is to the excess in the syzygies, and to the defect in the quadratures, as 11023, the half sum of those numbers, to their half difference 50.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Il dato 10973 : 11073 viene dalla Prop. XXVI (Fasc. 24a), non citata esplicitamente."
    },
    {
     "id": "L3-P31-Cor-p4",
     "la": "",
     "it": "Quindi, poiché il tempo della Luna in singole particelle uguali dell’orbita è inversamente come la sua velocità, il tempo mediocre negli ottanti starà all’eccesso del tempo nelle quadrature, e al difetto nelle sizigie, dovuti a questa causa, come 11023 sta a 50 con ottima approssimazione.",
     "en": "Wherefore since the time of the moon in the several little equal parts of its orbit is reciprocally as its velocity, the mean time in the octants will be to the excess of the time in the quadratures, and to the defect of the time in the syzygies arising from this cause, nearly as 11023 to 50.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P31-Cor-p5",
     "la": "",
     "it": "Procedendo poi dalle quadrature alle sizigie, trovo che l’eccesso dei momenti dell’area nei singoli luoghi, sul momento minimo nelle quadrature, è con ottima approssimazione come il quadrato del seno della distanza della Luna dalle quadrature; e perciò la differenza fra il momento in un luogo qualsiasi e il momento mediocre negli ottanti è come la differenza fra il quadrato del seno della distanza della Luna dalle quadrature e il quadrato del seno di 45 gradi, ossia la metà del quadrato del raggio; e l’incremento del tempo nei singoli luoghi fra gli ottanti e le quadrature, e il suo decremento fra gli ottanti e le sizigie, è nello stesso rapporto.",
     "en": "But, reckoning from the quadratures to the syzygies, I find that the excess of the moments of the area, in the several places above the least moment in the quadratures, is nearly as the square of the sine of the moon's distance from the quadratures; and therefore the difference betwixt the moment in any place, and the mean moment in the octants, is as the difference betwixt the square of the sine of the moon's distance from the quadratures, and the square of the sine of 45 degrees, or half the square of the radius; and the increment of the time in the several places between the octants and quadratures, and the decrement thereof between the octants and syzygies, is in the same proportion.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P31-Cor-p6",
     "la": "",
     "it": "Il moto dei nodi, poi, nel tempo in cui la Luna percorre singole particelle uguali dell’orbita, è accelerato o ritardato in rapporto duplicato del tempo.",
     "en": "But the motion of the nodes, while the moon describes the several little equal parts of its orbit, is accelerated or retarded in the duplicate proportion of the time;",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P31-Cor-p7",
     "la": "",
     "it": "Infatti questo moto, mentre la Luna percorre PM, è (a parità delle altre condizioni) come ML, e ML è in rapporto duplicato del tempo.",
     "en": "for that motion, while the moon describes PM, is (cæteris paribus) as ML, and ML is in the duplicate proportion of the time.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "ML"
      ]
     }
    },
    {
     "id": "L3-P31-Cor-p8",
     "la": "",
     "it": "Perciò il moto dei nodi nelle sizigie, compiuto nel tempo in cui la Luna percorre particelle date dell’orbita, è diminuito in rapporto duplicato del numero 11073 al numero 11023; e il decremento sta al moto restante come 100 sta a 10973, e al moto totale come 100 sta a 11073, con ottima approssimazione.",
     "en": "Wherefore the motion of the nodes in the syzygies, in the time while the moon describes given little parts of its orbit, is diminished in the duplicate proportion of the number 11073 to the number 11023; and the decrement is to the remaining motion as 100 to 10973; but to the whole motion as 100 to 11073 nearly.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Approssimazione al primo ordine: il valore esatto 1 − (11023/11073)² = 0,009011 contro 100/11073 = 0,009031 (nota N5)."
    },
    {
     "id": "L3-P31-Cor-p9",
     "la": "",
     "it": "Il decremento nei luoghi fra gli ottanti e le sizigie, e l’incremento nei luoghi fra gli ottanti e le quadrature, sta poi a questo decremento, con ottima approssimazione, come il moto totale in quei luoghi sta al moto totale nelle sizigie e la differenza fra il quadrato del seno della distanza della Luna dalla quadratura e la metà del quadrato del raggio sta alla metà del quadrato del raggio, considerati congiuntamente.",
     "en": "But the decrement in the places between the octants and syzygies, and the increment in the places between the octants and quadratures, is to this decrement nearly as the whole motion in these places to the whole motion in the syzygies, and the difference betwixt the square of the sine of the moon's distance from the quadrature, and the half square of the radius, to the half square of the radius conjunctly.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P31-Cor-p10",
     "la": "",
     "it": "Quindi, se i nodi si trovano nelle quadrature, e si prendono due luoghi ugualmente distanti dall’ottante da una parte e dall’altra, e altri due distanti degli stessi intervalli dalla sizigia e dalla quadratura, e dai decrementi dei moti nei due luoghi fra la sizigia e l’ottante si sottraggono gli incrementi dei moti negli altri due luoghi, che sono fra l’ottante e la quadratura, il decremento restante sarà uguale al decremento nella sizigia: come sarà facile constatare a chi faccia il calcolo.",
     "en": "Wherefore, if the nodes are in the quadratures, and we take two places, one on one side, one on the other, equally distant from the octant and other two distant by the same interval, one from the syzygy, the other from the quadrature, and from the decrements of the motions in the two places between the syzygy and octant we subtract the increments of the motions in the two other places between the octant and the quadrature, the remaining decrement will be equal to the decrement in the syzygy, as will easily appear by computation;",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "«in locis duabus»: atteso «duobus» (apparato A.5)."
    },
    {
     "id": "L3-P31-Cor-p11",
     "la": "",
     "it": "Pertanto il decremento mediocre, che va sottratto dal moto mediocre dei nodi, è la quarta parte del decremento nella sizigia.",
     "en": "and therefore the mean decrement, which ought to be subducted from the mean motion of the nodes, is the fourth part of the decrement in the syzygy.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Verificato per integrazione: la media vale esattamente 1/4 (nota N5)."
    },
    {
     "id": "L3-P31-Cor-p12",
     "la": "",
     "it": "Il moto orario totale dei nodi nelle sizigie, quando si supponeva che la Luna, con il raggio condotto alla Terra, descrivesse un’area proporzionale al tempo, era 32″ 42‴ 7ⁱᵛ.",
     "en": "The whole horary motion of the nodes in the syzygies (when the moon by a radius drawn to the earth was supposed to describe an area proportional to the time) was 32'' 42'' 7iv.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "= 2 × 16″ 21‴ 3ⁱᵛ 30ᵛ. Motte stampa «42''» per 42‴."
    },
    {
     "id": "L3-P31-Cor-p13",
     "la": "",
     "it": "E il decremento del moto dei nodi, nel tempo in cui la Luna, ora più veloce, descrive lo stesso spazio, abbiamo detto che sta a questo moto come 100 sta a 11073; e perciò quel decremento è 17‴ 43ⁱᵛ 11ᵛ, la cui quarta parte, 4‴ 25ⁱᵛ 48ᵛ, sottratta dal moto orario mediocre trovato sopra, 16″ 21‴ 3ⁱᵛ 30ᵛ, lascia 16″ 16‴ 37ⁱᵛ 42ᵛ, moto orario mediocre corretto.",
     "en": "And we have shewn that the decrement of the motion of the nodes, in the time while the moon, now moving with greater velocity, describes the same space, was to this motion as 100 to 11073; and therefore this decrement is 17''' 43iv. 11v. The fourth part of which 4''' 25iv. 48v. subtracted from the mean horary motion above found, 16'' 21'' 3iv. 30v. leaves 16'' 16''' 37iv. 42v. their correct mean horary motion.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Tutte le cifre verificate. Motte stampa «16'' 21'' 3iv. 30v.» per 16″ 21‴."
    },
    {
     "id": "L3-P31-Cor-p14",
     "la": "",
     "it": "Se i nodi si trovano fuori delle quadrature, e si considerano due luoghi ugualmente distanti dalle sizigie da una parte e dall’altra, la somma dei moti dei nodi, quando la Luna si trova in questi luoghi, starà alla somma dei moti quando la Luna si trova negli stessi luoghi e i nodi nelle quadrature, come AZ² sta ad AT².",
     "en": "If the nodes are without the quadratures, and two places are considered, one on one side, one on the other, equally distant from the syzygies, the sum of the motions of the nodes, when the moon is in those places, will be to the sum of their motions, when the moon is in the same places and the nodes in the quadratures, as AZ2 to AT2.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P31-Cor-p15",
     "la": "",
     "it": "E i decrementi dei moti, dovuti alle cause ora esposte, staranno fra loro come i moti stessi; e perciò i moti restanti staranno fra loro come AZ² sta ad AT², e i moti mediocri come i moti restanti.",
     "en": "And the decrements of the motions arising from the causes but now explained will be mutually as the motions themselves, and therefore the remaining motions will be mutually betwixt themselves as AZ2 to AT2; and the mean motions will be as the remaining motions.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P31-Cor-p16",
     "la": "",
     "it": "Il moto orario mediocre corretto, in una posizione data qualsiasi dei nodi, sta dunque a 16″ 16‴ 37ⁱᵛ 42ᵛ come AZ² sta ad AT², cioè come il quadrato del seno della distanza dei nodi dalle sizigie sta al quadrato del raggio.",
     "en": "And, therefore, in any given position of the nodes, their correct mean horary motion is to 16'' 16''' 37iv. 42v. as AZ2 to AT2; that is, as the square of the sine of the distance of the nodes from the syzygies to the square of the radius.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    }
   ]
  },
  {
   "id": "L3-P32",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXXII — moto medio annuo dei nodi: 19° 18′ 1″ 23‴",
   "copertura": [
    "III.G5.49",
    "III.G5.50",
    "III.G5.51"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XXXII)"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare il moto medio dei nodi della Luna.",
    "en": "To find the mean motion of the nodes of the moon."
   },
   "figura_base": {
    "punti": [
     "T",
     "N",
     "n",
     "A",
     "a",
     "Z",
     "Y",
     "S",
     "d",
     "e",
     "G",
     "F"
    ],
    "vincoli": [
     "cerchio NAn con centro T, raggio AT = 1; Nn linea dei nodi (fissa)",
     "TA diretta al Sole; Aa arco piccolissimo; AZ ⟂ Nn, aY ⟂ Nn",
     "dZ : ½AZ = AT² : (9,0827646 AT² + AZ²); curva NdGn luogo di d",
     "eZ : AZ = AZ² : (9,0827646 AT² + AZ²); curva NeFn luogo di e"
    ]
   },
   "dati": {
    "ore_anno_siderale": 8766.15,
    "moto_orario_quadrature": "16″ 16‴ 37ⁱᵛ 42ᵛ",
    "moto_annuo_massimo": "39° 38′ 7″ 50‴",
    "gradi": 39.6355,
    "rapporto": 9.0827646,
    "semicerchio_su_NeFn": {
     "Newton": "793/60 = 13,216667",
     "calcolato": 13.2166634
    },
    "moto_figura_duplicata": "1° 29′ 58″ 2‴",
    "moto_fra_congiunzioni": "18° 19′ 5″ 53‴",
    "Sole_fra_congiunzioni": "341° 40′ 54″ 7‴",
    "moto_medio_annuo": "19° 18′ 1″ 23‴",
    "tavole": "19° 21′ 21″ 50‴",
    "scarto": "3′ 20″ 27‴ = 1/348 (Newton: < 1/300)",
    "verifica": "tutte le cifre tornano; soluzione in forma chiusa del modello: 19° 18′ 1″ 23½‴"
   },
   "passi": [
    {
     "id": "L3-P32-p1",
     "la": "",
     "it": "Il moto medio annuo è la somma di tutti i moti orari mediocri nell’anno.",
     "en": "The yearly mean motion is the sum of all the mean horary motions throughout the course of the year.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P32-p2",
     "la": "",
     "it": "Immagina che il nodo si trovi in N e che, a ogni ora compiuta, sia riportato indietro al suo luogo precedente, così che, nonostante il suo moto proprio, conservi sempre una posizione data rispetto alle stelle fisse.",
     "en": "Suppose that the node is in N, and that, after every hour is elapsed, it is drawn back again to its former place; so that, notwithstanding its proper motion, it may constantly remain in the same situation with respect to the fixed stars;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "nodo N fisso"
      ]
     }
    },
    {
     "id": "L3-P32-p3",
     "la": "",
     "it": "Immagina inoltre che nel frattempo il Sole S, per il moto della Terra, avanzi a partire dal nodo e compia uniformemente il suo corso annuo apparente.",
     "en": "while in the mean time the sun S, by the motion of the earth, is seen to leave the node, and to proceed till it completes its apparent annual course by an uniform motion.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Sole S",
       "retta TS"
      ]
     }
    },
    {
     "id": "L3-P32-p4",
     "la": "",
     "it": "Sia poi Aa un arco dato piccolissimo che la retta TS, condotta sempre al Sole, con la sua intersezione con il cerchio NAn descrive in un tempo dato piccolissimo; e il moto orario mediocre (per quanto si è ora mostrato) sarà come AZ², cioè (essendo proporzionali AZ e ZY) come il rettangolo formato da AZ e ZY, cioè come l’area AZYa.",
     "en": "Let Aa represent a given least arc, which the right line TS always drawn to the sun, by its intersection with the circle NAn, describes in the least given moment of time; and the mean horary motion (from what we have above shewn) will be as AZ2, that is (because AZ and ZY are proportional), as the rectangle of AZ into ZY, that is, as the area AZYa;",
     "dipende_da": [
      "Prop. XXXI"
     ],
     "figura": {
      "mostra": [
       "arco Aa",
       "AZ",
       "aY",
       "area AZYa"
      ],
      "evidenzia": [
       "moto orario ∝ AZ² ∝ AZ×ZY"
      ]
     },
     "nota": "«per jam ostensa» rimanda alla fine della Prop. XXXI."
    },
    {
     "id": "L3-P32-p5",
     "la": "",
     "it": "E la somma di tutti i moti orari mediocri dall’inizio sarà come la somma di tutte le aree aYZA, cioè come l’area NAZ.",
     "en": "and the sum of all the mean horary motions from the beginning will be as the sum of all the areas aYZA, that is, as the area NAZ.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area NAZ"
      ]
     }
    },
    {
     "id": "L3-P32-p6",
     "la": "",
     "it": "Ma la massima AZYa è uguale al rettangolo formato dall’arco Aa e dal raggio del cerchio; e perciò la somma di tutti i rettangoli nel cerchio intero sta alla somma di altrettanti rettangoli massimi come l’area del cerchio intero sta al rettangolo formato dalla circonferenza intera e dal raggio, cioè come 1 sta a 2.",
     "en": "But the greatest AZYa is equal to the rectangle of the arc Aa into the radius of the circle; and therefore the sum of all these rectangles in the whole circle will be to the like sum of all the greatest rectangles as the area of the whole circle to the rectangle of the whole circumference into the radius, that is, as 1 to 2.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "media di sin² = 1/2"
      ]
     }
    },
    {
     "id": "L3-P32-p7",
     "la": "",
     "it": "Ora, il moto orario che corrisponde al rettangolo massimo era 16″ 16‴ 37ⁱᵛ 42ᵛ.",
     "en": "But the horary motion corresponding to that greatest rectangle was 16'' 16''' 37iv. 42v.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P32-p8",
     "la": "",
     "it": "E questo moto, nell’intero anno siderale di 365 giorni, 6 ore e 9 minuti, diventa 39° 38′ 7″ 50‴.",
     "en": "and this motion in the complete course of the sidereal year, 365d. 6h. 9', amounts to 39° 38' 7'' 50''',",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Verificato: 16″ 16‴ 37ⁱᵛ 42ᵛ × 8766,15 h = 39° 38′ 7″ 50‴."
    },
    {
     "id": "L3-P32-p9",
     "la": "",
     "it": "E perciò la sua metà, 19° 49′ 3″ 55‴, è il moto medio dei nodi che corrisponde al cerchio intero.",
     "en": "and therefore the half thereof, 19° 49' 3'' 55''', is the mean motion of the nodes corresponding to the whole circle.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P32-p10",
     "la": "",
     "it": "E il moto dei nodi, nel tempo in cui il Sole va da N ad A, sta a 19° 49′ 3″ 55‴ come l’area NAZ sta al cerchio intero.",
     "en": "And the motion of the nodes, in the time while the sun is carried from N to A, is to 19° 49' 3'' 55'' as the area NAZ to the whole circle.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Motte stampa «19° 49' 3'' 55''» per 55‴."
    },
    {
     "id": "L3-P32-p11",
     "la": "",
     "it": "Così stanno le cose nell’ipotesi che il nodo sia riportato ogni ora al luogo precedente, così che il Sole, compiuto l’anno intero, ritorni allo stesso nodo da cui si era allontanato all’inizio.",
     "en": "Thus it would be if the node was after every hour drawn back again to its former place, that so, after a complete revolution, the sun at the year's end would be found again in the same node which it had left when the year begun.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P32-p12",
     "la": "",
     "it": "Ma per il moto del nodo avviene che il Sole ritorni prima al nodo, e ora si deve calcolare l’abbreviazione del tempo.",
     "en": "But, because of the motion of the node in the mean time, the sun must needs meet the node sooner; and now it remains that we compute the abbreviation of the time.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P32-p13",
     "la": "",
     "it": "Poiché il Sole nell’intero anno compie 360 gradi, e il nodo con il moto massimo compirebbe nello stesso tempo 39° 38′ 7″ 50‴, ossia 39,6355 gradi, e il moto mediocre del nodo in un luogo qualsiasi N sta al suo moto mediocre nelle sue quadrature come AZ² sta ad AT², il moto del Sole starà al moto del nodo in N come 360 AT² sta a 39,6355 AZ², cioè come 9,0827646 AT² sta ad AZ².",
     "en": "Since, then, the sun, in the course of the year, travels 360 degrees, and the node in the same time by its greatest motion would be carried 39° 38' 7'' 50''', or 39,6355 degrees; and the mean motion of the node in any place N is to its mean motion in its quadratures as AZ2 to AT2; the motion of the sun will be to the motion of the node in N as 360AT2 to 39·6355AZ2; that is, as 9,0827646AT2 to AZ2.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "velocità del Sole : velocità del nodo = 9,0827646 AT² : AZ²"
      ]
     },
     "nota": "Verificato: 360/39,63550926 = 9,0827646 (con 39,6355 arrotondato si avrebbe 9,0827667). La trascrizione non ha il punto dopo «AZq»."
    },
    {
     "id": "L3-P32-p14",
     "la": "",
     "it": "Quindi, se la circonferenza NAn del cerchio intero si divide in particelle uguali Aa, il tempo in cui il Sole percorrerebbe la particella Aa, se il cerchio stesse in quiete, starà al tempo in cui percorre la stessa particella, se il cerchio ruota insieme con i nodi attorno al centro T, inversamente come 9,0827646 AT² sta a 9,0827646 AT² + AZ².",
     "en": "Wherefore if we suppose the circumference NAn of the whole circle to be divided into little equal parts, such as Aa, the time in which the sun would describe the little arc Aa, if the circle was quiescent, will be to the time of which it would describe the same arc, supposing the circle together with the nodes to be revolved about the centre T, reciprocally as 9,0827646AT2 to 9,0827646AT2 + AZ2;",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P32-p15",
     "la": "",
     "it": "Infatti il tempo è inversamente come la velocità con cui la particella è percorsa, e questa velocità è la somma delle velocità del Sole e del nodo.",
     "en": "for the time is reciprocally as the velocity with which the little arc is described, and this velocity is the sum of the velocities of both sun and node.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P32-p16",
     "la": "",
     "it": "Perciò, se il tempo in cui il Sole, senza il moto del nodo, percorrerebbe l’arco NA si rappresenta con il settore NTA, e la particella di tempo in cui percorrerebbe l’arco piccolissimo Aa si rappresenta con la particella ATa del settore; e (abbassata la perpendicolare aY su Nn) se in AZ si prende dZ di lunghezza tale che il rettangolo dZ per ZY stia alla particella ATa del settore come AZ² sta a 9,0827646 AT² + AZ², cioè tale che dZ stia a ½AZ come AT² sta a 9,0827646 AT² + AZ², il rettangolo dZ per ZY rappresenterà il decremento del tempo dovuto al moto del nodo, in tutto il tempo in cui l’arco Aa è percorso.",
     "en": "If, therefore, the sector NTA represent the time in which the sun by itself, without the motion of the node, would describe the arc NA, and the indefinitely small part ATa of the sector represent the little moment of the time in which it would describe the least arc Aa; and (letting fall aY perpendicular upon Nn) if in AZ we take dZ of such length that the rectangle of dZ into ZY may be to the least part ATa of the sector as AZ2 to 9,0827646AT2 + AZ2, that is to say, that dZ may be to [SVG 1049] as AT2 to 9,0827646AT2 + AZ2; the rectangle of dZ into ZY will represent the decrement of the time arising from the motion of the node, while the arc Aa is described;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "settore NTA",
       "particella ATa",
       "punto d su AZ",
       "rettangolo dZ×ZY"
      ],
      "evidenzia": [
       "dZ : ½AZ = AT² : (9,0827646 AT² + AZ²)"
      ]
     },
     "nota": "Trascrizione «12⁤AZ» = ½AZ (Motte SVG 1049, concorde)."
    },
    {
     "id": "L3-P32-p17",
     "la": "",
     "it": "E se il punto d percorre la curva NdGn, l’area curvilinea NdZ sarà il decremento totale nel tempo in cui è percorso l’intero arco NA; e perciò l’eccesso del settore NAT sull’area NdZ sarà quel tempo totale.",
     "en": "and if the curve NdGn is the locus where the point d is always found, the curvilinear area NdZ will be as the whole decrement of time while the whole arc NA is described; and, therefore, the excess of the sector NAT above the area NdZ will be as the whole time.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "curva NdGn",
       "area NdZ"
      ],
      "evidenzia": [
       "tempo = NTA − NdZ"
      ]
     }
    },
    {
     "id": "L3-P32-p18",
     "la": "",
     "it": "E poiché il moto del nodo in un tempo minore è minore in proporzione al tempo, anche l’area AaYZ dovrà essere diminuita nello stesso rapporto.",
     "en": "But because the motion of the node in a less time is less in proportion of the time, the area AaYZ must also be diminished in the same proportion;",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P32-p19",
     "la": "",
     "it": "Ciò avverrà se in AZ si prende una lunghezza eZ che stia alla lunghezza AZ come AZ² sta a 9,0827646 AT² + AZ².",
     "en": "which may be done by taking in AZ the line eZ of such length, that it may be to the length of AZ as AZ2 to 9,0827646AT2 + AZ2;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "punto e su AZ"
      ],
      "evidenzia": [
       "eZ : AZ = AZ² : (9,0827646 AT² + AZ²)"
      ]
     }
    },
    {
     "id": "L3-P32-p20",
     "la": "",
     "it": "Così infatti il rettangolo eZ per ZY starà all’area AZYa come il decremento del tempo in cui è percorso l’arco Aa sta al tempo totale in cui sarebbe percorso se il nodo stesse in quiete; e perciò quel rettangolo corrisponderà al decremento del moto del nodo.",
     "en": "for so the rectangle of eZ into ZY will be to the area AZYa as the decrement of the time in which the arc Aa is described to the whole time in which it would have been described, if the node had been quiescent; and, therefore, that rectangle will be as the decrement of the motion of the node.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "rettangolo eZ×ZY"
      ]
     }
    },
    {
     "id": "L3-P32-p21",
     "la": "",
     "it": "E se il punto e percorre la curva NeFn, l’area totale NeZ, che è la somma di tutti i decrementi, corrisponderà al decremento totale nel tempo in cui è percorso l’arco AN; e l’area restante NAe corrisponderà al moto restante, che è il moto vero del nodo nel tempo in cui l’intero arco NA è percorso per i moti congiunti del Sole e del nodo.",
     "en": "And if the curve NeFn is the locus of the point e, the whole area NeZ, which is the sum of all the decrements of that motion, will be as the whole decrement thereof during the time in which the arc AN is described; and the remaining area NAe will be as the remaining motion, which is the true motion of the node, during the time in which the whole arc NA is described by the joint motions of both sun and node.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "curva NeFn",
       "area NeZ",
       "area NAe"
      ],
      "evidenzia": [
       "moto vero = NAZ − NeZ = NAe"
      ]
     }
    },
    {
     "id": "L3-P32-p22",
     "la": "",
     "it": "Ora, l’area del semicerchio sta all’area della figura NeFn, trovata con il metodo delle serie infinite, come 793 sta a 60 con ottima approssimazione.",
     "en": "Now the area of the semi-circle is to the area of the figure NeFn found by the method of infinite series nearly as 793 to 60.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "figura NeFn"
      ]
     },
     "nota": "«vero vero»: parola ripetuta nella trascrizione. Verificato per quadratura numerica: semicerchio/NeFn = 13,216663 contro 793/60 = 13,216667 (nota N7)."
    },
    {
     "id": "L3-P32-p23",
     "la": "",
     "it": "Ma il moto che corrisponde al cerchio intero era 19° 49′ 3″ 55‴; e perciò il moto che corrisponde alla figura NeFn duplicata è 1° 29′ 58″ 2‴.",
     "en": "But the motion corresponding or proportional to the whole circle was 19° 49' 3'' 55'''; and therefore the motion corresponding to double the figure NeFn is 1° 29' 58'' 2''',",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "19° 49′ 3″ 55‴ × 60/793 = 1° 29′ 58″ 2‴ (verificato)."
    },
    {
     "id": "L3-P32-p24",
     "la": "",
     "it": "Questo, sottratto dal moto precedente, lascia 18° 19′ 5″ 53‴, moto totale del nodo rispetto alle stelle fisse fra due sue congiunzioni con il Sole; e questo moto, sottratto dal moto annuo del Sole di 360 gradi, lascia 341° 40′ 54″ 7‴, moto del Sole fra le stesse congiunzioni.",
     "en": "which taken from the former motion leaves 18° 19' 5'' 53''', the whole motion of the node with respect to the fixed stars in the interval between two of its conjunctions with the sun; and this motion subducted from the annual motion of the sun 360°, leaves 341° 40' 54'' 7''', the motion of the sun in the interval between the same conjunctions.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P32-p25",
     "la": "",
     "it": "Ma questo moto sta al moto annuo di 360° come il moto del nodo ora trovato, 18° 19′ 5″ 53‴, sta al suo moto annuo, che perciò sarà 19° 18′ 1″ 23‴.",
     "en": "But as this motion is to the annual motion 360°, so is the motion of the node but just now found 18° 19' 5'' 53''' to its annual motion, which will therefore be 19° 18' 1'' 23''';",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Verificato. Lo stesso valore (19° 18′ 1″ 23½‴) si ottiene risolvendo il modello in forma chiusa, come fa Machin (nota N8)."
    },
    {
     "id": "L3-P32-p26",
     "la": "",
     "it": "Questo è il moto medio dei nodi nell’anno siderale.",
     "en": "and this is the mean motion of the nodes in the sidereal year.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P32-p27",
     "la": "",
     "it": "Lo stesso, secondo le tavole astronomiche, è 19° 21′ 21″ 50‴.",
     "en": "By astronomical tables, it is 19° 21' 21'' 50'''.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P32-p28",
     "la": "",
     "it": "La differenza è minore della trecentesima parte del moto totale, e sembra nascere dall’eccentricità dell’orbita lunare e dalla sua inclinazione sul piano dell’eclittica.",
     "en": "The difference is less than [SVG 1050] part of the whole motion, and seems to arise from the eccentricity of the moon's orbit, and its inclination to the plane of the ecliptic.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Differenza 3′ 20″ 27‴ = 1/348 del moto: minore di 1/300, come dice il testo. Motte SVG 1050 = 1/300."
    },
    {
     "id": "L3-P32-p29",
     "la": "",
     "it": "Per l’eccentricità dell’orbita il moto dei nodi è troppo accelerato, e per la sua inclinazione è a sua volta un poco ritardato e ricondotto alla giusta velocità.",
     "en": "By the eccentricity of this orbit the motion of the nodes is too much accelerated; and, on the other hand, by the inclination of the orbit, the motion of the nodes is something retarded, and reduced to its just velocity.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    }
   ]
  },
  {
   "id": "L3-P33",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXXIII — moto vero dei nodi: costruzione dell’equazione semestrale",
   "copertura": [
    "III.G5.52",
    "III.G5.53"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Prop. XXXIII)"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare il moto vero dei nodi della Luna.",
    "en": "To find the true motion of the nodes of the moon."
   },
   "figura_base": {
    "punti": [
     "C",
     "D",
     "B",
     "E",
     "F",
     "A",
     "G",
     "g"
    ],
    "vincoli": [
     "cerchio BEFD con centro C; D, C, B, A allineati, con BC : AC = 1 : 38 3/10",
     "Gg tangente al cerchio in D (perpendicolare a DA)",
     "angolo BCE (o BCF) = doppio della distanza del Sole dal luogo medio del nodo",
     "AE (o AF) incontra DG in G; equazione = 9° 11′ 3″ × DG / circonferenza BED, ≈ angolo DAG"
    ]
   },
   "dati": {
    "AB_su_AC": "19° 18′ 1″ 23‴ : 19° 49′ 3″ 55‴",
    "BC_su_AC": "0° 31′ 2″ 32‴ : 19° 49′ 3″ 55‴ = 1 : 38,305 (Newton 38 3/10)",
    "moto_fra_le_sizigie": "9° 11′ 3″",
    "equazione_negli_ottanti_calcolata": "1° 30′ 0″ (massimo 1° 30′ 1″ per BCE ≈ 88,5°)",
    "angolo_DAG_negli_ottanti": "1° 29′ 44″"
   },
   "passi": [
    {
     "id": "L3-P33-p1",
     "la": "",
     "it": "Nel tempo che è come l’area NTA − NdZ (nella figura precedente), questo moto è come l’area NAe, e di qui è dato.",
     "en": "In the time which is as the area NTA - NdZ (in the preceding Fig.) that motion is as the area NAe, and is thence given;",
     "dipende_da": [
      "Prop. XXXII"
     ],
     "figura": {
      "mostra": []
     },
     "nota": "«in fig. præced.» rimanda alla figura della Prop. XXXII."
    },
    {
     "id": "L3-P33-p2",
     "la": "",
     "it": "Ma, per l’eccessiva difficoltà del calcolo, conviene usare la seguente costruzione del problema.",
     "en": "but because the calculus is too difficult, it will be better to use the following construction of the Problem.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P33-p3",
     "la": "",
     "it": "Con centro C e intervallo qualsiasi CD si descriva il cerchio BEFD.",
     "en": "About the centre C, with any interval CD, describe the circle BEFD;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "C",
       "cerchio BEFD",
       "D"
      ]
     }
    },
    {
     "id": "L3-P33-p4",
     "la": "",
     "it": "Si prolunghi DC fino ad A, così che AB stia ad AC come il moto medio sta alla metà del moto vero mediocre quando i nodi sono nelle quadrature, cioè come 19° 18′ 1″ 23‴ sta a 19° 49′ 3″ 55‴, e perciò BC stia ad AC come la differenza dei moti, 0° 31′ 2″ 32‴, sta al secondo moto, 19° 49′ 3″ 55‴, cioè come 1 sta a 38 3/10; poi per il punto D si conduca la retta infinita Gg, che tocchi il cerchio in D; e se si prende l’angolo BCE, o BCF, uguale al doppio della distanza del Sole dal luogo del nodo trovato con il moto medio, e si conduce AE, o AF, che tagli la perpendicolare DG in G, e si prende un angolo che stia al moto totale del nodo fra le sue sizigie (cioè a 9° 11′ 3″) come la tangente DG sta all’intera circonferenza del cerchio BED, e questo angolo (al posto del quale si può usare l’angolo DAG) si aggiunge al moto medio dei nodi quando i nodi passano dalle quadrature alle sizigie, e si sottrae dallo stesso moto medio quando passano dalle sizigie alle quadrature, si avrà il loro moto vero.",
     "en": "produce DC to A so as AB may be to AC as the mean motion to half the mean true motion when the nodes are in their quadratures (that is, as 19° 18' 1'' 23''' to 19° 49' 3'' 55'''; and therefore BC to AC as the difference of those motions 0° 31' 2'' 32''' to the latter motion 19° 49' 3'' 55'', that is, as 1 to [SVG 1051] ). Then through the point D draw the indefinite line Gg, touching the circle in D; and if we take the angle BCE, or BCF, equal to the double distance of the sun from the place of the node, as found by the mean motion, and drawing AE or AF cutting the perpendicular DG in G, we take another angle which shall be to the whole motion of the node in the interval between its syzygies (that is, to 9° 11'' 3''') as the tangent DG to the whole circumference of the circle BED, and add this last angle (for which the angle DAG may be used) to the mean motion of the nodes, while they are passing from the quadratures to the syzygies, and subtract it from their mean motion while they are passing from the syzygies to the quadratures, we shall have their true motion;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A",
       "B",
       "tangente Gg in D",
       "angolo BCE",
       "E",
       "AE",
       "G",
       "DG",
       "angolo DAG"
      ],
      "evidenzia": [
       "BC : AC = 1 : 38 3/10",
       "equazione = 9° 11′ 3″ × DG/circonferenza"
      ]
     },
     "nota": "«nNodi»: refuso della trascrizione. Trascrizione «38⁤310» = 38 3/10 (Motte SVG 1051). Motte stampa «9° 11'' 3'''» per 9° 11′ 3″ e «55''» per 55‴. Verifiche: nota N9."
    },
    {
     "id": "L3-P33-p5",
     "la": "",
     "it": "Infatti il moto vero così trovato concorderà con ottima approssimazione con il moto vero che risulta rappresentando il tempo con l’area NTA − NdZ e il moto del nodo con l’area NAe, come risulterà a chi esamini la cosa e faccia i calcoli.",
     "en": "for the true motion so found will nearly agree with the true motion which comes out from assuming the times as the area NTA - NdZ, and the motion of the node as the area NAe; as whoever will please to examine and make the computations will find:",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P33-p6",
     "la": "",
     "it": "Questa è l’equazione semestrale del moto dei nodi.",
     "en": "and this is the semi-menstrual equation of the motion of the nodes.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Motte «semi-menstrual» (semimensile) per semestris (semestrale): errore (apparato A.7)."
    },
    {
     "id": "L3-P33-p7",
     "la": "",
     "it": "C’è anche un’equazione mensile, ma essa non è affatto necessaria per trovare la latitudine della Luna.",
     "en": "But there is also a menstrual equation, but which is by no means necessary for finding of the moon's latitude;",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-P33-p8",
     "la": "",
     "it": "Infatti, poiché la variazione dell’inclinazione dell’orbita lunare sul piano dell’eclittica è soggetta a una duplice disuguaglianza, l’una semestrale, l’altra mensile, la disuguaglianza mensile di questa e l’equazione mensile dei nodi si temperano e si correggono a vicenda in modo tale che entrambe si possono trascurare nel determinare la latitudine della Luna.",
     "en": "for since the variation of the inclination of the moon's orbit to the plane of the ecliptic is liable to a twofold inequality, the one semi-menstrual, the other menstrual, the menstrual inequality of this variation, and the menstrual equation of the nodes, so moderate and correct each other, that in computing the latitude of the moon both may be neglected.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Motte «the one semi-menstrual» per alteri semestri: stesso errore."
    }
   ]
  },
  {
   "id": "L3-Machin-P1",
   "tipo": "Propositio (J. Machin)",
   "titolo": "Machin, Prop. I — il moto medio del Sole dal nodo come media proporzionale",
   "copertura": [
    "III.G5.56",
    "III.G5.57",
    "III.G5.58"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Scholium, Prop. I)"
   },
   "enunciato": {
    "la": "",
    "it": "Il moto medio del Sole dal nodo è definito dalla media proporzionale geometrica fra il moto medio del Sole stesso e quel moto mediocre con cui il Sole si allontana più velocemente dal nodo nelle quadrature.",
    "en": "The mean motion of the sun from the node is defined by a geometric mean proportional between the mean motion of the sun and that mean motion with which the sun recedes with the greatest swiftness from the node in the quadratures."
   },
   "figura_base": {
    "punti": [
     "T",
     "N",
     "n",
     "K",
     "M",
     "A",
     "a",
     "b",
     "B",
     "S",
     "H",
     "L",
     "β",
     "G",
     "F",
     "f"
    ],
    "vincoli": [
     "Nn linea dei nodi (fissa), KTM ⟂ Nn; cerchio NKnM di centro T e raggio TK",
     "TS : SK = moto orario medio del Sole : moto orario mediocre del nodo nelle quadrature; TH² = TS × TK",
     "ellisse NHnL di centro T, semiassi TN (= TK) e TH",
     "TA ruota con la velocità relativa Sole–nodo; Tba la incontra nell’ellisse in b; B sull’ellisse lungo TA, β sul cerchio dalla parte opposta",
     "BG ⟂ asse maggiore, prolungata fino al cerchio in F, f"
    ]
   },
   "passi": [
    {
     "id": "L3-Machin-P1-p1",
     "la": "",
     "it": "Sia T il luogo in cui si trova la Terra, Nn la linea dei nodi della Luna in un tempo dato qualsiasi, KTM una retta condotta ad angoli retti con essa, TA una retta che ruota attorno al centro con la velocità angolare con cui il Sole e il nodo si allontanano l’uno dall’altro, così che l’angolo fra la retta in quiete Nn e la retta rotante TA sia sempre uguale alla distanza fra i luoghi del Sole e del nodo.",
     "en": "Let T be the earth's place, Nn the line of the moon's nodes at any given time, KTM a perpendicular thereto, TA a right line revolving about the centre with the same angular velocity with which the sun and the node recede from one another, in such sort that the angle between the quiescent right line Nn and the revolving line TA may be always equal to the distance of the places of the sun and node.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "T",
       "Nn",
       "KTM",
       "TA (rotante)"
      ]
     }
    },
    {
     "id": "L3-Machin-P1-p2",
     "la": "",
     "it": "Ora, se una retta qualsiasi TK si divide nelle parti TS e SK, che stiano come il moto orario medio del Sole sta al moto orario mediocre del nodo nelle quadrature, e si pone la retta TH media proporzionale fra la parte TS e l’intera TK, questa retta, fra le altre, sarà proporzionale al moto medio del Sole dal nodo.",
     "en": "Now if any right line TK be divided into parts TS and SK, and those parts be taken as the mean horary motion of the sun to the mean horary motion of the node in the quadratures, and there be taken the right line TH, a mean proportional between the part TS and the whole TK, this right line will be proportional to the sun's mean motion from the node.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "TK",
       "S su TK",
       "H: TH² = TS×TK"
      ],
      "evidenzia": [
       "TH media proporzionale"
      ]
     },
     "nota": "Motte omette «inter reliquas» («fra le altre», cioè nella stessa scala delle altre rette)."
    },
    {
     "id": "L3-Machin-P1-p3",
     "la": "",
     "it": "Si descriva infatti il cerchio NKnM con centro T e raggio TK, e con lo stesso centro e i semiassi TH e TN si descriva l’ellisse NHnL; e, nel tempo in cui il Sole si allontana dal nodo per l’arco Na, se si conduce la retta Tba, l’area del settore NTa rappresenterà la somma dei moti del nodo e del Sole nello stesso tempo.",
     "en": "For let there be described the circle NKnM from the centre T and with the radius TK, and about the same centre, with the semi-axis TH and TN, let there be described an ellipsis NHnL; and in the time in which the sun recedes from the node through the arc Na, if there be drawn the right line Tba, the area of the sector NTa will be the exponent of the sum of the motions of the sun and node in the same time.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio NKnM",
       "ellisse NHnL",
       "arco Na",
       "retta Tba",
       "settore NTa"
      ]
     }
    },
    {
     "id": "L3-Machin-P1-p4",
     "la": "",
     "it": "Sia dunque aA l’arco piccolissimo che la retta Tba, ruotando secondo la legge detta, descrive uniformemente in una particella di tempo data; e il settore piccolissimo TAa sarà come la somma delle velocità con cui il Sole e il nodo sono portati, ciascuno per conto suo, in quel tempo.",
     "en": "Let, therefore, the extremely small arc aA be that which the right line Tba, revolving according to the aforesaid law, will uniformly describe in a given particle of time, and the extremely small sector TAa will be as the sum of the velocities with which the sun and node are carried two different ways in that time.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "arco aA",
       "settore TAa"
      ]
     }
    },
    {
     "id": "L3-Machin-P1-p5",
     "la": "",
     "it": "Ora, la velocità del Sole è quasi uniforme, poiché la sua piccola disuguaglianza non produce quasi alcuna diversità nel moto medio dei nodi.",
     "en": "Now the sun's velocity is almost uniform, its inequality being so small as scarcely to produce the least inequality in the mean motion of the nodes.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-Machin-P1-p6",
     "la": "",
     "it": "L’altra parte di questa somma, cioè la velocità del nodo nella sua quantità mediocre, aumenta, allontanandosi dalle sizigie, in rapporto duplicato del seno della sua distanza dal Sole, per il Cor. della Prop. 31 del Libro III dei *Principia*; e, quando è massima nelle quadrature, con il Sole in K, ha alla velocità del Sole lo stesso rapporto che SK ha a TS, cioè come (la differenza dei quadrati di TK e TH, ovvero) il rettangolo KHM sta al quadrato di TH.",
     "en": "The other part of this sum, namely, the mean quantity of the velocity of the node, is increased in the recess from the syzygies in a duplicate ratio of the sine of its distance from the sun (by Cor. Prop. XXXI, of this Book), and, being greatest in its quadratures with the sun in K, is in the same ratio to the sun's velocity as SK to TS, that is, as (the difference of the squares of TK and TH, or) the rectangle KHM to TH2.",
     "dipende_da": [
      "Prop. XXXI, Cor."
     ],
     "figura": {
      "mostra": [
       "K"
      ],
      "evidenzia": [
       "SK : TS = KHM : TH²"
      ]
     }
    },
    {
     "id": "L3-Machin-P1-p7",
     "la": "",
     "it": "Ma l’ellisse NBH divide il settore ATa, che rappresenta la somma di queste due velocità, in due parti ABba e BTb proporzionali alle velocità stesse.",
     "en": "But the ellipsis NBH divides the sector ATa, the exponent of the sum of these two velocities, into two parts ABba and BTb, proportional to the velocities.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "B, b sull’ellisse",
       "ABba",
       "BTb"
      ],
      "evidenzia": [
       "ABba : BTb = velocità del nodo : velocità del Sole"
      ]
     }
    },
    {
     "id": "L3-Machin-P1-p8",
     "la": "",
     "it": "Si prolunghi infatti BT fino al cerchio in β, e dal punto B si abbassi sull’asse maggiore la perpendicolare BG, che, prolungata da entrambe le parti, incontri il cerchio nei punti F e f; e poiché lo spazio ABba sta al settore TNb come il rettangolo ABβ sta al quadrato di BT (quel rettangolo infatti è uguale alla differenza dei quadrati di TA e TB, perché la retta Aβ è divisa in parti uguali in T e in parti disuguali in B).",
     "en": "For produce BT to the circle in [SVG 1052] , and from the point B let fall upon the greater axis the perpendicular BG, which being produced both ways may meet the circle in the points F and f; and because the space ABba is to the sector TBb as the rectangle [SVG 1053] to BT2 (that rectangle being equal to the difference of the squares of TA and TB, because the right line [SVG 1054] is equally cut in T, and unequally in B),",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "β",
       "BG",
       "F, f"
      ],
      "evidenzia": [
       "ABβ = TA² − TB²"
      ]
     },
     "nota": "«sectorem TNb»: atteso «TBb», come Motte (apparato A.9). «demitta <453> tur» con marcatore di pagina. «ocurrat»: refuso probabile per «occurrat». La frase latina resta sospesa (anacoluto), e così la traduzione."
    },
    {
     "id": "L3-Machin-P1-p9",
     "la": "",
     "it": "Dunque questo rapporto, quando lo spazio ABba è massimo in K, sarà lo stesso del rapporto del rettangolo KHM al quadrato di HT; ma la velocità mediocre massima del nodo stava alla velocità del Sole in questo rapporto.",
     "en": "therefore when the space ABba is the greatest of all in K, this ratio will be the same as the ratio of the rectangle KHM to HT2. But the greatest mean velocity of the node was shewn above to be in that very ratio to the velocity of the sun;",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-Machin-P1-p10",
     "la": "",
     "it": "Dunque nelle quadrature il settore ATa è diviso in parti proporzionali alle velocità.",
     "en": "and therefore in the quadratures the sector ATa is divided into parts proportional to the velocities.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-Machin-P1-p11",
     "la": "",
     "it": "E poiché il rettangolo KHM sta al quadrato di HT come FBf sta al quadrato di BG, e il rettangolo ABβ è uguale al rettangolo FBf.",
     "en": "And because the rectangle KHM is to HT2 as FBf to BG2, and the rectangle [SVG 1053] is equal to the rectangle FBf,",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "FBf"
      ],
      "evidenzia": [
       "KHM : HT² = FBf : BG²"
      ]
     },
     "nota": "Proposizione causale senza principale: la principale è la frase seguente."
    },
    {
     "id": "L3-Machin-P1-p12",
     "la": "",
     "it": "La piccola area ABba, dove è massima, starà dunque al settore restante TBb come il rettangolo ABβ sta al quadrato di BG.",
     "en": "therefore the little area ABba, where it is greatest, is to the remaining sector TBb as the rectangle [SVG 1053] to BG2",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "In Motte manca il punto dopo «BG2»."
    },
    {
     "id": "L3-Machin-P1-p13",
     "la": "",
     "it": "Ma il rapporto di queste piccole aree era sempre come il rettangolo ABβ sta al quadrato di BT; e perciò la piccola area ABba nel luogo A è minore della piccola area simile nelle quadrature in rapporto duplicato di BG a BT, cioè in rapporto duplicato del seno della distanza del Sole dal nodo.",
     "en": "But the ratio of these little areas always was as the rectangle [SVG 1053] to BT2; and therefore the little area ABba in the place A is less than its correspondent little area in the quadratures in the duplicate ratio of BG to BT, that is, in the duplicate ratio of the sine of the sun's distance from the node.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "ABba ∝ sin²(distanza Sole–nodo)"
      ]
     }
    },
    {
     "id": "L3-Machin-P1-p14",
     "la": "",
     "it": "E perciò la somma di tutte le piccole aree ABba, cioè lo spazio ABN, sarà come il moto del nodo nel tempo in cui il Sole si allontana dal nodo per l’arco NA.",
     "en": "And therefore the sum of all the little areas ABba, to wit, the space ABN, will be as the motion of the node in the time in which the sun hath been going over the arc NA since he left the node;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "spazio ABN"
      ]
     }
    },
    {
     "id": "L3-Machin-P1-p15",
     "la": "",
     "it": "E lo spazio restante, cioè il settore ellittico NTB, sarà come il moto medio del Sole nello stesso tempo.",
     "en": "and the remaining space, namely, the elliptic sector NTB, will be as the sun's mean motion in the same time.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "settore ellittico NTB"
      ]
     }
    },
    {
     "id": "L3-Machin-P1-p16",
     "la": "",
     "it": "E perciò, poiché il moto medio annuo del nodo è quello che avviene nel tempo in cui il Sole ha compiuto il suo periodo, il moto medio del nodo dal Sole starà al moto medio del Sole stesso come l’area del cerchio sta all’area dell’ellisse, cioè come la retta TK sta alla retta TH, che è media proporzionale fra TK e TS; o, il che torna lo stesso, come la media proporzionale TH sta alla retta TS.",
     "en": "And because the mean annual motion of the node is that motion which it performs in the time that the sun completes one period of its course, the mean motion of the node from the sun will be to the mean motion of the sun itself as the area of the circle to the area of the ellipsis; that is, as the right line TK to the right line TH, which is a mean proportional between TK and TS; or, which comes to the same as the mean proportional TH to the right line TS.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "cerchio : ellisse = TK : TH"
      ]
     },
     "nota": "Verificato: il moto relativo medio è √(s(s+n)), media geometrica (nota N11)."
    }
   ]
  },
  {
   "id": "L3-Machin-P2",
   "tipo": "Propositio (J. Machin)",
   "titolo": "Machin, Prop. II — dal moto medio al moto vero dei nodi",
   "copertura": [
    "III.G5.59",
    "III.G5.60"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Scholium, Prop. II)"
   },
   "enunciato": {
    "la": "",
    "it": "Dato il moto medio dei nodi della Luna, trovare il moto vero.",
    "en": "The mean motion of the moon's nodes being given, to find their true motion."
   },
   "figura_base": {
    "punti": [
     "T",
     "N",
     "A",
     "F",
     "B",
     "G",
     "K",
     "H"
    ],
    "vincoli": [
     "come nella Prop. I; F sul cerchio con la stessa ascissa di B; angolo FTN = A (medio), ATN = B (vero)"
    ]
   },
   "passi": [
    {
     "id": "L3-Machin-P2-p1",
     "la": "",
     "it": "Sia l’angolo A la distanza del Sole dal luogo medio del nodo, ossia il moto medio del Sole dal nodo.",
     "en": "Let the angle A be the distance of the sun from the mean place of the node, or the sun's mean motion from the node.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "angolo A"
      ]
     }
    },
    {
     "id": "L3-Machin-P2-p2",
     "la": "",
     "it": "Allora, se si prende un angolo B la cui tangente stia alla tangente dell’angolo A come TH sta a TK, cioè in rapporto subduplicato del moto orario mediocre del Sole al moto orario mediocre del Sole dal nodo, quando il nodo si trova nelle quadrature, questo angolo B sarà la distanza del Sole dal luogo vero del nodo.",
     "en": "Then if we take the angle B, whose tangent is to the tangent of the angle A as TH to TK, that is, in the sub-duplicate ratio of the mean horary motion of the sun to the mean horary motion of the sun from the node, when the node is in the quadrature, that angle B will be the distance of the sun from the node's true place.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "angolo B"
      ],
      "evidenzia": [
       "tan B : tan A = TH : TK"
      ]
     }
    },
    {
     "id": "L3-Machin-P2-p3",
     "la": "",
     "it": "Si congiunga infatti FT, e per la dimostrazione della proposizione precedente l’angolo FTN sarà la distanza del Sole dal luogo medio del nodo, l’angolo ATN invece la distanza dal luogo vero, e le tangenti di questi angoli stanno fra loro come TK sta a TH.",
     "en": "For join FT, and, by the demonstration of the last Proposition, the angle FTN will be the distance of the sun from the mean place of the node, and the angle ATN the distance from the true place, and the tangents of these angles are between themselves as TK to TH.",
     "dipende_da": [
      "Machin, Prop. I"
     ],
     "figura": {
      "mostra": [
       "FT",
       "angoli FTN, ATN"
      ],
      "evidenzia": [
       "tan FTN : tan ATN = FG : BG = TK : TH"
      ]
     },
     "nota": "Verificato per integrazione numerica del moto relativo (nota N11)."
    }
   ]
  },
  {
   "id": "L3-Machin-P2-Cor",
   "tipo": "Corollarium (J. Machin)",
   "titolo": "Machin, Prop. II, Cor. — l’equazione dei nodi",
   "copertura": [
    "III.G5.61"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Scholium, Prop. II, Cor.)"
   },
   "enunciato": {
    "la": "",
    "it": "Di qui l’angolo FTA è l’equazione dei nodi della Luna, e il seno di questo angolo, dove è massimo negli ottanti, sta al raggio come KH sta a TK + TH.",
    "en": "Hence the angle FTA is the equation of the moon's nodes; and the sine of this angle, where it is greatest in the octants, is to the radius as KH to TK + TH."
   },
   "figura_base": {
    "punti": [
     "F",
     "T",
     "A",
     "K",
     "H",
     "N"
    ],
    "vincoli": [
     "FTA = FTN − ATN"
    ]
   },
   "passi": [
    {
     "id": "L3-Machin-P2-Cor-p1",
     "la": "",
     "it": "Il seno di questa equazione in un altro luogo qualsiasi A sta poi al seno massimo come il seno della somma degli angoli FTN + ATN sta al raggio: cioè, all’incirca, come il seno del doppio della distanza del Sole dal luogo medio del nodo (cioè di 2 FTN) sta al raggio.",
     "en": "But the sine of this equation in any other place A is to the greatest sine as the sine of the sums of the angles FTN + ATN to the radius; that is, nearly as the sine of double the distance of the sun from the mean place of the node (namely, 2FTN) to the radius.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "angolo FTA"
      ],
      "evidenzia": [
       "sin FTA = (KH/(TK+TH)) · sin(FTN+ATN)"
      ]
     },
     "nota": "Identità esatta per tan B = k tan A; verificata (nota N11)."
    }
   ]
  },
  {
   "id": "L3-Machin-Schol",
   "tipo": "Scholium (J. Machin)",
   "titolo": "Machin, Scolio — i numeri: 18,6524761 e 18,61214",
   "copertura": [
    "III.G5.62",
    "III.G5.63"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, sezione corrispondente (Scholium)"
   },
   "dati": {
    "TH_su_TK": "√(9,0827646/10,0827646) = 0,9491158 = 18,6524761/19,6524761 (verificato)",
    "moto_medio": "360°/18,6524761 = 19° 18′ 1″ 23½‴ (Machin 23⅔‴)",
    "20_anni_giuliani": "386° 50′ 15″ → 19° 20′ 31″ 56‴ per anno siderale di 365 g 6 h 9 m (Machin 58‴; anno implicito 365,25638 g)",
    "TH_su_HK": "360°/19° 20′ 31″ 58‴ = 18,61214 (verificato)",
    "moto_orario_quadrature": "16″ 18‴ 48ⁱᵛ (verificato)",
    "equazione_massima": {
     "18,6524761": "1° 29′ 45″",
     "18,61214": "1° 29′ 57″ (verificato)"
    }
   },
   "passi": [
    {
     "id": "L3-Machin-Schol-p1",
     "la": "",
     "it": "Se il moto orario mediocre dei nodi nelle quadrature è 16″ 16‴ 37ⁱᵛ 42ᵛ, cioè, nell’intero anno siderale, 39° 38′ 7″ 50‴, TH starà a TK in rapporto subduplicato del numero 9,0827646 al numero 10,0827646, cioè come 18,6524761 sta a 19,6524761.",
     "en": "If the mean horary motion of the nodes in the quadratures be 16'' 16''' 37iv. 42v. that is, in a whole sidereal year, 39° 38' 7'' 50''', TH will be to TK in the subduplicate ratio of the number 9,0827646 to the number 10,0827646, that is, as 18,6524761 to 19,6524761.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-Machin-Schol-p2",
     "la": "",
     "it": "E perciò TH sta a HK come 18,6524761 sta a 1, cioè come il moto del Sole nell’anno siderale sta al moto medio del nodo, 19° 18′ 1″ 23⅔‴.",
     "en": "And, therefore, TH is to HK as 18,6524761 to 1; that is, as the motion of the sun in a sidereal year to the mean motion of the node 19° 18' 1'' [SVG 1055] .",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Trascrizione «23‴⁤23» = 23⅔‴ (Motte SVG 1055). Il calcolo dà 23½‴ (nota N12)."
    },
    {
     "id": "L3-Machin-Schol-p3",
     "la": "",
     "it": "Se invece il moto medio dei nodi della Luna in 20 anni giuliani è 386° 50′ 15″, come si deduce dalle osservazioni usate nella teoria della Luna, il moto medio dei nodi nell’anno siderale sarà 19° 20′ 31″ 58‴.",
     "en": "But if the mean motion of the moon's nodes in 20 Julian years is 386° 50' 15'', as is collected from the observations made use of in the theory of the moon, the mean motion of the nodes in one sidereal year will be 19° 20' 31'' 58'''.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-Machin-Schol-p4",
     "la": "",
     "it": "E TH starà a HK come 360° sta a 19° 20′ 31″ 58‴, cioè come 18,61214 sta a 1; donde il moto orario mediocre dei nodi nelle quadrature risulterà 16″ 18‴ 48ⁱᵛ.",
     "en": "and TH will be to HK as 360° to 19° 20' 31'' 58'''; that is, as 18,61214 to 1: and from hence the mean horary motion of the nodes in the quadratures will come out 16'' 18''' 48iv.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L3-Machin-Schol-p5",
     "la": "",
     "it": "E l’equazione massima dei nodi negli ottanti 1° 29′ 57″.",
     "en": "And the greatest equation of the nodes in the octants will be 1° 29' 57''.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    }
   ]
  }
 ]
}
```
