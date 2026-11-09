> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 19 — Libro II, Sezione VIII: il moto propagato attraverso i fluidi

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo traduce integralmente la **Sezione VIII** del Libro II, *De motu per fluida propagato*: le Proposizioni XLI–L (Teoremi XXXII–XXXVIII, Problemi X–XII), tutti i corollari e lo Scolio finale sulla luce e sul suono, con il calcolo newtoniano della velocità del suono. È una traduzione di lavoro, non un’edizione critica validata.

Gli identificatori **II.S8.01–II.S8.47** e i titoli tematici tra parentesi sono aggiunte editoriali. I numeri romani delle proposizioni, dei teoremi e dei problemi, e i numeri dei casi e dei corollari, appartengono al testo originale. Le integrazioni del curatore sono tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton.

Fuori perimetro: l’ultima frase della Sezione VII che, secondo il brief, poteva comparire all’inizio dell’estratto di Motte. Nel file `motte-1846-L2-S08.md` consegnato per questo fascicolo **non c’è**: l’estratto comincia direttamente con «SECTION VIII.». Nulla è stato escluso.

In coda al fascicolo c’è la **Parte B**, con i dati strutturati per le pagine interattive di 7 unità con figura e costruzione: Prop. XLI e il suo Corollario (che ha una dimostrazione propria con figura), Propp. XLII, XLIV, XLVI, XLVII e XLIX.

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro II, Sezione VIII, **pp. 357–374** (inizio della Prop. XLI a p. 357; i marcatori della trascrizione vanno da ‹358› a ‹374›). Trascrizione normalizzata del Newton Project, documento **NATP00088**, estratta in testo semplice senza correzioni: `fonti/latino-1726-L2-S08.md`. Figure citate: [FIG 63]–[FIG 69], [FIG 60] (sic, nella Prop. XLVII), [FIG 71].
2. **Inglese di confronto.** *Newton’s Principia*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, Section VIII (Project Gutenberg n. 76404), estratto `fonti/motte-1846-L2-S08.md`. L’estratto non contiene marcatori di pagina: per Motte cito la «sezione corrispondente». Le formule stampate come immagini compaiono come `[SVG 922]`–`[SVG 949]`: le ho rese con `rsvg-convert` dall’EPUB (cartella `OEBPS`, file `3191938728343764116_n.svg`) e lette tutte (§ A.13).
3. **Istruzioni del Libro II**, **brief comune** del Libro I, **Fascicolo 3** (modello di formato) e **Fascicolo 5** (modello di fascicolo di Sezione); per i rimandi, i Fascicoli 8 (Libro I, Prop. XXXVIII) e 9 (Libro I, Prop. LI e LII) e la fonte latina della Sezione V del Libro II (Prop. XIX).

Non ho consultato né riprodotto traduzioni moderne. Non ho potuto vedere la stampa del 1726, né Motte 1729, né le figure originali: le relazioni geometriche sono ricostruite dalle sole lettere del testo.

### Criteri di traduzione

- Il testo guida è il latino; l’inglese di Motte serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o si discosta.
- Si applicano il **glossario comune** del brief e il **glossario del Libro II** delle istruzioni: *medium* «mezzo», *fluidum* «fluido», *densitas* «densità», *compressio* «compressione», *vis elastica* «forza elastica», *unda* «onda», *pulsus* «pulsazione», *oscillatio* «oscillazione», *vibratio* «vibrazione», *itus & reditus* «andata e ritorno», *cyclois* «cicloide», *pendulum* «pendolo», *gravitas specifica* «gravità specifica», *pondus* «peso», *particulæ fluidi* «particelle del fluido», *partes* «parti», *canalis* «canale», *foramen* «foro», *aer* «aria», *aqua pluvialis* «acqua piovana», *argentum vivum* «mercurio» (alla prima occorrenza «mercurio (argento vivo)»), *globus* «globo», *conus* «cono», *pes Londinensis / Parisiensis* «piede londinese / parigino», *digitus* «pollice», *minutum secundum* «secondo», *experimentum* «esperimento», *Scholium* «Scolio»; dal glossario comune *ratio subduplicata* «rapporto subduplicato», *reciproce* «inversamente», *directe* «direttamente», *conjunctim* «considerate congiuntamente», *in directum* «in linea retta», *conatus* «tendenza», *impetus* «impeto», *impulsus* «spinta», *determinatus* (aggettivo) «determinato», *plaga* «parte» o «direzione» (§ A.0), *ex æquo* «ex æquo» (in corsivo, termine tecnico delle proporzioni), Q.E.D. «C.V.D.», Q.E.I. «C.V.T.».
- ***Pulsus* è reso «pulsazione»** (decisione del curatore), con nota alla prima occorrenza (II.S8.06): non è l’«impulso» (*impulsus*) della Prop. I del Libro I, ma l’onda di condensazione che si propaga nel mezzo.
- Le estensioni del glossario proprie di questo fascicolo sono elencate e motivate nel § A.0.
- Gli enunciati latini all’infinito o con *dico quod* sono resi con l’indicativo; i problemi (*Invenire…*) con l’infinito italiano.
- Le frazioni appiattite dalla trascrizione sono ricostruite e dichiarate nell’apparato (§ A.12): «619» = 6 1/9, «3118» = 3 1/18, «18313» = 183 1/3, «1323» = 13 2/3, «3915» = 39 1/5, «19034» = 190 3/4, «9799» = 979/9, «10710» = 10 7/10, «12PS» = ½PS, «1V−IM» = 1/(V−IM) e simili. Nel testo tradotto i numeri misti si scrivono «6 1/9», le frazioni con la barra; nessuna formula moderna entra nel testo.

---
## Traduzione italiana

### Sezione VIII. Il moto propagato attraverso i fluidi

### Proposizione XLI. Teorema XXXII (la pressione non si propaga in linea retta)

**[II.S8.01]** **La pressione non si propaga attraverso un fluido secondo linee rette, se non dove le particelle del fluido giacciono in linea retta.**

**[II.S8.02]** Se le particelle a, b, c, d, e giacciono in linea retta, la pressione può certo propagarsi direttamente da a a e; ma la particella e spingerà obliquamente le particelle f e g, poste obliquamente, e quelle particelle f e g non sosterranno la pressione ricevuta, se non sono sostenute da particelle più lontane h e k; e in quanto sono sostenute, premono le particelle che le sostengono; e queste non sosterranno la pressione, se non sono sostenute da altre più lontane, l e m, e non le premono, e così di seguito all’infinito. La pressione dunque, non appena si propaga a particelle che non giacciono in linea retta, comincerà a divaricarsi e si propagherà obliquamente all’infinito; e dopo che ha cominciato a propagarsi obliquamente, se incontra particelle più lontane che non giacciono in linea retta, si divaricherà di nuovo; e ciò tante volte quante incontrerà particelle che non giacciono esattamente in linea retta. C.V.D.

**[II.S8.03]** *Cor.* Se una parte della pressione propagata da un punto dato attraverso un fluido è intercettata da un ostacolo, la parte restante, che non è intercettata, si divaricherà negli spazi dietro l’ostacolo. Ciò si può dimostrare anche così. Dal punto A la pressione si propaghi in ogni direzione, e ciò, se è possibile, secondo linee rette; e, essendo l’ostacolo NBCK forato in BC, sia intercettata tutta, tranne la parte di forma conica APQ che passa attraverso il foro circolare BC. Con i piani trasversali de, fg, hi si divida il cono APQ in tronchi; e mentre il cono ABC, propagando la pressione, spinge il tronco di cono successivo degf sulla superficie de, e questo tronco spinge il tronco vicino fgih sulla superficie fg, e quel tronco spinge il terzo tronco, e così di seguito all’infinito, è manifesto (per la terza legge del moto) che il primo tronco defg, per la reazione del secondo tronco fghi, sarà spinto e premuto sulla superficie fg tanto quanto esso spinge e preme quel secondo tronco. Il tronco aegf [*sic*: degf] è dunque compresso da entrambe le parti, fra il cono Ade e il tronco fhig, e perciò (per il Cor. VI [*sic*: Caso 6] della Prop. XIX) non può conservare la sua figura, se non è compresso con la stessa forza da ogni parte. Con lo stesso impeto con cui è premuto sulle superfici de, fg, tenderà dunque a cedere verso i lati df, eg; e lì (poiché non è rigido, ma fluido in ogni senso) scorrerà fuori e si dilaterà, se non c’è un fluido circostante che trattenga questa tendenza. Perciò, con la tendenza a scorrere fuori, premerà con lo stesso impeto tanto il fluido circostante ai lati df, eg quanto il tronco fghi; e perciò la pressione si propagherà dai lati df, eg negli spazi NO, KL, da una parte e dall’altra, non meno di quanto si propaga dalla superficie fg verso PQ. C.V.D.

### Proposizione XLII. Teorema XXXIII (ogni moto propagato diverge negli spazi immoti)

**[II.S8.04]** **Ogni moto propagato attraverso un fluido diverge dal cammino rettilineo negli spazi immoti.**

**[II.S8.05]** *Caso 1.* Si propaghi un moto dal punto A attraverso il foro BC e proceda, se è possibile, nello spazio conico BCQP, secondo linee rette divergenti dal punto A. E supponiamo dapprima che questo moto sia quello delle onde sulla superficie di un’acqua stagnante. E siano de, fg, hi, kl, ecc. le parti più alte delle singole onde, separate l’una dall’altra da altrettante valli intermedie. Poiché dunque l’acqua nelle creste delle onde è più alta che nelle parti immote del fluido LK, NO, essa scorrerà giù dalle estremità delle creste e, g, i, l, ecc., d, f, h, k, ecc., da una parte e dall’altra, verso KL e NO; e poiché nelle valli delle onde è più bassa che nelle parti immote del fluido KL, NO, scorrerà giù da quelle parti immote [nelle] valli delle onde. Con il primo deflusso le creste delle onde, con il secondo le valli, si dilatano da una parte e dall’altra e si propagano verso KL e NO. E poiché il moto delle onde da A verso PQ avviene per un continuo deflusso dalle creste nelle valli vicine, e perciò non è più veloce di quanto comporti la velocità della discesa; e la discesa dell’acqua da una parte e dall’altra verso KL e NO deve compiersi con la stessa velocità; la dilatazione delle onde da una parte e dall’altra verso KL e NO si propagherà con la stessa velocità con cui le onde stesse avanzano in linea retta da A verso PQ. E perciò tutto lo spazio da una parte e dall’altra, verso KL e NO, sarà occupato dalle onde dilatate rfgr, shis, tklt, vmnv, ecc. C.V.D. Che le cose stiano così, chiunque può sperimentarlo in un’acqua stagnante.

**[II.S8.06]** *Caso 2.* Supponiamo ora che de, fg, hi, kl, mn rappresentino pulsazioni [N2] propagate successivamente dal punto A attraverso un mezzo elastico. Immagina che le pulsazioni si propaghino per condensazioni e rarefazioni successive del mezzo, così che la parte più densa di ciascuna pulsazione occupi una superficie sferica descritta attorno al centro A, e che fra pulsazioni successive intercorrano intervalli uguali. Le linee de, fg, hi, kl, ecc. rappresentino poi le parti più dense delle pulsazioni, propagate attraverso il foro BC. E poiché lì il mezzo è più denso che negli spazi da una parte e dall’altra verso KL e NO, si dilaterà tanto verso quegli spazi KL, NO situati da entrambe le parti quanto verso gli intervalli più radi fra le pulsazioni; e in questo modo, diventando sempre più rado in corrispondenza degli intervalli e più denso in corrispondenza delle pulsazioni, parteciperà del loro moto. E poiché il moto progressivo delle pulsazioni nasce dal continuo rilassarsi delle parti più dense verso gli intervalli più radi che stanno loro davanti; e le pulsazioni devono rilassarsi con quasi la stessa velocità da una parte e dall’altra verso le parti in quiete del mezzo KL, NO; quelle pulsazioni si dilateranno da ogni parte negli spazi immoti KL, NO con quasi la stessa velocità con cui si propagano direttamente dal centro A; e perciò occuperanno tutto lo spazio KLON. C.V.D. Lo sperimentiamo nei suoni, che si odono anche con un monte interposto, oppure, entrati in una stanza attraverso una finestra, si dilatano in tutte le parti della stanza e si odono in tutti gli angoli, non tanto riflessi dalle pareti opposte quanto propagati direttamente dalla finestra, per quanto è lecito giudicare con i sensi.

**[II.S8.07]** *Caso 3.* Supponiamo infine che un moto di qualsiasi genere si propaghi da A attraverso il foro BC. Poiché questa propagazione non avviene se non in quanto le parti del mezzo più vicine al centro A spingono e mettono in moto le parti più lontane; e le parti che sono spinte sono fluide, e perciò si ritirano in ogni direzione verso le regioni dove sono meno premute; esse si ritireranno verso tutte le parti del mezzo in quiete, tanto le laterali KL e NO quanto le anteriori PQ; e in questo modo ogni moto, non appena è passato attraverso il foro BC, comincerà a dilatarsi e di lì, come da un principio e da un centro, a propagarsi direttamente in ogni parte. C.V.D.

### Proposizione XLIII. Teorema XXXIV (il corpo tremulo nel mezzo elastico e non elastico)

**[II.S8.08]** **Ogni corpo tremulo, in un mezzo elastico, propagherà il moto delle pulsazioni da ogni parte in linea retta; in un mezzo non elastico, invece, ecciterà un moto circolare.**

**[II.S8.09]** *Caso 1.* Infatti le parti del corpo tremulo, andando e tornando alternativamente, con la loro andata spingeranno e sospingeranno le parti del mezzo a esse più vicine, e spingendole le comprimeranno e le condenseranno; poi, con il loro ritorno, lasceranno che le parti compresse si ritirino e si espandano. Le parti del mezzo più vicine al corpo tremulo andranno dunque e torneranno alternativamente, come le parti di quel corpo tremulo; e per la stessa ragione per cui le parti di questo corpo agitavano queste parti del mezzo, queste, agitate da tremiti simili, agiteranno le parti a esse più vicine, e quelle, agitate allo stesso modo, agiteranno le più lontane, e così di seguito all’infinito. E come le prime parti del mezzo andando si condensano e tornando si rilassano, così le parti restanti si condenseranno ogni volta che vanno e si espanderanno ogni volta che tornano. E perciò non andranno tutte e non torneranno tutte insieme (così infatti, conservando distanze determinate le une dalle altre, non si rarefarebbero e non si condenserebbero alternativamente), ma, avvicinandosi le une alle altre dove si condensano e allontanandosi dove si rarefanno, alcune andranno mentre altre tornano; e ciò alternativamente all’infinito. Le parti che vanno, e andando si condensano, per il loro moto progressivo con cui urtano gli ostacoli, sono le pulsazioni; e perciò le pulsazioni successive si propagheranno in linea retta da ogni corpo tremulo; e ciò a distanze reciproche all’incirca uguali, per gli intervalli di tempo uguali nei quali il corpo, con i suoi singoli tremiti, eccita le singole pulsazioni. E sebbene le parti del corpo tremulo vadano e tornino secondo una direzione certa e determinata, tuttavia le pulsazioni propagate di lì attraverso il mezzo si dilateranno verso i lati, per la proposizione precedente; e da quel corpo tremulo, come da un centro comune, si propagheranno da ogni parte secondo superfici quasi sferiche e concentriche. Ne abbiamo un esempio nelle onde: se sono eccitate da un dito tremulo, non soltanto procedono da una parte e dall’altra secondo la direzione del moto del dito, ma, a modo di cerchi concentrici, cingono subito il dito e si propagano da ogni parte. Infatti la gravità delle onde fa le veci della forza elastica.

**[II.S8.10]** Se invece il mezzo non è elastico, poiché le sue parti, premute dalle parti vibranti del corpo tremulo, non possono condensarsi, il moto si propagherà in un istante verso le parti dove il mezzo cede più facilmente, cioè verso le parti che il corpo tremulo altrimenti lascerebbe vuote dietro di sé. Il caso è lo stesso di quello di un corpo lanciato in un mezzo qualsiasi. Il mezzo, cedendo ai proiettili, non si ritira all’infinito, ma, andando in cerchio, procede verso gli spazi che il corpo lascia dietro di sé. Dunque, ogni volta che il corpo tremulo procede verso una parte qualsiasi, il mezzo, cedendo, procederà in cerchio verso le parti che il corpo lascia; e ogni volta che il corpo ritorna al luogo di prima, il mezzo ne sarà respinto e tornerà al suo luogo di prima. E anche se il corpo tremulo non è saldo, ma flessibile in ogni modo, se tuttavia rimane dato di grandezza, poiché con i suoi tremiti non può spingere il mezzo in alcun luogo senza cedergli nello stesso tempo altrove, farà sì che il mezzo, ritirandosi dalle parti dove è premuto, proceda sempre in giro verso le parti che gli cedono. C.V.D.

**[II.S8.11]** *Cor.* Si ingannano dunque coloro che credono che l’agitazione delle parti della fiamma contribuisca a propagare una pressione secondo linee rette attraverso il mezzo circostante. Una pressione di questo genere dovrà derivare non dalla sola agitazione delle parti della fiamma, ma dalla dilatazione del tutto.

### Proposizione XLIV. Teorema XXXV (l’acqua oscillante in un canale)

**[II.S8.12]** **Se l’acqua sale e scende alternativamente nei bracci verticali KL, MN di un canale, e si costruisce un pendolo la cui lunghezza fra il punto di sospensione e il centro di oscillazione sia uguale alla metà della lunghezza dell’acqua nel canale, dico che l’acqua salirà e scenderà negli stessi tempi in cui il pendolo oscilla.**

**[II.S8.13]** Misuro la lunghezza dell’acqua lungo gli assi del canale e dei bracci, ponendola uguale alla somma di questi assi; e qui non considero la resistenza dell’acqua che nasce dall’attrito del canale. Rappresentino dunque AB, CD l’altezza media dell’acqua nell’uno e nell’altro braccio; e quando l’acqua nel braccio KL sale all’altezza EF, l’acqua nel braccio MN sia scesa all’altezza GH. Sia poi P il corpo pendolo, VP il filo, V il punto di sospensione, RPQSS [*sic*: RPQS] la cicloide che il pendolo descrive, P il suo punto più basso, PQ un arco uguale all’altezza AE. La forza con cui il moto dell’acqua è alternativamente accelerato e ritardato è l’eccesso del peso dell’acqua in uno dei due bracci sul peso nell’altro; e perciò, quando l’acqua nel braccio KL sale a EF e nell’altro braccio scende a GH, quella forza è il doppio del peso dell’acqua EABF, e perciò sta al peso di tutta l’acqua come AE, ossia PQ, sta a VP, ossia PR. Anche la forza con cui il peso P, in un luogo qualsiasi Q, è accelerato e ritardato nella cicloide (per il Cor. della Prop. LI [del Libro I]) sta al suo peso totale come la sua distanza PQ dal luogo più basso P sta alla lunghezza PR della cicloide. Perciò le forze motrici dell’acqua e del pendolo, che descrivono spazi uguali AE, PQ, sono come i pesi da muovere; e perciò, se all’inizio l’acqua e il pendolo sono in quiete, quelle forze li muoveranno in egual misura in tempi uguali, e faranno sì che vadano e tornino insieme con moto reciproco. C.V.D.

**[II.S8.14]** *Cor. 1.* Dunque tutte le alternanze dell’acqua che sale e scende, sia che il moto sia più intenso sia che sia più debole, sono isocrone.

**[II.S8.15]** *Cor. 2.* Se la lunghezza di tutta l’acqua nel canale è di 6 1/9 piedi parigini, l’acqua scenderà nel tempo di un secondo e salirà nel tempo di un altro secondo; e così di seguito, alternativamente, all’infinito. Infatti un pendolo della lunghezza di 3 1/18 piedi oscilla nel tempo di un secondo.

**[II.S8.16]** *Cor. 3.* Aumentata o diminuita la lunghezza dell’acqua, il tempo dell’alternanza aumenta o diminuisce in rapporto subduplicato della lunghezza.

### Proposizione XLV. Teorema XXXVI (velocità delle onde e larghezza)

**[II.S8.17]** **La velocità delle onde è in rapporto subduplicato delle larghezze.**

**[II.S8.18]** Segue dalla costruzione della proposizione seguente.

### Proposizione XLVI. Problema X (trovare la velocità delle onde)

**[II.S8.19]** **Trovare la velocità delle onde.**

**[II.S8.20]** Si costruisca un pendolo la cui lunghezza, fra il punto di sospensione e il centro di oscillazione, sia uguale alla larghezza delle onde: nel tempo in cui quel pendolo compie le singole oscillazioni, le onde, avanzando, percorreranno all’incirca la loro larghezza.

**[II.S8.21]** Chiamo larghezza delle onde la misura trasversale che sta fra i fondi delle valli, oppure fra le sommità più alte. Rappresenti ABCDEF la superficie di un’acqua stagnante che sale e scende in onde successive; e siano A, C, E, ecc. le sommità delle onde, e B, D, F, ecc. le valli intermedie. E poiché il moto delle onde avviene per la salita e la discesa successive dell’acqua, così che le sue parti A, C, E, ecc., che ora sono le più alte, diventano subito dopo le più basse; e la forza motrice con cui le parti più alte scendono e le più basse salgono è il peso dell’acqua sollevata; quella salita e discesa alterna sarà analoga al moto reciproco dell’acqua nel canale e osserverà le stesse leggi quanto al tempo; e perciò (per la Prop. XLIV), se le distanze fra i luoghi più alti delle onde A, C, E e i più bassi B, D, F sono uguali al doppio della lunghezza del pendolo, le parti più alte A, C, E diventeranno le più basse nel tempo di una oscillazione, e nel tempo di un’altra oscillazione risaliranno. Dunque fra il passaggio di un’onda e quello della successiva il tempo sarà di due oscillazioni; cioè l’onda descriverà la sua larghezza nel tempo in cui quel pendolo oscilla due volte; ma nello stesso tempo un pendolo di lunghezza quadrupla, e perciò uguale alla larghezza delle onde, oscillerà una volta. C.V.T.

**[II.S8.22]** *Cor. 1.* Dunque le onde larghe 3 1/18 piedi parigini, avanzando, percorreranno la loro larghezza nel tempo di un secondo; e perciò nel tempo di un minuto percorreranno 183 1/3 piedi, e nello spazio di un’ora, con ottima approssimazione, 11000 piedi.

**[II.S8.23]** *Cor. 2.* E la velocità di onde maggiori o minori aumenterà o diminuirà in rapporto subduplicato della larghezza.

**[II.S8.24]** Queste cose stanno così nell’ipotesi che le parti dell’acqua salgano in linea retta e scendano in linea retta; ma quella salita e discesa avviene più veramente lungo un cerchio, e perciò affermo che il tempo è definito da questa proposizione soltanto con ottima approssimazione.

### Proposizione XLVII. Teorema XXXVII (le particelle del mezzo oscillano come un pendolo)

**[II.S8.25]** **Quando si propagano pulsazioni attraverso un fluido, le singole particelle del fluido, andando e tornando con un moto reciproco brevissimo, sono sempre accelerate e ritardate secondo la legge del pendolo che oscilla.**

**[II.S8.26]** Rappresentino AB, BC, CD, ecc. le distanze uguali di pulsazioni successive; ABC la direzione del moto delle pulsazioni propagate da A verso B; E, F, G tre punti fisici del mezzo in quiete, situati sulla retta AC a distanze uguali l’uno dall’altro; Ee, Ff, Gg spazi uguali brevissimi attraverso i quali quei punti, con moto reciproco, vanno e tornano a ogni vibrazione; ε, φ, γ luoghi intermedi qualsiasi degli stessi punti; ed EF, FG lineette fisiche, ossia parti lineari del mezzo interposte fra quei punti e trasportate successivamente nei luoghi εφ, φγ ed ef, fg. Si conduca la retta PS uguale alla retta Ee. La si divida a metà in O, e con centro O e raggio OP si descriva il cerchio SIPi. Con la sua circonferenza intera e con le sue parti si rappresenti il tempo intero di una vibrazione con le sue parti proporzionali; così che, compiuto un tempo qualsiasi PH o PHSh, se si abbassa su PS la perpendicolare HL o hl e si prende Eε uguale a PL o Pl, il punto fisico E si trovi in ε. Con questa legge un punto qualsiasi E, andando da E per ε fino a e, e di lì tornando per ε fino a E, compirà le singole vibrazioni con gli stessi gradi di accelerazione e di ritardo di un pendolo che oscilla. Si deve provare che i singoli punti fisici del mezzo devono essere agitati con un moto siffatto. Immaginiamo dunque che il mezzo sia messo in moto in questo modo da una causa qualsiasi, e vediamo che cosa ne segue.

**[II.S8.27]** Sulla circonferenza PHSh si prendano archi uguali HI, IK, o hi, ik, che abbiano con la circonferenza intera lo stesso rapporto che le rette uguali EF, FG hanno con l’intervallo intero delle pulsazioni BC. E si abbassino le perpendicolari IM, KN, o im, kn. Poiché i punti E, F, G sono agitati successivamente da moti simili e compiono le loro vibrazioni intere, composte di andata e ritorno, nel tempo in cui la pulsazione è trasportata da B a C, se PH o PHSh è il tempo dall’inizio del moto del punto E, PI o PHSi sarà il tempo dall’inizio del moto del punto F, e PK o PHSk il tempo dall’inizio del moto del punto G; e perciò Eε, Fφ, Gγ saranno uguali rispettivamente a PL, PM, PN nell’andata dei punti, oppure a Pl, Pn, Pm [*sic*: Pl, Pm, Pn] nel ritorno dei punti. Di qui εγ, ossia EG + Gγ − Eε, nell’andata dei punti sarà uguale a EG − LN, nel ritorno invece a EG + ln. Ma εγ è la larghezza, ossia l’espansione, della parte EG del mezzo nel luogo εγ; e perciò l’espansione di quella parte nell’andata sta alla sua espansione media come EG − LN sta a EG; nel ritorno, invece, come EG + ln, ossia EG + LN, sta a EG. Perciò, poiché LN sta a KH come IM sta al raggio OP, e KH sta a EG come la circonferenza PHShP sta a BC, cioè, se si pone V per il raggio del cerchio la cui circonferenza è uguale all’intervallo delle pulsazioni BC, come OP sta a V; ed *ex æquo* LN sta a EG come IM sta a V: l’espansione della parte EG, ossia del punto fisico F, nel luogo εγ starà all’espansione media che quella parte ha nel suo primo luogo EG come V − IM sta a V nell’andata, e come V + im sta a V nel ritorno. Di qui la forza elastica del punto F nel luogo εγ sta alla sua forza elastica media nel luogo EG come 1/(V − IM) sta a 1/V nell’andata; nel ritorno, invece, come 1/(V + im) sta a 1/V. E con lo stesso argomento le forze elastiche dei punti fisici E e G nell’andata stanno come 1/(V − HL) e 1/(V − KN) a 1/V; e la differenza delle forze sta alla forza elastica media del mezzo come (HL − KN)/(VV − V × HL − V × KN + HL × KN) sta a 1/V. Cioè come (HL − KN)/VV sta a 1/V, ossia come HL − KN sta a V, purché (per gli stretti limiti delle vibrazioni) supponiamo HL e KN indefinitamente minori della quantità V. Perciò, poiché la quantità V è data, la differenza delle forze è come HL − KN, cioè (poiché HL − KN sta a HK come OM sta a OI, o a OP, e HK e OP sono date) come OM; cioè, se Ff è divisa a metà in Ω, come Ωφ. E con lo stesso argomento la differenza delle forze elastiche dei punti fisici ε e γ, nel ritorno della lineetta fisica εγ, è come Ωφ. Ma quella differenza (cioè l’eccesso della forza elastica del punto ε sulla forza elastica del punto γ) è la forza da cui la lineetta fisica εγ del mezzo, interposta fra quei punti, è accelerata nell’andata e ritardata nel ritorno; e perciò la forza acceleratrice della lineetta fisica εγ è come la sua distanza dal luogo medio della vibrazione Ω. Perciò (per la Prop. XXXVIII del Libro I) il tempo è rappresentato correttamente dall’arco PI; e la parte lineare del mezzo εγ si muove secondo la legge prescritta, cioè secondo la legge del pendolo che oscilla; e lo stesso vale per tutte le parti lineari di cui è composto l’intero mezzo. C.V.D.

**[II.S8.28]** *Cor.* Di qui è chiaro che il numero delle pulsazioni propagate è lo stesso del numero delle vibrazioni del corpo tremulo, e non si moltiplica nel loro avanzare. Infatti la lineetta fisica εγ, non appena sarà tornata al suo primo luogo, starà in quiete; e in seguito non si muoverà più, se non è messa in moto con un moto nuovo o dall’impeto del corpo tremulo o dall’impeto delle pulsazioni che si propagano dal corpo tremulo. Starà dunque in quiete non appena le pulsazioni cessano di propagarsi dal corpo tremulo.

### Proposizione XLVIII. Teorema XXXVIII (velocità delle pulsazioni, forza elastica e densità)

**[II.S8.29]** **Le velocità delle pulsazioni propagate in un fluido elastico sono nel rapporto composto dal rapporto subduplicato della forza elastica, direttamente, e dal rapporto subduplicato della densità, inversamente; purché si supponga che la forza elastica del fluido sia proporzionale alla sua condensazione.**

**[II.S8.30]** *Caso 1.* Se i mezzi sono omogenei, e le distanze delle pulsazioni in questi mezzi sono uguali fra loro, ma il moto in un mezzo è più intenso, le contrazioni e le dilatazioni delle parti analoghe saranno come quei moti. Questa proporzione, a dire il vero, non è esatta. Tuttavia, se le contrazioni e le dilatazioni non sono molto intense, non sbaglierà in modo sensibile, e perciò può essere ritenuta fisicamente esatta. Ora, le forze elastiche motrici sono come le contrazioni e le dilatazioni; e le velocità generate nello stesso tempo in parti uguali sono come le forze. Perciò parti uguali e corrispondenti di pulsazioni corrispondenti compiranno insieme le loro andate e i loro ritorni attraverso spazi proporzionali alle contrazioni e alle dilatazioni, con velocità che sono come gli spazi; e perciò le pulsazioni, che nel tempo di un’andata e di un ritorno percorrono avanzando la loro larghezza e subentrano sempre nei luoghi delle pulsazioni immediatamente precedenti, per l’uguaglianza delle distanze avanzeranno con velocità uguale nell’uno e nell’altro mezzo.

**[II.S8.31]** *Caso 2.* Se invece le distanze, ossia le lunghezze, delle pulsazioni sono maggiori in un mezzo che nell’altro, supponiamo che le parti corrispondenti, a ogni andata e ritorno, descrivano spazi proporzionali alle larghezze delle pulsazioni: le loro contrazioni e dilatazioni saranno uguali. E perciò, se i mezzi sono omogenei, saranno uguali anche quelle forze elastiche motrici da cui esse sono agitate con moto reciproco. Ma la materia da muovere con queste forze è come la larghezza delle pulsazioni; e nello stesso rapporto è lo spazio attraverso cui devono muoversi a ogni andata e ritorno. E il tempo di un’andata e di un ritorno è nel rapporto composto dal rapporto subduplicato della materia e dal rapporto subduplicato dello spazio, e perciò è come lo spazio. Ma le pulsazioni, nei tempi di un’andata e di un ritorno, percorrono avanzando le loro larghezze, cioè percorrono spazi proporzionali ai tempi; e perciò sono ugualmente veloci.

**[II.S8.32]** *Caso 3.* Nei mezzi di pari densità e di pari forza elastica, dunque, tutte le pulsazioni sono ugualmente veloci. Se poi si accresce o la densità o la forza elastica del mezzo, poiché la forza motrice aumenta nel rapporto della forza elastica e la materia da muovere nel rapporto della densità, il tempo in cui si compiono gli stessi moti di prima aumenterà in rapporto subduplicato della densità e diminuirà in rapporto subduplicato della forza elastica. E perciò la velocità delle pulsazioni sarà nel rapporto composto dal rapporto subduplicato della densità del mezzo, inversamente, e dal rapporto subduplicato della forza elastica, direttamente. C.V.D.

**[II.S8.33]** Questa proposizione risulterà più chiara dalla costruzione della seguente.

### Proposizione XLIX. Problema XI (trovare la velocità delle pulsazioni)

**[II.S8.34]** **Date la densità e la forza elastica di un mezzo, trovare la velocità delle pulsazioni.**

**[II.S8.35]** Immaginiamo che il mezzo sia compresso da un peso sovrastante, come accade alla nostra aria; e sia A l’altezza di un mezzo omogeneo il cui peso uguagli il peso sovrastante e la cui densità sia la stessa del mezzo compresso in cui si propagano le pulsazioni. Si intenda poi costruito un pendolo la cui lunghezza fra il punto di sospensione e il centro di oscillazione sia A: nel tempo in cui quel pendolo compie un’oscillazione intera, composta di andata e ritorno, la pulsazione, andando, percorrerà uno spazio uguale alla circonferenza del cerchio descritto con raggio A.

**[II.S8.36]** Infatti, restando ferma la costruzione della Prop. XLVII, se una linea fisica qualsiasi EF, descrivendo a ogni vibrazione lo spazio PS, è sollecitata, nei luoghi estremi P e S di ciascuna andata e di ciascun ritorno, da una forza elastica uguale al suo peso, essa compirà le singole vibrazioni nel tempo in cui potrebbe oscillare in una cicloide il cui perimetro totale sia uguale alla lunghezza PS; e ciò perché forze uguali spingeranno nello stesso tempo corpuscoli uguali attraverso spazi uguali. Perciò, poiché i tempi delle oscillazioni sono in rapporto subduplicato della lunghezza dei pendoli, e la lunghezza del pendolo è uguale alla metà dell’arco della cicloide intera, il tempo di una vibrazione starebbe al tempo dell’oscillazione del pendolo la cui lunghezza è A in rapporto subduplicato della lunghezza ½PS, ossia PO, alla lunghezza A. Ma la forza elastica da cui è sollecitata la lineetta fisica EG, quando si trova nei suoi luoghi estremi P, S, stava (nella dimostrazione della Prop. XLVII) alla sua forza elastica totale come HL − KN sta a V, cioè (poiché il punto K cade ora in P) come HK sta a V; e quella forza totale, cioè il peso sovrastante da cui la lineetta EG è compressa, sta al peso della lineetta come l’altezza A del peso sovrastante sta alla lunghezza EG della lineetta; e perciò, *ex æquo*, la forza da cui la lineetta EG è sollecitata nei suoi luoghi P e S sta al peso di quella lineetta come HK × A sta a V × EG, ossia come PO × A sta a VV, perché HK stava a EG come PO sta a V. Perciò, poiché i tempi in cui corpi uguali sono spinti attraverso spazi uguali sono inversamente in rapporto subduplicato delle forze, il tempo di una vibrazione, sotto l’azione di quella forza elastica, starà al tempo di una vibrazione sotto l’azione della forza del peso in rapporto subduplicato di VV a PO × A, e quindi al tempo dell’oscillazione del pendolo la cui lunghezza è A nel rapporto subduplicato di VV a PO × A e nel rapporto subduplicato di PO ad A, considerati congiuntamente; cioè nel rapporto intero di V ad A. Ma nel tempo di una vibrazione composta di andata e ritorno la pulsazione, avanzando, percorre la sua larghezza BC. Dunque il tempo in cui la pulsazione percorre lo spazio BC sta al tempo di una oscillazione composta di andata e ritorno come V sta ad A, cioè come BC sta alla circonferenza del cerchio il cui raggio è A. Ma il tempo in cui la pulsazione percorrerà lo spazio BC sta nello stesso rapporto al tempo in cui percorrerà una lunghezza uguale a questa circonferenza; e perciò, nel tempo di una tale oscillazione, la pulsazione percorrerà una lunghezza uguale a questa circonferenza. C.V.D.

**[II.S8.37]** *Cor. 1.* La velocità delle pulsazioni è quella che i gravi acquistano cadendo con moto uniformemente accelerato e descrivendo nella loro caduta la metà dell’altezza A. Infatti nel tempo di questa caduta, con la velocità acquistata cadendo, la pulsazione percorrerà uno spazio uguale all’intera altezza A; e perciò, nel tempo di una oscillazione composta di andata e ritorno, percorrerà uno spazio uguale alla circonferenza del cerchio descritto con raggio A: il tempo della caduta sta infatti al tempo dell’oscillazione come il raggio del cerchio sta alla sua circonferenza.

**[II.S8.38]** *Cor. 2.* Di qui, poiché quell’altezza A è come la forza elastica del fluido, direttamente, e come la sua densità, inversamente, la velocità delle pulsazioni sarà nel rapporto composto dal rapporto subduplicato della densità, inversamente, e dal rapporto subduplicato della forza elastica, direttamente.

### Proposizione L. Problema XII (trovare le distanze delle pulsazioni)

**[II.S8.39]** **Trovare le distanze delle pulsazioni.**

**[II.S8.40]** Si trovi il numero delle vibrazioni, in un tempo dato, del corpo dal cui tremito sono eccitate le pulsazioni. Per quel numero si divida lo spazio che una pulsazione può percorrere nello stesso tempo, e la parte trovata sarà la larghezza di una pulsazione. C.V.T.

### Scolio (luce, suono e velocità del suono)

**[II.S8.41]** Le ultime proposizioni riguardano il moto della luce e dei suoni. La luce, infatti, poiché si propaga secondo linee rette, non può consistere nella sola azione (per le Propp. XLI e XLII). I suoni invece, poiché nascono da corpi tremuli, non sono altro che pulsazioni dell’aria propagate, per la Prop. XLIII. Ciò è confermato dai tremiti che essi eccitano nei corpi posti di fronte, purché siano forti e gravi, come sono i suoni dei tamburi. Infatti i tremiti più rapidi e più brevi si eccitano più difficilmente. Ma è anche notissimo che suoni qualsiasi, che colpiscono corde all’unisono con i corpi sonori, vi eccitano tremiti. È confermato anche dalla velocità dei suoni. Infatti, poiché i pesi specifici dell’acqua piovana e del mercurio (argento vivo) stanno fra loro come 1 a 13 2/3 circa, e, quando il mercurio nel barometro raggiunge l’altezza di 30 pollici inglesi, il peso specifico dell’aria e quello dell’acqua piovana stanno fra loro come 1 a 870 circa, i pesi specifici dell’aria e del mercurio staranno come 1 a 11890. Perciò, poiché l’altezza del mercurio è di 30 pollici, l’altezza dell’aria uniforme il cui peso potrebbe comprimere la nostra aria sottostante sarà di 356700 pollici, ossia di 29725 piedi inglesi. E questa altezza è proprio quella che nella costruzione del problema precedente abbiamo chiamato A. La circonferenza del cerchio descritto con raggio di 29725 piedi è di 186768 piedi. E poiché un pendolo lungo 39 1/5 pollici compie un’oscillazione composta di andata e ritorno nel tempo di due secondi, come è noto, un pendolo lungo 29725 piedi, ossia 356700 pollici, dovrà compiere un’oscillazione simile nel tempo di 190 3/4 secondi. In quel tempo, dunque, il suono, avanzando, percorrerà 186768 piedi, e perciò nel tempo di un secondo 979 piedi.

**[II.S8.42]** Del resto, in questo calcolo non si tiene alcun conto dello spessore delle particelle solide dell’aria, attraverso il quale il suono si propaga certamente in un istante. Poiché il peso dell’aria sta al peso dell’acqua come 1 a 870, e i sali sono quasi due volte più densi dell’acqua, se si suppone che le particelle dell’aria abbiano circa la stessa densità delle particelle o dell’acqua o dei sali, e che la rarità dell’aria nasca dagli intervalli fra le particelle, il diametro di una particella d’aria starà all’intervallo fra i centri delle particelle come 1 a 9 o 10 circa, e all’intervallo fra le particelle come 1 a 8 o 9. Perciò ai 979 piedi che il suono, secondo il calcolo precedente, percorrerà nel tempo di un secondo, è lecito aggiungere 979/9 piedi, ossia circa 109, per lo spessore delle particelle dell’aria; e così il suono percorrerà nel tempo di un secondo circa 1088 piedi.

**[II.S8.43]** Aggiungi a ciò che i vapori nascosti nell’aria, essendo di altra elasticità e di altro tono, partecipano a stento, o neppure a stento, del moto dell’aria vera con cui si propagano i suoni. Se poi questi stanno in quiete, quel moto si propagherà più velocemente attraverso la sola aria vera, e ciò in rapporto subduplicato della minore materia. Così, se l’atmosfera consta di dieci parti di aria vera e di una parte di vapori, il moto dei suoni sarà più veloce in rapporto subduplicato di 11 a 10, ossia circa nel rapporto intero di 21 a 20, che se si propagasse attraverso undici parti di aria vera; e perciò il moto dei suoni trovato sopra dovrà essere accresciuto in questo rapporto. In questo modo il suono, nel tempo di un secondo, percorrerà 1142 piedi.

**[II.S8.44]** Così devono stare le cose in primavera e in autunno, quando l’aria si rarefà per il calore moderato e la sua forza elastica si accresce alquanto. Ma d’inverno, quando l’aria si condensa per il freddo e la sua forza elastica si allenta, il moto dei suoni deve essere più lento in rapporto subduplicato della densità; e viceversa, d’estate deve essere più veloce.

**[II.S8.45]** Risulta poi dagli esperimenti che i suoni, nel tempo di un secondo, percorrono più o meno 1142 piedi londinesi, ossia 1070 parigini.

**[II.S8.46]** Conosciuta la velocità dei suoni, si conoscono anche gli intervalli delle pulsazioni. Il signor Sauveur, infatti, con esperimenti fatti da lui stesso, trovò che una canna aperta, la cui lunghezza è di circa cinque piedi parigini, emette un suono dello stesso tono del suono di una corda che nel tempo di un secondo [*minuti minus secundi*, *sic*] torna indietro cento volte. Vi sono dunque circa cento pulsazioni nello spazio di 1070 piedi parigini, che il suono percorre nel tempo di un secondo; e perciò una pulsazione occupa uno spazio di circa 10 7/10 piedi parigini, cioè circa il doppio della lunghezza della canna. Di qui è verosimile che le larghezze delle pulsazioni, nei suoni di tutte le canne aperte, siano uguali al doppio delle lunghezze delle canne.

**[II.S8.47]** Inoltre, perché i suoni cessino subito quando cessa il moto del corpo sonoro, e non si odano più a lungo quando siamo lontanissimi dai corpi sonori che quando ne siamo vicinissimi, è chiaro dal corollario della Prop. XLVII di questo libro. Ma anche perché i suoni si accrescano molto nelle trombe stentorofoniche è manifesto dai principi esposti. Ogni moto reciproco, infatti, suole essere accresciuto a ogni ritorno dalla causa che lo genera. Ma nei tubi che impediscono la dilatazione dei suoni il moto si perde più lentamente e ritorna più forte, e perciò è accresciuto di più dal moto nuovo impresso a ogni ritorno. E questi sono i principali fenomeni dei suoni.

**Fine della Sezione VIII. Nel testo originale segue la Sezione IX, *De motu circulari fluidorum*.**

---
## Apparato

### A.0 Estensioni del glossario

I termini seguenti non comparivano nel glossario comune né in quello del Libro II. Ognuno è reso in modo costante in tutto il fascicolo.

| Latino | Italiano | Motivazione |
|---|---|---|
| *pulsus* | «pulsazione» | Decisione del curatore. Nota N2 alla prima occorrenza (II.S8.06): non è l’*impulsus* della Prop. I del Libro I («impulso unico ma grande»), cioè un’azione istantanea che cambia la quantità di moto, ma la regione di condensazione che avanza nel mezzo; oggi diremmo «impulso d’onda» o «fronte d’onda». Motte «pulse». |
| *corpus tremulum*; *tremor* | «corpo tremulo»; «tremito» | Si conserva il lessico storico, distinto da *vibratio* («vibrazione», glossario), che Newton riserva al moto delle parti del mezzo (Prop. XLVII). «Corpo vibrante» avrebbe confuso le due parole. Motte «tremulous body», «tremor». |
| *propagare*; *divaricare* | «propagare»; «divaricarsi» | *Divaricare* (Prop. XLI) è l’aprirsi a ventaglio della pressione dalla linea retta; Motte «deflect». «Divaricarsi» conserva l’immagine latina. |
| *medium elasticum / non elasticum*; *condensatio*; *rarefactio*; *relaxatio*, *se relaxare*; *contractio*, *dilatatio*; *expansio* | «mezzo elastico / non elastico»; «condensazione»; «rarefazione»; «rilassamento», «rilassarsi»; «contrazione», «dilatazione»; «espansione» | Lessico della compressione, reso parola per parola. *Expansio* nella Prop. XLVII è la lunghezza attuale della lineetta (εγ), cioè la grandezza che varia inversamente alla densità. |
| *frustum* (*conicum*) | «tronco» (di cono) | Prop. XLI, Cor.; Motte «frustum». |
| *jugum*; *vallis*; *culmen*; *undarum partes altissimæ* | «cresta»; «valle»; «sommità»; «le parti più alte delle onde» | Prop. XLII e XLVI. *Vallis* è femminile in latino e in italiano. |
| *latitudo* (*undarum*, *pulsus*) | «larghezza» | Calco del latino, come Motte «breadth». Nelle note: è la **lunghezza d’onda** (Prop. XLVI: distanza fra due creste o fra due valli; Prop. L e Scolio: distanza fra due pulsazioni). |
| *punctum physicum*; *lineola physica*; *pars linearis* | «punto fisico»; «lineetta fisica»; «parte lineare» | Prop. XLVII: elementi del mezzo abbastanza piccoli da trattarsi come punti e segmenti, ma materiali. *Lineola* come nei fascicoli del Libro I (diminutivo reso con «lineetta»). |
| *motus reciprocus*; *vices*, *vicibus alternis*; *reciprocatio* | «moto reciproco»; «alternanze», «alternativamente»; «alternanza» | «Moto reciproco» (moto di andata e ritorno) è termine tecnico della meccanica classica; *vices* della Prop. XLIV, Cor. 1 è reso «alternanze». |
| *centrum oscillationis*; *punctum suspensionis*; *corpus pendulum* | «centro di oscillazione»; «punto di sospensione»; «corpo pendolo» | «Corpo pendolo» come nel Fascicolo 9 (Prop. LI–LII del Libro I). |
| *oscillatio* / *oscillatio integra ex itu & reditu composita* | «oscillazione» / «oscillazione intera, composta di andata e ritorno» | Newton distingue l’oscillazione semplice (una sola andata: Propp. XLIV, XLVI) dall’oscillazione intera (andata e ritorno: Prop. XLIX, Scolio). La distinzione è decisiva per i conti (nota N8) ed è mantenuta parola per parola. |
| *crus* (*canalis*) | «braccio» (del canale) | Prop. XLIV; Motte «legs». |
| *isochronus* | «isocrono» | Prop. XLIV, Cor. 1. |
| *urgere* | «spingere» (parti a contatto); «sollecitare» (con soggetto una forza) | In questa Sezione *urgere* e *premere* compaiono insieme (*urgebitur & premetur*, Prop. XLI, Cor.): per tenerli distinti, *premere* è «premere» e *urgere* «spingere». Con soggetto *vis* (Prop. XLIX: *urgeatur … a vi elastica*) si conserva «sollecitare», come nel Fascicolo 3 (Cor. VI). |
| *impellere* | «spingere» | Prop. XLIX (*impellent*, *impelluntur*). |
| *plaga* | «direzione» (Propp. XLIII, XLVII) | Il glossario dà «parte». Qui *plaga motus* è la direzione del moto (*ABC plagam motus pulsuum*, *secundum plagam aliquam certam & determinatam*): «parte del moto» sarebbe oscuro. Dubbio segnalato al coordinatore. |
| *exponere* | «rappresentare» | Prop. XLVII (*exponatur tempus*): una grandezza rappresentata da un’altra, come *exponens* nel Fascicolo 5. |
| *pondus specificum* | «peso specifico» | Scolio. È diverso da *gravitas specifica* («gravità specifica», glossario), che in questa Sezione non compare. |
| *incumbens pondus*; *aer uniformis*; *medium homogeneum* | «peso sovrastante»; «aria uniforme»; «mezzo omogeneo» | Prop. XLIX e Scolio: la colonna d’aria a densità costante che equilibra la pressione (l’«atmosfera omogenea»). |
| *crassitudo* (*particularum*) | «spessore» | Scolio; Motte «crassitude». |
| *aer verus*; *vapores*; *elater*; *tonus* | «aria vera»; «vapori»; «elasticità»; «tono» | Scolio. *Elater* (molla) è la forza elastica dell’aria nel lessico di Boyle; reso «elasticità» per non creare un doppione con *vis elastica*. |
| *fistula aperta*; *chorda*; *tympanum*; *tubus stenterophonicus* | «canna aperta»; «corda»; «tamburo»; «tromba stentorofonica» | Scolio. La tromba stentorofonica è il portavoce di Samuel Morland (nota N13, non verificato sulle fonti allegate). |
| *digitus Anglicus*; *pes Anglicus*; *minutum primum*; *hora* | «pollice inglese»; «piede inglese»; «minuto»; «ora» | Unità non previste dal glossario; *minutum secundum* resta «secondo». |
| *D.* (*D. Sauveur*) | «il signor» | *Dominus*; Motte «M.». |
| *hallucinari* | «ingannarsi» | Prop. XLIII, Cor. |
| *in instanti* | «in un istante» | Prop. XLIII e Scolio. |
| *ex æquo* | *ex æquo* (in corsivo) | Termine tecnico delle proporzioni (composizione per uguaglianza dei rapporti intermedi); Motte lo conserva. |

*Impulsus* non compare in questa Sezione; *impetus* compare tre volte (Prop. XLI, Cor.: *eodem impetu*, due volte; Prop. XLVII, Cor.: *ab impetu*, due volte), reso «impeto». *Vis insita*, *medium similare* e *medium rarum* non compaiono.

### A.1 Proposizione XLI

**Latino:** *Pressio non propagatur per fluidum secundum lineas rectas, nisi ubi particulæ fluidi in directum jacent.*

**Inglese:** “A pressure is not propagated through a fluid in rectilinear directions unless where the particles of the fluid lie in a right line.”

**Scelte.**

- *nisi ubi* → «se non dove»; *in directum* → «in linea retta» (glossario).
- *quatenus autem fulciuntur, premunt particulas fulcientes* → «e in quanto sono sostenute, premono le particelle che le sostengono». Motte rende *quatenus* con «but the particles that support them are also pressed by them», cambiando il soggetto.
- *nisi fulciantur ab ulterioribus l & m easque premant*: «se non sono sostenute… e non le premono». Motte «without being supported by, and pressing upon».
- *divaricare incipiet* → «comincerà a divaricarsi»; Motte «begins to deflect towards one hand and the other», con un’aggiunta esplicativa.
- **Corollario.** *quaquaversum* → «in ogni direzione»; Motte «towards any part», resa debole. *coniformem* → «di forma conica». *frusta* → «tronchi».
- *per corol. VI. prop. XIX.*: la Prop. XIX del Libro II (Sezione V) **non ha un Cor. VI**: ha sette casi e un solo corollario. Il contenuto citato (un fluido non premuto ugualmente da ogni parte cede alla pressione più forte) è il **Caso 6** della Prop. XIX. Motte scrive correttamente «by Case 6, Prop. XIX». Nel testo tradotto: «per il Cor. VI [*sic*: Caso 6] della Prop. XIX». Da controllare sulla stampa (§ A.14).
- *Frustum igitur aegf*: le altre occorrenze dello stesso tronco sono *degf* e *defg*; **aegf** è refuso probabile della trascrizione (Motte «degf»).
- *cum rigidum non sit, sed omnimodo fluidum* → «poiché non è rigido, ma fluido in ogni senso»; Motte «being not in the least tenacious or hard, but perfectly fluid»: amplia (*tenacious*) e intensifica.
- *conus ABC* (*interea dum conus ABC … urget*): così anche Motte. Il cono che preme sulla superficie de dovrebbe essere il cono Ade (come poco dopo, *inter conum Ade*); ABC indica la parte del cono dietro il foro. Non è chiaro se sia un refuso; lo segnalo senza correggere.

### A.2 Proposizione XLII

**Latino:** *Motus omnis per fluidum propagatus divergit a recto tramite in spatia immota.*

**Inglese:** “All motion propagated through a fluid diverges from a rectilinear progress into the unmoved spaces.”

**Scelte.**

- *a recto tramite* → «dal cammino rettilineo».
- **Caso 1.** *defluet eadem de partibus illis immotis undarum valles*: manca una preposizione (*in undarum valles*); la traduzione integra «[nelle]». Motte «run down into those hollows».
- **Omissione di Motte:** *Defluxu priore undarum juga, posteriore valles hinc inde dilatantur* → Motte «By the first deflux the ridges of the waves will dilate themselves this way and that way»: **manca il secondo membro**, quello delle valli (*posteriore valles*).
- *ideoque celerior non est quam pro celeritate descensus* → «e perciò non è più veloce di quanto comporti la velocità della discesa»; Motte «cannot be swifter than in proportion to the celerity of the descent».
- *fluidi partibus immotis LK, NO*: la prima volta il latino ha **LK**, poi sempre **KL**; Motte «KL». Variante d’ordine senza conseguenze.
- *rfgr, shis, tklt, vmnv, &c* senza punto finale: punteggiatura.
- **Caso 2.** Prima occorrenza di *pulsus*: nota N2. *Pulsus propagari concipe*: imperativo di seconda persona, reso «Immagina». *versus antecedentia intervalla rariora* → «verso gli intervalli più radi che stanno loro davanti»: qui *antecedentia* non è il termine tecnico *in antecedentia* del glossario.
- *eadem fere celeritate* → «con quasi la stessa velocità»; Motte «with very near the same celerity», poi «with almost the same celerity».
- *Hoc experimur in sonis, qui vel monte interposito audiuntur, vel …*: «che si odono anche con un monte interposto, oppure…».
- **Caso 3.** *partes medii … urgent commoventque partes ulteriores* → «spingono e mettono in moto»; Motte «disturb and agitate».

### A.3 Proposizione XLIII

**Latino:** *Corpus omne tremulum in medio elastico propagabit motum pulsuum undique in directum; in medio vero non elastico motum circularem excitabit.*

**Inglese:** “Every tremulous body in an elastic medium propagates the motion of the pulses on every side right forward; but in a non-elastic medium excites a circular motion.”

**Scelte.**

- Il latino ha *Cas. 1.* ma **non** un *Cas. 2.*: il secondo capoverso comincia con *Quod si medium non sit elasticum*. **Motte aggiunge l’etichetta «CASE 2.»**. Nella traduzione il capoverso II.S8.10 resta senza etichetta, come nel latino.
- *itu suo urgebunt & propellent* → «con la loro andata spingeranno e sospingeranno»; Motte «do in going urge and drive before them», e aggiunge «by that **impulse** compress».
- *sic enim determinatas ab invicem distantias servando*: «distanze determinate», aggettivo, non *determinatio*.
- *ob motum suum progressivum, quo feriunt obstacula, sunt pulsus*: «per il loro moto progressivo con cui urtano gli ostacoli, sono le pulsazioni»: il motivo del nome *pulsus* (da *pellere*, colpire) è dato dal testo stesso (nota N2).
- *Nam gravitas undarum supplet locum vis elasticæ* → «la gravità delle onde fa le veci della forza elastica»; Motte «the gravity of the water».
- *Et quamvis corpus tremulum non sit firmum* → «non è saldo»; Motte «be not firm **and hard**» (aggiunta).
- *magnitudine datum* → «dato di grandezza» (glossario).
- **Cor.** *Hallucinantur … qui credunt* → «Si ingannano … coloro che credono»; Motte «It is a mistake … to think, **as some have done**»: l’inciso esplicita il bersaglio polemico.

### A.4 Proposizione XLIV

**Latino:** *Si aqua in canalis cruribus erectisKL, MN vicibus alternis ascendat & descendat; construatur autem pendulum cujus longitudo inter punctum suspensionis & centrum oscillationis æquetur semissi longitudinis aquæ in canali: dico quod aqua ascendet & descendet iisdem temporibus quibus pendulum oscillatur.*

**Inglese:** “If water ascend and descend alternately in the erected legs KL, MN, of a canal or pipe; and a pendulum be constructed whose length between the point of suspension and the centre of oscillation is equal to half the length of the water in the canal; I say, that the water will ascend and descend in the same times in which the pendulum oscillates.”

**Scelte.**

- *erectisKL*: spazio mancante nella trascrizione (artefatto).
- *cruribus erectis* → «bracci verticali»; Motte «erected legs». **Aggiunta di Motte:** «of a canal **or pipe**».
- *RPQSS cyclois*: la S doppia è refuso probabile della trascrizione; Motte «RPQS». La cicloide è percorsa da R (estremo) per P (punto più basso) e Q fino a S.
- *VP seu PR*: nel pendolo cicloidale la lunghezza del filo VP è uguale alla semicicloide PR (Cor. 2 della Prop. LII del Libro I, Fascicolo 9: «come dimostrò Huygens»). Newton lo usa senza citarlo.
- *per corol. prop. LI.*: il latino non dice *lib. I.*, ma la Prop. LI del Libro II (Sezione IX) tratta dei vortici: il rimando è alla **Prop. LI del Libro I**, il cui corollario dà esattamente la forza tangenziale nella cicloide (§ A.15). Integrazione «[del Libro I]».
- *pondus P* → «il peso P»: Newton chiama «peso» il corpo pendolo.
- *motu reciproco simul eant & redeant* → «vadano e tornino insieme con moto reciproco».
- **Cor. 2.** «619» = 6 1/9; «3118» = 3 1/18 (frazioni appiattite). Motte stampa entrambe come immagini (SVG 922, 923). «feet of French measure» per *pedum Parisiensium*.

### A.5 Proposizione XLV

**Latino:** *Undarum velocitas est in subduplicata ratione latitudinum.*

**Inglese:** “The velocity of waves is in the subduplicate ratio of the breadths.”

Nessuna difficoltà. *Consequitur ex constructione propositionis sequentis* → «Segue dalla costruzione della proposizione seguente».

### A.6 Proposizione XLVI

**Latino:** *Invenire velocitatem undarum.*

**Inglese:** “To find the velocity of waves.”

**Scelte.**

- *Undarum latitudinem voco mensuram transversam, quæ vel vallibus imis, vel summis culminibus interjacet* → «la misura trasversale che sta fra i fondi delle valli, oppure fra le sommità più alte». Motte «lying between the deepest part of the hollows, or the tops of the ridges» è ambiguo (sembra «fra le valli e le creste»), mentre il latino intende la distanza fra due valli o fra due creste.
- *si distantiæ … æquentur duplæ penduli longitudini* → «uguali al doppio della lunghezza del pendolo»; Motte «of **any** pendulum».
- *inter transitum undarum singularum* → «fra il passaggio di un’onda e quello della successiva».
- **Cor. 1.** «3118» = 3 1/18; «18313» = 183 1/3 (Motte SVG 923, 924). *minuti unius primi* → «un minuto»; *horæ spatio* → «nello spazio di un’ora».
- *ex hypothesi quod partes aquæ recta ascendunt vel recta descendunt* → «salgano in linea retta e scendano in linea retta». *verius fit per circulum* → «avviene più veramente lungo un cerchio»: è l’osservazione che le particelle d’acqua descrivono orbite circolari (nota N7).
- *non nisi quamproxime* → «soltanto con ottima approssimazione»; Motte «as only near the truth».

### A.7 Proposizione XLVII

**Latino:** *Pulsibus per fluidum propagatis, singulæ fluidi particulæ, motu reciproco brevissimo euntes & redeuntes, accelerantur semper & retardantur pro lege oscillantis penduli.*

**Inglese:** “If pulses are propagated through a fluid, the several particles of the fluid, going and returning with the shortest reciprocal motion, are always accelerated or retarded according to the law of the oscillating pendulum.”

**Scelte.**

- Intestazione abbreviata nella trascrizione: *PROP. XLVII. THEOR. XXXVII.* (le altre proposizioni hanno *PROPOSITIO … THEOREMA …*). Resa con il titolo pieno «Proposizione XLVII. Teorema XXXVII».
- L’ablativo assoluto *Pulsibus … propagatis* è reso «Quando si propagano pulsazioni»; Motte «If pulses are propagated». *accelerantur … & retardantur*: Motte «accelerated **or** retarded».
- La figura è segnata **[FIG 60]**, fuori sequenza (le figure della Sezione vanno da 63 a 71, e la Prop. XLIX ha [FIG 71]): probabilmente [FIG 70]. Segnalato in § A.12.
- *ABC plagam motus pulsuum* → «ABC la direzione del moto delle pulsazioni» (§ A.0, *plaga*).
- *Per hujus circumferentiam totam cum partibus suis exponatur tempus totum vibrationis unius cum ipsius partibus proportionalibus* → «Con la sua circonferenza intera e con le sue parti si rappresenti il tempo intero…». È il «cerchio di riferimento» del moto armonico (nota N9).
- *vel ipsis Pl, Pn, Pm in punctorum reditu*: l’ordine atteso è **Pl, Pm, Pn** (in parallelo a PL, PM, PN); Motte «Pl, Pm, Pn». Inversione nella trascrizione o nella stampa, segnalata con «[*sic*]».
- Formule appiattite, lette così (Motte le stampa come immagini, SVG 935–941): «1V−IM ad 1V» = 1/(V − IM) a 1/V; «1V+im» = 1/(V + im); «1V−HL & 1V−KN» = 1/(V − HL) e 1/(V − KN); «HL−KNVV−V×HL−V×KN+HL×KN ad 1V» = (HL − KN)/(VV − V×HL − V×KN + HL×KN) a 1/V; «HL−KNVV ad 1V» = (HL − KN)/VV a 1/V. Le letture sono confermate dall’algebra e dalle immagini SVG 935–941 di Motte, che coincidono: 1/(V − HL) − 1/(V − KN) = (HL − KN)/((V − HL)(V − KN)) e (V − HL)(V − KN) = VV − V×HL − V×KN + HL×KN.
- *ob proportionales HL−KN ad HK, & OM ad OI vel OP*: «poiché HL − KN sta a HK come OM sta a OI, o a OP». Motte «because HL − KN is proportional to HK, and OM to OI or OP» fraintende la costruzione: non sono due proporzionalità, ma l’uguaglianza di due rapporti.
- *Ff bisecetur in Ω*: Ω è il punto medio della vibrazione di F (Motte SVG 942).
- *vis acceleratrix lineolæ physicæ εγ, est ut ipsius distantia a medio vibrationis loco Ω* → «la forza acceleratrice della lineetta fisica εγ è come la sua distanza dal luogo medio della vibrazione Ω». Newton scrive la distanza Ωφ: quella del punto φ, centro della lineetta εγ.
- *per prop. XXXVIII. lib. I.* → «per la Prop. XXXVIII del Libro I»: verificato (§ A.15).
- *estque par ratio partium omnium linearium* → «e lo stesso vale per tutte le parti lineari».
- **Cor.** *neque multiplicatur in eorum progressu* → «e non si moltiplica nel loro avanzare».

### A.8 Proposizione XLVIII

**Latino:** *Pulsuum in fluido elastico propagatorum velocitates sunt in ratione composita ex subduplicata ratione vis elastiæ directe & subduplicata ratione densitatis inverse; si modo fluidi vis elastica ejusdem condensationi proportionalis esse supponatur.*

**Inglese:** “The velocities of pulses propagated in an elastic fluid are in a ratio compounded of the subduplicate ratio of the elastic force directly, and the subduplicate ratio of the density inversely; supposing the elastic force of the fluid to be proportional to its condensation.”

**Scelte.**

- *elastiæ*: refuso probabile della trascrizione per *elasticæ*.
- *media homogenea* (Casi 1 e 2) → «mezzi omogenei»: qui significa mezzi della stessa natura, cioè di pari densità e forza elastica (lo dice il Caso 3, *In mediis igitur densitate & vi elastica paribus*), non mezzi internamente uniformi.
- *dilationes* (tre volte nel Caso 1, accanto a *dilatationes* del Caso 2): forma anomala, probabilmente refuso per *dilatationes* della stampa o della trascrizione; resa «dilatazioni».
- *Accurata quidem non est hæc proportio* → «Questa proporzione, a dire il vero, non è esatta»; Motte «not that this proportion is perfectly accurate».
- *pro physice accurata haberi potest* → «può essere ritenuta fisicamente esatta»; Motte «physically exact».
- **Caso 2.** *Estque tempus itus & reditus unius …* → Motte «And, **moreover**, the time…» (aggiunta). Il ragionamento: tempo ∝ √(materia × spazio / forza), con forza uguale; materia e spazio entrambi ∝ larghezza, quindi tempo ∝ larghezza.
- **Caso 3.** *tempus, quo motus iidem peragantur ac prius* → «il tempo in cui si compiono gli stessi moti di prima»; Motte «the time which is necessary for producing the same motion as before».

### A.9 Proposizione XLIX

**Latino:** *Datis medii densitate & vi elastica, invenire velocitatem pulsuum.*

**Inglese:** “The density and elastic force of a medium being given, to find the velocity of the pulses.”

**Scelte.**

- *pro more aëris nostri* → «come accade alla nostra aria»; Motte «after the manner of our air».
- *pulsus eundo conficiet spatium* → «la pulsazione, andando, percorrerà uno spazio»; Motte «will be propagated right onwards through a space».
- *stantibus quæ in propositione XLVII. constructa sunt* → «restando ferma la costruzione della Prop. XLVII».
- *si linea quævis physica EF … urgeatur … a vi elastica* → «è sollecitata … da una forza elastica» (§ A.0). Poco dopo il latino passa da EF a **EG** (*lineola physica EG*): nella Prop. XLVII la lineetta su cui si calcola la forza è proprio EG (con centro F); il passaggio è di Newton, non della trascrizione, perché Motte ha lo stesso.
- «12PS» = ½PS (frazione appiattita; Motte SVG 944).
- *urgente vi ponderis* → «sotto l’azione della forza del peso»; **Motte** «produced by the **impulse** of the weight» (aggiunta).
- *in subduplicata ratione VV ad PO×A, & subduplicata ratione PO ad A conjunctim* → «considerati congiuntamente»; *in ratione integra V ad A* → «nel rapporto intero di V ad A».
- **Errore di Motte:** *Sed tempore vibrationis unius ex itu & reditu compositæ, pulsus progrediendo conficit latitudinem suam BC* → Motte «But in the time of one vibration composed of the going and returning **of the pendulum**, the pulse…». Nel latino la vibrazione è quella della lineetta del mezzo (Prop. XLVII), non del pendolo: l’aggiunta di Motte confonde le due grandezze che la dimostrazione sta appunto confrontando.
- **Cor. 1.** *gravia æqualiter accelerato motu cadendo* → «cadendo con moto uniformemente accelerato».

### A.10 Proposizione L

**Latino:** *Invenire pulsuum distantias.*

**Inglese:** “To find the distances of the pulses.”

Nessuna difficoltà. *pars inventa erit pulsus unius latitudo* → «la parte trovata sarà la larghezza di una pulsazione»: *pars* è il quoziente della divisione.

### A.11 Scolio

**Scelte.**

- *Spectant propositiones novissimæ* → «Le ultime proposizioni riguardano».
- *in actione sola … consistere nequit* → «non può consistere nella sola azione»; **Motte** «it is **certain** that it cannot consist» (aggiunta). Il senso: la luce, che va in linea retta, non può essere soltanto una pressione o un moto propagato nel mezzo, perché per le Propp. XLI–XLII questi si divaricano.
- *in corporibus objectis* → «nei corpi posti di fronte»; Motte «in the bodies near them».
- *in chordas corporibus sonoris unisonas impactos* → «che colpiscono corde all’unisono con i corpi sonori».
- *argenti vivi* → «mercurio (argento vivo)» alla prima occorrenza (glossario); poi *mercurius*, *argentum vivum* → «mercurio».
- Numeri appiattiti: «1323» = 13 2/3; «3915» = 39 1/5; «19034» = 190 3/4; «9799» = 979/9; «10710» = 10 7/10 (Motte SVG 945–949). Le letture sono confermate dall’aritmetica (nota N11).
- *digitorum Anglicorum 30* → «30 pollici inglesi»; Motte «30 inches **of our measure**»; *pedum Anglicorum* → Motte «feet of our measure».
- *aërem nostrum subjectum comprimere posset* → «potrebbe comprimere la nostra aria sottostante»; Motte «sufficient to compress our air to the density we find it to be of» (ampliamento esplicativo).
- *uti notum est* → «come è noto»; Motte «as is commonly known».
- *crassitudinis solidarum particularum aëris, per quam sonus utique propagatur in instanti* → «attraverso il quale il suono si propaga certamente in un istante».
- *vapores … cum sint alterius elateris & alterius toni* → «di altra elasticità e di altro tono»; Motte «of another spring, and a different tone». *vix aut ne vix quidem* → «a stento, o neppure a stento»; Motte «hardly, if at all». *in subduplicata ratione minoris materiæ* → «in rapporto subduplicato della minore materia»; Motte «of the defect of the matter».
- *ubi aër per calorem temperatum rarescit* → «per il calore moderato»; Motte «by the gentle warmth of those seasons».
- *plus minus 1142* → «più o meno 1142»; Motte «about».
- *D. Sauveur* → «il signor Sauveur»; Motte «M. Sauveur». *chordæ* → «corda»; Motte «a **viol**-string» (aggiunta).
- *tempore minuti minus secundi centies recurrit*: **minus** è refuso probabile per *unius* (*minuti unius secundi*, formula costante nella Sezione); Motte «a hundred times in one second». La traduzione segue il senso con «[*sic*]».
- *versimile*: refuso probabile per *verisimile*.
- *tubis stenterophonicis*: grafia della trascrizione (da Stentore ci si aspetterebbe *stentorophonicis*); Motte «speaking-trumpets». Da controllare sulla stampa, senza conseguenze sul senso.
- *patet ex corollario propositionis XLVII. libri hujus* → «dal corollario della Prop. XLVII di questo libro»: il latino dice esplicitamente «di questo libro», e la traduzione lo conserva.

### A.12 Refusi e anomalie della trascrizione

| Luogo | Trascrizione | Lettura | Tipo |
|---|---|---|---|
| II.S8.03 | *aegf* | *degf* | refuso probabile |
| II.S8.03 | *per corol. VI. prop. XIX.* | *per cas. 6. prop. XIX.* (Motte «Case 6») | rimando errato (stampa o trascrizione) |
| II.S8.05 | *de partibus illis immotis undarum valles* | *… in undarum valles* | omissione probabile di *in* |
| II.S8.05 | *rfgr, shis, tklt, vmnv, &c* | — | punteggiatura |
| II.S8.12 | *erectisKL* | *erectis KL* | spaziatura |
| II.S8.13 | *RPQSS* | *RPQS* | refuso probabile |
| II.S8.15, II.S8.22 | *619*, *3118*, *18313* | 6 1/9, 3 1/18, 183 1/3 | frazioni appiattite |
| prima di II.S8.25 | *PROP. XLVII. THEOR. XXXVII.* | *PROPOSITIO XLVII. THEOREMA XXXVII.* | intestazione abbreviata (segnalata dal coordinatore) |
| II.S8.26 | *[FIG 60]* | probabilmente [FIG 70] | numerazione fuori sequenza |
| II.S8.26 | *ef,fg* | *ef, fg* | spaziatura |
| II.S8.27 | *Pl, Pn, Pm* | *Pl, Pm, Pn* | ordine invertito |
| II.S8.27 | *1V−IM*, *1V+im*, *1V−HL*, *1V−KN*, *1V* | 1/(V−IM) ecc. | frazioni appiattite |
| II.S8.27 | *HL−KNVV−V×HL−V×KN+HL×KN*; *HL−KNVV* | (HL−KN)/(VV−V×HL−V×KN+HL×KN); (HL−KN)/VV | frazioni appiattite |
| II.S8.29 | *elastiæ* | *elasticæ* | refuso probabile |
| II.S8.30 | *dilationes*, *dilationibus* (tre volte) | *dilatationes* | forma anomala, da verificare |
| II.S8.36 | *12PS* | ½PS | frazione appiattita |
| II.S8.41–II.S8.46 | *1323*, *3915*, *19034*, *9799*, *10710* | 13 2/3, 39 1/5, 190 3/4, 979/9, 10 7/10 | frazioni appiattite |
| II.S8.46 | *minuti minus secundi* | *minuti unius secundi* | refuso probabile |
| II.S8.46 | *versimile* | *verisimile* | refuso probabile |
| II.S8.47 | *stenterophonicis* | *stentorophonicis*? | grafia da controllare |

La traduzione segue il senso; la Parte B riporta il latino esatto della trascrizione.

### A.13 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| II.S8.02 | *quatenus autem fulciuntur, premunt particulas fulcientes* | «but the particles that support them are also pressed by them» | soggetto cambiato |
| II.S8.02 | *divaricare incipiet* | «begins to deflect towards one hand and the other» | ampliamento |
| II.S8.03 | *quaquaversum* | «towards any part» | resa debole |
| II.S8.03 | *per corol. VI. prop. XIX.* | «by Case 6, Prop. XIX» | **Motte corretto**, il latino no |
| II.S8.03 | *aegf* | «degf» | Motte ha la lettura attesa |
| II.S8.03 | *cum rigidum non sit, sed omnimodo fluidum* | «being not in the least tenacious or hard, but perfectly fluid» | ampliamento |
| II.S8.03 | *eodem impetu* | «with the same force» | *impetus* reso «force» |
| II.S8.05 | *Defluxu priore undarum juga, posteriore valles* | «By the first deflux the ridges» | **omissione** delle valli |
| II.S8.05 | *LK* | «KL» | ordine delle lettere |
| II.S8.07 | *urgent commoventque* | «disturb and agitate» | resa libera |
| II.S8.09 | *urgendo compriment* | «by that **impulse** compress» | aggiunta |
| II.S8.10 | (nessuna etichetta) | «CASE 2.» | aggiunta |
| II.S8.10 | *non sit firmum* | «be not firm and hard» | aggiunta |
| II.S8.11 | *Hallucinantur … qui credunt* | «It is a mistake … to think, as some have done» | aggiunta |
| II.S8.12 | *in canalis cruribus* | «of a canal or pipe» | aggiunta |
| II.S8.13 | *RPQSS* | «RPQS» | Motte ha la lettura attesa |
| II.S8.15, II.S8.22 | *Parisiensium*, *Parisienses* | «of French measure», «French feet» | resa |
| II.S8.21 | *quæ vel vallibus imis, vel summis culminibus interjacet* | «lying between the deepest part of the hollows, or the tops of the ridges» | ambiguo |
| II.S8.21 | *duplæ penduli longitudini* | «twice the length of **any** pendulum» | aggiunta |
| II.S8.25 | *accelerantur semper & retardantur* | «accelerated or retarded» | congiunzione |
| II.S8.26 | *ABC plagam motus* | «ABC the line of direction of the motion» | ampliamento |
| II.S8.27 | *Pl, Pn, Pm* | «Pl, Pm, Pn» | Motte ha l’ordine atteso |
| II.S8.26 | φ (luogo intermedio di F) | SVG 926: «π» | **refuso** dell’edizione 1846 |
| II.S8.27 | *ob proportionales HL−KN ad HK, & OM ad OI vel OP* | «because HL − KN is proportional to HK, and OM to OI or OP» | **fraintendimento** (due proporzionalità invece di un’uguaglianza di rapporti) |
| II.S8.31 | *Estque tempus* | «And, moreover, the time» | aggiunta |
| II.S8.36 | *urgente vi ponderis* | «produced by the impulse of the weight» | aggiunta |
| II.S8.36 | *tempore vibrationis unius ex itu & reditu compositæ* | «… composed of the going and returning **of the pendulum**» | **errore**: la vibrazione è della lineetta, non del pendolo |
| II.S8.41 | *consistere nequit* | «it is certain that it cannot consist» | aggiunta |
| II.S8.41 | *digitorum Anglicorum*, *pedum Anglicorum* | «inches of our measure», «feet of our measure» | resa |
| II.S8.41 | *aërem nostrum subjectum comprimere posset* | «sufficient to compress our air to the density we find it to be of» | ampliamento |
| II.S8.46 | *chordæ* | «a viol-string» | aggiunta |
| II.S8.46 | *minuti minus secundi* | «in one second» | Motte ha la lettura attesa |

**Formule SVG di Motte (922–949), controllate.** Le 28 immagini della sezione sono state rese con `rsvg-convert` dall’EPUB (`OEBPS/3191938728343764116_n.svg`) e lette una per una. **27 su 28 coincidono** con la lettura del latino (comprese tutte le frazioni appiattite della trascrizione, che risultano così confermate). **Una non torna:**

| SVG | Luogo | Latino | Motte 1846 (immagine) | Esito |
|---|---|---|---|---|
| 926 | Prop. XLVII, II.S8.26 (elenco dei luoghi intermedi «ε, φ, γ») | φ | **π** | **refuso dell’edizione 1846** (o della sua composizione delle formule): il punto è φ, come mostrano 928, 929, 931, 943 (εφ, φγ, Fφ, Ωφ) |

| SVG | Luogo | Immagine | Coincide con il latino |
|---|---|---|---|
| 922 | Prop. XLIV, Cor. 2 | 6 1/9 | sì |
| 923 | Prop. XLIV, Cor. 2; Prop. XLVI, Cor. 1 | 3 1/18 | sì |
| 924 | Prop. XLVI, Cor. 1 | 183 1/3 | sì |
| 925, 927 | Prop. XLVII | ε, γ | sì |
| 928, 929 | Prop. XLVII | εφ, φγ | sì |
| 930, 931, 932 | Prop. XLVII | Eε, Fφ, Gγ | sì |
| 933 | Prop. XLVII e Cor. | εγ | sì |
| 934 | Prop. XLVII | EG + Gγ − Eε | sì |
| 935, 936, 937 | Prop. XLVII | 1/(V − IM), 1/V, 1/(V + im) | sì |
| 938, 939 | Prop. XLVII | 1/(V − HL), 1/(V − KN) | sì |
| 940 | Prop. XLVII | (HL − KN)/(VV − V × HL − V × KN + HL × KN) | sì |
| 941 | Prop. XLVII | (HL − KN)/VV | sì |
| 942, 943 | Prop. XLVII | Ω, Ωφ | sì |
| 944 | Prop. XLIX | ½PS | sì |
| 945 | Scolio | 13 2/3 | sì |
| 946 | Scolio | 39 1/5 | sì |
| 947 | Scolio | 190 3/4 | sì |
| 948 | Scolio | 979/9 | sì |
| 949 | Scolio | 10 7/10 | sì |

Controllo doppio: le letture delle immagini coincidono una per una con l’attributo `data-tex` dell’EPUB (tabella `src_epub/svg_tex.tsv`), dove anche la 926 è `\pi`: il refuso è quindi nella sorgente dell’EPUB 1846, non nella resa grafica. SVG non visti: **nessuno**. Motte usa ε (lunato) per il latino ε: differenza solo tipografica.

### A.14 Punti da controllare sulla stampa ECCO

| Pagina 1726 | Trascrizione | Lettura attesa | Motivo |
|---|---|---|---|
| p. 358 | *per corol. VI. prop. XIX.* | *per cas. 6. prop. XIX.* | la Prop. XIX del Libro II ha un solo corollario; il contenuto è il Caso 6; Motte «Case 6» |
| p. 358 | *Frustum igitur aegf* | *degf* | lettere del tronco altrove *degf*, *defg*; Motte «degf» |
| p. 357 | *conus ABC* | *conus ABC* o *Ade*? | il cono che preme su de è altrove *Ade*; anche Motte ABC |
| p. 360 | *defluet eadem de partibus illis immotis undarum valles* | *… in undarum valles* | preposizione mancante |
| p. 363 | *RPQSS cyclois* | *RPQS* | lettera doppia; Motte RPQS |
| p. 364 | *pedum Parisiensium 619*, *pedum 3118* | 6 1/9, 3 1/18 | frazioni appiattite: verificare la forma a stampa |
| p. 366 | *PROP. XLVII. THEOR. XXXVII.* | forma piena? | intestazione abbreviata |
| p. 366 | *[FIG 60]* | figura della Prop. XLVII (n. 70?) | numerazione fuori sequenza |
| p. 367 | *vel ipsis Pl, Pn, Pm* | *Pl, Pm, Pn* | ordine invertito; Motte Pl, Pm, Pn |
| p. 368 | *vis elastiæ* | *elasticæ* | refuso |
| p. 369 | *dilationes* (tre volte) | *dilatationes* | forma anomala |
| p. 373 | *minuti minus secundi* | *minuti unius secundi* | refuso; Motte «in one second» |
| p. 374 | *versimile* | *verisimile* | refuso |
| p. 374 | *stenterophonicis* | *stentorophonicis*? | grafia |

### A.15 Rimandi verificati

| Luogo | Rimando nel latino | Resa | Esito |
|---|---|---|---|
| II.S8.03 | *per motus legem tertiam* | «per la terza legge del moto» | regge (Fascicolo 3, Legge III) |
| II.S8.03 | *per corol. VI. prop. XIX.* (Libro II) | «per il Cor. VI [*sic*: Caso 6] della Prop. XIX» | **non torna**: la Prop. XIX del Libro II (fonte `latino-1726-L2-S05.md`) ha i Casi 1–7 e un solo corollario, che non tratta di questo. Torna il **Caso 6**: «se quel fluido è chiuso in un vaso non rigido e non è premuto ugualmente da ogni parte, cederà alla pressione più forte». I Corollari 1–7 appartengono alla Prop. XX |
| II.S8.09 | *per propositionem præcedentem* | «per la proposizione precedente» | regge (Prop. XLII) |
| II.S8.13 | *per corol. prop. LI.* (Libro I) | «per il Cor. della Prop. LI [del Libro I]» | **regge** (Fascicolo 9, S10.19): la forza che accelera il corpo nella cicloide sta al peso totale come l’arco TR sta all’arco SR. Il corollario è enunciato per la cicloide nel globo con forza proporzionale alla distanza; per la cicloide comune sotto gravità uniforme vale al limite del Cor. 2 della Prop. LII del Libro I |
| II.S8.21 | *per prop. XLIV.* | «per la Prop. XLIV» | regge |
| II.S8.27 | *per prop. XXXVIII. lib. I.* | «per la Prop. XXXVIII del Libro I» | **regge** (Fascicolo 8, S7.19–S7.20): con forza proporzionale alla distanza dal centro, i tempi sono come gli archi del cerchio e gli spazi come i seni versi; quindi la posizione della lineetta, data dalla proiezione L di H su PS, corrisponde al tempo rappresentato dall’arco |
| II.S8.36 | *in propositione XLVII.*, *in demonstratione propositionis XLVII.* | «della Prop. XLVII» | regge |
| II.S8.41 | *per prop. XLI. & XLII.*; *per prop. XLIII.* | «per le Propp. XLI e XLII»; «per la Prop. XLIII» | reggono |
| II.S8.47 | *ex corollario propositionis XLVII. libri hujus* | «dal corollario della Prop. XLVII di questo libro» | regge |

Rimandi al Libro I: **2** (Prop. XXXVIII; Prop. LI, Cor.), entrambi verificati. Rimando interno che non torna: **1** (Prop. XIX, «Cor. VI» per «Caso 6»).

---
## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. Le verifiche numeriche sono state eseguite con due script Python (`verifica.py` e `verifica_p47.py`, conservati in `tmp/19-L2-S8/`). Ciò che deriva da conoscenza generale e non dalle fonti allegate è marcato **(non dalle fonti allegate)**.

### N1. Il disegno della Sezione

La Sezione procede in tre tempi: (1) Propp. XLI–XLIII, qualitative: pressione e moto propagati in un fluido non restano confinati in linea retta, ma si allargano dietro gli ostacoli; (2) Propp. XLIV–XLVI, le onde d’acqua, ricondotte al pendolo attraverso il moto dell’acqua in un canale; (3) Propp. XLVII–L, le pulsazioni in un mezzo elastico: moto armonico delle particelle, velocità di propagazione, distanza fra le pulsazioni. Lo Scolio applica tutto alla luce (per escluderla) e al suono (per calcolarne la velocità). In termini moderni è la prima teoria matematica della propagazione delle onde sonore (non dalle fonti allegate).

### N2. *Pulsus*: «pulsazione», non «impulso»

*Pulsus* (da *pellere*, colpire) indica qui la **regione di condensazione** del mezzo che avanza: Newton lo dice esplicitamente nella Prop. XLIII (II.S8.09: le parti che vanno e, andando, si condensano «sono le pulsazioni», perché urtano gli ostacoli). Non va confuso con l’*impulsus* della Prop. I del Libro I («con un impulso unico ma grande», Fascicolo 5, S2.02), che è un’azione istantanea che cambia la quantità di moto di un corpo, né con l’impulso della fisica moderna (**J** = Δ**p**). La «larghezza» di una pulsazione (*latitudo*) è la distanza fra due pulsazioni successive, cioè, in termini moderni, la **lunghezza d’onda** (Prop. L e Scolio).

### N3. Propp. XLI–XLII: pressione e diffrazione

Il ragionamento della Prop. XLI è corpuscolare: una pressione si trasmette in linea retta soltanto lungo una fila perfettamente allineata di particelle; ogni disallineamento la fa «divaricare». Il Corollario e la Prop. XLII mostrano con l’immagine del foro BC che pressione e moto, passato il foro, invadono anche gli spazi laterali KL, NO. In termini moderni è la **diffrazione**, che per il suono (lunghezze d’onda di metri) è evidente (il suono «che si ode con un monte interposto»), mentre per la luce è piccolissima. Su questo Newton fonda, nello Scolio, l’argomento contro una teoria della luce come semplice pressione o moto del mezzo (non dalle fonti allegate: la diffrazione della luce era già stata osservata da Grimaldi, e la teoria ondulatoria la spiegherà con la piccolezza della lunghezza d’onda).

### N4. Prop. XLIII: mezzo elastico e non elastico

Nel mezzo elastico la compressibilità permette la propagazione per condensazioni successive; in un mezzo incompressibile, invece, il moto si trasmette «in un istante» e il fluido circola attorno al corpo (è il moto di un fluido incompressibile attorno a un corpo che oscilla). Il Corollario sulla fiamma è polemico: non è chiaro dalle fonti allegate contro chi sia rivolto.

### N5. Prop. XLIV: il tubo a U

Con *L* lunghezza totale della colonna d’acqua e *x* lo spostamento del livello (AE), la forza di richiamo è il peso della colonna di altezza 2*x* (il «doppio del peso dell’acqua EABF»), cioè 2*x*/*L* del peso totale. Il moto è quindi armonico con periodo 2π√(*L*/2*g*): lo stesso di un pendolo semplice di lunghezza *L*/2. Il risultato di Newton è **esatto** per un tubo di sezione uniforme e senza attrito (verificato con lo script). Newton lo ricava confrontando la forza con quella del pendolo cicloidale, la cui forza tangenziale è esattamente proporzionale all’arco (Cor. della Prop. LI del Libro I): così l’isocronismo (Cor. 1) è esatto per qualsiasi ampiezza. Nota: se la sezione dei bracci è diversa da quella del tratto orizzontale, la «lunghezza dell’acqua» va pesata con le sezioni; Newton presuppone implicitamente un canale uniforme.

### N6. Prop. XLIV, Cor. 2: i numeri

Il pendolo che batte il secondo (una oscillazione semplice in un secondo) è lungo 3 1/18 piedi parigini; il doppio è 6 1/9 = 55/9: il conto è esatto. In metri (piede parigino ≈ 0,3248 m, non dalle fonti allegate): 3 1/18 piedi ≈ 0,993 m, in ottimo accordo con il valore moderno del pendolo che batte il secondo (≈ 0,994 m, non dalle fonti allegate); il semiperiodo calcolato con *g* = 9,807 m/s² è 0,9995 s.

### N7. Propp. XLV–XLVI: la velocità delle onde

Newton tratta la cresta che scende e la valle che sale come l’acqua del canale: la distanza fra cresta e valle (λ/2, se λ è la larghezza dell’onda) fa le veci della lunghezza dell’acqua, e quindi il pendolo equivalente ha lunghezza λ/4 (Prop. XLIV). La cresta diventa valle in un’oscillazione semplice di questo pendolo; un intero periodo dell’onda dura due oscillazioni, cioè quanto una sola oscillazione semplice del pendolo di lunghezza quadrupla, λ. Ne segue *v* = λ/(π√(λ/*g*)) = √(*g*λ)/π: la velocità cresce come la radice della larghezza (Prop. XLV).

**Controlli.**
- Cor. 1: 3 1/18 × 60 = 183 1/3 piedi al minuto; × 3600 = 11000 piedi all’ora, esattamente. Il «*quamproxime*» di Newton riguarda la teoria, non l’aritmetica.
- **Confronto moderno (non dalle fonti allegate).** Per onde di gravità in acqua profonda *v* = √(*g*λ/2π). Il rapporto fra la formula di Newton e quella moderna è √(2/π) ≈ 0,80: Newton sottostima la velocità del 20 % circa. Per λ ≈ 0,993 m la sua formula dà 0,99 m/s, quella moderna 1,25 m/s. Newton stesso avverte che il risultato è approssimato, perché le particelle si muovono «più veramente lungo un cerchio» (II.S8.24): è proprio il moto orbitale circolare delle particelle nelle onde in acqua profonda, che la teoria successiva confermerà.

### N8. Oscillazione semplice e oscillazione intera

Nelle Propp. XLIV e XLVI «oscillazione» è l’oscillazione **semplice** (una sola andata, mezzo periodo moderno): il pendolo di 3 1/18 piedi «oscilla nel tempo di un secondo». Nella Prop. XLIX e nello Scolio Newton specifica invece l’oscillazione **intera, composta di andata e ritorno** (un periodo moderno): il pendolo di 39 1/5 pollici la compie in due secondi. La traduzione conserva la distinzione parola per parola, perché ogni conto della Sezione dipende da essa.

### N9. Prop. XLVII: il moto armonico delle particelle

Il cerchio SIPi di diametro PS = Ee è il **cerchio di riferimento** del moto armonico: il punto H gira uniformemente, e la sua proiezione L su PS dà la posizione del punto fisico E. In termini moderni lo spostamento è ξ(*x*, *t*) = *a* cos(ω*t* − *kx*), con *k* = 2π/BC = 1/V (V è il raggio del cerchio di circonferenza BC: in termini moderni V = λ/2π). L’espansione della lineetta EG è proporzionale a 1 + ∂ξ/∂*x*; con la legge di Boyle (forza elastica inversamente proporzionale all’espansione, ipotesi della Prop. XLVIII) la differenza delle pressioni agli estremi, al primo ordine, è proporzionale a −ξ: forza di richiamo proporzionale alla distanza dal centro della vibrazione, quindi moto di pendolo (Prop. XXXVIII del Libro I).

**Il passaggio critico** è l’approssimazione «HL e KN indefinitamente minori di V»: Newton trascura i termini del secondo ordine nello spostamento. L’argomento è una **verifica di coerenza**: suppone il moto armonico («Immaginiamo dunque che il mezzo sia messo in moto in questo modo») e mostra che le forze elastiche lo mantengono; non dimostra che ogni moto del mezzo debba essere di questo tipo. Questa obiezione è classica (non dalle fonti allegate).

**Verifica numerica.** Con ξ = *a* cos(ω*t* − *kx*), λ = 1, lineetta di semilarghezza *h* = λ/50 e pressione inversamente proporzionale all’espansione, ho calcolato il rapporto fra la differenza delle pressioni agli estremi e lo spostamento −ξ del centro in 19 istanti. Il rapporto risulta costante entro lo 0,2 % per *a* = 10⁻⁴ (1,5731–1,5769, contro il valore teorico 2*hk*² = 1,579), entro il 2 % per *a* = 10⁻³ e varia del 25 % per *a* = 10⁻²: la legge del pendolo vale nel limite delle piccole vibrazioni, esattamente come Newton suppone.

### N10. Propp. XLVIII–XLIX: la velocità √(*p*/ρ)

La Prop. XLVIII è un argomento di similitudine: velocità ∝ √(forza elastica / densità). La Prop. XLIX dà la costante: la pulsazione percorre la circonferenza 2π*A* nel tempo di un’oscillazione intera del pendolo di lunghezza *A*, cioè 2π√(*A*/*g*); quindi *v* = √(*gA*). Poiché il peso della colonna omogenea di altezza *A* uguaglia la pressione, *gA* = *p*/ρ e *v* = √(*p*/ρ): è la **formula di Newton** (velocità isoterma). Il Cor. 1 lo dice in altra forma: un grave che cade da *A*/2 acquista la velocità √(2*g* · *A*/2) = √(*gA*); e il tempo di quella caduta, √(*A*/*g*), sta al periodo 2π√(*A*/*g*) come il raggio alla circonferenza (verificato).

**Verifica numerica.** Ho simulato una catena lagrangiana di 4000 strati di gas con pressione inversamente proporzionale al volume (legge di Boyle, *p* = ρ = 1) e una piccola perturbazione gaussiana: il massimo di compressione avanza con velocità 0,9995, contro √(*p*/ρ) = 1. La Prop. XLIX è corretta **nell’ipotesi di Newton** (forza elastica proporzionale alla condensazione).

### N11. Scolio: ricalcolo della velocità del suono

Ricalcolo con lo script di tutti i numeri di Newton:

| Passo | Newton | Ricalcolo | Esito |
|---|---|---|---|
| peso specifico mercurio/aria | 13 2/3 × 870 = 11890 | 11890 | esatto |
| altezza A in pollici | 30 × 11890 = 356700 | 356700 | esatto |
| altezza A in piedi | 356700 / 12 = 29725 | 29725 | esatto |
| circonferenza di raggio A | 186768 piedi | 2π × 29725 = 186767,7 | esatto (arrotondato) |
| periodo del pendolo di lunghezza A | 190 3/4 s | 2√(356700/39,2) = 190,78 s | corretto (Newton arrotonda a 3/4) |
| velocità | 979 piedi/s | 186768/190,75 = 979,1; con 190,78 s: 979,0 | esatto |
| correzione per lo spessore | 979/9 ≈ 109 | 108,8 | corretto |
| velocità corretta | 1088 | 979 + 108,8 = 1087,8 | esatto |
| rapporto diametro : interasse | 1 : 9 o 10 | ∛870 = 9,55 (acqua); ∛1740 = 12,0 (sali) | coerente con la densità dell’acqua; con quella dei sali verrebbe 1 : 12 |
| vapori: √(11/10) ≈ 21/20 | 1,05 | √1,1 = 1,0488 | buona approssimazione |
| velocità finale | 1142 | 1088 × 21/20 = 1142,4 (con √1,1: 1141,1) | esatto |
| Sauveur: 1070/100 | 10 7/10 piedi parigini | 10,7 | esatto |
| 1142 piedi londinesi e 1070 parigini | «ossia» | 1070 piedi parigini ≈ 1140 piedi inglesi | coerenti (non dalle fonti allegate: piede parigino 0,3248 m, inglese 0,3048 m) |

Nessuna cifra di Newton risulta sbagliata. Due osservazioni:

- **La correzione per lo spessore** aggiunge 1/9 di 979: equivale a supporre che il suono attraversi in un istante i diametri delle particelle e con velocità 979 gli spazi vuoti, con diametro : interasse = 1 : 10 (979 × 10/9 = 1087,8). Con il rapporto 1 : 9 la correzione sarebbe 979 × 9/8 − 979 = 122. Newton sceglie il valore che porta più vicino all’esperimento.
- **Il calcolo dei vapori** porta il risultato teorico **esattamente** al valore sperimentale di 1142 piedi londinesi (II.S8.45). Le due correzioni sono ipotesi *ad hoc*, non misure.

### N12. Il divario con l’esperienza e la correzione di Laplace (non dalle fonti allegate)

*Questa nota è una nota fisica moderna, non deriva dalle fonti allegate.*

- Il valore «puro» di Newton, 979 piedi inglesi al secondo, vale circa **298 m/s**. Lo stesso risultato si ottiene ricalcolando √(*p*/ρ) con i dati di Newton (30 pollici di mercurio ≈ 1,016 × 10⁵ Pa; densità dell’aria 1/870 di quella dell’acqua ≈ 1,149 kg/m³): **297 m/s**.
- Il valore sperimentale citato da Newton, 1142 piedi londinesi ≈ **348 m/s** (1070 piedi parigini ≈ 348 m/s), è vicino al valore moderno della velocità del suono nell’aria a temperatura ambiente: **331 m/s a 0 °C, 340 m/s a 15 °C, 343 m/s a 20 °C**.
- Il divario di circa il **16–18 %** non dipende dallo spessore delle particelle né dai vapori, ma dall’ipotesi di Boyle della Prop. XLVIII (forza elastica proporzionale alla condensazione, cioè compressione **isoterma**). Nelle compressioni rapide del suono l’aria si scalda e si raffredda senza avere il tempo di scambiare calore: la compressione è **adiabatica**, e la pressione cresce come ρ^γ, con γ = *c*ₚ/*c*ᵥ ≈ 1,40 per l’aria. La velocità diventa √(γ*p*/ρ): è la **correzione di Laplace** (1816), che moltiplica il valore di Newton per √1,4 ≈ 1,183. Con i dati di Newton: 297 × 1,183 ≈ **352 m/s**; 979 piedi × 1,183 ≈ 1158 piedi. Per la temperatura: isoterma √(*RT*) = 280 m/s a 0 °C, 290 m/s a 20 °C; adiabatica √(γ*RT*) = 331 m/s e 343 m/s.
- La dipendenza dalla stagione (II.S8.44) va corretta: a pressione data la velocità dipende dalla **temperatura** (∝ √*T*), e Newton la attribuisce a densità e forza elastica variabili; il segno dell’effetto (più veloce d’estate) è giusto.

### N13. Lo Scolio: Sauveur, le canne e le trombe

- Una canna aperta di circa 5 piedi parigini (≈ 1,6 m) all’unisono con una corda di 100 vibrazioni al secondo: lunghezza d’onda 1070/100 = 10,7 piedi, il doppio della canna. È la relazione moderna per la fondamentale di una canna aperta, λ = 2*L* (non dalle fonti allegate; anche il «verosimile» di Newton è una generalizzazione, che la correzione di bocca rende approssimata).
- Il corollario della Prop. XLVII (il numero delle pulsazioni non si moltiplica) spiega che il suono cessa con la sorgente e non si «prolunga» con la distanza.
- Le «trombe stentorofoniche» sono i portavoce (*speaking-trumpets* in Motte), detti stentorofonici da Stentore, l’araldo omerico dalla voce di bronzo; Samuel Morland ne aveva pubblicato uno nel 1671 (non verificato sulle fonti allegate). La spiegazione di Newton (il tubo impedisce la dilatazione laterale e il moto «ritorna più forte») è qualitativa.

---

## Controllo della copertura

Pagine 1726 dai marcatori ‹n› della trascrizione. L’estratto di Motte non contiene marcatori di pagina: «sezione corrispondente».

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| II.S8.01–II.S8.02 | *Pressio non propagatur per fluidum* | Prop. XLI, enunciato e dimostrazione | p. 357 | Sect. VIII, Prop. XLI |
| II.S8.03 | *Si pressionis, a dato puncto* | Prop. XLI, Cor. con seconda dimostrazione | pp. 357–358 | Prop. XLI, Cor. |
| II.S8.04–II.S8.07 | *Motus omnis per fluidum propagatus* | Prop. XLII, enunciato, Casi 1–3 | pp. 359–361 | Prop. XLII |
| II.S8.08–II.S8.10 | *Corpus omne tremulum* | Prop. XLIII, enunciato, Caso 1, mezzo non elastico | pp. 361–363 | Prop. XLIII |
| II.S8.11 | *Hallucinantur igitur* | Prop. XLIII, Cor. | p. 363 | Prop. XLIII, Cor. |
| II.S8.12–II.S8.13 | *Si aqua in canalis cruribus* | Prop. XLIV, enunciato e dimostrazione | pp. 363–364 | Prop. XLIV |
| II.S8.14–II.S8.16 | *Igitur aquæ ascendentis* … *Aucta autem vel diminuta* | Prop. XLIV, Cor. 1–3 | p. 364 | Prop. XLIV, Cor. 1–3 |
| II.S8.17–II.S8.18 | *Undarum velocitas est* | Prop. XLV | p. 365 | Prop. XLV |
| II.S8.19–II.S8.21 | *Invenire velocitatem undarum* | Prop. XLVI, enunciato, costruzione, dimostrazione | p. 365 | Prop. XLVI |
| II.S8.22–II.S8.24 | *Igitur undæ, quæ pedes* … *Hæc ita se habent ex hypothesi* | Prop. XLVI, Cor. 1–2, avvertenza | p. 366 | Prop. XLVI, Cor. 1–2 |
| II.S8.25–II.S8.27 | *Pulsibus per fluidum propagatis* | Prop. XLVII, enunciato, costruzione, dimostrazione | pp. 366–368 | Prop. XLVII |
| II.S8.28 | *Hinc patet quod numerus pulsuum* | Prop. XLVII, Cor. | p. 368 | Prop. XLVII, Cor. |
| II.S8.29–II.S8.33 | *Pulsuum in fluido elastico propagatorum* | Prop. XLVIII, enunciato, Casi 1–3, rinvio | pp. 368–369 | Prop. XLVIII |
| II.S8.34–II.S8.36 | *Datis medii densitate & vi elastica* | Prop. XLIX, enunciato, costruzione, dimostrazione | pp. 370–371 | Prop. XLIX |
| II.S8.37–II.S8.38 | *Velocitas pulsuum ea est* … *Unde cum altitudo illa A* | Prop. XLIX, Cor. 1–2 | p. 371 | Prop. XLIX, Cor. 1–2 |
| II.S8.39–II.S8.40 | *Invenire pulsuum distantias* | Prop. L | p. 372 | Prop. L |
| II.S8.41–II.S8.47 | *Spectant propositiones novissimæ* … *Et hæc sunt præcipua phænomena sonorum* | Scolio (sette capoversi) | pp. 372–374 | Scholium |

**Controlli eseguiti.**

1. **Copertura.** Ho riletto in sequenza ogni periodo della trascrizione, da *Pressio non propagatur per fluidum* a *Et hæc sunt præcipua phænomena sonorum*, contro la traduzione: nessuna frase manca. Dove il latino ha un periodo lungo (soprattutto nella Prop. XLVII), l’italiano lo divide in più frasi senza omettere membri. I 47 identificatori sono consecutivi e unici (controllo automatico).
2. **Parte B.** `check.py` sul file finale: JSON valido; tutte le stringhe `la` sono sottostringhe esatte della trascrizione e tutte le stringhe `en` sono sottostringhe esatte di Motte; ogni identificatore di `copertura` è presente nel testo. Esito riportato nel messaggio di consegna.
3. **Matematica e numeri.** Script `verifica.py`: tutti i numeri della Prop. XLIV, Cor. 2, della Prop. XLVI, Cor. 1 e dello Scolio (N6, N7, N11), e i confronti moderni (N7, N12). Script `verifica_p47.py`: legge del pendolo nella Prop. XLVII e velocità √(*p*/ρ) della Prop. XLIX (N9, N10). Nessun errore aritmetico di Newton.
4. **Motte.** Confronto di tutta la sezione corrispondente, comprese le 28 formule stampate come immagini (SVG 922–949), rese e lette una per una: 27 coincidono con il latino, la 926 ha π per φ (refuso dell’edizione 1846). Divergenze nel § A.13.
5. **Rimandi.** Verificati sui Fascicoli 8 e 9 e sulla fonte latina della Sezione V del Libro II (§ A.15).
6. **Separazione fra testo e commento.** Il testo tradotto non contiene formule moderne; le integrazioni del curatore sono tra parentesi quadre («[nelle]» in II.S8.05, «[del Libro I]» in II.S8.13, i «[*sic*]» e il rinvio «[N2]» in II.S8.06).

**Non ho potuto verificare:**

- **la stampa del 1726**: nessuno dei punti elencati in A.12 e A.14 è stato controllato sulla scansione ECCO;
- **le figure originali** (FIG 63–71 e la «FIG 60» della Prop. XLVII): la disposizione dei punti è ricostruita dal testo;
- **Motte 1729**, per sapere se l’aggiunta «of the pendulum» (Prop. XLIX) e le altre divergenze sono già nella prima edizione;
- **la paginazione di Motte 1846**: l’estratto non ha marcatori di pagina;
- i dati storici esterni (Morland, Grimaldi, Laplace 1816, valori moderni) usati nelle note N3, N12, N13: sono da conoscenza generale e marcati come tali.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Libro II, Sezione VIII (Propp. XLI–L, Scolio) | **Fascicolo 19, presente documento, prima versione** |
| Refusi e punti dubbi (A.12, A.14) | Da verificare sulla stampa del 1726 (scansione ECCO); priorità: *corol. VI.* / *Cas. 6* (p. 358), *Pl, Pn, Pm* (p. 367), *minuti minus secundi* (p. 373) |
| SVG 922–949 | Controllati tutti (§ A.13); nella pagina della Prop. XLVII correggere il testo a fronte di Motte: SVG 926 «π» → φ, con nota |
| *plaga* reso «direzione» | Da armonizzare dal coordinatore (§ A.0) |
| Scolio, calcolo della velocità del suono | Verificato (N11); candidato a una pagina interattiva numerica (catena di calcolo con correzioni regolabili e confronto con √(γ*p*/ρ)) |
| Prop. XLVII | Verificata numericamente (N9); la pagina interattiva può animare il cerchio di riferimento e la catena dei punti E, F, G |
| Figure | Da consultare per confermare `figura_base` nella Parte B |
| Revisione filologica e scientifica indipendente | Da eseguire |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce traduzioni italiane o inglesi moderne. **Licenza prevista** (decisione del curatore, Fascicolo 3): testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project; i testi di Motte sono di pubblico dominio.

---
## Parte B — Dati per le pagine interattive

Unità incluse: le proposizioni e i corollari con figura e costruzione o dimostrazione geometrica propria: Prop. XLI e il suo Corollario, Propp. XLII, XLIV, XLVI, XLVII, XLIX. **Escluse**: la Prop. XLIII (argomento fisico senza figura), la Prop. XLV (senza dimostrazione propria), la Prop. XLVIII (argomento di similitudine senza figura), la Prop. L (regola aritmetica), i corollari senza dimostrazione propria e lo Scolio (calcolo numerico senza figura: candidato a una pagina numerica, vedi Registro).

Convenzioni:

- `la`: testo latino esatto della trascrizione, refusi, frazioni appiattite e marcatori di pagina interni alle parole compresi (*fru <358> stum*, *æqua <364> lis*); le letture sono in `nota` e nell’apparato;
- `it`: la traduzione di questo fascicolo;
- `en`: Motte 1846, allineato per senso; le formule stampate come immagini restano come `[SVG n]` (ignorate dallo strumento di controllo; contenuto controllato nel § A.13);
- `dipende_da`: soltanto i rimandi citati nella frase latina;
- `figura.mostra`: elementi da rendere visibili, cumulativi; `figura.evidenzia`: relazioni da mettere in risalto.

```json
{
 "fascicolo": "19-L2-S8",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase latina",
  "en": "Motte 1846, allineato per senso; le formule stampate come immagini compaiono come [SVG n] e sono ignorate dallo strumento di controllo; le immagini sono state controllate (§ A.13)",
  "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione",
  "la": ""
 },
 "unita": [
  {
   "id": "L2-P41",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XLI — la pressione non si propaga in linea retta",
   "copertura": [
    "II.S8.01",
    "II.S8.02"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Sect. VIII, Prop. XLI"
   },
   "enunciato": {
    "la": "",
    "it": "La pressione non si propaga attraverso un fluido secondo linee rette, se non dove le particelle del fluido giacciono in linea retta.",
    "en": "A pressure is not propagated through a fluid in rectilinear directions unless where the particles of the fluid lie in a right line."
   },
   "figura_base": {
    "punti": [
     "a",
     "b",
     "c",
     "d",
     "e",
     "f",
     "g",
     "h",
     "k",
     "l",
     "m"
    ],
    "vincoli": [
     "a, b, c, d, e allineati",
     "f, g da una parte e dall’altra di e, fuori dalla retta",
     "h, k più lontani di f, g e a contatto con essi",
     "l, m più lontani di h, k"
    ]
   },
   "passi": [
    {
     "id": "L2-P41-p1",
     "la": "",
     "it": "Se le particelle a, b, c, d, e giacciono in linea retta, la pressione può certo propagarsi direttamente da a a e; ma la particella e spingerà obliquamente le particelle f e g, poste obliquamente, e quelle particelle f e g non sosterranno la pressione ricevuta, se non sono sostenute da particelle più lontane h e k; e in quanto sono sostenute, premono le particelle che le sostengono; e queste non sosterranno la pressione, se non sono sostenute da altre più lontane, l e m, e non le premono, e così di seguito all’infinito.",
     "en": "If the particles a, b, c, d, e, lie in a right line, the pressure may be indeed directly propagated from a to e; but then the particle e will urge the obliquely posited particles f and g obliquely, and those particles f and g will not sustain this pressure, unless they be supported by the particles h and k lying beyond them; but the particles that support them are also pressed by them; and those particles cannot sustain that pressure, without being supported by, and pressing upon, those particles that lie still farther, as l and m, and so on in infinitum.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "a",
       "b",
       "c",
       "d",
       "e",
       "f",
       "g",
       "h",
       "k",
       "l",
       "m",
       "pressione lungo a–e",
       "spinte oblique e→f, e→g"
      ],
      "evidenzia": [
       "la catena di sostegni che si allarga"
      ]
     }
    },
    {
     "id": "L2-P41-p2",
     "la": "",
     "it": "La pressione dunque, non appena si propaga a particelle che non giacciono in linea retta, comincerà a divaricarsi e si propagherà obliquamente all’infinito; e dopo che ha cominciato a propagarsi obliquamente, se incontra particelle più lontane che non giacciono in linea retta, si divaricherà di nuovo; e ciò tante volte quante incontrerà particelle che non giacciono esattamente in linea retta.",
     "en": "Therefore the pressure, as soon as it is propagated to particles that lie out of right lines, begins to deflect towards one hand and the other, and will be propagated obliquely in infinitum; and after it has begun to be propagated obliquely, if it reaches more distant particles lying out of the right line, it will deflect again on each hand and this it will do as often as it lights on particles that do not lie exactly in a right line.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "ventaglio di direzioni oblique"
      ],
      "evidenzia": [
       "divaricazione ripetuta"
      ]
     },
     "nota": "Motte «deflect towards one hand and the other» amplia *divaricare*."
    }
   ]
  },
  {
   "id": "L2-P41-Cor",
   "tipo": "Corollarium",
   "titolo": "Prop. XLI, Cor. — la pressione si divarica dietro l’ostacolo",
   "copertura": [
    "II.S8.03"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Sect. VIII, Prop. XLI, Cor."
   },
   "enunciato": {
    "la": "",
    "it": "Se una parte della pressione propagata da un punto dato attraverso un fluido è intercettata da un ostacolo, la parte restante, che non è intercettata, si divaricherà negli spazi dietro l’ostacolo.",
    "en": "If any part of a pressure, propagated through a fluid from a given point, be intercepted by any obstacle, the remaining part, which is not intercepted, will deflect into the spaces behind the obstacle."
   },
   "figura_base": {
    "punti": [
     "A",
     "N",
     "B",
     "C",
     "K",
     "P",
     "Q",
     "d",
     "e",
     "f",
     "g",
     "h",
     "i",
     "O",
     "L"
    ],
    "vincoli": [
     "ostacolo NBCK forato in BC (foro circolare)",
     "cono APQ con vertice A che passa per il foro BC",
     "piani trasversali de, fg, hi che dividono il cono in tronchi",
     "spazi NO e KL dietro l’ostacolo, ai lati del cono"
    ]
   },
   "passi": [
    {
     "id": "L2-P41-Cor-p1",
     "la": "",
     "it": "Ciò si può dimostrare anche così.",
     "en": "This may be demonstrated also after the following manner.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A",
       "ostacolo NBCK"
      ]
     }
    },
    {
     "id": "L2-P41-Cor-p2",
     "la": "",
     "it": "Dal punto A la pressione si propaghi in ogni direzione, e ciò, se è possibile, secondo linee rette; e, essendo l’ostacolo NBCK forato in BC, sia intercettata tutta, tranne la parte di forma conica APQ che passa attraverso il foro circolare BC.",
     "en": "Let a pressure be propagated from the point A towards any part, and, if it be possible, in rectilinear directions; and the obstacle NBCK being perforated in BC, let all the pressure be intercepted but the coniform part APQ passing through the circular hole BC.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A",
       "N",
       "B",
       "C",
       "K",
       "foro BC",
       "cono APQ"
      ],
      "evidenzia": [
       "ipotesi per assurdo: propagazione rettilinea"
      ]
     },
     "nota": "Motte «towards any part» per *quaquaversum* («in ogni direzione»)."
    },
    {
     "id": "L2-P41-Cor-p3",
     "la": "",
     "it": "Con i piani trasversali de, fg, hi si divida il cono APQ in tronchi; e mentre il cono ABC, propagando la pressione, spinge il tronco di cono successivo degf sulla superficie de, e questo tronco spinge il tronco vicino fgih sulla superficie fg, e quel tronco spinge il terzo tronco, e così di seguito all’infinito, è manifesto (per la terza legge del moto) che il primo tronco defg, per la reazione del secondo tronco fghi, sarà spinto e premuto sulla superficie fg tanto quanto esso spinge e preme quel secondo tronco.",
     "en": "Let the cone APQ be divided into frustums by the transverse planes, de, fg, hi. Then while the cone ABC, propagating the pressure, urges the conic frustum degf beyond it on the superficies de, and this frustum urges the next frustum fgih on the superficies fg, and that frustum urges a third frustum, and so in infinitum; it is manifest (by the third Law) that the first frustum defg is, by the re-action of the second frustum fghi, as much urged and pressed on the superficies fg, as it urges and presses that second frustum.",
     "dipende_da": [
      "Legge III"
     ],
     "figura": {
      "mostra": [
       "piani de, fg, hi",
       "tronchi degf, fghi"
      ],
      "evidenzia": [
       "azione e reazione sulla superficie fg"
      ]
     },
     "nota": "Il marcatore di pagina ‹358› cade dentro *fru‹358›stum*; *conus ABC* è così anche in Motte (§ A.1)."
    },
    {
     "id": "L2-P41-Cor-p4",
     "la": "",
     "it": "Il tronco aegf [sic: degf] è dunque compresso da entrambe le parti, fra il cono Ade e il tronco fhig, e perciò (per il Cor. VI [sic: Caso 6] della Prop. XIX) non può conservare la sua figura, se non è compresso con la stessa forza da ogni parte.",
     "en": "Therefore the frustum degf is compressed on both sides, that is, between the cone Ade and the frustum fhig; and therefore (by Case 6, Prop. XIX) cannot preserve its figure, unless it be compressed with the same force on all sides.",
     "dipende_da": [
      "Libro II, Prop. XIX, Caso 6 (il latino ha «corol. VI.»)"
     ],
     "figura": {
      "mostra": [
       "cono Ade",
       "tronco degf compresso su de e fg"
      ],
      "evidenzia": [
       "compressione da entrambe le basi"
      ]
     },
     "nota": "*aegf*: refuso probabile per *degf*. *corol. VI.*: la Prop. XIX ha un solo corollario; il contenuto è il Caso 6, come in Motte (§ A.15)."
    },
    {
     "id": "L2-P41-Cor-p5",
     "la": "",
     "it": "Con lo stesso impeto con cui è premuto sulle superfici de, fg, tenderà dunque a cedere verso i lati df, eg; e lì (poiché non è rigido, ma fluido in ogni senso) scorrerà fuori e si dilaterà, se non c’è un fluido circostante che trattenga questa tendenza.",
     "en": "Therefore with the same force with which it is pressed on the superficies de, fg, it will endeavour to break forth at the sides df, eg; and there (being not in the least tenacious or hard, but perfectly fluid) it will run out, expanding itself, unless there be an ambient fluid opposing that endeavour.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "lati df, eg",
       "frecce laterali"
      ],
      "evidenzia": [
       "tendenza a cedere ai lati"
      ]
     },
     "nota": "Motte rende *impetus* con «force» e amplia *cum rigidum non sit*."
    },
    {
     "id": "L2-P41-Cor-p6",
     "la": "",
     "it": "Perciò, con la tendenza a scorrere fuori, premerà con lo stesso impeto tanto il fluido circostante ai lati df, eg quanto il tronco fghi; e perciò la pressione si propagherà dai lati df, eg negli spazi NO, KL, da una parte e dall’altra, non meno di quanto si propaga dalla superficie fg verso PQ.",
     "en": "Therefore, by the effort it makes to run out, it will press the ambient fluid, at its sides df, eg, with the same force that it does the frustum fghi; and therefore, the pressure will be propagated as much from the sides df, eg, into the spaces NO, KL this way and that way, as it is propagated from the superficies fg towards PQ.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "spazi NO, KL",
       "pressione laterale"
      ],
      "evidenzia": [
       "pressione laterale uguale a quella in avanti verso PQ"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P42",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XLII — ogni moto propagato diverge negli spazi immoti",
   "copertura": [
    "II.S8.04",
    "II.S8.05",
    "II.S8.06",
    "II.S8.07"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Sect. VIII, Prop. XLII"
   },
   "enunciato": {
    "la": "",
    "it": "Ogni moto propagato attraverso un fluido diverge dal cammino rettilineo negli spazi immoti.",
    "en": "All motion propagated through a fluid diverges from a rectilinear progress into the unmoved spaces."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "C",
     "P",
     "Q",
     "K",
     "L",
     "N",
     "O",
     "d",
     "e",
     "f",
     "g",
     "h",
     "i",
     "k",
     "l",
     "m",
     "n",
     "r",
     "s",
     "t",
     "v"
    ],
    "vincoli": [
     "foro BC; spazio conico BCQP con vertice A",
     "de, fg, hi, kl (mn): creste delle onde (Caso 1) o parti più dense delle pulsazioni (Caso 2), archi con centro A",
     "KL e NO: parti immote ai lati",
     "rfgr, shis, tklt, vmnv: onde dilatate lateralmente"
    ]
   },
   "passi": [
    {
     "id": "L2-P42-p1",
     "la": "",
     "it": "Caso 1. Si propaghi un moto dal punto A attraverso il foro BC e proceda, se è possibile, nello spazio conico BCQP, secondo linee rette divergenti dal punto A.",
     "en": "CASE 1. Let a motion be propagated from the point A through the hole BC, and, if it be possible, let it proceed in the conic space BCQP according to right lines diverging from the point A.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A",
       "B",
       "C",
       "P",
       "Q",
       "spazio conico BCQP"
      ],
      "evidenzia": [
       "ipotesi per assurdo"
      ]
     }
    },
    {
     "id": "L2-P42-p2",
     "la": "",
     "it": "E supponiamo dapprima che questo moto sia quello delle onde sulla superficie di un’acqua stagnante.",
     "en": "And let us first suppose this motion to be that of waves in the surface of standing water;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "superficie d’acqua"
      ]
     }
    },
    {
     "id": "L2-P42-p3",
     "la": "",
     "it": "E siano de, fg, hi, kl, ecc. le parti più alte delle singole onde, separate l’una dall’altra da altrettante valli intermedie.",
     "en": "and let de, fg, hi, kl, &c., be the tops of the several waves, divided from each other by as many intermediate valleys or hollows.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "creste de, fg, hi, kl",
       "valli intermedie"
      ]
     }
    },
    {
     "id": "L2-P42-p4",
     "la": "",
     "it": "Poiché dunque l’acqua nelle creste delle onde è più alta che nelle parti immote del fluido LK, NO, essa scorrerà giù dalle estremità delle creste e, g, i, l, ecc., d, f, h, k, ecc., da una parte e dall’altra, verso KL e NO; e poiché nelle valli delle onde è più bassa che nelle parti immote del fluido KL, NO, scorrerà giù da quelle parti immote [nelle] valli delle onde.",
     "en": "Then, because the water in the ridges of the waves is higher than in the unmoved parts of the fluid KL, NO, it will run down from off the tops of those ridges, e, g, i, l, &c., d, f, h, k, &c., this way and that way towards KL and NO; and because the water is more depressed in the hollows of the waves than in the unmoved parts of the fluid KL, NO, it will run down into those hollows out of these unmoved parts.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "parti immote KL, NO",
       "deflusso dalle estremità delle creste",
       "deflusso nelle valli"
      ]
     },
     "nota": "*undarum valles* senza preposizione: integrato «[nelle]». *LK* alla prima occorrenza, poi *KL*."
    },
    {
     "id": "L2-P42-p5",
     "la": "",
     "it": "Con il primo deflusso le creste delle onde, con il secondo le valli, si dilatano da una parte e dall’altra e si propagano verso KL e NO.",
     "en": "By the first deflux the ridges of the waves will dilate themselves this way and that way, and be propagated towards KL and NO.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "creste e valli che si allargano"
      ]
     },
     "nota": "Motte omette il secondo membro (*posteriore valles*)."
    },
    {
     "id": "L2-P42-p6",
     "la": "",
     "it": "E poiché il moto delle onde da A verso PQ avviene per un continuo deflusso dalle creste nelle valli vicine, e perciò non è più veloce di quanto comporti la velocità della discesa; e la discesa dell’acqua da una parte e dall’altra verso KL e NO deve compiersi con la stessa velocità; la dilatazione delle onde da una parte e dall’altra verso KL e NO si propagherà con la stessa velocità con cui le onde stesse avanzano in linea retta da A verso PQ.",
     "en": "And because the motion of the waves from A towards PQ is carried on by a continual deflux from the ridges of the waves into the hollows next to them, and therefore cannot be swifter than in proportion to the celerity of the descent; and the descent of the water on each side towards KL and NO must be performed with the same velocity; it follows that the dilatation of the waves on each side towards KL and NO will be propagated with the same velocity as the waves themselves go forward with directly from A to PQ.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "velocità in avanti",
       "velocità laterale"
      ],
      "evidenzia": [
       "velocità laterale = velocità in avanti"
      ]
     }
    },
    {
     "id": "L2-P42-p7",
     "la": "",
     "it": "E perciò tutto lo spazio da una parte e dall’altra, verso KL e NO, sarà occupato dalle onde dilatate rfgr, shis, tklt, vmnv, ecc.",
     "en": "And therefore the whole space this way and that way towards KL and NO will be filled by the dilated waves rfgr, shis, tklt, vmnv, &c.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "onde dilatate rfgr, shis, tklt, vmnv"
      ],
      "evidenzia": [
       "lo spazio laterale invaso"
      ]
     }
    },
    {
     "id": "L2-P42-p8",
     "la": "",
     "it": "Che le cose stiano così, chiunque può sperimentarlo in un’acqua stagnante.",
     "en": "That these things are so, any one may find by making the experiment in still water.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P42-p9",
     "la": "",
     "it": "Caso 2. Supponiamo ora che de, fg, hi, kl, mn rappresentino pulsazioni propagate successivamente dal punto A attraverso un mezzo elastico.",
     "en": "CASE 2. Let us suppose that de, fg, hi, kl, mn, represent pulses successively propagated from the point A through an elastic medium.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "pulsazioni de, fg, hi, kl, mn"
      ]
     },
     "nota": "Prima occorrenza di *pulsus*, «pulsazione» (nota N2)."
    },
    {
     "id": "L2-P42-p10",
     "la": "",
     "it": "Immagina che le pulsazioni si propaghino per condensazioni e rarefazioni successive del mezzo, così che la parte più densa di ciascuna pulsazione occupi una superficie sferica descritta attorno al centro A, e che fra pulsazioni successive intercorrano intervalli uguali.",
     "en": "Conceive the pulses to be propagated by successive condensations and rarefactions of the medium, so that the densest part of every pulse may occupy a spherical superficies described about the centre A, and that equal intervals intervene between the successive pulses.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "superfici sferiche con centro A",
       "intervalli uguali"
      ]
     }
    },
    {
     "id": "L2-P42-p11",
     "la": "",
     "it": "Le linee de, fg, hi, kl, ecc. rappresentino poi le parti più dense delle pulsazioni, propagate attraverso il foro BC.",
     "en": "Let the lines de, fg, hi, kl, &c., represent the densest parts of the pulses, propagated through the hole BC;",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "parti più dense oltre il foro"
      ]
     }
    },
    {
     "id": "L2-P42-p12",
     "la": "",
     "it": "E poiché lì il mezzo è più denso che negli spazi da una parte e dall’altra verso KL e NO, si dilaterà tanto verso quegli spazi KL, NO situati da entrambe le parti quanto verso gli intervalli più radi fra le pulsazioni; e in questo modo, diventando sempre più rado in corrispondenza degli intervalli e più denso in corrispondenza delle pulsazioni, parteciperà del loro moto.",
     "en": "and because the medium is denser there than in the spaces on either side towards KL and NO, it will dilate itself as well towards those spaces KL, NO, on each hand, as towards the rare intervals between the pulses; and thence the medium, becoming always more rare next the intervals, and more dense next the pulses, will partake of their motion.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "dilatazione verso KL, NO"
      ]
     },
     "nota": "Il marcatore di pagina ‹361› cade fra *utrinque* e *sita*."
    },
    {
     "id": "L2-P42-p13",
     "la": "",
     "it": "E poiché il moto progressivo delle pulsazioni nasce dal continuo rilassarsi delle parti più dense verso gli intervalli più radi che stanno loro davanti; e le pulsazioni devono rilassarsi con quasi la stessa velocità da una parte e dall’altra verso le parti in quiete del mezzo KL, NO; quelle pulsazioni si dilateranno da ogni parte negli spazi immoti KL, NO con quasi la stessa velocità con cui si propagano direttamente dal centro A; e perciò occuperanno tutto lo spazio KLON.",
     "en": "And because the progressive motion of the pulses arises from the perpetual relaxation of the denser parts towards the antecedent rare intervals; and since the pulses will relax themselves on each hand towards the quiescent parts of the medium KL, NO, with very near the same celerity; therefore the pulses will dilate themselves on all sides into the unmoved parts KL, NO, with almost the same celerity with which they are propagated directly from the centre A; and therefore will fill up the whole space KLON.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "spazio KLON occupato"
      ],
      "evidenzia": [
       "velocità laterale ≈ velocità in avanti"
      ]
     }
    },
    {
     "id": "L2-P42-p14",
     "la": "",
     "it": "Lo sperimentiamo nei suoni, che si odono anche con un monte interposto, oppure, entrati in una stanza attraverso una finestra, si dilatano in tutte le parti della stanza e si odono in tutti gli angoli, non tanto riflessi dalle pareti opposte quanto propagati direttamente dalla finestra, per quanto è lecito giudicare con i sensi.",
     "en": "And we find the same by experience also in sounds which are heard through a mountain interposed; and, if they come into a chamber through the window, dilate themselves into all the parts of the room, and are heard in every corner; and not as reflected from the opposite walls, but directly propagated from the window, as far as our sense can judge.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Esempio fisico senza figura (nota N3)."
    },
    {
     "id": "L2-P42-p15",
     "la": "",
     "it": "Caso 3. Supponiamo infine che un moto di qualsiasi genere si propaghi da A attraverso il foro BC. Poiché questa propagazione non avviene se non in quanto le parti del mezzo più vicine al centro A spingono e mettono in moto le parti più lontane; e le parti che sono spinte sono fluide, e perciò si ritirano in ogni direzione verso le regioni dove sono meno premute; esse si ritireranno verso tutte le parti del mezzo in quiete, tanto le laterali KL e NO quanto le anteriori PQ; e in questo modo ogni moto, non appena è passato attraverso il foro BC, comincerà a dilatarsi e di lì, come da un principio e da un centro, a propagarsi direttamente in ogni parte.",
     "en": "CASE 3. Let us suppose, lastly, that a motion of any kind is propagated from A through the hole BC. Then since the cause of this propagation is that the parts of the medium that are near the centre A disturb and agitate those which lie farther from it; and since the parts which are urged are fluid, and therefore recede every way towards those spaces where they are less pressed, they will by consequence recede towards all the parts of the quiescent medium; as well to the parts on each hand, as KL and NO, as to those right before, as PQ; and by this means all the motion, as soon as it has passed through the hole BC, will begin to dilate itself, and from thence, as from its principle and centre, will be propagated directly every way.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "foro BC come nuovo centro di propagazione"
      ],
      "evidenzia": [
       "propagazione in ogni direzione dal foro"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P44",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XLIV — l’acqua oscillante in un canale e il pendolo",
   "copertura": [
    "II.S8.12",
    "II.S8.13"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Sect. VIII, Prop. XLIV"
   },
   "enunciato": {
    "la": "",
    "it": "Se l’acqua sale e scende alternativamente nei bracci verticali KL, MN di un canale, e si costruisce un pendolo la cui lunghezza fra il punto di sospensione e il centro di oscillazione sia uguale alla metà della lunghezza dell’acqua nel canale, dico che l’acqua salirà e scenderà negli stessi tempi in cui il pendolo oscilla.",
    "en": "If water ascend and descend alternately in the erected legs KL, MN, of a canal or pipe; and a pendulum be constructed whose length between the point of suspension and the centre of oscillation is equal to half the length of the water in the canal; I say, that the water will ascend and descend in the same times in which the pendulum oscillates."
   },
   "figura_base": {
    "punti": [
     "K",
     "L",
     "M",
     "N",
     "A",
     "B",
     "C",
     "D",
     "E",
     "F",
     "G",
     "H",
     "V",
     "P",
     "Q",
     "R",
     "S"
    ],
    "vincoli": [
     "canale a U con bracci verticali KL, MN",
     "AB, CD: livelli medi dell’acqua nei due bracci",
     "EF: livello salito in KL; GH: livello sceso in MN; AE = discesa in MN",
     "V punto di sospensione; P corpo pendolo; RPQS cicloide con punto più basso P",
     "arco PQ = AE; VP = PR (semicicloide)",
     "VP = metà della lunghezza dell’acqua"
    ]
   },
   "passi": [
    {
     "id": "L2-P44-p1",
     "la": "",
     "it": "Misuro la lunghezza dell’acqua lungo gli assi del canale e dei bracci, ponendola uguale alla somma di questi assi; e qui non considero la resistenza dell’acqua che nasce dall’attrito del canale.",
     "en": "I measure the length of the water along the axes of the canal and its legs, and make it equal to the sum of those axes; and take no notice of the resistance of the water arising from its attrition by the sides of the canal.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "canale KL–MN",
       "asse del canale"
      ]
     }
    },
    {
     "id": "L2-P44-p2",
     "la": "",
     "it": "Rappresentino dunque AB, CD l’altezza media dell’acqua nell’uno e nell’altro braccio; e quando l’acqua nel braccio KL sale all’altezza EF, l’acqua nel braccio MN sia scesa all’altezza GH.",
     "en": "Let, therefore, AB, CD, represent the mean height of the water in both legs; and when the water in the leg KL ascends to the height EF, the water will descend in the leg MN to the height GH.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "AB",
       "CD",
       "EF",
       "GH"
      ],
      "evidenzia": [
       "AE = discesa CG"
      ]
     }
    },
    {
     "id": "L2-P44-p3",
     "la": "",
     "it": "Sia poi P il corpo pendolo, VP il filo, V il punto di sospensione, RPQSS [sic: RPQS] la cicloide che il pendolo descrive, P il suo punto più basso, PQ un arco uguale all’altezza AE.",
     "en": "Let P be a pendulous body, VP the thread, V the point of suspension, RPQS the cycloid which the pendulum describes, P its lowest point, PQ an arc equal to the height AE.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "V",
       "P",
       "filo VP",
       "cicloide RPQS",
       "arco PQ"
      ],
      "evidenzia": [
       "PQ = AE"
      ]
     },
     "nota": "*RPQSS*: S doppia, refuso probabile; il marcatore ‹364› cade dentro *æqualis*."
    },
    {
     "id": "L2-P44-p4",
     "la": "",
     "it": "La forza con cui il moto dell’acqua è alternativamente accelerato e ritardato è l’eccesso del peso dell’acqua in uno dei due bracci sul peso nell’altro; e perciò, quando l’acqua nel braccio KL sale a EF e nell’altro braccio scende a GH, quella forza è il doppio del peso dell’acqua EABF, e perciò sta al peso di tutta l’acqua come AE, ossia PQ, sta a VP, ossia PR.",
     "en": "The force with which the motion of the water is accelerated and retarded alternately is the excess of the weight of the water in one leg above the weight in the other; and, therefore, when the water in the leg KL ascends to EF, and in the other leg descends to GH, that force is double the weight of the water EABF, and therefore is to the weight of the whole water as AE or PQ to VP or PR.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "colonna EABF",
       "PR"
      ],
      "evidenzia": [
       "forza / peso totale = AE / VP"
      ]
     },
     "nota": "VP = PR: proprietà del pendolo cicloidale (nota N5)."
    },
    {
     "id": "L2-P44-p5",
     "la": "",
     "it": "Anche la forza con cui il peso P, in un luogo qualsiasi Q, è accelerato e ritardato nella cicloide (per il Cor. della Prop. LI [del Libro I]) sta al suo peso totale come la sua distanza PQ dal luogo più basso P sta alla lunghezza PR della cicloide.",
     "en": "The force also with which the body P is accelerated or retarded in any place, as Q, of a cycloid, is (by Cor. Prop. LI) to its whole weight as its distance PQ from the lowest place P to the length PR of the cycloid.",
     "dipende_da": [
      "Libro I, Prop. LI, Cor."
     ],
     "figura": {
      "mostra": [
       "Q sulla cicloide"
      ],
      "evidenzia": [
       "forza tangenziale / peso = PQ / PR"
      ]
     },
     "nota": "Il latino non dice *lib. I.*, ma il rimando è al Libro I (§ A.15)."
    },
    {
     "id": "L2-P44-p6",
     "la": "",
     "it": "Perciò le forze motrici dell’acqua e del pendolo, che descrivono spazi uguali AE, PQ, sono come i pesi da muovere; e perciò, se all’inizio l’acqua e il pendolo sono in quiete, quelle forze li muoveranno in egual misura in tempi uguali, e faranno sì che vadano e tornino insieme con moto reciproco.",
     "en": "Therefore the motive forces of the water and pendulum, describing the equal spaces AE, PQ, are as the weights to be moved; and therefore if the water and pendulum are quiescent at first, those forces will move them in equal times, and will cause them to go and return together with a reciprocal motion.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "acqua e pendolo in moto sincrono"
      ],
      "evidenzia": [
       "stessa forza acceleratrice per spazi uguali"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P46",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XLVI — trovare la velocità delle onde",
   "copertura": [
    "II.S8.19",
    "II.S8.20",
    "II.S8.21"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Sect. VIII, Prop. XLVI"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare la velocità delle onde.",
    "en": "To find the velocity of waves."
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
     "ABCDEF superficie ondulata dell’acqua",
     "A, C, E sommità; B, D, F valli",
     "larghezza dell’onda = AC = BD",
     "pendolo di lunghezza uguale alla larghezza; pendolo ausiliario di lunghezza un quarto"
    ]
   },
   "passi": [
    {
     "id": "L2-P46-p1",
     "la": "",
     "it": "Si costruisca un pendolo la cui lunghezza, fra il punto di sospensione e il centro di oscillazione, sia uguale alla larghezza delle onde: nel tempo in cui quel pendolo compie le singole oscillazioni, le onde, avanzando, percorreranno all’incirca la loro larghezza.",
     "en": "Let a pendulum be constructed, whose length between the point of suspension and the centre of oscillation is equal to the breadth of the waves and in the time that the pendulum will perform one single oscillation the waves will advance forward nearly a space equal to their breadth.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "pendolo di lunghezza AC"
      ],
      "evidenzia": [
       "costruzione-risposta"
      ]
     }
    },
    {
     "id": "L2-P46-p2",
     "la": "",
     "it": "Chiamo larghezza delle onde la misura trasversale che sta fra i fondi delle valli, oppure fra le sommità più alte.",
     "en": "That which I call the breadth of the waves is the transverse measure lying between the deepest part of the hollows, or the tops of the ridges.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "larghezza fra due valli o due sommità"
      ]
     },
     "nota": "La «larghezza» è la lunghezza d’onda (nota N2, N7); Motte è ambiguo (§ A.6)."
    },
    {
     "id": "L2-P46-p3",
     "la": "",
     "it": "Rappresenti ABCDEF la superficie di un’acqua stagnante che sale e scende in onde successive; e siano A, C, E, ecc. le sommità delle onde, e B, D, F, ecc. le valli intermedie.",
     "en": "Let ABCDEF represent the surface of stagnant water ascending and descending in successive waves; and let A, C, E, &c., be the tops of the waves; and let B, D, F, &c., be the intermediate hollows.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A",
       "B",
       "C",
       "D",
       "E",
       "F",
       "superficie ABCDEF"
      ]
     }
    },
    {
     "id": "L2-P46-p4",
     "la": "",
     "it": "E poiché il moto delle onde avviene per la salita e la discesa successive dell’acqua, così che le sue parti A, C, E, ecc., che ora sono le più alte, diventano subito dopo le più basse; e la forza motrice con cui le parti più alte scendono e le più basse salgono è il peso dell’acqua sollevata; quella salita e discesa alterna sarà analoga al moto reciproco dell’acqua nel canale e osserverà le stesse leggi quanto al tempo; e perciò (per la Prop. XLIV), se le distanze fra i luoghi più alti delle onde A, C, E e i più bassi B, D, F sono uguali al doppio della lunghezza del pendolo, le parti più alte A, C, E diventeranno le più basse nel tempo di una oscillazione, e nel tempo di un’altra oscillazione risaliranno.",
     "en": "Because the motion of the waves is carried on by the successive ascent and descent of the water, so that the parts thereof, as A, C, E, &c., which are highest at one time become lowest immediately after; and because the motive force, by which the highest parts descend and the lowest ascend, is the weight of the elevated water, that alternate ascent and descent will be analogous to the reciprocal motion of the water in the canal, and observe the same laws as to the times of its ascent and descent; and therefore (by Prop. XLIV) if the distances between the highest places of the waves A, C, E, and the lowest B, D, F, be equal to twice the length of any pendulum, the highest parts A, C, E, will become the lowest in the time of one oscillation, and in the time of another oscillation will ascend again.",
     "dipende_da": [
      "Prop. XLIV"
     ],
     "figura": {
      "mostra": [
       "distanza AB (cresta–valle)",
       "pendolo ausiliario di lunghezza AB/2"
      ],
      "evidenzia": [
       "analogia con il canale della Prop. XLIV"
      ]
     },
     "nota": "Motte aggiunge «any» (pendulum)."
    },
    {
     "id": "L2-P46-p5",
     "la": "",
     "it": "Dunque fra il passaggio di un’onda e quello della successiva il tempo sarà di due oscillazioni; cioè l’onda descriverà la sua larghezza nel tempo in cui quel pendolo oscilla due volte; ma nello stesso tempo un pendolo di lunghezza quadrupla, e perciò uguale alla larghezza delle onde, oscillerà una volta.",
     "en": "Therefore between the passage of each wave, the time of two oscillations will intervene; that is, the wave will describe its breadth in the time that pendulum will oscillate twice; but a pendulum of four times that length, and which therefore is equal to the breadth of the waves, will just oscillate once in that time.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "pendolo di lunghezza AC (quadrupla)"
      ],
      "evidenzia": [
       "due oscillazioni del pendolo AB/2 = una del pendolo AC"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P47",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XLVII — le particelle del mezzo oscillano secondo la legge del pendolo",
   "copertura": [
    "II.S8.25",
    "II.S8.26",
    "II.S8.27"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Sect. VIII, Prop. XLVII"
   },
   "enunciato": {
    "la": "",
    "it": "Quando si propagano pulsazioni attraverso un fluido, le singole particelle del fluido, andando e tornando con un moto reciproco brevissimo, sono sempre accelerate e ritardate secondo la legge del pendolo che oscilla.",
    "en": "If pulses are propagated through a fluid, the several particles of the fluid, going and returning with the shortest reciprocal motion, are always accelerated or retarded according to the law of the oscillating pendulum."
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
     "e",
     "f",
     "g",
     "ε",
     "φ",
     "γ",
     "Ω",
     "P",
     "S",
     "O",
     "H",
     "I",
     "K",
     "h",
     "i",
     "k",
     "L",
     "M",
     "N",
     "l",
     "m",
     "n"
    ],
    "vincoli": [
     "AB = BC = CD: distanza fra pulsazioni successive (BC = λ)",
     "E, F, G su AC, equidistanti; Ee = Ff = Gg brevissimi (ampiezza della vibrazione)",
     "PS = Ee; O punto medio di PS; cerchio SIPi di centro O e raggio OP",
     "il tempo di una vibrazione è rappresentato dalla circonferenza intera",
     "H sulla circonferenza al tempo PH; L proiezione di H su PS; Eε = PL",
     "archi HI = IK con HI : circonferenza = EF : BC",
     "M, N proiezioni di I, K su PS",
     "V raggio del cerchio di circonferenza BC (non disegnato)",
     "Ω punto medio di Ff"
    ]
   },
   "passi": [
    {
     "id": "L2-P47-p1",
     "la": "",
     "it": "Rappresentino AB, BC, CD, ecc. le distanze uguali di pulsazioni successive; ABC la direzione del moto delle pulsazioni propagate da A verso B; E, F, G tre punti fisici del mezzo in quiete, situati sulla retta AC a distanze uguali l’uno dall’altro; Ee, Ff, Gg spazi uguali brevissimi attraverso i quali quei punti, con moto reciproco, vanno e tornano a ogni vibrazione; ε, φ, γ luoghi intermedi qualsiasi degli stessi punti; ed EF, FG lineette fisiche, ossia parti lineari del mezzo interposte fra quei punti e trasportate successivamente nei luoghi εφ, φγ ed ef, fg.",
     "en": "Let AB, BC, CD, &c., represent equal distances of successive pulses, ABC the line of direction of the motion of the successive pulses propagated from A to B; E, F, G three physical points of the quiescent medium situate in the right line AC at equal distances from each other; Ee, Ff, Gg, equal spaces of extreme shortness, through which those points go and return with a reciprocal motion in each vibration; [SVG 925], [SVG 926], [SVG 927], any intermediate places of the same points; EF, FG physical lineolæ, or linear parts of the medium lying between those points, and successively transferred into the places [SVG 928], [SVG 929], and ef, fg.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A",
       "B",
       "C",
       "D",
       "E",
       "F",
       "G",
       "e",
       "f",
       "g",
       "ε",
       "φ",
       "γ",
       "lineette EF, FG"
      ],
      "evidenzia": [
       "E, F, G equidistanti; Ee = Ff = Gg"
      ]
     },
     "nota": "SVG 925–929 = ε, π [sic: φ], γ, εφ, φγ: l’immagine 926 di Motte 1846 ha π per φ (refuso, § A.13)."
    },
    {
     "id": "L2-P47-p2",
     "la": "",
     "it": "Si conduca la retta PS uguale alla retta Ee.",
     "en": "Let there be drawn the right line PS equal to the right line Ee.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "P",
       "S",
       "PS"
      ],
      "evidenzia": [
       "PS = Ee"
      ]
     }
    },
    {
     "id": "L2-P47-p3",
     "la": "",
     "it": "La si divida a metà in O, e con centro O e raggio OP si descriva il cerchio SIPi.",
     "en": "Bisect the same in O, and from the centre O, with the interval OP, describe the circle SIPi.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "O",
       "cerchio SIPi"
      ]
     }
    },
    {
     "id": "L2-P47-p4",
     "la": "",
     "it": "Con la sua circonferenza intera e con le sue parti si rappresenti il tempo intero di una vibrazione con le sue parti proporzionali; così che, compiuto un tempo qualsiasi PH o PHSh, se si abbassa su PS la perpendicolare HL o hl e si prende Eε uguale a PL o Pl, il punto fisico E si trovi in ε.",
     "en": "Let the whole time of one vibration; with its proportional parts, be expounded by the whole circumference of this circle and its parts, in such sort, that, when any time PH or PHSh is completed, if there be let fall to PS the perpendicular HL or hl, and there be taken [SVG 930] equal to PL or Pl, the physical point E may be found in [SVG 925].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "H",
       "h",
       "L",
       "l",
       "HL ⊥ PS"
      ],
      "evidenzia": [
       "Eε = PL: cerchio di riferimento del moto armonico"
      ]
     },
     "nota": "SVG 930 = Eε, SVG 925 = ε (controllati)."
    },
    {
     "id": "L2-P47-p5",
     "la": "",
     "it": "Con questa legge un punto qualsiasi E, andando da E per ε fino a e, e di lì tornando per ε fino a E, compirà le singole vibrazioni con gli stessi gradi di accelerazione e di ritardo di un pendolo che oscilla.",
     "en": "A point, as E, moving according to this law with a reciprocal motion in its going from E through [SVG 925] to e, and returning again through [SVG 925] to E, will perform its several vibrations with the same degrees of acceleration and retardation with those of an oscillating pendulum.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "moto di E fra E ed e"
      ],
      "evidenzia": [
       "moto armonico"
      ]
     }
    },
    {
     "id": "L2-P47-p6",
     "la": "",
     "it": "Si deve provare che i singoli punti fisici del mezzo devono essere agitati con un moto siffatto.",
     "en": "We are now to prove that the several physical points of the medium will be agitated with such a kind of motion.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     }
    },
    {
     "id": "L2-P47-p7",
     "la": "",
     "it": "Immaginiamo dunque che il mezzo sia messo in moto in questo modo da una causa qualsiasi, e vediamo che cosa ne segue.",
     "en": "Let us suppose, then, that a medium hath such a motion excited in it from any cause whatsoever, and consider what will follow from thence.",
     "dipende_da": [],
     "figura": {
      "mostra": []
     },
     "nota": "Verifica di coerenza, non deduzione (nota N9)."
    },
    {
     "id": "L2-P47-p8",
     "la": "",
     "it": "Sulla circonferenza PHSh si prendano archi uguali HI, IK, o hi, ik, che abbiano con la circonferenza intera lo stesso rapporto che le rette uguali EF, FG hanno con l’intervallo intero delle pulsazioni BC.",
     "en": "In the circumference PHSh let there be taken the equal arcs, HI, IK, or hi, ik, having the same ratio to the whole circumference as the equal right lines EF, FG have to BC, the whole interval of the pulses.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "I",
       "K",
       "i",
       "k",
       "archi HI, IK"
      ],
      "evidenzia": [
       "HI : circonferenza = EF : BC (sfasamento)"
      ]
     }
    },
    {
     "id": "L2-P47-p9",
     "la": "",
     "it": "E si abbassino le perpendicolari IM, KN, o im, kn. Poiché i punti E, F, G sono agitati successivamente da moti simili e compiono le loro vibrazioni intere, composte di andata e ritorno, nel tempo in cui la pulsazione è trasportata da B a C, se PH o PHSh è il tempo dall’inizio del moto del punto E, PI o PHSi sarà il tempo dall’inizio del moto del punto F, e PK o PHSk il tempo dall’inizio del moto del punto G; e perciò Eε, Fφ, Gγ saranno uguali rispettivamente a PL, PM, PN nell’andata dei punti, oppure a Pl, Pn, Pm [sic: Pl, Pm, Pn] nel ritorno dei punti.",
     "en": "Let fall the perpendiculars IM, KN, or im, kn; then because the points E, F, G are successively agitated with like motions, and perform their entire vibrations composed of their going and return, while the pulse is transferred from B to C; if PH or PHSh be the time elapsed since the beginning of the motion of the point E, then will PI or PHSi be the time elapsed since the beginning of the motion of the point F, and PK or PHSk the time elapsed since the beginning of the motion of the point G; and therefore [SVG 930], [SVG 931], [SVG 932], will be respectively equal to PL, PM, PN, while the points are going, and to Pl, Pm, Pn, when the points are returning.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "M",
       "N",
       "m",
       "n",
       "IM, KN ⊥ PS"
      ],
      "evidenzia": [
       "Eε = PL, Fφ = PM, Gγ = PN"
      ]
     },
     "nota": "Latino *Pl, Pn, Pm*, Motte *Pl, Pm, Pn* (ordine atteso)."
    },
    {
     "id": "L2-P47-p10",
     "la": "",
     "it": "Di qui εγ, ossia EG + Gγ − Eε, nell’andata dei punti sarà uguale a EG − LN, nel ritorno invece a EG + ln.",
     "en": "Therefore [SVG 933] or [SVG 934] will, when the points are going, be equal to EG - LN and in their return equal to EG + ln.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "εγ",
       "LN"
      ],
      "evidenzia": [
       "εγ = EG − LN"
      ]
     }
    },
    {
     "id": "L2-P47-p11",
     "la": "",
     "it": "Ma εγ è la larghezza, ossia l’espansione, della parte EG del mezzo nel luogo εγ; e perciò l’espansione di quella parte nell’andata sta alla sua espansione media come EG − LN sta a EG; nel ritorno, invece, come EG + ln, ossia EG + LN, sta a EG.",
     "en": "But [SVG 933] is the breadth or expansion of the part EG of the medium in the place [SVG 933]; and therefore the expansion of that part in its going is to its mean expansion as EG - LN to EG; and in its return, as EG + ln or EG + LN to EG.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "espansione : espansione media = (EG − LN) : EG"
      ]
     }
    },
    {
     "id": "L2-P47-p12",
     "la": "",
     "it": "Perciò, poiché LN sta a KH come IM sta al raggio OP, e KH sta a EG come la circonferenza PHShP sta a BC, cioè, se si pone V per il raggio del cerchio la cui circonferenza è uguale all’intervallo delle pulsazioni BC, come OP sta a V; ed ex æquo LN sta a EG come IM sta a V: l’espansione della parte EG, ossia del punto fisico F, nel luogo εγ starà all’espansione media che quella parte ha nel suo primo luogo EG come V − IM sta a V nell’andata, e come V + im sta a V nel ritorno.",
     "en": "Therefore since LN is to KH as IM to the radius OP, and KH to EG as the circumference PHShP to BC; that is, if we put V for the radius of a circle whose circumference is equal to BC the interval of the pulses, as OP to V; and, ex æquo, LN to EG as IM to V; the expansion of the part EG, or of the physical point F in the place [SVG 933], to the mean expansion of the same part in its first place EG, will be as V - IM to V in going, and as V + im to V in its return.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "corda HK",
       "V (raggio ausiliario)"
      ],
      "evidenzia": [
       "LN : KH = IM : OP",
       "LN : EG = IM : V"
      ]
     }
    },
    {
     "id": "L2-P47-p13",
     "la": "",
     "it": "Di qui la forza elastica del punto F nel luogo εγ sta alla sua forza elastica media nel luogo EG come 1/(V − IM) sta a 1/V nell’andata; nel ritorno, invece, come 1/(V + im) sta a 1/V.",
     "en": "Hence the elastic force of the point F in the place [SVG 933] to its mean elastic force in the place EG is as [SVG 935] to [SVG 936] in its going, and as [SVG 937] to [SVG 936] in its return.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "forza elastica inversamente come l’espansione (Boyle)"
      ]
     },
     "nota": "Frazioni appiattite «1V−IM» = 1/(V−IM); SVG 935–937 = 1/(V−IM), 1/V, 1/(V+im) (controllati)."
    },
    {
     "id": "L2-P47-p14",
     "la": "",
     "it": "E con lo stesso argomento le forze elastiche dei punti fisici E e G nell’andata stanno come 1/(V − HL) e 1/(V − KN) a 1/V; e la differenza delle forze sta alla forza elastica media del mezzo come (HL − KN)/(VV − V × HL − V × KN + HL × KN) sta a 1/V.",
     "en": "And by the same reasoning the elastic forces of the physical points E and G in going are as [SVG 938] and [SVG 939] to [SVG 936]; and the difference of the forces to the mean elastic force of the medium as [SVG 940] to [SVG 936];",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "differenza delle forze agli estremi"
      ]
     },
     "nota": "Frazione appiattita: (HL−KN)/(VV−V×HL−V×KN+HL×KN); SVG 938–940."
    },
    {
     "id": "L2-P47-p15",
     "la": "",
     "it": "Cioè come (HL − KN)/VV sta a 1/V, ossia come HL − KN sta a V, purché (per gli stretti limiti delle vibrazioni) supponiamo HL e KN indefinitamente minori della quantità V.",
     "en": "that is, as [SVG 941] to [SVG 936], or as HL - KN to V; if we suppose (by reason of the very short extent of the vibrations) HL and KN to be indefinitely less than the quantity V.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "approssimazione delle piccole vibrazioni"
      ]
     },
     "nota": "Passaggio critico: si trascurano i termini del secondo ordine (nota N9)."
    },
    {
     "id": "L2-P47-p16",
     "la": "",
     "it": "Perciò, poiché la quantità V è data, la differenza delle forze è come HL − KN, cioè (poiché HL − KN sta a HK come OM sta a OI, o a OP, e HK e OP sono date) come OM; cioè, se Ff è divisa a metà in Ω, come Ωφ.",
     "en": "Therefore since the quantity V is given, the difference of the forces is as HL - KN; that is (because HL - KN is proportional to HK, and OM to OI or OP; and because HK and OP are given) as OM; that is, if Ff be bisected in [SVG 942], as [SVG 943].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "OM",
       "Ω (punto medio di Ff)",
       "Ωφ"
      ],
      "evidenzia": [
       "HL − KN : HK = OM : OI",
       "differenza delle forze ∝ Ωφ"
      ]
     },
     "nota": "Motte fraintende *ob proportionales* (§ A.7). SVG 942 = Ω, 943 = Ωφ."
    },
    {
     "id": "L2-P47-p17",
     "la": "",
     "it": "E con lo stesso argomento la differenza delle forze elastiche dei punti fisici ε e γ, nel ritorno della lineetta fisica εγ, è come Ωφ.",
     "en": "And for the same reason the difference of the elastic forces of the physical points [SVG 925] and [SVG 927], in the return of the physical lineola [SVG 933], is as [SVG 943].",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "anche nel ritorno"
      ]
     }
    },
    {
     "id": "L2-P47-p18",
     "la": "",
     "it": "Ma quella differenza (cioè l’eccesso della forza elastica del punto ε sulla forza elastica del punto γ) è la forza da cui la lineetta fisica εγ del mezzo, interposta fra quei punti, è accelerata nell’andata e ritardata nel ritorno; e perciò la forza acceleratrice della lineetta fisica εγ è come la sua distanza dal luogo medio della vibrazione Ω.",
     "en": "But that difference (that is, the excess of the elastic force of the point [SVG 925] above the elastic force of the point [SVG 927]) is the very force by which the intervening physical lineola [SVG 933] of the medium is accelerated in going, and retarded in returning; and therefore the accelerative force of the physical lineola [SVG 933] is as its distance from [SVG 942], the middle place of the vibration.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "forza sulla lineetta εγ"
      ],
      "evidenzia": [
       "forza acceleratrice ∝ distanza da Ω"
      ]
     }
    },
    {
     "id": "L2-P47-p19",
     "la": "",
     "it": "Perciò (per la Prop. XXXVIII del Libro I) il tempo è rappresentato correttamente dall’arco PI; e la parte lineare del mezzo εγ si muove secondo la legge prescritta, cioè secondo la legge del pendolo che oscilla; e lo stesso vale per tutte le parti lineari di cui è composto l’intero mezzo.",
     "en": "Therefore (by Prop. XXXVIII, Book I) the time is rightly expounded by the arc PI; and the linear part of the medium [SVG 933] is moved according to the law above-mentioned, that is, according to the law of a pendulum oscillating; and the case is the same of all the linear parts of which the whole medium is compounded.",
     "dipende_da": [
      "Libro I, Prop. XXXVIII"
     ],
     "figura": {
      "mostra": [
       "arco PI"
      ],
      "evidenzia": [
       "tempo ∝ arco: legge del pendolo"
      ]
     }
    }
   ]
  },
  {
   "id": "L2-P49",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XLIX — trovare la velocità delle pulsazioni",
   "copertura": [
    "II.S8.34",
    "II.S8.35",
    "II.S8.36"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, Sect. VIII, Prop. XLIX"
   },
   "enunciato": {
    "la": "",
    "it": "Date la densità e la forza elastica di un mezzo, trovare la velocità delle pulsazioni.",
    "en": "The density and elastic force of a medium being given, to find the velocity of the pulses."
   },
   "figura_base": {
    "punti": [
     "B",
     "C",
     "E",
     "F",
     "G",
     "P",
     "S",
     "O",
     "H",
     "K"
    ],
    "vincoli": [
     "costruzione della Prop. XLVII (cerchio di diametro PS, centro O)",
     "A: altezza del mezzo omogeneo che equilibra il peso sovrastante (grandezza, non punto)",
     "pendolo di lunghezza A; cerchio di raggio A",
     "V raggio del cerchio di circonferenza BC",
     "nei luoghi estremi K cade in P"
    ]
   },
   "passi": [
    {
     "id": "L2-P49-p1",
     "la": "",
     "it": "Immaginiamo che il mezzo sia compresso da un peso sovrastante, come accade alla nostra aria; e sia A l’altezza di un mezzo omogeneo il cui peso uguagli il peso sovrastante e la cui densità sia la stessa del mezzo compresso in cui si propagano le pulsazioni.",
     "en": "Suppose the medium to be pressed by an incumbent weight after the manner of our air; and let A be the height of a homogeneous medium, whose weight is equal to the incumbent weight, and whose density is the same with the density of the compressed medium in which the pulses are propagated.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "colonna omogenea di altezza A"
      ],
      "evidenzia": [
       "peso della colonna = peso sovrastante"
      ]
     }
    },
    {
     "id": "L2-P49-p2",
     "la": "",
     "it": "Si intenda poi costruito un pendolo la cui lunghezza fra il punto di sospensione e il centro di oscillazione sia A: nel tempo in cui quel pendolo compie un’oscillazione intera, composta di andata e ritorno, la pulsazione, andando, percorrerà uno spazio uguale alla circonferenza del cerchio descritto con raggio A.",
     "en": "Suppose a pendulum to be constructed whose length between the point of suspension and the centre of oscillation is A: and in the time in which that pendulum will perform one entire oscillation composed of its going and returning, the pulse will be propagated right onwards through a space equal to the circumference of a circle described with the radius A.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "pendolo di lunghezza A",
       "cerchio di raggio A"
      ],
      "evidenzia": [
       "costruzione-risposta: v = 2πA / periodo"
      ]
     }
    },
    {
     "id": "L2-P49-p3",
     "la": "",
     "it": "Infatti, restando ferma la costruzione della Prop. XLVII, se una linea fisica qualsiasi EF, descrivendo a ogni vibrazione lo spazio PS, è sollecitata, nei luoghi estremi P e S di ciascuna andata e di ciascun ritorno, da una forza elastica uguale al suo peso, essa compirà le singole vibrazioni nel tempo in cui potrebbe oscillare in una cicloide il cui perimetro totale sia uguale alla lunghezza PS; e ciò perché forze uguali spingeranno nello stesso tempo corpuscoli uguali attraverso spazi uguali.",
     "en": "For, letting those things stand which were constructed in Prop. XLVII, if any physical line, as EF, describing the space PS in each vibration, be acted on in the extremities P and S of every going and return that it makes by an elastic force that is equal to its weight, it will perform its several vibrations in the time in which the same might oscillate in a cycloid whose whole perimeter is equal to the length PS; and that because equal forces will impel equal corpuscles through equal spaces in the same or equal times.",
     "dipende_da": [
      "Prop. XLVII"
     ],
     "figura": {
      "mostra": [
       "P",
       "S",
       "PS",
       "cicloide ausiliaria di perimetro PS"
      ],
      "evidenzia": [
       "forza estrema = peso ⇒ cicloide di perimetro PS"
      ]
     }
    },
    {
     "id": "L2-P49-p4",
     "la": "",
     "it": "Perciò, poiché i tempi delle oscillazioni sono in rapporto subduplicato della lunghezza dei pendoli, e la lunghezza del pendolo è uguale alla metà dell’arco della cicloide intera, il tempo di una vibrazione starebbe al tempo dell’oscillazione del pendolo la cui lunghezza è A in rapporto subduplicato della lunghezza ½PS, ossia PO, alla lunghezza A.",
     "en": "Therefore since the times of the oscillations are in the subduplicate ratio of the lengths of the pendulums, and the length of the pendulum is equal to half the arc of the whole cycloid, the time of one vibration would be to the time of the oscillation of a pendulum whose length is A in the subduplicate ratio of the length [SVG 944] or PO to the length A.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "O",
       "PO = ½PS"
      ],
      "evidenzia": [
       "tempo ∝ √(PO / A)"
      ]
     },
     "nota": "«12PS» = ½PS (frazione appiattita); SVG 944 = ½PS (controllato)."
    },
    {
     "id": "L2-P49-p5",
     "la": "",
     "it": "Ma la forza elastica da cui è sollecitata la lineetta fisica EG, quando si trova nei suoi luoghi estremi P, S, stava (nella dimostrazione della Prop. XLVII) alla sua forza elastica totale come HL − KN sta a V, cioè (poiché il punto K cade ora in P) come HK sta a V; e quella forza totale, cioè il peso sovrastante da cui la lineetta EG è compressa, sta al peso della lineetta come l’altezza A del peso sovrastante sta alla lunghezza EG della lineetta; e perciò, ex æquo, la forza da cui la lineetta EG è sollecitata nei suoi luoghi P e S sta al peso di quella lineetta come HK × A sta a V × EG, ossia come PO × A sta a VV, perché HK stava a EG come PO sta a V.",
     "en": "But the elastic force with which the physical lineola EG is urged, when it is found in its extreme places P, S, was (in the demonstration of Prop. XLVII) to its whole elastic force as HL - KN to V, that is (since the point K now falls upon P), as HK to V: and all that force, or which is the same thing, the incumbent weight by which the lineola EG is compressed, is to the weight of the lineola as the altitude A of the incumbent weight to EG the length of the lineola; and therefore, ex æquo, the force with which the lineola EG is urged in the places P and S is to the weight of that lineola as HK × A to V × EG; or as PO × A to VV; because HK was to EG as PO to V.",
     "dipende_da": [
      "Prop. XLVII"
     ],
     "figura": {
      "mostra": [
       "H",
       "K in P",
       "lineetta EG"
      ],
      "evidenzia": [
       "forza estrema : peso = PO × A : VV"
      ]
     },
     "nota": "Il latino passa da EF a EG; così anche Motte (§ A.9)."
    },
    {
     "id": "L2-P49-p6",
     "la": "",
     "it": "Perciò, poiché i tempi in cui corpi uguali sono spinti attraverso spazi uguali sono inversamente in rapporto subduplicato delle forze, il tempo di una vibrazione, sotto l’azione di quella forza elastica, starà al tempo di una vibrazione sotto l’azione della forza del peso in rapporto subduplicato di VV a PO × A, e quindi al tempo dell’oscillazione del pendolo la cui lunghezza è A nel rapporto subduplicato di VV a PO × A e nel rapporto subduplicato di PO ad A, considerati congiuntamente; cioè nel rapporto intero di V ad A.",
     "en": "Therefore since the times in which equal bodies are impelled through equal spaces are reciprocally in the subduplicate ratio of the forces, the time of one vibration, produced by the action of that elastic force, will be to the time of a vibration, produced by the impulse of the weight in a subduplicate ratio of VV to PO × A, and therefore to the time of the oscillation of a pendulum whose length is A in the subduplicate ratio of VV to PO × A, and the subduplicate ratio of PO to A conjunctly; that is, in the entire ratio of V to A.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "√(VV / (PO × A)) × √(PO / A) = V / A"
      ]
     },
     "nota": "Motte aggiunge «impulse» per *urgente vi ponderis*."
    },
    {
     "id": "L2-P49-p7",
     "la": "",
     "it": "Ma nel tempo di una vibrazione composta di andata e ritorno la pulsazione, avanzando, percorre la sua larghezza BC.",
     "en": "But in the time of one vibration composed of the going and returning of the pendulum, the pulse will be propagated right onward through a space equal to its breadth BC.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "B",
       "C",
       "BC"
      ],
      "evidenzia": [
       "in una vibrazione la pulsazione avanza di BC"
      ]
     },
     "nota": "Errore di Motte: «of the pendulum» non è nel latino; la vibrazione è della lineetta del mezzo (§ A.9)."
    },
    {
     "id": "L2-P49-p8",
     "la": "",
     "it": "Dunque il tempo in cui la pulsazione percorre lo spazio BC sta al tempo di una oscillazione composta di andata e ritorno come V sta ad A, cioè come BC sta alla circonferenza del cerchio il cui raggio è A.",
     "en": "Therefore the time in which a pulse runs over the space BC is to the time of one oscillation composed of the going and returning of the pendulum as V to A, that is, as BC to the circumference of a circle whose radius is A.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio di raggio A"
      ],
      "evidenzia": [
       "V : A = BC : 2πA"
      ]
     }
    },
    {
     "id": "L2-P49-p9",
     "la": "",
     "it": "Ma il tempo in cui la pulsazione percorrerà lo spazio BC sta nello stesso rapporto al tempo in cui percorrerà una lunghezza uguale a questa circonferenza; e perciò, nel tempo di una tale oscillazione, la pulsazione percorrerà una lunghezza uguale a questa circonferenza.",
     "en": "But the time in which the pulse will run over the space BC is to the time in which it will run over a length equal to that circumference in the same ratio; and therefore in the time of such an oscillation the pulse will run over a length equal to that circumference.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "v = 2πA / (2π√(A/g)) = √(gA) (nota N10)"
      ]
     }
    }
   ]
  }
 ]
}
```
