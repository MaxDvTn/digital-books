> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 8 — Libro I, Sezioni VI, VII e VIII

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo traduce integralmente tre Sezioni consecutive del Libro I (*De motu corporum*):

- **Sezione VI**, *De inventione motuum in orbibus datis*: Prop. XXX (posizione nella parabola), Lemma XXVIII con il suo corollario (nessun ovale ha area algebricamente determinabile), Prop. XXXI (posizione nell’ellisse per mezzo della trocoide, cioè il problema di Keplero) e lo Scolio con i metodi approssimati;
- **Sezione VII**, *De corporum ascensu & descensu rectilineo*: Prop. XXXII–XXXIX con i loro corollari;
- **Sezione VIII**, *De inventione orbium in quibus corpora viribus quibuscunque centripetis agitata revolvuntur*: Prop. XL–XLII con i loro corollari e l’avvertenza finale.

È una traduzione di lavoro, non un’edizione critica validata. Gli identificatori **S6.01–S6.17**, **S7.01–S7.31** e **S8.01–S8.15** e i titoli tematici tra parentesi sono aggiunte editoriali. I numeri romani di proposizioni, problemi, teoremi e lemmi appartengono al testo originale. Le integrazioni del curatore sono tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton.

In coda al fascicolo c’è la **Parte B**, con i dati strutturati per le pagine interattive delle sedici unità che hanno una costruzione geometrica o una figura: Prop. XXX, Lemma XXVIII, Prop. XXXI, Prop. XXXII–XXXIX, Cor. 1 e Cor. 3 della Prop. XXXIX, Prop. XL–XLII.

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro I: Sezione VI, pp. 104–112; Sezione VII, pp. 112–122; Sezione VIII, pp. 123–129 (numeri di pagina tra parentesi angolari nella trascrizione). Trascrizione normalizzata del Newton Project, documento **NATP00087**: <https://www.newtonproject.ox.ac.uk/view/texts/normalized/NATP00087>, nelle copie di lavoro `fonti/latino-1726-L1-S06.md`, `-S07.md`, `-S08.md`, estratte in testo semplice senza correzioni.
2. **Inglese di confronto.** *Newton’s Principia. The Mathematical Principles of Natural Philosophy*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, Project Gutenberg n. 76404, nelle copie `fonti/motte-1846-L1-S06.md`, `-S07.md`, `-S08.md`. Pagine secondo i marcatori `Page_n` dell’EPUB: Sezione VI, pp. 153–159; Sezione VII, pp. 159–168; Sezione VIII, pp. 168–172. L’ultima frase della Sezione VII di Motte («…rectangle 2PD × DL to the area DLme.») si trova all’inizio del file della Sezione VIII. Le formule stampate come immagini (SVG 112–156) sono state rese con `rsvg-convert` e lette una per una.
3. **Fascicolo 3** del progetto (`Newton_Principia_IT_03_Leggi.md`), per il formato, il tono e il glossario, e il **brief comune** dei fascicoli 4–12.

Non ho consultato né riprodotto traduzioni moderne (Cajori, Cohen–Whitman, Pala, Giudice). Non ho potuto vedere né la stampa del 1726 né le figure originali NATP00087-73…99: le relazioni geometriche sono ricostruite soltanto dalle lettere citate nel testo e controllate con figure di prova calcolate (note N1–N15).

### Criteri di traduzione

- Il testo guida è il latino; l’inglese serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o sbaglia.
- Si applica il **glossario comune** del brief (fascicoli 1–3 e termini tecnici del Libro I): «fuoco» (*umbilicus*), «vertice principale», «lato retto», «lato trasverso», «ordinata», «ascissa», «traiettoria», «orbita», «dato di posizione», «tempo periodico», «apside/apsidi», «seno», «seno verso», «corda», «rapporto duplicato / subduplicato», «inversamente», «considerate congiuntamente», «quantità nascenti», «rapporto primo / ultimo», C.V.D., C.V.T., C.V.F.
- Le estensioni proprie del fascicolo sono elencate e motivate nel § A.0. Le principali: *quæ potest aream* «il cui quadrato è uguale all’area»; *latus quadratum* «lato quadrato»; *altitudo* «altezza»; *lineola* «piccola linea»; *componendo / dividendo / ex æquo* «per composizione / per separazione / per uguaglianza»; *æquatio* (in astronomia) «equazione»; *motus medius (æquatus)* «moto medio (equato)»; *trochoides* «trocoide»; *hyperbola rectangula* «iperbole rettangola».
- Gli enunciati all’infinito sono resi con l’indicativo; i problemi con l’infinito italiano («Trovare…», «Determinare…»), come nei titoli latini.
- Nel testo tradotto non compaiono formule moderne. Le espressioni della trascrizione come «AOq», «PE cub.», «12AB» sono scritte AO², PE³, ½AB. Le frazioni appiattite dalla trascrizione sono ricostruite con la barra (per esempio *2CPq×AOACB* = 2CP² × AO/ACB) e dichiarate nell’apparato. I segni di radice che la trascrizione ha perduto nella Sezione VIII sono ristabiliti come √, segno che compare nella stampa inglese di Motte; vedi § A.16.
- Le lettere delle figure restano come nel latino, comprese le minuscole corsive (c, d, f, k, e, g, m, q, p, r, b, v, w, x, y, z).

---

## Traduzione italiana

## Sezione VI. La determinazione dei moti in orbite date

### Proposizione XXX. Problema XXII (il luogo nella parabola)

**[S6.01]** **Trovare il luogo, a un tempo assegnato, di un corpo che si muove su una traiettoria parabolica data.**

**[S6.02]** Sia S il fuoco e A il vertice principale della parabola, e sia 4AS × M uguale all’area parabolica APS che il raggio SP o ha descritto dopo che il corpo è uscito dal vertice, o deve descrivere prima che il corpo vi giunga. La grandezza di quell’area da tagliare si conosce dal tempo, che le è proporzionale. Si divida AS a metà in G, si innalzi la perpendicolare GH uguale a 3M, e il cerchio descritto con centro H e raggio HS taglierà la parabola nel luogo cercato P.

**[S6.03]** Infatti, abbassata sull’asse la perpendicolare PO e condotta PH, si ha AG² + GH² (= HP² = (AO − AG)² + (PO − GH)²) = AO² + PO² − 2GAO − 2GH × PO + AG² + GH². Quindi 2GH × PO (= AO² + PO² − 2GAO) = AO² + ¾PO². Al posto di AO² si scriva AO × PO²/4AS; e, divisi tutti i termini per 3PO e moltiplicati per 2AS, si avrà (4/3)GH × AS (= ⅙AO × PO + ½AS × PO = (AO + 3AS)/6 × PO = (4AO − 3SO)/6 × PO = area APO − SPO) = area APS. Ma GH era 3M, e quindi (4/3)GH × AS è 4AS × M. Dunque l’area APS è uguale all’area da tagliare 4AS × M. C.V.D.

**[S6.04]** *Cor. 1.* Di qui GH sta ad AS come il tempo in cui il corpo ha descritto l’arco AP sta al tempo in cui il corpo ha descritto l’arco compreso fra il vertice A e la perpendicolare all’asse innalzata dal fuoco S.

**[S6.05]** *Cor. 2.* E, se un cerchio ASP passa sempre per il corpo in moto, la velocità del punto H sta alla velocità che il corpo aveva nel vertice A come 3 sta a 8; e perciò nello stesso rapporto sta la linea GH alla retta che il corpo, nel tempo del suo moto da A a P, potrebbe descrivere con la velocità che aveva nel vertice A.

**[S6.06]** *Cor. 3.* Di qui si può anche, viceversa, trovare il tempo in cui il corpo ha descritto un arco qualsiasi assegnato AP. Si congiunga AP e nel suo punto medio si innalzi la perpendicolare, che incontri la retta GH in H.

### Lemma XXVIII (nessun ovale ha area determinabile con equazioni finite)

**[S6.07]** **Non esiste alcuna figura ovale la cui area, tagliata da rette a piacere, si possa trovare in generale per mezzo di equazioni finite quanto al numero dei termini e delle dimensioni.**

**[S6.08]** All’interno dell’ovale sia dato un punto qualsiasi, attorno al quale, come attorno a un polo, ruoti senza sosta una linea retta con moto uniforme; e intanto su quella retta un punto mobile esca dal polo e proceda sempre con una velocità che sia come il quadrato della parte di quella retta interna all’ovale. Con questo moto quel punto descriverà una spirale con infinite spire. Ora, se la porzione dell’area dell’ovale tagliata da quella retta si può trovare per mezzo di un’equazione finita, per mezzo della stessa equazione si troverà anche la distanza del punto dal polo, che è proporzionale a quest’area; perciò tutti i punti della spirale si possono trovare per mezzo di un’equazione finita, e quindi anche l’intersezione con la spirale di una retta qualsiasi data di posizione si può trovare per mezzo di un’equazione finita. Ma ogni retta prolungata all’infinito taglia la spirale in un numero infinito di punti; e l’equazione con cui si trova un’intersezione qualsiasi di due linee mostra tutte le loro intersezioni con altrettante radici, e perciò sale a tante dimensioni quante sono le intersezioni. Poiché due cerchi si tagliano a vicenda in due punti, una delle intersezioni non si troverà se non per mezzo di un’equazione di due dimensioni, con la quale si trovi anche l’altra intersezione. Poiché due sezioni coniche possono avere quattro intersezioni, nessuna di esse si può trovare in generale se non per mezzo di un’equazione di quattro dimensioni, con la quale si trovino tutte insieme. Se infatti quelle intersezioni si cercano separatamente, poiché la legge e la condizione di tutte è la stessa, il calcolo sarà lo stesso in ciascun caso, e perciò sempre la stessa la conclusione, che dunque deve comprendere tutte le intersezioni insieme e mostrarle indifferentemente. Di qui anche le intersezioni delle sezioni coniche con le curve della terza potenza, poiché possono essere sei, risultano insieme per mezzo di equazioni di sei dimensioni; e le intersezioni di due curve della terza potenza, poiché possono essere nove, risultano insieme per mezzo di equazioni di nove dimensioni. Se ciò non avvenisse necessariamente, si potrebbero ridurre tutti i problemi solidi a piani, e quelli più che solidi a solidi. Parlo qui di curve irriducibili quanto alla potenza. Se infatti l’equazione per cui la curva è definita si può ridurre a una potenza inferiore, la curva non sarà unica, ma composta di due o più curve, le cui intersezioni si possono trovare separatamente con calcoli diversi. Allo stesso modo le due intersezioni delle rette con le sezioni coniche risultano sempre per mezzo di equazioni di due dimensioni; le tre delle rette con le curve irriducibili [della terza potenza per mezzo di equazioni di tre dimensioni; le quattro delle rette con le curve irriducibili] della quarta potenza per mezzo di equazioni di quattro dimensioni; e così all’infinito. Dunque le intersezioni, in numero infinito, della retta e della spirale, poiché questa curva è semplice e non riducibile a più curve, richiedono equazioni infinite quanto al numero delle dimensioni e delle radici, con le quali si possano mostrare tutte insieme. È infatti la stessa per tutte la legge, e lo stesso il calcolo. Se infatti dal polo si abbassa la perpendicolare sulla retta secante, e quella perpendicolare ruota attorno al polo insieme con la secante, le intersezioni della spirale passeranno l’una nell’altra: quella che era la prima, cioè la più vicina, dopo una rivoluzione sarà la seconda, dopo due la terza, e così via; né intanto l’equazione muterà, se non per il mutare della grandezza delle quantità mediante le quali si determina la posizione della secante. Perciò, poiché quelle quantità dopo ogni rivoluzione ritornano alle grandezze iniziali, l’equazione ritornerà alla forma iniziale; e quindi una sola e medesima equazione mostrerà tutte le intersezioni, e avrà perciò un numero infinito di radici, con le quali si possano mostrare tutte. Non si può dunque trovare in generale l’intersezione della retta e della spirale per mezzo di un’equazione finita; e perciò non esiste alcun ovale la cui area, tagliata da rette prescritte, si possa esprimere in generale per mezzo di una tale equazione.

**[S6.09]** Con lo stesso argomento, se la distanza fra il polo e il punto che descrive la spirale si prende proporzionale al perimetro tagliato dell’ovale, si può provare che la lunghezza del perimetro non si può esprimere in generale per mezzo di un’equazione finita. Parlo qui, però, di ovali che non sono toccati da figure coniugate che proseguono all’infinito.

**[S6.10]** *Corollario.* Di qui l’area dell’ellisse descritta dal raggio condotto dal fuoco al corpo in moto non si ricava dal tempo dato per mezzo di un’equazione finita; e perciò non si può determinare per mezzo della descrizione di curve geometricamente razionali. Chiamo geometricamente razionali le curve i cui punti si possono tutti determinare per mezzo di lunghezze definite da equazioni, cioè per mezzo di rapporti composti di lunghezze; e chiamo geometricamente irrazionali le altre (come le spirali, le quadratrici, le trocoidi). Infatti le lunghezze che stanno o non stanno fra loro come un numero a un numero (come nel decimo libro degli *Elementi*) sono aritmeticamente razionali o irrazionali. Taglio dunque l’area dell’ellisse proporzionale al tempo per mezzo di una curva geometricamente irrazionale, come segue.

### Proposizione XXXI. Problema XXIII (il luogo nell’ellisse: la trocoide)

**[S6.11]** **Trovare il luogo, a un tempo assegnato, di un corpo che si muove su una traiettoria ellittica data.**

**[S6.12]** Dell’ellisse APB sia A il vertice principale, S il fuoco, O il centro, e sia P il luogo del corpo da trovare. Si prolunghi OA fino a G, in modo che OG stia a OA come OA sta a OS. Si innalzi la perpendicolare GH; con centro O e raggio OG si descriva il cerchio GEF; e sulla riga GH, come su una base, la ruota GEF avanzi girando attorno al proprio asse, e intanto con il suo punto A descriva la trocoide ALI. Fatto ciò, si prenda GK in rapporto al perimetro GEFG della ruota come il tempo in cui il corpo, avanzando da A, ha descritto l’arco AP sta al tempo di una rivoluzione nell’ellisse. Si innalzi la perpendicolare KL, che incontri la trocoide in L, e la LP, condotta parallela a KG, incontrerà l’ellisse nel luogo cercato P del corpo.

**[S6.13]** Infatti, con centro O e raggio OA si descriva il semicerchio AQB; LP, prolungata se occorre, incontri l’arco AQ in Q, e si congiungano SQ, OQ. OQ incontri l’arco EFG in F, e su OQ si abbassi la perpendicolare SR. L’area APS è come l’area AQS, cioè come la differenza fra il settore OQA e il triangolo OQS, ossia come la differenza dei rettangoli ½OQ × AQ e ½OQ × SR, cioè, essendo dato ½OQ, come la differenza fra l’arco AQ e la retta SR; e perciò (poiché sono uguali i rapporti dati di SR al seno dell’arco AQ, di OS a OA, di OA a OG, di AQ a GF, e, per separazione, di AQ − SR a GF − seno dell’arco AQ) come GK, differenza fra l’arco GF e il seno dell’arco AQ. C.V.D.

### Scolio (soluzioni approssimate: ellisse, iperbole, calcolo astronomico)

**[S6.14]** Del resto, poiché la descrizione di questa curva è difficile, conviene usare una soluzione prossima al vero. Si trovino sia un certo angolo B, che stia all’angolo di 57,29578 gradi, sotteso da un arco uguale al raggio, come la distanza dei fuochi SH sta al diametro AB dell’ellisse, sia una certa lunghezza L, che stia al raggio nello stesso rapporto, inversamente. Trovati questi una volta per tutte, il problema si risolve poi con l’analisi seguente. Con una costruzione qualsiasi, o anche facendo comunque una congettura, si conosca un luogo P del corpo prossimo al suo luogo vero p. Abbassata sull’asse dell’ellisse l’ordinata PR, dalla proporzione dei diametri dell’ellisse sarà data l’ordinata RQ del cerchio circoscritto AQB, che è il seno dell’angolo AOQ, preso AO come raggio, e che taglia l’ellisse in P. Basta trovare quell’angolo con un calcolo rozzo, in numeri prossimi al vero. Si conosca anche l’angolo proporzionale al tempo, cioè quello che sta a quattro retti come il tempo in cui il corpo ha descritto l’arco AP sta al tempo di una rivoluzione nell’ellisse. Sia N quest’angolo. Poi si prendano l’angolo D, che stia all’angolo B come quel seno dell’angolo AOQ sta al raggio, e l’angolo E, che stia all’angolo N − AOQ + D come la lunghezza L sta alla stessa lunghezza L diminuita del coseno dell’angolo AOQ quando quest’angolo è minore di un retto, aumentata quando è maggiore. In seguito si prendano l’angolo F, che stia all’angolo B come il seno dell’angolo AOQ + E sta al raggio, e l’angolo G, che stia all’angolo N − AOQ − E + F come la lunghezza L sta alla stessa lunghezza diminuita del coseno dell’angolo AOQ + E quando quest’angolo è minore di un retto, aumentata quando è maggiore. La terza volta si prendano l’angolo H, che stia all’angolo B come il seno dell’angolo AOQ + E + G sta al raggio, e l’angolo I, che stia all’angolo N − AOQ − E − G + H come la lunghezza L sta alla stessa lunghezza diminuita del coseno dell’angolo AOQ + E + G, quando quest’angolo è minore di un retto, aumentata quando è maggiore. E così si può procedere all’infinito. Infine si prenda l’angolo AOq uguale all’angolo AOQ + E + G + I + ecc.; e dal suo coseno Or e dall’ordinata pr, che sta al suo seno qr come l’asse minore dell’ellisse sta all’asse maggiore, si avrà il luogo corretto p del corpo. Se talvolta l’angolo N − AOQ + D è negativo, il segno + di E deve essere mutato ovunque in −, e il segno − in +. Lo stesso si deve intendere dei segni di G e di I, quando gli angoli N − AOQ − E + F e N − AOQ − E − G + H risultano negativi. La serie infinita AOQ + E + G + I + ecc. converge poi rapidissimamente, tanto che quasi mai sarà necessario procedere oltre il secondo termine E. E il calcolo si fonda su questo teorema: che l’area APS è come la differenza fra l’arco AQ e la retta abbassata perpendicolarmente dal fuoco S sul raggio OQ.

**[S6.15]** Con un calcolo non dissimile si risolve il problema nell’iperbole. Sia O il suo centro, A il vertice, S il fuoco e OK l’asintoto. Si conosca la grandezza dell’area da tagliare, proporzionale al tempo. Sia essa A, e si faccia una congettura sulla posizione della retta SP che tagli un’area APS prossima a quella vera. Si congiunga OP, e da A e da P si conducano verso l’asintoto AI, PK, parallele all’altro asintoto: per mezzo della tavola dei logaritmi sarà data l’area AIKP, e uguale a essa l’area OPA, che, sottratta dal triangolo OPS, lascerà l’area tagliata APS. Applicando alla linea SN, che dal fuoco S è perpendicolare alla tangente TP, il doppio della differenza fra l’area da tagliare A e l’area tagliata APS, 2APS − 2A o 2A − 2APS, risulterà la lunghezza della corda PQ. Si inscriva poi quella corda PQ fra A e P se l’area tagliata APS è maggiore dell’area da tagliare A, altrimenti dalla parte opposta del punto P: e il punto Q sarà un luogo più accurato del corpo. E ripetendo il calcolo lo si troverà sempre più accurato, senza fine.

**[S6.16]** E con questi calcoli il problema si risolve in generale per via analitica. Ma per gli usi astronomici è più adatto il calcolo particolare che segue. Essendo AO, OB, OD i semiassi dell’ellisse, L il suo lato retto e D la differenza fra il semiasse minore OD e la metà ½L del lato retto, si cerchino sia l’angolo Y, il cui seno stia al raggio come il rettangolo sotto quella differenza D e la semisomma degli assi AO + [OD] sta al quadrato dell’asse maggiore AB, sia l’angolo Z, il cui seno stia al raggio come il doppio rettangolo sotto la distanza dei fuochi SH e quella differenza D sta al triplo del quadrato del semiasse maggiore AO. Trovati una volta questi angoli, il luogo del corpo si determinerà poi così. Si prenda l’angolo T proporzionale al tempo in cui è stato descritto l’arco BP, ossia uguale al moto medio (come lo chiamano); e l’angolo V, prima equazione del moto medio, che stia all’angolo Y, prima equazione massima, come il seno del doppio dell’angolo T sta al raggio; e l’angolo X, seconda equazione, che stia all’angolo Z, seconda equazione massima, come il cubo del seno dell’angolo T sta al cubo del raggio. Si prenda l’angolo BHP, moto medio equato, uguale alla somma T + X + V degli angoli T, V, X, se l’angolo T è minore di un retto, oppure alla differenza T + X − V, se esso è maggiore di un retto e minore di due retti; e se HP incontra l’ellisse in P, la SP condotta taglierà l’area BSP proporzionale al tempo con ottima approssimazione. Questo procedimento sembra abbastanza spedito, poiché degli angoli piccolissimi V e X, espressi, se si vuole, in secondi, basta trovare le prime due o tre cifre. Ed è anche abbastanza accurato per la teoria dei pianeti. Infatti, anche nell’orbita di Marte, la cui equazione del centro massima è di dieci gradi, l’errore supererà a stento un secondo. Trovato poi l’angolo BHP del moto medio equato, l’angolo BSP del moto vero e la distanza SP si hanno subito con il notissimo metodo di Ward.

**[S6.17]** Fin qui del moto dei corpi su linee curve. Può però accadere che un mobile scenda o salga in linea retta; e passo ora a esporre ciò che riguarda moti di questo genere.

## Sezione VII. La salita e la discesa rettilinea dei corpi

### Proposizione XXXII. Problema XXIV (caduta rettilinea con forza inversa del quadrato)

**[S7.01]** **Posto che la forza centripeta sia inversamente proporzionale al quadrato della distanza dei luoghi dal centro, definire gli spazi che un corpo, cadendo in linea retta, descrive in tempi dati.**

**[S7.02]** *Caso 1.* Se il corpo non cade perpendicolarmente, esso descriverà (per il Cor. 1 della Prop. XIII) una sezione conica il cui fuoco coincide con il centro delle forze. Sia ARPB quella sezione conica e S il suo fuoco. E in primo luogo, se la figura è un’ellisse, sul suo asse maggiore AB si descriva il semicerchio ADB, e per il corpo che cade passi la retta DPC perpendicolare all’asse; condotte DS, PS, l’area ASD sarà proporzionale all’area ASP, e perciò anche al tempo. Restando fisso l’asse AB, si diminuisca continuamente la larghezza dell’ellisse, e l’area ASD resterà sempre proporzionale al tempo. Si diminuisca quella larghezza all’infinito: e, quando l’orbita APB coincide ormai con l’asse AB e il fuoco S con l’estremo B dell’asse, il corpo scenderà lungo la retta AC, e l’area ABD diventerà proporzionale al tempo. Sarà dato dunque lo spazio AC che il corpo, cadendo perpendicolarmente dal luogo A, descrive in un tempo dato, purché si prenda l’area ABD proporzionale al tempo e dal punto D si abbassi sulla retta AB la perpendicolare DC. C.V.T.

**[S7.03]** *Caso 2.* Se la figura RPB è un’iperbole, sullo stesso diametro principale AB si descriva l’iperbole rettangola BED; e poiché le aree CSP, CBfP, SPfB stanno alle aree CSD, CBED, SDEB, ciascuna alla corrispondente, nel rapporto dato delle altezze CP, CD, e l’area SPfB è proporzionale al tempo in cui il corpo P si muoverà lungo l’arco PfB, anche l’area SDEB sarà proporzionale allo stesso tempo. Si diminuisca all’infinito il lato retto dell’iperbole RPB, restando fisso il lato trasverso: l’arco PB verrà a coincidere con la retta CB, il fuoco S con il vertice B e la retta SD con la retta BD. Di conseguenza l’area BDEB sarà proporzionale al tempo in cui il corpo C, con discesa rettilinea, descrive la linea CB. C.V.T.

**[S7.04]** *Caso 3.* E con un argomento simile, se la figura RPB è una parabola, e con lo stesso vertice principale B si descrive un’altra parabola BED, che resti sempre data mentre la prima parabola, sul cui perimetro si muove il corpo P, diminuito e ridotto a nulla il suo lato retto, viene a coincidere con la linea CB, il segmento parabolico BDEB diventerà proporzionale al tempo in cui quel corpo P, o C, scenderà al centro S, o B. C.V.T.

### Proposizione XXXIII. Teorema IX (la velocità nella caduta)

**[S7.05]** **Poste le cose ora trovate, dico che la velocità del corpo che cade, in un luogo qualsiasi C, sta alla velocità di un corpo che descrive un cerchio con centro B e raggio BC in rapporto subduplicato di quello che AC, distanza del corpo dal vertice più lontano A del cerchio o dell’iperbole rettangola, ha con il semidiametro principale della figura, ½AB.**

**[S7.06]** Si divida a metà in O la retta AB, diametro comune delle due figure RPB, DEB; si conduca la retta PT, che tocchi la figura RPB in P e tagli anche quel diametro comune AB (prolungato, se occorre) in T; siano SY perpendicolare a questa retta e BQ perpendicolare a questo diametro, e si ponga L il lato retto della figura RPB. Per il Cor. 9 della Prop. XVI è noto che la velocità di un corpo che si muove sulla linea RPB attorno al centro S, in un luogo qualsiasi P, sta alla velocità di un corpo che descrive un cerchio attorno allo stesso centro alla distanza SP in rapporto subduplicato del rettangolo ½L × SP al quadrato di SY. Ma dalle coniche ACB sta a CP² come 2AO sta a L, e perciò 2CP² × AO/ACB è uguale a L. Dunque quelle velocità stanno fra loro in rapporto subduplicato di CP² × AO × SP/ACB a SY². Inoltre, dalle coniche, CO sta a BO come BO sta a TO, e, per composizione o per separazione, come CB sta a BT. Di qui, per separazione o per composizione, BO − o + CO sta a BO come CT sta a BT, cioè AC sta ad AO come CP sta a BQ; e quindi CP² × AO × SP/ACB è uguale a BQ² × AC × SP/(AO × BC). Si diminuisca ora all’infinito la larghezza CP della figura RPB, in modo che il punto P coincida con il punto C, il punto S con il punto B, la linea SP con la linea BC e la linea SY con la linea BQ: la velocità del corpo che ormai scende in linea retta lungo la linea CB starà alla velocità di un corpo che descrive un cerchio con centro B e raggio BC in rapporto subduplicato di BQ² × AC × SP/(AO × BC) a SY², cioè (trascurati i rapporti di uguaglianza di SP a BC e di BQ² a SY²) in rapporto subduplicato di AC ad AO, ossia a ½AB. C.V.D.

**[S7.07]** *Cor. 1.* Quando i punti B e S coincidono, TC sta a TS come AC sta ad AO.

**[S7.08]** *Cor. 2.* Un corpo che ruota in un cerchio qualsiasi a una distanza data dal centro, se il suo moto è volto verso l’alto, salirà fino al doppio della sua distanza dal centro.

### Proposizione XXXIV. Teorema X (il caso parabolico)

**[S7.09]** **Se la figura BED è una parabola, dico che la velocità del corpo che cade, in un luogo qualsiasi C, è uguale alla velocità con cui un corpo può descrivere uniformemente un cerchio con centro B alla metà della sua distanza BC.**

**[S7.10]** Infatti la velocità di un corpo che descrive la parabola RPB attorno al centro S, in un luogo qualsiasi P (per il Cor. 7 della Prop. XVI), è uguale alla velocità di un corpo che descrive uniformemente un cerchio attorno allo stesso centro S alla metà della distanza SP. Si diminuisca all’infinito la larghezza CP della parabola, in modo che l’arco parabolico PfB coincida con la retta CB, il centro S con il vertice B e la distanza SP con la distanza BC, e la proposizione risulterà evidente. C.V.D.

### Proposizione XXXV. Teorema XI (l’area della figura DES e il moto circolare uniforme)

**[S7.11]** **Poste le stesse cose, dico che l’area della figura DES, descritta dal raggio indefinito SD, è uguale all’area che un corpo, ruotando uniformemente attorno al centro S con raggio uguale alla metà del lato retto della figura DES, può descrivere nello stesso tempo.**

**[S7.12]** Immagina infatti che il corpo C, cadendo, descriva in una particella di tempo piccolissima la piccola linea Cc, e che intanto un altro corpo K, ruotando uniformemente nel cerchio OKk attorno al centro S, descriva l’arco Kk. Si innalzino le perpendicolari CD, cd, che incontrino la figura DES in D, d. Si congiungano SD, Sd, SK, Sk, si conduca Dd, che incontri l’asse AS in T, e su di essa si abbassi la perpendicolare SY.

**[S7.13]** *Caso 1.* Ora, se la figura DES è un cerchio o un’iperbole, si divida a metà in O il suo diametro trasverso AS, e SO sarà la metà del lato retto. E poiché TC sta a TD come Cc sta a Dd, e TD sta a TS come CD sta a SY, per uguaglianza TC sta a TS come CD × Cc sta a SY × Dd. Ma (per il Cor. 1 della Prop. XXXIII) TC sta a TS come AC sta ad AO, s’intende se, nel congiungersi dei punti D, d, si prendono i rapporti ultimi delle linee. Dunque AC sta ad AO, ossia a SK, come CD × Cc sta a SY × Dd. Inoltre la velocità del corpo che scende, in C, sta alla velocità di un corpo che descrive un cerchio attorno al centro S alla distanza SC in rapporto subduplicato di AC ad AO o SK (per la Prop. XXXIII). E questa velocità sta alla velocità del corpo che descrive il cerchio OKk in rapporto subduplicato di SK a SC (per il Cor. 6 della Prop. IV); e, per uguaglianza, la prima velocità sta all’ultima, cioè la piccola linea Cc sta all’arco Kk, in rapporto subduplicato di AC a SC, cioè nel rapporto di AC a CD. Perciò CD × Cc è uguale ad AC × Kk, e di conseguenza AC sta a SK come AC × Kk sta a SY × Dd; quindi SK × Kk è uguale a SY × Dd, e ½SK × Kk è uguale a ½SY × Dd, cioè l’area KSk è uguale all’area SDd. In ogni particella di tempo si generano dunque particelle KSk e SDd delle due aree che, se la loro grandezza diminuisce e il loro numero aumenta all’infinito, ottengono il rapporto di uguaglianza; e perciò (per il corollario del Lemma IV) le aree totali generate insieme sono sempre uguali. C.V.D.

**[S7.14]** *Caso 2.* Se poi la figura DES è una parabola, si troverà, come sopra, che CD × Cc sta a SY × Dd come TC sta a TS, cioè come 2 sta a 1, e quindi che ¼CD × Cc è uguale a ½SY × Dd. Ma la velocità del corpo che cade, in C, è uguale alla velocità con cui si potrebbe descrivere uniformemente un cerchio alla distanza ½SC (per la Prop. XXXIV). E questa velocità sta alla velocità con cui si potrebbe descrivere un cerchio di raggio SK, cioè la piccola linea Cc sta all’arco Kk (per il Cor. 6 della Prop. IV), in rapporto subduplicato di SK a ½SC, cioè nel rapporto di SK a ½CD. Perciò ½SK × Kk è uguale a ¼CD × Cc, e quindi uguale a ½SY × Dd; cioè l’area KSk è uguale all’area SDd, come sopra. C.V.D.

### Proposizione XXXVI. Problema XXV (i tempi della caduta da un luogo dato)

**[S7.15]** **Determinare i tempi di discesa di un corpo che cade da un luogo dato A.**

**[S7.16]** Sul diametro AS, distanza del corpo dal centro all’inizio, si descriva il semicerchio ADS, e anche il semicerchio OKH, uguale a questo, attorno al centro S. Da un luogo qualsiasi C del corpo si innalzi l’ordinata CD. Si congiunga SD, e si costruisca il settore OSK uguale all’area ASD. È evidente, per la Prop. XXXV, che il corpo, cadendo, descriverà lo spazio AC nello stesso tempo in cui un altro corpo, ruotando uniformemente attorno al centro S, può descrivere l’arco OK. C.V.F.

### Proposizione XXXVII. Problema XXVI (i tempi di un corpo lanciato in alto o in basso)

**[S7.17]** **Definire i tempi di salita o di discesa di un corpo lanciato da un luogo dato verso l’alto o verso il basso.**

**[S7.18]** Il corpo esca dal luogo dato G lungo la linea GS con una velocità qualsiasi. Si prenda GA a ½AS nel rapporto duplicato di questa velocità alla velocità uniforme in un cerchio con cui il corpo potrebbe ruotare attorno al centro S alla distanza data SG. Se quel rapporto è quello del numero due all’unità, il punto A è infinitamente distante; e in tal caso si deve descrivere una parabola con vertice S, asse SC e lato retto qualsiasi. Ciò risulta dalla Prop. XXXIV. Se invece quel rapporto è minore o maggiore di 2 a 1, nel primo caso si deve descrivere sul diametro SA un cerchio, nel secondo un’iperbole rettangola. Ciò risulta dalla Prop. XXXIII. Poi con centro S e raggio uguale alla metà del lato retto si descriva il cerchio HKk, e nel luogo G del corpo che scende o sale e in un altro luogo qualsiasi C si innalzino le perpendicolari GI, CD, che incontrino la sezione conica o il cerchio in I e D. Poi, congiunte SI, SD, si facciano i settori HSK, HSk uguali ai segmenti SEIS, SEDS: per la Prop. XXXV il corpo G descriverà lo spazio GC nello stesso tempo in cui il corpo K può descrivere l’arco Kk. C.V.F.

### Proposizione XXXVIII. Teorema XII (forza proporzionale alla distanza)

**[S7.19]** **Posto che la forza centripeta sia proporzionale all’altezza, ossia alla distanza dei luoghi dal centro, dico che i tempi dei corpi che cadono, le velocità e gli spazi descritti sono proporzionali rispettivamente agli archi, ai seni retti e ai seni versi degli archi.**

**[S7.20]** Il corpo cada da un luogo qualsiasi A lungo la retta AS; con centro delle forze S e raggio AS si descriva il quadrante di cerchio AE, e sia CD il seno retto di un arco qualsiasi AD: il corpo A, nel tempo AD, cadendo descriverà lo spazio AC, e nel luogo C acquisterà la velocità CD.

**[S7.21]** Si dimostra dalla Prop. X nello stesso modo in cui la Prop. XXXII è stata dimostrata dalla Prop. XI.

**[S7.22]** *Cor. 1.* Di qui sono uguali i tempi in cui un corpo, cadendo dal luogo A, giunge al centro S, e un altro corpo, ruotando, descrive l’arco di un quadrante ADE.

**[S7.23]** *Cor. 2.* Di conseguenza sono uguali tutti i tempi in cui i corpi cadono da luoghi qualsiasi fino al centro. Infatti tutti i tempi periodici dei corpi che ruotano sono uguali (per il Cor. 3 della Prop. IV).

### Proposizione XXXIX. Problema XXVII (forza qualsiasi: velocità e tempi per quadrature)

**[S7.24]** **Posta una forza centripeta di qualsiasi genere, e concesse le quadrature delle figure curvilinee, si richiede, per un corpo che sale o scende in linea retta, sia la velocità nei singoli luoghi, sia il tempo in cui il corpo giungerà a un luogo qualsiasi; e viceversa.**

**[S7.25]** Da un luogo qualsiasi A della retta ADEC cada il corpo E, e dal suo luogo E si innalzi sempre la perpendicolare EG, proporzionale alla forza centripeta che in quel luogo tende al centro C; e sia BFG la linea curva che il punto G descrive continuamente. All’inizio stesso del moto EG coincida con la perpendicolare AB: la velocità del corpo in un luogo qualsiasi E sarà come la retta il cui quadrato è uguale all’area curvilinea ABGE. C.V.T.

**[S7.26]** In EG si prenda EM inversamente proporzionale alla retta il cui quadrato è uguale all’area ABGE, e sia VLM la linea curva che il punto M descrive continuamente e di cui è asintoto la retta AB prolungata: il tempo in cui il corpo, cadendo, descrive la linea AE sarà come l’area curvilinea ABTVME. C.V.T.

**[S7.27]** Infatti nella retta AE si prenda una piccolissima linea DE di lunghezza data, e sia DLF la posizione della linea EMG quando il corpo si trovava in D; e se la forza centripeta è tale che la retta il cui quadrato è uguale all’area ABGE sia come la velocità del corpo che scende, l’area stessa sarà in rapporto duplicato della velocità; cioè, se per le velocità in D ed E si scrivono V e V + I, l’area ABFD sarà come VV e l’area ABGE come VV + 2VI + II, e per separazione l’area DFGE come 2VI + II, e perciò DFGE/DE come (2VI + II)/DE; cioè, se si prendono i rapporti primi delle quantità nascenti, la lunghezza DF sarà come la quantità 2VI/DE, e quindi anche come la sua metà, I × V/DE. Ma il tempo in cui il corpo, cadendo, descrive la piccola linea DE è come quella linea direttamente e la velocità V inversamente; e la forza è come l’incremento I della velocità direttamente e il tempo inversamente; e perciò, se si prendono i rapporti primi delle quantità nascenti, come I × V/DE, cioè come la lunghezza DF. Dunque una forza proporzionale a DF o a EG fa sì che il corpo scenda con una velocità che sia come la retta il cui quadrato è uguale all’area ABGE. C.V.D.

**[S7.28]** Inoltre, poiché il tempo in cui si descrive una piccola linea qualsiasi DE di lunghezza data è come la velocità inversamente, e quindi inversamente come la linea retta il cui quadrato è uguale all’area ABFD; e poiché DL, e quindi l’area nascente DLME, è come la stessa linea retta inversamente; il tempo sarà come l’area DLME, e la somma di tutti i tempi come la somma di tutte le aree, cioè (per il corollario del Lemma IV) il tempo totale in cui si descrive la linea AE sarà come l’area totale ATVME. C.V.D.

**[S7.29]** *Cor. 1.* Sia P il luogo da cui un corpo deve cadere affinché, sollecitato da una forza centripeta uniforme nota (quale si suppone comunemente la gravità), acquisti nel luogo D una velocità uguale alla velocità che un altro corpo, cadendo per una forza qualsiasi, ha acquistato nello stesso luogo D; nella perpendicolare DF si prenda DR, che stia a DF come quella forza uniforme sta all’altra forza nel luogo D; si completi il rettangolo PDRQ, e gli si tagli uguale l’area ABFD: A sarà il luogo da cui è caduto l’altro corpo. Infatti, completato il rettangolo DRSE, poiché l’area ABFD sta all’area DFGE come VV sta a 2VI, e quindi come ½V sta a I, cioè come la metà della velocità totale sta all’incremento della velocità del corpo che cade per una forza non uniforme; e similmente l’area PQRD sta all’area DRSE come la metà della velocità totale sta all’incremento della velocità del corpo che cade per la forza uniforme; e poiché quegli incrementi (per l’uguaglianza dei tempi nascenti) sono come le forze che li generano, cioè come le ordinate DF, DR, e quindi come le aree nascenti DFGE, DRSE; per uguaglianza le aree totali ABFD, PQRD staranno fra loro come le metà delle velocità totali, e perciò, essendo uguali le velocità, sono uguali.

**[S7.30]** *Cor. 2.* Di qui, se un corpo qualsiasi è lanciato da un luogo qualsiasi D con una velocità data, verso l’alto o verso il basso, ed è data la legge della forza centripeta, si troverà la sua velocità in un altro luogo qualsiasi e innalzando l’ordinata eg e prendendo quella velocità alla velocità nel luogo D come la retta il cui quadrato è uguale al rettangolo PQRD, aumentato dell’area curvilinea DFge se il luogo e è più basso del luogo D, o diminuito di essa se è più alto, sta alla retta il cui quadrato è uguale al solo rettangolo PQRD.

**[S7.31]** *Cor. 3.* Si conoscerà anche il tempo innalzando l’ordinata em inversamente proporzionale al lato quadrato di PQRD + o − DFge, e prendendo il tempo in cui il corpo ha descritto la linea De al tempo in cui l’altro corpo è caduto da P per una forza uniforme ed è giunto cadendo in D, come l’area curvilinea DLme sta al rettangolo 2PD × DL. Infatti il tempo in cui il corpo che scende per una forza uniforme ha descritto la linea PD sta al tempo in cui lo stesso corpo ha descritto la linea PE in rapporto subduplicato di PD a PE, cioè (mentre la piccola linea DE sta appena nascendo) nel rapporto di PD a PD + ½DE, ossia di 2PD a 2PD + DE; e, per separazione, sta al tempo in cui lo stesso corpo ha descritto la piccola linea DE come 2PD sta a DE, e quindi come il rettangolo 2PD × DL sta all’area DLME; e il tempo in cui l’uno e l’altro corpo hanno descritto la piccola linea DE sta al tempo in cui l’altro corpo, con moto non uniforme, ha descritto la linea De come l’area DLME sta all’area DLme; e, per uguaglianza, il primo tempo sta all’ultimo come il rettangolo 2PD × DL sta all’area DLme.

## Sezione VIII. La determinazione delle orbite in cui ruotano i corpi mossi da forze centripete qualsiasi

### Proposizione XL. Teorema XIII (velocità uguali ad altezze uguali)

**[S8.01]** **Se un corpo, costretto da una forza centripeta qualsiasi, si muove in un modo qualunque, e un altro corpo sale o scende in linea retta, e le loro velocità sono uguali in un caso qualsiasi di altezze uguali, le loro velocità saranno uguali a tutte le altezze uguali.**

**[S8.02]** Un corpo scenda da A per D ed E verso il centro C, e un altro corpo si muova da V sulla linea curva VIKk. Con centro C e distanze qualsiasi si descrivano i cerchi concentrici DI, EK, che incontrino la retta AC in D ed E e la curva VIK in I e K. Si congiunga IC, che incontri KE in N, e su IK si abbassi la perpendicolare NT; la distanza DE, o IN, fra le circonferenze dei cerchi sia piccolissima, e i corpi abbiano in D e in I velocità uguali. Poiché le distanze CD, CI sono uguali, le forze centripete in D e in I saranno uguali. Si rappresentino queste forze con le piccole linee uguali DE, IN; e se una delle due forze, IN, si scompone (per il Cor. 2 delle leggi) in due, NT e IT, la forza NT, agendo lungo la linea NT perpendicolare al percorso ITK del corpo, non muterà affatto la velocità del corpo in quel percorso, ma lo distoglierà soltanto dal percorso rettilineo e lo farà deviare continuamente dalla tangente dell’orbita e procedere sulla via curvilinea ITKk. Nel produrre questo effetto quella forza si consumerà tutta; l’altra forza, IT, agendo lungo il percorso del corpo, lo accelererà tutta, e in un tempo dato piccolissimo genererà un’accelerazione proporzionale a sé stessa. Perciò le accelerazioni dei corpi in D e in I prodotte in tempi uguali (se si prendono i rapporti primi delle linee nascenti DE, IN, IK, IT, NT) sono come le linee DE, IT; in tempi disuguali, invece, come quelle linee e i tempi considerati congiuntamente. Ma i tempi in cui sono descritte DE e IK, per l’uguaglianza delle velocità, sono come le vie descritte DE e IK; e quindi le accelerazioni, nel percorso dei corpi lungo le linee DE e IK, sono come DE e IT, DE e IK considerate congiuntamente, cioè come il quadrato di DE e il rettangolo IT × IK. Ma il rettangolo IT × IK è uguale al quadrato di IN, cioè uguale al quadrato di DE; e perciò le accelerazioni generate nel passaggio dei corpi da D e da I a E e a K sono uguali. Uguali sono dunque le velocità dei corpi in E e in K; e con lo stesso argomento si troveranno sempre uguali alle successive distanze uguali. C.V.D.

**[S8.03]** Ma anche, con lo stesso argomento, corpi ugualmente veloci e ugualmente distanti dal centro saranno ritardati in egual misura nella salita fino a distanze uguali. C.V.D.

**[S8.04]** *Cor. 1.* Di qui, se un corpo oscilla appeso a un filo, o è costretto a muoversi su una linea curva da un ostacolo qualsiasi levigatissimo e perfettamente liscio, e un altro corpo sale o scende in linea retta, e le loro velocità sono uguali a una stessa altezza qualsiasi, le loro velocità saranno uguali a qualsiasi altra altezza uguale. Infatti il filo del corpo appeso, o l’ostacolo di un vaso assolutamente liscio, produce lo stesso effetto della forza trasversale NT. Il corpo non ne è né ritardato né accelerato, ma soltanto costretto ad allontanarsi dal percorso rettilineo.

**[S8.05]** *Cor. 2.* Di qui anche, se la quantità P è la massima distanza dal centro alla quale un corpo, sia oscillando sia ruotando su una traiettoria qualsiasi, possa salire, lanciato verso l’alto da un punto qualsiasi della traiettoria con la velocità che ha in quel punto; e se la quantità A è la distanza del corpo dal centro in un altro punto qualsiasi dell’orbita, e la forza centripeta è sempre come una potenza qualsiasi di A, Aⁿ⁻¹, il cui esponente n − 1 è un numero qualsiasi n diminuito di un’unità; la velocità del corpo a ogni altezza A sarà come √(nPⁿ − nAⁿ), e perciò è data. Infatti la velocità di un corpo che sale e scende in linea retta (per la Prop. XXXIX) è proprio in questo rapporto.

### Proposizione XLI. Problema XXVIII (trovare le traiettorie per quadrature)

**[S8.06]** **Posta una forza centripeta di qualsiasi genere, e concesse le quadrature delle figure curvilinee, si richiedono sia le traiettorie su cui i corpi si muoveranno, sia i tempi dei moti sulle traiettorie trovate.**

**[S8.07]** Tenda una forza qualsiasi al centro C, e si debba trovare la traiettoria VIKk. Sia dato il cerchio VR, descritto con centro C e raggio qualsiasi CV, e con lo stesso centro si descrivano altri cerchi qualsiasi ID, KE, che taglino la traiettoria in I e K e la retta CV in D ed E. Si conducano poi sia la retta CNIX, che tagli i cerchi KE, VR in N e X, sia la retta CKY, che incontri il cerchio VR in Y. Siano poi i punti I e K vicinissimi fra loro, e il corpo proceda da V per I e K fino a k; e sia A il luogo da cui un altro corpo deve cadere per acquistare nel luogo D una velocità uguale alla velocità del primo corpo in I. Restando ferme le cose stabilite nella Prop. XXXIX, la piccola linea IK, descritta in un tempo dato piccolissimo, sarà come la velocità, e quindi come la retta il cui quadrato è uguale all’area ABFD; e il triangolo ICK, proporzionale al tempo, sarà dato; e perciò KN sarà inversamente come l’altezza IC, cioè, se è data una quantità Q e l’altezza IC si chiama A, come Q/A.

**[S8.08]** Chiamiamo Z questa quantità Q/A, e poniamo che la grandezza di Q sia tale che in un caso qualsiasi √ABFD stia a Z come IK sta a KN: in ogni caso √ABFD starà a Z come IK sta a KN, e ABFD a ZZ come IK² sta a KN², e per separazione ABFD − ZZ starà a ZZ come IN² sta a KN²; e quindi √(ABFD − ZZ) starà a Z, ossia a Q/A, come IN sta a KN, e perciò A × KN sarà uguale a Q × IN/√(ABFD − ZZ). Di qui, poiché YX × XC sta ad A × KN come CX² sta ad AA, il rettangolo YX × XC sarà uguale a Q × IN × CX²/(AA√(ABFD − ZZ)).

**[S8.09]** Se dunque nella perpendicolare DF si prendono sempre Db, Dc uguali rispettivamente a Q/(2√(ABFD − ZZ)) e a Q × CX²/(2AA√(ABFD − ZZ)), e si descrivono le linee curve ab, ac, che i punti b, c descrivono continuamente; e dal punto V si innalza sulla linea AC la perpendicolare Va, che taglia le aree curvilinee VDba, VDca, e si innalzano anche le ordinate Ez, Ex: poiché il rettangolo Db × IN, ossia DbzE, è uguale alla metà del rettangolo A × KN, ossia al triangolo ICK, e il rettangolo Dc × IN, ossia DcxE, è uguale alla metà del rettangolo YX × XC, ossia al triangolo XCY; cioè, poiché le particelle nascenti DbzE, ICK delle aree VDba, VIC sono sempre uguali, e le particelle nascenti DcxE, XCY delle aree VDca, VCX sono sempre uguali, l’area generata VDba sarà uguale all’area generata VIC, e quindi proporzionale al tempo, e l’area generata VDca sarà uguale al settore generato VCX. Dato dunque un tempo qualsiasi trascorso da quando il corpo è partito dal luogo V, sarà data l’area VDba proporzionale a esso, e di qui sarà data l’altezza del corpo CD o CI; e l’area VDca, e il settore VCX uguale a essa, insieme con il suo angolo VCI. Dati poi l’angolo VCI e l’altezza CI, è dato il luogo I in cui il corpo si troverà al compiersi di quel tempo. C.V.T.

**[S8.10]** *Cor. 1.* Di qui si possono trovare speditamente le altezze massime e minime dei corpi, cioè gli apsidi delle traiettorie. Gli apsidi sono infatti quei punti in cui la retta IC condotta per il centro cade perpendicolarmente sulla traiettoria VIK: ciò avviene quando le rette IK e NK sono uguali, e quindi quando l’area ABFD è uguale a ZZ.

**[S8.11]** *Cor. 2.* Ma anche l’angolo KIN, sotto il quale la traiettoria taglia in un punto qualsiasi la linea IC, si trova speditamente dall’altezza data IC del corpo: cioè prendendo il suo seno al raggio come KN sta a IK, ossia come Z sta al lato quadrato dell’area ABFD.

**[S8.12]** *Cor. 3.* Se con centro C e vertice principale V si descrive una sezione conica qualsiasi VRS, e da un suo punto qualsiasi R si conduce la tangente RT, che incontri in T l’asse CV prolungato all’infinito; poi, congiunta CR, si conduce la retta CP, uguale all’ascissa CT, che formi un angolo VCP proporzionale al settore VCR; e se verso il centro C tende una forza centripeta inversamente proporzionale al cubo della distanza dei luoghi dal centro, e il corpo esce dal luogo V con la velocità giusta lungo la linea perpendicolare alla retta CV: quel corpo procederà sulla traiettoria che il punto P descrive continuamente; e perciò, se la sezione conica VRS è un’iperbole, esso scenderà al centro; se invece è un’ellisse, salirà continuamente e se ne andrà all’infinito. E viceversa, se il corpo esce dal luogo V con una velocità qualsiasi e, a seconda che abbia cominciato a scendere obliquamente verso il centro o a salire obliquamente da esso, la figura VRS è un’iperbole o un’ellisse, si può trovare la traiettoria aumentando o diminuendo l’angolo VCP in un rapporto dato. E anche, mutata la forza centripeta in centrifuga, il corpo salirà obliquamente sulla traiettoria VPQ, che si trova prendendo l’angolo VCP proporzionale al settore ellittico VRC e la lunghezza CP uguale alla lunghezza CT, come sopra. Tutto ciò segue dalla proposizione precedente, mediante la quadratura di una certa curva, la cui scoperta, poiché è abbastanza facile, tralascio per brevità.

### Proposizione XLII. Problema XXIX (il moto da condizioni iniziali date)

**[S8.13]** **Data la legge della forza centripeta, si richiede il moto di un corpo partito da un luogo dato, con una velocità data, lungo una retta data.**

**[S8.14]** Restando ferme le cose stabilite nelle tre proposizioni precedenti, il corpo esca dal luogo I lungo la piccola linea IK con la velocità che un altro corpo, cadendo dal luogo P per una forza centripeta uniforme, potrebbe acquistare in D; e questa forza uniforme stia alla forza con cui il primo corpo è sollecitato in I come DR sta a DF. Il corpo proceda poi verso k; con centro C e raggio Ck si descriva il cerchio ke, che incontri la retta PD in e, e si innalzino le ordinate eg, ev, ew delle curve BFg, abv, acw. Dal rettangolo dato PDRQ e dalla legge data della forza centripeta da cui è mosso il primo corpo è data la linea curva BFg, per la costruzione del Problema XXVII e del suo Cor. 1. Poi dall’angolo dato CIK è dato il rapporto delle nascenti IK, KN, e di qui, per la costruzione del Problema XXVIII, è data la quantità Q insieme con le linee curve abv, acw: e perciò, compiuto un tempo qualsiasi Dbve, è data sia l’altezza del corpo Ce o Ck, sia l’area Dcwe, e il settore XCy uguale a essa, e l’angolo ICk, e il luogo k in cui il corpo si troverà allora. C.V.T.

**[S8.15]** Supponiamo poi, in queste proposizioni, che la forza centripeta vari, allontanandosi dal centro, secondo una legge qualsiasi che si possa immaginare, ma che a distanze uguali dal centro sia ovunque la stessa. E fin qui abbiamo considerato il moto dei corpi in orbite immobili. Resta da aggiungere poche cose sul loro moto in orbite che ruotano attorno al centro delle forze.

**Fine della Sezione VIII. Nel testo originale segue la Sezione IX, *De motu corporum in orbibus mobilibus, deque motu apsidum*.**

---

## Apparato

### A.0 Estensioni del glossario

I termini seguenti non compaiono nel glossario comune. Ognuno è reso in modo costante in tutto il fascicolo.

| Latino | Italiano | Motivazione |
|---|---|---|
| *recta quæ potest aream ABGE* | «la retta il cui quadrato è uguale all’area ABGE» | *Posse* è il termine euclideo della «potenza» di una retta (il quadrato costruito su di essa). Una resa letterale («la retta che può l’area») sarebbe oscura per uno studente; la perifrasi conserva il significato geometrico senza introdurre la radice. Motte fa la stessa scelta («a right line whose square is equal to»). |
| *latus quadratum* | «lato quadrato» | Il lato del quadrato uguale a un’area data, cioè la radice quadrata. Si conserva il termine storico (S7.31, S8.11); l’equivalenza è nella nota N11. Motte: «square root». |
| *altitudo* | «altezza» | Nelle Sezioni VII–VIII è la distanza dal centro delle forze, non l’altezza sopra un piano (lo dice Newton stesso in S7.19: *altitudini seu distantiæ*). |
| *lineola* | «piccola linea» | Diminutivo tecnico per un segmento nascente (Cc, DE, IK). «Lineetta» suonerebbe tipografico. |
| *quam minimus* | «piccolissimo» | Superlativo assoluto; il valore di limite è dato dal contesto (*rationes primæ*, *ultimæ*). |
| *componendo / composite; dividendo / divisim; ex æquo* | «per composizione; per separazione; per uguaglianza» | Sono le operazioni sulle proporzioni del libro V degli *Elementi*: da A : B = C : D si passa a (A + B) : B = (C + D) : D, a (A − B) : B = (C − D) : D, e, da due proporzioni concatenate, al rapporto fra gli estremi. Motte: «by composition», «by division», «ex æquo». |
| *intervallo X* (nel descrivere un cerchio) | «con raggio X»; per un corpo che ruota: «alla distanza X» | Uso costante del latino geometrico; «intervallo» non è italiano corrente in questo senso. |
| *æquatio* (in astronomia, S6.16) | «equazione» | Termine tecnico dell’astronomia classica: la correzione angolare che, aggiunta al moto medio, dà il moto vero o un moto intermedio. Non va confuso con l’«equazione» algebrica del Lemma XXVIII; la nota N6 lo spiega. |
| *motus medius*; *motus medius æquatus*; *æquatio centri* | «moto medio»; «moto medio equato»; «equazione del centro» | Lessico astronomico storico, conservato. |
| *dimensiones* (di un’equazione); *potestas* (di una curva o di un’equazione); *dignitas* | «dimensioni»; «potenza»; «potenza» | «Equazione di due dimensioni» = di secondo grado; «curva della terza potenza» = curva algebrica di terzo ordine. Si conserva il lessico seicentesco; l’equivalenza moderna è nella nota N2. *Dignitas* (S8.05) è la potenza di una grandezza, Aⁿ⁻¹. |
| *problemata solida, plana* | «problemi solidi, piani» | Classificazione classica (Pappo): piani quelli risolubili con riga e compasso, solidi quelli che richiedono sezioni coniche. |
| *curva geometrice rationalis / irrationalis* | «curva geometricamente razionale / irrazionale» | Definizione di Newton stesso (S6.10); oggi: curve algebriche e trascendenti (nota N2). |
| *trochoides* | «trocoide» | La curva descritta da un punto solidale a una ruota che rotola. In S6.12 il punto A sta dentro la ruota (OA < OG): è una trocoide accorciata, non una cicloide. Motte rende «cycloid» (§ A.17). |
| *spiralis*, *gyrus* | «spirale», «spira» | — |
| *hyperbola rectangula* | «iperbole rettangola» | È l’iperbole con asintoti perpendicolari (oggi «equilatera»). Si conserva l’aggettivo del latino. |
| *latus transversum* | «lato trasverso» | Coerente con *axis transversus* del glossario comune. |
| *latitudo* (di una conica) | «larghezza» | La dimensione trasversale che Newton fa tendere a zero per passare dal moto curvilineo alla caduta rettilinea. |
| *quam punctum G perpetuo tangit* | «che il punto G descrive continuamente» | Letteralmente «che il punto G tocca continuamente», cioè il luogo dei punti G. «Descrive» rende il senso; il verbo latino è annotato qui una volta. |
| *vis uniformis*; *vis inæquabilis*, *motus inæquabilis* | «forza uniforme»; «forza non uniforme», «moto non uniforme» | — |
| *urgere* | «sollecitare» | Come nel Fascicolo 3 per le forze acceleratrici (S7.29, S8.14). |
| *vis transversa* | «forza trasversale» | La componente NT perpendicolare al percorso (S8.04). |
| *cursus*, *via* | «percorso», «via» | — |
| *impedimentum politissimum & perfecte lubricum*; *vas absolute lubricum* | «ostacolo levigatissimo e perfettamente liscio»; «vaso assolutamente liscio» | Il vincolo senza attrito (nota N12). |
| *concipe*, *junge*, *biseca* (imperativi di seconda persona) | «immagina»; altrove impersonale («si congiunga», «si divida a metà») | Come nel Fascicolo 3 (*concipe* → «immagina»). Gli imperativi di costruzione sono resi con il congiuntivo esortativo impersonale, uso normale della geometria italiana. |
| *Q.E.I.*, *Q.E.F.* | «C.V.T.», «C.V.F.» | Glossario comune. |

### A.1 Proposizione XXX

**Latino:** *Corporis in data trajectoria parabolica moti invenire locum ad tempus assignatum.*

**Inglese:** “To find at any assigned time the place of a body moving in a given parabolic trajectory.”

**Scelte e letture.**

- **Formule appiattite.** La trascrizione dà la catena di uguaglianze di S6.03 senza frazioni né parentesi. La lettura adottata, confermata dalle formule SVG 113–121 di Motte e dal calcolo (nota N1), è: «AO−AG¯: quad.» = (AO − AG)²; «2GAO» = 2GA × AO (rettangolo GAO, lasciato nella forma di Newton); «34POq» = ¾PO²; «AO×POq4AS» = AO × PO²/4AS; «43GH×AS» = (4/3)GH × AS; «16AO×PO» = ⅙AO × PO; «12AS×PO» = ½AS × PO; «AO+3AS6×PO» = (AO + 3AS)/6 × PO; «4AO−3SO6×PO» = (4AO − 3SO)/6 × PO; «areæ APO−SPO¯» = area APO − SPO.
- *applicatis terminis omnibus ad 3PO*: «applicare» un’area a una linea è dividerla per quella linea; reso «divisi tutti i termini per 3PO», come Motte («dividing»).
- *abscindenæ* è un **refuso probabile della trascrizione** per *abscindendæ* («da tagliare»), da verificare sulla stampa.
- *circulo ASP per corpus motum perpetuo transeunte* (Cor. 2) è reso «se un cerchio ASP passa sempre per il corpo in moto»: è il cerchio di centro H che passa per A, S e P, perché HA = HS per costruzione (H sta sulla perpendicolare a metà di AS).

### A.2 Lemma XXVIII e Corollario

**Latino:** *Nulla extat figura ovalis cujus area, rectis pro lubitu abscissa, possit per æquationes numero terminorum ac dimensionum finitas generaliter inveniri.*

**Inglese:** “There is no oval figure whose area, cut off by right lines at pleasure, can be universally found by means of equations of any number of finite terms and dimensions.”

**Scelte e letture.**

- *finitas* concorda con *æquationes* ed è limitato da *numero terminorum ac dimensionum*: «equazioni finite quanto al numero dei termini e delle dimensioni». Motte, con «of any number of finite terms», sposta l’aggettivo sui termini; il senso non cambia.
- *ceu polum* è reso «come attorno a un polo».
- **Lacuna probabile.** La trascrizione ha: *intersectiones binæ rectarum & sectionum conicarum prodeunt semper per æquationes duarum dimensionum, ternæ rectarum & curvarum irreducibilium quartæ potestatis per æquationes dimensionum quatuor*. Così com’è, la frase attribuisce «tre» intersezioni a curve della quarta potenza e le fa trovare con equazioni di quattro dimensioni: è incoerente. Motte ha la serie completa («the three intersections … of the third order by equations of three dimensions; the four intersections … of the fourth order, by equations of four dimensions»). È verosimile un salto dallo stesso allo stesso (da *curvarum irreducibilium* a *curvarum irreducibilium*) nella trascrizione o nella stampa. La traduzione integra tra parentesi quadre la parte mancante secondo il senso e secondo Motte. **Da verificare sulla stampa del 1726.**
- *in infinium* è un **refuso probabile della trascrizione** per *in infinitum*.
- *rectis imperatis* è reso «rette prescritte»; Motte «right lines at pleasure» ripete la formula dell’enunciato.
- **Corollario.** *per longitudinum rationes complicatas* è reso «per mezzo di rapporti composti di lunghezze»; Motte «complicated ratios». *quemadmodum in decimo elementorum* rimanda al libro X degli *Elementi* di Euclide, sugli incommensurabili.
- *igtur* è un **refuso probabile della trascrizione** per *igitur*.
- *trochoides* è reso «trocoidi»; Motte «cycloids» (vedi § A.0).

### A.3 Proposizione XXXI

**Latino:** *Corporis in data trajectoria elliptica moti invenire locum ad tempus assignatum.*

**Inglese:** “To find the place of a body moving in a given elliptic trajectory at any assigned time.”

**Scelte e letture.**

- *OGad OA*: spazio mancante nella trascrizione (*OG ad OA*).
- *super regula GH, ceu fundo* è reso «sulla riga GH, come su una base»; Motte «on the ruler GH, as a base».
- **La trocoide.** Il punto A della ruota GEF dista dal centro O di OA, minore del raggio OG della ruota (perché OG : OA = OA : OS e OS < OA). La curva ALI è quindi una trocoide accorciata. Motte scrive «cycloid»: imprecisione terminologica (§ A.17).
- **Formule.** «12OQ×AQ», «12OQ×SR», «12OQ» = ½OQ × AQ, ½OQ × SR, ½OQ (Motte SVG 122–124).
- *divisim AQ−SR ad GF− sinu arcus AQ*: «per separazione, di AQ − SR a GF − seno dell’arco AQ». Il controllo numerico della costruzione (GK = GF − seno di AQ, nella scala del cerchio di raggio OA) è nella nota N3.

### A.4 Scolio della Proposizione XXXI

- **Primo metodo (S6.14).** *tum … tum etiam* è reso «sia … sia». Motte trasforma in elenco («First … Secondly»).
- *57.29578*: valore dell’angolo sotteso da un arco uguale al raggio, cioè 180/π = 57,2957795…; il numero di Newton è arrotondato correttamente alla quinta decimale. Motte stampa «57,29578».
- *porportionalis*, *augulus* sono **refusi probabili della trascrizione** per *proportionalis*, *angulus*.
- **Lettere.** Il latino ha *tempus, quo corpus descripsit arcum AP*; Motte «the arc Ap», con la p minuscola del luogo vero. Il tempo dato è quello del luogo vero; ma il latino ha AP, e la traduzione lo conserva.
- **«AOq».** In *capiatur angulus AOq* la q minuscola è il punto q (luogo corretto sul cerchio), non l’abbreviazione di *quadratum*. La traduzione scrive «l’angolo AOq»; Motte idem.
- *cosinu* è la forma di Newton per «coseno»; *ex cosinu ejus Or* è reso «dal suo coseno Or».
- **Iperbole (S6.15).** *applicando … ad lineam SN* = dividendo per SN. *per tabulam logarithmorum* rimanda al fatto che l’area iperbolica fra asintoto e curva è logaritmica (nota N5).
- **Calcolo particolare (S6.16).**
  - «lateris recti semissem 12» = ½L (Motte SVG 127).
  - **Lacuna della trascrizione:** *semisumma axium AO+ ad quadratum axis majoris AB* manca del secondo addendo. Motte ha «AO + OD the half sum of the axes». La semisomma degli assi AB e 2OD è appunto AO + OD: la traduzione integra «[OD]». Il calcolo della nota N6 conferma che con AO + OD l’angolo Y coincide con il valore ottimo.
  - La lettera D indica qui sia il vertice del semiasse minore (OD) sia la differenza OD − ½L: è un’ambiguità dell’originale, conservata.
  - *æquationem maximam primam / secundam* è reso «prima equazione massima», «seconda equazione massima». Motte ha «the greatest first equation» per Y, ma «the second greatest equation» per Z, che significa un’altra cosa («la seconda per grandezza»).
  - **Errore di Motte:** *ad triplum quadratum semiaxis majoris AO* diventa «to triple the square of **half** the greater semi-axis AO». Con «half» l’angolo Z risulterebbe quadruplo e la correzione darebbe errori di circa 84″ invece di circa 3″ (nota N6).
  - *quamproxime* è reso «con ottima approssimazione», come *quam proxime* nel Fascicolo 3.
  - *error vix superabit minutum unum secundum*: «l’errore supererà a stento un secondo». Il controllo numerico (nota N6) dà circa 2″ per un’orbita la cui equazione del centro massima è di dieci gradi.
  - *per Wardi methodum notissimam*: il metodo di Seth Ward (1617–1689), astronomo di Oxford. Motte omette il nome: «by the known methods».
- **Chiusura (S6.17).** *recta descendat vel recta ascendat* è reso «scenda o salga in linea retta».

### A.5 Proposizione XXXII

**Latino:** *Posito quod vis centripeta sit reciproce proportionalis quadrato distantiæ locorum a centro, spatia definire quæ corpus recta cadendo datis temporibus describit.*

**Inglese:** “Supposing that the centripetal force is reciprocally proportional to the square of the distance of the places from the centre; it is required to define the spaces which a body, falling directly, describes in given times.”

**Scelte e letture.**

- *recta cadendo* è reso «cadendo in linea retta»; Motte «falling directly».
- *um <113> bilicus*: la parola è spezzata dal cambio di pagina della trascrizione.
- *capatur* è un **refuso probabile della trascrizione** per *capiatur*.
- *orbe APB jam coincidente*: ablativo assoluto reso con una temporale («quando l’orbita APB coincide ormai…»).
- Le figure dei tre casi (FIG 80–82) non sono disponibili. Dalle lettere: nel Caso 1 B è l’estremo dell’asse verso cui degenera il fuoco S, A l’altro estremo, D il punto del semicerchio sopra C; nei Casi 2 e 3 B è il vertice e f un punto dell’arco PB.

### A.6 Proposizione XXXIII

**Latino:** *Positis jam inventis, dico quod corporis cadentis velocitas in loco quovis C est ad velocitatem corporis centro B intervallo BC circulum describentis, in subduplicata ratione quam AC, distantia corporis a circuli vel hyperbolæ rectangulæ vertice ulteriore A, habet ad figuræ semidiametrum principalem 12AB.*

**Inglese:** “The things above found being supposed, I say, that the velocity of a falling body in any place C is to the velocity of a body, describing a circle about the centre B at the distance BC, in the subduplicate ratio of AC, the distance of the body from the remoter vertex A of the circle or rectangular hyperbola, to [SVG 128], the principal semi-diameter of the figure.”

**Scelte e letture.**

- «12AB» = ½AB (SVG 128).
- «ACB» è il rettangolo AC × CB; la notazione di Newton è conservata nel testo.
- Le frazioni appiattite sono lette così (SVG 129–133 di Motte): «12L×SP» = ½L × SP; «2CPq×AOACB» = 2CP² × AO/ACB; «CPq×AO×SPACB» = CP² × AO × SP/ACB; «BQq×AC×SPAO×BC» = BQ² × AC × SP/(AO × BC).
- *BO− vel +CO*: «BO − o + CO», cioè BO − CO nell’ellisse, BO + CO nell’iperbole, secondo che si sia operato per separazione o per composizione.
- *neglectis æqualitatis rationibus*: «trascurati i rapporti di uguaglianza», cioè i rapporti che al limite valgono 1.
- **Cor. 2.** *motu suo sursum verso* è reso «se il suo moto è volto verso l’alto»; Motte «by its motion converted upwards».

### A.7 Proposizione XXXIV

**Latino:** *Si figura BED parabola est, dico quod corporis cadentis velocitas in loco quovis C æqualis est velocitati qua corpus centro B dimidio intervalli sui BC circulum uniformiter describere potest.*

**Inglese:** “If the figure BED is a parabola, I say, that the velocity of a falling body in any place C is equal to the velocity by which a body may uniformly describe a circle about the centre B at half the interval BC.”

**Scelte e letture.**

- *dimidio intervalli sui BC*: «alla metà della sua distanza BC».
- Nella Parte B la prima frase latina è ricomposta: la segmentazione automatica la spezzava dopo *per corol.*

### A.8 Proposizione XXXV

**Latino:** *Iisdem positis, dico quod area figuræ DES, radio indefinito SD descripta, æqualis sit areæ quam corpus, radio dimidium lateris recti figuræ DES æquante, circa centrum S uniformiter gyrando, eodem tempore describere potest.*

**Inglese:** “The same things supposed, I say, that the area of the figure DES, described by the indefinite radius SD, is equal to the area which a body with a radius equal to half the latus rectum of the figure DES, by uniformly revolving about the centre S, may describe in the same time.”

**Scelte e letture.**

- *radio indefinito SD*: «raggio indefinito», cioè di lunghezza variabile.
- *puta si in coitu punctorum D, d*: «s’intende se, nel congiungersi dei punti D, d».
- **Caso 1.** Il latino dice *si figura DES circulus est vel hyperbola*; Motte aggiunge «rectangular». L’aggiunta è coerente con la Prop. XXXII, Caso 2 (iperbole rettangola), ma non è nel testo di questo passo.
- Le frazioni: «12SK×Kk» = ½SK × Kk; «12SY×Dd» = ½SY × Dd; «14CD×Cc» = ¼CD × Cc; «12SC» = ½SC; «12CD» = ½CD.
- **Errore di Motte (Caso 1):** la formula SVG 134 dice «½SY × Kk» uguale a «½SY × Dd». Deve essere ½**SK** × Kk, come nel latino e come richiede l’argomento (l’area KSk del settore circolare).
- **Caso 2:** la trascrizione ha *in subduplicata ratione SK ad 12Sc*: la c minuscola è un **refuso probabile della trascrizione** per ½SC (Motte SVG 137: ½SC), da verificare sulla stampa. La c minuscola indicherebbe il punto c, estremo della piccola linea Cc, e al limite non cambierebbe il risultato; ma tutto il resto del passo usa SC.

### A.9 Proposizione XXXVI

**Latino:** *Corporis de loco dato A cadentis determinare tempora descensus.*

**Inglese:** “To determine the times of the descent of a body falling from a given place A.”

- *sub initio*: «all’inizio». *constitue sectorem*: «si costruisca il settore».
- Il semicerchio OKH ha raggio uguale alla metà di AS, cioè alla metà del lato retto del cerchio ADS (Prop. XXXV, Caso 1: SO è la metà del lato retto).

### A.10 Proposizione XXXVII

**Latino:** *Corporis de loco dato sursum vel deorsum projecti definire tempora ascensus vel descensus.*

**Inglese:** “To define the times of the ascent or descent of a body projected upwards or downwards from a given place.”

**Scelte e letture.**

- «12AS» = ½AS (SVG 140).
- *numeri binarii ad unitatem*: «del numero due all’unità».
- **Lettere.** Il latino ha *parabola vertice S, axe SC*; Motte «axis SG». Le due lettere stanno sulla stessa retta GS, quindi indicano lo stesso asse; il latino è conservato. Il latino ha *circulus HKk*, Motte «HkK»: è lo stesso cerchio, con le lettere in ordine diverso.
- *segmentis SEIS, SEDS*: i segmenti della conica compresi fra l’arco e le corde SI, SD; E è un punto dell’arco (figura FIG 89 non disponibile).

### A.11 Proposizione XXXVIII

**Latino:** *Posito quod vis centripeta proportionalis sit altitudini seu distantiæ locorum a centro, dico quod cadentium tempora, velocitates & spatia descripta sunt arcubus, arcuumque sinibus rectis & sinibus versis respective proportionalia.*

**Inglese:** “Supposing that the centripetal force is proportional to the altitude or distance of places from the centre, I say, that the times and velocities of falling bodies, and the spaces which they describe, are respectively proportional to the arcs, and the right and versed sines of the arcs.”

- *sinus rectus*: «seno retto», cioè il seno ordinario, contrapposto al seno verso.
- *tempore AD*: «nel tempo AD», cioè in un tempo rappresentato dall’arco AD.

### A.12 Proposizione XXXIX e corollari

**Latino:** *Posita cujuscunque generis vi centripeta, & concessis figurarum curvilinearum quadraturis, requiritur corporis recta ascendentis vel descendentis tum velocitas in locis singulis, tum tempus quo corpus ad locum quemvis perveniet: Et contra.*

**Inglese:** “Supposing a centripetal force of any kind, and granting the quadratures of curvilinear figures; it is required to find the velocity of a body, ascending or descending in a right line, in the several places through which it passes; as also the time in which it will arrive at any place; and vice versa.”

**Scelte e letture.**

- *concessis figurarum curvilinearum quadraturis*: «concesse le quadrature delle figure curvilinee», cioè supposto di saper calcolare le aree sotto le curve (oggi: gli integrali).
- *SitqueBFG*: spazio mancante nella trascrizione. *curvilineæm*: **refuso probabile della trascrizione** per *curvilineam*.
- **Frazioni** (SVG 141–146): «DFGEDE» = DFGE/DE; «2VI+IIDE» = (2VI + II)/DE; «2VIDE» = 2VI/DE; «I×VDE» = I × V/DE; «12V» = ½V; «12DE» = ½DE.
- **Lettere delle aree.** Il latino ha prima *area curvilinea ABTVME* (S7.26), poi *area tota ATVME* (S7.28); Motte conserva entrambe le forme. Probabilmente indicano la stessa regione (B sta sulla retta AB, che è l’asintoto della curva VLM); la traduzione conserva le due sigle.
- *si ea sit vis centripeta, ut recta, quæ potest aream ABGE, sit ut descendentis velocitas*: la seconda *ut* è consecutiva («tale che»).
- **Cor. 1.** *urgente aliqua uniformi vi centripeta nota (qualis vulgo supponitur gravitas)*: «sollecitato da una forza centripeta uniforme nota (quale si suppone comunemente la gravità)». *eique æqualis abscindatur area ABFD*: «e gli si tagli uguale l’area ABFD». Nella trascrizione la parentesi *(ob æqualitatem velocitatum,* non si chiude e *erunt ex æquo)* ha una parentesi chiusa senza apertura: è verosimile che nella stampa si leggano *(ob æqualitatem temporum nascentium)* … *erunt (ex æquo)* … *(ob æqualitatem velocitatum)*; la punteggiatura è da verificare, il senso non cambia.
- **Cor. 3.** *lateri quadrato ex PQRD+ vel −DFge*: «al lato quadrato di PQRD + o − DFge». Motte: «square root». *lineola DE jamjam nascente*: «mentre la piccola linea DE sta appena nascendo».

### A.13 Proposizione XL e corollari

**Latino:** *Si corpus, cogente vi quacunque centripeta, moveatur utcunque, & corpus aliud recta ascendat vel descendat, sintque eorum velocitates in aliquo æqualium altitudinum casu æquales, velocitates eorum in omnibus æqualibus altitudinibus erunt æquales.*

**Inglese:** “If a body, acted upon by any centripetal force, is any how moved, and another body ascends or descends in a right line, and their velocities be equal in any one case of equal altitudes, their velocities will be also equal at all equal altitudes.”

**Scelte e letture.**

- *cogente vi*: «costretto da una forza»; Motte «acted upon».
- *occurentes*: **refuso probabile della trascrizione** per *occurrentes*.
- *per legum corol. 2.*: «per il Cor. 2 delle leggi», cioè il Corollario II degli Assiomi (Fascicolo 3, L10).
- *DE quad. & IT×IK rectangulum*: «il quadrato di DE e il rettangolo IT × IK».
- **Cor. 2, formula della velocità.** La trascrizione ha *velocitas corporis in omni altitudine A erit ut nPn−nAn*. Motte stampa √(Pⁿ − Aⁿ) (SVG 148). La trascrizione ha perso i segni di radice anche nella Prop. XLI (dove Motte ha √ABFD); la lettura adottata è quindi **√(nPⁿ − nAⁿ)**, con il fattore n che la trascrizione conserva due volte e Motte non ha. Il fattore conta: per n negativo (per esempio n = −1, forza inversa del quadrato) Pⁿ − Aⁿ è negativo, mentre nPⁿ − nAⁿ resta positivo (nota N12). La lezione di Motte vale quindi solo per n > 0. **Da verificare sulla stampa del 1726.**

### A.14 Proposizione XLI e corollari

**Latino:** *Posita cujuscunque generis vi centripeta & concessis figurarum curvilinearum quadraturis, requiruntur tum trajectoriæ in quibus corpora movebuntur, tum tempora motuum in trajectoriis inventis.*

**Inglese:** “Supposing a centripetal force of any kind, and granting the quadratures of curvilinear figures, it is required to find as well the trajectories in which bodies will move, as the times of their motions in the trajectories found.”

**Scelte e letture.**

- **Formule e radici perdute.** La trascrizione dà «ut QA» per Q/A; «sit in aliquo casu ABFD ad Z» dove Motte ha √ABFD (SVG 151); «ABFD−ZZ ad Z» per √(ABFD − ZZ) a Z (SVG 152); «Q×INABFD−ZZ» per Q × IN/√(ABFD − ZZ) (SVG 153); «Q×IN×CX quad.AAABFD−ZZ» per Q × IN × CX²/(AA√(ABFD − ZZ)) (SVG 154); «Q2ABFD−ZZ» e «Q×CX quad.2AAABFD−ZZ» per Q/(2√(ABFD − ZZ)) e Q × CX²/(2AA√(ABFD − ZZ)) (SVG 155–156). La proporzione «ABFD a ZZ come IK² a KN²», senza radice, è coerente con √ABFD a Z come IK a KN: la lettura con la radice è quindi necessaria, non solo suggerita da Motte.
- *Sint autem puncta I & K sibi invicem vicinissima*: «siano poi i punti I e K vicinissimi fra loro».
- *quas puncta, b, c perpetuo tangunt*: la virgola dopo *puncta* è un probabile artefatto della trascrizione.
- **Cor. 3.** *axi infinitæ producto*: forma anomala; il senso è *in infinitum producto*, «prolungato all’infinito» (Motte «indefinitely produced»). **Refuso probabile della trascrizione o della stampa**, da verificare. *justa cum velocitate*: «con la velocità giusta», cioè quella richiesta dalla costruzione.
- **Cor. 3, aggiunta di Motte:** «that body will proceed in a trajectory **VPQ**, which the point P will always touch». Il latino dice soltanto *in trajectoria quam punctum P perpetuo tangit*; la sigla VPQ compare nel latino solo più avanti, per il caso della forza centrifuga.
- *cujus inventionem, ut satis facilem, brevitatis gratia missam facio*: «la cui scoperta, poiché è abbastanza facile, tralascio per brevità».

### A.15 Proposizione XLII e avvertenza finale

**Latino:** *Data lege vis centripetæ, requiritur motus corporis de loco dato, data cum velocitate, secundum datam rectam egressi.*

**Inglese:** “The law of centripetal force being given, it is required to find the motion of a body setting out from a given place, with a given velocity, in the direction of a given right line.”

**Scelte e letture.**

- *per constructionem problematis xxvii*: il Problema XXVII è la **Prop. XXXIX** (S7.24–S7.31); *prob. xxviii* è la **Prop. XLI**. La traduzione conserva la numerazione dei problemi, come il latino. **Errore di Motte:** «by the construction of **Prop.** XXVII», che rimanda a un’altra proposizione; poco dopo Motte scrive correttamente «Prob. XXVIII».
- *completo tempore quovis Dbve*: il tempo è rappresentato dall’area Dbve.
- **Avvertenza finale (S8.15).** *in recessu quidem a centro*: «allontanandosi dal centro». Motte divide in due capoversi l’ultima parte («I have hitherto considered…»): scelta tipografica.

### A.16 Refusi e anomalie della trascrizione

| Luogo | Trascrizione | Lettura adottata | Natura |
|---|---|---|---|
| S6.03 | *abscindenæ* | *abscindendæ* | refuso probabile |
| S6.03 e passim | *34POq*, *43GH*, *16AO*, *12AS* … | ¾PO², (4/3)GH, ⅙AO, ½AS | frazioni appiattite |
| S6.08 | *ternæ rectarum & curvarum irreducibilium quartæ potestatis* | integrazione tra parentesi quadre | lacuna probabile (salto dallo stesso allo stesso) |
| S6.08 | *in infinium* | *in infinitum* | refuso probabile |
| S6.10 | *igtur* | *igitur* | refuso probabile |
| S6.12 | *OGad OA* | *OG ad OA* | spazio mancante |
| S6.14 | *porportionalis*, *augulus* | *proportionalis*, *angulus* | refusi probabili |
| S6.16 | *semisumma axium AO+* | AO + [OD] | addendo perduto |
| S6.16 | *lateris recti semissem 12* | ½L | lettera perduta |
| S7.02 | *capatur* | *capiatur* | refuso probabile |
| S7.14 | *12Sc* | ½SC | refuso probabile |
| S7.25 | *SitqueBFG*; *curvilineæm* | *Sitque BFG*; *curvilineam* | spazio; refuso probabile |
| S7.29 | *(ob æqualitatem velocitatum,*; *ex æquo)* | parentesi da sistemare | punteggiatura |
| S8.02 | *occurentes* | *occurrentes* | refuso probabile |
| S8.05 | *nPn−nAn* | √(nPⁿ − nAⁿ) | radice perduta; fattore n da verificare |
| S8.07–S8.09 | *ABFD ad Z*, *ABFD−ZZ ad Z* … | √ABFD, √(ABFD − ZZ) … | radici perdute |
| S8.12 | *axi infinitæ producto* | *in infinitum producto* | forma anomala |

Nessuno di questi punti è stato verificato sulla stampa del 1726.

### A.17 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| S6.03 | *−2GH×PO* | SVG 115: «− 2GH + PO» | errore di formula (+ per ×) |
| S6.08 | lacuna della trascrizione | serie completa (terza e quarta potenza) | Motte integra ciò che la trascrizione perde |
| S6.10, S6.12 | *trochoides*, *trochoidem* | «cycloids», «cycloid» | termine impreciso |
| S6.14 | *tum … tum etiam* | «First … Secondly» | ristrutturazione |
| S6.14 | *arcum AP* | «the arc Ap» | lettera diversa |
| S6.16 | *semisumma axium AO+* | «AO + OD the half sum» | Motte integra |
| S6.16 | *æquationem maximam secundam* | «the second greatest equation» | senso cambiato |
| S6.16 | *triplum quadratum semiaxis majoris AO* | «triple the square of **half** the greater semi-axis AO» | errore (Z quadruplicato) |
| S6.16 | *per Wardi methodum notissimam* | «by the known methods» | omissione del nome |
| S7.06 | *Est autem* | «For» | connettivo cambiato |
| S7.13 | *hyperbola* | «rectangular hyperbola» | aggiunta |
| S7.13 | ½SK × Kk | SVG 134: «½SY × Kk» | errore di formula |
| S7.18 | *axe SC*; *HKk* | «axis SG»; «HkK» | lettere diverse, stesso oggetto |
| S7.25 | *erigatur* | «imagine a perpendicular» | aggiunta |
| S8.02 | *ob æqualitatem velocitatum* | «… (in D and I)» | aggiunta |
| S8.05 | √(nPⁿ − nAⁿ) (lettura) | √(Pⁿ − Aⁿ) | fattore n assente (vedi § A.13) |
| S8.07 | *vicinissima* | «Let the points I and K **he** indefinitely near» | refuso dell’edizione 1846 |
| S8.09 | *quas puncta b, c perpetuo tangunt* | «the **foci** of the points b and c» | refuso per «loci» |
| S8.08 | *YX×XC* | «XY × XC» (una volta) | stesso rettangolo |
| S8.12 | *in trajectoria quam punctum P perpetuo tangit* | «a trajectory **VPQ**, which…» | aggiunta |
| S8.14 | *per constructionem problematis xxvii* | «by the construction of **Prop.** XXVII» | rimando errato |
| S8.15 | un capoverso | due capoversi | tipografia |

Per il resto Motte segue il latino da vicino; le sue formule SVG, salvo i casi segnalati, coincidono con le letture ricostruite qui.

---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. I controlli numerici sono stati eseguiti con script Python scritti per questo fascicolo (unità con μ = 1, cioè forza = μ/r² per la forza inversa del quadrato).

### N1. Prop. XXX: il «problema di Keplero» nella parabola

In termini moderni l’area APS, proporzionale al tempo, si esprime con l’anomalia vera ν: posto *D* = tan(ν/2), il tempo dal vertice è proporzionale a *D* + *D*³/3. Newton evita l’equazione cubica con una costruzione con riga e compasso: il cerchio di centro H, con GH = 3M, passa per A e per S e taglia la parabola nel punto cercato.

**Verifica numerica** (parabola *y*² = 4*x*, AS = 1). Per quattro posizioni di prova di P (ascissa AO = 0,3; 1; 2,5; 7) ho calcolato l’area APS = ⅔AO × PO − ½SO × PO, ho posto M = APS/4AS e GH = 3M, e ho intersecato il cerchio di centro H e raggio HS con la parabola. In tutti i casi l’intersezione coincide con P entro 10⁻¹⁰, e HA = HS.

- **Cor. 1.** Il rapporto GH : AS coincide con il rapporto fra l’area APS e l’area fino all’estremo del lato retto (per AO = 2,5: 2,17406589 in entrambi i casi).
- **Cor. 2.** Poiché l’area cresce con velocità costante h/2 (h = momento angolare per unità di massa), GH = 3APS/4AS cresce con velocità 3h/8AS; con velocità al vertice √(2μ/AS) si ottiene esattamente 3/8 = 0,375.
- **Cor. 3.** Nel caso AO = 2,5: HA = HP = 2,230821. H sta dunque sulla perpendicolare nel punto medio di AP, come dice il testo.

### N2. Lemma XXVIII: aree non algebriche

Il lemma afferma, in linguaggio moderno, che l’area di un ovale tagliata da una retta variabile non è funzione algebrica dei parametri della retta. L’argomento della spirale è ingegnoso: un’equazione algebrica ha un numero finito di radici, mentre la retta taglia la spirale in infiniti punti. Il Corollario ne trae che l’equazione di Keplero (nota N3) non si può risolvere con curve algebriche («geometricamente razionali»): servono curve trascendenti («geometricamente irrazionali»), come la trocoide della Prop. XXXI. La clausola finale esclude gli ovali che fanno parte di curve con rami all’infinito («figure coniugate»). Il rigore generale dell’argomento di Newton è stato discusso dai matematici successivi; qui non si entra nel merito.

Equivalenze di lessico: «equazione di *k* dimensioni» = equazione di grado *k*; «curva della terza potenza» = curva algebrica di terzo ordine; due curve di ordini *m* e *n* hanno al più *mn* intersezioni (2 × 2 = 4, 2 × 3 = 6, 3 × 3 = 9), come nel testo.

### N3. Prop. XXXI: equazione di Keplero e trocoide

Con OA = *a* (semiasse maggiore), OS = *ae* (*e* eccentricità) e l’angolo AOQ = *E* (oggi «anomalia eccentrica»), l’arco AQ vale *aE* e SR = OS sin *E* = *ae* sin *E*. La proporzionalità dell’area al tempo dà quindi l’**equazione di Keplero**:

*M* = *E* − *e* sin *E*,

dove *M* = 2π *t*/*T* è l’«anomalia media», l’angolo N dello Scolio. La ruota di raggio OG = *a*/*e* che rotola sulla riga GH porta con sé il punto A, a distanza *a* dal centro: dopo una rotazione *E*, l’avanzamento è GF = (*a*/*e*)*E* e lo scarto orizzontale del punto della trocoide è GK = (*a*/*e*)*E* − *a* sin *E* = (*a*/*e*)·*M*. GK sta al perimetro 2π*a*/*e* come *M* sta a 2π: è esattamente la costruzione del testo.

**Verifica numerica** (*e* = 0,6). Per *E* = 20°, 75°, 140° l’area APS calcolata direttamente, la quantità (*b*/2)(AQ − SR) e il rapporto GK/(perimetro della ruota) danno le stesse frazioni del periodo: 0,02289504; 0,11609421; 0,32750719.

### N4. Scolio, primo metodo: è il metodo di Newton-Raphson

Con raggio 1, l’angolo B vale *e* radianti espressi in gradi (*e* × 57,29578°) e la lunghezza L vale 1/*e*. Allora D = B sin AOQ, ed E = (N − AOQ + D) · L/(L − cos AOQ) si riscrive

*E*₁ = *E*₀ + (*M* − *E*₀ + *e* sin *E*₀)/(1 − *e* cos *E*₀),

che è un passo del metodo di Newton per l’equazione di Keplero. La regola dei segni del testo (+ e − scambiati se l’angolo è negativo; «diminuita» o «aumentata» secondo che l’angolo sia minore o maggiore di un retto) equivale a usare seno e coseno con il loro segno.

**Verifica numerica**: errore su *E*, in secondi d’arco, partendo dalla congettura rozza *E*₀ = N:

| *e* | N | dopo E | dopo G | dopo I |
|---|---|---|---|---|
| 0,0167 | 100° | 0,45″ | < 10⁻⁸″ | — |
| 0,0934 | 30° | 13,9″ | 2,6 × 10⁻⁵″ | — |
| 0,0934 | 100° | 75″ | 0,001″ | — |
| 0,2056 | 100° | 732″ | 0,23″ | 2 × 10⁻⁸″ |
| 0,5 | 30° | 8770″ | 106″ | 0,016″ |
| 0,9 | 30° | 237 000″ | 55 400″ | 6080″ |

Con una congettura migliore, *E*₀ = N + *e* sin N, l’errore massimo dopo il solo termine E è 0,16″ per *e* = 0,0934 e 9,7″ per *e* = 0,2056. L’affermazione di Newton («quasi mai sarà necessario procedere oltre il secondo termine E») è dunque corretta per le eccentricità planetarie, purché la congettura iniziale sia ragionevole. Per eccentricità grandi (*e* = 0,9) la convergenza dal punto di partenza N è lenta e il primo passo peggiora l’errore.

### N5. Scolio, iperbole

Per l’iperbole di semiassi *a*, *b*, in coordinate *x* = *a* cosh *u*, *y* = *b* sinh *u*, l’area OPA vale (*ab*/2)*u* = (*ab*/2) ln(*x*/*a* + *y*/*b*): per questo serve la «tavola dei logaritmi». La correzione PQ = 2(A − APS)/SN viene dal fatto che il triangolo SPQ ha area ½ SN × PQ: è ancora un passo del metodo di Newton.

**Verifica numerica** (*a* = 1, *b* = 0,8; valore vero *u* = 1,3; congettura *u* = 1,1): l’errore sull’area dopo tre passi vale 5,4 × 10⁻³, 9,4 × 10⁻⁶, 2,9 × 10⁻¹¹. La convergenza è quadratica, come nell’ellisse.

### N6. Scolio, «calcolo particolare»: equante e correzioni

Il metodo astronomico usa il **fuoco vuoto** H: l’angolo BHP, visto dal fuoco in cui non sta il Sole, cresce quasi uniformemente (è l’antica idea dell’equante). Newton corregge l’equante con due termini: BHP = T + V + X, con V = Y sin 2T e X = Z sin³T (in valore con segno; la regola «T + X + V» e «T + X − V» del testo dà proprio questo per T minore o maggiore di un retto).

- **Il vertice B è l’afelio.** Il controllo numerico mostra che il metodo funziona con T contato dall’afelio (vertice lontano da S); contato dal perielio l’errore sale a circa 3,7′. Nella figura (FIG 78–79, non disponibile) B è quindi il vertice dalla parte del fuoco H.
- **I valori di Y e Z.** Con *a* = AO, *b* = OD, D = *b* − *b*²/*a*: per *e* = 0,0934 Newton dà Y = 447,9″ e Z = 111,8″. Un adattamento ai minimi quadrati dei termini sin 2T e sin³T sull’errore vero dell’equante dà Y = 447,9″ e Z = 112,3″: le costanti di Newton sono praticamente ottimali. Per *e* piccolo, Y ≈ *e*²/4 e Z ≈ ⅔*e*³ (in radianti).
- **L’errore.** Errore massimo sull’anomalia vera: 3,1″ per *e* = 0,0934 (equazione del centro massima 10,7°); 2,3″ per *e* = 0,0873 (equazione del centro massima 10,0°, il valore citato da Newton per Marte). L’equante semplice (Y = Z = 0) sbaglia fino a 492″. L’affermazione «l’errore supererà a stento un secondo» è dunque ottimistica di un fattore 2–3, ma il metodo riduce l’errore dell’equante di circa 200 volte. Con la lezione di Motte («half the greater semi-axis») l’errore salirebbe a 84″.
- Il «metodo di Ward» risolve il triangolo SHP: noti l’angolo in H, SH = 2*ae* e SP + HP = 2*a*, si ricavano l’angolo in S (moto vero) e la distanza SP.

### N7. Prop. XXXII: la caduta rettilinea come ellisse degenere

Newton passa dal moto su una conica alla caduta rettilinea facendo tendere a zero la larghezza della conica a semiasse fisso: il fuoco va nell’estremo dell’asse e la legge delle aree resta valida sul cerchio ausiliario. In termini moderni, per la caduta da ferma da distanza R:

*t* = √(R³/2μ) · [arccos √(*r*/R) + √((*r*/R)(1 − *r*/R))].

**Verifica numerica** (R = 1, μ = 1). Integrazione numerica dell’equazione del moto (Runge-Kutta) e tempo ricavato dall’area ASD del cerchio sul diametro AS (Prop. XXXV–XXXVI, con raggio uniforme SO = ½):

| *r* | *t* numerico | *t* dall’area |
|---|---|---|
| 0,8 | 0,610691 | 0,610691 |
| 0,5 | 0,908914 | 0,908914 |
| 0,2 | 1,065715 | 1,065715 |
| 0,05 | 1,105369 | 1,105369 |

**Caso iperbolico** (velocità superiore a quella di fuga; iperbole rettangola con AO = 0,7): il tempo dato dall’area SDEB coincide con quello analitico (0,012355 e 0,368545 in due posizioni).

### N8. Prop. XXXIII–XXXIV: velocità di caduta e velocità di fuga

Dalla conservazione dell’energia, *v*² = 2μ(1/*r* − 1/R); la velocità circolare alla stessa distanza è *v*꜀² = μ/*r*. Il rapporto *v*²/*v*꜀² = 2(R − *r*)/R = AC/AO, con AO = R/2: è l’enunciato. Numericamente: per *r* = 0,8, *v*/*v*꜀ = 0,632456 = √(0,2/0,5); per *r* = 0,2, 1,264911 = √(0,8/0,5).

- **Cor. 2** della Prop. XXXIII: con *v* = *v*꜀ diretta verso l’alto l’energia è −μ/2*r*₀ e l’altezza massima è 2*r*₀ (verificato).
- **Prop. XXXIV**: nel caso parabolico (A all’infinito) *v* = √(2μ/*r*), cioè la velocità circolare alla distanza *r*/2. È la moderna **velocità di fuga**.

### N9. Prop. XXXV–XXXVII: tempi come aree

La Prop. XXXV trasforma il tempo di caduta in un’area descritta uniformemente: un corpo che ruota sul cerchio di raggio uguale al semilato retto *p*/2 descrive area con velocità ½√(μ*p*/2). Nel caso della parabola (caduta da distanza infinita) ho confrontato il tempo vero, (√2/3)(*r*₁^{3/2} − *r*₂^{3/2})/√μ, con quello ricavato dall’area SDd: da 2 a 1, 0,861929 in entrambi i casi; da 4 a 0,5, 3,604569. Nella Prop. XXXVII il rapporto GA : ½AS = *v*² : *v*꜀² è confermato per *v*/*v*꜀ = 0,5 (0,25) e 1,2 (1,44, caso iperbolico).

### N10. Prop. XXXVIII: forza proporzionale alla distanza

È il moto armonico: *r* = R cos ω*t*. Il tempo è proporzionale all’arco AD, la velocità al seno retto CD, lo spazio percorso AC al seno verso. Verifica (R = 1, ω = 1): per *r* = 0,9, tempo 0,451027 = arco; velocità 0,435890 = seno; AC = 0,1 = seno verso. **Cor. 2**: il tempo per giungere al centro vale π/2 = 1,570796 sia partendo da 0,3 sia da 2,0: è l’isocronismo, che non dipende dall’ampiezza.

### N11. Prop. XXXIX: il teorema dell’energia in forma geometrica

L’area ABGE sotto la curva della forza è, oggi, ∫F d*r*; la sua proporzionalità a *v*² è il teorema dell’energia cinetica, ½*v*² = ∫F d*r*. Il tempo è l’area sotto la curva di 1/*v*: *t* = ∫d*r*/*v*. La «retta il cui quadrato è uguale all’area» e il «lato quadrato» sono la radice quadrata.

**Verifica numerica.** Con F = μ/*r*² e partenza da 1: per *r* = 0,5, *v* = 1,414214 e *t* = 0,908914, uguali ai valori della Prop. XXXII (nota N7). Con una forza arbitraria F = *x*⁻³ + 0,5:

- **Cor. 1**: il corpo che cade da P con forza uniforme 2, con PD × DR uguale all’area ABFD, giunge in D con velocità 1,157936, come il corpo vero;
- **Cor. 3**: il rapporto fra il tempo De del corpo vero e il tempo PD del corpo con forza uniforme vale 0,318141, uguale al rapporto DLme : 2PD × DL.

### N12. Prop. XL: conservazione dell’energia; il fattore n del Cor. 2

La Prop. XL è, in termini moderni, la conservazione dell’energia meccanica per forze centrali: la velocità dipende soltanto dalla distanza dal centro. Il **Cor. 1** dice che i vincoli lisci (filo, superficie senza attrito) non compiono lavoro, perché agiscono perpendicolarmente al moto. **Verifica numerica** con la forza F(*r*) = *r*⁻²·⁵ + 0,3*r* e un’orbita qualsiasi: alle distanze 1,2452; 1,1158; 0,9857; 1,1967 le velocità sull’orbita e quelle del moto rettilineo coincidono alla sesta cifra.

**Cor. 2.** Con F = *k*Aⁿ⁻¹ si ha *v*² = (2*k*/*n*)(Pⁿ − Aⁿ) = (2*k*/*n*²)(*n*Pⁿ − *n*Aⁿ). Verificato numericamente per *n* = 2, −1, ½. La forma √(*n*Pⁿ − *n*Aⁿ), letta nella trascrizione, è reale per ogni *n* ≠ 0, perché A ≤ P; la forma di Motte, √(Pⁿ − Aⁿ), è immaginaria per *n* < 0 (per esempio *n* = −1, la gravità). Il caso *n* = 0 (forza ∝ 1/A) richiede un logaritmo e non è coperto dalla formula.

### N13. Prop. XLI: le orbite per quadratura

È la soluzione generale del moto in un campo centrale, ridotta a due quadrature. In notazione moderna, con *h* = *r*² dθ/d*t* costante e ½*v*² = area ABFD:

*t* = ∫ d*r* / √(*v*² − *h*²/*r*²), θ = ∫ *h* d*r* / (*r*² √(*v*² − *h*²/*r*²)).

Le curve ab e ac della costruzione sono gli integrandi; Z = Q/A è la velocità trasversale (in scala). **Verifica numerica** (forza inversa del quadrato, partenza da V a distanza 1 con velocità perpendicolare 1,2): l’angolo VCI ricavato dall’area VDca vale 1,09893449, 1,80007253 e π alle distanze 1,2; 1,6 e 2,571429, uguale all’anomalia vera dell’ellisse kepleriana; l’area VDba coincide con l’area focale VIC (rapporto 1,000000).

- **Cor. 1**: all’afelio *r* = 2,571429 si ha ABFD − ZZ = 4 × 10⁻¹⁷: gli apsidi sono gli zeri di ABFD − ZZ.
- **Cor. 2**: alla distanza 1,5 il seno dell’angolo fra traiettoria e raggio vale Z/√ABFD = 0,909718, uguale a *v*ₜ/*v*.

### N14. Prop. XLI, Cor. 3: forza inversa del cubo

Con forza μ/*r*³ l’equazione dell’orbita (in *u* = 1/*r*) è lineare, e partendo perpendicolarmente al raggio si ottiene *r* = *a*/cos(*k*θ) oppure *r* = *a*/cosh(*k*θ), con *k* = √|1 − μ/*h*²|. La costruzione di Newton dà proprio queste curve: per l’ellisse, con R = (*a* cos *u*, *b* sin *u*), si ha CT = *a*/cos *u* e settore VCR = *abu*/2; per l’iperbole, CT = *a*/cosh *u* e settore = *abu*/2 (verificato). Prendendo l’angolo VCP proporzionale al settore, CP = CT riproduce le due famiglie.

**Verifica numerica** (integrazione dell’equazione del moto, partenza da *r* = 1 con velocità 1 perpendicolare): attrazione forte (μ = 2, iperbole): spirale verso il centro, scarto massimo dalla costruzione 7 × 10⁻¹³ fino a *r* = 0,05; attrazione debole (μ = 0,5, ellisse): fuga all’infinito, scarto 4 × 10⁻¹⁴; forza centrifuga (μ = −0,5, ancora ellisse con *k* > 1): scarto 2 × 10⁻¹⁴. Queste curve sono oggi note come spirali di Cotes.

### N15. Prop. XLII: il problema ai valori iniziali

La Prop. XLII mostra che posizione, velocità e direzione iniziali, con la legge della forza, determinano il moto: la costruzione combina la Prop. XXXIX (energia, curva BFg) e la Prop. XLI (quadrature, curve abv, acw). La costante Q, cioè il momento angolare, si ricava dall’angolo CIK di partenza. L’avvertenza finale dichiara l’ipotesi di simmetria sferica della forza («a distanze uguali dal centro sia ovunque la stessa») e annuncia la Sezione IX sulle orbite mobili.

---

## Controllo della copertura

Le pagine 1726 sono quelle segnate nella trascrizione; le pagine Motte sono quelle dei marcatori `Page_n` dell’EPUB.

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| S6.01–S6.06 | *Corporis in data trajectoria parabolica* | Prop. XXX e Cor. 1–3 | pp. 104–105 | pp. 153–154 |
| S6.07–S6.10 | *Nulla extat figura ovalis* | Lemma XXVIII e Corollario | pp. 106–108 | pp. 154–156 |
| S6.11–S6.13 | *Corporis in data trajectoria elliptica* | Prop. XXXI | pp. 108–109 | pp. 156–157 |
| S6.14 | *Cæterum, cum difficilis sit* | Scolio: metodo iterativo per l’ellisse | pp. 109–110 | pp. 157–158 |
| S6.15 | *Non dissimili calculo* | Scolio: iperbole | p. 111 | p. 158 |
| S6.16 | *Atque his calculis* | Scolio: calcolo astronomico | pp. 111–112 | pp. 158–159 |
| S6.17 | *Hactenus de motu corporum* | Passaggio alla Sezione VII | p. 112 | p. 159 |
| S7.01–S7.04 | *Posito quod vis centripeta sit reciproce* | Prop. XXXII, Casi 1–3 | pp. 112–113 | pp. 159–161 |
| S7.05–S7.08 | *Positis jam inventis* | Prop. XXXIII e Cor. 1–2 | pp. 114–115 | pp. 161–162 |
| S7.09–S7.10 | *Si figura BED parabola est* | Prop. XXXIV | pp. 115–116 | p. 162 |
| S7.11–S7.14 | *Iisdem positis, dico quod area* | Prop. XXXV, Casi 1–2 | pp. 116–118 | pp. 162–164 |
| S7.15–S7.16 | *Corporis de loco dato A cadentis* | Prop. XXXVI | p. 118 | p. 164 |
| S7.17–S7.18 | *Corporis de loco dato sursum* | Prop. XXXVII | pp. 118–119 | pp. 164–165 |
| S7.19–S7.23 | *Posito quod vis centripeta proportionalis* | Prop. XXXVIII e Cor. 1–2 | p. 119 | p. 165 |
| S7.24–S7.28 | *Posita cujuscunque generis vi centripeta* | Prop. XXXIX | pp. 120–121 | pp. 165–166 |
| S7.29–S7.31 | *Si P sit locus*; *Unde si corpus*; *Tempus quoque* | Prop. XXXIX, Cor. 1–3 | pp. 121–122 | pp. 166–168 |
| S8.01–S8.05 | *Si corpus, cogente vi quacunque* | Prop. XL, seconda conclusione, Cor. 1–2 | pp. 123–124 | pp. 168–169 |
| S8.06–S8.09 | *Posita cujuscunque generis vi centripeta & concessis* | Prop. XLI | pp. 125–127 | pp. 169–171 |
| S8.10–S8.12 | *Hinc maximæ minimæque* | Prop. XLI, Cor. 1–3 | pp. 127–128 | p. 171 |
| S8.13–S8.14 | *Data lege vis centripetæ* | Prop. XLII | pp. 128–129 | pp. 171–172 |
| S8.15 | *Supponimus autem* | Avvertenza finale | p. 129 | p. 172 |

**Controlli eseguiti.**

1. **Rilettura frase per frase contro il latino.** Ho confrontato in sequenza ogni periodo delle tre trascrizioni (pp. 104–129) con la traduzione, dal titolo *De inventione motuum in orbibus datis* all’ultima frase, *Superest ut de motu eorum in orbibus, qui circa centrum virium revolvuntur, adjiciamus pauca.* Nessuna frase manca. Le uniche integrazioni sono tra parentesi quadre (S6.08, S6.16) e sono motivate nell’apparato. Le 114 frasi latine delle dimostrazioni della Parte B sono state estratte automaticamente dalla trascrizione, e la loro successione copre per intero le dimostrazioni incluse.
2. **Matematica.** Tutte le costruzioni e le leggi verificabili sono state controllate su figure di prova (note N1–N14): Prop. XXX e Cor. 1–3; Prop. XXXI (equazione di Keplero); i due metodi iterativi dello Scolio; il «calcolo particolare» astronomico (con la stima dell’errore e il controllo della lezione di Motte); le leggi di caduta per forza ∝ 1/*r*² (Prop. XXXII–XXXVII, casi ellittico, parabolico e iperbolico) e ∝ *r* (Prop. XXXVIII); Prop. XXXIX e Cor. 1, 3; Prop. XL e Cor. 2; Prop. XLI e Cor. 1–3. Tutte le affermazioni di Newton risultano esatte, salvo la stima d’errore dello Scolio (2–3″ invece di «a stento un secondo», nota N6).
3. **Confronto con Motte.** Ho confrontato tutte e tre le Sezioni, pp. 153–172, comprese le 45 formule SVG 112–156, rese come immagini e lette. Le divergenze sono nel § A.17.
4. **Parte B.** Validata con `check.py` sulle tre trascrizioni latine e sui tre file di Motte (esito riportato in fondo alla Parte B).

**Non ho potuto verificare:**

- **la stampa del 1726**: tutti i refusi e le lacune del § A.16 sono segnalati come probabili; in particolare la lacuna del Lemma XXVIII (S6.08), il fattore *n* nel Cor. 2 della Prop. XL (S8.05) e *infinitæ producto* (S8.12);
- **le figure originali** NATP00087-73…99: le relazioni geometriche sono ricostruite dalle lettere del testo; in particolare non ho potuto confermare sulla figura che B, nel calcolo astronomico dello Scolio, sia l’afelio (lo indica il calcolo, nota N6), né la forma delle aree ABTVME / ATVME (S7.26, S7.28);
- **la numerazione di pagina di Motte**, che deriva dai marcatori dell’EPUB Gutenberg e non da un esemplare a stampa; e la prima edizione di Motte (1729), che permetterebbe di attribuire gli errori di formula (SVG 115, 134) all’edizione 1846 o al traduttore.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Sezioni VI–VIII (Prop. XXX–XLII, Lemma XXVIII, Scolio) | **Fascicolo 8, presente documento, prima versione** |
| Lacuna del Lemma XXVIII (S6.08), *AO+[OD]* (S6.16), *nPⁿ − nAⁿ* (S8.05), *12Sc* (S7.14), *infinitæ producto* (S8.12) | Da controllare sulla stampa del 1726 (scansione ECCO) |
| Errori di formula di Motte 1846 (SVG 115, 134) e «half» in S6.16 | Da controllare su Motte 1729, come per PE³ nel Fascicolo 3 (F3) |
| Figure NATP00087-73…99 | Da vedere: confermare B afelio nello Scolio, la posizione di Q in Prop. XXXIII, le aree della Prop. XXXIX |
| Pagine interattive | Dati pronti nella Parte B per 16 unità. Candidati prioritari per la didattica: Prop. XXXI (trocoide e equazione di Keplero), Prop. XXXII (caduta come ellisse degenere), Prop. XXXVIII (moto armonico), Prop. XLI (orbite per quadratura) |
| Scolio della Prop. XXXI | Escluso dalla Parte B (non è lemma né proposizione), ma ha figure (FIG 75–79) e si presta a una pagina con il metodo di Newton-Raphson e il confronto con l’equante |
| Prop. XLI, Cor. 3 | Escluso dalla Parte B: ha figure (FIG 97–98) ma nessuna dimostrazione («tralascio per brevità»); candidato per una pagina sulle spirali di Cotes |
| Revisione filologica e scientifica indipendente | Da eseguire, come previsto dalla skill di verifica |

Il presente testo è una nuova traduzione assistita da IA. Non riproduce traduzioni italiane o inglesi moderne. **Licenza prevista** (decisione del curatore, Fascicolo 3): testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project e non va ridistribuita finché non se ne chiariscono le condizioni d’uso; il testo di Motte è di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Unità incluse (lemmi e proposizioni con figura o costruzione geometrica): Prop. XXX, Lemma XXVIII, Prop. XXXI, Prop. XXXII–XXXIX, Prop. XXXIX Cor. 1 e Cor. 3, Prop. XL–XLII. Esclusi: lo Scolio della Prop. XXXI e il Cor. 3 della Prop. XLI (vedi registro); i corollari privi di dimostrazione propria con figura.

Convenzioni:

- `la`: frase latina esatta della trascrizione, compresi refusi e formule appiattite (annotati in `nota` e nel § A.16); i marcatori di pagina e di figura sono tolti;
- `it`: la traduzione di questo fascicolo;
- `en`: Motte 1846, allineato per senso; le formule stampate come immagini restano indicate `[SVG n]`;
- `dipende_da`: soltanto i rimandi citati nella frase;
- `figura.mostra`: elementi da rendere visibili al passo, cumulativi salvo indicazione; `figura.evidenzia`: relazioni da mettere in risalto.

```json
{
 "fascicolo": "08-L1-S6-8",
 "versione": "0.1",
 "data": "2026-11-08",
 "convenzioni": {
  "dipende_da": "solo rimandi citati esplicitamente nella frase latina",
  "en": "Motte 1846, allineato per senso; [SVG n] = formula stampata come immagine",
  "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione",
  "la": ""
 },
 "unita": [
  {
   "id": "L1-P30",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXX — il luogo nella parabola",
   "copertura": [
    "S6.01",
    "S6.02",
    "S6.03"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 153–154"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare il luogo, a un tempo assegnato, di un corpo che si muove su una traiettoria parabolica data.",
    "en": "To find at any assigned time the place of a body moving in a given parabolic trajectory."
   },
   "figura_base": {
    "punti": [
     "S",
     "A",
     "G",
     "H",
     "P",
     "O"
    ],
    "vincoli": [
     "parabola di fuoco S e vertice principale A",
     "G punto medio di AS",
     "GH perpendicolare ad AS, GH = 3M, con 4AS × M = area APS",
     "cerchio di centro H e raggio HS: passa per A e per S",
     "PO perpendicolare all’asse, O sull’asse"
    ]
   },
   "passi": [
    {
     "id": "L1-P30-p1",
     "la": "",
     "it": "Sia S il fuoco e A il vertice principale della parabola, e sia 4AS × M uguale all’area parabolica APS che il raggio SP o ha descritto dopo che il corpo è uscito dal vertice, o deve descrivere prima che il corpo vi giunga.",
     "en": "Let S be the focus, and A the principal vertex of the parabola; and suppose 4AS × M equal to the parabolic area to be cut off APS, which either was described by the radius SP, since the body's departure from the vertex, or is to be described thereby before its arrival there.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "parabola",
       "S",
       "A",
       "asse AS",
       "raggio SP",
       "area APS"
      ],
      "evidenzia": [
       "area APS = 4AS × M"
      ]
     }
    },
    {
     "id": "L1-P30-p2",
     "la": "",
     "it": "La grandezza di quell’area da tagliare si conosce dal tempo, che le è proporzionale.",
     "en": "Now the quantity of that area to be cut off is known from the time which is proportional to it.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "area APS proporzionale al tempo"
      ]
     }
    },
    {
     "id": "L1-P30-p3",
     "la": "",
     "it": "Si divida AS a metà in G, si innalzi la perpendicolare GH uguale a 3M, e il cerchio descritto con centro H e raggio HS taglierà la parabola nel luogo cercato P.",
     "en": "Bisect AS in G, and erect the perpendicular GH equal to 3M, and a circle described about the centre H, with the interval HS, will cut the parabola in the place P required.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "G",
       "perpendicolare GH",
       "H",
       "cerchio di centro H e raggio HS",
       "P"
      ],
      "evidenzia": [
       "GH = 3M",
       "P = cerchio ∩ parabola"
      ]
     }
    },
    {
     "id": "L1-P30-p4",
     "la": "",
     "it": "Infatti, abbassata sull’asse la perpendicolare PO e condotta PH, si ha AG² + GH² (= HP² = (AO − AG)² + (PO − GH)²) = AO² + PO² − 2GAO − 2GH × PO + AG² + GH².",
     "en": "For letting fall PO perpendicular on the axis, and drawing [SVG 112], there will be [SVG 113] (= [SVG 114]) = [SVG 115].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "perpendicolare PO",
       "O",
       "segmento PH"
      ],
      "evidenzia": [
       "HP = HS",
       "AG² + GH² = HP²"
      ]
     },
     "nota": "Formula appiattita nella trascrizione: «AO−AG¯: quad.» = (AO − AG)²; «2GAO» = 2GA × AO. Motte, SVG 115, stampa «− 2GH + PO» per «− 2GH × PO» (§ A.17)."
    },
    {
     "id": "L1-P30-p5",
     "la": "",
     "it": "Quindi 2GH × PO (= AO² + PO² − 2GAO) = AO² + ¾PO².",
     "en": "Whence [SVG 116].",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "PO² = 4AS × AO"
      ]
     },
     "nota": "«34POq» = ¾PO², perché 2GA × AO = AS × AO = ¼PO²."
    },
    {
     "id": "L1-P30-p6",
     "la": "",
     "it": "Al posto di AO² si scriva AO × PO²/4AS; e, divisi tutti i termini per 3PO e moltiplicati per 2AS, si avrà (4/3)GH × AS (= ⅙AO × PO + ½AS × PO = (AO + 3AS)/6 × PO = (4AO − 3SO)/6 × PO = area APO − SPO) = area APS.",
     "en": "For [SVG 117] write [SVG 118]; then dividing all the terms by 3PO, and multiplying them by 2AS, we shall have [SVG 119] = to the area [SVG 120] = to the area APS.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area parabolica APO",
       "triangolo SPO"
      ],
      "evidenzia": [
       "(4/3)GH × AS = area APO − SPO = area APS"
      ]
     },
     "nota": "Frazioni appiattite: «AO×POq4AS» = AO × PO²/4AS; «43» = 4/3; «16» = 1/6; «12» = 1/2; «AO+3AS6» = (AO + 3AS)/6."
    },
    {
     "id": "L1-P30-p7",
     "la": "",
     "it": "Ma GH era 3M, e quindi (4/3)GH × AS è 4AS × M.",
     "en": "But GH was 3M, and therefore [SVG 121] is 4AS × M.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "(4/3)GH × AS = 4AS × M"
      ]
     },
     "nota": "«43GH×AS» = (4/3)GH × AS."
    },
    {
     "id": "L1-P30-p8",
     "la": "",
     "it": "Dunque l’area APS è uguale all’area da tagliare 4AS × M. C.V.D.",
     "en": "Wherefore the area cut off APS is equal to the area that was to be cut off 4AS × M. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "area APS = 4AS × M"
      ]
     },
     "nota": "«abscindenæ»: refuso probabile della trascrizione per «abscindendæ»."
    }
   ]
  },
  {
   "id": "L1-Lem28",
   "tipo": "Lemma",
   "titolo": "Lemma XXVIII — nessun ovale ha area determinabile con equazioni finite",
   "copertura": [
    "S6.07",
    "S6.08"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 154–155"
   },
   "enunciato": {
    "la": "",
    "it": "Non esiste alcuna figura ovale la cui area, tagliata da rette a piacere, si possa trovare in generale per mezzo di equazioni finite quanto al numero dei termini e delle dimensioni.",
    "en": "There is no oval figure whose area, cut off by right lines at pleasure, can be universally found by means of equations of any number of finite terms and dimensions."
   },
   "figura_base": {
    "punti": [
     "polo (punto interno all’ovale)",
     "punto mobile sulla retta rotante"
    ],
    "vincoli": [
     "ovale dato",
     "retta che ruota uniformemente attorno al polo",
     "velocità del punto mobile proporzionale al quadrato della corda interna all’ovale",
     "la distanza dal polo è proporzionale all’area tagliata",
     "spirale con infinite spire",
     "retta secante data di posizione"
    ]
   },
   "passi": [
    {
     "id": "L1-Lem28-p1",
     "la": "",
     "it": "All’interno dell’ovale sia dato un punto qualsiasi, attorno al quale, come attorno a un polo, ruoti senza sosta una linea retta con moto uniforme; e intanto su quella retta un punto mobile esca dal polo e proceda sempre con una velocità che sia come il quadrato della parte di quella retta interna all’ovale.",
     "en": "Suppose that within the oval any point is given, about which as a pole a right line is perpetually revolving with an uniform motion, while in that right line a moveable point going out from the pole moves always forward with a velocity proportional to the square of that right line within the oval.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "ovale",
       "polo",
       "retta rotante",
       "punto mobile"
      ],
      "evidenzia": [
       "velocità ∝ (corda interna)²"
      ]
     }
    },
    {
     "id": "L1-Lem28-p2",
     "la": "",
     "it": "Con questo moto quel punto descriverà una spirale con infinite spire.",
     "en": "By this motion that point will describe a spiral with infinite circumgyrations.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "spirale"
      ],
      "evidenzia": [
       "infinite spire"
      ]
     }
    },
    {
     "id": "L1-Lem28-p3",
     "la": "",
     "it": "Ora, se la porzione dell’area dell’ovale tagliata da quella retta si può trovare per mezzo di un’equazione finita, per mezzo della stessa equazione si troverà anche la distanza del punto dal polo, che è proporzionale a quest’area; perciò tutti i punti della spirale si possono trovare per mezzo di un’equazione finita, e quindi anche l’intersezione con la spirale di una retta qualsiasi data di posizione si può trovare per mezzo di un’equazione finita.",
     "en": "Now if a portion of the area of the oval cut off by that right line could be found by a finite equation, the distance of the point from the pole, which is proportional to this area, might be found by the same equation, and therefore all the points of the spiral might be found by a finite equation also; and therefore the intersection of a right line given in position with the spiral might also be found by a finite equation.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area tagliata",
       "distanza dal polo",
       "retta secante"
      ],
      "evidenzia": [
       "distanza ∝ area"
      ]
     }
    },
    {
     "id": "L1-Lem28-p4",
     "la": "",
     "it": "Ma ogni retta prolungata all’infinito taglia la spirale in un numero infinito di punti; e l’equazione con cui si trova un’intersezione qualsiasi di due linee mostra tutte le loro intersezioni con altrettante radici, e perciò sale a tante dimensioni quante sono le intersezioni.",
     "en": "But every right line infinitely produced cuts a spiral in an infinite number of points; and the equation by which any one intersection of two lines is found at the same time exhibits all their intersections by as many roots, and therefore rises to as many dimensions as there are intersections.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "intersezioni retta–spirale"
      ],
      "evidenzia": [
       "infinite intersezioni"
      ]
     }
    },
    {
     "id": "L1-Lem28-p5",
     "la": "",
     "it": "Poiché due cerchi si tagliano a vicenda in due punti, una delle intersezioni non si troverà se non per mezzo di un’equazione di due dimensioni, con la quale si trovi anche l’altra intersezione.",
     "en": "Because two circles mutually cut one another in two points, one of those intersections is not to be found but by an equation of two dimensions, by which the other intersection may be also found.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "due cerchi",
       "due intersezioni"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem28-p6",
     "la": "",
     "it": "Poiché due sezioni coniche possono avere quattro intersezioni, nessuna di esse si può trovare in generale se non per mezzo di un’equazione di quattro dimensioni, con la quale si trovino tutte insieme.",
     "en": "Because there may be four intersections of two conic sections, any one of them is not to be found universally, but by an equation of four dimensions, by which they may be all found together.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "due coniche",
       "quattro intersezioni"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem28-p7",
     "la": "",
     "it": "Se infatti quelle intersezioni si cercano separatamente, poiché la legge e la condizione di tutte è la stessa, il calcolo sarà lo stesso in ciascun caso, e perciò sempre la stessa la conclusione, che dunque deve comprendere tutte le intersezioni insieme e mostrarle indifferentemente.",
     "en": "For if those intersections are severally sought, because the law and condition of all is the same, the calculus will be the same in every case, and therefore the conclusion always the same, which must therefore comprehend all those intersections at once within itself, and exhibit them all indifferently.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "stesso calcolo per tutte le intersezioni"
      ]
     }
    },
    {
     "id": "L1-Lem28-p8",
     "la": "",
     "it": "Di qui anche le intersezioni delle sezioni coniche con le curve della terza potenza, poiché possono essere sei, risultano insieme per mezzo di equazioni di sei dimensioni; e le intersezioni di due curve della terza potenza, poiché possono essere nove, risultano insieme per mezzo di equazioni di nove dimensioni.",
     "en": "Hence it is that the intersections of the conic sections with the curves of the third order, because they may amount to six, come out together by equations of six dimensions; and the intersections of two curves of the third order, because they may amount to nine, come out together by equations of nine dimensions.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "6 = 2 × 3; 9 = 3 × 3"
      ]
     }
    },
    {
     "id": "L1-Lem28-p9",
     "la": "",
     "it": "Se ciò non avvenisse necessariamente, si potrebbero ridurre tutti i problemi solidi a piani, e quelli più che solidi a solidi.",
     "en": "If this did not necessarily happen, we might reduce all solid to plane Problems, and those higher than solid to solid Problems.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem28-p10",
     "la": "",
     "it": "Parlo qui di curve irriducibili quanto alla potenza.",
     "en": "But here I speak of curves irreducible in power.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem28-p11",
     "la": "",
     "it": "Se infatti l’equazione per cui la curva è definita si può ridurre a una potenza inferiore, la curva non sarà unica, ma composta di due o più curve, le cui intersezioni si possono trovare separatamente con calcoli diversi.",
     "en": "For if the equation by which the curve is defined may be reduced to a lower power, the curve will not be one single curve, but composed of two, or more, whose intersections may be severally found by different calculuses.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem28-p12",
     "la": "",
     "it": "Allo stesso modo le due intersezioni delle rette con le sezioni coniche risultano sempre per mezzo di equazioni di due dimensioni; le tre delle rette con le curve irriducibili [della terza potenza per mezzo di equazioni di tre dimensioni; le quattro delle rette con le curve irriducibili] della quarta potenza per mezzo di equazioni di quattro dimensioni; e così all’infinito.",
     "en": "After the same manner the two intersections of right lines with the conic sections come out always by equations of two dimensions; the three intersections of right lines with the irreducible curves of the third order by equations of three dimensions; the four intersections of right lines with the irreducible curves of the fourth order, by equations of four dimensions; and so on in infinitum.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "k intersezioni ↔ equazione di k dimensioni"
      ]
     },
     "nota": "Lacuna probabile della trascrizione: la frase passa da «ternæ rectarum & curvarum irreducibilium» a «quartæ potestatis … quatuor». La traduzione integra tra parentesi quadre la parte mancante, come in Motte (§ A.2). «in infinium»: refuso probabile per «in infinitum»."
    },
    {
     "id": "L1-Lem28-p13",
     "la": "",
     "it": "Dunque le intersezioni, in numero infinito, della retta e della spirale, poiché questa curva è semplice e non riducibile a più curve, richiedono equazioni infinite quanto al numero delle dimensioni e delle radici, con le quali si possano mostrare tutte insieme.",
     "en": "Wherefore the innumerable intersections of a right line with a spiral, since this is but one simple curve and not reducible to more curves, require equations infinite in number of dimensions and roots, by which they may be all exhibited together.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "intersezioni retta–spirale"
      ],
      "evidenzia": [
       "infinite radici"
      ]
     }
    },
    {
     "id": "L1-Lem28-p14",
     "la": "",
     "it": "È infatti la stessa per tutte la legge, e lo stesso il calcolo.",
     "en": "For the law and calculus of all is the same.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-Lem28-p15",
     "la": "",
     "it": "Se infatti dal polo si abbassa la perpendicolare sulla retta secante, e quella perpendicolare ruota attorno al polo insieme con la secante, le intersezioni della spirale passeranno l’una nell’altra: quella che era la prima, cioè la più vicina, dopo una rivoluzione sarà la seconda, dopo due la terza, e così via; né intanto l’equazione muterà, se non per il mutare della grandezza delle quantità mediante le quali si determina la posizione della secante.",
     "en": "For if a perpendicular is let fall from the pole upon that intersecting right line, and that perpendicular together with the intersecting line revolves about the pole, the intersections of the spiral will mutually pass the one into the other; and that which was first or nearest, after one revolution, will be the second; after two, the third; and so on: nor will the equation in the mean time be changed but as the magnitudes of those quantities are changed, by which the position of the intersecting line is determined.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "perpendicolare dal polo alla secante",
       "rotazione della secante"
      ],
      "evidenzia": [
       "la prima intersezione diventa la seconda, poi la terza"
      ]
     }
    },
    {
     "id": "L1-Lem28-p16",
     "la": "",
     "it": "Perciò, poiché quelle quantità dopo ogni rivoluzione ritornano alle grandezze iniziali, l’equazione ritornerà alla forma iniziale; e quindi una sola e medesima equazione mostrerà tutte le intersezioni, e avrà perciò un numero infinito di radici, con le quali si possano mostrare tutte.",
     "en": "Wherefore since those quantities after every revolution return to their first magnitudes, the equation will return to its first form; and consequently one and the same equation will exhibit all the intersections, and will therefore have an infinite number of roots, by which they may be all exhibited.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "dopo ogni giro l’equazione torna la stessa"
      ]
     }
    },
    {
     "id": "L1-Lem28-p17",
     "la": "",
     "it": "Non si può dunque trovare in generale l’intersezione della retta e della spirale per mezzo di un’equazione finita; e perciò non esiste alcun ovale la cui area, tagliata da rette prescritte, si possa esprimere in generale per mezzo di una tale equazione.",
     "en": "And therefore the intersection of a right line with a spiral cannot be universally found by any finite equation; and of consequence there is no oval figure whose area cut off by right lines at pleasure, can be universally exhibited by any such equation.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "nessuna equazione finita"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P31",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXXI — il luogo nell’ellisse: la trocoide",
   "copertura": [
    "S6.11",
    "S6.12",
    "S6.13"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 156–157"
   },
   "enunciato": {
    "la": "",
    "it": "Trovare il luogo, a un tempo assegnato, di un corpo che si muove su una traiettoria ellittica data.",
    "en": "To find the place of a body moving in a given elliptic trajectory at any assigned time."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "S",
     "O",
     "P",
     "G",
     "H",
     "E",
     "F",
     "K",
     "L",
     "Q",
     "R"
    ],
    "vincoli": [
     "ellisse APB di centro O, fuoco S, vertice principale A",
     "G sul prolungamento di OA con OG : OA = OA : OS",
     "GH perpendicolare a OG",
     "ruota GEF di centro O e raggio OG che rotola su GH",
     "trocoide ALI descritta dal punto A della ruota (OA < OG)",
     "GK : perimetro GEFG = tempo da A a P : periodo",
     "KL perpendicolare a GH; LP parallela a KG",
     "semicerchio AQB di raggio OA; SR perpendicolare a OQ"
    ]
   },
   "passi": [
    {
     "id": "L1-P31-p1",
     "la": "",
     "it": "Dell’ellisse APB sia A il vertice principale, S il fuoco, O il centro, e sia P il luogo del corpo da trovare.",
     "en": "Suppose A to be the principal vertex, S the focus, and O the centre of the ellipsis APB; and let P be the place of the body to be found.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "ellisse APB",
       "A",
       "S",
       "O",
       "P (da trovare)"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P31-p2",
     "la": "",
     "it": "Si prolunghi OA fino a G, in modo che OG stia a OA come OA sta a OS.",
     "en": "Produce OA to G so as OG may be to OA as OA to OS.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "G"
      ],
      "evidenzia": [
       "OG : OA = OA : OS"
      ]
     },
     "nota": "«OGad OA»: spazio mancante nella trascrizione."
    },
    {
     "id": "L1-P31-p3",
     "la": "",
     "it": "Si innalzi la perpendicolare GH; con centro O e raggio OG si descriva il cerchio GEF; e sulla riga GH, come su una base, la ruota GEF avanzi girando attorno al proprio asse, e intanto con il suo punto A descriva la trocoide ALI.",
     "en": "Erect the perpendicular GH; and about the centre O, with the interval OG, describe the circle GEF; and on the ruler GH, as a base, suppose the wheel GEF to move forwards, revolving about its axis, and in the mean time by its point A describing the cycloid ALI.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "GH",
       "ruota GEF",
       "trocoide ALI"
      ],
      "evidenzia": [
       "il punto A della ruota descrive la trocoide"
      ]
     },
     "nota": "Motte: «cycloid» per «trochoidem» (§ A.3)."
    },
    {
     "id": "L1-P31-p4",
     "la": "",
     "it": "Fatto ciò, si prenda GK in rapporto al perimetro GEFG della ruota come il tempo in cui il corpo, avanzando da A, ha descritto l’arco AP sta al tempo di una rivoluzione nell’ellisse.",
     "en": "Which done, take GK to the perimeter GEFG of the wheel, in the ratio of the time in which the body proceeding from A described the arc AP, to the time of a whole revolution in the ellipsis.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "K"
      ],
      "evidenzia": [
       "GK : perimetro = tempo : periodo"
      ]
     }
    },
    {
     "id": "L1-P31-p5",
     "la": "",
     "it": "Si innalzi la perpendicolare KL, che incontri la trocoide in L, e la LP, condotta parallela a KG, incontrerà l’ellisse nel luogo cercato P del corpo.",
     "en": "Erect the perpendicular KL meeting the cycloid in L; then LP drawn parallel to KG will meet the ellipsis in P, the required place of the body.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "KL",
       "L",
       "LP",
       "P"
      ],
      "evidenzia": [
       "LP ∥ KG"
      ]
     }
    },
    {
     "id": "L1-P31-p6",
     "la": "",
     "it": "Infatti, con centro O e raggio OA si descriva il semicerchio AQB; LP, prolungata se occorre, incontri l’arco AQ in Q, e si congiungano SQ, OQ.",
     "en": "For about the centre O with the interval OA describe the semi-circle AQB, and let LP, produced, if need be, meet the arc AQ, in Q, and join SQ, OQ.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "semicerchio AQB",
       "Q",
       "SQ",
       "OQ"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P31-p7",
     "la": "",
     "it": "OQ incontri l’arco EFG in F, e su OQ si abbassi la perpendicolare SR.",
     "en": "Let OQ meet the arc EFG in F, and upon OQ let fall the perpendicular SR.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "F",
       "SR"
      ],
      "evidenzia": [
       "SR ⟂ OQ"
      ]
     }
    },
    {
     "id": "L1-P31-p8",
     "la": "",
     "it": "L’area APS è come l’area AQS, cioè come la differenza fra il settore OQA e il triangolo OQS, ossia come la differenza dei rettangoli ½OQ × AQ e ½OQ × SR, cioè, essendo dato ½OQ, come la differenza fra l’arco AQ e la retta SR; e perciò (poiché sono uguali i rapporti dati di SR al seno dell’arco AQ, di OS a OA, di OA a OG, di AQ a GF, e, per separazione, di AQ − SR a GF − seno dell’arco AQ) come GK, differenza fra l’arco GF e il seno dell’arco AQ. C.V.D.",
     "en": "The area APS is as the area AQS, that is, as the difference between the sector OQA and the triangle OQS, or as the difference of the rectangles [SVG 122], and [SVG 123], that is, because [SVG 124] is given, as the difference between the arc AQ and the right line SR; and therefore (because of the equality of the given ratios SR to the sine of the arc AQ, OS to OA, OA to OG, AQ to GF; and by division, AQ - SR to GF - sine of the arc AQ) as GK, the difference between the arc GF and the sine of the arc AQ. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "settore OQA",
       "triangolo OQS"
      ],
      "evidenzia": [
       "area APS ∝ arco AQ − SR ∝ GK"
      ]
     },
     "nota": "«12OQ×AQ» = ½OQ × AQ. È l’equazione di Keplero (nota N3)."
    }
   ]
  },
  {
   "id": "L1-P32",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXXII — caduta rettilinea con forza inversa del quadrato",
   "copertura": [
    "S7.01",
    "S7.02",
    "S7.03",
    "S7.04"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 159–161"
   },
   "enunciato": {
    "la": "",
    "it": "Posto che la forza centripeta sia inversamente proporzionale al quadrato della distanza dei luoghi dal centro, definire gli spazi che un corpo, cadendo in linea retta, descrive in tempi dati.",
    "en": "Supposing that the centripetal force is reciprocally proportional to the square of the distance of the places from the centre; it is required to define the spaces which a body, falling directly, describes in given times."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "S",
     "C",
     "D",
     "P",
     "R",
     "E",
     "f"
    ],
    "vincoli": [
     "Caso 1: ellisse ARPB di fuoco S; semicerchio ADB sull’asse maggiore AB; DPC perpendicolare all’asse",
     "Caso 2: iperbole RPB; iperbole rettangola BED sullo stesso diametro principale AB",
     "Caso 3: parabola RPB; parabola BED con lo stesso vertice B, fissa",
     "limite: larghezza della conica → 0, fuoco S → B"
    ]
   },
   "passi": [
    {
     "id": "L1-P32-p1",
     "la": "",
     "it": "Caso 1. Se il corpo non cade perpendicolarmente, esso descriverà (per il Cor. 1 della Prop. XIII) una sezione conica il cui fuoco coincide con il centro delle forze. Sia ARPB quella sezione conica e S il suo fuoco.",
     "en": "CASE 1. If the body does not fall perpendicularly, it will (by Cor. 1 Prop. XIII) describe some conic section whose focus is placed in the centre of force. Suppose that conic section to be ARPB and its focus S.",
     "dipende_da": [
      "Prop. XIII, Cor. 1"
     ],
     "figura": {
      "mostra": [
       "sezione conica ARPB",
       "fuoco S"
      ],
      "evidenzia": [
       "fuoco = centro delle forze"
      ]
     },
     "nota": "Nella trascrizione «um <113> bilicus»: parola spezzata dal cambio di pagina (qui tolto il marcatore)."
    },
    {
     "id": "L1-P32-p2",
     "la": "",
     "it": "E in primo luogo, se la figura è un’ellisse, sul suo asse maggiore AB si descriva il semicerchio ADB, e per il corpo che cade passi la retta DPC perpendicolare all’asse; condotte DS, PS, l’area ASD sarà proporzionale all’area ASP, e perciò anche al tempo.",
     "en": "And, first, if the figure be an ellipsis, upon the greater axis thereof AB describe the semi-circle ADB, and let the right line DPC pass through the falling body, making right angles with the axis; and drawing DS, PS, the area ASD will be proportional to the area ASP, and therefore also to the time.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "semicerchio ADB",
       "retta DPC",
       "D",
       "P",
       "C",
       "DS",
       "PS"
      ],
      "evidenzia": [
       "area ASD ∝ area ASP ∝ tempo"
      ]
     }
    },
    {
     "id": "L1-P32-p3",
     "la": "",
     "it": "Restando fisso l’asse AB, si diminuisca continuamente la larghezza dell’ellisse, e l’area ASD resterà sempre proporzionale al tempo.",
     "en": "The axis AB still remaining the same, let the breadth of the ellipsis be perpetually diminished, and the area ASD will always remain proportional to the time.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "larghezza dell’ellisse che diminuisce, AB fisso"
      ]
     }
    },
    {
     "id": "L1-P32-p4",
     "la": "",
     "it": "Si diminuisca quella larghezza all’infinito: e, quando l’orbita APB coincide ormai con l’asse AB e il fuoco S con l’estremo B dell’asse, il corpo scenderà lungo la retta AC, e l’area ABD diventerà proporzionale al tempo.",
     "en": "Suppose that breadth to be diminished in infinitum; and the orbit APB in that case coinciding with the axis AB, and the focus S with the extreme point of the axis B, the body will descend in the right line AC, and the area ABD will become proportional to the time.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "retta AC"
      ],
      "evidenzia": [
       "orbita → asse AB; S → B; area ABD ∝ tempo"
      ]
     }
    },
    {
     "id": "L1-P32-p5",
     "la": "",
     "it": "Sarà dato dunque lo spazio AC che il corpo, cadendo perpendicolarmente dal luogo A, descrive in un tempo dato, purché si prenda l’area ABD proporzionale al tempo e dal punto D si abbassi sulla retta AB la perpendicolare DC. C.V.T.",
     "en": "Wherefore the space AC will be given which the body describes in a given time by its perpendicular fall from the place A, if the area ABD is taken proportional to the time, and from the point D the right line DC is let fall perpendicularly on the right line AB. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "perpendicolare DC"
      ],
      "evidenzia": [
       "spazio AC dal tempo"
      ]
     },
     "nota": "«capatur»: refuso probabile per «capiatur»."
    },
    {
     "id": "L1-P32-p6",
     "la": "",
     "it": "Caso 2. Se la figura RPB è un’iperbole, sullo stesso diametro principale AB si descriva l’iperbole rettangola BED; e poiché le aree CSP, CBfP, SPfB stanno alle aree CSD, CBED, SDEB, ciascuna alla corrispondente, nel rapporto dato delle altezze CP, CD, e l’area SPfB è proporzionale al tempo in cui il corpo P si muoverà lungo l’arco PfB, anche l’area SDEB sarà proporzionale allo stesso tempo.",
     "en": "CASE 2. If the figure RPB is an hyperbola, on the same principal diameter AB describe the rectangular hyperbola BED; and because the areas CSP, CBfP, SPfB, are severally to the several areas CSD, CBED, SDEB, in the given ratio of the heights CP, CD, and the area SPfB is proportional to the time in which the body P will move through the arc PfB, the area SDEB will be also proportional to that time.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "iperbole RPB",
       "iperbole rettangola BED",
       "f"
      ],
      "evidenzia": [
       "aree in rapporto CP : CD"
      ]
     }
    },
    {
     "id": "L1-P32-p7",
     "la": "",
     "it": "Si diminuisca all’infinito il lato retto dell’iperbole RPB, restando fisso il lato trasverso: l’arco PB verrà a coincidere con la retta CB, il fuoco S con il vertice B e la retta SD con la retta BD.",
     "en": "Let the latus rectum of the hyperbola RPB be diminished in infinitum, the latus transversum remaining the same; and the arc PB will come to coincide with the right line CB, and the focus S, with the vertex B, and the right line SD with the right line BD.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "arco PB → retta CB; S → B; SD → BD"
      ]
     }
    },
    {
     "id": "L1-P32-p8",
     "la": "",
     "it": "Di conseguenza l’area BDEB sarà proporzionale al tempo in cui il corpo C, con discesa rettilinea, descrive la linea CB. C.V.T.",
     "en": "And therefore the area BDEB will be proportional to the time in which the body C, by its perpendicular descent, describes the line CB. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area BDEB"
      ],
      "evidenzia": [
       "area BDEB ∝ tempo di discesa CB"
      ]
     }
    },
    {
     "id": "L1-P32-p9",
     "la": "",
     "it": "Caso 3. E con un argomento simile, se la figura RPB è una parabola, e con lo stesso vertice principale B si descrive un’altra parabola BED, che resti sempre data mentre la prima parabola, sul cui perimetro si muove il corpo P, diminuito e ridotto a nulla il suo lato retto, viene a coincidere con la linea CB, il segmento parabolico BDEB diventerà proporzionale al tempo in cui quel corpo P, o C, scenderà al centro S, o B. C.V.T.",
     "en": "CASE 3. And by the like argument, if the figure RPB is a parabola, and to the same principal vertex B another parabola BED is described, that may always remain given while the former parabola in whose perimeter the body P moves, by having its latus rectum diminished and reduced to nothing, comes to coincide with the line CB, the parabolic segment BDEB will be proportional to the time in which that body P or C will descend to the centre S or B. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "parabola RPB",
       "parabola BED",
       "segmento BDEB"
      ],
      "evidenzia": [
       "segmento BDEB ∝ tempo"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P33",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XXXIII — la velocità nella caduta",
   "copertura": [
    "S7.05",
    "S7.06"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 161–162"
   },
   "enunciato": {
    "la": "",
    "it": "Poste le cose ora trovate, dico che la velocità del corpo che cade, in un luogo qualsiasi C, sta alla velocità di un corpo che descrive un cerchio con centro B e raggio BC in rapporto subduplicato di quello che AC, distanza del corpo dal vertice più lontano A del cerchio o dell’iperbole rettangola, ha con il semidiametro principale della figura, ½AB.",
    "en": "The things above found being supposed, I say, that the velocity of a falling body in any place C is to the velocity of a body, describing a circle about the centre B at the distance BC, in the subduplicate ratio of AC, the distance of the body from the remoter vertex A of the circle or rectangular hyperbola, to [SVG 128], the principal semi-diameter of the figure."
   },
   "figura_base": {
    "punti": [
     "A",
     "B",
     "O",
     "C",
     "P",
     "S",
     "T",
     "Y",
     "Q"
    ],
    "vincoli": [
     "AB diametro comune delle figure RPB e DEB; O punto medio",
     "PT tangente a RPB in P, T su AB",
     "SY perpendicolare a PT",
     "BQ perpendicolare ad AB, Q su PT",
     "L lato retto di RPB; ACB = rettangolo AC × CB"
    ]
   },
   "passi": [
    {
     "id": "L1-P33-p1",
     "la": "",
     "it": "Si divida a metà in O la retta AB, diametro comune delle due figure RPB, DEB; si conduca la retta PT, che tocchi la figura RPB in P e tagli anche quel diametro comune AB (prolungato, se occorre) in T; siano SY perpendicolare a questa retta e BQ perpendicolare a questo diametro, e si ponga L il lato retto della figura RPB.",
     "en": "Let AB, the common diameter of both figures RPB, DEB, be bisected in O; and draw the right line PT that may touch the figure RPB in P, and likewise cut that common diameter AB (produced, if need be) in T; and let SY be perpendicular to this line, and BQ to this diameter, and suppose the latus rectum of the figure RPB to be L.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "O",
       "tangente PT",
       "T",
       "SY",
       "BQ"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P33-p2",
     "la": "",
     "it": "Per il Cor. 9 della Prop. XVI è noto che la velocità di un corpo che si muove sulla linea RPB attorno al centro S, in un luogo qualsiasi P, sta alla velocità di un corpo che descrive un cerchio attorno allo stesso centro alla distanza SP in rapporto subduplicato del rettangolo ½L × SP al quadrato di SY.",
     "en": "From Cor. 9, Prop. XVI, it is manifest that the velocity of a body, moving in the line RPB about the centre S, in any place P, is to the velocity of a body describing a circle about the same centre, at the distance SP, in the subduplicate ratio of the rectangle [SVG 129] to SY2.",
     "dipende_da": [
      "Prop. XVI, Cor. 9"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "v(P) : v circolare(SP) = √(½L × SP) : SY"
      ]
     }
    },
    {
     "id": "L1-P33-p3",
     "la": "",
     "it": "Ma dalle coniche ACB sta a CP² come 2AO sta a L, e perciò 2CP² × AO/ACB è uguale a L.",
     "en": "For by the properties of the conic sections ACB is to CP2 as 2AO to L, and therefore [SVG 130] is equal to L.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "L = 2CP² × AO/ACB"
      ]
     },
     "nota": "Frazione appiattita: «2CPq×AOACB» = 2CP² × AO/ACB."
    },
    {
     "id": "L1-P33-p4",
     "la": "",
     "it": "Dunque quelle velocità stanno fra loro in rapporto subduplicato di CP² × AO × SP/ACB a SY².",
     "en": "Therefore those velocities are to each other in the subduplicate ratio of [SVG 131] to SY2.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P33-p5",
     "la": "",
     "it": "Inoltre, dalle coniche, CO sta a BO come BO sta a TO, e, per composizione o per separazione, come CB sta a BT.",
     "en": "Moreover, by the properties of the conic sections, CO is to BO as BO to TO and (by composition or division) as CB to BT.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "CO : BO = BO : TO"
      ]
     }
    },
    {
     "id": "L1-P33-p6",
     "la": "",
     "it": "Di qui, per separazione o per composizione, BO − o + CO sta a BO come CT sta a BT, cioè AC sta ad AO come CP sta a BQ; e quindi CP² × AO × SP/ACB è uguale a BQ² × AC × SP/(AO × BC).",
     "en": "Whence (by division or composition) BO - or + CO will be to BO as CT to BT, that is, AC will be to AO as CP to BQ; and therefore [SVG 131] is equal to [SVG 132].",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "AC : AO = CP : BQ"
      ]
     },
     "nota": "«BQq×AC×SPAO×BC» = BQ² × AC × SP/(AO × BC)."
    },
    {
     "id": "L1-P33-p7",
     "la": "",
     "it": "Si diminuisca ora all’infinito la larghezza CP della figura RPB, in modo che il punto P coincida con il punto C, il punto S con il punto B, la linea SP con la linea BC e la linea SY con la linea BQ: la velocità del corpo che ormai scende in linea retta lungo la linea CB starà alla velocità di un corpo che descrive un cerchio con centro B e raggio BC in rapporto subduplicato di BQ² × AC × SP/(AO × BC) a SY², cioè (trascurati i rapporti di uguaglianza di SP a BC e di BQ² a SY²) in rapporto subduplicato di AC ad AO, ossia a ½AB. C.V.D.",
     "en": "Now suppose CP, the breadth of the figure RPB, to be diminished in infinitum, so as the point P may come to coincide with the point C, and the point S with the point B, and the line SP with the line BC, and the line SY with the line BQ; and the velocity of the body now descending perpendicularly in the line CB will be to the velocity of a body describing a circle about the centre B, at the distance BC, in the subduplicate ratio of [SVG 133] to SY2, that is (neglecting the ratios of equality of SP to BC, and BQ2 to SY2), in the subduplicate ratio of AC to AO, or [SVG 128]. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "C",
       "B"
      ],
      "evidenzia": [
       "P → C, S → B, SY → BQ: v(C) : v circolare(BC) = √(AC : AO)"
      ]
     },
     "nota": "«12AB» = ½AB (Motte SVG 128). Verifica numerica nella nota N8."
    }
   ]
  },
  {
   "id": "L1-P34",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XXXIV — il caso parabolico",
   "copertura": [
    "S7.09",
    "S7.10"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 162"
   },
   "enunciato": {
    "la": "",
    "it": "Se la figura BED è una parabola, dico che la velocità del corpo che cade, in un luogo qualsiasi C, è uguale alla velocità con cui un corpo può descrivere uniformemente un cerchio con centro B alla metà della sua distanza BC.",
    "en": "If the figure BED is a parabola, I say, that the velocity of a falling body in any place C is equal to the velocity by which a body may uniformly describe a circle about the centre B at half the interval BC."
   },
   "figura_base": {
    "punti": [
     "B",
     "C",
     "D",
     "E",
     "P",
     "R",
     "S",
     "f"
    ],
    "vincoli": [
     "parabola RPB di fuoco S",
     "parabola BED",
     "larghezza CP → 0: arco PfB → retta CB, S → B"
    ]
   },
   "passi": [
    {
     "id": "L1-P34-p1",
     "la": "",
     "it": "Infatti la velocità di un corpo che descrive la parabola RPB attorno al centro S, in un luogo qualsiasi P (per il Cor. 7 della Prop. XVI), è uguale alla velocità di un corpo che descrive uniformemente un cerchio attorno allo stesso centro S alla metà della distanza SP.",
     "en": "For (by Cor. 7, Prop. XVI) the velocity of a body describing a parabola RPB about the centre S, in any place P, is equal to the velocity of a body uniformly describing a circle about the same centre S at half the interval SP.",
     "dipende_da": [
      "Prop. XVI, Cor. 7"
     ],
     "figura": {
      "mostra": [
       "parabola RPB",
       "S",
       "P",
       "cerchio di raggio ½SP"
      ],
      "evidenzia": [
       "v(P) = v circolare(½SP)"
      ]
     },
     "nota": "La segmentazione automatica spezzava la frase dopo «per corol.»; qui è ricomposta."
    },
    {
     "id": "L1-P34-p2",
     "la": "",
     "it": "Si diminuisca all’infinito la larghezza CP della parabola, in modo che l’arco parabolico PfB coincida con la retta CB, il centro S con il vertice B e la distanza SP con la distanza BC, e la proposizione risulterà evidente. C.V.D.",
     "en": "Let the breadth CP of the parabola be diminished in infinitum, so as the parabolic arc PfB may come to coincide with the right line CB, the centre S with the vertex B, and the interval SP with the interval BC, and the proposition will be manifest. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "retta CB"
      ],
      "evidenzia": [
       "PfB → CB; SP → BC"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P35",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XXXV — l’area della figura DES e il moto circolare uniforme",
   "copertura": [
    "S7.11",
    "S7.12",
    "S7.13",
    "S7.14"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 162–164"
   },
   "enunciato": {
    "la": "",
    "it": "Poste le stesse cose, dico che l’area della figura DES, descritta dal raggio indefinito SD, è uguale all’area che un corpo, ruotando uniformemente attorno al centro S con raggio uguale alla metà del lato retto della figura DES, può descrivere nello stesso tempo.",
    "en": "The same things supposed, I say, that the area of the figure DES, described by the indefinite radius SD, is equal to the area which a body with a radius equal to half the latus rectum of the figure DES, by uniformly revolving about the centre S, may describe in the same time."
   },
   "figura_base": {
    "punti": [
     "A",
     "S",
     "O",
     "C",
     "c",
     "D",
     "d",
     "T",
     "Y",
     "K",
     "k"
    ],
    "vincoli": [
     "figura DES: cerchio o iperbole (Caso 1) o parabola (Caso 2) con asse AS",
     "CD, cd perpendicolari all’asse",
     "Dd incontra l’asse in T; SY perpendicolare a Dd",
     "cerchio OKk di centro S e raggio SK = metà del lato retto",
     "Cc percorso dal corpo che cade nello stesso tempo dell’arco Kk"
    ]
   },
   "passi": [
    {
     "id": "L1-P35-p1",
     "la": "",
     "it": "Immagina infatti che il corpo C, cadendo, descriva in una particella di tempo piccolissima la piccola linea Cc, e che intanto un altro corpo K, ruotando uniformemente nel cerchio OKk attorno al centro S, descriva l’arco Kk.",
     "en": "For suppose a body C in the smallest moment of time describes in falling the infinitely little line Cc, while another body K, uniformly revolving about the centre S in the circle OKk, describes the arc Kk.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "C",
       "c",
       "cerchio OKk",
       "K",
       "k"
      ],
      "evidenzia": [
       "Cc e Kk nello stesso tempo"
      ]
     }
    },
    {
     "id": "L1-P35-p2",
     "la": "",
     "it": "Si innalzino le perpendicolari CD, cd, che incontrino la figura DES in D, d.",
     "en": "Erect the perpendiculars CD, cd, meeting the figure DES in D, d.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "CD",
       "cd",
       "D",
       "d"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P35-p3",
     "la": "",
     "it": "Si congiungano SD, Sd, SK, Sk, si conduca Dd, che incontri l’asse AS in T, e su di essa si abbassi la perpendicolare SY.",
     "en": "Join SD, Sd, SK, Sk, and draw Dd meeting the axis AS in T, and thereon let fall the perpendicular SY.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "SD",
       "Sd",
       "SK",
       "Sk",
       "Dd",
       "T",
       "SY"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P35-p4",
     "la": "",
     "it": "Caso 1. Ora, se la figura DES è un cerchio o un’iperbole, si divida a metà in O il suo diametro trasverso AS, e SO sarà la metà del lato retto.",
     "en": "CASE 1. If the figure DES is a circle, or a rectangular hyperbola, bisect its transverse diameter AS in O, and SO will be half the latus rectum.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "O"
      ],
      "evidenzia": [
       "SO = semilato retto"
      ]
     }
    },
    {
     "id": "L1-P35-p5",
     "la": "",
     "it": "E poiché TC sta a TD come Cc sta a Dd, e TD sta a TS come CD sta a SY, per uguaglianza TC sta a TS come CD × Cc sta a SY × Dd.",
     "en": "And because TC is to TD as Cc to Dd, and TD to TS as CD to SY; ex æquo TC will be to TS as CD × Cc to SY × Dd.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "TC : TS = CD × Cc : SY × Dd"
      ]
     }
    },
    {
     "id": "L1-P35-p6",
     "la": "",
     "it": "Ma (per il Cor. 1 della Prop. XXXIII) TC sta a TS come AC sta ad AO, s’intende se, nel congiungersi dei punti D, d, si prendono i rapporti ultimi delle linee.",
     "en": "But (by Cor. 1, Prop. XXXIII) TC is to TS as AC to AO; to wit, if in the coalescence of the points D, d, the ultimate ratios of the lines are taken.",
     "dipende_da": [
      "Prop. XXXIII, Cor. 1"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "TC : TS = AC : AO"
      ]
     }
    },
    {
     "id": "L1-P35-p7",
     "la": "",
     "it": "Dunque AC sta ad AO, ossia a SK, come CD × Cc sta a SY × Dd.",
     "en": "Wherefore AC is to AO or SK as CD × Cc to SY × Dd.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "AC : SK = CD × Cc : SY × Dd"
      ]
     }
    },
    {
     "id": "L1-P35-p8",
     "la": "",
     "it": "Inoltre la velocità del corpo che scende, in C, sta alla velocità di un corpo che descrive un cerchio attorno al centro S alla distanza SC in rapporto subduplicato di AC ad AO o SK (per la Prop. XXXIII). E questa velocità sta alla velocità del corpo che descrive il cerchio OKk in rapporto subduplicato di SK a SC (per il Cor. 6 della Prop. IV); e, per uguaglianza, la prima velocità sta all’ultima, cioè la piccola linea Cc sta all’arco Kk, in rapporto subduplicato di AC a SC, cioè nel rapporto di AC a CD.",
     "en": "Farther, the velocity of the descending body in C is to the velocity of a body describing a circle about the centre S, at the interval SC, in the subduplicate ratio of AC to AO or SK (by Prop. XXXIII); and this velocity is to the velocity of a body describing the circle OKk in the subduplicate ratio of SK to SC (by Cor. 6, Prop IV); and, ex æquo, the first velocity to the last, that is, the little line Cc to the arc Kk, in the subduplicate ratio of AC to SC, that is, in the ratio of AC to CD.",
     "dipende_da": [
      "Prop. XXXIII",
      "Prop. IV, Cor. 6"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "Cc : Kk = AC : CD"
      ]
     }
    },
    {
     "id": "L1-P35-p9",
     "la": "",
     "it": "Perciò CD × Cc è uguale ad AC × Kk, e di conseguenza AC sta a SK come AC × Kk sta a SY × Dd; quindi SK × Kk è uguale a SY × Dd, e ½SK × Kk è uguale a ½SY × Dd, cioè l’area KSk è uguale all’area SDd.",
     "en": "Wherefore CD × Cc is equal to AC × Kk, and consequently AC to SK as AC × Kk to SY × Dd, and thence SK × Kk equal to SY × Dd, and [SVG 134] equal to [SVG 135], that is, the area KSk equal to the area SDd.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area KSk",
       "area SDd"
      ],
      "evidenzia": [
       "area KSk = area SDd"
      ]
     },
     "nota": "Motte, SVG 134, stampa «½SY × Kk» per ½SK × Kk (§ A.8)."
    },
    {
     "id": "L1-P35-p10",
     "la": "",
     "it": "In ogni particella di tempo si generano dunque particelle KSk e SDd delle due aree che, se la loro grandezza diminuisce e il loro numero aumenta all’infinito, ottengono il rapporto di uguaglianza; e perciò (per il corollario del Lemma IV) le aree totali generate insieme sono sempre uguali. C.V.D.",
     "en": "Therefore in every moment of time two equal particles, KSk and SDd, of areas are generated, which, if their magnitude is diminished, and their number increased in infinitum, obtain the ratio of equality, and consequently (by Cor. Lem. IV), the whole areas together generated are always equal. Q.E.D.",
     "dipende_da": [
      "Lemma IV, Cor."
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "somma delle particelle: aree totali uguali"
      ]
     }
    },
    {
     "id": "L1-P35-p11",
     "la": "",
     "it": "Caso 2. Se poi la figura DES è una parabola, si troverà, come sopra, che CD × Cc sta a SY × Dd come TC sta a TS, cioè come 2 sta a 1, e quindi che ¼CD × Cc è uguale a ½SY × Dd.",
     "en": "CASE 2. But if the figure DES is a parabola, we shall find, as above, CD × Cc to SY × Dd as TC to TS, that is, as 2 to 1; and that therefore [SVG 136], is equal to [SVG 135].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "parabola DES"
      ],
      "evidenzia": [
       "TC : TS = 2 : 1"
      ]
     }
    },
    {
     "id": "L1-P35-p12",
     "la": "",
     "it": "Ma la velocità del corpo che cade, in C, è uguale alla velocità con cui si potrebbe descrivere uniformemente un cerchio alla distanza ½SC (per la Prop. XXXIV). E questa velocità sta alla velocità con cui si potrebbe descrivere un cerchio di raggio SK, cioè la piccola linea Cc sta all’arco Kk (per il Cor. 6 della Prop. IV), in rapporto subduplicato di SK a ½SC, cioè nel rapporto di SK a ½CD.",
     "en": "But the velocity of the falling body in C is equal to the velocity with which a circle may be uniformly described at the interval [SVG 137] (by Prop. XXXIV). And this velocity to the velocity with which a circle may be described with the radius SK, that is, the little line Cc to the arc Kk, is (by Cor. 6, Prop. IV) in the subduplicate ratio of SK to [SVG 137]; that is, in the ratio of SK to [SVG 138].",
     "dipende_da": [
      "Prop. XXXIV",
      "Prop. IV, Cor. 6"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "Cc : Kk = SK : ½CD"
      ]
     },
     "nota": "«12Sc»: refuso probabile per ½SC (Motte SVG 137)."
    },
    {
     "id": "L1-P35-p13",
     "la": "",
     "it": "Perciò ½SK × Kk è uguale a ¼CD × Cc, e quindi uguale a ½SY × Dd; cioè l’area KSk è uguale all’area SDd, come sopra. C.V.D.",
     "en": "Wherefore [SVG 139] is equal to [SVG 136], and therefore equal to [SVG 135]; that is, the area KSk is equal to the area SDd, as above. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "area KSk",
       "area SDd"
      ],
      "evidenzia": [
       "area KSk = area SDd"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P36",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXXVI — i tempi della caduta da un luogo dato",
   "copertura": [
    "S7.15",
    "S7.16"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 164"
   },
   "enunciato": {
    "la": "",
    "it": "Determinare i tempi di discesa di un corpo che cade da un luogo dato A.",
    "en": "To determine the times of the descent of a body falling from a given place A."
   },
   "figura_base": {
    "punti": [
     "A",
     "S",
     "C",
     "D",
     "O",
     "K",
     "H"
    ],
    "vincoli": [
     "semicerchio ADS sul diametro AS",
     "semicerchio OKH di centro S e raggio ½AS",
     "CD ordinata in C",
     "settore OSK = area ASD"
    ]
   },
   "passi": [
    {
     "id": "L1-P36-p1",
     "la": "",
     "it": "Sul diametro AS, distanza del corpo dal centro all’inizio, si descriva il semicerchio ADS, e anche il semicerchio OKH, uguale a questo, attorno al centro S.",
     "en": "Upon the diameter AS, the distance of the body from the centre at the beginning, describe the semi-circle ADS, as likewise the semi-circle OKH equal thereto, about the centre S.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A",
       "S",
       "semicerchio ADS",
       "semicerchio OKH"
      ],
      "evidenzia": [
       "raggio di OKH = ½AS"
      ]
     }
    },
    {
     "id": "L1-P36-p2",
     "la": "",
     "it": "Da un luogo qualsiasi C del corpo si innalzi l’ordinata CD.",
     "en": "From any place C of the body erect the ordinate CD.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "C",
       "ordinata CD",
       "D"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P36-p3",
     "la": "",
     "it": "Si congiunga SD, e si costruisca il settore OSK uguale all’area ASD.",
     "en": "Join SD, and make the sector OSK equal to the area ASD.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "SD",
       "settore OSK"
      ],
      "evidenzia": [
       "settore OSK = area ASD"
      ]
     }
    },
    {
     "id": "L1-P36-p4",
     "la": "",
     "it": "È evidente, per la Prop. XXXV, che il corpo, cadendo, descriverà lo spazio AC nello stesso tempo in cui un altro corpo, ruotando uniformemente attorno al centro S, può descrivere l’arco OK. C.V.F.",
     "en": "It is evident (by Prop. XXXV) that the body in falling will describe the space AC in the same time in which another body, uniformly revolving about the centre S, may describe the arc OK. Q.E.F.",
     "dipende_da": [
      "Prop. XXXV"
     ],
     "figura": {
      "mostra": [
       "arco OK"
      ],
      "evidenzia": [
       "tempo AC = tempo dell’arco OK"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P37",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXXVII — i tempi di un corpo lanciato in alto o in basso",
   "copertura": [
    "S7.17",
    "S7.18"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 164–165"
   },
   "enunciato": {
    "la": "",
    "it": "Definire i tempi di salita o di discesa di un corpo lanciato da un luogo dato verso l’alto o verso il basso.",
    "en": "To define the times of the ascent or descent of a body projected upwards or downwards from a given place."
   },
   "figura_base": {
    "punti": [
     "G",
     "S",
     "A",
     "C",
     "I",
     "D",
     "E",
     "H",
     "K",
     "k"
    ],
    "vincoli": [
     "lancio da G lungo GS",
     "GA : ½AS = (v : v circolare in G)²",
     "cerchio, parabola (A all’infinito) o iperbole rettangola sul diametro SA",
     "cerchio HKk di centro S e raggio = semilato retto",
     "GI, CD perpendicolari a SA",
     "settori HSK, HSk = segmenti SEIS, SEDS"
    ]
   },
   "passi": [
    {
     "id": "L1-P37-p1",
     "la": "",
     "it": "Il corpo esca dal luogo dato G lungo la linea GS con una velocità qualsiasi.",
     "en": "Suppose the body to go off from the given place G, in the direction of the line GS, with any velocity.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "G",
       "S",
       "retta GS"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P37-p2",
     "la": "",
     "it": "Si prenda GA a ½AS nel rapporto duplicato di questa velocità alla velocità uniforme in un cerchio con cui il corpo potrebbe ruotare attorno al centro S alla distanza data SG.",
     "en": "In the duplicate ratio of this velocity to the uniform velocity in a circle, with which the body may revolve about the centre S at the given interval SG, take GA to [SVG 140].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A"
      ],
      "evidenzia": [
       "GA : ½AS = (v/v circolare)²"
      ]
     },
     "nota": "«12AS» = ½AS."
    },
    {
     "id": "L1-P37-p3",
     "la": "",
     "it": "Se quel rapporto è quello del numero due all’unità, il punto A è infinitamente distante; e in tal caso si deve descrivere una parabola con vertice S, asse SC e lato retto qualsiasi.",
     "en": "If that ratio is the same as of the number 2 to 1, the point A is infinitely remote; in which case a parabola is to be described with any latus rectum to the vertex S, and axis SG",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "parabola di vertice S"
      ],
      "evidenzia": [
       "rapporto 2 : 1 → A all’infinito"
      ]
     },
     "nota": "Motte: «axis SG» per «axe SC» (stessa retta)."
    },
    {
     "id": "L1-P37-p4",
     "la": "",
     "it": "Ciò risulta dalla Prop. XXXIV.",
     "en": "as appears by Prop. XXXIV.",
     "dipende_da": [
      "Prop. XXXIV"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P37-p5",
     "la": "",
     "it": "Se invece quel rapporto è minore o maggiore di 2 a 1, nel primo caso si deve descrivere sul diametro SA un cerchio, nel secondo un’iperbole rettangola.",
     "en": "But if that ratio is less or greater than the ratio of 2 to 1, in the former case a circle, in the latter a rectangular hyperbola, is to be described on the diameter SA",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio o iperbole rettangola su SA"
      ],
      "evidenzia": [
       "< 2 : 1 cerchio; > 2 : 1 iperbole"
      ]
     }
    },
    {
     "id": "L1-P37-p6",
     "la": "",
     "it": "Ciò risulta dalla Prop. XXXIII.",
     "en": "as appears by Prop. XXXIII.",
     "dipende_da": [
      "Prop. XXXIII"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P37-p7",
     "la": "",
     "it": "Poi con centro S e raggio uguale alla metà del lato retto si descriva il cerchio HKk, e nel luogo G del corpo che scende o sale e in un altro luogo qualsiasi C si innalzino le perpendicolari GI, CD, che incontrino la sezione conica o il cerchio in I e D.",
     "en": "Then about the centre S, with an interval equal to half the latus rectum, describe the circle HkK; and at the place G of the ascending or descending body, and at any other place C, erect the perpendiculars GI, CD, meeting the conic section or circle in I and D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio HKk",
       "GI",
       "CD",
       "I",
       "D"
      ],
      "evidenzia": []
     },
     "nota": "Motte: «HkK» per «HKk»."
    },
    {
     "id": "L1-P37-p8",
     "la": "",
     "it": "Poi, congiunte SI, SD, si facciano i settori HSK, HSk uguali ai segmenti SEIS, SEDS: per la Prop. XXXV il corpo G descriverà lo spazio GC nello stesso tempo in cui il corpo K può descrivere l’arco Kk. C.V.F.",
     "en": "Then joining SI, SD, let the sectors HSK, HSk be made equal to the segments SEIS, SEDS, and (by Prop. XXXV) the body G will describe the space GC in the same time in which the body K may describe the arc Kk. Q.E.F.",
     "dipende_da": [
      "Prop. XXXV"
     ],
     "figura": {
      "mostra": [
       "settori HSK, HSk",
       "segmenti SEIS, SEDS"
      ],
      "evidenzia": [
       "tempo GC = tempo dell’arco Kk"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P38",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XXXVIII — forza proporzionale alla distanza",
   "copertura": [
    "S7.19",
    "S7.20",
    "S7.21"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, p. 165"
   },
   "enunciato": {
    "la": "",
    "it": "Posto che la forza centripeta sia proporzionale all’altezza, ossia alla distanza dei luoghi dal centro, dico che i tempi dei corpi che cadono, le velocità e gli spazi descritti sono proporzionali rispettivamente agli archi, ai seni retti e ai seni versi degli archi.",
    "en": "Supposing that the centripetal force is proportional to the altitude or distance of places from the centre, I say, that the times and velocities of falling bodies, and the spaces which they describe, are respectively proportional to the arcs, and the right and versed sines of the arcs."
   },
   "figura_base": {
    "punti": [
     "A",
     "S",
     "E",
     "D",
     "C"
    ],
    "vincoli": [
     "quadrante AE di centro S e raggio AS",
     "CD seno retto dell’arco AD, C su AS",
     "tempo ∝ arco AD; velocità ∝ CD; spazio AC = seno verso"
    ]
   },
   "passi": [
    {
     "id": "L1-P38-p1",
     "la": "",
     "it": "Il corpo cada da un luogo qualsiasi A lungo la retta AS; con centro delle forze S e raggio AS si descriva il quadrante di cerchio AE, e sia CD il seno retto di un arco qualsiasi AD: il corpo A, nel tempo AD, cadendo descriverà lo spazio AC, e nel luogo C acquisterà la velocità CD.",
     "en": "Suppose the body to fall from any place A in the right line AS; and about the centre of force S, with the interval AS, describe the quadrant of a circle AE; and let CD be the right sine of any arc AD; and the body A will in the time AD in falling describe the space AC, and in the place C will acquire the velocity CD.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A",
       "S",
       "quadrante AE",
       "arco AD",
       "D",
       "CD",
       "C"
      ],
      "evidenzia": [
       "tempo = arco AD; velocità = CD; spazio = AC"
      ]
     }
    },
    {
     "id": "L1-P38-p2",
     "la": "",
     "it": "Si dimostra dalla Prop. X nello stesso modo in cui la Prop. XXXII è stata dimostrata dalla Prop. XI.",
     "en": "This is demonstrated the same way from Prop. X, as Prop. XXXII was demonstrated from Prop. XI.",
     "dipende_da": [
      "Prop. X",
      "Prop. XXXII",
      "Prop. XI"
     ],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "come la Prop. XXXII dalla Prop. XI: ellisse di centro S che degenera nel segmento AS"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P39",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XXXIX — forza qualsiasi: velocità e tempi per quadrature",
   "copertura": [
    "S7.24",
    "S7.25",
    "S7.26",
    "S7.27",
    "S7.28"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 165–166"
   },
   "enunciato": {
    "la": "",
    "it": "Posta una forza centripeta di qualsiasi genere, e concesse le quadrature delle figure curvilinee, si richiede, per un corpo che sale o scende in linea retta, sia la velocità nei singoli luoghi, sia il tempo in cui il corpo giungerà a un luogo qualsiasi; e viceversa.",
    "en": "Supposing a centripetal force of any kind, and granting the quadratures of curvilinear figures; it is required to find the velocity of a body, ascending or descending in a right line, in the several places through which it passes; as also the time in which it will arrive at any place; and vice versa."
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
     "L",
     "M",
     "T",
     "V"
    ],
    "vincoli": [
     "retta ADEC verso il centro C",
     "EG perpendicolare, proporzionale alla forza in E; curva BFG",
     "EM inversamente proporzionale a √(area ABGE); curva VLM con asintoto AB",
     "DE piccolissima; DLF posizione di EMG quando il corpo è in D"
    ]
   },
   "passi": [
    {
     "id": "L1-P39-p1",
     "la": "",
     "it": "Da un luogo qualsiasi A della retta ADEC cada il corpo E, e dal suo luogo E si innalzi sempre la perpendicolare EG, proporzionale alla forza centripeta che in quel luogo tende al centro C; e sia BFG la linea curva che il punto G descrive continuamente.",
     "en": "Suppose the body E to fall from any place A in the right line ADEC; and from its place E imagine a perpendicular EG always erected proportional to the centripetal force in that place tending to the centre C; and let BFG be a curve line, the locus of the point G.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "retta ADEC",
       "A",
       "E",
       "C",
       "perpendicolare EG",
       "curva BFG"
      ],
      "evidenzia": [
       "EG ∝ forza in E"
      ]
     }
    },
    {
     "id": "L1-P39-p2",
     "la": "",
     "it": "All’inizio stesso del moto EG coincida con la perpendicolare AB: la velocità del corpo in un luogo qualsiasi E sarà come la retta il cui quadrato è uguale all’area curvilinea ABGE. C.V.T.",
     "en": "And in the beginning of the motion suppose EG to coincide with the perpendicular AB; and the velocity of the body in any place E will be as a right line whose square is equal to the curvilinear area ABGE. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "AB",
       "area ABGE"
      ],
      "evidenzia": [
       "velocità in E ∝ √(area ABGE)"
      ]
     },
     "nota": "«curvilineæm»: refuso probabile per «curvilineam»."
    },
    {
     "id": "L1-P39-p3",
     "la": "",
     "it": "In EG si prenda EM inversamente proporzionale alla retta il cui quadrato è uguale all’area ABGE, e sia VLM la linea curva che il punto M descrive continuamente e di cui è asintoto la retta AB prolungata: il tempo in cui il corpo, cadendo, descrive la linea AE sarà come l’area curvilinea ABTVME. C.V.T.",
     "en": "In EG take EM reciprocally proportional to a right line whose square is equal to the area ABGE, and let VLM be a curve line wherein the point M is always placed, and to which the right line AB produced is an asymptote; and the time in which the body in falling describes the line AE, will be as the curvilinear area ABTVME. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "EM",
       "curva VLM",
       "area ABTVME"
      ],
      "evidenzia": [
       "tempo AE ∝ area ABTVME"
      ]
     }
    },
    {
     "id": "L1-P39-p4",
     "la": "",
     "it": "Infatti nella retta AE si prenda una piccolissima linea DE di lunghezza data, e sia DLF la posizione della linea EMG quando il corpo si trovava in D; e se la forza centripeta è tale che la retta il cui quadrato è uguale all’area ABGE sia come la velocità del corpo che scende, l’area stessa sarà in rapporto duplicato della velocità; cioè, se per le velocità in D ed E si scrivono V e V + I, l’area ABFD sarà come VV e l’area ABGE come VV + 2VI + II, e per separazione l’area DFGE come 2VI + II, e perciò DFGE/DE come (2VI + II)/DE; cioè, se si prendono i rapporti primi delle quantità nascenti, la lunghezza DF sarà come la quantità 2VI/DE, e quindi anche come la sua metà, I × V/DE.",
     "en": "For in the right line AE let there be taken the very small line DE of a given length, and let DLF be the place of the line EMG, when the body was in D; and if the centripetal force be such, that a right line, whose square is equal to the area ABGE, is as the velocity of the descending body, the area itself will be as the square of that velocity; that is, if for the velocities in D and E we write V and V + I, the area ABFD will be as VV, and the area ABGE as VV + 2VI + II; and by division, the area DFGE as 2VI + II, and therefore [SVG 141] will be as [SVG 142]; that is, if we take the first ratios of those quantities when just nascent, the length DF is as the quantity [SVG 143], and therefore also as half that quantity [SVG 144].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "D",
       "DE",
       "DF",
       "area DFGE"
      ],
      "evidenzia": [
       "area ABFD ∝ VV; DF ∝ I × V/DE"
      ]
     },
     "nota": "Frazioni appiattite: «DFGEDE» = DFGE/DE; «2VI+IIDE» = (2VI + II)/DE; «2VIDE» = 2VI/DE; «I×VDE» = I × V/DE."
    },
    {
     "id": "L1-P39-p5",
     "la": "",
     "it": "Ma il tempo in cui il corpo, cadendo, descrive la piccola linea DE è come quella linea direttamente e la velocità V inversamente; e la forza è come l’incremento I della velocità direttamente e il tempo inversamente; e perciò, se si prendono i rapporti primi delle quantità nascenti, come I × V/DE, cioè come la lunghezza DF.",
     "en": "But the time in which the body in falling describes the very small line DE, is as that line directly and the velocity V inversely; and the force will be as the increment I of the velocity directly and the time inversely; and therefore if we take the first ratios when those quantities are just nascent, as [SVG 144], that is, as the length DF.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "forza ∝ I × V/DE ∝ DF"
      ]
     }
    },
    {
     "id": "L1-P39-p6",
     "la": "",
     "it": "Dunque una forza proporzionale a DF o a EG fa sì che il corpo scenda con una velocità che sia come la retta il cui quadrato è uguale all’area ABGE. C.V.D.",
     "en": "Therefore a force proportional to DF or EG will cause the body to descend with a velocity that is as the right line whose square is equal to the area ABGE. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P39-p7",
     "la": "",
     "it": "Inoltre, poiché il tempo in cui si descrive una piccola linea qualsiasi DE di lunghezza data è come la velocità inversamente, e quindi inversamente come la linea retta il cui quadrato è uguale all’area ABFD; e poiché DL, e quindi l’area nascente DLME, è come la stessa linea retta inversamente; il tempo sarà come l’area DLME, e la somma di tutti i tempi come la somma di tutte le aree, cioè (per il corollario del Lemma IV) il tempo totale in cui si descrive la linea AE sarà come l’area totale ATVME. C.V.D.",
     "en": "Moreover, since the time in which a very small line DE of a given length may be described is as the velocity inversely, and therefore also inversely as a right line whose square is equal to the area ABFD; and since the line DL, and by consequence the nascent area DLME, will be as the same right line inversely, the time will be as the area DLME, and the sum of all the times will be as the sum of all the areas; that is (by Cor. Lem. IV), the whole time in which the line AE is described will be as the whole area ATVME. Q.E.D.",
     "dipende_da": [
      "Lemma IV, Cor."
     ],
     "figura": {
      "mostra": [
       "DL",
       "area DLME",
       "area ATVME"
      ],
      "evidenzia": [
       "tempo DE ∝ area DLME"
      ]
     },
     "nota": "Il latino ha qui «ATVME», prima «ABTVME» (§ A.12)."
    }
   ]
  },
  {
   "id": "L1-P39-Cor1",
   "tipo": "Corollarium",
   "titolo": "Prop. XXXIX, Cor. 1 — confronto con la caduta per forza uniforme",
   "copertura": [
    "S7.29"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 166–167"
   },
   "enunciato": {
    "la": "",
    "it": "Sia P il luogo da cui un corpo deve cadere affinché, sollecitato da una forza centripeta uniforme nota (quale si suppone comunemente la gravità), acquisti nel luogo D una velocità uguale alla velocità che un altro corpo, cadendo per una forza qualsiasi, ha acquistato nello stesso luogo D; nella perpendicolare DF si prenda DR, che stia a DF come quella forza uniforme sta all’altra forza nel luogo D; si completi il rettangolo PDRQ, e gli si tagli uguale l’area ABFD: A sarà il luogo da cui è caduto l’altro corpo.",
    "en": "Let P be the place from whence a body ought to fall, so as that, when urged by any known uniform centripetal force (such as gravity is vulgarly supposed to be), it may acquire in the place D a velocity equal to the velocity which another body, falling by any force whatever, hath acquired in that place D. In the perpendicular DF let there be taken DR, which may be to DF as that uniform force to the other force in the place D. Complete the rectangle PDRQ, and cut off the area ABFD equal to that rectangle. Then A will be the place from whence the other body fell."
   },
   "figura_base": {
    "punti": [
     "P",
     "D",
     "R",
     "Q",
     "A",
     "B",
     "F",
     "E",
     "G",
     "S"
    ],
    "vincoli": [
     "DR : DF = forza uniforme : forza in D",
     "rettangolo PDRQ = area ABFD",
     "rettangolo DRSE"
    ]
   },
   "passi": [
    {
     "id": "L1-P39-Cor1-p1",
     "la": "",
     "it": "Sia P il luogo da cui un corpo deve cadere affinché, sollecitato da una forza centripeta uniforme nota (quale si suppone comunemente la gravità), acquisti nel luogo D una velocità uguale alla velocità che un altro corpo, cadendo per una forza qualsiasi, ha acquistato nello stesso luogo D; nella perpendicolare DF si prenda DR, che stia a DF come quella forza uniforme sta all’altra forza nel luogo D; si completi il rettangolo PDRQ, e gli si tagli uguale l’area ABFD: A sarà il luogo da cui è caduto l’altro corpo.",
     "en": "Let P be the place from whence a body ought to fall, so as that, when urged by any known uniform centripetal force (such as gravity is vulgarly supposed to be), it may acquire in the place D a velocity equal to the velocity which another body, falling by any force whatever, hath acquired in that place D. In the perpendicular DF let there be taken DR, which may be to DF as that uniform force to the other force in the place D. Complete the rectangle PDRQ, and cut off the area ABFD equal to that rectangle. Then A will be the place from whence the other body fell.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "P",
       "DR",
       "rettangolo PDRQ",
       "area ABFD"
      ],
      "evidenzia": [
       "PDRQ = ABFD"
      ]
     }
    },
    {
     "id": "L1-P39-Cor1-p2",
     "la": "",
     "it": "Infatti, completato il rettangolo DRSE, poiché l’area ABFD sta all’area DFGE come VV sta a 2VI, e quindi come ½V sta a I, cioè come la metà della velocità totale sta all’incremento della velocità del corpo che cade per una forza non uniforme; e similmente l’area PQRD sta all’area DRSE come la metà della velocità totale sta all’incremento della velocità del corpo che cade per la forza uniforme; e poiché quegli incrementi (per l’uguaglianza dei tempi nascenti) sono come le forze che li generano, cioè come le ordinate DF, DR, e quindi come le aree nascenti DFGE, DRSE; per uguaglianza le aree totali ABFD, PQRD staranno fra loro come le metà delle velocità totali, e perciò, essendo uguali le velocità, sono uguali.",
     "en": "For completing the rectangle DRSE, since the area ABFD is to the area DFGE as VV to 2VI, and therefore as [SVG 145] to I, that is, as half the whole velocity to the increment of the velocity of the body falling by the unequable force; and in like manner the area PQRD to the area DRSE as half the whole velocity to the increment of the velocity of the body falling by the uniform force; and since those increments (by reason of the equality of the nascent times) are as the generating forces, that is, as the ordinates DF, DR, and consequently as the nascent areas DFGE, DRSE; therefore, ex æquo, the whole areas ABFD, PQRD will be to one another as the halves of the whole velocities; and therefore, because the velocities are equal, they become equal also.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "rettangolo DRSE",
       "area DFGE"
      ],
      "evidenzia": [
       "aree nascenti ∝ incrementi di velocità"
      ]
     },
     "nota": "Parentesi non bilanciate nella trascrizione: «erunt ex æquo)» e «(ob æqualitatem velocitatum,» (§ A.12)."
    }
   ],
   "nota": "Incluso perché ha una dimostrazione propria con costruzione geometrica."
  },
  {
   "id": "L1-P39-Cor3",
   "tipo": "Corollarium",
   "titolo": "Prop. XXXIX, Cor. 3 — il tempo di un corpo lanciato",
   "copertura": [
    "S7.31"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 167–168"
   },
   "enunciato": {
    "la": "",
    "it": "Si conoscerà anche il tempo innalzando l’ordinata em inversamente proporzionale al lato quadrato di PQRD + o − DFge, e prendendo il tempo in cui il corpo ha descritto la linea De al tempo in cui l’altro corpo è caduto da P per una forza uniforme ed è giunto cadendo in D, come l’area curvilinea DLme sta al rettangolo 2PD × DL.",
    "en": "The time is also known by erecting the ordinate em reciprocally proportional to the square root of PQRD + or - DFge, and taking the time in which the body has described the line De to the time in which another body has fallen with an uniform force from P, and in falling arrived at D in the proportion of the curvilinear area DLme to the rectangle 2PD × DL."
   },
   "figura_base": {
    "punti": [
     "P",
     "D",
     "E",
     "e",
     "L",
     "M",
     "m"
    ],
    "vincoli": [
     "em inversamente proporzionale al lato quadrato di PQRD ± DFge",
     "DL ordinata corrispondente in D",
     "rettangolo 2PD × DL"
    ]
   },
   "passi": [
    {
     "id": "L1-P39-Cor3-p1",
     "la": "",
     "it": "Si conoscerà anche il tempo innalzando l’ordinata em inversamente proporzionale al lato quadrato di PQRD + o − DFge, e prendendo il tempo in cui il corpo ha descritto la linea De al tempo in cui l’altro corpo è caduto da P per una forza uniforme ed è giunto cadendo in D, come l’area curvilinea DLme sta al rettangolo 2PD × DL.",
     "en": "The time is also known by erecting the ordinate em reciprocally proportional to the square root of PQRD + or - DFge, and taking the time in which the body has described the line De to the time in which another body has fallen with an uniform force from P, and in falling arrived at D in the proportion of the curvilinear area DLme to the rectangle 2PD × DL.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "ordinata em",
       "area DLme",
       "rettangolo 2PD × DL"
      ],
      "evidenzia": [
       "tempo De : tempo PD = DLme : 2PD × DL"
      ]
     }
    },
    {
     "id": "L1-P39-Cor3-p2",
     "la": "",
     "it": "Infatti il tempo in cui il corpo che scende per una forza uniforme ha descritto la linea PD sta al tempo in cui lo stesso corpo ha descritto la linea PE in rapporto subduplicato di PD a PE, cioè (mentre la piccola linea DE sta appena nascendo) nel rapporto di PD a PD + ½DE, ossia di 2PD a 2PD + DE; e, per separazione, sta al tempo in cui lo stesso corpo ha descritto la piccola linea DE come 2PD sta a DE, e quindi come il rettangolo 2PD × DL sta all’area DLME; e il tempo in cui l’uno e l’altro corpo hanno descritto la piccola linea DE sta al tempo in cui l’altro corpo, con moto non uniforme, ha descritto la linea De come l’area DLME sta all’area DLme; e, per uguaglianza, il primo tempo sta all’ultimo come il rettangolo 2PD × DL sta all’area DLme.",
     "en": "For the time in which a body falling with an uniform force hath described the line PD, is to the time in which the same body has described the line PE in the subduplicate ratio of PD to PE; that is (the very small line DE being just nascent), in the ratio of PD to PD + [SVG 146], or 2PD to 2PD + DE, and, by division, to the time in which the body hath described the small line DE, as 2PD to DE, and therefore as the rectangle 2PD × DL to the area DLME; and the time in which both the bodies described the very small line DE is to the time in which the body moving unequably hath described the line De as the area DLME to the area DLme; and, ex æquo, the first mentioned of these times is to the last as the",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "PE",
       "DE",
       "area DLME"
      ],
      "evidenzia": [
       "tempo PD : tempo DE = 2PD : DE"
      ]
     },
     "nota": "La fine della frase di Motte («rectangle 2PD × DL to the area DLme.») è all’inizio del file della Sezione VIII; qui `en` si ferma alla fine del file della Sezione VII. «12DE» = ½DE."
    }
   ],
   "nota": "Incluso perché ha una dimostrazione propria; FIG 92 accompagna i Cor. 2–3."
  },
  {
   "id": "L1-P40",
   "tipo": "Propositio/Theorema",
   "titolo": "Prop. XL — velocità uguali ad altezze uguali",
   "copertura": [
    "S8.01",
    "S8.02",
    "S8.03"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 168–169"
   },
   "enunciato": {
    "la": "",
    "it": "Se un corpo, costretto da una forza centripeta qualsiasi, si muove in un modo qualunque, e un altro corpo sale o scende in linea retta, e le loro velocità sono uguali in un caso qualsiasi di altezze uguali, le loro velocità saranno uguali a tutte le altezze uguali.",
    "en": "If a body, acted upon by any centripetal force, is any how moved, and another body ascends or descends in a right line, and their velocities be equal in any one case of equal altitudes, their velocities will be also equal at all equal altitudes."
   },
   "figura_base": {
    "punti": [
     "A",
     "C",
     "D",
     "E",
     "V",
     "I",
     "K",
     "k",
     "N",
     "T"
    ],
    "vincoli": [
     "corpo in caduta lungo AC",
     "corpo sulla curva VIKk",
     "cerchi concentrici DI, EK di centro C",
     "N = IC ∩ cerchio EK; NT perpendicolare a IK",
     "DE = IN piccolissime"
    ]
   },
   "passi": [
    {
     "id": "L1-P40-p1",
     "la": "",
     "it": "Un corpo scenda da A per D ed E verso il centro C, e un altro corpo si muova da V sulla linea curva VIKk.",
     "en": "Let a body descend from A through D and E, to the centre C; and let another body move from V in the curve line VIKk.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "A",
       "D",
       "E",
       "C",
       "V",
       "curva VIKk"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P40-p2",
     "la": "",
     "it": "Con centro C e distanze qualsiasi si descrivano i cerchi concentrici DI, EK, che incontrino la retta AC in D ed E e la curva VIK in I e K.",
     "en": "From the centre C, with any distances, describe the concentric circles DI, EK, meeting the right line AC in D and E, and the curve VIK in I and K.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchi DI, EK",
       "I",
       "K"
      ],
      "evidenzia": []
     },
     "nota": "«occurentes»: refuso probabile per «occurrentes»."
    },
    {
     "id": "L1-P40-p3",
     "la": "",
     "it": "Si congiunga IC, che incontri KE in N, e su IK si abbassi la perpendicolare NT; la distanza DE, o IN, fra le circonferenze dei cerchi sia piccolissima, e i corpi abbiano in D e in I velocità uguali.",
     "en": "Draw IC meeting KE in N, and on IK let fall the perpendicular NT; and let the interval DE or IN between the circumferences of the circles be very small; and imagine the bodies in D and I to have equal velocities.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "IC",
       "N",
       "NT",
       "T"
      ],
      "evidenzia": [
       "v(D) = v(I)"
      ]
     }
    },
    {
     "id": "L1-P40-p4",
     "la": "",
     "it": "Poiché le distanze CD, CI sono uguali, le forze centripete in D e in I saranno uguali.",
     "en": "Then because the distances CD and CI are equal, the centripetal forces in D and I will be also equal.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "forza in D = forza in I"
      ]
     }
    },
    {
     "id": "L1-P40-p5",
     "la": "",
     "it": "Si rappresentino queste forze con le piccole linee uguali DE, IN; e se una delle due forze, IN, si scompone (per il Cor. 2 delle leggi) in due, NT e IT, la forza NT, agendo lungo la linea NT perpendicolare al percorso ITK del corpo, non muterà affatto la velocità del corpo in quel percorso, ma lo distoglierà soltanto dal percorso rettilineo e lo farà deviare continuamente dalla tangente dell’orbita e procedere sulla via curvilinea ITKk.",
     "en": "Let those forces be expressed by the equal lineolæ DE and IN; and let the force IN (by Cor. 2 of the Laws of Motion) be resolved into two others, NT and IT. Then the force NT acting in the direction of the line NT perpendicular to the path ITK of the body will not at all affect or change the velocity of the body in that path, but only draw it aside from a rectilinear course, and make it deflect perpetually from the tangent of the orbit, and proceed in the curvilinear path ITKk.",
     "dipende_da": [
      "Leggi, Cor. II"
     ],
     "figura": {
      "mostra": [
       "DE",
       "IN",
       "NT",
       "IT"
      ],
      "evidenzia": [
       "IN = NT + IT (scomposizione)"
      ]
     }
    },
    {
     "id": "L1-P40-p6",
     "la": "",
     "it": "Nel produrre questo effetto quella forza si consumerà tutta; l’altra forza, IT, agendo lungo il percorso del corpo, lo accelererà tutta, e in un tempo dato piccolissimo genererà un’accelerazione proporzionale a sé stessa.",
     "en": "That whole force, therefore, will be spent in producing this effect; but the other force IT, acting in the direction of the course of the body, will be all employed in accelerating it, and in the least given time will produce an acceleration proportional to itself.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "NT curva la via; IT accelera"
      ]
     }
    },
    {
     "id": "L1-P40-p7",
     "la": "",
     "it": "Perciò le accelerazioni dei corpi in D e in I prodotte in tempi uguali (se si prendono i rapporti primi delle linee nascenti DE, IN, IK, IT, NT) sono come le linee DE, IT; in tempi disuguali, invece, come quelle linee e i tempi considerati congiuntamente.",
     "en": "Therefore the accelerations of the bodies in D and I, produced in equal times, are as the lines DE, IT (if we take the first ratios of the nascent lines DE, IN, IK, IT, NT); and in unequal times as those lines and the times conjunctly.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "accelerazioni ∝ DE, IT"
      ]
     }
    },
    {
     "id": "L1-P40-p8",
     "la": "",
     "it": "Ma i tempi in cui sono descritte DE e IK, per l’uguaglianza delle velocità, sono come le vie descritte DE e IK; e quindi le accelerazioni, nel percorso dei corpi lungo le linee DE e IK, sono come DE e IT, DE e IK considerate congiuntamente, cioè come il quadrato di DE e il rettangolo IT × IK.",
     "en": "But the times in which DE and IK are described, are, by reason of the equal velocities (in D and I) as the spaces described DE and IK, and therefore the accelerations in the course of the bodies through the lines DE and IK are as DE and IT, and DE and IK conjunctly; that is, as the square of DE to the rectangle IT into IK.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "tempi ∝ DE, IK"
      ]
     },
     "nota": "Motte aggiunge «(in D and I)»."
    },
    {
     "id": "L1-P40-p9",
     "la": "",
     "it": "Ma il rettangolo IT × IK è uguale al quadrato di IN, cioè uguale al quadrato di DE; e perciò le accelerazioni generate nel passaggio dei corpi da D e da I a E e a K sono uguali.",
     "en": "But the rectangle IT × IK is equal to the square of IN, that is, equal to the square of DE; and therefore the accelerations generated in the passage of the bodies from D and I to E and K are equal.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "IT × IK = IN² = DE²"
      ]
     }
    },
    {
     "id": "L1-P40-p10",
     "la": "",
     "it": "Uguali sono dunque le velocità dei corpi in E e in K; e con lo stesso argomento si troveranno sempre uguali alle successive distanze uguali. C.V.D.",
     "en": "Therefore the velocities of the bodies in E and K are also equal: and by the same reasoning they will always be found equal in any subsequent equal distances. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "E",
       "K"
      ],
      "evidenzia": [
       "v(E) = v(K)"
      ]
     }
    },
    {
     "id": "L1-P40-p11",
     "la": "",
     "it": "Ma anche, con lo stesso argomento, corpi ugualmente veloci e ugualmente distanti dal centro saranno ritardati in egual misura nella salita fino a distanze uguali. C.V.D.",
     "en": "By the same reasoning, bodies of equal velocities and equal distances from the centre will be equally retarded in their ascent to equal distances. Q.E.D.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "vale anche in salita"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P41",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XLI — trovare le traiettorie per quadrature",
   "copertura": [
    "S8.06",
    "S8.07",
    "S8.08",
    "S8.09"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 169–171"
   },
   "enunciato": {
    "la": "",
    "it": "Posta una forza centripeta di qualsiasi genere, e concesse le quadrature delle figure curvilinee, si richiedono sia le traiettorie su cui i corpi si muoveranno, sia i tempi dei moti sulle traiettorie trovate.",
    "en": "Supposing a centripetal force of any kind, and granting the quadratures of curvilinear figures, it is required to find as well the trajectories in which bodies will move, as the times of their motions in the trajectories found."
   },
   "figura_base": {
    "punti": [
     "C",
     "V",
     "R",
     "I",
     "K",
     "k",
     "D",
     "E",
     "N",
     "X",
     "Y",
     "A",
     "B",
     "F",
     "a",
     "b",
     "c",
     "z",
     "x"
    ],
    "vincoli": [
     "cerchio VR di centro C e raggio CV",
     "cerchi ID, KE di centro C",
     "retta CNIX; retta CKY",
     "I, K vicinissimi sulla traiettoria VIKk",
     "A: luogo di caduta che dà in D la velocità del corpo in I (Prop. XXXIX)",
     "Db = Q/(2√(ABFD − ZZ)); Dc = Q × CX²/(2AA√(ABFD − ZZ)), con A = CI, Z = Q/A",
     "curve ab, ac; perpendicolare Va"
    ]
   },
   "passi": [
    {
     "id": "L1-P41-p1",
     "la": "",
     "it": "Tenda una forza qualsiasi al centro C, e si debba trovare la traiettoria VIKk.",
     "en": "Let any centripetal force tend to the centre C, and let it be required to find the trajectory VIKk.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "C",
       "traiettoria VIKk"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P41-p2",
     "la": "",
     "it": "Sia dato il cerchio VR, descritto con centro C e raggio qualsiasi CV, e con lo stesso centro si descrivano altri cerchi qualsiasi ID, KE, che taglino la traiettoria in I e K e la retta CV in D ed E.",
     "en": "Let there be given the circle VR, described from the centre C with any interval CV; and from the same centre describe any other circles ID, KE cutting the trajectory in I and K, and the right line CV in D and E.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "cerchio VR",
       "cerchi ID, KE",
       "I",
       "K",
       "D",
       "E"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P41-p3",
     "la": "",
     "it": "Si conducano poi sia la retta CNIX, che tagli i cerchi KE, VR in N e X, sia la retta CKY, che incontri il cerchio VR in Y.",
     "en": "Then draw the right line CNIX cutting the circles KE, VR in N and X, and the right line CKY meeting the circle VR in Y.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "retta CNIX",
       "N",
       "X",
       "retta CKY",
       "Y"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P41-p4",
     "la": "",
     "it": "Siano poi i punti I e K vicinissimi fra loro, e il corpo proceda da V per I e K fino a k; e sia A il luogo da cui un altro corpo deve cadere per acquistare nel luogo D una velocità uguale alla velocità del primo corpo in I.",
     "en": "Let the points I and K he indefinitely near; and let the body go on from V through I and K to k; and let the point A be the place from whence another body is to fall, so as in the place D to acquire a velocity equal to the velocity of the first body in I.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "k",
       "A"
      ],
      "evidenzia": [
       "v(D) del corpo che cade = v(I)"
      ]
     }
    },
    {
     "id": "L1-P41-p5",
     "la": "",
     "it": "Restando ferme le cose stabilite nella Prop. XXXIX, la piccola linea IK, descritta in un tempo dato piccolissimo, sarà come la velocità, e quindi come la retta il cui quadrato è uguale all’area ABFD; e il triangolo ICK, proporzionale al tempo, sarà dato; e perciò KN sarà inversamente come l’altezza IC, cioè, se è data una quantità Q e l’altezza IC si chiama A, come Q/A.",
     "en": "And things remaining as in Prop. XXXIX, the lineola IK, described in the least given time will be as the velocity, and therefore as the right line whose square is equal to the area ABFD, and the triangle ICK proportional to the time will be given, and therefore KN will be reciprocally as the altitude IC; that is (if there be given any quantity Q, and the altitude IC be called A), as [SVG 149].",
     "dipende_da": [
      "Prop. XXXIX"
     ],
     "figura": {
      "mostra": [
       "IK",
       "triangolo ICK"
      ],
      "evidenzia": [
       "IK ∝ √ABFD; KN = Q/A"
      ]
     },
     "nota": "«ut QA» = Q/A."
    },
    {
     "id": "L1-P41-p6",
     "la": "",
     "it": "Chiamiamo Z questa quantità Q/A, e poniamo che la grandezza di Q sia tale che in un caso qualsiasi √ABFD stia a Z come IK sta a KN: in ogni caso √ABFD starà a Z come IK sta a KN, e ABFD a ZZ come IK² sta a KN², e per separazione ABFD − ZZ starà a ZZ come IN² sta a KN²; e quindi √(ABFD − ZZ) starà a Z, ossia a Q/A, come IN sta a KN, e perciò A × KN sarà uguale a Q × IN/√(ABFD − ZZ).",
     "en": "This quantity [SVG 150] call Z, and suppose the magnitude of Q to be such that in some case [SVG 151] may be to Z as IK to KN, and then in all cases [SVG 151] will be to Z as IK to KN, and ABFD to ZZ as IK2 to KN2, and by division ABFD - ZZ to ZZ as IN2 to KN2, and therefore [SVG 152] to Z, or [SVG 149] as IN to KN; and therefore A × KN will be equal to [SVG 153].",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "√(ABFD − ZZ) : Z = IN : KN"
      ]
     },
     "nota": "La trascrizione perde i segni di radice: «ABFD ad Z» = √ABFD a Z (Motte SVG 151); «ABFD−ZZ ad Z» = √(ABFD − ZZ) a Z; «Q×INABFD−ZZ» = Q × IN/√(ABFD − ZZ)."
    },
    {
     "id": "L1-P41-p7",
     "la": "",
     "it": "Di qui, poiché YX × XC sta ad A × KN come CX² sta ad AA, il rettangolo YX × XC sarà uguale a Q × IN × CX²/(AA√(ABFD − ZZ)).",
     "en": "Therefore since YX × XC is to A × KN as CX2, to AA, the rectangle XY × XC will be equal to [SVG 154].",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "rettangolo YX × XC"
      ],
      "evidenzia": [
       "YX × XC : A × KN = CX² : AA"
      ]
     },
     "nota": "«Q×IN×CX quad.AAABFD−ZZ» = Q × IN × CX²/(AA√(ABFD − ZZ)). Motte scrive una volta «XY × XC»."
    },
    {
     "id": "L1-P41-p8",
     "la": "",
     "it": "Se dunque nella perpendicolare DF si prendono sempre Db, Dc uguali rispettivamente a Q/(2√(ABFD − ZZ)) e a Q × CX²/(2AA√(ABFD − ZZ)), e si descrivono le linee curve ab, ac, che i punti b, c descrivono continuamente; e dal punto V si innalza sulla linea AC la perpendicolare Va, che taglia le aree curvilinee VDba, VDca, e si innalzano anche le ordinate Ez, Ex: poiché il rettangolo Db × IN, ossia DbzE, è uguale alla metà del rettangolo A × KN, ossia al triangolo ICK, e il rettangolo Dc × IN, ossia DcxE, è uguale alla metà del rettangolo YX × XC, ossia al triangolo XCY; cioè, poiché le particelle nascenti DbzE, ICK delle aree VDba, VIC sono sempre uguali, e le particelle nascenti DcxE, XCY delle aree VDca, VCX sono sempre uguali, l’area generata VDba sarà uguale all’area generata VIC, e quindi proporzionale al tempo, e l’area generata VDca sarà uguale al settore generato VCX.",
     "en": "Therefore in the perpendicular DF let there be taken continually Db, Dc equal to [SVG 155], [SVG 156] respectively, and let the curve lines ab, ac, the foci of the points b and c, be described: and from the point V let the perpendicular Va be erected to the line AC, cutting off the curvilinear areas VDba, VDca, and let the ordinates Ez, Ex, be erected also. Then because the rectangle Db × IN or DbzE is equal to half the rectangle A × KN, or to the triangle ICK; and the rectangle Dc × IN or DcxE is equal to half the rectangle YX × XC, or to the triangle XCY; that is, because the nascent particles DbzE, ICK of the areas VDba, VIC are always equal; and the nascent particles DcxE, XCY of the areas VDca, VCX are always equal: therefore the generated area VDba will be equal to the generated area VIC, and therefore proportional to the time; and the generated area VDca is equal to the generated sector VCX.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "Db",
       "Dc",
       "curve ab, ac",
       "Va",
       "aree VDba, VDca",
       "Ez",
       "Ex"
      ],
      "evidenzia": [
       "area VDba = area VIC ∝ tempo; area VDca = settore VCX"
      ]
     },
     "nota": "«Q2ABFD−ZZ» = Q/(2√(ABFD − ZZ)). Motte: «the foci of the points b and c», refuso per «loci»."
    },
    {
     "id": "L1-P41-p9",
     "la": "",
     "it": "Dato dunque un tempo qualsiasi trascorso da quando il corpo è partito dal luogo V, sarà data l’area VDba proporzionale a esso, e di qui sarà data l’altezza del corpo CD o CI; e l’area VDca, e il settore VCX uguale a essa, insieme con il suo angolo VCI.",
     "en": "If, therefore, any time be given during which the body has been moving from V, there will be also given the area proportional to it VDba; and thence will be given the altitude of the body CD or CI; and the area VDca, and the sector VCX equal thereto, together with its angle VCI.",
     "dipende_da": [],
     "figura": {
      "mostra": [],
      "evidenzia": [
       "tempo → altezza CI; area VDca → angolo VCI"
      ]
     }
    },
    {
     "id": "L1-P41-p10",
     "la": "",
     "it": "Dati poi l’angolo VCI e l’altezza CI, è dato il luogo I in cui il corpo si troverà al compiersi di quel tempo. C.V.T.",
     "en": "But the angle VCI, and the altitude CI being given, there is also given the place I, in which the body will be found at the end of that time. Q.E.I.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "I"
      ],
      "evidenzia": [
       "luogo I dal raggio CI e dall’angolo VCI"
      ]
     }
    }
   ]
  },
  {
   "id": "L1-P42",
   "tipo": "Propositio/Problema",
   "titolo": "Prop. XLII — il moto da condizioni iniziali date",
   "copertura": [
    "S8.13",
    "S8.14"
   ],
   "fonti": {
    "la": "",
    "en": "Motte 1846, pp. 171–172"
   },
   "enunciato": {
    "la": "",
    "it": "Data la legge della forza centripeta, si richiede il moto di un corpo partito da un luogo dato, con una velocità data, lungo una retta data.",
    "en": "The law of centripetal force being given, it is required to find the motion of a body setting out from a given place, with a given velocity, in the direction of a given right line."
   },
   "figura_base": {
    "punti": [
     "I",
     "K",
     "k",
     "C",
     "P",
     "D",
     "R",
     "Q",
     "e",
     "g",
     "v",
     "w",
     "X",
     "y"
    ],
    "vincoli": [
     "partenza da I lungo IK",
     "velocità iniziale = velocità acquistata cadendo da P a D con forza uniforme",
     "DR : DF = forza uniforme : forza in I",
     "cerchio ke di centro C e raggio Ck, e su PD",
     "curve BFg, abv, acw con ordinate eg, ev, ew"
    ]
   },
   "passi": [
    {
     "id": "L1-P42-p1",
     "la": "",
     "it": "Restando ferme le cose stabilite nelle tre proposizioni precedenti, il corpo esca dal luogo I lungo la piccola linea IK con la velocità che un altro corpo, cadendo dal luogo P per una forza centripeta uniforme, potrebbe acquistare in D; e questa forza uniforme stia alla forza con cui il primo corpo è sollecitato in I come DR sta a DF.",
     "en": "Suppose the same things as in the three preceding propositions; and let the body go off from the place I in the direction of the little line, IK, with the same velocity as another body, by falling with an uniform centripetal force from the place P, may acquire in D; and let this uniform force be to the force with which the body is at first urged in I, as DR to DF.",
     "dipende_da": [
      "Prop. XXXIX",
      "Prop. XL",
      "Prop. XLI"
     ],
     "figura": {
      "mostra": [
       "I",
       "IK",
       "P",
       "D",
       "DR",
       "DF"
      ],
      "evidenzia": [
       "velocità iniziale data dalla caduta PD"
      ]
     },
     "nota": "«tribus propositionibus præcedentibus»: le Prop. XXXIX–XLI; il rimando è generico, qui esplicitato."
    },
    {
     "id": "L1-P42-p2",
     "la": "",
     "it": "Il corpo proceda poi verso k; con centro C e raggio Ck si descriva il cerchio ke, che incontri la retta PD in e, e si innalzino le ordinate eg, ev, ew delle curve BFg, abv, acw.",
     "en": "Let the body go on towards k; and about the centre C, with the interval Ck, describe the circle ke, meeting the right line PD in e, and let there be erected the lines eg, ev, ew, ordinately applied to the curves BFg, abv, acw.",
     "dipende_da": [],
     "figura": {
      "mostra": [
       "k",
       "cerchio ke",
       "e",
       "ordinate eg, ev, ew"
      ],
      "evidenzia": []
     }
    },
    {
     "id": "L1-P42-p3",
     "la": "",
     "it": "Dal rettangolo dato PDRQ e dalla legge data della forza centripeta da cui è mosso il primo corpo è data la linea curva BFg, per la costruzione del Problema XXVII e del suo Cor. 1.",
     "en": "From the given rectangle PDRQ and the given law of centripetal force, by which the first body is acted on, the curve line BFg is also given, by the construction of Prop. XXVII, and its Cor. 1.",
     "dipende_da": [
      "Probl. XXVII (= Prop. XXXIX)",
      "Prop. XXXIX, Cor. 1"
     ],
     "figura": {
      "mostra": [
       "curva BFg",
       "rettangolo PDRQ"
      ],
      "evidenzia": []
     },
     "nota": "Motte: «by the construction of Prop. XXVII», rimando errato; il Problema XXVII è la Prop. XXXIX (§ A.15)."
    },
    {
     "id": "L1-P42-p4",
     "la": "",
     "it": "Poi dall’angolo dato CIK è dato il rapporto delle nascenti IK, KN, e di qui, per la costruzione del Problema XXVIII, è data la quantità Q insieme con le linee curve abv, acw: e perciò, compiuto un tempo qualsiasi Dbve, è data sia l’altezza del corpo Ce o Ck, sia l’area Dcwe, e il settore XCy uguale a essa, e l’angolo ICk, e il luogo k in cui il corpo si troverà allora. C.V.T.",
     "en": "Then from the given angle CIK is given the proportion of the nascent lines IK, KN; and thence, by the construction of Prob. XXVIII, there is given the quantity Q, with the curve lines abv, acw; and therefore, at the end of any time Dbve, there is given both the altitude of the body Ce or Ck, and the area Dcwe, with the sector equal to it XCy, the angle ICk, and the place k, in which the body will then be found. Q.E.I.",
     "dipende_da": [
      "Probl. XXVIII (= Prop. XLI)"
     ],
     "figura": {
      "mostra": [
       "Q",
       "curve abv, acw",
       "area Dbve",
       "area Dcwe",
       "settore XCy",
       "angolo ICk",
       "k"
      ],
      "evidenzia": [
       "tempo → altezza Ck e angolo ICk"
      ]
     }
    }
   ]
  }
 ]
}
```

**Esito della validazione** (`check.py` sulle tre trascrizioni latine e sui tre file di Motte, 8 novembre 2026): 16 unità, 114 passi, 63 identificatori nel testo; JSON valido; tutte le stringhe `la` ed `en` sono sottostringhe esatte delle fonti; nessun errore, nessun avviso.
