> **Copia pubblica.** In questa versione i campi `"la"` della Parte B sono vuoti: le frasi latine vengono dalla trascrizione del Newton Project, che non si ridistribuisce. Il latino del 1726 si legge su newtonproject.ox.ac.uk.

# Isaac Newton
# Principi matematici della filosofia naturale

## Fascicolo 10 — Libro I, Sezione XI: il moto dei corpi che si dirigono gli uni verso gli altri per effetto di forze centripete

**Nuova traduzione italiana di lavoro dal latino del 1726, confrontata con l’inglese di Andrew Motte nell’edizione del 1846.**

Versione 0.1 — 8 novembre 2026. Preparata con Claude (Anthropic) per Massimo Bosetti.

### Stato e perimetro

Questo fascicolo traduce integralmente la **Sezione XI del Libro I**, *De motu corporum viribus centripetis se mutuo petentium*: il proemio, le Proposizioni LVII–LXIX con i loro casi e corollari (compresi i 22 corollari della Prop. LXVI, la prima trattazione del problema dei tre corpi) e lo Scolio finale, che introduce la Sezione XII. È una traduzione di lavoro, non un’edizione critica validata.

Gli identificatori **S11.01–S11.72** e i titoli tematici tra parentesi sono aggiunte editoriali. Servono a orientare la lettura e a controllare la completezza. I numeri romani delle proposizioni, dei teoremi e dei problemi e i numeri dei casi e dei corollari appartengono al testo originale. Eventuali integrazioni del curatore sono tra parentesi quadre. Le note poste dopo la traduzione non fanno parte del testo di Newton.

In coda al fascicolo la **Parte B** contiene i dati strutturati per le pagine interattive delle proposizioni con dimostrazione geometrica e figura: LVIII, LXIV, LXVI (Casi 1 e 2), LXVII e LXVIII. I corollari della Prop. LXVI, discorsivi anche quando il latino segnala una figura, sono soltanto tradotti e annotati.

### Fonti effettivamente consultate

1. **Latino di riferimento.** Isaac Newton, *Philosophiæ Naturalis Principia Mathematica*, terza edizione, Londra, 1726, Libro I, Sezione XI, pp. 160–188. Trascrizione normalizzata del Newton Project, documento **NATP00087**, nel file di lavoro `fonti/latino-1726-L1-S11.md` (scaricato l’8 novembre 2026, testo semplice senza correzioni). Le pagine sono ricavate dai marcatori <161>…<189> della trascrizione: la sezione comincia a p. 160 e lo Scolio termina a p. 188. Le figure NATP00087-120…131, segnalate con [FIG n], non erano disponibili.
2. **Inglese di confronto.** *Newton’s Principia. The Mathematical Principles of Natural Philosophy*, traduzione di Andrew Motte, New York, Daniel Adee, 1846, Section XI, **pp. 194–218** secondo i marcatori di pagina (`id="Page_n"`) dell’EPUB Project Gutenberg n. 76404, file `76404-h-13` e `-14`. Estratto di lavoro: `fonti/motte-1846-L1-S11.md`. Nell’estratto non compaiono formule-immagine [SVG]; l’unico esponente, «ST3» nel Cor. 14 della Prop. LXVI, è nell’EPUB `ST<sup>3</sup>`, cioè ST³.
3. **Fascicolo 3** (modello di formato) e **Fascicolo 1** (per la resa di *impulsus* e *attractio* nella Def. VIII), insieme al brief comune del Libro I.
4. Per controllare la numerazione dei rimandi interni (problemi, teoremi, corollari) ho consultato le trascrizioni latine delle Sezioni I–X dello stesso documento NATP00087, nei file `fonti/latino-1726-L1-S01…S10.md`.

Non ho consultato né riprodotto traduzioni moderne. Non ho potuto controllare la stampa del 1726: i refusi segnalati sono «refusi probabili della trascrizione, da verificare sulla stampa».

### Criteri di traduzione

- Il testo guida è il latino; l’inglese serve a controllare le interpretazioni ed è annotato quando aggiunge, omette o sbaglia (§ A.13).
- Si applica il **glossario comune** del brief del Libro I (fascicoli 1–3 e termini tecnici del Libro I): in particolare «forza acceleratrice», «forza motrice», «forza assoluta», «forza centripeta», «rapporto duplicato / triplicato / subduplicato / sesquiplicato», «inversamente», «considerate congiuntamente», «in linea retta», «tempo periodico», «apside», «in conseguenza / in antecedenza», «lato retto», «fuoco», «asse principale», «Caso», «Cor.», «Scolio».
- Italiano contemporaneo, con la struttura argomentativa e il lessico storico: i rapporti restano rapporti; le formule moderne stanno solo nelle note.
- Gli enunciati in accusativo e infinito (Prop. LIX, LXV) sono resi all’indicativo.
- Le abbreviazioni del tipo «ST cub.» sono scritte ST³; il prodotto «SD×T» resta «SD × T», come nella trascrizione.
- Le **estensioni del glossario** proprie di questa sezione (lessico astronomico del problema dei tre corpi: sizigie, quadrature, ottanti, nodi, auge, apside superiore e inferiore, errori, e altri termini) sono elencate e motivate nel § A.0.

---

## Traduzione italiana

### Sezione XI. Il moto dei corpi che si dirigono gli uni verso gli altri per effetto di forze centripete

**[S11.01]** Finora ho esposto i moti dei corpi attratti verso un centro immobile, quale tuttavia difficilmente esiste in natura. Le attrazioni, infatti, sogliono essere dirette verso corpi; e le azioni dei corpi che attraggono e di quelli attratti sono sempre reciproche e uguali, per la Legge III: cosicché, se i corpi sono due, né quello che attrae né quello attratto possono essere in quiete, ma entrambi (per il Cor. IV delle leggi), come per un’attrazione reciproca, ruotano attorno al centro comune di gravità; e, se i corpi sono più di due, e o sono attratti da uno solo e lo attraggono a loro volta, o si attraggono tutti a vicenda, devono muoversi fra loro in modo che il centro comune di gravità o sia in quiete o si muova uniformemente in linea retta. Per questa ragione passo ora a esporre il moto dei corpi che si attraggono a vicenda, considerando le forze centripete come attrazioni, benché forse, se parliamo in termini fisici, sarebbe più corretto chiamarle spinte. Ci occupiamo infatti ora di matematica; e perciò, messe da parte le dispute fisiche, usiamo un linguaggio familiare, per poter essere compresi più facilmente dai lettori matematici.

### Proposizione LVII. Teorema XX (figure simili attorno al centro comune e attorno all’altro corpo)

**[S11.02]** **Due corpi che si attraggono a vicenda descrivono figure simili, sia attorno al centro comune di gravità, sia l’uno attorno all’altro.**

**[S11.03]** Le distanze dal centro comune di gravità sono infatti inversamente proporzionali ai corpi, e perciò stanno fra loro in un rapporto dato e, componendo, stanno in un rapporto dato con la distanza totale fra i corpi. Queste distanze, poi, ruotano attorno al loro estremo comune con moto angolare uguale, perché, giacendo sempre in linea retta, non mutano la loro inclinazione reciproca. Ora, le linee rette che stanno fra loro in un rapporto dato e ruotano con moto angolare uguale attorno ai loro estremi descrivono attorno a quegli stessi estremi figure del tutto simili, in piani che, insieme con quegli estremi, o sono in quiete o si muovono di un moto qualsiasi non angolare. Sono dunque simili le figure descritte dalla rotazione di queste distanze. C.V.D.

### Proposizione LVIII. Teorema XXI (orbita relativa e orbita attorno a un corpo immobile)

**[S11.04]** **Se due corpi si attraggono a vicenda con forze qualsiasi e intanto ruotano attorno al centro comune di gravità, dico che, con le stesse forze, si può descrivere attorno a uno dei due, immobile, una figura simile e uguale alle figure che i corpi, così mossi, descrivono l’uno attorno all’altro.**

**[S11.05]** Ruotino i corpi S, P attorno al centro comune di gravità C, procedendo da S verso T e da P verso Q. Da un punto dato s si conducano sempre sp, sq uguali e parallele a SP, TQ: la curva pqv, che il punto p descrive ruotando attorno al punto immobile s, sarà simile e uguale alle curve che i corpi S, P descrivono l’uno attorno all’altro; e quindi (per il Teor. XX) simile alle curve ST e PQV che gli stessi corpi descrivono attorno al centro comune di gravità C; e ciò perché sono dati i rapporti fra loro delle linee SC, CP e SP, o sp.

**[S11.06]** Caso 1. Quel centro comune di gravità C, per il Cor. IV delle leggi, o è in quiete o si muove uniformemente in linea retta. Supponiamo dapprima che sia in quiete, e in s e p si pongano due corpi, uno immobile in s e uno mobile in p, simili e uguali ai corpi S e P. Poi le rette PR e pr tocchino le curve PQ e pq in P e p, e si prolunghino CQ e sq fino a R e r. Per la similitudine delle figure CPRQ, sprq, RQ starà a rq come CP sta a sp, e quindi in un rapporto dato. Perciò, se la forza con cui il corpo P è attratto verso il corpo S, e quindi verso il centro intermedio C, stesse alla forza con cui il corpo p è attratto verso il centro s in quello stesso rapporto dato, queste forze, in tempi uguali, trarrebbero sempre i corpi dalle tangenti PR, pr verso gli archi PQ, pq per intervalli proporzionali a esse, RQ, rq; e quindi la seconda forza farebbe sì che il corpo p girasse lungo la curva pqv, simile alla curva PQV lungo la quale la prima forza fa girare il corpo P, e le rivoluzioni si compirebbero negli stessi tempi. Ma poiché quelle forze non stanno fra loro nel rapporto di CP a sp, ma sono uguali fra loro (per la similitudine e l’uguaglianza dei corpi S e s, P e p, e per l’uguaglianza delle distanze SP, sp), i corpi in tempi uguali saranno tratti in egual misura dalle tangenti; e perciò, perché il secondo corpo p sia tratto per l’intervallo maggiore rq, si richiede un tempo maggiore, e precisamente in rapporto subduplicato degli intervalli, perché (per il Lemma X) gli spazi descritti all’inizio stesso del moto stanno in rapporto duplicato dei tempi. Si ponga dunque che la velocità del corpo p stia alla velocità del corpo P in rapporto subduplicato della distanza sp alla distanza CP, in modo che gli archi pq, PQ, che stanno nel rapporto semplice [delle distanze], siano descritti in tempi che stanno in quello stesso rapporto subduplicato: e i corpi P, p, attratti sempre da forze uguali, descriveranno attorno ai centri in quiete C e s figure simili PQV, pqv, la seconda delle quali, pqv, è simile e uguale alla figura che il corpo P descrive attorno al corpo mobile S. C.V.D.

**[S11.07]** Caso 2. Supponiamo ora che il centro comune di gravità, insieme con lo spazio in cui i corpi si muovono fra loro, avanzi uniformemente in linea retta: (per il Cor. VI delle leggi) tutti i moti in questo spazio si compiranno come prima, e quindi i corpi descriveranno l’uno attorno all’altro le stesse figure di prima, e perciò figure simili e uguali a pqv. C.V.D.

**[S11.08]** Cor. 1. Di qui due corpi che si attraggono a vicenda con forze proporzionali alla loro distanza descrivono (per la Prop. X), sia attorno al centro comune di gravità sia l’uno attorno all’altro, ellissi concentriche; e viceversa, se si descrivono figure di questo genere, le forze sono proporzionali alla distanza.

**[S11.09]** Cor. 2. E due corpi, con forze inversamente proporzionali al quadrato della loro distanza, descrivono (per le Prop. XI, XII, XIII), sia attorno al centro comune di gravità sia l’uno attorno all’altro, sezioni coniche che hanno il fuoco nel centro attorno al quale le figure sono descritte. E viceversa, se si descrivono figure di questo genere, le forze centripete sono inversamente proporzionali al quadrato della distanza.

**[S11.10]** Cor. 3. Due corpi qualsiasi che girano attorno al centro comune di gravità, con raggi condotti sia a quel centro sia dall’uno all’altro, descrivono aree proporzionali ai tempi.

### Proposizione LIX. Teorema XXII (rapporto dei tempi periodici)

**[S11.11]** **Il tempo periodico di due corpi S e P che ruotano attorno al centro comune di gravità C sta al tempo periodico di uno dei due, P, che giri attorno all’altro, S, immobile, descrivendo una figura simile e uguale alle figure che i corpi descrivono l’uno attorno all’altro, in rapporto subduplicato dell’altro corpo S alla somma dei corpi S + P.**

**[S11.12]** Infatti, per la dimostrazione della proposizione precedente, i tempi nei quali sono descritti due archi simili qualsiasi PQ e pq stanno in rapporto subduplicato delle distanze CP e SP, o sp, cioè in rapporto subduplicato del corpo S alla somma dei corpi S + P. E, componendo, le somme dei tempi nei quali sono descritti tutti gli archi simili PQ e pq, cioè i tempi totali nei quali sono descritte le figure intere simili, stanno nello stesso rapporto subduplicato. C.V.D.

### Proposizione LX. Teorema XXIII (rapporto degli assi principali)

**[S11.13]** **Se due corpi S e P, che si attraggono a vicenda con forze inversamente proporzionali al quadrato della loro distanza, ruotano attorno al centro comune di gravità, dico che l’asse principale dell’ellisse che uno dei due, P, descrive con questo moto attorno all’altro, S, starà all’asse principale dell’ellisse che lo stesso corpo P potrebbe descrivere nello stesso tempo periodico attorno all’altro, S, in quiete, come la somma dei due corpi S + P sta alla prima di due medie proporzionali fra questa somma e quell’altro corpo S.**

**[S11.14]** Se infatti le ellissi descritte fossero uguali fra loro, i tempi periodici (per il teorema precedente) starebbero in rapporto subduplicato del corpo S alla somma dei corpi S + P. Si diminuisca in questo rapporto il tempo periodico nella seconda ellisse, e i tempi periodici diverranno uguali; ma l’asse principale dell’ellisse (per la Prop. XV) diminuirà in un rapporto di cui questo è il sesquiplicato, cioè in un rapporto di cui il rapporto di S a S + P è il triplicato; e perciò starà all’asse principale dell’altra ellisse come la prima di due medie proporzionali fra S + P e S sta a S + P. E, inversamente, l’asse principale dell’ellisse descritta attorno al corpo mobile starà all’asse principale di quella descritta attorno al corpo immobile come S + P sta alla prima di due medie proporzionali fra S + P e S. C.V.D.

### Proposizione LXI. Teorema XXIV (riduzione a un corpo posto nel centro comune)

**[S11.15]** **Se due corpi che si attraggono a vicenda con forze qualsiasi, e che non sono altrimenti agitati o impediti, si muovono in un modo qualsiasi, i loro moti saranno gli stessi che se non si attraessero a vicenda, ma fossero attratti entrambi, con le stesse forze, da un terzo corpo posto nel centro comune di gravità. E la legge delle forze attrattive sarà la stessa rispetto alla distanza dei corpi da quel centro comune e rispetto alla distanza totale fra i corpi.**

**[S11.16]** Infatti le forze con cui i corpi si attraggono a vicenda, tendendo ai corpi, tendono al centro comune di gravità intermedio; e perciò sono le stesse che se emanassero da un corpo intermedio. C.V.D.

**[S11.17]** E poiché è dato il rapporto della distanza di ciascuno dei due corpi da quel centro comune alla distanza fra i corpi, sarà dato il rapporto di una potenza qualsiasi di una distanza alla stessa potenza dell’altra; così come il rapporto di una quantità qualsiasi, derivata in un modo qualunque da una delle distanze e da quantità date, a un’altra quantità derivata in modo simile dall’altra distanza e da altrettante quantità date, che stiano alle prime in quel rapporto dato delle distanze. Perciò, se la forza con cui un corpo è attratto dall’altro è direttamente o inversamente come la distanza dei corpi fra loro, o come una qualsiasi potenza di questa distanza, o infine come una quantità qualsiasi derivata in un modo qualunque da questa distanza e da quantità date, la stessa forza con cui lo stesso corpo è attratto verso il centro comune di gravità sarà anch’essa direttamente o inversamente come la distanza del corpo attratto da quel centro comune, o come la stessa potenza di questa distanza, o infine come una quantità derivata in modo simile da questa distanza e da quantità date analoghe. Cioè, la legge della forza attrattiva sarà la stessa rispetto all’una e all’altra distanza. C.V.D.

### Proposizione LXII. Problema XXXVIII (due corpi lasciati cadere)

**[S11.18]** **Determinare i moti di due corpi che si attraggono a vicenda con forze inversamente proporzionali al quadrato della loro distanza e sono lasciati andare da luoghi dati.**

**[S11.19]** I corpi (per l’ultimo teorema) si muoveranno come se fossero attratti da un terzo corpo posto nel centro comune di gravità; e quel centro, per ipotesi, sarà in quiete all’inizio stesso del moto, e perciò (per il Cor. IV delle leggi) sarà sempre in quiete. Si devono dunque determinare i moti dei corpi (per il Probl. XXV) come se fossero sollecitati da forze dirette verso quel centro, e si avranno i moti dei corpi che si attraggono a vicenda. C.V.T.

### Proposizione LXIII. Problema XXXIX (due corpi lanciati)

**[S11.20]** **Determinare i moti di due corpi che si attraggono a vicenda con forze inversamente proporzionali al quadrato della loro distanza e partono da luoghi dati, secondo rette date, con velocità date.**

**[S11.21]** Dati i moti dei corpi all’inizio, è dato il moto uniforme del centro comune di gravità, come pure il moto dello spazio che si muove uniformemente in linea retta insieme con questo centro, e anche i moti iniziali dei corpi rispetto a questo spazio. I moti successivi, poi (per il Cor. V delle leggi e per l’ultimo teorema), avvengono in questo spazio come se lo spazio stesso, insieme con quel centro comune di gravità, fosse in quiete, e i corpi non si attraessero a vicenda, ma fossero attratti da un terzo corpo situato in quel centro. Si deve dunque determinare, con i Probl. IX e XXVI, il moto di uno dei due corpi in questo spazio mobile, che parte da un luogo dato, secondo una retta data, con una velocità data, ed è preso da una forza centripeta diretta verso quel centro; e si avrà insieme il moto dell’altro corpo attorno allo stesso centro. Con questo moto si deve comporre il moto progressivo uniforme, trovato sopra, del sistema formato dallo spazio e dai corpi che vi girano dentro, e si avrà il moto assoluto dei corpi nello spazio immobile. C.V.T.

### Proposizione LXIV. Problema XL (più corpi con forze proporzionali alle distanze)

**[S11.22]** **Se le forze con cui i corpi si attraggono a vicenda crescono in rapporto semplice delle distanze dai centri, si cercano i moti di più corpi fra loro.**

**[S11.23]** Si pongano dapprima due corpi T e L, che hanno il centro comune di gravità in D. Essi descriveranno (per il Cor. 1 del Teor. XXI) ellissi che hanno i centri in D, la cui grandezza si conosce dal Probl. V.

**[S11.24]** Ora un terzo corpo S attragga i primi due, T e L, con le forze acceleratrici ST, SL, e sia attratto da essi a sua volta. La forza ST (per il Cor. II delle leggi) si scompone nelle forze SD, DT, e la forza SL nelle forze SD, DL. Le forze DT, DL, che stanno come la loro somma TL, e quindi come le forze acceleratrici con cui i corpi T e L si attraggono a vicenda, aggiunte a queste forze dei corpi T e L, la prima alla prima e la seconda alla seconda, compongono forze proporzionali alle distanze DT e DL, come prima, ma maggiori delle forze di prima; e perciò (per il Cor. 1 della Prop. X e per i Cor. 1 e 8 della Prop. IV) fanno sì che quei corpi descrivano ellissi come prima, ma con moto più veloce. Le restanti forze acceleratrici SD e SD, con le azioni motrici SD × T e SD × L, che stanno come i corpi, attraendo quei corpi in egual misura e lungo le linee TI, LK parallele a DS, non mutano affatto le loro posizioni reciproche, ma fanno sì che essi si avvicinino in egual misura alla linea IK, che si immagini condotta per il centro del corpo S e perpendicolare alla linea DS. Questo avvicinamento alla linea IK sarà però impedito facendo sì che il sistema dei corpi T e L da una parte e il corpo S dall’altra, con le velocità opportune, girino attorno al centro comune di gravità C. Con un tale moto il corpo S, poiché la somma delle forze motrici SD × T e SD × L, proporzionale alla distanza CS, tende verso il centro C, descrive un’ellisse attorno allo stesso C; e il punto D, poiché CS e CD sono proporzionali, descriverà dalla parte opposta un’ellisse simile. I corpi T e L, poi, attratti dalle forze motrici SD × T e SD × L, il primo dalla prima e il secondo dalla seconda, in egual misura e lungo le linee parallele TI e LK, come si è detto, continueranno (per i Cor. V e VI delle leggi) a descrivere le loro ellissi attorno al centro mobile D, come prima. C.V.T.

**[S11.25]** Si aggiunga ora un quarto corpo V, e con un argomento simile si concluderà che questo e il punto C descrivono ellissi attorno al centro comune di gravità di tutti, B, mentre i moti dei corpi precedenti T, L e S attorno ai centri D e C restano gli stessi, ma accelerati. E con lo stesso metodo si potranno aggiungere più corpi. C.V.T.

**[S11.26]** Le cose stanno così anche se i corpi T e L si attraggono a vicenda con forze acceleratrici maggiori o minori di quelle con cui attraggono gli altri corpi in proporzione alle distanze. Siano le attrazioni acceleratrici reciproche di tutti i corpi come le distanze moltiplicate per i corpi che attraggono: dalle cose precedenti si dedurrà facilmente che tutti i corpi descrivono, con tempi periodici uguali, ellissi diverse attorno al centro comune di gravità di tutti, B, in un piano immobile. C.V.T.

### Proposizione LXV. Teorema XXV (più corpi con forze inverse del quadrato: ellissi approssimate)

**[S11.27]** **Più corpi, le cui forze decrescono in rapporto duplicato delle distanze dai loro centri, possono muoversi fra loro in ellissi e, con raggi condotti ai fuochi, descrivere aree proporzionali ai tempi con ottima approssimazione.**

**[S11.28]** Nella proposizione precedente è stato dimostrato il caso in cui più moti si compiono esattamente in ellissi. Quanto più la legge delle forze si allontana dalla legge lì posta, tanto più i corpi perturberanno i moti l’uno dell’altro; e non è possibile che corpi che si attraggono a vicenda secondo la legge qui posta si muovano esattamente in ellissi, se non mantenendo una certa proporzione delle distanze fra loro. Nei casi seguenti, però, non ci si allontanerà molto dalle ellissi.

**[S11.29]** Caso 1. Supponi che più corpi minori ruotino attorno a uno massimo, a distanze diverse da esso, e che verso ciascuno tendano forze assolute proporzionali agli stessi corpi. E poiché il centro comune di gravità di tutti (per il Cor. IV delle leggi) o è in quiete o si muove uniformemente in linea retta, immaginiamo che i corpi minori siano tanto piccoli che il corpo massimo non disti mai sensibilmente da questo centro: quel massimo o sarà in quiete o si muoverà uniformemente in linea retta, senza errore sensibile; e i minori ruoteranno attorno a questo massimo in ellissi e, con raggi condotti a esso, descriveranno aree proporzionali ai tempi, se non in quanto si introducono errori o per lo scostamento del massimo da quel centro comune di gravità o per le azioni dei corpi minori l’uno sull’altro. Ma i corpi minori si possono diminuire finché quello scostamento e le azioni reciproche siano minori di qualunque quantità data, e quindi finché le orbite coincidano con le ellissi e le aree corrispondano ai tempi senza un errore che non sia minore di qualunque quantità data. C.V.M.

**[S11.30]** Caso 2. Immaginiamo ora che un sistema di corpi minori, che ruotano nel modo ora descritto attorno al massimo, o qualsiasi altro sistema di due corpi che ruotano l’uno attorno all’altro, avanzi uniformemente in linea retta e intanto sia sollecitato lateralmente dalla forza di un altro corpo di gran lunga maggiore, posto a grande distanza. E poiché forze acceleratrici uguali, con cui i corpi sono sollecitati lungo linee parallele, non mutano le posizioni reciproche dei corpi, ma fanno sì che il sistema intero sia trasportato tutto insieme, conservando i moti delle parti fra loro, è manifesto che dalle attrazioni verso il corpo massimo non nascerà assolutamente alcun cambiamento del moto dei corpi attratti fra loro, se non o dalla disuguaglianza delle attrazioni acceleratrici o dall’inclinazione reciproca delle linee lungo le quali avvengono le attrazioni. Supponi dunque che tutte le attrazioni acceleratrici verso il corpo massimo stiano fra loro inversamente come i quadrati delle distanze; e, aumentando la distanza del corpo massimo finché le differenze delle rette condotte da esso agli altri, rispetto alla loro lunghezza, e le loro inclinazioni reciproche siano minori di qualunque quantità data, i moti delle parti del sistema fra loro continueranno senza errori che non siano minori di qualunque quantità data. E poiché, per la piccolissima distanza di quelle parti fra loro, il sistema intero è attratto come un corpo solo, esso sarà mosso da questa attrazione come un corpo solo: cioè, con il suo centro di gravità, descriverà attorno al corpo massimo una sezione conica (cioè un’iperbole o una parabola se l’attrazione è debole, un’ellisse se è più forte) e, con un raggio condotto al massimo, descriverà aree proporzionali ai tempi, senza errori se non quelli che possono produrre le distanze delle parti, che sono certo piccolissime e si possono diminuire a piacere. C.V.M.

**[S11.31]** Con un argomento simile si può procedere all’infinito a casi più complessi.

**[S11.32]** Cor. 1. Nel secondo caso, quanto più il corpo massimo di tutti si avvicina al sistema di due o più corpi, tanto più saranno perturbati i moti delle parti del sistema fra loro, perché ora è maggiore l’inclinazione reciproca delle linee condotte dal corpo massimo verso di esse, e maggiore la disuguaglianza della proporzione.

**[S11.33]** Cor. 2. Saranno però perturbati al massimo se si suppone che le attrazioni acceleratrici delle parti del sistema verso il corpo massimo di tutti non stiano fra loro inversamente come i quadrati delle distanze da quel corpo massimo; soprattutto se la disuguaglianza di questa proporzione è maggiore della disuguaglianza della proporzione delle distanze dal corpo massimo. Se infatti la forza acceleratrice, agendo in egual misura e lungo linee parallele, non perturba affatto i moti fra loro, è necessario che la perturbazione nasca dalla disuguaglianza dell’azione, e che sia maggiore o minore secondo che la disuguaglianza è maggiore o minore. L’eccesso delle spinte maggiori, agendo su alcuni corpi e non agendo su altri, muterà necessariamente la loro posizione reciproca. E questa perturbazione, aggiunta a quella che nasce dall’inclinazione e dalla disuguaglianza delle linee, renderà maggiore la perturbazione totale.

**[S11.34]** Cor. 3. Perciò, se le parti di questo sistema si muovono in ellissi o in cerchi senza perturbazioni notevoli, è manifesto che esse o non sono sollecitate, se non debolissimamente, da forze acceleratrici dirette verso altri corpi, oppure sono sollecitate in egual misura e lungo linee parallele con ottima approssimazione.

### Proposizione LXVI. Teorema XXVI (il problema dei tre corpi)

**[S11.35]** **Se tre corpi, le cui forze decrescono in rapporto duplicato delle distanze, si attraggono a vicenda, e le attrazioni acceleratrici di due qualsiasi verso il terzo stanno fra loro inversamente come i quadrati delle distanze, e i minori ruotano attorno al massimo, dico che il più interno, con raggi condotti al più interno e massimo, descriverà attorno a esso aree più proporzionali ai tempi, e una figura più vicina alla forma di un’ellisse che ha il fuoco nel punto d’incontro dei raggi, se il corpo massimo è agitato da queste attrazioni, che se quel massimo o, non attratto dai minori, fosse in quiete, o, attratto molto meno o molto più, fosse agitato molto meno o molto più.**

**[S11.36]** Ciò risulta quasi evidente dalla dimostrazione del Cor. 2 della proposizione precedente; ma con un argomento più distinto e di portata più generale lo si prova così.

**[S11.37]** Caso 1. Ruotino i corpi minori P e S nello stesso piano attorno al massimo T: P descriva l’orbita interna PAB, e S l’orbita esterna ESE. Sia SK la distanza media dei corpi P e S; e l’attrazione acceleratrice del corpo P verso S, a quella distanza media, sia rappresentata dalla stessa SK. Si prenda SL che stia a SK in rapporto duplicato di SK a SP: SL sarà l’attrazione acceleratrice del corpo P verso S a una distanza qualsiasi SP. Congiungi PT, e conduci a essa la parallela LM, che incontri ST in M: l’attrazione SL si scomporrà (per il Cor. II delle leggi) nelle attrazioni SM, LM. E così il corpo P sarà sollecitato da una triplice forza acceleratrice. Una forza tende a T e nasce dall’attrazione reciproca dei corpi T e P. Per effetto di questa sola forza il corpo P dovrebbe descrivere attorno al corpo T, sia esso immobile o agitato da questa attrazione, sia aree proporzionali ai tempi con il raggio PT, sia un’ellisse che ha il fuoco nel centro del corpo T. Ciò risulta dalla Prop. XI e dai Cor. 2 e 3 del Teor. XXI. La seconda forza è quella dell’attrazione LM, che, poiché tende da P a T, sovrapposta alla prima forza coinciderà con essa, e così farà sì che le aree siano descritte ancora proporzionali ai tempi, per il Cor. 3 del Teor. XXI. Ma poiché non è inversamente proporzionale al quadrato della distanza PT, essa comporrà con la prima forza una forza che si scosta da questa proporzione, e tanto più quanto maggiore è il rapporto di questa forza alla prima, a parità di altre condizioni. Perciò, poiché (per la Prop. XI e per il Cor. 2 del Teor. XXI) la forza con cui l’ellisse è descritta attorno al fuoco T deve tendere a quel fuoco ed essere inversamente proporzionale al quadrato della distanza PT, quella forza composta, scostandosi da questa proporzione, farà sì che l’orbita PAB si scosti dalla forma di un’ellisse che ha il fuoco in T; e tanto più quanto maggiore è lo scostamento da questa proporzione, e quindi anche quanto maggiore è il rapporto della seconda forza LM alla prima, a parità di altre condizioni. Ora la terza forza SM, attraendo il corpo P lungo una linea parallela a ST, comporrà con le forze precedenti una forza che non è più diretta da P verso T, e che da questa direzione si scosta tanto più quanto maggiore è il rapporto di questa terza forza alle forze precedenti, a parità di altre condizioni; e che perciò farà sì che il corpo P, con il raggio TP, descriva aree non più proporzionali ai tempi, e che lo scostamento da questa proporzionalità sia tanto maggiore quanto maggiore è il rapporto di questa terza forza alle altre. Questa terza forza, poi, accrescerà lo scostamento dell’orbita PAB dalla suddetta forma ellittica per una duplice ragione: sia perché non è diretta da P verso T, sia perché non è inversamente proporzionale al quadrato della distanza PT. Comprese queste cose, è manifesto che le aree sono massimamente proporzionali ai tempi quando la terza forza, restando invariate le altre, è minima; e che l’orbita PAB si avvicina massimamente alla suddetta forma ellittica quando sia la seconda sia la terza forza, ma soprattutto la terza, sono minime, restando invariata la prima.

**[S11.38]** Si rappresenti con la linea SN l’attrazione acceleratrice del corpo T verso S. Se le attrazioni acceleratrici SM, SN fossero uguali, esse, attraendo i corpi T e P in egual misura e lungo linee parallele, non muterebbero affatto la loro posizione reciproca. I moti di quei corpi fra loro sarebbero allora gli stessi (per il Cor. VI delle leggi) che se queste attrazioni fossero tolte. E, per la stessa ragione, se l’attrazione SN fosse minore dell’attrazione SM, toglierebbe dall’attrazione SM la parte SN, e resterebbe la sola parte MN, dalla quale sarebbero perturbate la proporzionalità dei tempi e delle aree e quella forma ellittica dell’orbita. E similmente, se l’attrazione SN fosse maggiore dell’attrazione SM, dalla sola differenza MN nascerebbe la perturbazione della proporzionalità e dell’orbita. Così, per mezzo dell’attrazione SN, la terza attrazione suddetta, SM, si riduce sempre all’attrazione MN, mentre la prima e la seconda attrazione restano del tutto immutate; e perciò le aree e i tempi si avvicinano massimamente alla proporzionalità, e l’orbita PAB alla suddetta forma ellittica, quando l’attrazione MN o è nulla o è la minima possibile; cioè quando le attrazioni acceleratrici dei corpi P e T, dirette verso il corpo S, si avvicinano quanto più è possibile all’uguaglianza; cioè quando l’attrazione SN non è nulla, né minore della minima di tutte le attrazioni SM, ma è quasi media fra la massima e la minima di tutte le attrazioni SM, cioè non molto maggiore né molto minore dell’attrazione SK. C.V.D.

**[S11.39]** Caso 2. Ruotino ora i corpi minori P, S attorno al massimo T in piani diversi. La forza LM, agendo lungo la linea PT, situata nel piano dell’orbita PAB, avrà lo stesso effetto di prima, e non sposterà il corpo P dal piano della sua orbita. Ma l’altra forza, NM, agendo lungo una linea parallela a ST (e quindi inclinata sul piano dell’orbita PAB quando il corpo S si trova fuori della linea dei nodi), oltre alla perturbazione del moto in longitudine già esposta, introdurrà una perturbazione del moto in latitudine, traendo il corpo P fuori del piano della sua orbita. E questa perturbazione, in una qualsiasi posizione reciproca data dei corpi P e T, sarà come la forza MN che la genera, e perciò diverrà minima quando MN è minima, cioè (come ho già esposto) quando l’attrazione SN non è molto maggiore né molto minore dell’attrazione SK. C.V.D.

#### Corollari della Prop. LXVI

**[S11.40]** Cor. 1. Di qui si ricava facilmente che, se più corpi minori P, S, R ecc. ruotano attorno al massimo T, il moto del corpo più interno P sarà perturbato il meno possibile dalle attrazioni dei corpi esterni quando il corpo massimo T è attratto e agitato dagli altri, in proporzione alle forze acceleratrici, nella stessa misura in cui gli altri lo sono fra loro.

**[S11.41]** Cor. 2. In un sistema di tre corpi T, P, S, se le attrazioni acceleratrici di due qualsiasi verso il terzo stanno fra loro inversamente come i quadrati delle distanze, il corpo P, con il raggio PT, descriverà l’area attorno al corpo T più velocemente presso la congiunzione A e l’opposizione B che presso le quadrature C, D. Infatti ogni forza da cui il corpo P è sollecitato e il corpo T non lo è, e che non agisce lungo la linea PT, accelera o ritarda la descrizione dell’area secondo che è diretta in conseguenza o in antecedenza. Tale è la forza NM. Nel passaggio del corpo P da C ad A essa tende in conseguenza e accelera il moto; poi, fino a D, in antecedenza, e ritarda il moto; quindi in conseguenza fino a B, e infine in antecedenza nel passare da B a C.

**[S11.42]** Cor. 3. E con lo stesso argomento risulta evidente che il corpo P, a parità di altre condizioni, si muove più velocemente nella congiunzione e nell’opposizione che nelle quadrature.

**[S11.43]** Cor. 4. L’orbita del corpo P, a parità di altre condizioni, è più curva nelle quadrature che nella congiunzione e nell’opposizione. I corpi più veloci, infatti, deviano meno dal percorso rettilineo. E inoltre la forza KL, o NM, nella congiunzione e nell’opposizione è contraria alla forza con cui il corpo T attrae il corpo P, e quindi diminuisce quella forza; e il corpo P devierà meno dal percorso rettilineo dove è sollecitato meno verso il corpo T.

**[S11.44]** Cor. 5. Perciò il corpo P, a parità di altre condizioni, si allontanerà di più dal corpo T nelle quadrature che nella congiunzione e nell’opposizione. Questo vale escludendo il moto dell’eccentricità. Se infatti l’orbita del corpo P è eccentrica, la sua eccentricità (come si mostrerà fra poco nel Cor. 9 di questa proposizione) diventerà massima quando le apsidi sono nelle sizigie; e di qui può accadere che il corpo P, giungendo all’apside superiore, disti di più dal corpo T nelle sizigie che nelle quadrature.

**[S11.45]** Cor. 6. Poiché la forza centripeta del corpo centrale T, con cui il corpo P è trattenuto nella sua orbita, è aumentata nelle quadrature per l’aggiunta della forza LM ed è diminuita nelle sizigie per la sottrazione della forza KL, e, per la grandezza della forza KL, è diminuita più di quanto sia aumentata; e poiché quella forza centripeta (per il Cor. 2 della Prop. IV) sta nel rapporto composto dal rapporto semplice del raggio TP, direttamente, e dal rapporto duplicato del tempo periodico, inversamente: è evidente che questo rapporto composto è diminuito dall’azione della forza KL; e quindi che il tempo periodico, se il raggio TP dell’orbita resta lo stesso, è aumentato, e precisamente nel rapporto subduplicato di quello in cui quella forza centripeta è diminuita; e che perciò, se questo raggio è aumentato o diminuito, il tempo periodico è aumentato di più, o diminuito di meno, che nel rapporto sesquiplicato di questo raggio (per il Cor. 6 della Prop. IV). Se quella forza del corpo centrale si indebolisse a poco a poco, il corpo P, attratto sempre meno, si allontanerebbe continuamente sempre di più dal centro T; e, al contrario, se quella forza aumentasse, si avvicinerebbe. Se dunque l’azione del corpo lontano S, con cui quella forza è diminuita, aumenta e diminuisce alternativamente, il raggio TP aumenterà e diminuirà insieme alternativamente; e il tempo periodico aumenterà e diminuirà nel rapporto composto dal rapporto sesquiplicato del raggio e dal rapporto subduplicato di quello in cui la forza centripeta del corpo centrale T è diminuita o aumentata per l’aumento o la diminuzione dell’azione del corpo lontano S.

**[S11.46]** Cor. 7. Dalle premesse segue anche che l’asse dell’ellisse descritta dal corpo P, ossia la linea delle apsidi, quanto al moto angolare avanza e retrocede alternativamente, ma tuttavia avanza di più, e per l’eccesso dell’avanzamento è portato in conseguenza. Infatti la forza con cui il corpo P è sollecitato verso il corpo T nelle quadrature, dove la forza MN si è annullata, è composta dalla forza LM e dalla forza centripeta con cui il corpo T attrae il corpo P. La prima forza, LM, se la distanza PT aumenta, aumenta all’incirca nello stesso rapporto di questa distanza, e la seconda decresce in rapporto duplicato; perciò la somma di queste forze decresce in un rapporto minore del duplicato della distanza PT, e quindi (per il Cor. 1 della Prop. XLV) fa sì che l’auge, ossia l’apside superiore, retroceda. Nella congiunzione e nell’opposizione, invece, la forza con cui il corpo P è sollecitato verso il corpo T è la differenza fra la forza con cui il corpo T attrae il corpo P e la forza KL; e questa differenza, poiché la forza KL aumenta con ottima approssimazione nel rapporto della distanza PT, decresce in un rapporto maggiore del duplicato della distanza PT, e perciò (per il Cor. 1 della Prop. XLV) fa sì che l’auge avanzi. Nei luoghi fra le sizigie e le quadrature il moto dell’auge dipende da entrambe le cause considerate congiuntamente, cosicché esso avanza o retrocede secondo l’eccesso dell’una o dell’altra. Poiché dunque la forza KL nelle sizigie è circa il doppio della forza LM nelle quadrature, l’eccesso sarà dalla parte della forza KL, e porterà l’auge in conseguenza. La verità di questo corollario e del precedente si capirà più facilmente immaginando che il sistema dei due corpi T, P sia circondato da ogni parte da più corpi S, S, S ecc., disposti sull’orbita ESE. Per le loro azioni, infatti, l’azione di T sarà diminuita da ogni parte e decrescerà in un rapporto più che duplicato della distanza.

**[S11.47]** Cor. 8. Poiché poi l’avanzamento o la retrocessione delle apsidi dipende dal decremento della forza centripeta, avvenuto in un rapporto maggiore o minore del duplicato della distanza TP, nel passaggio del corpo dall’apside inferiore all’apside superiore, come pure da un simile incremento nel ritorno all’apside inferiore, ed è perciò massimo dove il rapporto della forza nell’apside superiore alla forza nell’apside inferiore si allontana massimamente dal rapporto duplicato inverso delle distanze, è manifesto che le apsidi, quando si trovano nelle loro sizigie, per la forza sottrattiva KL, o NM − LM, avanzeranno più velocemente, e quando si trovano nelle loro quadrature retrocederanno più lentamente per la forza additiva LM. Per la lunga durata del tempo in cui continua la velocità dell’avanzamento o la lentezza della retrocessione, questa disuguaglianza diventa di gran lunga la maggiore.

**[S11.48]** Cor. 9. Se un corpo, per effetto di una forza inversamente proporzionale al quadrato della sua distanza da un centro, ruotasse attorno a questo centro in un’ellisse, e poi, nella discesa dall’apside superiore, o auge, all’apside inferiore, quella forza, per l’aggiunta continua di una forza nuova, aumentasse in un rapporto più che duplicato della distanza diminuita, è manifesto che il corpo, spinto sempre verso il centro dall’aggiunta continua di quella forza nuova, si piegherebbe verso questo centro più che se fosse sollecitato dalla sola forza crescente in rapporto duplicato della distanza diminuita; e perciò descriverebbe un’orbita interna all’orbita ellittica e nell’apside inferiore si avvicinerebbe al centro più di prima. Con l’aggiunta di questa forza nuova, dunque, l’orbita diventerà più eccentrica. Se ora la forza, nell’allontanarsi del corpo dall’apside inferiore verso l’apside superiore, decrescesse per gli stessi gradi per cui prima era cresciuta, il corpo tornerebbe alla distanza di prima; e perciò, se la forza decresce in un rapporto maggiore, il corpo, ora meno attratto, salirà a una distanza maggiore, e così l’eccentricità dell’orbita aumenterà ancora di più. Perciò, se il rapporto dell’incremento e del decremento della forza centripeta aumenta a ogni rivoluzione, l’eccentricità aumenterà sempre; e al contrario diminuirà se quel rapporto decresce. Ora, nel sistema dei corpi T, P, S, quando le apsidi dell’orbita PAB sono nelle quadrature, quel rapporto dell’incremento e del decremento è minimo, e diventa massimo quando le apsidi sono nelle sizigie. Se le apsidi sono poste nelle quadrature, il rapporto presso le apsidi è minore, e presso le sizigie maggiore, del duplicato delle distanze; e da quel rapporto maggiore nasce il moto diretto dell’auge, come si è già detto. Ma se si considera il rapporto dell’incremento o del decremento totale nel percorso fra le apsidi, esso è minore del duplicato delle distanze. La forza nell’apside inferiore sta alla forza nell’apside superiore in un rapporto minore del duplicato della distanza dell’apside superiore dal fuoco dell’ellisse alla distanza dell’apside inferiore dallo stesso fuoco; e, al contrario, quando le apsidi sono poste nelle sizigie, la forza nell’apside inferiore sta alla forza nell’apside superiore in un rapporto maggiore del duplicato delle distanze. Infatti le forze LM nelle quadrature, aggiunte alle forze del corpo T, compongono forze in un rapporto minore; e le forze KL nelle sizigie, sottratte alle forze del corpo T, lasciano forze in un rapporto maggiore. Il rapporto del decremento e dell’incremento totale nel passaggio fra le apsidi è dunque minimo nelle quadrature e massimo nelle sizigie; e perciò, nel passaggio delle apsidi dalle quadrature alle sizigie, aumenta continuamente e aumenta l’eccentricità dell’ellisse; e nel passaggio dalle sizigie alle quadrature diminuisce continuamente e diminuisce l’eccentricità.

**[S11.49]** Cor. 10. Per rendere ragione degli errori in latitudine, immaginiamo che il piano dell’orbita EST resti immobile. Dalla causa degli errori esposta sopra è manifesto che, delle forze NM, ML, che ne sono l’intera causa, la forza ML, agendo sempre nel piano dell’orbita PAB, non perturba mai i moti in latitudine; e che la forza NM, quando i nodi sono nelle sizigie, agendo anch’essa nello stesso piano dell’orbita, non perturba questi moti; quando invece sono nelle quadrature, li perturba al massimo e, traendo continuamente il corpo P fuori del piano della sua orbita, diminuisce l’inclinazione del piano nel passaggio del corpo dalle quadrature alle sizigie, e la aumenta di nuovo nel passaggio dalle sizigie alle quadrature. Ne segue che, quando il corpo si trova nelle sizigie, l’inclinazione diventa la minima di tutte, e torna all’incirca alla grandezza di prima quando il corpo giunge al nodo successivo. Se invece i nodi sono posti negli ottanti dopo le quadrature, cioè fra C e A, D e B, si capirà da quanto ora esposto che, nel passaggio del corpo P da uno dei nodi fino al novantesimo grado da esso, l’inclinazione del piano diminuisce continuamente; poi, nel passaggio per i 45 gradi successivi, fino alla quadratura più vicina, l’inclinazione aumenta; e in seguito, nel passaggio per altri 45 gradi, fino al nodo successivo, diminuisce di nuovo. L’inclinazione dunque diminuisce più di quanto aumenti, e perciò è sempre minore nel nodo successivo che nel precedente. E con un ragionamento simile l’inclinazione aumenta più di quanto diminuisca quando i nodi sono negli altri ottanti, fra A e D, B e C. L’inclinazione, quando i nodi sono nelle sizigie, è dunque la massima di tutte. Nel loro passaggio dalle sizigie alle quadrature essa diminuisce a ogni arrivo del corpo ai nodi, e diventa la minima di tutte quando i nodi sono nelle quadrature e il corpo nelle sizigie; poi cresce per gli stessi gradi per cui prima era decresciuta, e, quando i nodi giungono alle sizigie successive, torna alla grandezza iniziale.

**[S11.50]** Cor. 11. Poiché il corpo P, quando i nodi sono nelle quadrature, è tratto continuamente fuori del piano della sua orbita, e precisamente verso la parte di S nel suo passaggio dal nodo C, attraverso la congiunzione A, al nodo D, e verso la parte contraria nel passaggio dal nodo D, attraverso l’opposizione B, al nodo C, è manifesto che nel suo moto a partire dal nodo C il corpo si allontana continuamente dal primo piano CD della sua orbita, finché giunge al nodo successivo; e perciò in questo nodo, distando al massimo da quel primo piano CD, attraversa il piano dell’orbita EST non nell’altro nodo D di quel piano, ma in un punto che da lì piega verso la parte del corpo S, e che è quindi il nuovo luogo del nodo, spostato verso le parti anteriori. E con un argomento simile i nodi continueranno a retrocedere nel passaggio del corpo da questo nodo al nodo successivo. I nodi posti nelle quadrature, dunque, retrocedono continuamente; nelle sizigie, dove il moto in latitudine non è affatto perturbato, sono fermi; nei luoghi intermedi, partecipi dell’una e dell’altra condizione, retrocedono più lentamente; e perciò, sempre o retrogradi o stazionari, a ogni rivoluzione sono portati in antecedenza.

**[S11.51]** Cor. 12. Tutti gli errori descritti in questi corollari sono un po’ maggiori nella congiunzione dei corpi P, S che nella loro opposizione, e ciò per le maggiori forze generatrici NM e ML.

**[S11.52]** Cor. 13. E poiché le ragioni di questi corollari non dipendono dalla grandezza del corpo S, tutte le cose precedenti valgono anche quando si stabilisce che il corpo S abbia una grandezza tale che il sistema dei due corpi T e P ruoti attorno a esso. E, aumentato il corpo S e quindi aumentata la sua forza centripeta, dalla quale nascono gli errori del corpo P, tutti quegli errori, a parità di distanze, diventeranno maggiori in questo caso che nell’altro, in cui il corpo S ruota attorno al sistema dei corpi P e T.

**[S11.53]** Cor. 14. Poiché poi le forze NM, ML, quando il corpo S è lontano, stanno con ottima approssimazione come la forza SK e il rapporto di PT a ST considerati congiuntamente, cioè, se sono date sia la distanza PT sia la forza assoluta del corpo S, inversamente come ST³; e poiché quelle forze NM, ML sono le cause di tutti gli errori e gli effetti trattati nei corollari precedenti, è manifesto che tutti quegli effetti, restando invariato il sistema dei corpi T e P e mutando soltanto la distanza ST e la forza assoluta del corpo S, stanno con ottima approssimazione nel rapporto composto dal rapporto diretto della forza assoluta del corpo S e dal rapporto triplicato inverso della distanza ST. Perciò, se il sistema dei corpi T e P ruota attorno al corpo lontano S, quelle forze NM, ML e i loro effetti saranno (per i Cor. 2 e 6 della Prop. IV) inversamente in rapporto duplicato del tempo periodico. E di qui anche, se la grandezza del corpo S è proporzionale alla sua forza assoluta, quelle forze NM, ML e i loro effetti saranno direttamente come il cubo del diametro apparente del corpo lontano S visto dal corpo T, e viceversa. Questi rapporti sono infatti gli stessi del rapporto composto di sopra.

**[S11.54]** Cor. 15. E poiché, se, restando invariate la forma delle orbite ESE e PAB, le loro proporzioni e la loro inclinazione reciproca, ne muta la grandezza, e se le forze dei corpi S e T o restano le stesse o mutano in un rapporto dato qualsiasi, queste forze (cioè la forza del corpo T, con cui il corpo P è costretto a deviare dal percorso rettilineo nell’orbita PAB, e la forza del corpo S, con cui lo stesso corpo P è costretto a scostarsi da quell’orbita) agiscono sempre nello stesso modo e nella stessa proporzione, è necessario che tutti gli effetti siano simili e proporzionali, e proporzionali i tempi degli effetti; cioè che tutti gli errori lineari stiano come i diametri delle orbite, quelli angolari siano gli stessi di prima, e i tempi degli errori lineari simili, o di quelli angolari uguali, stiano come i tempi periodici delle orbite.

**[S11.55]** Cor. 16. Perciò, se sono date le forme delle orbite e la loro inclinazione reciproca, e mutano in un modo qualsiasi le grandezze, le forze e le distanze dei corpi, dagli errori dati e dai tempi degli errori in un caso si possono ricavare gli errori e i tempi degli errori in qualunque altro, con ottima approssimazione; ma più brevemente con questo metodo. Le forze NM, ML, restando invariato il resto, stanno come il raggio TP, e i loro effetti periodici (per il Cor. 2 del Lemma X) stanno come le forze e il quadrato del tempo periodico del corpo P considerati congiuntamente. Questi sono gli errori lineari del corpo P; e di qui gli errori angolari visti dal centro T (cioè sia i moti dell’auge e dei nodi sia tutti gli errori apparenti in longitudine e in latitudine) stanno, in ogni rivoluzione del corpo P, come il quadrato del tempo della rivoluzione, con ottima approssimazione. Si congiungano questi rapporti con i rapporti del Cor. 14: in un qualsiasi sistema di corpi T, P, S, in cui P ruota attorno a T, a esso vicino, e T attorno a S, lontano, gli errori angolari del corpo P, visti dal centro T, staranno, in ciascuna rivoluzione di quel corpo P, come il quadrato del tempo periodico del corpo P, direttamente, e il quadrato del tempo periodico del corpo T, inversamente. E di qui il moto medio dell’auge starà in un rapporto dato al moto medio dei nodi; ed entrambi i moti staranno come il quadrato del tempo periodico del corpo P, direttamente, e il quadrato del tempo periodico del corpo T, inversamente. Aumentando o diminuendo l’eccentricità e l’inclinazione dell’orbita PAB, i moti dell’auge e dei nodi non mutano sensibilmente, se non quando quelle sono troppo grandi.

**[S11.56]** Cor. 17. Poiché poi la linea LM è ora maggiore ora minore del raggio PT, si rappresenti la forza media LM con quel raggio PT: essa starà alla forza media SK, o SN (che si può rappresentare con ST), come la lunghezza PT sta alla lunghezza ST. Ora la forza media SN, o ST, con cui il corpo T è trattenuto nella sua orbita attorno a S, sta alla forza con cui il corpo P è trattenuto nella sua orbita attorno a T nel rapporto composto dal rapporto del raggio ST al raggio PT e dal rapporto duplicato del tempo periodico del corpo P attorno a T al tempo periodico del corpo T attorno a S. E, per uguaglianza, la forza media LM sta alla forza con cui il corpo P è trattenuto nella sua orbita attorno a T (o con cui lo stesso corpo P, nello stesso tempo periodico, potrebbe ruotare attorno a un qualsiasi punto immobile T alla distanza PT) in quel rapporto duplicato dei tempi periodici. Dati dunque i tempi periodici insieme con la distanza PT, è data la forza media LM; e, data questa, è data anche la forza MN, con ottima approssimazione, per l’analogia delle linee PT, MN.

**[S11.57]** Cor. 18. Con le stesse leggi con cui il corpo P ruota attorno al corpo T, immaginiamo che più corpi fluidi si muovano attorno allo stesso T a distanze uguali da esso; poi che, divenuti contigui, si fondano in un anello fluido, rotondo e concentrico al corpo T: le singole parti dell’anello, compiendo tutti i loro moti secondo la legge del corpo P, si avvicineranno di più al corpo T, e si muoveranno più velocemente, nella congiunzione e nell’opposizione fra esse e il corpo S che nelle quadrature. E i nodi di questo anello, ossia le sue intersezioni con il piano dell’orbita del corpo S o T, saranno fermi nelle sizigie; fuori delle sizigie si muoveranno invece in antecedenza, e più velocemente nelle quadrature, più lentamente negli altri luoghi. Anche l’inclinazione dell’anello varierà, e il suo asse oscillerà a ogni rivoluzione e, compiuta la rivoluzione, tornerà alla posizione primitiva, se non in quanto è portato in giro dalla precessione dei nodi.

**[S11.58]** Cor. 19. Immagina ora che il globo del corpo T, costituito di materia non fluida, si ampli e si estenda fino a questo anello, e che, scavato lungo la circonferenza un canale, contenga acqua e ruoti uniformemente attorno al proprio asse con lo stesso moto periodico. Questo liquido, accelerato e ritardato alternativamente (come nel corollario precedente), sarà più veloce della superficie del globo nelle sizigie, più lento nelle quadrature, e così scorrerà nel canale e rifluirà a modo di mare. L’acqua, ruotando attorno al centro del globo in quiete, se si toglie l’attrazione del corpo S, non acquisterà alcun moto di flusso e riflusso. Lo stesso vale per un globo che avanzi uniformemente in linea retta e intanto ruoti attorno al proprio centro (per il Cor. V delle leggi), come pure per un globo tratto uniformemente fuori del suo corso rettilineo (per il Cor. VI delle leggi). Si avvicini però il corpo S, e per la sua attrazione non uniforme l’acqua sarà subito turbata. Sarà infatti maggiore l’attrazione dell’acqua più vicina, minore quella dell’acqua più lontana. E la forza LM trarrà l’acqua verso il basso nelle quadrature e la farà discendere fino alle sizigie; e la forza KL la trarrà verso l’alto nelle sizigie, ne arresterà la discesa e la farà salire fino alle quadrature.

**[S11.59]** Cor. 20. Se ora l’anello diventa rigido e il globo si rimpicciolisce, cesserà il moto di flusso e riflusso; ma resteranno quel moto oscillatorio dell’inclinazione e la precessione dei nodi. Abbia il globo lo stesso asse dell’anello, compia i giri negli stessi tempi, lo tocchi dall’interno con la sua superficie e vi aderisca: partecipando al suo moto, la struttura formata da entrambi oscillerà e i nodi retrocederanno. Il globo, infatti, come si dirà fra poco, è indifferente a ricevere qualunque impressione. L’angolo massimo d’inclinazione dell’anello privato del globo si ha quando i nodi sono nelle sizigie. Di lì, nell’avanzare dei nodi verso le quadrature, esso tende a diminuire la sua inclinazione, e con questa tendenza imprime un moto all’intero globo. Il globo conserva il moto impresso finché l’anello, con una tendenza contraria, non toglie questo moto e ne imprime uno nuovo verso la parte contraria. E per questa ragione il moto massimo dell’inclinazione decrescente si ha nelle quadrature dei nodi, e l’angolo minimo d’inclinazione negli ottanti dopo le quadrature; poi il moto massimo di reclinazione nelle sizigie, e l’angolo massimo negli ottanti successivi. Lo stesso vale per un globo privo dell’anello che nelle regioni dell’equatore sia o un poco più alto che presso i poli o costituito di materia un poco più densa. Quell’eccesso di materia nelle regioni dell’equatore fa infatti le veci dell’anello. E benché, aumentata in qualsiasi modo la forza centripeta di questo globo, si supponga che tutte le sue parti tendano verso il basso, a modo delle parti gravi della Terra, tuttavia i fenomeni di questo corollario e del precedente ne saranno appena mutati, se non che i luoghi delle altezze massime e minime dell’acqua saranno diversi. L’acqua infatti ora si sostiene e permane nella sua orbita non per la sua forza centrifuga, ma per il canale in cui scorre. E inoltre la forza LM trae l’acqua verso il basso al massimo nelle quadrature, e la forza KL, o NM − LM, la trae verso l’alto al massimo nelle sizigie. E queste forze congiunte cessano di trarre l’acqua verso il basso e cominciano a trarla verso l’alto negli ottanti prima delle sizigie, e cessano di trarla verso l’alto e cominciano a trarla verso il basso negli ottanti dopo le sizigie. E di qui l’altezza massima dell’acqua può verificarsi all’incirca negli ottanti dopo le sizigie, e la minima negli ottanti dopo le quadrature; se non in quanto il moto di salita o di discesa impresso da queste forze o, per la forza insita dell’acqua, perseveri un po’ più a lungo, o, per gli impedimenti del canale, si arresti un po’ prima.

**[S11.60]** Cor. 21. Per la stessa ragione per cui la materia del globo sovrabbondante presso l’equatore fa sì che i nodi retrocedano, e perciò con il suo aumento questa retrocessione cresce, con la sua diminuzione diminuisce e con la sua rimozione si annulla, se si toglie più della materia sovrabbondante, cioè se il globo presso l’equatore è reso o più depresso o più rado che presso i poli, nascerà un moto dei nodi in conseguenza.

**[S11.61]** Cor. 22. E di qui, viceversa, dal moto dei nodi si conosce la costituzione del globo. Se cioè il globo conserva senza interruzione gli stessi poli e il moto avviene in antecedenza, la materia presso l’equatore sovrabbonda; se in conseguenza, manca. Supponi che un globo uniforme e perfettamente rotondo sia dapprima in quiete negli spazi liberi; poi che, per un impeto qualsiasi impresso obliquamente sulla sua superficie, sia spinto in avanti e ne riceva un moto in parte circolare, in parte in linea retta. Poiché questo globo si comporta in modo indifferente rispetto a tutti gli assi che passano per il suo centro, e non è più incline a un asse, o a una posizione dell’asse, che a un altro qualsiasi, è evidente che esso, con la propria forza, non muterà mai il suo asse né l’inclinazione dell’asse. Ora il globo sia spinto obliquamente, nella stessa parte della superficie di prima, da un nuovo impulso qualsiasi; e, poiché il fatto che l’impulso venga dato prima o dopo non ne muta affatto l’effetto, è manifesto che questi due impulsi, impressi successivamente, produrranno lo stesso moto che se fossero stati impressi insieme, cioè lo stesso che se il globo fosse stato spinto da una forza semplice composta da entrambi (per il Cor. II delle leggi), e quindi un moto semplice attorno a un asse di inclinazione data. E lo stesso vale per un secondo impulso dato in un altro luogo qualsiasi dell’equatore del primo moto, come pure per un primo impulso dato in un luogo qualsiasi dell’equatore del moto che il secondo impulso genererebbe senza il primo, e quindi per entrambi gli impulsi dati in luoghi qualsiasi: essi genereranno lo stesso moto circolare che se fossero stati impressi insieme e in una volta nel luogo d’intersezione degli equatori dei moti che genererebbero separatamente. Un globo omogeneo e perfetto, dunque, non conserva più moti distinti, ma compone tutti quelli impressi e li riduce a uno solo, e, per quanto sta in esso, gira sempre con un moto semplice e uniforme attorno a un unico asse, di inclinazione data e sempre invariabile. Ma neppure la forza centripeta può mutare l’inclinazione dell’asse o la velocità della rotazione. Se si immagina che il globo sia diviso in due emisferi da un piano qualsiasi passante per il suo centro e per il centro verso cui la forza è diretta, quella forza solleciterà sempre in egual misura l’uno e l’altro emisfero, e perciò non farà inclinare il globo da nessuna parte quanto al moto di rotazione. Si aggiunga invece in qualche luogo fra il polo e l’equatore della materia nuova, ammucchiata in forma di monte: questa, con la sua tendenza continua ad allontanarsi dal centro del suo moto, turberà il moto del globo e farà sì che i suoi poli vaghino sulla sua superficie e descrivano continuamente cerchi attorno a sé e al punto opposto. E questa smisuratezza del vagare non sarà corretta se non ponendo quel monte o in uno dei due poli, nel qual caso (per il Cor. 21) i nodi dell’equatore avanzeranno, o nell’equatore, nel qual modo (per il Cor. 20) i nodi retrocederanno, o infine aggiungendo dall’altra parte dell’asse della materia nuova con cui il monte sia equilibrato durante il moto; e in questo modo i nodi o avanzeranno o retrocederanno secondo che il monte e questa nuova materia siano più vicini al polo o all’equatore.

### Proposizione LXVII. Teorema XXVII (il corpo esterno attorno al centro comune dei due interni)

**[S11.62]** **Poste le stesse leggi delle attrazioni, dico che il corpo esterno S, attorno al centro comune di gravità O dei corpi interni P, T, con raggi condotti a quel centro, descrive aree più proporzionali ai tempi, e un’orbita più vicina alla forma di un’ellisse che ha il fuoco nello stesso centro, di quanto possa descriverne attorno al corpo più interno e massimo T con raggi condotti a esso.**

**[S11.63]** Le attrazioni del corpo S verso T e verso P compongono infatti la sua attrazione assoluta, che è diretta verso il centro comune di gravità O dei corpi T e P più che verso il corpo massimo T, e che è inversamente proporzionale al quadrato della distanza SO più che al quadrato della distanza ST: come risulterà facilmente a chi consideri la cosa con attenzione.

### Proposizione LXVIII. Teorema XXVIII (il corpo esterno quando il corpo massimo è agitato)

**[S11.64]** **Poste le stesse leggi delle attrazioni, dico che il corpo esterno S, attorno al centro comune di gravità O dei corpi interni P e T, con raggi condotti a quel centro, descrive aree più proporzionali ai tempi, e un’orbita più vicina alla forma di un’ellisse che ha il fuoco nello stesso centro, se il corpo più interno e massimo è agitato da queste attrazioni come gli altri, che se esso o, non attratto, fosse in quiete, o, attratto molto più o molto meno, fosse agitato molto più o molto meno.**

**[S11.65]** Si dimostra quasi nello stesso modo della Prop. LXVI, ma con un argomento più lungo, che perciò tralascio. Basterà valutare la cosa così. Dalla dimostrazione dell’ultima proposizione risulta che il centro verso cui il corpo S è sollecitato dalle forze congiunte è vicinissimo al centro comune di gravità di quei due corpi. Se questo centro coincidesse con quel centro comune, e il centro comune di gravità dei tre corpi fosse in quiete, il corpo S da una parte e il centro comune degli altri due dall’altra descriverebbero ellissi esatte attorno al centro comune di tutti, in quiete. Ciò risulta dal Cor. 2 della Prop. LVIII confrontato con quanto è stato dimostrato nelle Prop. LXIV e LXV. Questo moto ellittico è perturbato un poco dalla distanza del centro dei due corpi dal centro verso cui il terzo, S, è attratto. Si dia inoltre un moto al centro comune dei tre, e la perturbazione aumenterà. Perciò la perturbazione è minima quando il centro comune dei tre è in quiete, cioè quando il corpo più interno e massimo T è attratto secondo la legge degli altri; ed è sempre maggiore quando quel centro comune dei tre, per la diminuzione del moto del corpo T, comincia a muoversi, e poi è agitato sempre di più.

**[S11.66]** Cor. E di qui, se più corpi minori ruotano attorno al massimo, si può dedurre che le orbite descritte si avvicineranno di più alle ellittiche, e le descrizioni delle aree diverranno più uniformi, se tutti i corpi si attraggono e si agitano a vicenda con forze acceleratrici che stanno come le loro forze assolute, direttamente, e i quadrati delle distanze, inversamente, e il fuoco di ciascuna orbita è collocato nel centro comune di gravità di tutti i corpi più interni (cioè il fuoco della prima orbita, la più interna, nel centro di gravità del corpo massimo e più interno; quello della seconda orbita nel centro comune di gravità dei due corpi più interni; quello della terza nel centro comune di gravità dei tre più interni; e così via), che se il corpo più interno fosse in quiete e fosse stabilito come fuoco comune di tutte le orbite.

### Proposizione LXIX. Teorema XXIX (le forze assolute stanno come i corpi)

**[S11.67]** **In un sistema di più corpi A, B, C, D ecc., se un corpo A attrae tutti gli altri B, C, D ecc. con forze acceleratrici che sono inversamente come i quadrati delle distanze da quello che attrae, e un altro corpo B attrae anch’esso gli altri A, C, D ecc. con forze che sono inversamente come i quadrati delle distanze da quello che attrae, le forze assolute dei corpi che attraggono, A e B, staranno fra loro come gli stessi corpi A, B di cui sono le forze.**

**[S11.68]** Infatti le attrazioni acceleratrici di tutti i corpi B, C, D verso A, a parità di distanze, sono uguali fra loro per ipotesi; e similmente sono uguali fra loro, a parità di distanze, le attrazioni acceleratrici di tutti i corpi verso B. Ora la forza assoluta attrattiva del corpo A sta alla forza assoluta attrattiva del corpo B come l’attrazione acceleratrice di tutti i corpi verso A sta all’attrazione acceleratrice di tutti i corpi verso B, a parità di distanze; e così sta l’attrazione acceleratrice del corpo B verso A all’attrazione acceleratrice del corpo A verso B. Ma l’attrazione acceleratrice del corpo B verso A sta all’attrazione acceleratrice del corpo A verso B come la massa del corpo A sta alla massa del corpo B, perché le forze motrici, che (per le Definizioni II, VII e VIII) stanno come le forze acceleratrici e i corpi attratti considerati congiuntamente, sono qui (per la terza legge del moto) uguali fra loro. Dunque la forza assoluta attrattiva del corpo A sta alla forza assoluta attrattiva del corpo B come la massa del corpo A sta alla massa del corpo B. C.V.D.

**[S11.69]** Cor. 1. Di qui, se i singoli corpi del sistema A, B, C, D ecc., considerati separatamente, attraggono tutti gli altri con forze acceleratrici che sono inversamente come i quadrati delle distanze da quello che attrae, le forze assolute di tutti quei corpi staranno fra loro come gli stessi corpi.

**[S11.70]** Cor. 2. Con lo stesso argomento, se i singoli corpi del sistema A, B, C, D ecc., considerati separatamente, attraggono tutti gli altri con forze acceleratrici che sono o inversamente o direttamente nel rapporto di una potenza qualsiasi delle distanze da quello che attrae, o che sono definite dalle distanze da ciascun corpo che attrae secondo una qualsiasi legge comune, risulta che le forze assolute di quei corpi stanno come i corpi.

**[S11.71]** Cor. 3. In un sistema di corpi le cui forze decrescono in rapporto duplicato delle distanze, se i minori ruotano attorno al massimo in ellissi quanto più possibile esatte, che hanno il fuoco comune nel centro di quel massimo, e con raggi condotti a quel massimo descrivono aree quanto più possibile proporzionali ai tempi, le forze assolute di quei corpi staranno fra loro, o esattamente o con ottima approssimazione, nel rapporto dei corpi; e viceversa. Ciò risulta dal Cor. della Prop. LXVIII confrontato con il Cor. 1 di questa.

### Scolio

**[S11.72]** Da queste proposizioni siamo condotti per mano all’analogia fra le forze centripete e i corpi centrali verso cui quelle forze sogliono essere dirette. È infatti conforme a ragione che le forze dirette verso i corpi dipendano dalla natura e dalla quantità di questi, come accade nei fenomeni magnetici. E ogni volta che si presentano casi di questo genere, si dovranno valutare le attrazioni dei corpi assegnando a ciascuna delle loro particelle le forze proprie e raccogliendo le somme delle forze. Uso qui la parola «attrazione» in senso generale, per qualunque tendenza dei corpi ad avvicinarsi gli uni agli altri: sia che questa tendenza nasca dall’azione dei corpi che si dirigono gli uni verso gli altri o che si agitano a vicenda per mezzo di spiriti emessi, sia che nasca dall’azione dell’etere, o dell’aria, o di un mezzo qualsiasi, corporeo o incorporeo, che spinga in qualche modo gli uni verso gli altri i corpi che vi sono immersi. Nello stesso senso generale uso la parola «spinta», considerando in questo trattato non le specie delle forze e le qualità fisiche, ma le quantità e le proporzioni matematiche, come ho spiegato nelle definizioni. Nella matematica si devono indagare le quantità delle forze e quei rapporti che conseguono da condizioni qualsiasi poste; poi, quando si scende alla fisica, questi rapporti si devono confrontare con i fenomeni, perché si conosca quali condizioni delle forze competano a ciascun genere di corpi attrattivi. E soltanto allora si potrà disputare con maggiore sicurezza sulle specie, sulle cause e sulle ragioni fisiche delle forze. Vediamo dunque con quali forze debbano agire l’uno sull’altro corpi sferici costituiti di particelle attrattive nel modo ora esposto, e quali moti ne conseguano.

**Fine della Sezione XI. Nel testo originale segue la Sezione XII, *De corporum sphæricorum viribus attractivis*.**

---

## Apparato

### A.0 Estensioni del glossario

I termini seguenti non comparivano nel glossario comune o richiedono una precisazione. Ognuno è reso in modo costante in tutto il fascicolo.

| Latino | Italiano | Motivazione |
|---|---|---|
| *se mutuo petere* (titolo; Scolio) | «dirigersi gli uni verso gli altri» | *petere* è «cercare, dirigersi verso»; la resa evita di decidere fra attrazione e spinta, come chiede lo Scolio finale. Motte: «tending to each other». |
| *trahere*, *attrahere* | «attrarre»; *trahere de tangentibus*, *de plano*: «trarre dalle tangenti», «trarre fuori del piano» | Newton usa i due verbi come sinonimi; quando il verbo indica lo spostamento prodotto (non la forza), «trarre» conserva l’immagine. |
| *agitare*, *agitari* | «agitare», «essere agitato» | Nella Sezione XI significa «mettere in moto, far muovere» un corpo per effetto delle attrazioni (Prop. LXVI, LXVIII). Il termine storico è conservato e spiegato in nota (N9). |
| *revolvi*, *gyrari*, *circumagi* | «ruotare», «girare», «rotazione» | Distinzione lessicale del latino mantenuta dove possibile; il senso è lo stesso (moto orbitale). |
| *medie proportionales* | «medie proporzionali» | Termine euclideo: x e y sono le due medie proporzionali fra a e b se a : x = x : y = y : b (nota N4). |
| *mediocris* (*distantia*, *vis*) | «media» | Valore medio lungo l’orbita, non «mediocre». |
| *syzygiæ*, *conjunctio*, *oppositio*, *quadraturæ*, *octantes* | «sizigie», «congiunzione», «opposizione», «quadrature», «ottanti» | Lessico astronomico tradizionale, ancora in uso. Le posizioni sono definite dall’angolo fra P e S visto da T: 0° congiunzione, 180° opposizione, 90° e 270° quadrature, i multipli dispari di 45° ottanti (nota N10). |
| *nodi*, *linea nodorum* | «nodi», «linea dei nodi» | Intersezioni dell’orbita di P con il piano dell’orbita di S (o di T). |
| *aux*, *apsis summa*, *apsis ima*, *apsidum linea* | «auge», «apside superiore», «apside inferiore», «linea delle apsidi» | *Aux* è il termine medievale per l’apside più lontana; Newton lo glossa con *apsis summa*. «Superiore / inferiore» traducono *summa / ima* nel senso della distanza dal centro. *Apside* è usato al femminile. |
| *motus in longitudinem / in latitudinem* | «moto in longitudine / in latitudine» | Lessico astronomico: componenti nel piano dell’orbita e fuori di esso. |
| *errores* | «errori» | Nel linguaggio astronomico dell’epoca sono le disuguaglianze, cioè gli scostamenti dal moto kepleriano; si conserva il termine (nota N10). |
| *errores lineares / angulares* | «errori lineari / angolari» | Scostamenti misurati come lunghezze o come angoli visti dal centro (Cor. 15–16). |
| *inclinatio*, *reclinatio* | «inclinazione», «reclinazione» | *Reclinatio* (Cor. 20) è il moto che riporta l’inclinazione a crescere dopo il minimo; si conserva il termine e lo si spiega in nota (N16). |
| *vis ablatitia / addititia* | «forza sottrattiva / additiva» | Cor. 8: la forza che si sottrae (KL) o si aggiunge (LM) alla forza centripeta di T. |
| *annulus*, *alveus*, *fluxus & refluxus*, *compages* | «anello», «canale», «flusso e riflusso», «struttura» | Cor. 18–20. *Compages utriusque* è l’insieme rigido formato da globo e anello. |
| *præcessio nodorum* | «precessione dei nodi» | Termine conservato; in questa sezione il moto è retrogrado (nota N16). |
| *cæteris paribus* | «a parità di altre condizioni» | Motte lascia il latino. |
| *quam proxime*, *quamproxime* | «con ottima approssimazione» | Come nel Fascicolo 3. |
| *datis quibusvis minores* | «minori di qualunque quantità data» | Formula dei rapporti ultimi (Sezione I). |
| *rectus trames* | «percorso rettilineo» | Cor. 4 e 15. |
| *vis absoluta attractiva* | «forza assoluta attrattiva» | Prop. LXIX; estensione di «forza assoluta» (Def. VI). |
| *mutatio motus … inter se* (Prop. LXV, Caso 2) | «cambiamento del moto … fra loro» | Qui *motus* indica i moti relativi delle parti del sistema, non una grandezza: non si applica la resa «cambiamento della quantità di moto», come per i *motus inter se* del Cor. V delle leggi (Fascicolo 3). |
| *impulsus* | «spinta» (S11.01, S11.33, S11.72); «impulso» (S11.61) | «Spinta» dove Newton contrappone attrazione e spinta come modi di parlare della forza (proemio e Scolio), in coerenza con la Def. VIII del Fascicolo 1 («le attrazioni e le spinte»), e nel Cor. 2 della Prop. LXV. «Impulso» nel Cor. 22 della Prop. LXVI, dove si tratta di un’azione istantanea che cambia il moto del globo (eccezione prevista dal glossario). *Impetus quocunque* (S11.61) è «un impeto qualsiasi». |
| *constanter* (S11.61) | «senza interruzione» | Applicazione della resa fissata per il Lemma I. |
| *in anteriora vergens* (S11.50) | «spostato verso le parti anteriori» | Resa letterale; dal contesto il nuovo nodo cade contro il verso del moto, cioè *in antecedentia*, come rende Motte (nota N15). |
| *in consequentia / in antecedentia* | «in conseguenza / in antecedenza» | Glossario comune; spiegazione alla prima occorrenza nella nota N11. |
| *spiritus emissi* (Scolio) | «spiriti emessi» | Termine della filosofia naturale del Seicento (effluvi sottili); si conserva. |

### A.1 Proemio e titolo della Sezione

**Latino (titolo):** *De motu corporum viribus centripetis se mutuo petentium.*

**Inglese:** “Of the motions of bodies tending to each other with centripetal forces.”

**Scelte.**

- *quale tamen vix extat in rerum natura* è reso «quale tuttavia difficilmente esiste in natura». Motte rafforza: «though very probably there is no such thing existent in nature».
- *neque attrahens possit quiescere neque attractum* è reso con il modale: «né quello che attrae né quello attratto possono essere in quiete». Motte rende con un indicativo e un avverbio: «is truly at rest».
- *verius dicantur impulsus*: «sarebbe più corretto chiamarle spinte» (§ A.0). Motte: «impulses».
- *In mathematicis enim jam versamur* è reso «ci occupiamo infatti ora di matematica». Motte parafrasa: «But these propositions are to be considered as purely mathematical».

### A.2 Prop. LVII

**Latino:** *Corpora duo se invicem trahentia describunt, & circum commune centrum gravitatis, & circum se mutuo, figuras similes.*

**Inglese:** “Two bodies attracting each other mutually describe similar figures about their common centre of gravity, and about each other mutually.”

**Scelte.** *Terminus communis* è «estremo comune»: il centro di gravità C è l’estremo comune dei due segmenti CS e CP, che giacciono sulla stessa retta. *Motu quovis non angulari* è reso «di un moto qualsiasi non angolare», cioè di pura traslazione. Nessuna divergenza rilevante di Motte. La proposizione non ha figura nella trascrizione e non entra nella Parte B.

### A.3 Prop. LVIII

**Latino:** *Si corpora duo Viribus quibusvis se mutuo trahunt, & interea revolvuntur circa gravitatis centrum commune: dico quod figuris, quas corpora sic mota describunt circum se mutuo, potest figura similis & æqualis, circum corpus alterutrum immotum, viribus iisdem describi.*

**Inglese:** “If two bodies attract each other mutually with forces of any kind, and in the mean time revolve about the common centre of gravity; I say, that, by the same forces, there may be described round either body unmoved a figure similar and equal to the figures which the bodies so moving describe round each other mutually.”

**Scelte.**

- *Viribus* con la maiuscola è una particolarità della trascrizione, senza conseguenze.
- *pergendo de S ad T, deque P ad Q*: S e T, P e Q sono posizioni successive dei due corpi; T qui non è il corpo T della Prop. LXVI.
- Nella frase finale del Caso 1, *qui sunt in ratione integra* è reso «che stanno nel rapporto semplice [delle distanze]»: *integra* si oppone a *subduplicata*. L’integrazione fra parentesi quadre è del curatore; Motte rende «which are in a simple proportion to each other».
- **Aggiunta di Motte:** «this last force **(tending to s)**».
- **Trascrizione:** *unifor <163> miter* (Caso 2) è la parola *uniformiter* spezzata dal marcatore di pagina.
- **Rimando da verificare.** Nel Caso 2 il latino cita *legum corollarium sextum*; per uno spazio che avanza uniformemente in linea retta ci si aspetterebbe il Cor. V (moti in uno spazio in moto uniforme), mentre il Cor. VI riguarda forze acceleratrici uguali e parallele. Motte ha anch’egli «Cor. 6». La traduzione conserva il rimando del testo; il punto va controllato sulla stampa del 1726.

### A.4 Prop. LIX

**Latino:** *Corporum duorum S & P, circa commune gravitatis centrum C revolventium, tempus periodicum esse ad tempus periodicum corporis alterutrius P, circa alterum immotum S gyrantis, & figuris, quæ corpora circum se mutuo describunt, figuram similem & æqualem describentis, in subduplicata ratione corporis alterius S, ad summam corporum S+P.*

**Inglese:** “The periodic time of two bodies S and P revolving round their common centre of gravity C, is to the periodic time of one of the bodies P revolving round the other S remaining unmoved, and describing a figure similar and equal to those which the bodies describe about each other mutually, in a subduplicate ratio of the other body S to the sum of the bodies S + P.”

**Scelte.** L’enunciato è in accusativo e infinito ed è reso all’indicativo. Nessuna divergenza di Motte. Verifica numerica in N3.

### A.5 Prop. LX

**Latino:** *Si corpora duo S & P, viribus quadrato distantiæ suæ reciproce proportionalibus, se mutuo trahentia, revoluntur circa gravitatis centrum commune: dico quod ellipseos, quam corpus alterutrum P hoc motu circa alterum S describit, axis principalis erit ad axem principalem ellipseos, quam corpus idem P circa alterum quiescens S eodem tempore periodico describere posset, ut summa corporum duorum S+P ad primum duorum medie proportionalium inter hanc summan & corpus illud alterum S.*

**Inglese:** “If two bodies S and P, attracting each other with forces reciprocally proportional to the squares of their distance, revolve about their common centre of gravity; I say, that the principal axis of the ellipsis which either of the bodies, as P, describes by this motion about the other S, will be to the principal axis of the ellipsis, which the same body P may describe in the same periodical time about the other body S quiescent, as the sum of the two bodies S + P to the first of two mean proportionals between that sum and the other body S.”

**Scelte e trascrizione.**

- *revoluntur* è un refuso probabile della trascrizione per *revolvuntur*, da verificare sulla stampa.
- *hanc summan* è un refuso probabile della trascrizione per *hanc summam*, da verificare sulla stampa.
- *in ratione, cujus hæc est sesquiplicata* è reso «in un rapporto di cui questo è il sesquiplicato»: il rapporto degli assi è quello la cui potenza 3/2 dà il rapporto dei tempi (nota N4).

### A.6 Prop. LXI

**Latino:** *Si corpora duo viribus quibusvis se mutuo trahentia, neque alias agitata vel impedita, quomodocunque moveantur; motus eorum perinde se habebunt, ac si non traherent se mutuo, sed utrumque a corpore tertio in communi gravitatis centro constituto viribus iisdem traheretur: Et virium trahentium eadem erit lex respectu distantiæ corporum a centro illo communi atque respectu distantiæ totius inter corpora.*

**Inglese:** “If two bodies attracting each other with any kind of forces, and not otherwise agitated or obstructed, are moved in any manner whatsoever, those motions will be the same as if they did not at all attract each other mutually, but were both attracted with the same forces by a third body placed in their common centre of gravity; and the law of the attracting forces will be the same in respect of the distance of the bodies from the common centre, as in respect of the distance between the two bodies.”

**Scelte.** *vis trahens* è reso «forza attrattiva». La seconda parte della dimostrazione (S11.17) ha un secondo C.V.D.: è un’aggiunta che dimostra la seconda metà dell’enunciato. Motte rende *intermedium* con «lying directly between them», corretto.

### A.7 Prop. LXII

**Latino:** *Corporum duorum, quæ viribus quadrato distantiæ suæ reciproce proportionalibus se mutuo trahunt, ac de locis datis demittuntur, determinare motus.*

**Inglese:** “To determine the motions of two bodies which attract each other with forces reciprocally proportional to the squares of the distance between them, and are let fall from given places.”

**Scelte.** *demittuntur* è reso «sono lasciati andare» (cioè partono da fermi). Il rimando *per prob. xxv.* è al Problema XXV, cioè la Prop. XXXVI della Sezione VII (moto rettilineo di caduta), secondo la numerazione della trascrizione (`latino-1726-L1-S07.md`).

### A.8 Prop. LXIII

**Latino:** *Corporum duorum quæ viribus quadrato distantiæ suæ reciproce proportionalibus se mutuo trahunt, deque locis datis, secundum datas rectas, datis cum velocitatibus exeunt, determinare motus.*

**Inglese:** “To determine the motions of two bodies attracting each other with forces reciprocally proportional to the squares of their distance, and going off from given places in given directions with given velocities.”

**Scelte.** *correpti* («preso» da una forza) è reso letteralmente. I Problemi IX e XXVI sono le Prop. XVII (Sezione III) e XXXVII (Sezione VII). Motte rende *motus initiales* con «the very first, or beginning motions»: ampliamento senza conseguenze.

### A.9 Prop. LXIV

**Latino:** *Viribus quibus corpora se mutuo trahunt crescentibus in simplici ratione distantiarum a centris: requiruntur motus plurium corporum inter se.*

**Inglese:** “Supposing forces with which bodies mutually attract each other to increase in a simple ratio of their distances from the centres; it is required to find the motions of several bodies among themselves.”

**Scelte e divergenze.**

- Il *corollarium primum theorematis xxi.* è il Cor. 1 della Prop. LVIII; il *problema v.* è la Prop. X (Sezione II).
- **Errore di Motte (lettere).** Il latino ha *Vires reliquæ acceleratrices* ***SD & SD***: sono le due forze uguali SD che agiscono l’una su T e l’altra su L. Motte scrive «The remaining accelerative forces **SD and DL**», lettura verificata anche sull’EPUB. DL è invece una delle forze già sommate alle attrazioni reciproche di T e L: l’errore contraddice la frase precedente.
- **Punteggiatura di Motte.** Nella stessa frase manca la virgola dopo «which are as the bodies»: la relativa «quæ sunt ut corpora» (le forze motrici stanno come i corpi) si salda in Motte con «attracting those bodies equally», e la frase diventa ambigua.
- *quam ductam concipe per medium corporis S* è reso «che si immagini condotta per il centro del corpo S»: *medium* è il centro del corpo.
- *e regione* è reso «dalla parte opposta»; Motte: «over against it».
- **Trascrizione:** *attractio <168> nes* è la parola *attractiones* spezzata dal marcatore di pagina.

### A.10 Prop. LXV

**Latino:** *Corpora plura, quorum vires decrescunt in duplicata ratione distantiarum ab eorundem centris, moveri posse inter se in ellipsibus; & radiis ad umbilicos ductis areas describere temporibus proportionales quam proxime.*

**Inglese:** “Bodies, whose forces decrease in a duplicate ratio of their distances from their centres, may move among themselves in ellipses; and by radii drawn to the foci may describe areas proportional to the times very nearly.”

**Scelte, trascrizione e divergenze.**

- Accusativo e infinito reso all’indicativo («possono muoversi»).
- *Q.E.O.* (*quod erat ostendendum*) è reso «C.V.M.», secondo il glossario.
- **Trascrizione (Caso 2):** la parentesi *(perexiguæ sane & pro lubitu minuendæ, valeant efficere* non è chiusa. La lettura adottata è *(perexiguæ sane & pro lubitu minuendæ) valeant efficere*: refuso probabile della trascrizione, da verificare sulla stampa. La traduzione rende l’inciso con una relativa.
- *Hyperbolam vel parabolam attractione languida, ellipsim fortiore*: Motte inverte l’ordine («a parabola or hyperbola»).
- Cor. 2: *Excessus impulsuum majorum* è reso «l’eccesso delle spinte maggiori» (§ A.0). Motte aggiunge «cause a perturbation **somewhere**».
- Cor. 3: Motte ristruttura la frase («if they are at all impelled … the impulse is very weak, or else is impressed very near equally»), introducendo un «impulse» che nel latino non c’è.

### A.11 Prop. LXVI e corollari

**Latino:** *Si corpora tria, quorum vires decrescunt in duplicata ratione distantiarum, se mutuo trahant; & attractiones acceleratrices binorum quorumcunque in tertium sint inter se reciproce ut quadrata distantiarum; minora autem circa maximum revolvantur: dico quod interius circa intimum & maximum, radiis ad ipsum ductis, describet areas temporibus magis proportionales, & figuram ad formam ellipseos umbilicum in concursu radiorum habentis magis accedentem; si corpus maximum his attractionibus agitetur; quam si maximum illud vel a minoribus non attractum quiescat, vel multo minus vel multo magis attractum, aut multo minus aut multo magis agitetur.*

**Inglese:** “If three bodies whose forces decrease in a duplicate ratio of the distances attract each other mutually; and the accelerative attractions of any two towards the third be between themselves reciprocally as the squares of the distances; and the two least revolve about the greatest; I say, that the interior of the two revolving bodies will, by radii drawn to the innermost and greatest, describe round that body areas more proportional to the times, and a figure more approaching to that of an ellipsis having its focus in the point of concourse of the radii, if that great body be agitated by those attractions, than it would do if that great body were not attracted at all by the lesser, but remained at rest; or than it would if that great body were very much more or very much less attracted, or very much more or very much less agitated, by the attractions.”

**Scelte.**

- *interius … intimum & maximum*: «il più interno [dei due minori]» e «il più interno e massimo» (T). L’italiano conserva la coppia di superlativi.
- *In duplicata ratione SK ad SP capiatur SL ad SK*: «si prenda SL che stia a SK in rapporto duplicato di SK a SP», cioè SL : SK = SK² : SP². Motte rende correttamente «as the square of SK to the square of SP».
- *exponatur per eandem* (Caso 1): l’attrazione alla distanza media è rappresentata dalla stessa linea SK.
- I corollari usano due nomi per la stessa forza perturbatrice radiale nelle sizigie: **KL** (= SL − SK) e **NM − LM**. Il Cor. 8 e il Cor. 20 li dichiarano equivalenti (*vis ablatitia KL seu NM−LM*): la verifica numerica è in N10.
- Cor. 2: *in antecedencia* è un refuso probabile della trascrizione per *in antecedentia* (la stessa frase ha poi *in antecedentia*).
- Cor. 7: *aux, seu apsis summa*: «l’auge, ossia l’apside superiore». **Aggiunta di Motte:** «the line of the apsides, or, which is the same thing, the upper apsis», e in seguito «line of the apsides» per *aux*.
- Cor. 9: la frase di Motte «it should decrease by the same degrees by which it increases before the body would return» ha perso una virgola («…increased before, the body would return»): il senso del latino è chiaro.
- Cor. 11: *in anteriora vergens*: Motte «in antecedentia to its former place» (vedi § A.0 e N15).
- Cor. 13: *rationes horum corollariorum*: «le ragioni di questi corollari». Motte amplia in «the causes and proportions of the errors and variations mentioned in these Corollaries».
- Cor. 14: *ut ST cub. reciproce* è reso «inversamente come ST³». Nell’estratto di Motte si legge «ST3», ma l’EPUB ha `ST<sup>3</sup>`: non è un errore di Motte.
- **Cor. 16, errore di Motte.** Il latino dice che entrambi i moti medi (auge e nodi) stanno *ut quadratum temporis periodici corporis P directe & quadratum temporis periodici corporis T inverse*. Motte scrive «as **the periodical time** of the body P directly, and the square of the periodical time of the body T inversely»: manca «the square» per P, lettura verificata sull’EPUB. Il latino è coerente con la frase precedente dello stesso corollario, che ha il quadrato per entrambi i tempi.
- Cor. 16, ultima frase: *nisi ubi eædem sunt nimis magnæ* si riferisce all’eccentricità e all’inclinazione; Motte riferisce la restrizione all’aumento o alla diminuzione («unless that increase or diminution be very great indeed»).
- Cor. 18: *deinde ex his contiguis factis conflari annulum*. **Aggiunta di Motte:** «to be so numerous, that they may all become contiguous».
- **Cor. 19, aggiunta di Motte.** Motte chiude il corollario con «except only in so far as the motion of flux and reflux may be directed by the channel of the water, and be a little retarded by friction». La trascrizione latina del 1726 termina con *& faciet ipsam ascendere usque ad quadraturas.* Non ho potuto verificare se l’inciso provenga da un’edizione latina precedente: va controllato sulla stampa del 1726 e sulle edizioni del 1687 e del 1713. Nello stesso corollario Motte rende *mox turbabitur aqua* con «the water will receive this new motion».
- Cor. 19: *circa globi centrum quiescens*: «attorno al centro del globo in quiete»; *quiescens* può concordare con *centrum*, come intende Motte («the quiescent centre»).
- Cor. 20: *aqæ* (due volte) è un refuso probabile della trascrizione per *aquæ*.
- Cor. 22: *quiscere* è un refuso probabile della trascrizione per *quiescere*. *Impetu quocunque* è «un impeto qualsiasi»; Motte «some impulse».
- **Trascrizione:** *ex <171> teriorem* (Caso 1), *præ <173> fatam* (Caso 1), *parti <179> cipes* (Cor. 11), *tem <180> pora* (Cor. 15), *obli <184> que* (Cor. 22) sono parole spezzate dai marcatori di pagina; *theor xxi.* (Caso 1) ha perso il punto dopo *theor*.

### A.12 Prop. LXVII, LXVIII, LXIX e Scolio

**Prop. LXVII. Latino:** *Positis iisdem attractionum legibus, dico quod corpus exterius S, circa interiorum P, T commune gravitatis centrum O, radiis ad centrum illud ductis, describit areas temporibus magis proportionales & orbem ad formam ellipseos umbilicum in centro eodem habentis magis accedentem, quam circa corpus intimum & maximum T, radiis ad ipsum ductis, describere potest.*

**Inglese:** “The same laws of attraction being supposed, I say, that the exterior body S does, by radii drawn to the point O, the common centre of gravity of the interior bodies P and T, describe round that centre areas more proportional to the times, and an orbit more approaching to the form of an ellipsis having its focus in that centre, than it can describe round the innermost and greatest body T by radii drawn to that body.”

- Nell’estratto di Motte il titolo «PROPOSITION LXVII. THEOREM XXVII.» è saldato all’enunciato senza a capo; nell’EPUB il titolo della Sezione XII compare per errore fra i due: difetto dell’edizione digitale, non del testo.
- *ut rem perpendenti facile constabit*: «come risulterà facilmente a chi consideri la cosa con attenzione».

**Prop. LXVIII. Latino:** *Positis iisdem attractionum legibus, dico quod corpus exterius S, circa interiorum P & T commune gravitatis centrum O, radiis ad centrum illud ductis, describit areas temporibus magis proportionales, & orbem ad formam ellipseos umbilicum in centro eodem habentis magis accedentem, si corpus intimum & maximum his attractionibus perinde atque cætera agitetur, quam si id vel non attractum quiescat, vel multo magis aut multo minus attractum aut multo magis aut multo minus agitetur.*

**Inglese:** “The same laws of attraction supposed, I say, that the exterior body S will, by radii drawn to O, the common centre of gravity of the interior bodies P and T, describe round that centre areas more proportional to the times, and an orbit more approaching to the form of an ellipsis having its focus in that centre, if the innermost and greatest body be agitated by these attractions as well as the rest, than it would do if that body were either at rest as not attracted, or were much more or much less attracted, or much more or much less agitated.”

- *quisceret* è un refuso probabile della trascrizione per *quiesceret*, da verificare sulla stampa.
- *proximum esse* è reso «è vicinissimo»; Motte «is very near».
- *Detur præterea motus communi trium centro, & augebitur perturbatio*: Motte aggiunge «yet more».

**Prop. LXIX. Latino:** *In systemate corporum plurium A, B, C, D, &c. si corpus aliquod A trahit cætera omnia B, C, D, &c. viribus acceleratricibus quæ sunt reciproce ut quadrata distantiarum a trahente; & corpus aliud B trahit etiam cætera A, C, D, &c. viribus quæ sunt reciproce ut quadrata distantiarum a trahente: erunt absolutæ corporum trahentium A, B vires ad invicem, ut sunt ipsa corpora A, B, quorum sunt vires.*

**Inglese:** “In a system of several bodies A, B, C, D, &c., if any one of those bodies, as A, attract all the rest, B, C, D, &c., with accelerative forces that are reciprocally as the squares of the distances from the attracting body; and another body, as B, attracts also the rest, A, C, D, &c., with forces that are reciprocally as the squares of the distances from the attracting body; the absolute forces of the attracting bodies A and B will be to each other as those very bodies A and B to which those forces belong.”

- *virum acceleratrices* è un refuso probabile della trascrizione per *virium acceleratrices*.
- *massa* compare qui per la prima volta nella sezione; si rende «massa», come nel latino.
- **Cor. 3, errore di Motte.** Il latino rimanda a *corol. prop. lxviii.*; Motte scrive «Cor. of Prop. **XLVIII**», lettura verificata sull’EPUB. Il rimando corretto è al corollario della Prop. LXVIII (S11.66), che tratta proprio dei fuochi delle orbite nei centri comuni di gravità.
- Cor. 3: *quam fieri potest accuratissimis* e *quam maxime proportionales* sono superlativi relativi («quanto più possibile esatte», «quanto più possibile proporzionali»). Motte li rende con «of a figure exceedingly accurate» e «proportional to the times **exactly**»: il secondo afferma un’esattezza che il latino non pretende.

**Scolio.**

- *ut fit in magneticis*: «come accade nei fenomeni magnetici». Motte aggiunge «as we see they do in magnetical **experiments**».
- *Eodem sensu generali usurpo vocem impulsus*: «uso la parola “spinta”» (§ A.0); Motte «the word impulse».
- *ut in definitionibus explicui*: il rimando è alla Def. VIII e al suo commento (Fascicolo 1).

### A.13 Riepilogo: dove Motte aggiunge, omette o sbaglia

| Luogo | Latino | Motte 1846 | Tipo |
|---|---|---|---|
| S11.01 | *vix extat* | «very probably there is no such thing» | rafforzamento |
| S11.01 | *possit quiescere* | «is truly at rest» | modale perso |
| S11.01 | *In mathematicis enim jam versamur* | «these propositions are to be considered as purely mathematical» | parafrasi |
| S11.06 | *vis posterior* | «this last force **(tending to s)**» | aggiunta |
| S11.24 | *Vires reliquæ acceleratrices SD & SD* | «SD **and DL**» | **lettere errate** |
| S11.24 | *quæ sunt ut corpora, trahendo* | «which are as the bodies attracting» | virgola mancante, senso ambiguo |
| S11.30 | *Hyperbolam vel parabolam* | «a parabola or hyperbola» | ordine invertito |
| S11.33 | *ut ex actionis inæqualitate perturbatio oriatur* | «cause a perturbation **somewhere**» | aggiunta |
| S11.34 | *aut non urgentur nisi levissime* | «the impulse is very weak» | parafrasi, termine introdotto |
| S11.45 | *ob magnitudinem vis KL* | «because the force KL is greater than LM» | esplicitazione |
| S11.46 | *aux, seu apsis summa* | «the line of the apsides, or, which is the same thing, the upper apsis» | aggiunta |
| S11.48 | *decresceret … rediret corpus* | «…increases before the body would return» | punteggiatura alterata |
| S11.50 | *in anteriora vergens* | «in antecedentia to its former place» | interpretazione (corretta nel senso) |
| S11.52 | *rationes horum corollariorum* | «the causes and proportions of the errors and variations» | ampliamento |
| S11.55 | *ut quadratum temporis periodici corporis P* | «as **the periodical time** of the body P» | **omissione: manca il quadrato** |
| S11.55 | *nisi ubi eædem sunt nimis magnæ* | «unless that increase or diminution be very great» | riferimento spostato |
| S11.57 | *ex his contiguis factis* | «to be so numerous, that they may all become contiguous» | aggiunta |
| S11.58 | *mox turbabitur aqua* | «the water will receive this new motion» | parafrasi |
| S11.58 | — | «except only in so far as … retarded by friction» | **frase assente nella trascrizione 1726** |
| S11.61 | *impetu quocunque* | «some impulse» | termine non equivalente |
| S11.65 | *augebitur perturbatio* | «will be increased **yet more**» | aggiunta |
| S11.71 | *quam maxime proportionales* | «proportional to the times **exactly**» | sopravvalutazione |
| S11.71 | *corol. prop. lxviii.* | «Cor. of Prop. **XLVIII**» | **rimando errato** |
| S11.72 | *in magneticis* | «in magnetical **experiments**» | aggiunta |

Motte conserva in latino *cæteris paribus*, *in consequentia*, *in antecedentia*, *ex æquo*, *vis insita*. Nelle Prop. LXV e LXVIII divide in più capoversi testi che il latino stampa di seguito: scelta tipografica senza conseguenze.

---

## Note editoriali e fisiche

Queste note sono aggiunte del presente fascicolo, non affermazioni tradotte da Newton. Le verifiche numeriche sono state eseguite con script Python (NumPy, SciPy) scritti per questo fascicolo; in unità arbitrarie, con G = 1.

### N1. Il proemio: dal centro immobile ai corpi che si attraggono

Le Sezioni II–X trattano un centro di forza fisso. Qui Newton osserva che un tale centro «difficilmente esiste in natura»: per la Legge III l’attrazione è reciproca, e per il Cor. IV delle leggi si muove (o resta in quiete) soltanto il centro comune di gravità. La sezione mostra come i risultati precedenti si trasferiscano al caso reale. La precisazione sulle «spinte» e sul «linguaggio familiare» anticipa lo Scolio finale (S11.72): la parola «attrazione» non impegna Newton su una causa fisica.

### N2. Prop. LVII–LVIII: il problema dei due corpi e l’orbita relativa

In termini moderni, con *m*_S e *m*_P al posto dei «corpi» S e P, le distanze dal baricentro sono CP = *m*_S·SP/(*m*_S + *m*_P) e CS = *m*_P·SP/(*m*_S + *m*_P): stanno in rapporto fisso fra loro e con SP. Per questo le tre curve (di S e di P attorno a C, e di P attorno a S) sono simili (Prop. LVII). La Prop. LVIII aggiunge che la curva relativa pqv può essere descritta attorno a un corpo **immobile** s, con le stesse forze, purché si cambi la velocità: è la riduzione al moto di un corpo attorno a un centro fisso, oggi scritta con la massa ridotta o, equivalentemente, con l’equazione del moto relativo **r̈** = −G(*m*_S + *m*_P)**r**/*r*³.

Il passo chiave del Caso 1 usa il Lemma X: a parità di forza, lo spazio «tratto dalla tangente» cresce come il quadrato del tempo, quindi per percorrere un intervallo rq maggiore di RQ nel rapporto sp : CP serve un tempo maggiore nel rapporto subduplicato. La velocità del corpo p sta a quella di P come √(sp/CP).

**Verifica numerica (F1).** Due corpi S = 3, P = 1, separazione iniziale 1, velocità relativa 1,2 (orbita ellittica), integrati per tre periodi: il centro di gravità resta fermo entro 6·10⁻¹⁵ e il rapporto CP/SP resta 0,750000 (= S/(S + P)) entro 3·10⁻¹⁶. Le figure attorno a C e attorno a S sono quindi simili.

### N3. Prop. LIX: i tempi periodici

Con la stessa forza, l’orbita relativa del sistema mobile ha periodo *T* = 2π√(*a*³/G(S + P)); la stessa figura descritta attorno a S immobile ha periodo 2π√(*a*³/GS). Il rapporto è √(S/(S + P)), come afferma Newton.

**Verifica numerica (F1).** Per S = 3, P = 1 il periodo misurato dell’orbita relativa sta al periodo della stessa ellisse attorno a S fisso come 0,8660254038; √(3/4) = 0,8660254038.

### N4. Prop. LX: le due medie proporzionali

Le due medie proporzionali *x*, *y* fra *a* = S + P e *b* = S soddisfano *a* : *x* = *x* : *y* = *y* : *b*; dunque *x* = (S + P)^(2/3)·S^(1/3). Il rapporto degli assi dell’enunciato è (S + P)/*x* = ((S + P)/S)^(1/3). È la terza legge di Keplero corretta per la massa del corpo che orbita: *a*³ ∝ (S + P)·*T*². La «prima delle due medie proporzionali» è il modo euclideo di scrivere una radice cubica (lo stesso problema della duplicazione del cubo).

**Verifica numerica (F1).** Per S = 3, P = 1: (S + P)/*x* = 1,1006424163; il rapporto fra l’asse dell’orbita relativa e l’asse dell’ellisse descritta attorno a S fisso **nello stesso tempo periodico**, calcolato dalla simulazione, è 1,1006424163. I tre rapporti *a*/*x*, *x*/*y*, *y*/*b* risultano tutti 1,1006424163, come richiede la definizione.

### N5. Prop. LXI–LXIII: un terzo corpo fittizio nel centro comune

La Prop. LXI giustifica l’uso dei problemi delle sezioni precedenti: ciascun corpo si muove come se fosse attratto da un corpo fittizio nel centro comune. Poiché CP = *k*·SP con *k* costante, una forza che va come una funzione qualsiasi di SP va come la funzione analoga di CP, con costanti diverse: per una potenza, *f* ∝ SPⁿ = CPⁿ/*k*ⁿ. Le Prop. LXII e LXIII applicano la riduzione alla caduta rettilinea (Probl. XXV = Prop. XXXVI) e al lancio con velocità date (Probl. IX e XXVI = Prop. XVII e XXXVII); nella LXIII il moto uniforme del centro si aggiunge alla fine, per il Cor. V delle leggi.

### N6. Prop. LXIV: forze proporzionali alla distanza

Con forze acceleratrici proporzionali alle distanze e ai corpi che attraggono, l’accelerazione di ogni corpo è *k*·(Σ*m*)·(**B** − **r**_i), dove **B** è il centro comune di gravità: ogni corpo è un oscillatore armonico attorno a B, con la stessa pulsazione √(*k*Σ*m*). Tutti descrivono ellissi centrate in B con lo stesso tempo periodico, come conclude S11.26. Newton ci arriva per gradi: due corpi (ellissi centrate in D), poi un terzo, che aggiunge a T e L forze DT, DL proporzionali alle distanze (ellissi «con moto più veloce») e forze uguali e parallele SD, che spostano il sistema senza alterarne i moti interni (Cor. V e VI delle leggi).

**Verifica numerica (F2).** Quattro corpi di masse 2; 1; 3; 0,5 con posizioni e velocità iniziali casuali: dopo il periodo 2π/√(*k*Σ*m*) = 2,4645 tutti tornano, rispetto al centro comune traslato di moto uniforme, alla posizione iniziale entro 4·10⁻¹². Verificate anche l’identità **ST** = **SD** + **DT** e la proporzione DT : TL = L : (T + L) (= 1/3 nell’esempio).

Le due forze «SD e SD» del latino sono le due forze uguali SD, l’una su T e l’altra su L; la lettura «SD and DL» di Motte è un errore (§ A.9).

### N7. Prop. LXV: ellissi approssimate con l’inverso del quadrato

Con l’inverso del quadrato le ellissi esatte valgono solo per due corpi. Newton mostra due situazioni limite in cui l’errore può essere reso minore di qualunque quantità data: corpi minori molto piccoli attorno a uno massimo (Caso 1, il sistema planetario); un sistema compatto molto lontano dal corpo massimo (Caso 2, un pianeta con i suoi satelliti attorno al Sole). Nel Caso 2 la perturbazione nasce soltanto dalla **disuguaglianza** e dall’**inclinazione** delle attrazioni verso il corpo lontano: è ciò che oggi si chiama forza di marea, che decresce come il cubo della distanza (N8, N16). Il Cor. 3 rovescia l’argomento: se le orbite di un sistema sono quasi ellittiche, le forze esterne sono deboli o quasi uniformi.

### N8. Prop. LXVI, Caso 1: la costruzione delle forze (figura 123–124)

Il corpo T è il centrale; P ruota vicino; S lontano. Si rappresenta l’attrazione di P verso S alla distanza media con la linea SK; alla distanza SP essa vale SL = SK³/SP², misurata sulla retta SP. La parallela LM a PT incontra ST in M. I triangoli SLM e SPT sono simili, quindi

LM = PT · SL/SP,  SM = ST · SL/SP.

L’attrazione SL si scompone in LM, diretta da P verso T, e SM, parallela a ST. L’attrazione di T verso S è SN = SK³/ST². Il moto **relativo** di P attorno a T risente solo della differenza MN = SM − SN, oltre che di LM. In termini moderni LM + MN è esattamente l’accelerazione perturbatrice

**a** = G*M*_S [(**s** − **r**)/|**s** − **r**|³ − **s**/|**s**|³],

con **r** = TP e **s** = TS: la parte «diretta» meno la parte «indiretta», cioè l’accelerazione di T.

**Verifica numerica (F3).** Con ST = SK = 100 e PT = 1 (unità arbitrarie), al variare dell’angolo di P visto da T a partire dalla direzione di S:

| Angolo | SL/SP = SM/ST = LM/PT | MN | KL = SL − SK |
|---:|---:|---:|---:|
| 0° (congiunzione) | 1,0306 | +3,061 | +2,030 |
| 45° | 1,0214 | +2,144 | +1,424 |
| 90° (quadratura) | 0,9999 | −0,015 | −0,010 |
| 135° | 0,9790 | −2,099 | −1,404 |
| 180° (opposizione) | 0,9706 | −2,941 | −1,970 |

- I tre rapporti coincidono in ogni posizione (similitudine verificata) e LM resta parallela a PT entro 10⁻¹⁴.
- La scomposizione vettoriale SL = SM + LM e l’uguaglianza fra LM + MN e la formula moderna della marea sono verificate a ogni angolo di prova (differenza nulla entro l’arrotondamento).
- Nelle quadrature LM ≈ PT; nelle sizigie la forza netta che allontana P da T, MN − LM, vale ≈ 2 PT ed è uguale a KL. Così si spiega il *quasi duplo* del Cor. 7 (KL ≈ 2,03 contro LM ≈ 1,00) e l’uguaglianza *KL seu NM − LM* dei Cor. 8 e 20.

### N9. Il senso di «agitato» e la conclusione del Caso 1

La tesi della Prop. LXVI è che il moto di P attorno a T è il più regolare possibile quando anche T è «agitato», cioè accelerato, dall’attrazione di S nella misura giusta (SN prossima al valore medio SK). Se T fosse fermo, agirebbe su P tutta la forza SM; se T fosse accelerato molto di più o molto di meno, resterebbe una differenza MN grande. È lo stesso principio del Cor. VI delle leggi: forze acceleratrici uguali e parallele non alterano i moti relativi. In linguaggio moderno, nel riferimento in caduta libera di T sopravvive solo la parte non uniforme del campo di S.

### N10. I corollari della Prop. LXVI: lessico e corrispondenze lunari

Nella Sezione XI Newton non nomina la Luna, la Terra e il Sole: i corpi sono P, T, S. Le corrispondenze (P Luna, T Terra, S Sole; oppure satelliti di Giove) sono sviluppate nel Libro III. Il lessico è quello dell’astronomia lunare: **congiunzione** A e **opposizione** B (le due **sizigie**, P allineato con T e S), **quadrature** C, D (a 90°), **ottanti** (a 45° da sizigie e quadrature). Gli «errori» sono le disuguaglianze del moto rispetto all’ellisse kepleriana: nei Cor. 2–5 riconosciamo la disuguaglianza oggi detta **variazione**, nel Cor. 6 la dipendenza del periodo dalla forza del corpo lontano, nei Cor. 7–8 il moto delle apsidi, nel Cor. 9 la variazione dell’eccentricità (oggi **evezione**), nei Cor. 10–11 la variazione dell’inclinazione e la retrocessione dei nodi.

**Verifica numerica del Cor. 2 (F3).** Con la costruzione di N8, il momento della forza perturbatrice rispetto a T (P in senso antiorario, A = 0°, D = 90°, B = 180°, C = 270°) è positivo a 300° e 330° (da C ad A: accelera la descrizione delle aree), negativo a 30° e 60° (da A a D: ritarda), positivo a 120° e 150° (da D a B), negativo a 210° e 240° (da B a C). L’alternanza è esattamente quella del Cor. 2.

**Verifica numerica dei Cor. 2–5 (F4).** Problema ristretto: S su un’orbita circolare attorno a T, P di massa trascurabile su un’orbita inizialmente circolare, rapporto dei periodi *m* = *T*_P/*T*_T = 1/13,37 (valore lunare), sei «anni» di integrazione. Medie su finestre di ±5° attorno a sizigie e quadrature:

- distanza TP: sizigie/quadrature = 0,986 (P più lontano nelle quadrature, Cor. 5);
- velocità di P: 1,023 (più veloce nelle sizigie, Cor. 3);
- velocità areolare: 1,009 (aree più veloci nelle sizigie, Cor. 2).

I valori sono indicativi, perché partendo da un’orbita circolare resta una piccola eccentricità libera; il segno degli effetti è quello indicato da Newton.

### N11. «In conseguenza» e «in antecedenza» (prima occorrenza: S11.41)

*In consequentia* significa nel verso del moto orbitale (e dei segni dello zodiaco); *in antecedentia* contro il verso del moto. Nel Cor. 2, una forza «diretta in conseguenza» ha una componente tangenziale concorde con la velocità di P e accelera la descrizione delle aree.

### N12. Cor. 6–8: periodo e moto delle apsidi

- **Cor. 6.** Per il Cor. 2 della Prop. IV la forza centripeta in un cerchio sta come *r*/*T*². In media la forza sottratta nelle sizigie (≈ 2 PT nella scala di N8) supera quella aggiunta nelle quadrature (≈ PT): la forza centripeta media è diminuita e il periodo, a parità di raggio, si allunga.
- **Cor. 7.** Nelle quadrature alla forza di T si aggiunge LM, che cresce come la distanza: la forza totale decresce meno rapidamente dell’inverso del quadrato, e per il Cor. 1 della Prop. XLV l’apside retrocede. Nelle sizigie si sottrae KL, anch’essa proporzionale alla distanza: la forza decresce più rapidamente, e l’apside avanza. Poiché KL ≈ 2 LM (N8), prevale l’avanzamento.
- **Verifica numerica (F4).** Nel problema ristretto con *m* = 1/13,37, eccentricità iniziale 0,05, quattro «anni»: la linea delle apsidi avanza di **+2,97° per rivoluzione**, in conseguenza, come afferma il Cor. 7. La teoria moderna al primo ordine in *m* dà (3/4)·*m*²·360° = 1,51° per rivoluzione: la simulazione completa dà circa il doppio, perché i termini di ordine superiore sono grandi. È la difficoltà storica del moto dell’apogeo lunare, che l’argomento qualitativo di Newton non affronta; il dato storico sulla sua soluzione nel Settecento non è verificato sulle fonti di questo progetto.

### N13. Cor. 9: l’eccentricità

Il ragionamento confronta il rapporto delle forze nelle due apsidi con il rapporto duplicato inverso delle distanze. Se la forza cresce, scendendo verso l’apside inferiore, più che come l’inverso del quadrato, il corpo «piega» di più verso il centro e l’orbita diventa più eccentrica. Con le apsidi nelle sizigie la sottrazione di KL produce proprio questo effetto; con le apsidi nelle quadrature l’aggiunta di LM produce l’effetto opposto. Ne segue un’oscillazione dell’eccentricità con il periodo con cui la linea delle apsidi passa dalle quadrature alle sizigie: è la disuguaglianza lunare chiamata evezione. Non ho fatto una verifica numerica specifica di questo corollario.

### N14. Cor. 10–11: inclinazione e nodi

La forza NM ha una componente perpendicolare al piano dell’orbita di P solo quando S è fuori della linea dei nodi; è nulla quando i nodi sono nelle sizigie. Il Cor. 11 mostra che, con i nodi nelle quadrature, P «attraversa» il piano di riferimento in un punto spostato verso S: i nodi retrocedono, cioè si muovono in antecedenza.

**Verifica numerica (F4).** Nel problema ristretto con *m* = 1/13,37 e inclinazione iniziale di 5° (nodi inizialmente nelle sizigie), i nodi retrocedono di **−1,43° per rivoluzione** (teoria al primo ordine: −1,51°) e l’inclinazione oscilla fra 4,72° e 5,00°: è massima con i nodi nelle sizigie, come afferma la fine del Cor. 10.

### N15. Cor. 11: *in anteriora vergens*

Il nuovo nodo cade in un punto che «piega verso la parte del corpo S» rispetto al vecchio nodo D. Poiché P va da C ad A a D, e il punto d’intersezione è raggiunto prima di D, lo spostamento è contro il verso del moto: *in antecedentia*. La resa «spostato verso le parti anteriori» conserva il latino; Motte esplicita il senso.

### N16. Cor. 13–17: leggi di scala

- **Cor. 14.** Dalla costruzione, LM ≈ PT·SK³/ST³ e MN ≈ 3 PT·SK³/ST³ cos θ (N8): le forze perturbatrici stanno come la forza assoluta di S (che è proporzionale a SK³) e come PT/ST³. Se il volume («grandezza») di S è proporzionale alla sua forza assoluta, cioè la densità è fissata, la forza assoluta va come *D*³ e il rapporto *D*³/ST³ è il cubo del diametro apparente *D*/ST. È per questo che Sole e Luna, con diametri apparenti quasi uguali, producono effetti di marea dello stesso ordine, e il loro rapporto dipende dalle densità: Newton svilupperà il punto nel Libro III.
- **Cor. 15–16.** Gli errori angolari per rivoluzione stanno come (*T*_P/*T*_T)². **Verifica numerica (F4):** dimezzando *m* (da 1/13,37 a 1/26,74) la retrocessione dei nodi per rivoluzione passa da 1,431° a 0,372°, rapporto 3,85 (atteso 4); l’avanzamento delle apsidi passa da 2,973° a 0,525°, rapporto 5,7. La legge del quadrato vale bene per i nodi; per le apsidi i termini di ordine superiore sono rilevanti quando *m* è grande, e Newton infatti dice *quam proxime*.
- **Cor. 17.** La forza media LM sta alla forza con cui T trattiene P come (*T*_P/*T*_T)². Con i valori lunari (mese sidereo 27,3217 giorni, anno sidereo 365,2564 giorni) il rapporto è 0,005595, circa 1/178,7. Il calcolo è del curatore; Newton non dà qui valori numerici.

### N17. Cor. 18–22: anello, maree, precessione

I corollari finali passano da un singolo corpo P a un anello di corpi, poi a un anello d’acqua in un canale scavato nel globo T (Cor. 19, modello delle maree), poi a un anello rigido saldato al globo (Cor. 20). L’anello rigido, e quindi il rigonfiamento equatoriale di un globo schiacciato, oscilla nell’inclinazione e fa retrocedere i nodi dell’equatore: è il meccanismo della **precessione degli equinozi**, che Newton tratterà nel Libro III. Il Cor. 22 enuncia che un globo omogeneo perfetto ruota sempre attorno a un asse fisso e che una massa aggiunta fuori dei poli e dell’equatore fa «vagare» i poli: in termini moderni, la rotazione libera di un corpo con momenti d’inerzia uguali è stabile attorno a qualunque asse, mentre un’asimmetria produce un moto del polo. Questi corollari sono qualitativi e non sono stati verificati numericamente.

### N18. Prop. LXVII–LXVIII: il corpo esterno e il centro comune dei due interni

Per un corpo S lontano, l’attrazione verso T e P insieme è quasi quella di una massa T + P posta nel loro centro comune O. Per questo le orbite esterne si riferiscono meglio a O che a T (oggi: coordinate di Jacobi).

**Verifica numerica (F5).** T = 1, P = 0,3 a distanza 1 su un’orbita circolare relativa, S = 0,001 a distanza 6 da O, tre rivoluzioni di S. Variazione relativa (deviazione standard / media) della velocità areolare di S:

| Configurazione | attorno a O | attorno a T |
|---|---:|---:|
| T libero, attratto come gli altri (Prop. LXVII) | 2,0·10⁻⁴ | 4,2·10⁻¹ |
| T tenuto fermo, non attratto (Prop. LXVIII) | 2,0 | 2,8·10⁻⁴ |

Attorno a O le aree sono molto più uniformi quando T è «agitato» come gli altri (Prop. LXVIII). Quando T è tenuto fermo il centro O oscilla con P e le aree misurate attorno a O non sono più regolari; diventano regolari attorno a T, ma restano un po’ meno uniformi (2,8·10⁻⁴) del caso libero attorno a O (2,0·10⁻⁴), in accordo con il corollario della Prop. LXVIII.

### N19. Prop. LXIX: forza assoluta e massa

La forza assoluta di un corpo (Def. VI) è oggi G*M*. L’argomento combina la Legge III con le Def. VII–VIII: le forze motrici sono uguali, quindi le accelerazioni *a*_B→A = G*M*_A/*r*² e *a*_A→B = G*M*_B/*r*² stanno come *M*_A : *M*_B. È qui che Newton collega esplicitamente la forza attrattiva di un corpo alla sua **massa**: il risultato servirà nel Libro III per misurare le masse dei pianeti dai moti dei loro satelliti. Il Cor. 2 estende il risultato a qualsiasi legge comune di dipendenza dalla distanza.

### N20. Lo Scolio: matematica prima, fisica poi

Lo Scolio ribadisce il metodo: si calcolano matematicamente le conseguenze di ipotesi sulle forze, poi le si confronta con i fenomeni. La frase finale annuncia la Sezione XII: le attrazioni dei corpi sferici composti di particelle che attraggono «nel modo ora esposto», cioè con forze proporzionali ai corpi.

---

## Controllo della copertura

Le pagine del 1726 sono quelle dei marcatori <n> della trascrizione (la sezione comincia a p. 160); quelle di Motte derivano dai marcatori `Page_n` dell’EPUB Gutenberg.

| Identificatori | Incipit latino | Contenuto | 1726 | Motte 1846 |
|---|---|---|---|---|
| S11.01 | *Hactenus exposui motus corporum* | Titolo e proemio | p. 160 | p. 194 |
| S11.02–S11.03 | *Corpora duo se invicem trahentia describunt* | Prop. LVII | pp. 160–161 | pp. 194–195 |
| S11.04–S11.05 | *Si corpora duo Viribus quibusvis* | Prop. LVIII, enunciato e costruzione | p. 161 | p. 195 |
| S11.06–S11.07 | *Cas. 1. Commune illud gravitatis centrum* | Prop. LVIII, Casi 1 e 2 | pp. 161–163 | pp. 195–196 |
| S11.08–S11.10 | *Hinc corpora duo viribus distantiæ* | Prop. LVIII, Cor. 1–3 | p. 163 | pp. 196–197 |
| S11.11–S11.12 | *Corporum duorum S & P* | Prop. LIX | p. 163 | p. 197 |
| S11.13–S11.14 | *Si corpora duo S & P, viribus quadrato* | Prop. LX | p. 164 | p. 197 |
| S11.15–S11.17 | *Si corpora duo viribus quibusvis se mutuo trahentia, neque alias* | Prop. LXI | pp. 164–165 | pp. 197–198 |
| S11.18–S11.19 | *Corporum duorum … de locis datis demittuntur* | Prop. LXII | p. 165 | p. 198 |
| S11.20–S11.21 | *Corporum duorum … datis cum velocitatibus exeunt* | Prop. LXIII | p. 166 | pp. 198–199 |
| S11.22–S11.26 | *Viribus quibus corpora se mutuo trahunt crescentibus* | Prop. LXIV | pp. 166–168 | pp. 199–200 |
| S11.27–S11.31 | *Corpora plura, quorum vires decrescunt* | Prop. LXV, enunciato, Casi 1–2 | pp. 168–169 | pp. 200–201 |
| S11.32–S11.34 | *In casu secundo, quo propius accedit* | Prop. LXV, Cor. 1–3 | pp. 169–170 | pp. 201–202 |
| S11.35–S11.36 | *Si corpora tria, quorum vires decrescunt* | Prop. LXVI, enunciato | p. 170 | p. 202 |
| S11.37–S11.38 | *Cas. 1. Revolvantur corpora minora P & S* | Prop. LXVI, Caso 1 | pp. 170–173 | pp. 202–204 |
| S11.39 | *Cas. 2. Revolvantur jam corpora minora* | Prop. LXVI, Caso 2 | p. 173 | p. 204 |
| S11.40–S11.41 | *Ex his facile colligitur* | Cor. 1–2 | p. 173 | p. 205 |
| S11.42–S11.44 | *Et eodem argumento patet* | Cor. 3–5 | p. 174 | p. 205 |
| S11.45 | *Quoniam vis centripeta corporis centralis T* | Cor. 6 | pp. 174–175 | pp. 205–206 |
| S11.46 | *Ex præmissis consequitur etiam* | Cor. 7 | p. 175 | pp. 206–207 |
| S11.47 | *Cum autem pendeat apsidum progressus* | Cor. 8 | p. 176 | p. 207 |
| S11.48 | *Si corpus aliquod, vi reciproce proportionali* | Cor. 9 | pp. 176–177 | pp. 207–208 |
| S11.49 | *Ut rationem ineamus errorum in latitudinem* | Cor. 10 | pp. 177–178 | pp. 208–209 |
| S11.50 | *Quoniam corpus P, ubi nodi sunt in quadraturis* | Cor. 11 | pp. 178–179 | p. 209 |
| S11.51–S11.53 | *Omnes illi in his corollariis descripti errores* | Cor. 12–14 | p. 179 | pp. 209–210 |
| S11.54 | *Et quoniam si, manentibus orbium ESE & PAB forma* | Cor. 15 | pp. 179–180 | p. 210 |
| S11.55 | *Unde, si dentur orbium formæ* | Cor. 16 | p. 180 | pp. 210–211 |
| S11.56 | *Cum autem linea LM nunc major sit* | Cor. 17 | p. 181 | p. 211 |
| S11.57 | *Iisdem legibus, quibus corpus P circum corpus T* | Cor. 18 | p. 181 | p. 212 |
| S11.58 | *Fingas jam globum corporis T* | Cor. 19 | pp. 181–182 | p. 212 |
| S11.59 | *Si annulus jam rigeat* | Cor. 20 | pp. 182–183 | pp. 212–213 |
| S11.60 | *Eadem ratione, qua materia globi* | Cor. 21 | p. 183 | pp. 213–214 |
| S11.61 | *Et inde vicissim, ex motu nodorum* | Cor. 22 | pp. 183–184 | pp. 214–215 |
| S11.62–S11.63 | *Positis iisdem attractionum legibus, dico quod corpus exterius S, circa interiorum P, T* | Prop. LXVII | p. 185 | p. 215 |
| S11.64–S11.66 | *Positis iisdem attractionum legibus … si corpus intimum & maximum* | Prop. LXVIII e corollario | pp. 185–186 | pp. 215–216 |
| S11.67–S11.68 | *In systemate corporum plurium A, B, C, D* | Prop. LXIX | pp. 186–187 | pp. 216–217 |
| S11.69–S11.71 | *Hinc si singula systematis corpora* | Prop. LXIX, Cor. 1–3 | pp. 187–188 | p. 217 |
| S11.72 | *His propositionibus manuducimur* | Scolio | p. 188 | pp. 217–218 |

**Controlli eseguiti.**

1. **Copertura.** Ho riletto in sequenza, frase per frase, l’intera trascrizione (pp. 160–188), da *Hactenus exposui motus corporum* a *& quales motus inde consequantur*, contro la traduzione. Nessuna frase manca; dove il latino ha periodi molto lunghi (Prop. LXVI, Caso 1; Cor. 9, 10, 20, 22) l’italiano li divide in più frasi senza omettere membri. Nella Parte B tutte le stringhe `la` (enunciati e passi) sono sottostringhe esatte della trascrizione e tutte le stringhe `en` sono sottostringhe esatte di Motte (esito di `check.py` più sotto).
2. **Matematica.** Cinque script di verifica:
   - F1, Prop. LVIII–LX: similitudine delle figure, rapporto dei periodi √(S/(S + P)), rapporto degli assi con le due medie proporzionali (N2–N4);
   - F2, Prop. LXIV: quattro corpi con forze lineari, periodo comune, scomposizione ST = SD + DT (N6);
   - F3, Prop. LXVI: costruzione SL, LM, SM, SN, MN, KL in cinque posizioni, identità con la formula moderna della marea, segni del Cor. 2, rapporto KL : LM ≈ 2 del Cor. 7 (N8, N10);
   - F4, corollari della Prop. LXVI: problema ristretto con rapporto lunare dei periodi (variazione, apsidi, nodi, inclinazione, scala in *m*², Cor. 17) (N10, N12, N14, N16);
   - F5, Prop. LXVII–LXVIII: uniformità delle aree del corpo esterno attorno a O e a T, con T libero o fermo (N18).
   Tutti i rapporti dichiarati da Newton risultano confermati; le leggi di scala del Cor. 16 valgono bene per i nodi e solo in modo approssimato per le apsidi (N16). Prop. LXIX: controllo aritmetico immediato (N19).
3. **Confronto con Motte.** Ho confrontato tutta la sezione corrispondente, pp. 194–218. Le divergenze sono raccolte nel § A.13; le tre più gravi (SD and DL, il quadrato mancante del Cor. 16, il rimando XLVIII) sono state verificate direttamente sul file EPUB.
4. **Separazione fra testo e commento.** Il testo tradotto non contiene formule moderne; le integrazioni del curatore sono tra parentesi quadre (una sola, in S11.06).

**Non ho potuto verificare:**

- **la stampa del 1726**: i refusi della trascrizione (*revoluntur*, *summan*, *in antecedencia*, *aqæ*, *quiscere*, *quisceret*, *virum*, la parentesi non chiusa della Prop. LXV) sono segnalati come probabili, da verificare;
- **le figure NATP00087-120…131**: le relazioni geometriche della Parte B sono ricostruite soltanto dalle lettere del testo; in particolare non so come la figura disponga i punti K, N, I e le quadrature C, D rispetto al verso del moto;
- **l’origine dell’inciso finale di Motte nel Cor. 19** («except only in so far as … retarded by friction»), assente nella trascrizione del 1726;
- **la corrispondenza esatta della numerazione di pagina di Motte**, che deriva dai marcatori dell’EPUB e non da un esemplare a stampa;
- **i dati storici** citati nelle note N12 e N16 (soluzione settecentesca del moto dell’apogeo lunare; uso dei risultati nel Libro III), che non sono nelle fonti del progetto.

---

## Registro del lavoro successivo

| Unità | Stato |
|---|---|
| Sezione XI: proemio, Prop. LVII–LXIX, Cor. 1–22 della Prop. LXVI, Scolio | **Fascicolo 10, presente documento, prima versione** |
| Refusi della trascrizione (§ A.5, A.10, A.11, A.12) | Da verificare sulla stampa del 1726 |
| Figure NATP00087-120…131 | Da scaricare e confrontare con le relazioni della Parte B (posizione di K, N, I; verso del moto rispetto a C, D) |
| Cor. 19, inciso di Motte | Da confrontare con le edizioni latine 1687 e 1713 |
| Pagine interattive candidate | Prop. LVIII (orbita relativa e orbita attorno a s fisso); Prop. LXVI, Caso 1 (costruzione SL, LM, SM, SN, MN, con P mobile sull’orbita: è la pagina più ricca della sezione); Prop. LXIV (oscillatori); Prop. LXVIII (confronto T libero / T fermo) |
| Corollari della Prop. LXVI | Candidati a una pagina di simulazione unica (variazione, apsidi, nodi) basata sugli script F4 |
| Revisione filologica e scientifica indipendente | Da eseguire, come previsto dalla skill di verifica |

Il presente testo è una nuova traduzione assistita da IA e non riproduce traduzioni italiane moderne. Licenza prevista dal curatore: testi e traduzioni CC BY-SA 4.0, codice MIT. La trascrizione latina è © The Newton Project; i testi di Motte sono di pubblico dominio.

---

## Parte B — Dati per le pagine interattive

Unità incluse: le proposizioni con dimostrazione geometrica e figura (LVIII, LXIV, LXVI, LXVII, LXVIII). La Prop. LVII ha un argomento geometrico ma nessuna figura; le Prop. LIX–LXIII, LXV e LXIX non hanno figura; i corollari della Prop. LXVI sono discorsivi e non hanno dimostrazione geometrica propria.

Convenzioni:

- `la`: testo latino esatto della trascrizione, compresi i refusi e le parole spezzate dai marcatori di pagina (rimossi da `check.py`), annotati in `nota`;
- `it`: la traduzione di questo fascicolo;
- `en`: Motte 1846, allineato per senso;
- `dipende_da`: soltanto i rimandi citati nella frase;
- `figura.mostra`: gli elementi da rendere visibili al passo, cumulativi; `figura.evidenzia`: le relazioni da mettere in risalto.

```json
{
  "fascicolo": "10-L1-S11",
  "versione": "0.1",
  "data": "2026-11-08",
  "convenzioni": {
    "dipende_da": "solo rimandi citati esplicitamente nella frase latina",
    "en": "Motte 1846, allineato per senso",
    "figura.mostra": "elementi da rendere visibili al passo, cumulativi salvo indicazione"
  },
  "unita": [
    {
      "id": "L1-P58",
      "tipo": "Propositio/Theorema",
      "titolo": "Prop. LVIII (Teor. XXI) — orbita relativa e orbita attorno a un corpo immobile",
      "copertura": [
        "S11.04",
        "S11.05",
        "S11.06",
        "S11.07"
      ],
      "fonti": {
        "la": "",
        "en": "Motte 1846, pp. 195–196"
      },
      "enunciato": {
        "la": "",
        "it": "Se due corpi si attraggono a vicenda con forze qualsiasi e intanto ruotano attorno al centro comune di gravità, dico che, con le stesse forze, si può descrivere attorno a uno dei due, immobile, una figura simile e uguale alle figure che i corpi, così mossi, descrivono l’uno attorno all’altro.",
        "en": "If two bodies attract each other mutually with forces of any kind, and in the mean time revolve about the common centre of gravity; I say, that, by the same forces, there may be described round either body unmoved a figure similar and equal to the figures which the bodies so moving describe round each other mutually."
      },
      "figura_base": {
        "punti": [
          "S",
          "P",
          "C",
          "T",
          "Q",
          "V",
          "s",
          "p",
          "q",
          "v",
          "R",
          "r"
        ],
        "vincoli": [
          "C centro comune di gravità di S e P, sul segmento SP, con SC : CP = P : S",
          "T, Q posizioni successive di S, P (T non è il corpo T della Prop. LXVI)",
          "s punto fisso dato; sp = SP e sp ∥ SP; sq = TQ e sq ∥ TQ",
          "pqv curva descritta da p attorno a s (orbita relativa)",
          "PR tangente in P alla curva PQ; pr tangente in p alla curva pq",
          "R su CQ prolungata; r su sq prolungata",
          "figure CPRQ e sprq simili"
        ],
        "nota": "Figure non disponibili: relazioni ricavate dalle lettere del testo."
      },
      "passi": [
        {
          "id": "L1-P58-p1",
          "la": "",
          "it": "Ruotino i corpi S, P attorno al centro comune di gravità C, procedendo da S verso T e da P verso Q.",
          "en": "Let the bodies S and P revolve about their common centre of gravity C, proceeding from S to T, and from P to Q.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "corpi S, P",
              "centro C",
              "posizioni successive T (di S) e Q (di P)"
            ],
            "evidenzia": [
              "S e P da parti opposte di C, allineati"
            ]
          }
        },
        {
          "id": "L1-P58-p2",
          "la": "",
          "it": "Da un punto dato s si conducano sempre sp, sq uguali e parallele a SP, TQ: la curva pqv, che il punto p descrive ruotando attorno al punto immobile s, sarà simile e uguale alle curve che i corpi S, P descrivono l’uno attorno all’altro; e quindi (per il Teor. XX) simile alle curve ST e PQV che gli stessi corpi descrivono attorno al centro comune di gravità C; e ciò perché sono dati i rapporti fra loro delle linee SC, CP e SP, o sp.",
          "en": "From the given point s let there be continually drawn sp, sq, equal and parallel to SP, TQ; and the curve pqv, which the point p describes in its revolution round the immovable point s, will be similar and equal to the curves which the bodies S and P describe about each other mutually; and therefore, by Theor. XX, similar to the curves ST and PQV which the same bodies describe about their common centre of gravity C; and that because the proportions of the lines SC, CP, and SP or sp, to each other, are given.",
          "dipende_da": [
            "Teor. XX"
          ],
          "figura": {
            "mostra": [
              "punto fisso s",
              "sp = SP, sp ∥ SP",
              "sq = TQ, sq ∥ TQ",
              "curva pqv",
              "curve ST e PQV attorno a C"
            ],
            "evidenzia": [
              "pqv simile e uguale all’orbita relativa",
              "pqv simile a PQV (rapporto sp : CP)"
            ]
          }
        },
        {
          "id": "L1-P58-p3",
          "la": "",
          "it": "Caso 1. Quel centro comune di gravità C, per il Cor. IV delle leggi, o è in quiete o si muove uniformemente in linea retta.",
          "en": "CASE 1. The common centre of gravity C (by Cor. 4, of the Laws of Motion) is either at rest, or moves uniformly in a right line.",
          "dipende_da": [
            "Leggi, Cor. IV"
          ],
          "figura": {
            "mostra": [
              "C"
            ],
            "evidenzia": [
              "C in quiete o in moto rettilineo uniforme"
            ]
          }
        },
        {
          "id": "L1-P58-p4",
          "la": "",
          "it": "Supponiamo dapprima che sia in quiete, e in s e p si pongano due corpi, uno immobile in s e uno mobile in p, simili e uguali ai corpi S e P.",
          "en": "Let us first suppose it at rest, and in s and p let there be placed two bodies, one immovable in s, the other movable in p, similar and equal to the bodies S and P.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "corpo immobile in s",
              "corpo mobile in p"
            ],
            "evidenzia": [
              "s ≅ S, p ≅ P"
            ]
          }
        },
        {
          "id": "L1-P58-p5",
          "la": "",
          "it": "Poi le rette PR e pr tocchino le curve PQ e pq in P e p, e si prolunghino CQ e sq fino a R e r.",
          "en": "Then let the right lines PR and pr touch the curves PQ and pq in P and p, and produce CQ and sq to R and r.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "tangente PR in P",
              "tangente pr in p",
              "CQ prolungata fino a R",
              "sq prolungata fino a r"
            ],
            "evidenzia": [
              "segmenti RQ e rq (deviazioni dalle tangenti)"
            ]
          }
        },
        {
          "id": "L1-P58-p6",
          "la": "",
          "it": "Per la similitudine delle figure CPRQ, sprq, RQ starà a rq come CP sta a sp, e quindi in un rapporto dato.",
          "en": "And because the figures CPRQ, sprq are similar, RQ will be to rq as CP to sp, and therefore in a given ratio.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "figure CPRQ, sprq"
            ],
            "evidenzia": [
              "RQ : rq = CP : sp"
            ]
          }
        },
        {
          "id": "L1-P58-p7",
          "la": "",
          "it": "Perciò, se la forza con cui il corpo P è attratto verso il corpo S, e quindi verso il centro intermedio C, stesse alla forza con cui il corpo p è attratto verso il centro s in quello stesso rapporto dato, queste forze, in tempi uguali, trarrebbero sempre i corpi dalle tangenti PR, pr verso gli archi PQ, pq per intervalli proporzionali a esse, RQ, rq; e quindi la seconda forza farebbe sì che il corpo p girasse lungo la curva pqv, simile alla curva PQV lungo la quale la prima forza fa girare il corpo P, e le rivoluzioni si compirebbero negli stessi tempi.",
          "en": "Hence if the force with which the body P is attracted towards the body S, and by consequence towards the intermediate point the centre C, were to the force with which the body p is attracted towards the centre s, in the same given ratio, these forces would in equal times attract the bodies from the tangents PR, pr to the arcs PQ, pq, through the intervals proportional to them RQ, rq; and therefore this last force (tending to s) would make the body p revolve in the curve pqv, which would become similar to the curve PQV, in which the first force obliges the body P to revolve; and their revolutions would be completed in the same times.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "forza su P verso C",
              "forza su p verso s"
            ],
            "evidenzia": [
              "caso ipotetico: forze nel rapporto CP : sp → tempi uguali"
            ]
          },
          "nota": "Motte aggiunge «(tending to s)»."
        },
        {
          "id": "L1-P58-p8",
          "la": "",
          "it": "Ma poiché quelle forze non stanno fra loro nel rapporto di CP a sp, ma sono uguali fra loro (per la similitudine e l’uguaglianza dei corpi S e s, P e p, e per l’uguaglianza delle distanze SP, sp), i corpi in tempi uguali saranno tratti in egual misura dalle tangenti; e perciò, perché il secondo corpo p sia tratto per l’intervallo maggiore rq, si richiede un tempo maggiore, e precisamente in rapporto subduplicato degli intervalli, perché (per il Lemma X) gli spazi descritti all’inizio stesso del moto stanno in rapporto duplicato dei tempi.",
          "en": "But because those forces are not to each other in the ratio of CP to sp, but (by reason of the similarity and equality of the bodies S and s, P and p and the equality of the distances SP, sp) mutually equal, the bodies in equal times will be equally drawn from the tangents; and therefore that the body p may be attracted through the greater interval rq, there is required a greater time, which will be in the subduplicate ratio of the intervals; because, by Lemma X, the spaces described at the very beginning of the motion are in a duplicate ratio of the times.",
          "dipende_da": [
            "Lemma X"
          ],
          "figura": {
            "mostra": [
              "RQ",
              "rq"
            ],
            "evidenzia": [
              "forze uguali: tempo per rq : tempo per RQ = √(rq : RQ)"
            ]
          }
        },
        {
          "id": "L1-P58-p9",
          "la": "",
          "it": "Si ponga dunque che la velocità del corpo p stia alla velocità del corpo P in rapporto subduplicato della distanza sp alla distanza CP, in modo che gli archi pq, PQ, che stanno nel rapporto semplice [delle distanze], siano descritti in tempi che stanno in quello stesso rapporto subduplicato: e i corpi P, p, attratti sempre da forze uguali, descriveranno attorno ai centri in quiete C e s figure simili PQV, pqv, la seconda delle quali, pqv, è simile e uguale alla figura che il corpo P descrive attorno al corpo mobile S. C.V.D.",
          "en": "Suppose, then the velocity of the body p to be to the velocity of the body P in a subduplicate ratio of the distance sp to the distance CP, so that the arcs pq, PQ, which are in a simple proportion to each other, may be described in times that are in a subduplicate ratio of the distances; and the bodies P, p, always attracted by equal forces, will describe round the quiescent centres C and s similar figures PQV, pqv, the latter of which pqv is similar and equal to the figure which the body P describes round the movable body S. Q.E.D.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "orbite complete PQV attorno a C e pqv attorno a s"
            ],
            "evidenzia": [
              "v(p) : v(P) = √(sp : CP)",
              "pqv simile e uguale all’orbita di P attorno a S"
            ]
          }
        },
        {
          "id": "L1-P58-p10",
          "la": "",
          "it": "Caso 2. Supponiamo ora che il centro comune di gravità, insieme con lo spazio in cui i corpi si muovono fra loro, avanzi uniformemente in linea retta: (per il Cor. VI delle leggi) tutti i moti in questo spazio si compiranno come prima, e quindi i corpi descriveranno l’uno attorno all’altro le stesse figure di prima, e perciò figure simili e uguali a pqv. C.V.D.",
          "en": "CASE 2. Suppose now that the common centre of gravity, together with the space in which the bodies are moved among themselves, proceeds uniformly in a right line; and (by Cor. 6, of the Laws of Motion) all the motions in this space will be performed in the same manner as before; and therefore the bodies will describe mutually about each other the same figures as before, which will be therefore similar and equal to the figure pqv. Q.E.D.",
          "dipende_da": [
            "Leggi, Cor. VI"
          ],
          "figura": {
            "mostra": [
              "spazio con C in moto rettilineo uniforme"
            ],
            "evidenzia": [
              "stesse figure relative del Caso 1"
            ]
          },
          "nota": "La trascrizione ha «unifor <163> miter»: la parola uniformiter è spezzata dal marcatore di pagina. Il latino cita il Cor. VI delle leggi, dove ci si aspetterebbe il Cor. V (spazio in moto uniforme); Motte ha anch’egli «Cor. 6». Si registra il rimando com’è."
        }
      ]
    },
    {
      "id": "L1-P64",
      "tipo": "Propositio/Problema",
      "titolo": "Prop. LXIV (Probl. XL) — più corpi con forze proporzionali alle distanze",
      "copertura": [
        "S11.22",
        "S11.23",
        "S11.24",
        "S11.25",
        "S11.26"
      ],
      "fonti": {
        "la": "",
        "en": "Motte 1846, pp. 199–200"
      },
      "enunciato": {
        "la": "",
        "it": "Se le forze con cui i corpi si attraggono a vicenda crescono in rapporto semplice delle distanze dai centri, si cercano i moti di più corpi fra loro.",
        "en": "Supposing forces with which bodies mutually attract each other to increase in a simple ratio of their distances from the centres; it is required to find the motions of several bodies among themselves."
      },
      "figura_base": {
        "punti": [
          "T",
          "L",
          "D",
          "S",
          "C",
          "I",
          "K",
          "V",
          "B"
        ],
        "vincoli": [
          "D centro comune di gravità di T e L, sul segmento TL",
          "C centro comune di gravità di S e del sistema T+L (sul segmento SD)",
          "I, K su rette per T e L parallele a DS (TI ∥ LK ∥ DS)",
          "retta IK per il centro di S, perpendicolare a DS",
          "V quarto corpo; B centro comune di gravità di tutti"
        ],
        "nota": "Figura non disponibile: relazioni ricavate dalle lettere del testo."
      },
      "passi": [
        {
          "id": "L1-P64-p1",
          "la": "",
          "it": "Si pongano dapprima due corpi T e L, che hanno il centro comune di gravità in D.",
          "en": "Suppose the first two bodies T and L to have their common centre of gravity in D.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "T",
              "L",
              "D"
            ],
            "evidenzia": [
              "D su TL"
            ]
          }
        },
        {
          "id": "L1-P64-p2",
          "la": "",
          "it": "Essi descriveranno (per il Cor. 1 del Teor. XXI) ellissi che hanno i centri in D, la cui grandezza si conosce dal Probl. V.",
          "en": "These, by Cor. 1, Theor. XXI, will describe ellipses having their centres in D, the magnitudes of which ellipses are known by Prob. V.",
          "dipende_da": [
            "Teor. XXI, Cor. 1",
            "Probl. V"
          ],
          "figura": {
            "mostra": [
              "ellissi di T e L centrate in D"
            ],
            "evidenzia": [
              "ellissi concentriche in D"
            ]
          }
        },
        {
          "id": "L1-P64-p3",
          "la": "",
          "it": "Ora un terzo corpo S attragga i primi due, T e L, con le forze acceleratrici ST, SL, e sia attratto da essi a sua volta.",
          "en": "Let now a third body S attract the two former T and L with the accelerative forces ST, SL, and let it be attracted again by them.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "S",
              "forze ST, SL"
            ],
            "evidenzia": [
              "ST, SL come forze acceleratrici su T e L"
            ]
          }
        },
        {
          "id": "L1-P64-p4",
          "la": "",
          "it": "La forza ST (per il Cor. II delle leggi) si scompone nelle forze SD, DT, e la forza SL nelle forze SD, DL.",
          "en": "The force ST (by Cor. 2, of the Laws of Motion) is resolved into the forces SD, DT; and the force SL into the forces SD and DL.",
          "dipende_da": [
            "Leggi, Cor. II"
          ],
          "figura": {
            "mostra": [
              "SD",
              "DT",
              "DL"
            ],
            "evidenzia": [
              "ST = SD + DT",
              "SL = SD + DL"
            ]
          },
          "nota": "La trascrizione ha il marcatore di pagina <167> fra «legum» e «cor.»."
        },
        {
          "id": "L1-P64-p5",
          "la": "",
          "it": "Le forze DT, DL, che stanno come la loro somma TL, e quindi come le forze acceleratrici con cui i corpi T e L si attraggono a vicenda, aggiunte a queste forze dei corpi T e L, la prima alla prima e la seconda alla seconda, compongono forze proporzionali alle distanze DT e DL, come prima, ma maggiori delle forze di prima; e perciò (per il Cor. 1 della Prop. X e per i Cor. 1 e 8 della Prop. IV) fanno sì che quei corpi descrivano ellissi come prima, ma con moto più veloce.",
          "en": "Now the forces DT, DL, which are as their sum TL, and therefore as the accelerative forces with which the bodies T and L attract each other mutually, added to the forces of the bodies T and L, the first to the first, and the last to the last, compose forces proportional to the distances DT and DL as before, but only greater than those former forces: and therefore (by Cor. 1, Prop. X, and Cor. 1, and 8, Prop. IV) they will cause those bodies to describe ellipses as before, but with a swifter motion.",
          "dipende_da": [
            "Prop. X, Cor. 1",
            "Prop. IV, Cor. 1",
            "Prop. IV, Cor. 8"
          ],
          "figura": {
            "mostra": [
              "DT, DL sommate alle attrazioni reciproche di T e L"
            ],
            "evidenzia": [
              "forze ancora proporzionali a DT, DL: ellissi più veloci"
            ]
          }
        },
        {
          "id": "L1-P64-p6",
          "la": "",
          "it": "Le restanti forze acceleratrici SD e SD, con le azioni motrici SD × T e SD × L, che stanno come i corpi, attraendo quei corpi in egual misura e lungo le linee TI, LK parallele a DS, non mutano affatto le loro posizioni reciproche, ma fanno sì che essi si avvicinino in egual misura alla linea IK, che si immagini condotta per il centro del corpo S e perpendicolare alla linea DS.",
          "en": "The remaining accelerative forces SD and DL, by the motive forces SD × T and SD × L, which are as the bodies attracting those bodies equally and in the direction of the lines TI, LK parallel to DS, do not at all change their situations with respect to one another, but cause them equally to approach to the line IK; which must be imagined drawn through the middle of the body S, and perpendicular to the line DS.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "forze motrici SD × T, SD × L",
              "linee TI, LK ∥ DS",
              "retta IK ⊥ DS per S"
            ],
            "evidenzia": [
              "forze uguali e parallele: posizioni reciproche invariate"
            ]
          },
          "nota": "Motte scrive «SD and DL» per «SD & SD»: errore (apparato A.9)."
        },
        {
          "id": "L1-P64-p7",
          "la": "",
          "it": "Questo avvicinamento alla linea IK sarà però impedito facendo sì che il sistema dei corpi T e L da una parte e il corpo S dall’altra, con le velocità opportune, girino attorno al centro comune di gravità C.",
          "en": "But that approach to the line IK will be hindered by causing the system of the bodies T and L on one side, and the body S on the other, with proper velocities, to revolve round the common centre of gravity C.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "C su SD"
            ],
            "evidenzia": [
              "rotazione di S e del sistema T+L attorno a C"
            ]
          }
        },
        {
          "id": "L1-P64-p8",
          "la": "",
          "it": "Con un tale moto il corpo S, poiché la somma delle forze motrici SD × T e SD × L, proporzionale alla distanza CS, tende verso il centro C, descrive un’ellisse attorno allo stesso C; e il punto D, poiché CS e CD sono proporzionali, descriverà dalla parte opposta un’ellisse simile.",
          "en": "With such a motion the body S, because the sum of the motive forces SD × T and SD × L is proportional to the distance CS, tends to the centre C, will describe an ellipsis round the same centre C; and the point D, because the lines CS and CD are proportional, will describe a like ellipsis over against it.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "ellisse di S attorno a C",
              "ellisse di D attorno a C"
            ],
            "evidenzia": [
              "CS : CD costante: ellissi simili, da parti opposte"
            ]
          }
        },
        {
          "id": "L1-P64-p9",
          "la": "",
          "it": "I corpi T e L, poi, attratti dalle forze motrici SD × T e SD × L, il primo dalla prima e il secondo dalla seconda, in egual misura e lungo le linee parallele TI e LK, come si è detto, continueranno (per i Cor. V e VI delle leggi) a descrivere le loro ellissi attorno al centro mobile D, come prima. C.V.T.",
          "en": "But the bodies T and L, attracted by the motive forces SD × T and SD × L, the first by the first, and the last by the last, equally and in the direction of the parallel lines TI and LK, as was said before, will (by Cor. 5 and 6, of the Laws of Motion) continue to describe their ellipses round the movable centre D, as before. Q.E.I.",
          "dipende_da": [
            "Leggi, Cor. V",
            "Leggi, Cor. VI"
          ],
          "figura": {
            "mostra": [
              "ellissi di T e L attorno a D mobile"
            ],
            "evidenzia": [
              "moto relativo di T e L non alterato"
            ]
          }
        },
        {
          "id": "L1-P64-p10",
          "la": "",
          "it": "Si aggiunga ora un quarto corpo V, e con un argomento simile si concluderà che questo e il punto C descrivono ellissi attorno al centro comune di gravità di tutti, B, mentre i moti dei corpi precedenti T, L e S attorno ai centri D e C restano gli stessi, ma accelerati.",
          "en": "Let there be added a fourth body V, and, by the like reasoning, it will be demonstrated that this body and the point C will describe ellipses about the common centre of gravity B; the motions of the bodies T, L, and S round the centres D and C remaining the same as before; but accelerated.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "V",
              "B"
            ],
            "evidenzia": [
              "V e C su ellissi attorno a B"
            ]
          }
        },
        {
          "id": "L1-P64-p11",
          "la": "",
          "it": "E con lo stesso metodo si potranno aggiungere più corpi. C.V.T.",
          "en": "And by the same method one may add yet more bodies at pleasure. Q.E.I.",
          "dipende_da": [],
          "figura": {
            "mostra": [],
            "evidenzia": []
          }
        },
        {
          "id": "L1-P64-p12",
          "la": "",
          "it": "Le cose stanno così anche se i corpi T e L si attraggono a vicenda con forze acceleratrici maggiori o minori di quelle con cui attraggono gli altri corpi in proporzione alle distanze.",
          "en": "This would be the case, though the bodies T and L attract each other mutually with accelerative forces either greater or less than those with which they attract the other bodies in proportion to their distance.",
          "dipende_da": [],
          "figura": {
            "mostra": [],
            "evidenzia": [
              "attrazione reciproca di T e L di intensità diversa"
            ]
          }
        },
        {
          "id": "L1-P64-p13",
          "la": "",
          "it": "Siano le attrazioni acceleratrici reciproche di tutti i corpi come le distanze moltiplicate per i corpi che attraggono: dalle cose precedenti si dedurrà facilmente che tutti i corpi descrivono, con tempi periodici uguali, ellissi diverse attorno al centro comune di gravità di tutti, B, in un piano immobile. C.V.T.",
          "en": "Let all the mutual accelerative attractions be to each other as the distances multiplied into the attracting bodies; and from what has gone before it will easily be concluded that all the bodies will describe different ellipses with equal periodical times about their common centre of gravity B, in an immovable plane. Q.E.I.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "tutte le ellissi attorno a B"
            ],
            "evidenzia": [
              "tempo periodico comune"
            ]
          },
          "nota": "La trascrizione ha «attractio <168> nes»: parola spezzata dal marcatore di pagina."
        }
      ]
    },
    {
      "id": "L1-P66",
      "tipo": "Propositio/Theorema",
      "titolo": "Prop. LXVI (Teor. XXVI) — tre corpi: la costruzione delle forze perturbatrici",
      "copertura": [
        "S11.35",
        "S11.36",
        "S11.37",
        "S11.38",
        "S11.39"
      ],
      "fonti": {
        "la": "",
        "en": "Motte 1846, pp. 202–204"
      },
      "enunciato": {
        "la": "",
        "it": "Se tre corpi, le cui forze decrescono in rapporto duplicato delle distanze, si attraggono a vicenda, e le attrazioni acceleratrici di due qualsiasi verso il terzo stanno fra loro inversamente come i quadrati delle distanze, e i minori ruotano attorno al massimo, dico che il più interno, con raggi condotti al più interno e massimo, descriverà attorno a esso aree più proporzionali ai tempi, e una figura più vicina alla forma di un’ellisse che ha il fuoco nel punto d’incontro dei raggi, se il corpo massimo è agitato da queste attrazioni, che se quel massimo o, non attratto dai minori, fosse in quiete, o, attratto molto meno o molto più, fosse agitato molto meno o molto più.",
        "en": "If three bodies whose forces decrease in a duplicate ratio of the distances attract each other mutually; and the accelerative attractions of any two towards the third be between themselves reciprocally as the squares of the distances; and the two least revolve about the greatest; I say, that the interior of the two revolving bodies will, by radii drawn to the innermost and greatest, describe round that body areas more proportional to the times, and a figure more approaching to that of an ellipsis having its focus in the point of concourse of the radii, if that great body be agitated by those attractions, than it would do if that great body were not attracted at all by the lesser, but remained at rest; or than it would if that great body were very much more or very much less attracted, or very much more or very much less agitated, by the attractions."
      },
      "figura_base": {
        "punti": [
          "T",
          "P",
          "S",
          "A",
          "B",
          "E",
          "K",
          "L",
          "M",
          "N"
        ],
        "vincoli": [
          "T corpo massimo e centrale; P sull’orbita interna PAB; S sull’orbita esterna ESE, nello stesso piano (Caso 1)",
          "A, B: punti dell’orbita di P in congiunzione e opposizione rispetto a S (dai corollari)",
          "K sulla retta SP con SK = distanza media di P e S",
          "L sulla retta SP con SL : SK = SK² : SP²",
          "M su ST con LM ∥ PT (triangoli SLM e SPT simili)",
          "N su ST con SN = attrazione acceleratrice di T verso S (non molto diversa da SK)",
          "MN = SM − SN: forza perturbatrice parallela a ST; LM: forza perturbatrice diretta da P a T"
        ],
        "nota": "Figure non disponibili: relazioni ricavate dalle lettere del testo. Controllo numerico della costruzione in N8."
      },
      "passi": [
        {
          "id": "L1-P66-p1",
          "la": "",
          "it": "Ciò risulta quasi evidente dalla dimostrazione del Cor. 2 della proposizione precedente; ma con un argomento più distinto e di portata più generale lo si prova così.",
          "en": "This appears plainly enough from the demonstration of the second Corollary of the foregoing Proposition; but it may be made out after this manner by a way of reasoning more distinct and more universally convincing.",
          "dipende_da": [
            "Prop. LXV, Cor. 2"
          ],
          "figura": {
            "mostra": [],
            "evidenzia": []
          }
        },
        {
          "id": "L1-P66-p2",
          "la": "",
          "it": "Caso 1. Ruotino i corpi minori P e S nello stesso piano attorno al massimo T: P descriva l’orbita interna PAB, e S l’orbita esterna ESE.",
          "en": "CASE 1. Let the lesser bodies P and S revolve in the same plane about the greatest body T, the body P describing the interior orbit PAB, and S the exterior orbit ESE.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "T",
              "orbita PAB con P",
              "orbita ESE con S"
            ],
            "evidenzia": [
              "stesso piano"
            ]
          },
          "nota": "La trascrizione ha «ex <171> teriorem»: parola spezzata dal marcatore di pagina."
        },
        {
          "id": "L1-P66-p3",
          "la": "",
          "it": "Sia SK la distanza media dei corpi P e S; e l’attrazione acceleratrice del corpo P verso S, a quella distanza media, sia rappresentata dalla stessa SK.",
          "en": "Let SK be the mean distance of the bodies P and S; and let the accelerative attraction of the body P towards S, at that mean distance, be expressed by that line SK.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "K su SP",
              "SK"
            ],
            "evidenzia": [
              "SK rappresenta l’attrazione alla distanza media"
            ]
          }
        },
        {
          "id": "L1-P66-p4",
          "la": "",
          "it": "Si prenda SL che stia a SK in rapporto duplicato di SK a SP: SL sarà l’attrazione acceleratrice del corpo P verso S a una distanza qualsiasi SP.",
          "en": "Make SL to SK as the square of SK to the square of SP, and SL will be the accelerative attraction of the body P towards S at any distance SP.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "L su SP",
              "SL"
            ],
            "evidenzia": [
              "SL = SK³/SP² (inverso del quadrato)"
            ]
          }
        },
        {
          "id": "L1-P66-p5",
          "la": "",
          "it": "Congiungi PT, e conduci a essa la parallela LM, che incontri ST in M: l’attrazione SL si scomporrà (per il Cor. II delle leggi) nelle attrazioni SM, LM.",
          "en": "Join PT, and draw LM parallel to it meeting ST in M; and the attraction SL will be resolved (by Cor. 2, of the Laws of Motion) into the attractions SM, LM.",
          "dipende_da": [
            "Leggi, Cor. II"
          ],
          "figura": {
            "mostra": [
              "PT",
              "LM ∥ PT",
              "M su ST"
            ],
            "evidenzia": [
              "SL = SM + LM",
              "triangoli SLM ~ SPT"
            ]
          }
        },
        {
          "id": "L1-P66-p6",
          "la": "",
          "it": "E così il corpo P sarà sollecitato da una triplice forza acceleratrice.",
          "en": "And so the body P will be urged with a threefold accelerative force.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "tre forze su P"
            ],
            "evidenzia": []
          }
        },
        {
          "id": "L1-P66-p7",
          "la": "",
          "it": "Una forza tende a T e nasce dall’attrazione reciproca dei corpi T e P.",
          "en": "One of these forces tends towards T, and arises from the mutual attraction of the bodies T and P.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "forza 1: attrazione di T su P"
            ],
            "evidenzia": [
              "diretta da P a T"
            ]
          }
        },
        {
          "id": "L1-P66-p8",
          "la": "",
          "it": "Per effetto di questa sola forza il corpo P dovrebbe descrivere attorno al corpo T, sia esso immobile o agitato da questa attrazione, sia aree proporzionali ai tempi con il raggio PT, sia un’ellisse che ha il fuoco nel centro del corpo T.",
          "en": "By this force alone the body P would describe round the body T, by the radius PT, areas proportional to the times, and an ellipsis whose focus is in the centre of the body T; and this it would do whether the body T remained unmoved, or whether it were agitated by that attraction.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "ellisse kepleriana di fuoco T"
            ],
            "evidenzia": [
              "aree proporzionali ai tempi"
            ]
          }
        },
        {
          "id": "L1-P66-p9",
          "la": "",
          "it": "Ciò risulta dalla Prop. XI e dai Cor. 2 e 3 del Teor. XXI.",
          "en": "This appears from Prop. XI, and Cor. 2 and 3 of Theor. XXI.",
          "dipende_da": [
            "Prop. XI",
            "Teor. XXI, Cor. 2",
            "Teor. XXI, Cor. 3"
          ],
          "figura": {
            "mostra": [],
            "evidenzia": []
          }
        },
        {
          "id": "L1-P66-p10",
          "la": "",
          "it": "La seconda forza è quella dell’attrazione LM, che, poiché tende da P a T, sovrapposta alla prima forza coinciderà con essa, e così farà sì che le aree siano descritte ancora proporzionali ai tempi, per il Cor. 3 del Teor. XXI.",
          "en": "The other force is that of the attraction LM, which, because it tends from P to T, will be superadded to and coincide with the former force; and cause the areas to be still proportional to the times, by Cor. 3, Theor. XXI.",
          "dipende_da": [
            "Teor. XXI, Cor. 3"
          ],
          "figura": {
            "mostra": [
              "forza 2: LM lungo PT"
            ],
            "evidenzia": [
              "LM radiale: aree ancora proporzionali ai tempi"
            ]
          }
        },
        {
          "id": "L1-P66-p11",
          "la": "",
          "it": "Ma poiché non è inversamente proporzionale al quadrato della distanza PT, essa comporrà con la prima forza una forza che si scosta da questa proporzione, e tanto più quanto maggiore è il rapporto di questa forza alla prima, a parità di altre condizioni.",
          "en": "But because it is not reciprocally proportional to the square of the distance PT, it will compose, when added to the former, a force varying from that proportion; which variation will be the greater by how much the proportion of this force to the former is greater, cæteris paribus.",
          "dipende_da": [],
          "figura": {
            "mostra": [],
            "evidenzia": [
              "forza radiale totale non più ∝ 1/PT²"
            ]
          }
        },
        {
          "id": "L1-P66-p12",
          "la": "",
          "it": "Perciò, poiché (per la Prop. XI e per il Cor. 2 del Teor. XXI) la forza con cui l’ellisse è descritta attorno al fuoco T deve tendere a quel fuoco ed essere inversamente proporzionale al quadrato della distanza PT, quella forza composta, scostandosi da questa proporzione, farà sì che l’orbita PAB si scosti dalla forma di un’ellisse che ha il fuoco in T; e tanto più quanto maggiore è lo scostamento da questa proporzione, e quindi anche quanto maggiore è il rapporto della seconda forza LM alla prima, a parità di altre condizioni.",
          "en": "Therefore, since by Prop. XI, and by Cor. 2, Theor. XXI, the force with which the ellipsis is described about the focus T ought to be directed to that focus, and to be reciprocally proportional to the square of the distance PT, that compounded force varying from that proportion will make the orbit PAB vary from the figure of an ellipsis that has its focus in the point T; and so much the more by how much the variation from that proportion is greater; and by consequence by how much the proportion of the second force LM to the first force is greater, cæteris paribus.",
          "dipende_da": [
            "Prop. XI",
            "Teor. XXI, Cor. 2"
          ],
          "figura": {
            "mostra": [
              "orbita PAB deformata rispetto all’ellisse"
            ],
            "evidenzia": [
              "deformazione crescente con LM"
            ]
          }
        },
        {
          "id": "L1-P66-p13",
          "la": "",
          "it": "Ora la terza forza SM, attraendo il corpo P lungo una linea parallela a ST, comporrà con le forze precedenti una forza che non è più diretta da P verso T, e che da questa direzione si scosta tanto più quanto maggiore è il rapporto di questa terza forza alle forze precedenti, a parità di altre condizioni; e che perciò farà sì che il corpo P, con il raggio TP, descriva aree non più proporzionali ai tempi, e che lo scostamento da questa proporzionalità sia tanto maggiore quanto maggiore è il rapporto di questa terza forza alle altre.",
          "en": "But now the third force SM, attracting the body P in a direction parallel to ST, composes with the other forces a new force which is no longer directed from P to T; and which varies so much more from this direction by how much the proportion of this third force to the other forces is greater, cæteris paribus; and therefore causes the body P to describe, by the radius TP, areas no longer proportional to the times; and therefore makes the variation from that proportionality so much greater by how much the proportion of this force to the others is greater.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "forza 3: SM ∥ ST"
            ],
            "evidenzia": [
              "risultante non più diretta verso T: aree non più proporzionali ai tempi"
            ]
          }
        },
        {
          "id": "L1-P66-p14",
          "la": "",
          "it": "Questa terza forza, poi, accrescerà lo scostamento dell’orbita PAB dalla suddetta forma ellittica per una duplice ragione: sia perché non è diretta da P verso T, sia perché non è inversamente proporzionale al quadrato della distanza PT.",
          "en": "But this third force will increase the variation of the orbit PAB from the elliptical figure before-mentioned upon two accounts; first because that force is not directed from P to T; and, secondly, because it is not reciprocally proportional to the square of the distance PT.",
          "dipende_da": [],
          "figura": {
            "mostra": [],
            "evidenzia": [
              "duplice causa di scostamento"
            ]
          }
        },
        {
          "id": "L1-P66-p15",
          "la": "",
          "it": "Comprese queste cose, è manifesto che le aree sono massimamente proporzionali ai tempi quando la terza forza, restando invariate le altre, è minima; e che l’orbita PAB si avvicina massimamente alla suddetta forma ellittica quando sia la seconda sia la terza forza, ma soprattutto la terza, sono minime, restando invariata la prima.",
          "en": "These things being premised, it is manifest that the areas are then most nearly proportional to the times, when that third force is the least possible, the rest preserving their former quantity; and that the orbit PAB does then approach nearest to the elliptical figure above-mentioned, when both the second and third, but especially the third force, is the least possible; the first force remaining in its former quantity.",
          "dipende_da": [],
          "figura": {
            "mostra": [],
            "evidenzia": [
              "condizione: SM minima (aree); LM e SM minime (forma ellittica)"
            ]
          }
        },
        {
          "id": "L1-P66-p16",
          "la": "",
          "it": "Si rappresenti con la linea SN l’attrazione acceleratrice del corpo T verso S. Se le attrazioni acceleratrici SM, SN fossero uguali, esse, attraendo i corpi T e P in egual misura e lungo linee parallele, non muterebbero affatto la loro posizione reciproca.",
          "en": "Let the accelerative attraction of the body T towards S be expressed by the line SN; then if the accelerative attractions SM and SN were equal, these, attracting the bodies T and P equally and in parallel directions would not at all change their situation with respect to each other.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "N su ST",
              "SN: attrazione di T verso S"
            ],
            "evidenzia": [
              "SM = SN: forze uguali e parallele su T e P"
            ]
          }
        },
        {
          "id": "L1-P66-p17",
          "la": "",
          "it": "I moti di quei corpi fra loro sarebbero allora gli stessi (per il Cor. VI delle leggi) che se queste attrazioni fossero tolte.",
          "en": "The motions of the bodies between themselves would be the same in that case as if those attractions did not act at all, by Cor. 6, of the Laws of Motion.",
          "dipende_da": [
            "Leggi, Cor. VI"
          ],
          "figura": {
            "mostra": [],
            "evidenzia": [
              "moto relativo indifferente a SM = SN"
            ]
          }
        },
        {
          "id": "L1-P66-p18",
          "la": "",
          "it": "E, per la stessa ragione, se l’attrazione SN fosse minore dell’attrazione SM, toglierebbe dall’attrazione SM la parte SN, e resterebbe la sola parte MN, dalla quale sarebbero perturbate la proporzionalità dei tempi e delle aree e quella forma ellittica dell’orbita.",
          "en": "And, by a like reasoning, if the attraction SN is less than the attraction SM, it will take away out of the attraction SM the part SN, so that there will remain only the part (of the attraction) MN to disturb the proportionality of the areas and times, and the elliptical figure of the orbit.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "MN"
            ],
            "evidenzia": [
              "SN < SM: resta MN"
            ]
          }
        },
        {
          "id": "L1-P66-p19",
          "la": "",
          "it": "E similmente, se l’attrazione SN fosse maggiore dell’attrazione SM, dalla sola differenza MN nascerebbe la perturbazione della proporzionalità e dell’orbita.",
          "en": "And in like manner if the attraction SN be greater than the attraction SM, the perturbation of the orbit and proportion will be produced by the difference MN alone.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "MN"
            ],
            "evidenzia": [
              "SN > SM: agisce la differenza MN"
            ]
          }
        },
        {
          "id": "L1-P66-p20",
          "la": "",
          "it": "Così, per mezzo dell’attrazione SN, la terza attrazione suddetta, SM, si riduce sempre all’attrazione MN, mentre la prima e la seconda attrazione restano del tutto immutate; e perciò le aree e i tempi si avvicinano massimamente alla proporzionalità, e l’orbita PAB alla suddetta forma ellittica, quando l’attrazione MN o è nulla o è la minima possibile; cioè quando le attrazioni acceleratrici dei corpi P e T, dirette verso il corpo S, si avvicinano quanto più è possibile all’uguaglianza; cioè quando l’attrazione SN non è nulla, né minore della minima di tutte le attrazioni SM, ma è quasi media fra la massima e la minima di tutte le attrazioni SM, cioè non molto maggiore né molto minore dell’attrazione SK. C.V.D.",
          "en": "After this manner the attraction SN reduces always the attraction SM to the attraction MN, the first and second attractions remaining perfectly unchanged; and therefore the areas and times come then nearest to proportionality, and the orbit PAB to the above-mentioned elliptical figure, when the attraction MN is either none, or the least that is possible; that is, when the accelerative attractions of the bodies P and T approach as near as possible to equality; that is, when the attraction SN is neither none at all, nor less than the least of all the attractions SM, but is, as it were, a mean between the greatest and least of all those attractions SM, that is, not much greater nor much less than the attraction SK. Q.E.D.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "SN variabile",
              "MN risultante"
            ],
            "evidenzia": [
              "perturbazione minima per SN ≈ SK (T «agitato» come P)"
            ]
          },
          "nota": "La trascrizione ha «præ <173> fatam»: parola spezzata dal marcatore di pagina. Nella pagina interattiva si può far variare SN da 0 a oltre SK e mostrare MN."
        },
        {
          "id": "L1-P66-p21",
          "la": "",
          "it": "Caso 2. Ruotino ora i corpi minori P, S attorno al massimo T in piani diversi. La forza LM, agendo lungo la linea PT, situata nel piano dell’orbita PAB, avrà lo stesso effetto di prima, e non sposterà il corpo P dal piano della sua orbita.",
          "en": "CASE 2. Let now the lesser bodies P, S, revolve about a greater T in different planes; and the force LM, acting in the direction of the line PT situate in the plane of the orbit PAB, will have the same effect as before; neither will it draw the body P from the plane of its orbit.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "piani diversi delle orbite PAB ed ESE",
              "linea dei nodi"
            ],
            "evidenzia": [
              "LM nel piano di PAB"
            ]
          }
        },
        {
          "id": "L1-P66-p22",
          "la": "",
          "it": "Ma l’altra forza, NM, agendo lungo una linea parallela a ST (e quindi inclinata sul piano dell’orbita PAB quando il corpo S si trova fuori della linea dei nodi), oltre alla perturbazione del moto in longitudine già esposta, introdurrà una perturbazione del moto in latitudine, traendo il corpo P fuori del piano della sua orbita.",
          "en": "But the other force NM acting in the direction of a line parallel to ST (and which, therefore, when the body S is without the line of the nodes is inclined to the plane of the orbit PAB), besides the perturbation of the motion just now spoken of as to longitude, introduces another perturbation also as to latitude, attracting the body P out of the plane of its orbit.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "NM ∥ ST, inclinata sul piano di PAB"
            ],
            "evidenzia": [
              "perturbazione in latitudine (nulla se S è sulla linea dei nodi)"
            ]
          }
        },
        {
          "id": "L1-P66-p23",
          "la": "",
          "it": "E questa perturbazione, in una qualsiasi posizione reciproca data dei corpi P e T, sarà come la forza MN che la genera, e perciò diverrà minima quando MN è minima, cioè (come ho già esposto) quando l’attrazione SN non è molto maggiore né molto minore dell’attrazione SK. C.V.D.",
          "en": "And this perturbation, in any given situation of the bodies P and T to each other, will be as the generating force MN; and therefore becomes least when the force MN is least, that is (as was just now shewn), where the attraction SN is not much greater nor much less than the attraction SK. Q.E.D.",
          "dipende_da": [],
          "figura": {
            "mostra": [],
            "evidenzia": [
              "perturbazione in latitudine ∝ MN, minima per SN ≈ SK"
            ]
          }
        }
      ]
    },
    {
      "id": "L1-P67",
      "tipo": "Propositio/Theorema",
      "titolo": "Prop. LXVII (Teor. XXVII) — il corpo esterno attorno al centro comune O",
      "copertura": [
        "S11.62",
        "S11.63"
      ],
      "fonti": {
        "la": "",
        "en": "Motte 1846, p. 215"
      },
      "enunciato": {
        "la": "",
        "it": "Poste le stesse leggi delle attrazioni, dico che il corpo esterno S, attorno al centro comune di gravità O dei corpi interni P, T, con raggi condotti a quel centro, descrive aree più proporzionali ai tempi, e un’orbita più vicina alla forma di un’ellisse che ha il fuoco nello stesso centro, di quanto possa descriverne attorno al corpo più interno e massimo T con raggi condotti a esso.",
        "en": "The same laws of attraction being supposed, I say, that the exterior body S does, by radii drawn to the point O, the common centre of gravity of the interior bodies P and T, describe round that centre areas more proportional to the times, and an orbit more approaching to the form of an ellipsis having its focus in that centre, than it can describe round the innermost and greatest body T by radii drawn to that body."
      },
      "figura_base": {
        "punti": [
          "T",
          "P",
          "O",
          "S"
        ],
        "vincoli": [
          "O centro comune di gravità di T e P, sul segmento TP",
          "S esterno, lontano rispetto a TP"
        ],
        "nota": "Figura non disponibile."
      },
      "passi": [
        {
          "id": "L1-P67-p1",
          "la": "",
          "it": "Le attrazioni del corpo S verso T e verso P compongono infatti la sua attrazione assoluta, che è diretta verso il centro comune di gravità O dei corpi T e P più che verso il corpo massimo T, e che è inversamente proporzionale al quadrato della distanza SO più che al quadrato della distanza ST: come risulterà facilmente a chi consideri la cosa con attenzione.",
          "en": "For the attractions of the body S towards T and P compose its absolute attraction, which is more directed towards O, the common centre of gravity of the bodies T and P, than it is to the greatest body T; and which is more in a reciprocal proportion to the square of the distance SO, than it is to the square of the distance ST; as will easily appear by a little consideration.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "attrazioni di S verso T e verso P",
              "risultante",
              "O"
            ],
            "evidenzia": [
              "risultante quasi diretta verso O",
              "intensità quasi ∝ 1/SO²"
            ]
          },
          "nota": "La trascrizione inserisce [FIG 130] fra «versus» e «T & P». Verifica numerica in N18."
        }
      ]
    },
    {
      "id": "L1-P68",
      "tipo": "Propositio/Theorema",
      "titolo": "Prop. LXVIII (Teor. XXVIII) — il corpo esterno quando il corpo massimo è agitato",
      "copertura": [
        "S11.64",
        "S11.65"
      ],
      "fonti": {
        "la": "",
        "en": "Motte 1846, pp. 215–216"
      },
      "enunciato": {
        "la": "",
        "it": "Poste le stesse leggi delle attrazioni, dico che il corpo esterno S, attorno al centro comune di gravità O dei corpi interni P e T, con raggi condotti a quel centro, descrive aree più proporzionali ai tempi, e un’orbita più vicina alla forma di un’ellisse che ha il fuoco nello stesso centro, se il corpo più interno e massimo è agitato da queste attrazioni come gli altri, che se esso o, non attratto, fosse in quiete, o, attratto molto più o molto meno, fosse agitato molto più o molto meno.",
        "en": "The same laws of attraction supposed, I say, that the exterior body S will, by radii drawn to O, the common centre of gravity of the interior bodies P and T, describe round that centre areas more proportional to the times, and an orbit more approaching to the form of an ellipsis having its focus in that centre, if the innermost and greatest body be agitated by these attractions as well as the rest, than it would do if that body were either at rest as not attracted, or were much more or much less attracted, or much more or much less agitated."
      },
      "figura_base": {
        "punti": [
          "T",
          "P",
          "O",
          "S"
        ],
        "vincoli": [
          "O centro comune di gravità di T e P",
          "centro comune dei tre corpi in quiete nel caso ideale"
        ],
        "nota": "Figura non disponibile."
      },
      "passi": [
        {
          "id": "L1-P68-p1",
          "la": "",
          "it": "Si dimostra quasi nello stesso modo della Prop. LXVI, ma con un argomento più lungo, che perciò tralascio.",
          "en": "This may be demonstrated after the same manner as Prop. LXVI, but by a more prolix reasoning, which I therefore pass over.",
          "dipende_da": [
            "Prop. LXVI"
          ],
          "figura": {
            "mostra": [],
            "evidenzia": []
          }
        },
        {
          "id": "L1-P68-p2",
          "la": "",
          "it": "Basterà valutare la cosa così.",
          "en": "It will be sufficient to consider it after this manner.",
          "dipende_da": [],
          "figura": {
            "mostra": [],
            "evidenzia": []
          }
        },
        {
          "id": "L1-P68-p3",
          "la": "",
          "it": "Dalla dimostrazione dell’ultima proposizione risulta che il centro verso cui il corpo S è sollecitato dalle forze congiunte è vicinissimo al centro comune di gravità di quei due corpi.",
          "en": "From the demonstration of the last Proposition it is plain, that the centre, towards which the body S is urged by the two forces conjunctly, is very near to the common centre of gravity of those two other bodies.",
          "dipende_da": [
            "Prop. LXVII"
          ],
          "figura": {
            "mostra": [
              "centro verso cui è sollecitato S",
              "O"
            ],
            "evidenzia": [
              "i due centri quasi coincidono"
            ]
          },
          "nota": "«propositionis novissimæ» è la Prop. LXVII, citata senza numero. La trascrizione ha il marcatore <186> dopo «in quod»."
        },
        {
          "id": "L1-P68-p4",
          "la": "",
          "it": "Se questo centro coincidesse con quel centro comune, e il centro comune di gravità dei tre corpi fosse in quiete, il corpo S da una parte e il centro comune degli altri due dall’altra descriverebbero ellissi esatte attorno al centro comune di tutti, in quiete.",
          "en": "If this centre were to coincide with that common centre, and moreover the common centre of gravity of all the three bodies were at rest, the body S on one side, and the common centre of gravity of the other two bodies on the other side, would describe true ellipses about that quiescent common centre.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "S e O su ellissi attorno al centro comune dei tre"
            ],
            "evidenzia": [
              "caso ideale: ellissi esatte"
            ]
          },
          "nota": "«quisceret» è un refuso probabile della trascrizione per «quiesceret». La trascrizione inserisce [FIG 131] dopo «ex altera parte,»."
        },
        {
          "id": "L1-P68-p5",
          "la": "",
          "it": "Ciò risulta dal Cor. 2 della Prop. LVIII confrontato con quanto è stato dimostrato nelle Prop. LXIV e LXV.",
          "en": "This appears from Cor. 2, Prop. LVIII, compared with what was demonstrated in Prop. LXIV, and LXV.",
          "dipende_da": [
            "Prop. LVIII, Cor. 2",
            "Prop. LXIV",
            "Prop. LXV"
          ],
          "figura": {
            "mostra": [],
            "evidenzia": []
          }
        },
        {
          "id": "L1-P68-p6",
          "la": "",
          "it": "Questo moto ellittico è perturbato un poco dalla distanza del centro dei due corpi dal centro verso cui il terzo, S, è attratto.",
          "en": "Now this accurate elliptical motion will be disturbed a little by the distance of the centre of the two bodies from the centre towards which the third body S is attracted.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "distanza fra O e il centro di attrazione di S"
            ],
            "evidenzia": [
              "prima causa di perturbazione"
            ]
          }
        },
        {
          "id": "L1-P68-p7",
          "la": "",
          "it": "Si dia inoltre un moto al centro comune dei tre, e la perturbazione aumenterà.",
          "en": "Let there be added, moreover, a motion to the common centre of the three, and the perturbation will be increased yet more.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "centro comune dei tre in moto"
            ],
            "evidenzia": [
              "seconda causa di perturbazione"
            ]
          },
          "nota": "Motte aggiunge «yet more»."
        },
        {
          "id": "L1-P68-p8",
          "la": "",
          "it": "Perciò la perturbazione è minima quando il centro comune dei tre è in quiete, cioè quando il corpo più interno e massimo T è attratto secondo la legge degli altri; ed è sempre maggiore quando quel centro comune dei tre, per la diminuzione del moto del corpo T, comincia a muoversi, e poi è agitato sempre di più.",
          "en": "Therefore the perturbation is least when the common centre of the three bodies is at rest; that is, when the innermost and greatest body T is attracted according to the same law as the rest are; and is always greatest when the common centre of the three, by the diminution of the motion of the body T, begins to be moved, and is more and more agitated.",
          "dipende_da": [],
          "figura": {
            "mostra": [
              "confronto: T attratto come gli altri / T fermo"
            ],
            "evidenzia": [
              "perturbazione minima con il centro dei tre in quiete"
            ]
          },
          "nota": "Verifica numerica in N18: con T libero le aree di S attorno a O variano di 2·10⁻⁴, con T fermo di 2 (valori relativi)."
        }
      ]
    }
  ]
}
```

**Fine del Fascicolo 10.**
